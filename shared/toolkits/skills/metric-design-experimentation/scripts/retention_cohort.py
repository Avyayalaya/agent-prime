#!/usr/bin/env python3
"""
retention_cohort.py — Retention Cohort Analysis Generator

Part of PM Skills Arsenal — Metric Design & Experimentation (BLD-003)
License: MIT

Generates retention cohort tables and flags degradation patterns from user activity data.
Accepts CSV with user_id, signup_date, and activity_date columns.

Dependencies: none (pure Python — uses pandas if available for performance)
"""

import argparse
import csv
import io
import sys
from collections import defaultdict
from datetime import datetime, timedelta

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def parse_date(s: str) -> datetime:
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: '{s}'. Supported: YYYY-MM-DD, YYYY/MM/DD, MM/DD/YYYY, DD-MM-YYYY")


def load_data(filepath: str, signup_col: str, activity_col: str, user_col: str):
    """Load CSV and return dict of user_id -> (signup_date, set of activity_dates)."""
    users = {}
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        available = reader.fieldnames
        for col in [user_col, signup_col, activity_col]:
            if col not in available:
                print(f"Error: Column '{col}' not found. Available: {available}")
                sys.exit(1)
        for row in reader:
            uid = row[user_col].strip()
            signup = parse_date(row[signup_col])
            activity = parse_date(row[activity_col])
            if uid not in users:
                users[uid] = {"signup": signup, "activities": set()}
            users[uid]["activities"].add(activity)
    return users


def build_cohorts(users: dict, granularity: str = "month"):
    """Group users into cohorts by signup period."""
    cohorts = defaultdict(lambda: {"users": set(), "active_at": defaultdict(set)})

    for uid, data in users.items():
        signup = data["signup"]
        if granularity == "month":
            cohort_key = signup.strftime("%Y-%m")
        elif granularity == "week":
            monday = signup - timedelta(days=signup.weekday())
            cohort_key = monday.strftime("%Y-W%W")
        else:
            cohort_key = signup.strftime("%Y-%m")

        cohorts[cohort_key]["users"].add(uid)
        for act_date in data["activities"]:
            days_since = (act_date - signup).days
            if days_since >= 0:
                cohorts[cohort_key]["active_at"][days_since].add(uid)

    return dict(sorted(cohorts.items()))


def compute_retention(cohorts: dict, periods: list):
    """Compute retention rate at each period for each cohort."""
    results = {}
    for cohort_key, cohort_data in cohorts.items():
        total = len(cohort_data["users"])
        if total == 0:
            continue
        retention = {}
        for period_days in periods:
            # Count users active on any day within the period window
            window_start = period_days
            window_end = period_days + (7 if period_days <= 14 else 14 if period_days <= 60 else 30)
            active = set()
            for day in range(window_start, window_end):
                active |= cohort_data["active_at"].get(day, set())
            retention[period_days] = len(active) / total
        results[cohort_key] = {"total_users": total, "retention": retention}
    return results


def detect_degradation(results: dict, period: int) -> dict:
    """Check if newer cohorts retain worse at a given period."""
    cohort_keys = sorted(results.keys())
    values = []
    for key in cohort_keys:
        r = results[key]["retention"].get(period)
        if r is not None:
            values.append((key, r))

    if len(values) < 3:
        return {"status": "insufficient_data", "message": "Need ≥3 cohorts for degradation detection"}

    # Check trend: are more recent cohorts worse?
    declines = 0
    for i in range(1, len(values)):
        if values[i][1] < values[i - 1][1]:
            declines += 1

    decline_rate = declines / (len(values) - 1)
    first_val = values[0][1]
    last_val = values[-1][1]
    absolute_change = last_val - first_val

    if decline_rate >= 0.7 and absolute_change < -0.05:
        status = "🔴 DEGRADING"
        message = f"Newer cohorts retaining worse. Day-{period} retention dropped {abs(absolute_change)*100:.1f}pp across {len(values)} cohorts."
    elif decline_rate >= 0.5 and absolute_change < -0.02:
        status = "⚠️ WARNING"
        message = f"Possible degradation trend. Day-{period} retention down {abs(absolute_change)*100:.1f}pp."
    else:
        status = "✅ STABLE"
        message = f"No degradation detected at day-{period}."

    return {"status": status, "message": message, "first": first_val, "last": last_val, "change": absolute_change}


def main():
    parser = argparse.ArgumentParser(
        description="Generate retention cohort analysis from user activity data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic analysis
  python retention_cohort.py --input users.csv --signup-col signup_date --activity-col login_date

  # Weekly cohorts with custom user ID column
  python retention_cohort.py --input data.csv --signup-col created_at --activity-col active_date --user-col user_id --granularity week

CSV format:
  user_id,signup_date,activity_date
  u001,2026-01-05,2026-01-05
  u001,2026-01-05,2026-01-08
  u001,2026-01-05,2026-01-15
  u002,2026-01-05,2026-01-05
        """,
    )
    parser.add_argument("--input", required=True, help="CSV file path")
    parser.add_argument("--signup-col", required=True, help="Column name for signup/registration date")
    parser.add_argument("--activity-col", required=True, help="Column name for activity/login date")
    parser.add_argument("--user-col", default="user_id", help="Column name for user identifier (default: user_id)")
    parser.add_argument("--granularity", choices=["week", "month"], default="month", help="Cohort grouping (default: month)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    users = load_data(args.input, args.signup_col, args.activity_col, args.user_col)
    print(f"Loaded {len(users):,} unique users\n")

    cohorts = build_cohorts(users, args.granularity)
    periods = [1, 7, 14, 30, 60, 90]
    results = compute_retention(cohorts, periods)

    if args.json:
        import json
        output = {}
        for key, data in results.items():
            output[key] = {
                "users": data["total_users"],
                "retention": {f"day_{p}": round(r, 4) for p, r in data["retention"].items()},
            }
        print(json.dumps(output, indent=2))
        return

    # Markdown output
    print("## Retention Cohort Table\n")
    header = "| Cohort | Users | " + " | ".join(f"Day {p}" for p in periods) + " |"
    separator = "|--------|------:|" + "|".join("------:" for _ in periods) + "|"
    print(header)
    print(separator)

    for key, data in results.items():
        row = f"| {key} | {data['total_users']:,} |"
        for p in periods:
            r = data["retention"].get(p)
            if r is not None:
                row += f" {r*100:.1f}% |"
            else:
                row += " — |"
        print(row)

    # Degradation check
    print("\n## Cohort Degradation Check\n")
    for check_period in [7, 30, 90]:
        deg = detect_degradation(results, check_period)
        if deg["status"] != "insufficient_data":
            print(f"**Day {check_period}:** {deg['status']} — {deg['message']}")
        else:
            print(f"**Day {check_period}:** ℹ️ {deg['message']}")

    # Curve shape detection
    print("\n## Retention Curve Shape\n")
    for key, data in results.items():
        rates = [data["retention"].get(p, 0) for p in periods if data["retention"].get(p) is not None]
        if len(rates) < 3:
            continue
        # Check if curve is flattening (smile) or continuously declining (frown)
        diffs = [rates[i] - rates[i - 1] for i in range(1, len(rates))]
        late_diffs = diffs[len(diffs) // 2:]
        if all(d > -0.02 for d in late_diffs):
            shape = "✅ Smile (flattening)"
        elif all(d < -0.03 for d in late_diffs):
            shape = "❌ Frown (declining)"
        else:
            shape = "➡️ Mixed"
        print(f"- **{key}**: {shape}")


if __name__ == "__main__":
    main()
