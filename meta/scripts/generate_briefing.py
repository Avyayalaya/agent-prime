#!/usr/bin/env python3
"""
Agent Prime — Session Briefing Generator

Reads shared/registry.json and prime/dispatch.md to generate:
  prime/briefing.md — auto-generated session briefing with priorities,
                      dispatch queue status, owner-owed items, and
                      recommended session plan.

Run: python meta/scripts/generate_briefing.py
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Resolve paths relative to Agent Prime root
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent.parent
REGISTRY_PATH = ROOT / "shared" / "registry.json"
DISPATCH_PATH = ROOT / "prime" / "dispatch.md"
BRIEFING_PATH = ROOT / "prime" / "briefing.md"
QUICK_LOG_PATH = ROOT / "prime" / "quick_log.md"
GOAL_LEDGER_PATH = ROOT / "prime" / "goal_ledger.md"
PROOF_STACK_PATH = ROOT / "prime" / "proof_stack.json"
LEARNINGS_PATH = ROOT / "shared" / "learnings.md"


def apply_quick_log(registry):
    """
    Reads prime/quick_log.md for pending entries, applies them to registry items,
    moves applied entries to the Archive section, and rewrites the file.

    Supported entry types:
        DONE: {ID} | {note} | {date}
        SUPERSEDED: {ID} | {note} | {date}
        IN_PROGRESS: {ID} | {note} | {date}

    Returns list of (entry_line, registry_change_summary) for reporting.
    """
    if not QUICK_LOG_PATH.exists():
        return []

    text = QUICK_LOG_PATH.read_text(encoding="utf-8")
    items_by_id = {item["id"]: item for item in registry["items"]}

    # Find the Pending section
    pending_start = text.find("## Pending")
    archive_start = text.find("## Archive")
    if pending_start == -1:
        return []

    pending_block_end = archive_start if archive_start != -1 else len(text)
    pending_block = text[pending_start:pending_block_end]

    applied = []
    today = datetime.now().strftime("%Y-%m-%d")

    entry_pattern = re.compile(
        r"^(DONE|SUPERSEDED|IN_PROGRESS):\s*([^\|]+)\|([^\|]+)\|([^\n]+)",
        re.MULTILINE | re.IGNORECASE,
    )

    for match in entry_pattern.finditer(pending_block):
        action = match.group(1).strip().upper()
        id_or_title = match.group(2).strip()
        note = match.group(3).strip()
        entry_date = match.group(4).strip()
        raw_line = match.group(0).strip()

        # Try to find matching item — exact ID first, then title substring
        item = items_by_id.get(id_or_title)
        if not item:
            for reg_item in registry["items"]:
                if id_or_title.lower() in reg_item.get("title", "").lower():
                    item = reg_item
                    break

        if not item:
            print(f"  [quick_log] WARNING: no registry match for '{id_or_title}' — skipping")
            continue

        old_status = item["status"]
        if action == "DONE":
            item["status"] = "done"
            item["completed"] = entry_date or today
            item["next_action"] = None
        elif action == "SUPERSEDED":
            item["status"] = "done"
            item["completed"] = entry_date or today
            item["notes"] = (item.get("notes") or "") + f" | Superseded: {note}"
            item["next_action"] = None
        elif action == "IN_PROGRESS":
            item["status"] = "in_progress"

        item["updated"] = today
        change_summary = f"status {old_status}→{item['status']}, updated {today}"
        applied.append((raw_line, item["id"], change_summary))
        print(f"  [quick_log] Applied: {item['id']} — {change_summary}")

    if not applied:
        return []

    # Save updated registry
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    # Rewrite quick_log: remove applied entries from Pending, add to Archive
    # Remove matched lines from pending block
    new_pending_block = pending_block
    for raw_line, _, _ in applied:
        new_pending_block = new_pending_block.replace(raw_line, "")

    # Build archive rows
    archive_rows = "\n".join(
        f"| {raw_line} | {today} | {change} |"
        for raw_line, _, change in applied
    )

    # Reconstruct file
    header = text[:pending_start]
    archive_section = text[archive_start:] if archive_start != -1 else "## Archive (applied entries — last 30 days)\n\n| Entry | Applied On | Registry Change |\n|-------|-----------|-----------------|"

    new_text = header + new_pending_block.rstrip() + "\n\n---\n\n" + archive_section.rstrip()
    # Insert new archive rows just after the archive table header
    table_header_end = new_text.find("| Entry | Applied On | Registry Change |")
    if table_header_end != -1:
        separator_end = new_text.find("\n", new_text.find("|-------|", table_header_end)) + 1
        new_text = new_text[:separator_end] + archive_rows + "\n" + new_text[separator_end:]

    QUICK_LOG_PATH.write_text(new_text, encoding="utf-8")
    return applied


def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def days_since(date_str):
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.now() - d).days
    except ValueError:
        return None


def is_overdue(item):
    """Overdue means due date is strictly before today (not same day)."""
    if not item.get("due"):
        return False
    try:
        due = datetime.strptime(item["due"], "%Y-%m-%d").date()
        return datetime.now().date() > due and item["status"] not in ("done", "published", "parked")
    except ValueError:
        return False


def is_due_today(item):
    if not item.get("due"):
        return False
    return item["due"] == datetime.now().strftime("%Y-%m-%d")


def parse_dispatch_queue(dispatch_path):
    """Parse dispatch.md to extract active queue items and done log."""
    if not dispatch_path.exists():
        return [], []

    text = dispatch_path.read_text(encoding="utf-8")

    active_items = []
    done_items = []

    # Find Active Queue table
    in_active = False
    in_done = False
    for line in text.split("\n"):
        line = line.strip()
        if "## Active Queue" in line:
            in_active = True
            in_done = False
            continue
        if "## Done Log" in line:
            in_active = False
            in_done = True
            continue
        if line.startswith("## ") and "Active Queue" not in line and "Done Log" not in line:
            in_active = False
            in_done = False
            continue

        if not line.startswith("| Q-"):
            continue

        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 8:
            continue

        q_id = cells[0]
        agent = cells[1].replace("**", "")
        task = cells[2]
        decision_type = cells[3].replace("`", "")
        priority = cells[4]
        blocked_on = cells[7] if len(cells) > 7 else ""

        entry = {
            "q_id": q_id,
            "agent": agent,
            "task": task,
            "decision_type": decision_type,
            "priority": priority,
            "blocked_on": blocked_on,
            "is_done": "~~" in task,
        }

        if in_active:
            active_items.append(entry)
        elif in_done:
            done_items.append(entry)

    return active_items, done_items


def generate_briefing(registry, dispatch_active, dispatch_done, proof_changes=None, new_ledger_events=None, unpropagated=None):
    items = registry["items"]
    today = datetime.now().strftime("%Y-%m-%d")
    priority_order = {"P0": 0, "P1": 1, "P2": 2}

    # Categorize items
    active_items = [i for i in items if i["status"] in ("in_progress", "planning", "review", "blocked", "backlog")]
    p0_items = [i for i in active_items if i.get("priority") == "P0"]
    p1_items = [i for i in active_items if i.get("priority") == "P1"]

    # Due today
    due_today = [i for i in items if is_due_today(i) and i["status"] not in ("done", "published", "parked")]

    # Overdue
    overdue = [i for i in items if is_overdue(i)]

    # Owner-owed
    owner_tasks = [i for i in active_items if i.get("owner") == "owner" and i["type"] == "TSK"]
    owner_overdue = [t for t in owner_tasks if is_overdue(t)]

    # Stale (not updated in 7+ days)
    stale_items = []
    for i in items:
        if i["status"] in ("done", "published", "parked"):
            continue
        d = days_since(i.get("updated"))
        if d and d >= 7:
            stale_items.append((i, d))
    stale_items.sort(key=lambda x: -x[1])

    # Blocked items
    blocked = [i for i in items if i.get("blocked_on") and i["status"] not in ("done", "published", "parked")]

    # Dispatch queue analysis
    q_actionable = [q for q in dispatch_active if not q["is_done"] and not q["blocked_on"].strip().startswith("Q-") and q["blocked_on"].strip() != ""]
    q_auto = [q for q in dispatch_active if not q["is_done"] and q["decision_type"] == "auto" and (not q["blocked_on"] or q["blocked_on"].strip() == "" or q["blocked_on"].strip() == "\u2014")]
    q_approve = [q for q in dispatch_active if not q["is_done"] and q["decision_type"] == "approve" and (not q["blocked_on"] or q["blocked_on"].strip() == "" or q["blocked_on"].strip() == "\u2014")]
    q_review = [q for q in dispatch_active if not q["is_done"] and q["decision_type"] == "review" and (not q["blocked_on"] or q["blocked_on"].strip() == "" or q["blocked_on"].strip() == "\u2014")]
    q_input = [q for q in dispatch_active if not q["is_done"] and q["decision_type"] == "input" and (not q["blocked_on"] or q["blocked_on"].strip() == "" or q["blocked_on"].strip() == "\u2014")]
    q_blocked = [q for q in dispatch_active if not q["is_done"] and q["blocked_on"] and q["blocked_on"].strip() not in ("", "\u2014")]

    # Build briefing
    lines = []
    lines.append("# Session Briefing")
    lines.append("")
    lines.append(f"> **Date:** {today}")
    lines.append("> **Auto-generated** from `shared/registry.json` + `prime/dispatch.md`.")
    lines.append("> **Run:** `python meta/scripts/generate_briefing.py`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. Pulse
    lines.append("## Pulse")
    lines.append("")
    if due_today:
        for item in due_today:
            lines.append(f"**DUE TODAY:** [{item['id']}] {item['title']}")
    if overdue:
        for item in overdue:
            lines.append(f"**OVERDUE:** [{item['id']}] {item['title']} (due {item['due']})")
    lines.append(f"**Active items:** {len(active_items)} ({len(p0_items)} P0, {len(p1_items)} P1)")
    lines.append(f"**Owner owes:** {len(owner_tasks)} task(s) ({len(owner_overdue)} overdue)")
    lines.append(f"**Stale:** {len(stale_items)} item(s) not updated in 7+ days")
    lines.append("")

    # Proof stack changes (from goal ledger auto-compute)
    if proof_changes:
        lines.append("### Proof Stack Changes")
        lines.append("")
        for c in proof_changes:
            lines.append(f"- **{c['dimension']}:** {c['old']} → {c['computed']} ({c['note']})")
        lines.append("")

    if unpropagated:
        lines.append(f"### Unpropagated Learnings ({len(unpropagated)})")
        lines.append("")
        lines.append("These learnings need to be pushed to their target files:")
        lines.append("")
        for u in unpropagated:
            lines.append(f"- **{u['learning']}** → `{u['target']}`")
        lines.append("")

    if new_ledger_events:
        lines.append("### New Events to Add to Goal Ledger")
        lines.append("")
        for e in new_ledger_events:
            lines.append(f"- [{e['id']}] {e['title']} (completed {e['completed']})")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 2. Today's Priorities
    lines.append("## Today's Priorities")
    lines.append("")
    if p0_items:
        lines.append("### P0 (Do Now)")
        lines.append("")
        for item in sorted(p0_items, key=lambda x: x.get("due") or "9999"):
            due_str = f" (due {item['due']})" if item.get("due") else ""
            blocked_str = f" **BLOCKED:** {item['blocked_on']}" if item.get("blocked_on") else ""
            status_icon = {"in_progress": "IN PROGRESS", "backlog": "READY", "planning": "PLANNING", "review": "NEEDS REVIEW", "blocked": "BLOCKED"}.get(item["status"], item["status"])
            lines.append(f"- [{item['id']}] **{item['title']}** [{status_icon}]{due_str}{blocked_str}")
            if item.get("next_action"):
                lines.append(f"  Next: {item['next_action']}")
        lines.append("")

    if p1_items:
        lines.append("### P1 (This Week)")
        lines.append("")
        for item in sorted(p1_items, key=lambda x: (x.get("due") or "9999", x["id"])):
            due_str = f" (due {item['due']})" if item.get("due") else ""
            overdue_flag = " **OVERDUE**" if is_overdue(item) else ""
            blocked_str = f" BLOCKED: {item['blocked_on']}" if item.get("blocked_on") else ""
            lines.append(f"- [{item['id']}] {item['title']}{due_str}{overdue_flag}{blocked_str}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 3. Dispatch Queue Status
    lines.append("## Dispatch Queue")
    lines.append("")
    if q_auto:
        lines.append(f"**Ready to auto-run ({len(q_auto)}):**")
        for q in q_auto:
            lines.append(f"- {q['q_id']}: {q['agent']} — {q['task']}")
        lines.append("")
    if q_approve:
        lines.append(f"**Need your approval ({len(q_approve)}):**")
        for q in q_approve:
            lines.append(f"- {q['q_id']}: {q['agent']} — {q['task']}")
        lines.append("")
    if q_review:
        lines.append(f"**Need your review ({len(q_review)}):**")
        for q in q_review:
            lines.append(f"- {q['q_id']}: {q['agent']} — {q['task']}")
        lines.append("")
    if q_input:
        lines.append(f"**Need your input ({len(q_input)}):**")
        for q in q_input:
            lines.append(f"- {q['q_id']}: {q['agent']} — {q['task']}")
        lines.append("")
    if q_blocked:
        lines.append(f"**Blocked ({len(q_blocked)}):**")
        for q in q_blocked:
            lines.append(f"- {q['q_id']}: {q['agent']} — {q['task']} (on: {q['blocked_on']})")
        lines.append("")

    if not (q_auto or q_approve or q_review or q_input or q_blocked):
        lines.append("Dispatch queue is empty.")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 4. Owner's Plate
    if owner_tasks:
        lines.append("## Owner's Plate")
        lines.append("")
        lines.append("| ID | Task | Priority | Due | Overdue? |")
        lines.append("|----|------|----------|-----|----------|")
        for t in sorted(owner_tasks, key=lambda x: (priority_order.get(x.get("priority", "P2"), 2), x.get("due") or "9999")):
            due = t.get("due") or "\u2014"
            overdue_str = "YES" if is_overdue(t) else "\u2014"
            lines.append(f"| {t['id']} | {t['title']} | {t.get('priority', '\u2014')} | {due} | {overdue_str} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 5. Staleness Report
    if stale_items:
        lines.append("## Stale Items")
        lines.append("")
        for item, d in stale_items:
            flag = "CRITICAL" if d >= 14 else "WARNING"
            lines.append(f"- [{item['id']}] {item['title']} — **{d} days** since update [{flag}]")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 6. Recommended Session Plan
    lines.append("## Recommended Session Plan")
    lines.append("")
    step = 1

    # Due today items first
    for item in due_today:
        lines.append(f"{step}. **[{item['id']}] {item['title']}** — due today")
        step += 1

    # Auto-run dispatch items (TSK-022: auto-chain these immediately)
    if q_auto:
        lines.append(f"{step}. **AUTO-CHAIN: Run {len(q_auto)} auto task(s)** — no approval needed, execute now:")
        for q in q_auto:
            lines.append(f"   - {q['q_id']}: {q['agent']} — {q['task']}")
        step += 1

    # Unpropagated learnings
    if unpropagated:
        lines.append(f"{step}. **Propagate {len(unpropagated)} unpushed learning(s)** to target files")
        step += 1

    # Owner overdue tasks
    for t in owner_overdue:
        if t not in due_today:
            lines.append(f"{step}. **[{t['id']}] {t['title']}** — overdue (due {t.get('due', 'no date')})")
            step += 1

    # P0 items not yet mentioned
    for item in p0_items:
        if item not in due_today and not is_overdue(item):
            lines.append(f"{step}. **[{item['id']}] {item['title']}** — P0")
            step += 1

    # Stale items need attention
    if stale_items:
        lines.append(f"{step}. **Address {len(stale_items)} stale items** — update status or park")
        step += 1

    # Regenerate dashboard at end
    lines.append(f"{step}. **Regenerate dashboard** — `python meta/scripts/generate_dashboard.py`")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Auto-generated from registry.json + dispatch.md on {today}*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Goal Ledger → Proof Stack Auto-Compute
# ---------------------------------------------------------------------------

# Maps proof_stack dimension IDs to the event columns that count as evidence.
# "validated" statuses mean the event actually happened (not just invited/drafted).
VALIDATED_STATUSES = {"delivered", "published", "active", "received", "in progress"}

DIMENSION_EVENT_MAPPING = {
    "vision": ["Publication", "Speaking"],
    "industry_influence": ["Publication", "Speaking", "Recognition", "Advisory"],
    "org_building": ["Speaking", "Teaching", "Advisory", "Tools"],
    "scale_execution": ["Recognition", "Publication"],
    "cross_domain": ["Publication", "Speaking"],
    "business_acumen": ["Advisory", "Publication", "Investment Research"],
}


def parse_goal_ledger():
    """
    Parse goal_ledger.md tables to extract events with their proof dimensions
    and validation status. Returns list of dicts:
      {type, date, title, status, dimensions: [str], source}
    """
    if not GOAL_LEDGER_PATH.exists():
        return []

    text = GOAL_LEDGER_PATH.read_text(encoding="utf-8")
    events = []

    # Determine which section heading maps to which event type
    section_type_map = {
        "Recruiter Inbound": "Recruiter",
        "Speaking Invitations": "Speaking",
        "Advisory / Board": "Advisory",
        "Recognition": "Recognition",
        "Publications": "Publication",
        "Teaching / Mentorship": "Teaching",
        "Tools / Open Source": "Tools",
        "Investment Research": "Investment Research",
    }

    current_type = None
    in_table = False
    headers = []

    for line in text.split("\n"):
        stripped = line.strip()

        # Detect section heading (### level)
        if stripped.startswith("### "):
            heading = stripped[4:].strip()
            current_type = section_type_map.get(heading)
            in_table = False
            headers = []
            continue

        # Detect table header row
        if current_type and stripped.startswith("|") and not in_table:
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if cells and cells[0] in ("Date", ""):
                headers = [c.lower() for c in cells]
                in_table = True
                continue

        # Skip separator row
        if in_table and stripped.startswith("|") and set(stripped.replace("|", "").replace("-", "").strip()) <= {"", " "}:
            continue

        # Parse data rows
        if in_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) < len(headers):
                cells.extend([""] * (len(headers) - len(cells)))

            row = dict(zip(headers, cells))
            event = {
                "type": current_type,
                "date": row.get("date", ""),
                "status": row.get("status", row.get("outcome", "")),
                "source": row.get("source", ""),
                "dimensions": [],
            }

            # Extract proof dimensions
            dims_raw = row.get("proof dimensions", "")
            if dims_raw:
                event["dimensions"] = [d.strip() for d in dims_raw.split(",") if d.strip()]

            # Extract title — use first non-date, non-status descriptive column
            for key in ("event", "title", "what", "company", "project", "organization"):
                if key in row and row[key]:
                    event["title"] = row[key]
                    break
            else:
                event["title"] = current_type

            events.append(event)
        elif in_table and not stripped.startswith("|"):
            in_table = False

    return events


def compute_proof_scores(events):
    """
    Given parsed ledger events, compute a score per proof dimension.
    Returns dict: {dimension_id: {"count": int, "validated": int, "score": int}}
    """
    scores = {}
    for dim_id, event_types in DIMENSION_EVENT_MAPPING.items():
        matching = [e for e in events if e["type"] in event_types and dim_id in e.get("dimensions", [])]
        validated = [e for e in matching if e.get("status", "").lower() in VALIDATED_STATUSES]
        count = len(matching)
        val_count = len(validated)

        if count == 0:
            score = 1
        elif count <= 2 and val_count == 0:
            score = 3
        elif count <= 2 and val_count >= 1:
            score = 4
        elif count >= 3 and val_count < count:
            score = 5
        else:
            score = 7

        scores[dim_id] = {"count": count, "validated": val_count, "score": score}

    return scores


def update_proof_stack_and_detect_changes(computed_scores):
    """
    Read proof_stack.json, compare computed scores vs current scores.
    Update _computed field. Return list of changes for briefing.
    """
    if not PROOF_STACK_PATH.exists():
        return []

    with open(PROOF_STACK_PATH, "r", encoding="utf-8") as f:
        proof_stack = json.load(f)

    changes = []
    today = datetime.now().strftime("%Y-%m-%d")

    for dim in proof_stack.get("dimensions", []):
        dim_id = dim["id"]
        if dim_id not in computed_scores:
            continue

        old_score = dim.get("score", 0)
        computed = computed_scores[dim_id]
        new_score = computed["score"]

        # Always store the computed value for transparency
        dim["_computed"] = new_score

        # Respect manual override
        if dim.get("_override") is not None:
            if new_score > dim["_override"]:
                changes.append({
                    "dimension": dim["name"],
                    "dim_id": dim_id,
                    "old": dim["_override"],
                    "computed": new_score,
                    "note": f"Ledger ({computed['count']} events, {computed['validated']} validated) now exceeds override={dim['_override']}",
                    "count": computed["count"],
                    "validated": computed["validated"],
                })
            continue

        # Ledger can only push scores UP — career history scores are the floor.
        # Only flag a change when new evidence raises the dimension.
        if new_score > old_score:
            dim["score"] = new_score
            changes.append({
                "dimension": dim["name"],
                "dim_id": dim_id,
                "old": old_score,
                "computed": new_score,
                "note": f"Ledger: {computed['count']} events, {computed['validated']} validated → raised from {old_score}",
                "count": computed["count"],
                "validated": computed["validated"],
            })

    proof_stack["_last_computed"] = today

    with open(PROOF_STACK_PATH, "w", encoding="utf-8") as f:
        json.dump(proof_stack, f, indent=2, ensure_ascii=False)

    return changes


def append_ledger_change_log(changes):
    """Append rating changes to the Change Log table in goal_ledger.md."""
    if not changes or not GOAL_LEDGER_PATH.exists():
        return

    text = GOAL_LEDGER_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")

    new_rows = []
    for c in changes:
        new_rows.append(f"| {today} | {c['dim_id']} | {c['old']} | {c['computed']} | {c['note']} |")

    # Find the last row in the Change Log table (insert after it)
    marker = "| Date | Dimension | Old | New | Trigger |"
    marker_pos = text.find(marker)
    if marker_pos == -1:
        return

    # Find end of table (next blank line or section after the table)
    after_marker = text[marker_pos:]
    lines = after_marker.split("\n")
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("|"):
            insert_idx = i
        elif line.strip() == "" or line.strip().startswith("#") or line.strip().startswith("---"):
            break

    # Insert new rows after the last table row
    abs_line_start = text[:marker_pos].count("\n")
    all_lines = text.split("\n")
    insert_at = abs_line_start + insert_idx + 1
    for row in reversed(new_rows):
        all_lines.insert(insert_at, row)

    GOAL_LEDGER_PATH.write_text("\n".join(all_lines), encoding="utf-8")


def scan_unpropagated_learnings():
    """
    Scan shared/learnings.md Propagation Tracker for unpushed items (☐ marker).
    Returns list of dicts: {learning, targets, section}
    """
    if not LEARNINGS_PATH.exists():
        return []

    text = LEARNINGS_PATH.read_text(encoding="utf-8")
    unpropagated = []

    for line in text.split("\n"):
        stripped = line.strip()
        # Match tracker rows with ☐ (unchecked) marker — but skip deferred (⏸)
        if stripped.startswith("|") and "☐" in stripped and "⏸" not in stripped:
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 3:
                learning = cells[0]
                target = cells[1]
                unpropagated.append({
                    "learning": learning,
                    "target": target,
                })

    return unpropagated


def scan_registry_for_new_ledger_events(registry):
    """
    Scan registry for recently completed items with external visibility
    that aren't already in the goal ledger. Returns list of events to suggest.
    """
    if not GOAL_LEDGER_PATH.exists():
        return []

    ledger_text = GOAL_LEDGER_PATH.read_text(encoding="utf-8")
    suggestions = []

    for item in registry["items"]:
        if item["status"] not in ("done", "published"):
            continue
        if not item.get("completed"):
            continue

        # Check if this item ID is already referenced in the ledger
        if item["id"] in ledger_text:
            continue

        # Items that have external visibility potential
        item_type = item.get("type", "")
        title = item.get("title", "")

        # THS (thesis) completions = potential publications
        # EVT (event) completions = potential speaking/teaching
        # EXP (experiment) completions with public output = tools
        if item_type in ("THS", "EVT", "EXP", "PRG"):
            suggestions.append({
                "id": item["id"],
                "title": title,
                "type": item_type,
                "completed": item["completed"],
            })

    return suggestions


def main():
    if not REGISTRY_PATH.exists():
        print(f"Registry not found at {REGISTRY_PATH}")
        return

    registry = load_registry()
    print(f"Loaded registry: {len(registry['items'])} items")

    # Apply any out-of-session completions from quick_log.md FIRST
    applied = apply_quick_log(registry)
    if applied:
        print(f"Quick log: applied {len(applied)} update(s) to registry")
        # Reload registry after quick_log writes it
        registry = load_registry()
    else:
        print("Quick log: no pending entries")

    # Goal Ledger → Proof Stack auto-compute
    proof_changes = []
    new_events = []
    ledger_events = parse_goal_ledger()
    if ledger_events:
        computed_scores = compute_proof_scores(ledger_events)
        proof_changes = update_proof_stack_and_detect_changes(computed_scores)
        if proof_changes:
            append_ledger_change_log(proof_changes)
            print(f"Goal ledger: {len(proof_changes)} proof_stack rating change(s) detected")
            for c in proof_changes:
                print(f"  {c['dimension']}: {c['old']} → {c['computed']} ({c['note']})")
        else:
            print(f"Goal ledger: {len(ledger_events)} events, no rating changes")
    else:
        print("Goal ledger: not found or empty")

    # Check for unpropagated learnings (TSK-021)
    unpropagated_learnings = scan_unpropagated_learnings()
    if unpropagated_learnings:
        print(f"Learnings: {len(unpropagated_learnings)} unpropagated item(s) found")
        for u in unpropagated_learnings[:5]:  # Show first 5
            print(f"  {u['learning']} → {u['target']}")
    else:
        print("Learnings: all propagated (0 unpushed)")

    # Check for registry items that should be in the ledger
    new_events = scan_registry_for_new_ledger_events(registry)
    if new_events:
        print(f"Goal ledger: {len(new_events)} registry item(s) may need adding:")
        for e in new_events:
            print(f"  [{e['id']}] {e['title']} (completed {e['completed']})")

    dispatch_active, dispatch_done = parse_dispatch_queue(DISPATCH_PATH)
    print(f"Parsed dispatch: {len(dispatch_active)} active, {len(dispatch_done)} done")

    briefing = generate_briefing(registry, dispatch_active, dispatch_done,
                                  proof_changes=proof_changes if ledger_events else None,
                                  new_ledger_events=new_events if ledger_events else None,
                                  unpropagated=unpropagated_learnings)
    with open(BRIEFING_PATH, "w", encoding="utf-8") as f:
        f.write(briefing)
    print(f"Briefing written to {BRIEFING_PATH}")

    # Print summary to console
    items = registry["items"]
    today = datetime.now().strftime("%Y-%m-%d")
    active = [i for i in items if i["status"] not in ("done", "published", "parked")]
    p0 = [i for i in active if i.get("priority") == "P0"]
    due_today = [i for i in items if i.get("due") == today and i["status"] not in ("done", "published", "parked")]
    overdue = [i for i in items if is_overdue(i)]

    print("")
    print(f"Session Briefing [{today}]")
    if due_today:
        for item in due_today:
            print(f"  DUE TODAY: [{item['id']}] {item['title']}")
    if overdue:
        for item in overdue:
            print(f"  OVERDUE: [{item['id']}] {item['title']} (due {item['due']})")
    if p0:
        print(f"  Top P0: [{p0[0]['id']}] {p0[0]['title']}")
    print(f"  Active: {len(active)} items | Dispatch: {len(dispatch_active)} queued")


if __name__ == "__main__":
    main()
