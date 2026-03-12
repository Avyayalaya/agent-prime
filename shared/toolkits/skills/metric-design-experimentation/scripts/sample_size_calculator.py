#!/usr/bin/env python3
"""
sample_size_calculator.py — Experiment Sample Size & Duration Estimator

Part of PM Skills Arsenal — Metric Design & Experimentation (BLD-003)
License: MIT

Calculates required sample size per variant for an A/B test given:
- Baseline conversion/metric rate
- Minimum Detectable Effect (MDE)
- Significance level (alpha)
- Statistical power (1 - beta)

Optionally estimates experiment duration given daily traffic.

Dependencies: none (pure Python — uses scipy if available for precision, falls back to approximation)
"""

import argparse
import io
import math
import sys

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    from scipy.stats import norm
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def z_score(p: float) -> float:
    """Approximate inverse normal CDF (Beasley-Springer-Moro algorithm)."""
    if HAS_SCIPY:
        return norm.ppf(p)
    # Rational approximation for 0.5 < p < 1
    if p < 0.5:
        return -z_score(1 - p)
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)


def sample_size_proportions(baseline: float, mde_relative: float, alpha: float, power: float) -> int:
    """Sample size per variant for a two-proportion z-test."""
    p1 = baseline
    p2 = baseline * (1 + mde_relative / 100)
    z_alpha = z_score(1 - alpha / 2)
    z_beta = z_score(power)
    pooled_var = p1 * (1 - p1) + p2 * (1 - p2)
    n = pooled_var * ((z_alpha + z_beta) ** 2) / ((p2 - p1) ** 2)
    return math.ceil(n)


def sample_size_means(baseline_mean: float, std_dev: float, mde_relative: float, alpha: float, power: float) -> int:
    """Sample size per variant for a two-sample t-test (continuous metrics)."""
    delta = baseline_mean * (mde_relative / 100)
    z_alpha = z_score(1 - alpha / 2)
    z_beta = z_score(power)
    n = 2 * (std_dev ** 2) * ((z_alpha + z_beta) ** 2) / (delta ** 2)
    return math.ceil(n)


def format_duration(days: int) -> str:
    if days <= 7:
        return f"{days} days"
    weeks = days / 7
    if weeks <= 8:
        return f"{days} days (~{weeks:.1f} weeks)"
    return f"{days} days (~{days/30:.1f} months)"


def main():
    parser = argparse.ArgumentParser(
        description="Calculate A/B test sample size and duration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Conversion rate test: 5% baseline, detect 10% relative lift
  python sample_size_calculator.py --baseline 0.05 --mde 10

  # With daily traffic estimate
  python sample_size_calculator.py --baseline 0.05 --mde 10 --daily-traffic 5000

  # Continuous metric (e.g., revenue per user)
  python sample_size_calculator.py --baseline-mean 25.0 --std-dev 15.0 --mde 5

  # Custom alpha and power
  python sample_size_calculator.py --baseline 0.12 --mde 8 --alpha 0.01 --power 0.90
        """,
    )
    parser.add_argument("--baseline", type=float, help="Baseline conversion rate (0-1), e.g., 0.05 for 5%%")
    parser.add_argument("--baseline-mean", type=float, help="Baseline mean for continuous metrics")
    parser.add_argument("--std-dev", type=float, help="Standard deviation for continuous metrics")
    parser.add_argument("--mde", type=float, required=True, help="Minimum Detectable Effect as relative %% (e.g., 10 = detect 10%% lift)")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level (default: 0.05)")
    parser.add_argument("--power", type=float, default=0.80, help="Statistical power (default: 0.80)")
    parser.add_argument("--daily-traffic", type=int, help="Daily eligible users (to estimate duration)")
    parser.add_argument("--variants", type=int, default=2, help="Number of variants including control (default: 2)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.baseline is None and args.baseline_mean is None:
        parser.error("Provide either --baseline (proportions) or --baseline-mean + --std-dev (continuous)")

    is_proportions = args.baseline is not None

    if is_proportions:
        if not (0 < args.baseline < 1):
            parser.error("--baseline must be between 0 and 1")
        n_per_variant = sample_size_proportions(args.baseline, args.mde, args.alpha, args.power)
        effect_absolute = args.baseline * (args.mde / 100)
        metric_type = "proportion"
    else:
        if args.std_dev is None:
            parser.error("--std-dev is required for continuous metrics")
        n_per_variant = sample_size_means(args.baseline_mean, args.std_dev, args.mde, args.alpha, args.power)
        effect_absolute = args.baseline_mean * (args.mde / 100)
        metric_type = "continuous"

    total_n = n_per_variant * args.variants
    duration_days = math.ceil(total_n / args.daily_traffic) if args.daily_traffic else None

    if args.json:
        import json
        result = {
            "metric_type": metric_type,
            "baseline": args.baseline if is_proportions else args.baseline_mean,
            "mde_relative_pct": args.mde,
            "mde_absolute": round(effect_absolute, 6),
            "alpha": args.alpha,
            "power": args.power,
            "variants": args.variants,
            "sample_size_per_variant": n_per_variant,
            "total_sample_size": total_n,
        }
        if duration_days:
            result["daily_traffic"] = args.daily_traffic
            result["estimated_duration_days"] = duration_days
        print(json.dumps(result, indent=2))
        return

    # Markdown output
    print("## Sample Size Calculation\n")
    print("| Parameter | Value |")
    print("|-----------|-------|")
    if is_proportions:
        print(f"| Baseline rate | {args.baseline:.4f} ({args.baseline*100:.2f}%) |")
        print(f"| Target rate | {args.baseline + effect_absolute:.4f} ({(args.baseline + effect_absolute)*100:.2f}%) |")
    else:
        print(f"| Baseline mean | {args.baseline_mean:.2f} |")
        print(f"| Std deviation | {args.std_dev:.2f} |")
        print(f"| Target mean | {args.baseline_mean + effect_absolute:.2f} |")
    print(f"| MDE (relative) | {args.mde:.1f}% |")
    print(f"| MDE (absolute) | {effect_absolute:.4f} |")
    print(f"| Significance (α) | {args.alpha} |")
    print(f"| Power (1-β) | {args.power} |")
    print(f"| Variants | {args.variants} |")
    print(f"| **Sample per variant** | **{n_per_variant:,}** |")
    print(f"| **Total sample needed** | **{total_n:,}** |")

    if duration_days:
        print(f"| Daily traffic | {args.daily_traffic:,} |")
        print(f"| **Estimated duration** | **{format_duration(duration_days)}** |")
        if duration_days < 7:
            print(f"\n⚠️ Duration < 7 days. Consider running for at least 1 full week to account for day-of-week effects.")
        if duration_days > 90:
            print(f"\n⚠️ Duration > 90 days. Consider: (1) increasing MDE threshold, (2) increasing traffic via broader targeting, or (3) using a different methodology.")

    print(f"\n{'ℹ️ Using scipy.stats for precision' if HAS_SCIPY else 'ℹ️ Using approximation (install scipy for higher precision)'}")


if __name__ == "__main__":
    main()
