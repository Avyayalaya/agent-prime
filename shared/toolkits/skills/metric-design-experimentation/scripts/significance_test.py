#!/usr/bin/env python3
"""
significance_test.py — A/B Test Statistical Significance Analyzer

Part of PM Skills Arsenal — Metric Design & Experimentation (BLD-003)
License: MIT

Tests whether experiment results are statistically significant.
Reports: p-value, confidence interval, effect size, achieved power.

Dependencies: none (pure Python — uses scipy if available)
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
    if HAS_SCIPY:
        return norm.ppf(p)
    if p < 0.5:
        return -z_score(1 - p)
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)


def normal_cdf(x: float) -> float:
    if HAS_SCIPY:
        return norm.cdf(x)
    # Approximation using error function
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def test_proportions(ctrl_n: int, ctrl_conv: int, treat_n: int, treat_conv: int, alpha: float):
    p_ctrl = ctrl_conv / ctrl_n
    p_treat = treat_conv / treat_n
    p_pooled = (ctrl_conv + treat_conv) / (ctrl_n + treat_n)

    se_pooled = math.sqrt(p_pooled * (1 - p_pooled) * (1 / ctrl_n + 1 / treat_n))
    if se_pooled == 0:
        return {"error": "Zero variance — all observations identical"}

    z = (p_treat - p_ctrl) / se_pooled
    p_value = 2 * (1 - normal_cdf(abs(z)))

    # Confidence interval (unpooled SE)
    se_unpooled = math.sqrt(p_ctrl * (1 - p_ctrl) / ctrl_n + p_treat * (1 - p_treat) / treat_n)
    z_crit = z_score(1 - alpha / 2)
    ci_lower = (p_treat - p_ctrl) - z_crit * se_unpooled
    ci_upper = (p_treat - p_ctrl) + z_crit * se_unpooled

    # Effect size
    lift_absolute = p_treat - p_ctrl
    lift_relative = (lift_absolute / p_ctrl * 100) if p_ctrl > 0 else float("inf")

    # Achieved power
    se_alt = math.sqrt(p_ctrl * (1 - p_ctrl) / ctrl_n + p_treat * (1 - p_treat) / treat_n)
    if se_alt > 0:
        noncentrality = abs(p_treat - p_ctrl) / se_alt
        power = 1 - normal_cdf(z_crit - noncentrality)
    else:
        power = 0

    return {
        "control_rate": p_ctrl,
        "treatment_rate": p_treat,
        "lift_absolute": lift_absolute,
        "lift_relative": lift_relative,
        "z_statistic": z,
        "p_value": p_value,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "achieved_power": power,
        "significant": p_value < alpha,
        "alpha": alpha,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Test A/B experiment statistical significance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic test: 10000 control (500 converted), 10000 treatment (550 converted)
  python significance_test.py --control-n 10000 --control-conv 500 --treatment-n 10000 --treatment-conv 550

  # Stricter alpha
  python significance_test.py --control-n 5000 --control-conv 250 --treatment-n 5000 --treatment-conv 290 --alpha 0.01
        """,
    )
    parser.add_argument("--control-n", type=int, required=True, help="Control group sample size")
    parser.add_argument("--control-conv", type=int, required=True, help="Control group conversions")
    parser.add_argument("--treatment-n", type=int, required=True, help="Treatment group sample size")
    parser.add_argument("--treatment-conv", type=int, required=True, help="Treatment group conversions")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level (default: 0.05)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.control_conv > args.control_n or args.treatment_conv > args.treatment_n:
        parser.error("Conversions cannot exceed sample size")

    result = test_proportions(args.control_n, args.control_conv, args.treatment_n, args.treatment_conv, args.alpha)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    if args.json:
        import json
        print(json.dumps({k: round(v, 6) if isinstance(v, float) else v for k, v in result.items()}, indent=2))
        return

    sig = result["significant"]
    sig_icon = "✅" if sig else "❌"
    direction = "↑" if result["lift_absolute"] > 0 else "↓"

    print("## A/B Test Results\n")
    print("| Metric | Control | Treatment |")
    print("|--------|---------|-----------|")
    print(f"| Sample size | {args.control_n:,} | {args.treatment_n:,} |")
    print(f"| Conversions | {args.control_conv:,} | {args.treatment_conv:,} |")
    print(f"| Rate | {result['control_rate']:.4f} ({result['control_rate']*100:.2f}%) | {result['treatment_rate']:.4f} ({result['treatment_rate']*100:.2f}%) |")

    print(f"\n### Analysis\n")
    print(f"| Measure | Value |")
    print(f"|---------|-------|")
    print(f"| Lift (absolute) | {direction} {abs(result['lift_absolute']):.4f} |")
    print(f"| Lift (relative) | {direction} {abs(result['lift_relative']):.2f}% |")
    print(f"| z-statistic | {result['z_statistic']:.4f} |")
    print(f"| p-value | {result['p_value']:.6f} |")
    print(f"| {100*(1-args.alpha):.0f}% CI | [{result['ci_lower']:.4f}, {result['ci_upper']:.4f}] |")
    print(f"| Achieved power | {result['achieved_power']:.2f} |")
    print(f"| **Significant at α={args.alpha}?** | **{sig_icon} {'Yes' if sig else 'No'}** |")

    if sig:
        if result["achieved_power"] < 0.8:
            print(f"\n⚠️ Statistically significant but **underpowered** (power = {result['achieved_power']:.2f} < 0.80). Result may not replicate. Consider larger sample.")
        else:
            print(f"\n✅ Result is statistically significant and adequately powered.")
    else:
        print(f"\n❌ Not statistically significant at α={args.alpha}.")
        if result["achieved_power"] < 0.8:
            print(f"   Power = {result['achieved_power']:.2f}. Test may be underpowered — a real effect could exist but the sample is too small to detect it.")

    if 0 in (result["ci_lower"], result["ci_upper"]) or (result["ci_lower"] < 0 < result["ci_upper"]):
        print(f"\nℹ️ Confidence interval crosses zero — the true effect could be positive, negative, or zero.")


if __name__ == "__main__":
    main()
