#!/usr/bin/env python3
"""
Agent Prime — Dispatcher

Reads prime/dispatch.md, finds unblocked `auto` tasks, assembles context
from agent prompts + input files, calls LLM API (GitHub Models GPT-4o primary,
LM Studio fallback), writes output, marks tasks done, appends successor tasks.

Usage:
  python meta/scripts/dispatcher.py              # process all auto tasks
  python meta/scripts/dispatcher.py --dry-run    # preview without calling LLM
  python meta/scripts/dispatcher.py --task Q-006 # run one specific task (any type)
  python meta/scripts/dispatcher.py --limit 3    # cap at 3 tasks
  python meta/scripts/dispatcher.py --fallback   # force LM Studio local model
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent.parent
CONFIG_PATH = SCRIPT_DIR.parent / "config" / "dispatcher_config.json"
DISPATCH_PATH = ROOT / "prime" / "dispatch.md"
REGISTRY_PATH = ROOT / "shared" / "registry.json"
LEARNINGS_PATH = ROOT / "shared" / "learnings.md"
CONTEXT_PATH = ROOT / "shared" / "context.md"
LOG_DIR = ROOT / "meta" / "logs" / "dispatcher"
ENV_PATH = ROOT / ".env"


# ── Env + Config ──────────────────────────────────────────────────────────────

def load_env():
    """Load .env into os.environ (no external dependency needed)."""
    if not ENV_PATH.exists():
        return
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


# ── LLM Client ────────────────────────────────────────────────────────────────

def get_client(config, force_fallback=False):
    """
    Return (client, default_model, source_label).

    Primary: LM Studio (local, no limits, 131K context).
    Fallback: GitHub Models (cloud, 16K token cap) — used when LM Studio is offline
              or --fallback flag is passed.
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: openai package not installed. Run: pip install openai")
        sys.exit(1)

    if not force_fallback:
        # Try LM Studio first
        primary = config["apis"]["primary"]
        base_url = os.environ.get("LMSTUDIO_BASE_URL", primary["base_url"])
        model    = os.environ.get("LMSTUDIO_MODEL",    config["models"]["quality"])
        try:
            import urllib.request
            urllib.request.urlopen(base_url.replace("/v1", "/v1/models"), timeout=2)
            client = OpenAI(base_url=base_url, api_key="lm-studio")
            return client, model, "lmstudio"
        except Exception:
            print("[dispatcher] LM Studio not reachable — falling back to GitHub Models")

    # Fallback: GitHub Models
    if not os.environ.get("GITHUB_TOKEN"):
        print("ERROR: LM Studio offline and GITHUB_TOKEN not set. Cannot proceed.")
        sys.exit(1)
    fallback = config["apis"]["fallback"]
    cloud_model = config["models"].get("fallback_cloud", "gpt-4o")
    client = OpenAI(base_url=fallback["base_url"], api_key=os.environ["GITHUB_TOKEN"])
    return client, cloud_model, "github_models"


def resolve_model(config, agent_name, client_source):
    """Return the model to use for this agent + client combination."""
    if client_source == "github_models":
        return config["models"].get("fallback_cloud", "gpt-4o")
    # LM Studio: single model handles all tiers (131K context, no limits)
    return os.environ.get("LMSTUDIO_MODEL", config["models"]["quality"])


# ── Dispatch Parsing ──────────────────────────────────────────────────────────

def parse_dispatch_queue(dispatch_path):
    """Parse the Active Queue section of dispatch.md. Returns list of task dicts."""
    if not dispatch_path.exists():
        print(f"ERROR: dispatch.md not found at {dispatch_path}")
        return []

    text = dispatch_path.read_text(encoding="utf-8")
    tasks = []
    in_active = False

    for line in text.splitlines():
        stripped = line.strip()
        if "## Active Queue" in stripped:
            in_active = True
            continue
        if stripped.startswith("## ") and "Active Queue" not in stripped:
            in_active = False
            continue
        if not in_active or not stripped.startswith("| Q-"):
            continue

        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if len(cells) < 8:
            continue

        task_text = cells[2]
        is_done = "~~" in task_text

        tasks.append({
            "q_id":          cells[0].strip(),
            "agent":         re.sub(r"\*\*|\[.*?\]\(.*?\)", "", cells[1]).strip(),
            "task":          re.sub(r"~~", "", task_text).strip(),
            "decision_type": cells[3].replace("`", "").strip(),
            "priority":      cells[4].strip(),
            "input_files":   cells[5].strip(),
            "triggered_by":  cells[6].strip() if len(cells) > 6 else "",
            "blocked_on":    cells[7].strip() if len(cells) > 7 else "",
            "added":         cells[8].strip() if len(cells) > 8 else "",
            "is_done":       is_done,
            "raw_line":      stripped,
        })

    return tasks


def find_runnable_tasks(tasks, target_q_id=None):
    """
    Return tasks eligible to run:
    - If target_q_id given: that specific task regardless of type.
    - Otherwise: auto + unblocked + not done.
    """
    runnable = []
    for t in tasks:
        if t["is_done"]:
            continue
        if target_q_id:
            if t["q_id"] == target_q_id:
                runnable.append(t)
            continue
        if t["decision_type"] != "auto":
            continue
        # "—" or empty = not blocked
        blocked = t["blocked_on"].replace("—", "").replace("\u2014", "").strip()
        if blocked:
            continue
        runnable.append(t)
    return runnable


# ── Context Assembly ──────────────────────────────────────────────────────────

def load_file_safe(path, max_chars=None):
    """Read a file; return a placeholder string if missing."""
    p = Path(path)
    if not p.exists():
        return f"[FILE NOT FOUND: {path}]"
    text = p.read_text(encoding="utf-8", errors="replace")
    if max_chars:
        text = text[:max_chars]
    return text


def parse_input_file_paths(input_files_str):
    """
    Parse the input_files column from dispatch.md into a list of relative paths.
    Handles backtick-quoted paths and comma-separated plain paths.
    """
    if not input_files_str or input_files_str in ("—", "\u2014", ""):
        return []
    quoted = re.findall(r"`([^`]+)`", input_files_str)
    if quoted:
        return quoted
    parts = [p.strip() for p in input_files_str.split(",")]
    return [re.sub(r"\(.*?\)", "", p).strip() for p in parts
            if p and p not in ("—", "\u2014")]


def assemble_context(task, config):
    """
    Build (system_message, user_message) for the LLM.

    System: agent prompt + learnings (hard constraints) + user context
    User:   automated mode note + core context files + task input files + output format

    Token budget (GitHub Models free tier = ~16K tokens / ~60K chars):
      system: agent prompt(8K) + learnings(4K) + context(3K) ≈ 15K
      user:   core files(2K×4=8K) + input files(5K×n) + task/instructions(2K) ≈ 20K+
    """
    agent_name = task["agent"].lower()

    # System message
    agent_prompt = load_file_safe(ROOT / "agents" / agent_name / "prompt.md", max_chars=15000)
    learnings    = load_file_safe(LEARNINGS_PATH, max_chars=10000)
    context      = load_file_safe(CONTEXT_PATH,   max_chars=8000)

    system_msg = (
        f"# AGENT PROMPT\n\n{agent_prompt}\n\n"
        f"---\n\n# ACCUMULATED LEARNINGS (hard constraints)\n\n{learnings}\n\n"
        f"---\n\n# USER CONTEXT\n\n{context}"
    )

    # User message
    user_parts = [
        "**AUTOMATED DISPATCHER MODE:** All required context files are loaded below. "
        "Your Context Verification Gate is satisfied — do NOT stop to request files. "
        "Proceed directly to your task output.\n\n---\n\n",
        f"## Task\n\n**{task['q_id']}** — {task['task']}\n",
        f"**Triggered by:** {task['triggered_by']}\n\n---\n\n## Core Context Files\n",
    ]

    # Core context files (satisfies Context Verification Gates)
    for rel_path in config["dispatcher"].get("core_context_files", []):
        content = load_file_safe(ROOT / rel_path, max_chars=10000)
        user_parts.append(f"\n### `{rel_path}`\n\n{content}")

    user_parts.append("\n\n---\n\n## Task-Specific Input Files\n")

    for rel_path in parse_input_file_paths(task["input_files"]):
        content = load_file_safe(ROOT / rel_path, max_chars=15000)
        user_parts.append(f"\n### `{rel_path}`\n\n{content}")

    if not parse_input_file_paths(task["input_files"]):
        user_parts.append("_(no input files specified)_")

    user_parts.append("""

---

## Output Instructions

Produce your full output. Apply all learnings and voice rules before writing.

At the very end, include a `## Successor Tasks` block listing the next logical
agent task(s) per the Successor Rules in dispatch.md. Use this exact format:

```json
[
  {
    "agent": "<AgentName>",
    "task": "<task description>",
    "decision_type": "<auto|approve|review|input>",
    "priority": "<P0|P1|P2>",
    "input_files": "<relative paths or —>",
    "triggered_by": "<what caused this>"
  }
]
```

If no successor is needed, write:

## Successor Tasks
```json
[]
```
""")

    user_msg = "".join(user_parts)
    return system_msg, user_msg


# ── LLM Call ─────────────────────────────────────────────────────────────────

def call_llm(client, model, system_msg, user_msg, dry_run=False):
    """Call the LLM and return the response text."""
    if dry_run:
        return f"[DRY RUN — would call {model} with {len(system_msg) + len(user_msg):,} chars]\n\n## Successor Tasks\n```json\n[]\n```"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user",   "content": user_msg},
        ],
        max_tokens=4096,
        temperature=0.3,
    )
    return response.choices[0].message.content


# ── Output + Dispatch Updates ─────────────────────────────────────────────────

def write_output(task, output_text, config):
    """Write LLM output to the correct agent folder. Returns Path."""
    agent_name = task["agent"].lower()
    agent_cfg  = config["agent_config"].get(agent_name, {})
    output_dir = ROOT / agent_cfg.get("output_dir", f"agents/{agent_name}")
    output_dir.mkdir(parents=True, exist_ok=True)

    today    = datetime.now().strftime("%Y-%m-%d")
    suffix   = agent_cfg.get("output_suffix", "output.md")
    q_slug   = task["q_id"].replace("-", "").lower()
    filename = f"{q_slug}_{agent_name}_{today}_{suffix}"

    header = (
        f"# {task['q_id']} — {task['task']}\n\n"
        f"> **Agent:** {task['agent']}  \n"
        f"> **Generated:** {today} (auto-dispatched)  \n\n"
        f"---\n\n"
    )
    out_path = output_dir / filename
    out_path.write_text(header + output_text, encoding="utf-8")
    return out_path


def extract_successor_tasks(output_text):
    """Parse the ## Successor Tasks JSON block from LLM output."""
    match = re.search(
        r"##\s*Successor Tasks\s*\n+```json\s*\n(.*?)\n```",
        output_text,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return []
    try:
        tasks = json.loads(match.group(1).strip())
        return tasks if isinstance(tasks, list) else []
    except json.JSONDecodeError:
        return []


def _next_q_id(text):
    """Find highest Q-NNN in text and return next one."""
    ids = re.findall(r"Q-(\d+)", text)
    return f"Q-{max((int(i) for i in ids), default=18) + 1:03d}"


def append_successor_tasks(successors, completed_q_id, dispatch_path):
    """Append successor tasks to the Active Queue in dispatch.md."""
    if not successors:
        return

    text  = dispatch_path.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    new_rows = []

    for s in successors:
        q_id    = _next_q_id(text)
        agent   = s.get("agent", "Prime")
        task    = s.get("task", "")
        dtype   = s.get("decision_type", "approve")
        prio    = s.get("priority", "P2")
        inputs  = s.get("input_files", "—")
        trigger = s.get("triggered_by", f"{completed_q_id} completion")

        row = f"| {q_id} | **{agent}** | {task} | `{dtype}` | {prio} | {inputs} | {trigger} | — | {today} |"
        new_rows.append(row)
        text += f"\n{row}"  # keep text current so _next_q_id increments correctly

    insertion = "\n".join(new_rows) + "\n"

    # Insert before the Successor Rules divider
    marker = "## Successor Rules"
    if f"\n---\n\n{marker}" in text:
        text = text.replace(f"\n---\n\n{marker}", f"\n{insertion}\n---\n\n{marker}")
    else:
        text += "\n" + insertion

    dispatch_path.write_text(text, encoding="utf-8")
    print(f"  → Appended {len(new_rows)} successor task(s)")


def mark_task_done(task, output_path, dispatch_path):
    """
    In dispatch.md:
    1. Strikethrough the task description in the Active Queue row.
    2. Append a row to the Done Log.
    """
    text  = dispatch_path.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    q_id  = re.escape(task["q_id"])

    # Strikethrough task cell in the Active Queue row
    def strikethrough(match):
        line  = match.group(0)
        cells = line.split("|")
        if len(cells) > 3 and "~~" not in cells[3]:
            cells[3] = f" ~~{cells[3].strip()}~~ "
        return "|".join(cells)

    text = re.sub(
        rf"^\| {q_id} \|.*$",
        strikethrough,
        text,
        flags=re.MULTILINE,
    )

    # Append to Done Log table
    done_marker = "## Done Log"
    if done_marker in text:
        done_row = (
            f"| {task['q_id']} | {task['agent']} | {task['task'][:60]} "
            f"| {today} | Auto-dispatched → `{output_path.name}` |"
        )
        sep_idx = text.find("|---|", text.find(done_marker))
        if sep_idx != -1:
            next_nl = text.find("\n", sep_idx) + 1
            text = text[:next_nl] + done_row + "\n" + text[next_nl:]

    dispatch_path.write_text(text, encoding="utf-8")


# ── Logging ───────────────────────────────────────────────────────────────────

def log_run(results, log_dir):
    """Append a run summary to meta/logs/dispatcher/<date>.md."""
    log_dir.mkdir(parents=True, exist_ok=True)
    today    = datetime.now().strftime("%Y-%m-%d")
    now      = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = log_dir / f"dispatch_run_{today}.md"

    lines = [f"\n## Run — {now}\n"]
    for r in results:
        icon = "✅" if r["success"] else "❌"
        lines.append(f"\n### {icon} {r['q_id']} — {r['agent']}: {r['task'][:60]}")
        if r.get("output_path"):
            lines.append(f"- Output: `{Path(r['output_path']).relative_to(ROOT)}`")
        if r.get("successors"):
            lines.append(f"- Successors appended: {len(r['successors'])}")
        if r.get("error"):
            lines.append(f"- Error: {r['error']}")

    entry = "\n".join(lines) + "\n"
    if log_path.exists():
        log_path.write_text(log_path.read_text(encoding="utf-8") + "\n---" + entry, encoding="utf-8")
    else:
        log_path.write_text(f"# Dispatcher Log — {today}\n" + entry, encoding="utf-8")
    return log_path


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Agent Prime Dispatcher")
    parser.add_argument("--dry-run",  action="store_true", help="Preview without calling LLM")
    parser.add_argument("--task",     metavar="Q-NNN",      help="Run a specific task by ID")
    parser.add_argument("--limit",    type=int,             help="Max tasks to process")
    parser.add_argument("--fallback", action="store_true",  help="Force LM Studio local model")
    args = parser.parse_args()

    load_env()
    config = load_config()
    client, _, client_source = get_client(config, force_fallback=args.fallback)
    limit = args.limit or config["dispatcher"].get("max_tasks_per_run", 5)

    print(f"[dispatcher] API: {client_source}")
    if args.dry_run:
        print("[dispatcher] DRY RUN — no LLM calls, no writes")

    all_tasks = parse_dispatch_queue(DISPATCH_PATH)
    runnable  = find_runnable_tasks(all_tasks, target_q_id=args.task)

    if not runnable:
        print("[dispatcher] No runnable tasks found.")
        if not args.task:
            print("  Tip: only `auto` + unblocked + not-done tasks run automatically.")
        return

    print(f"[dispatcher] {len(runnable)} runnable task(s) — processing up to {limit}.\n")

    results = []
    for task in runnable[:limit]:
        print(f"→ {task['q_id']}: [{task['agent']}] {task['task'][:70]}")
        model  = resolve_model(config, task["agent"], client_source)
        result = {
            "q_id": task["q_id"], "agent": task["agent"],
            "task": task["task"], "success": False,
        }

        try:
            system_msg, user_msg = assemble_context(task, config)
            ctx_size = len(system_msg) + len(user_msg)
            print(f"  context: {ctx_size:,} chars | model: {model}")

            output_text = call_llm(client, model, system_msg, user_msg, dry_run=args.dry_run)

            if not args.dry_run:
                out_path   = write_output(task, output_text, config)
                successors = extract_successor_tasks(output_text)
                print(f"  output:  {out_path.relative_to(ROOT)}")

                append_successor_tasks(successors, task["q_id"], DISPATCH_PATH)
                mark_task_done(task, out_path, DISPATCH_PATH)

                result.update(output_path=str(out_path), successors=successors)
            else:
                print(f"  [DRY RUN] Would write output and mark done")

            result["success"] = True

        except Exception as e:
            print(f"  ERROR: {e}")
            result["error"] = str(e)

        results.append(result)
        print()

    if not args.dry_run and results:
        log_path = log_run(results, LOG_DIR)
        print(f"[dispatcher] Log: {log_path.relative_to(ROOT)}")

    succeeded = sum(1 for r in results if r["success"])
    print(f"[dispatcher] Done: {succeeded}/{len(results)} succeeded.")


if __name__ == "__main__":
    main()
