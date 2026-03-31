#!/usr/bin/env python3
"""
Agent Prime — First Run

A guided entry point that helps first-time users choose between:
  - preview: open the workspace MVP / hosted preview
  - quick-trial: load the startup-founder example and generate the dashboard
  - onboard: guide the user through @onboarder, then finish verification
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import textwrap
import webbrowser
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HOSTED_PREVIEW_URL = "https://avyayalaya.github.io/agent-prime/workspace-mvp/"
LOCAL_PREVIEW_PATH = ROOT / "workspace-mvp" / "index.html"

EXAMPLE_FILES = {
    ROOT / "examples" / "startup-founder" / "context.md": ROOT / "shared" / "context.md",
    ROOT / "examples" / "startup-founder" / "registry.json": ROOT / "shared" / "registry.json",
    ROOT / "examples" / "startup-founder" / "dispatch.md": ROOT / "prime" / "dispatch.md",
    ROOT / "examples" / "startup-founder" / "config.json": ROOT / "prime" / "config.json",
}


def banner() -> None:
    print()
    print("Agent Prime — First Run")
    print("=" * 40)
    print("Choose how you want to start:")
    print("  1) Preview the product shell")
    print("  2) Load a quick trial example")
    print("  3) Run guided onboarding")
    print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Guided first-run entry point for Agent Prime."
    )
    parser.add_argument(
        "--mode",
        choices=("preview", "quick-trial", "onboard"),
        help="Start directly in one mode instead of showing the menu.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Auto-confirm prompts where possible.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not try to open a browser window for preview mode.",
    )
    parser.add_argument(
        "--skip-dashboard",
        action="store_true",
        help="Skip dashboard generation when a mode normally generates it.",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help="Skip setup verification and integrity checks.",
    )
    return parser.parse_args()


def require_python() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required.")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def looks_like_blank_context(path: Path) -> bool:
    content = read_text(path)
    markers = (
        "AGENT_PRIME_TEMPLATE: CONTEXT",
        "This file starts intentionally neutral.",
        "<!-- Add your name -->",
    )
    return any(marker in content for marker in markers)


def registry_has_items(path: Path) -> bool:
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    return bool(data.get("items", []))


def config_has_goals(path: Path) -> bool:
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    return bool(data.get("goals", {}))


def dispatch_has_tasks(path: Path) -> bool:
    content = read_text(path)
    return bool(re.search(r"^## Q-\d+:", content, flags=re.MULTILINE))


def repo_is_configured() -> bool:
    return any(
        (
            not looks_like_blank_context(ROOT / "shared" / "context.md"),
            registry_has_items(ROOT / "shared" / "registry.json"),
            config_has_goals(ROOT / "prime" / "config.json"),
            dispatch_has_tasks(ROOT / "prime" / "dispatch.md"),
        )
    )


def ask_yes_no(prompt: str, default: bool = False, auto_yes: bool = False) -> bool:
    if auto_yes:
        print(f"{prompt} yes")
        return True

    suffix = "[Y/n]" if default else "[y/N]"
    answer = input(f"{prompt} {suffix} ").strip().lower()
    if not answer:
        return default
    return answer in {"y", "yes"}


def choose_mode(explicit_mode: str | None) -> str:
    if explicit_mode:
        return explicit_mode

    banner()
    while True:
        choice = input("Select a mode (1-3): ").strip()
        mapping = {"1": "preview", "2": "quick-trial", "3": "onboard"}
        if choice in mapping:
            return mapping[choice]
        print("Please enter 1, 2, or 3.")


def run_python_script(relative_path: str) -> int:
    script_path = ROOT / relative_path
    command = [sys.executable, str(script_path)]
    result = subprocess.run(command, cwd=ROOT, check=False)
    return result.returncode


def backup_targets(paths: list[Path]) -> Path | None:
    configured_targets = [path for path in paths if path.exists()]
    if not configured_targets:
        return None

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = ROOT / ".agent-prime-backups" / timestamp
    for path in configured_targets:
        relative = path.relative_to(ROOT)
        backup_path = backup_root / relative
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup_path)
    return backup_root


def finish_setup(skip_dashboard: bool, skip_verify: bool) -> int:
    exit_code = 0

    if not skip_dashboard:
        print()
        print("Generating dashboard and project index...")
        dashboard_rc = run_python_script("meta/scripts/generate_dashboard.py")
        exit_code = max(exit_code, dashboard_rc)

    if not skip_verify:
        print()
        print("Running setup verification...")
        verify_rc = run_python_script("meta/scripts/verify_setup.py")
        print()
        print("Running integrity check...")
        integrity_rc = run_python_script("meta/scripts/integrity_check.py")
        exit_code = max(exit_code, verify_rc, integrity_rc)

    return exit_code


def normalize_quick_trial_registry() -> None:
    registry_path = ROOT / "shared" / "registry.json"
    if not registry_path.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    future_due = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    data = json.loads(registry_path.read_text(encoding="utf-8"))

    for item in data.get("items", []):
        item["created"] = today
        item["updated"] = today
        if item.get("due"):
            item["due"] = future_due

    meta = data.setdefault("meta", {})
    meta["last_updated"] = today
    registry_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def preview_mode(no_browser: bool) -> int:
    print()
    print("Preview mode")
    print("-" * 12)
    print(f"Hosted preview: {HOSTED_PREVIEW_URL}")
    print(f"Local preview:  {LOCAL_PREVIEW_PATH}")
    print()
    print("What you can see there:")
    print("  - guided onboarding")
    print("  - starter workflows")
    print("  - run state + artifact review")
    print("  - rule capture + export/reset")

    if no_browser:
        return 0

    if LOCAL_PREVIEW_PATH.exists():
        webbrowser.open(LOCAL_PREVIEW_PATH.resolve().as_uri())
    else:
        webbrowser.open(HOSTED_PREVIEW_URL)

    return 0


def quick_trial_mode(auto_yes: bool, skip_dashboard: bool, skip_verify: bool) -> int:
    print()
    print("Quick trial mode")
    print("-" * 16)
    print("This will load the startup-founder example into your working files.")

    targets = list(EXAMPLE_FILES.values())
    backup_root = None

    if repo_is_configured():
        confirm = ask_yes_no(
            "This repo already looks configured. Overwrite working files with the quick-trial example?",
            default=False,
            auto_yes=auto_yes,
        )
        if not confirm:
            print("Cancelled.")
            return 1
        backup_root = backup_targets(targets)
    elif ask_yes_no(
        "Proceed with the quick-trial example?",
        default=True,
        auto_yes=auto_yes,
    ):
        backup_root = None
    else:
        print("Cancelled.")
        return 1

    for source, destination in EXAMPLE_FILES.items():
        if not source.exists():
            raise SystemExit(f"Missing example file: {source}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    normalize_quick_trial_registry()

    if backup_root:
        print(f"Backup created at: {backup_root}")

    exit_code = finish_setup(skip_dashboard=skip_dashboard, skip_verify=skip_verify)

    print()
    print("Quick trial is ready.")
    print("Next steps:")
    print("  1) Open prime/dashboard.md")
    print("  2) Ask: @prime Show me the system pulse")
    print("  3) Explore the startup-founder example, then rerun onboarding when you want your own system")
    return exit_code


def onboard_mode(auto_yes: bool, skip_dashboard: bool, skip_verify: bool) -> int:
    print()
    print("Onboarding mode")
    print("-" * 15)

    if repo_is_configured():
        print("This repo already has user configuration.")
        if not ask_yes_no(
            "Use the current files and finish setup from here?",
            default=True,
            auto_yes=auto_yes,
        ):
            print("Okay. Re-run this command when you're ready.")
            return 1
        return finish_setup(skip_dashboard=skip_dashboard, skip_verify=skip_verify)

    print(
        textwrap.dedent(
            """
            Next:
              1) Open this repo in Claude Code or VS Code with Copilot Chat
              2) Run: @onboarder
              3) Answer the setup questions
              4) Return here when onboarding has finished
            """
        ).strip()
    )

    if auto_yes:
        print()
        print("Auto-confirm mode enabled. Run @onboarder, then re-run this command to finish setup.")
        return 0

    answer = input("Press Enter after @onboarder finishes, or type skip to stop now: ").strip().lower()
    if answer == "skip":
        print("Okay. Re-run this command after onboarding.")
        return 0

    return finish_setup(skip_dashboard=skip_dashboard, skip_verify=skip_verify)


def main() -> int:
    require_python()
    args = parse_args()
    mode = choose_mode(args.mode)

    if mode == "preview":
        return preview_mode(no_browser=args.no_browser)
    if mode == "quick-trial":
        return quick_trial_mode(
            auto_yes=args.yes,
            skip_dashboard=args.skip_dashboard,
            skip_verify=args.skip_verify,
        )
    if mode == "onboard":
        return onboard_mode(
            auto_yes=args.yes,
            skip_dashboard=args.skip_dashboard,
            skip_verify=args.skip_verify,
        )

    raise SystemExit(f"Unsupported mode: {mode}")


if __name__ == "__main__":
    raise SystemExit(main())
