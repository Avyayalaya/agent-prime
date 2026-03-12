# Example Pipeline: AI Robotics Industry Analysis

> **Input:** One sentence.
> **Output:** 50 pages of structural analysis + investment thesis.
> **Time:** 2 sessions (~2 hours). Without the system: 2-3 weeks.

## What this demonstrates

This is a real pipeline run from Agent Prime — not a template, not a mock-up. A single question activated two specialized agents that produced publication-grade analysis with evidence tiers, scenario modeling, and adversarial stress testing.

## The pipeline

| Stage | Agent | What it produced | Lines |
|-------|-------|-----------------|-------|
| 1 | **Scout** | Signal digest — 8 sourced signals from research reports, market data, company filings | ~50 |
| 2 | **Industry Analyst** | 9-step structural analysis — value chain, bottlenecks, player matrix, scenarios, bear cases | 705 |
| 3 | **Investment Analyst** | 4-lens valuation — scenario/EV, adoption curves, comparables, stress test, watchlist | 623 |
| 4 | **Validation** | 10-test E2E verification — 8 pass, 1 fail, 1 partial | 253 |

## Files in this example

| File | What it is |
|------|-----------|
| [input.md](input.md) | The one-sentence prompt + pipeline flow diagram |
| [02-industry-analysis.md](02-industry-analysis.md) | Full structural analysis (705 lines) |
| [03-investment-thesis.md](03-investment-thesis.md) | Full investment thesis (623 lines) |
| [comparison.md](comparison.md) | Side-by-side: raw AI vs Agent Prime on the same question |

## Key insights the system found

Things raw AI misses that Agent Prime's methodology surfaced:

1. **The real bottleneck isn't compute — it's actuators.** Harmonic Drive and Nabtesco hold a duopoly on precision gears. Every humanoid robot depends on them. This structural dependency is invisible in a generic industry overview.

2. **Humanoids are pre-chasm. Industrial cobots are the investable wave.** The system positioned each segment on the S-curve independently, rather than treating "robotics" as one market.

3. **VLA models are the hidden dependency.** Vision-Language-Action models are the "robot brain" layer that doesn't exist yet at scale. The system identified this as a structural risk that most analyses miss.

4. **7 quantified bear cases** — from actuator supply chain disruption to China dumping subsidized robots. Each with estimated portfolio impact ranges.

## How to read the artifacts

**If you have 5 minutes:** Read the Executive Summary of each file — they're designed to stand alone.

**If you have 30 minutes:** Read the Executive Summary + Decision Bridge (investment thesis) + Bottleneck Identification (structural analysis).

**If you want the full picture:** Read both files end-to-end. The structural analysis feeds the investment thesis — you'll see explicit "assumption inheritance" where the Investment Analyst flags low-confidence inputs from the Industry Analyst.

## Note on sanitization

Portfolio-specific dollar amounts and personal financial data have been replaced with percentage-based allocations. All analytical content, frameworks, and methodology are preserved exactly as produced by the system.
