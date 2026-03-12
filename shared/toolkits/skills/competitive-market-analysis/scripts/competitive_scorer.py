#!/usr/bin/env python3
"""
competitive_scorer.py — 7 Powers Competitive Scoring Matrix

Part of PM Skills Arsenal (BLD-003)
License: MIT

Produces markdown-formatted competitive scorecards with:
- 7 Powers heat map with weighted scores
- Moat Durability Index (MDI) per competitor
- Power accrual/erosion trajectory
- Aggregate competitive position ranking

Dependencies: numpy
"""

import argparse
import io
import json
import sys
from typing import Optional

# Fix Windows emoji output encoding
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


POWERS = [
    "Scale Economies",
    "Network Effects",
    "Counter-Positioning",
    "Switching Costs",
    "Branding",
    "Cornered Resource",
    "Process Power",
]

RATING_MAP = {
    "strong": 3,
    "moderate": 2,
    "weak": 1,
    "none": 0,
    "3": 3, "2": 2, "1": 1, "0": 0,
}

RATING_EMOJI = {3: "🟢", 2: "🟡", 1: "🔴", 0: "🔴"}
RATING_LABEL = {3: "Strong", 2: "Moderate", 1: "Weak", 0: "Absent"}

TRAJECTORY_MAP = {
    "accruing": "↑",
    "stable": "→",
    "eroding": "↓",
}

# Default weights — can be overridden per analysis
DEFAULT_WEIGHTS = {
    "Scale Economies": 1.0,
    "Network Effects": 1.2,
    "Counter-Positioning": 1.0,
    "Switching Costs": 1.1,
    "Branding": 0.8,
    "Cornered Resource": 1.0,
    "Process Power": 0.9,
}


def parse_rating(value: str) -> int:
    """Convert a rating string to numeric score."""
    return RATING_MAP.get(str(value).lower().strip(), 0)


def calculate_mdi(scores: list[int], trajectories: Optional[list[str]] = None) -> float:
    """
    Calculate Moat Durability Index.
    
    MDI = weighted average of power scores, adjusted by trajectory.
    Accruing powers get 1.2x, eroding get 0.7x.
    """
    weights = list(DEFAULT_WEIGHTS.values())
    adjusted_scores = []
    
    for i, score in enumerate(scores):
        trajectory_multiplier = 1.0
        if trajectories and i < len(trajectories):
            t = trajectories[i].lower().strip()
            if t == "accruing":
                trajectory_multiplier = 1.2
            elif t == "eroding":
                trajectory_multiplier = 0.7
        adjusted_scores.append(score * trajectory_multiplier * weights[i])

    if HAS_NUMPY:
        total_weight = np.sum(weights)
        mdi = np.sum(adjusted_scores) / (total_weight * 3) * 100  # normalize to 0-100
    else:
        total_weight = sum(weights)
        mdi = sum(adjusted_scores) / (total_weight * 3) * 100

    return round(mdi, 1)


def generate_heat_map(competitors: dict, trajectories: Optional[dict] = None) -> str:
    """
    Generate a 7 Powers heat map in markdown format.
    
    Args:
        competitors: {name: {power: rating}} where rating is strong/moderate/weak/none
        trajectories: {name: {power: accruing/stable/eroding}} (optional)
    """
    output = []
    output.append("## 7 Powers Competitive Scorecard")
    output.append("")

    # Header
    comp_names = list(competitors.keys())
    header = "| Power | " + " | ".join(comp_names) + " |"
    separator = "|-------|" + "|".join([":---:" for _ in comp_names]) + "|"
    output.append(header)
    output.append(separator)

    # Rows
    mdi_scores = {name: [] for name in comp_names}
    trajectory_data = {name: [] for name in comp_names}

    for power in POWERS:
        row = f"| **{power}** |"
        for name in comp_names:
            rating_str = competitors[name].get(power, "none")
            score = parse_rating(rating_str)
            emoji = RATING_EMOJI[score]
            label = RATING_LABEL[score]
            
            traj_str = ""
            traj_value = "stable"
            if trajectories and name in trajectories:
                traj_value = trajectories[name].get(power, "stable")
                traj_str = f" {TRAJECTORY_MAP.get(traj_value.lower(), '')}"

            row += f" {emoji} {label}{traj_str} |"
            mdi_scores[name].append(score)
            trajectory_data[name].append(traj_value)
        output.append(row)

    # MDI row
    output.append("")
    output.append("### Moat Durability Index (MDI)")
    output.append("")
    output.append("| Competitor | MDI Score | Rating | Dominant Power |")
    output.append("|-----------|:---------:|--------|---------------|")

    for name in comp_names:
        mdi = calculate_mdi(mdi_scores[name], trajectory_data[name])
        scores = mdi_scores[name]

        if mdi >= 70:
            mdi_rating = "🟢 Durable"
        elif mdi >= 40:
            mdi_rating = "🟡 Moderate"
        else:
            mdi_rating = "🔴 Fragile"

        dominant_idx = scores.index(max(scores))
        dominant_power = POWERS[dominant_idx]

        output.append(f"| {name} | {mdi:.1f}/100 | {mdi_rating} | {dominant_power} |")

    # Interpretation
    output.append("")
    output.append("**MDI Interpretation:**")
    output.append("- 70-100: Durable moat — would take 3+ years to erode")
    output.append("- 40-69: Moderate moat — defensible but vulnerable to sustained attack")
    output.append("- 0-39: Fragile position — limited structural competitive advantage")
    output.append("")
    output.append("**Trajectory indicators:** ↑ accruing (strengthening) | → stable | ↓ eroding (weakening)")

    return "\n".join(output)


def generate_progress_bars(competitors: dict) -> str:
    """Generate switching cost decomposition with progress bars."""
    cost_types = [
        "Financial", "Procedural/Learning", "Data/Migration",
        "Relational", "Identity", "Workflow/Integration", "Contractual/Regulatory"
    ]

    output = []
    output.append("## Switching Cost Decomposition")
    output.append("")

    comp_names = list(competitors.keys())
    header = "| Cost Type | " + " | ".join(comp_names) + " |"
    separator = "|-----------|" + "|".join([":---:" for _ in comp_names]) + "|"
    output.append(header)
    output.append(separator)

    for cost in cost_types:
        row = f"| **{cost}** |"
        for name in comp_names:
            score = competitors[name].get(cost, 5)
            score = max(0, min(10, int(score)))
            filled = "█" * score
            empty = "░" * (10 - score)
            row += f" {filled}{empty} {score}/10 |"
        output.append(row)

    return "\n".join(output)


def run_example():
    """Run a demo competitive scoring for AI copilot market."""
    competitors = {
        "Google Gemini": {
            "Scale Economies": "strong",
            "Network Effects": "strong",
            "Counter-Positioning": "none",
            "Switching Costs": "weak",
            "Branding": "strong",
            "Cornered Resource": "strong",
            "Process Power": "moderate",
        },
        "Apple Intelligence": {
            "Scale Economies": "moderate",
            "Network Effects": "moderate",
            "Counter-Positioning": "strong",
            "Switching Costs": "strong",
            "Branding": "strong",
            "Cornered Resource": "strong",
            "Process Power": "strong",
        },
        "Microsoft Copilot": {
            "Scale Economies": "strong",
            "Network Effects": "strong",
            "Counter-Positioning": "none",
            "Switching Costs": "strong",
            "Branding": "moderate",
            "Cornered Resource": "moderate",
            "Process Power": "moderate",
        },
        "ChatGPT": {
            "Scale Economies": "moderate",
            "Network Effects": "moderate",
            "Counter-Positioning": "strong",
            "Switching Costs": "weak",
            "Branding": "strong",
            "Cornered Resource": "moderate",
            "Process Power": "weak",
        },
    }

    trajectories = {
        "Google Gemini": {
            "Scale Economies": "stable",
            "Network Effects": "accruing",
            "Counter-Positioning": "stable",
            "Switching Costs": "accruing",
            "Branding": "stable",
            "Cornered Resource": "accruing",
            "Process Power": "stable",
        },
        "Apple Intelligence": {
            "Scale Economies": "stable",
            "Network Effects": "accruing",
            "Counter-Positioning": "stable",
            "Switching Costs": "accruing",
            "Branding": "stable",
            "Cornered Resource": "stable",
            "Process Power": "stable",
        },
        "Microsoft Copilot": {
            "Scale Economies": "stable",
            "Network Effects": "accruing",
            "Counter-Positioning": "stable",
            "Switching Costs": "stable",
            "Branding": "accruing",
            "Cornered Resource": "stable",
            "Process Power": "stable",
        },
        "ChatGPT": {
            "Scale Economies": "accruing",
            "Network Effects": "accruing",
            "Counter-Positioning": "eroding",
            "Switching Costs": "accruing",
            "Branding": "stable",
            "Cornered Resource": "accruing",
            "Process Power": "accruing",
        },
    }

    print("# Competitive Scoring Example: AI Copilot Market (2026)")
    print()
    print(generate_heat_map(competitors, trajectories))
    print()
    print("---")
    print()

    switching_costs = {
        "Google Gemini": {
            "Financial": 3, "Procedural/Learning": 4, "Data/Migration": 4,
            "Relational": 3, "Identity": 5, "Workflow/Integration": 2, "Contractual/Regulatory": 2,
        },
        "Apple Intelligence": {
            "Financial": 5, "Procedural/Learning": 3, "Data/Migration": 6,
            "Relational": 8, "Identity": 9, "Workflow/Integration": 7, "Contractual/Regulatory": 3,
        },
        "Microsoft Copilot": {
            "Financial": 8, "Procedural/Learning": 6, "Data/Migration": 9,
            "Relational": 7, "Identity": 8, "Workflow/Integration": 9, "Contractual/Regulatory": 7,
        },
        "ChatGPT": {
            "Financial": 2, "Procedural/Learning": 3, "Data/Migration": 3,
            "Relational": 2, "Identity": 6, "Workflow/Integration": 2, "Contractual/Regulatory": 1,
        },
    }

    print(generate_progress_bars(switching_costs))


def main():
    parser = argparse.ArgumentParser(
        description="7 Powers Competitive Scorer — PM Skills Arsenal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --example
  %(prog)s --competitors "Google,Apple,Microsoft" --powers-json scores.json
  %(prog)s --competitors "Google,Apple" --powers-json scores.json --trajectories-json traj.json

JSON format for --powers-json:
  {"Google": {"Scale Economies": "strong", "Network Effects": "moderate", ...}, ...}

JSON format for --trajectories-json:
  {"Google": {"Scale Economies": "accruing", "Network Effects": "stable", ...}, ...}
        """,
    )
    parser.add_argument("--competitors", type=str, help="Comma-separated competitor names")
    parser.add_argument("--powers-json", type=str, help="Path to JSON file with power ratings")
    parser.add_argument("--trajectories-json", type=str, help="Path to JSON file with trajectories (optional)")
    parser.add_argument("--switching-costs-json", type=str, help="Path to JSON file with switching cost scores (optional)")
    parser.add_argument("--example", action="store_true", help="Run a demo competitive scoring")

    args = parser.parse_args()

    if args.example:
        run_example()
        return

    if not args.powers_json:
        parser.print_help()
        sys.exit(1)

    with open(args.powers_json, "r") as f:
        competitors = json.load(f)

    trajectories = None
    if args.trajectories_json:
        with open(args.trajectories_json, "r") as f:
            trajectories = json.load(f)

    print(generate_heat_map(competitors, trajectories))

    if args.switching_costs_json:
        with open(args.switching_costs_json, "r") as f:
            switching_costs = json.load(f)
        print()
        print("---")
        print()
        print(generate_progress_bars(switching_costs))


if __name__ == "__main__":
    main()
