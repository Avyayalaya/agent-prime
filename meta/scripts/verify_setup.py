#!/usr/bin/env python3
"""
Agent Prime — Setup Verification Script
Checks that the system is configured and ready to use.
Run after onboarding or manual setup to verify everything is in place.
"""

import json
import os
import sys


def looks_like_blank_context(content):
    markers = [
        "AGENT_PRIME_TEMPLATE: CONTEXT",
        "This file starts intentionally neutral.",
        "<!-- Add your name -->",
        "<!-- Goal 1 -->"
    ]
    return any(marker in content for marker in markers)

def check(label, passed, detail=""):
    icon = "PASS" if passed else "FAIL"
    msg = f"  [{icon}] {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)
    return passed

def main():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    passed = 0
    failed = 0
    total = 0

    print("\n  Agent Prime — Setup Verification")
    print("  " + "=" * 40)
    print()

    # 1. Check context.md is filled in
    total += 1
    context_path = os.path.join(root, "shared", "context.md")
    if os.path.exists(context_path):
        with open(context_path, "r", encoding="utf-8") as f:
            content = f.read()
        if not looks_like_blank_context(content) and len(content) > 400:
            passed += 1
            check("Identity configured", True, "shared/context.md")
        else:
            failed += 1
            check("Identity configured", False, "shared/context.md is still the neutral template. Run @onboarder or fill in your identity, goals, voice, and constraints.")
    else:
        failed += 1
        check("Identity configured", False, "shared/context.md not found")

    # 2. Check registry has items
    total += 1
    registry_path = os.path.join(root, "shared", "registry.json")
    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("items", [])
                if len(items) > 0:
                    passed += 1
                    check("Registry has work items", True, f"{len(items)} item(s) in shared/registry.json")
                else:
                    failed += 1
                    check("Registry has work items", False, "shared/registry.json is still empty. This is normal on a fresh install; run @onboarder or add your first work item manually.")
            except json.JSONDecodeError:
                failed += 1
                check("Registry has work items", False, "shared/registry.json has invalid JSON")
    else:
        failed += 1
        check("Registry has work items", False, "shared/registry.json not found")

    # 3. Check config has goals
    total += 1
    config_path = os.path.join(root, "prime", "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            try:
                config = json.load(f)
                goals = config.get("goals", {})
                if len(goals) > 0:
                    passed += 1
                    check("Goals configured", True, f"{len(goals)} goal(s) in prime/config.json")
                else:
                    failed += 1
                    check("Goals configured", False, "prime/config.json still has no user goals. Run @onboarder or add your goal mappings manually.")
            except json.JSONDecodeError:
                failed += 1
                check("Goals configured", False, "prime/config.json has invalid JSON")
    else:
        failed += 1
        check("Goals configured", False, "prime/config.json not found")

    # 4. Check dispatch.md exists
    total += 1
    dispatch_path = os.path.join(root, "prime", "dispatch.md")
    if os.path.exists(dispatch_path):
        passed += 1
        check("Dispatch queue exists", True, "prime/dispatch.md")
    else:
        failed += 1
        check("Dispatch queue exists", False, "prime/dispatch.md not found")

    # 5. Check agent prompts exist
    total += 1
    agents_dir = os.path.join(root, "agents")
    expected_agents = ["prime", "scout", "synthesizer", "writer", "planner", "builder"]
    found = [a for a in expected_agents if os.path.exists(os.path.join(agents_dir, a, "prompt.md"))]
    if len(found) == len(expected_agents):
        passed += 1
        check("Agent prompts present", True, f"{len(found)}/{len(expected_agents)} core agents")
    else:
        missing = set(expected_agents) - set(found)
        failed += 1
        check("Agent prompts present", False, f"Missing: {', '.join(missing)}")

    # 6. Check Python scripts exist
    total += 1
    scripts = ["generate_briefing.py", "generate_dashboard.py", "integrity_check.py"]
    scripts_dir = os.path.join(root, "meta", "scripts")
    found_scripts = [s for s in scripts if os.path.exists(os.path.join(scripts_dir, s))]
    if len(found_scripts) == len(scripts):
        passed += 1
        check("Automation scripts present", True, f"{len(found_scripts)}/{len(scripts)} scripts")
    else:
        missing = set(scripts) - set(found_scripts)
        failed += 1
        check("Automation scripts present", False, f"Missing: {', '.join(missing)}")

    # 7. Check learnings.md exists
    total += 1
    learnings_path = os.path.join(root, "shared", "learnings.md")
    if os.path.exists(learnings_path):
        passed += 1
        check("Learnings file exists", True, "shared/learnings.md (starts empty, grows with use)")
    else:
        failed += 1
        check("Learnings file exists", False, "shared/learnings.md not found")

    # Summary
    print()
    print("  " + "-" * 40)
    if failed == 0:
        print(f"  System ready! {passed}/{total} checks passed.")
        print()
        print("  Next steps:")
        print("    1. Run: python meta/scripts/generate_dashboard.py")
        print("    2. Try Guided Project 1: getting-started/project-1-research-publish/")
        print("    3. Or invoke Prime: @prime Show me the system pulse")
        print()
        return 0
    else:
        print(f"  {failed} issue(s) found. {passed}/{total} checks passed.")
        print()
        print("  Fix the issues above, then run this script again.")
        print("  For help: see QUICKSTART.md or run the Onboarding Agent (@onboarder)")
        print()
        return 1

if __name__ == "__main__":
    sys.exit(main())
