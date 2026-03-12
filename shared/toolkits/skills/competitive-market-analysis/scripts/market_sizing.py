#!/usr/bin/env python3
"""
market_sizing.py — TAM/SAM/SOM Calculator for Competitive & Market Analysis

Part of PM Skills Arsenal (BLD-003)
License: MIT

Produces markdown-formatted market sizing tables from population, penetration,
and ARPU inputs. Supports top-down, bottom-up, and value-theory approaches.

Dependencies: stdlib only (no external packages)
"""

import argparse
import json
import sys
from typing import Optional


def format_currency(value: float) -> str:
    """Format a number as a readable currency string."""
    if abs(value) >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"
    elif abs(value) >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    elif abs(value) >= 1_000:
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:.0f}"


def format_number(value: float) -> str:
    """Format a number with commas."""
    if abs(value) >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    elif abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    elif abs(value) >= 1_000:
        return f"{value / 1_000:.1f}K"
    else:
        return f"{value:,.0f}"


def top_down_sizing(
    total_market_population: float,
    tam_penetration: float,
    sam_penetration: float,
    som_penetration: float,
    arpu: float,
    cagr: Optional[float] = None,
    years: int = 5,
) -> str:
    """
    Top-down market sizing: Total population × penetration rates × ARPU.

    Args:
        total_market_population: Total addressable population (users/companies)
        tam_penetration: % of total population that could use ANY solution (0-1)
        sam_penetration: % of TAM reachable with YOUR solution (0-1)
        som_penetration: % of SAM you can realistically capture (0-1)
        arpu: Average Revenue Per User (annual)
        cagr: Compound Annual Growth Rate (optional, 0-1)
        years: Projection years (default 5)
    """
    tam_users = total_market_population * tam_penetration
    sam_users = tam_users * sam_penetration
    som_users = sam_users * som_penetration

    tam_revenue = tam_users * arpu
    sam_revenue = sam_users * arpu
    som_revenue = som_users * arpu

    output = []
    output.append("## Market Sizing — Top-Down Approach")
    output.append("")
    output.append("| Metric | Users | Revenue | Penetration |")
    output.append("|--------|-------|---------|-------------|")
    output.append(
        f"| **TAM** (Total Addressable) | {format_number(tam_users)} | "
        f"{format_currency(tam_revenue)} | {tam_penetration*100:.0f}% of total market |"
    )
    output.append(
        f"| **SAM** (Serviceable Addressable) | {format_number(sam_users)} | "
        f"{format_currency(sam_revenue)} | {sam_penetration*100:.0f}% of TAM |"
    )
    output.append(
        f"| **SOM** (Serviceable Obtainable) | {format_number(som_users)} | "
        f"{format_currency(som_revenue)} | {som_penetration*100:.0f}% of SAM |"
    )
    output.append("")
    output.append("**Assumptions:**")
    output.append(f"- Total market population: {format_number(total_market_population)}")
    output.append(f"- ARPU: {format_currency(arpu)}/year")

    if cagr is not None:
        output.append("")
        output.append(f"### {years}-Year Projection (CAGR: {cagr*100:.1f}%)")
        output.append("")
        output.append("| Year | TAM | SAM | SOM |")
        output.append("|------|-----|-----|-----|")
        for y in range(years + 1):
            growth = (1 + cagr) ** y
            output.append(
                f"| Y{y} | {format_currency(tam_revenue * growth)} | "
                f"{format_currency(sam_revenue * growth)} | "
                f"{format_currency(som_revenue * growth)} |"
            )

    return "\n".join(output)


def bottom_up_sizing(
    segments: list[dict],
    arpu_by_segment: Optional[dict] = None,
) -> str:
    """
    Bottom-up market sizing: Sum of individual segments.

    Args:
        segments: List of dicts with keys: name, users, arpu
        arpu_by_segment: Optional override ARPUs by segment name
    """
    output = []
    output.append("## Market Sizing — Bottom-Up Approach")
    output.append("")
    output.append("| Segment | Users | ARPU | Revenue | % of Total |")
    output.append("|---------|-------|------|---------|------------|")

    total_revenue = 0
    segment_data = []
    for seg in segments:
        name = seg["name"]
        users = seg["users"]
        arpu = seg.get("arpu", 0)
        if arpu_by_segment and name in arpu_by_segment:
            arpu = arpu_by_segment[name]
        revenue = users * arpu
        total_revenue += revenue
        segment_data.append((name, users, arpu, revenue))

    for name, users, arpu, revenue in segment_data:
        pct = (revenue / total_revenue * 100) if total_revenue > 0 else 0
        output.append(
            f"| {name} | {format_number(users)} | {format_currency(arpu)} | "
            f"{format_currency(revenue)} | {pct:.1f}% |"
        )

    output.append(f"| **Total** | | | **{format_currency(total_revenue)}** | 100% |")

    return "\n".join(output)


def run_example():
    """Run a demo calculation for AI copilot market."""
    print("# Market Sizing Example: AI Copilot/Assistant Market (2026)")
    print()
    print(top_down_sizing(
        total_market_population=4_400_000_000,  # global internet users
        tam_penetration=0.25,  # 25% could use an AI assistant
        sam_penetration=0.15,  # 15% reachable via our channels
        som_penetration=0.02,  # 2% realistic capture in Y1
        arpu=120,  # $10/month
        cagr=0.35,  # 35% CAGR
        years=5,
    ))
    print()
    print("---")
    print()
    print(bottom_up_sizing(
        segments=[
            {"name": "Enterprise (>1000 employees)", "users": 50_000_000, "arpu": 360},
            {"name": "SMB (50-1000 employees)", "users": 200_000_000, "arpu": 180},
            {"name": "Prosumer / Freelancer", "users": 500_000_000, "arpu": 96},
            {"name": "Consumer (free tier)", "users": 1_000_000_000, "arpu": 0},
        ]
    ))


def main():
    parser = argparse.ArgumentParser(
        description="TAM/SAM/SOM Market Sizing Calculator — PM Skills Arsenal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --tam 1000000000 --penetration 0.25,0.15,0.02 --arpu 120
  %(prog)s --tam 1000000000 --penetration 0.25,0.15,0.02 --arpu 120 --cagr 0.35 --years 5
  %(prog)s --example
  %(prog)s --segments '[{"name":"Enterprise","users":50000000,"arpu":360}]'
        """,
    )
    parser.add_argument("--tam", type=float, help="Total market population (users/companies)")
    parser.add_argument(
        "--penetration",
        type=str,
        help="Comma-separated penetration rates: TAM%%,SAM%%,SOM%% (as decimals, e.g., 0.25,0.15,0.02)",
    )
    parser.add_argument("--arpu", type=float, help="Average Revenue Per User (annual, USD)")
    parser.add_argument("--cagr", type=float, help="Compound Annual Growth Rate (decimal, e.g., 0.35)")
    parser.add_argument("--years", type=int, default=5, help="Projection years (default: 5)")
    parser.add_argument("--segments", type=str, help='JSON array of segments: [{"name":"X","users":N,"arpu":N}]')
    parser.add_argument("--example", action="store_true", help="Run a demo calculation")

    args = parser.parse_args()

    if args.example:
        run_example()
        return

    if args.segments:
        segments = json.loads(args.segments)
        print(bottom_up_sizing(segments))
        return

    if not all([args.tam, args.penetration, args.arpu]):
        parser.print_help()
        sys.exit(1)

    rates = [float(r) for r in args.penetration.split(",")]
    if len(rates) != 3:
        print("Error: --penetration requires exactly 3 comma-separated values (TAM,SAM,SOM)")
        sys.exit(1)

    print(top_down_sizing(
        total_market_population=args.tam,
        tam_penetration=rates[0],
        sam_penetration=rates[1],
        som_penetration=rates[2],
        arpu=args.arpu,
        cagr=args.cagr,
        years=args.years,
    ))


if __name__ == "__main__":
    main()
