#!/usr/bin/env python3
"""
Agent Prime — System Integrity Check

Reads shared/registry.json and meta/dependencies.json to verify:
  1. All artifact paths in registry exist on disk
  2. Staleness across all active items
  3. Orphaned items (no next_action, not done)
  4. Agent folder structure compliance
  5. Dependency chain freshness (if dependencies.json exists)

Run: python meta/scripts/integrity_check.py
"""

import json
import os
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent.parent
REGISTRY_PATH = ROOT / "shared" / "registry.json"
DEPS_PATH = ROOT / "meta" / "dependencies.json"

SEVERITY = {"critical": "🔴", "warning": "🟡", "info": "ℹ️"}


def load_json(path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def days_since(date_str):
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.now() - d).days
    except ValueError:
        return None


def check_artifact_paths(registry):
    """Check that all artifact paths in registry exist on disk."""
    issues = []
    for item in registry["items"]:
        for artifact in item.get("artifacts", []):
            path = ROOT / artifact["path"]
            if not path.exists():
                issues.append({
                    "severity": "critical",
                    "item_id": item["id"],
                    "message": f"Artifact not found: {artifact['path']}",
                    "fix": f"Update registry artifact path or restore the file"
                })
    return issues


def check_staleness(registry):
    """Flag items that haven't been updated recently."""
    issues = []
    for item in registry["items"]:
        if item["status"] in ("done", "published", "parked"):
            continue
        days = days_since(item.get("updated"))
        if days is not None and days >= 14:
            issues.append({
                "severity": "critical",
                "item_id": item["id"],
                "message": f"Not updated in {days} days (status: {item['status']})",
                "fix": "Update status or park the item"
            })
        elif days is not None and days >= 7:
            issues.append({
                "severity": "warning",
                "item_id": item["id"],
                "message": f"Not updated in {days} days (status: {item['status']})",
                "fix": "Review and update"
            })
    return issues


def check_overdue(registry):
    """Flag items past their due date."""
    issues = []
    for item in registry["items"]:
        if item["status"] in ("done", "published", "parked"):
            continue
        if item.get("due"):
            try:
                due = datetime.strptime(item["due"], "%Y-%m-%d")
                if datetime.now() > due:
                    days_over = (datetime.now() - due).days
                    issues.append({
                        "severity": "critical" if days_over > 7 else "warning",
                        "item_id": item["id"],
                        "message": f"Overdue by {days_over} day(s) (due: {item['due']})",
                        "fix": "Complete, reschedule, or park"
                    })
            except ValueError:
                pass
    return issues


def check_orphaned_items(registry):
    """Items with no next_action and not completed."""
    issues = []
    for item in registry["items"]:
        if item["status"] in ("done", "published", "parked"):
            continue
        if not item.get("next_action"):
            issues.append({
                "severity": "warning",
                "item_id": item["id"],
                "message": f"No next_action defined (status: {item['status']})",
                "fix": "Define what happens next"
            })
    return issues


def check_blocked_items(registry):
    """Items blocked for too long."""
    issues = []
    for item in registry["items"]:
        if item["status"] == "blocked" or item.get("blocked_on"):
            days = days_since(item.get("updated"))
            if days and days >= 14:
                issues.append({
                    "severity": "critical",
                    "item_id": item["id"],
                    "message": f"Blocked for {days}+ days on: {item.get('blocked_on', 'unknown')}",
                    "fix": "Unblock or kill"
                })
    return issues


def check_agent_structure():
    """Verify all agent folders have required files."""
    issues = []
    agents_dir = ROOT / "agents"
    if not agents_dir.exists():
        return issues

    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir():
            continue
        prompt = agent_dir / "prompt.md"
        if not prompt.exists():
            issues.append({
                "severity": "critical",
                "item_id": f"agent:{agent_dir.name}",
                "message": f"Missing prompt.md in agents/{agent_dir.name}/",
                "fix": "Create prompt.md for this agent"
            })
    return issues


def check_in_progress_items(registry):
    """Flag items stuck in_progress (crash detection)."""
    issues = []
    for item in registry["items"]:
        if item["status"] == "in_progress":
            days = days_since(item.get("updated"))
            if days and days >= 1:
                issues.append({
                    "severity": "warning",
                    "item_id": item["id"],
                    "message": f"Still in_progress for {days} day(s) — possible crashed session",
                    "fix": "Verify status: complete or revert to previous status"
                })
    return issues


def check_dependencies(registry):
    """If meta/dependencies.json exists, check timestamp freshness."""
    issues = []
    deps = load_json(DEPS_PATH)
    if not deps:
        return issues

    for chain in deps.get("chains", []):
        source_path = ROOT / chain["source"]
        if not source_path.exists():
            issues.append({
                "severity": "warning",
                "item_id": "deps",
                "message": f"Dependency source missing: {chain['source']}",
                "fix": "Update dependencies.json or restore file"
            })
            continue

        source_mtime = datetime.fromtimestamp(source_path.stat().st_mtime)

        for dep_path_str in chain.get("dependents", []):
            dep_path = ROOT / dep_path_str
            if not dep_path.exists():
                continue
            dep_mtime = datetime.fromtimestamp(dep_path.stat().st_mtime)
            if source_mtime > dep_mtime:
                delta = (source_mtime - dep_mtime).days
                issues.append({
                    "severity": "warning" if delta < 7 else "critical",
                    "item_id": "deps",
                    "message": f"Source {chain['source']} updated {delta}d after dependent {dep_path_str}",
                    "fix": f"Update {dep_path_str} to reflect changes in {chain['source']}"
                })
    return issues


def main():
    if not REGISTRY_PATH.exists():
        print(f"❌ Registry not found at {REGISTRY_PATH}")
        return

    registry = load_json(REGISTRY_PATH)
    print(f"📖 Loaded registry: {len(registry['items'])} items")
    print("")

    all_issues = []
    checks = [
        ("Artifact Paths", check_artifact_paths(registry)),
        ("Staleness", check_staleness(registry)),
        ("Overdue", check_overdue(registry)),
        ("Orphaned Items", check_orphaned_items(registry)),
        ("Blocked Items", check_blocked_items(registry)),
        ("Agent Structure", check_agent_structure()),
        ("Crash Detection", check_in_progress_items(registry)),
        ("Dependencies", check_dependencies(registry)),
    ]

    for check_name, issues in checks:
        all_issues.extend(issues)
        icon = "✅" if not issues else SEVERITY.get(issues[0]["severity"], "")
        print(f"{icon} {check_name}: {len(issues)} issue(s)")
        for issue in issues:
            print(f"   {SEVERITY[issue['severity']]} [{issue['item_id']}] {issue['message']}")
            print(f"      Fix: {issue['fix']}")

    # Summary
    critical = sum(1 for i in all_issues if i["severity"] == "critical")
    warning = sum(1 for i in all_issues if i["severity"] == "warning")
    info = sum(1 for i in all_issues if i["severity"] == "info")

    print("")
    print("─" * 50)
    if critical == 0 and warning == 0:
        print("✅ System healthy. No issues found.")
    else:
        print(f"🔴 {critical} critical  🟡 {warning} warning  ℹ️ {info} info")
        if critical > 0:
            print("⚠️  Critical issues need attention before next session.")

    return all_issues


if __name__ == "__main__":
    main()
