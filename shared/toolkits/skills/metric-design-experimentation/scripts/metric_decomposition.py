#!/usr/bin/env python3
"""
metric_decomposition.py — Rate Change Decomposition (Numerator vs Denominator Attribution)

Part of PM Skills Arsenal — Metric Design & Experimentation (BLD-003)
License: MIT

Decomposes a rate metric change into:
- How much came from the numerator changing (real improvement)
- How much came from the denominator changing (mix shift / denominator effect)

Catches FM-8 (The Denominator Shift) — rate improves because denominator shrank,
not because numerator grew.

Dependencies: none (pure Python)
"""

import argparse
import io
import sys

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def decompose_rate(num_before: float, den_before: float, num_after: float, den_after: float):
    """
    Decompose rate change into numerator and denominator effects.

    Method: Hold one component constant, vary the other.
    - Numerator effect: rate(num_after, den_before) - rate(num_before, den_before)
    - Denominator effect: rate(num_before, den_after) - rate(num_before, den_before)
    - Interaction: total - numerator_effect - denominator_effect
    """
    if den_before == 0 or den_after == 0:
        return {"error": "Denominator cannot be zero"}

    rate_before = num_before / den_before
    rate_after = num_after / den_after

    total_change = rate_after - rate_before

    # Numerator effect: change in rate if only numerator changed
    num_effect = (num_after / den_before) - rate_before

    # Denominator effect: change in rate if only denominator changed
    den_effect = (num_before / den_after) - rate_before

    # Interaction term
    interaction = total_change - num_effect - den_effect

    # Attribution percentages
    total_abs = abs(num_effect) + abs(den_effect) + abs(interaction)
    if total_abs == 0:
        pct_num = pct_den = pct_int = 0
    else:
        pct_num = num_effect / total_change * 100 if total_change != 0 else 0
        pct_den = den_effect / total_change * 100 if total_change != 0 else 0
        pct_int = interaction / total_change * 100 if total_change != 0 else 0

    return {
        "rate_before": rate_before,
        "rate_after": rate_after,
        "total_change": total_change,
        "numerator_effect": num_effect,
        "denominator_effect": den_effect,
        "interaction": interaction,
        "pct_from_numerator": pct_num,
        "pct_from_denominator": pct_den,
        "pct_interaction": pct_int,
        "numerator": {"before": num_before, "after": num_after, "change": num_after - num_before, "change_pct": (num_after - num_before) / num_before * 100 if num_before != 0 else 0},
        "denominator": {"before": den_before, "after": den_after, "change": den_after - den_before, "change_pct": (den_after - den_before) / den_before * 100 if den_before != 0 else 0},
    }


def main():
    parser = argparse.ArgumentParser(
        description="Decompose rate metric change into numerator vs denominator effects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Conversion rate: was 500/10000, now 480/8000
  python metric_decomposition.py --num-before 500 --den-before 10000 --num-after 480 --den-after 8000

  # With labels
  python metric_decomposition.py --num-before 500 --den-before 10000 --num-after 480 --den-after 8000 \\
    --metric-name "Conversion Rate" --num-label "Purchases" --den-label "Visitors"

Catches: FM-8 (Denominator Shift) — rate looks better but denominator shrank
        """,
    )
    parser.add_argument("--num-before", type=float, required=True, help="Numerator in period 1")
    parser.add_argument("--den-before", type=float, required=True, help="Denominator in period 1")
    parser.add_argument("--num-after", type=float, required=True, help="Numerator in period 2")
    parser.add_argument("--den-after", type=float, required=True, help="Denominator in period 2")
    parser.add_argument("--metric-name", default="Rate", help="Name of the metric (default: Rate)")
    parser.add_argument("--num-label", default="Numerator", help="Label for numerator (e.g., Purchases)")
    parser.add_argument("--den-label", default="Denominator", help="Label for denominator (e.g., Visitors)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    result = decompose_rate(args.num_before, args.den_before, args.num_after, args.den_after)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    if args.json:
        import json
        print(json.dumps({k: round(v, 6) if isinstance(v, float) else v for k, v in result.items()}, indent=2))
        return

    r = result
    direction = "↑" if r["total_change"] > 0 else "↓" if r["total_change"] < 0 else "→"

    print(f"## {args.metric_name} Decomposition\n")
    print("| Component | Before | After | Change |")
    print("|-----------|-------:|------:|-------:|")
    print(f"| {args.num_label} | {args.num_before:,.0f} | {args.num_after:,.0f} | {r['numerator']['change']:+,.0f} ({r['numerator']['change_pct']:+.1f}%) |")
    print(f"| {args.den_label} | {args.den_before:,.0f} | {args.den_after:,.0f} | {r['denominator']['change']:+,.0f} ({r['denominator']['change_pct']:+.1f}%) |")
    print(f"| **{args.metric_name}** | **{r['rate_before']:.4f}** ({r['rate_before']*100:.2f}%) | **{r['rate_after']:.4f}** ({r['rate_after']*100:.2f}%) | **{direction} {abs(r['total_change']):.4f}** ({r['total_change']/r['rate_before']*100:+.1f}% relative) |")

    print(f"\n### Attribution\n")
    print(f"| Source | Effect | % of Total Change |")
    print(f"|--------|-------:|------------------:|")
    print(f"| {args.num_label} effect | {r['numerator_effect']:+.4f} | {r['pct_from_numerator']:.1f}% |")
    print(f"| {args.den_label} effect | {r['denominator_effect']:+.4f} | {r['pct_from_denominator']:.1f}% |")
    if abs(r["interaction"]) > 0.0001:
        print(f"| Interaction | {r['interaction']:+.4f} | {r['pct_interaction']:.1f}% |")

    # Diagnosis
    print(f"\n### Diagnosis\n")
    den_pct = abs(r["pct_from_denominator"])
    num_pct = abs(r["pct_from_numerator"])

    if den_pct > 60 and r["total_change"] > 0 and r["denominator"]["change"] < 0:
        print(f"⚠️ **FM-8 DETECTED: Denominator Shift.** {args.metric_name} improved primarily because {args.den_label} dropped ({r['denominator']['change_pct']:.1f}%), not because {args.num_label} grew. This is a mix effect, not a real improvement.")
    elif den_pct > 40:
        print(f"⚠️ **Partial denominator effect.** {den_pct:.0f}% of the rate change comes from {args.den_label} movement. Investigate whether the {args.den_label} change is expected or a data artifact.")
    elif num_pct > 80:
        print(f"✅ **Real improvement.** {num_pct:.0f}% of the rate change comes from {args.num_label} movement. The {args.den_label} is stable — this is a genuine change.")
    else:
        print(f"ℹ️ **Mixed sources.** Rate change driven by both {args.num_label} ({num_pct:.0f}%) and {args.den_label} ({den_pct:.0f}%). Investigate both.")


if __name__ == "__main__":
    main()
