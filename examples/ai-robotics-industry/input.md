# Pipeline Input

## The prompt

> "I want to understand the AI robotics industry — key players, structural dynamics, and investment implications."

That's it. One sentence. No additional context, no research brief, no framework selection.

## What happened next

Agent Prime's orchestrator (Prime) read the input and activated the **Research + Analysis** pipeline:

```
Input (1 sentence)
     │
     ▼
┌─────────┐
│  Scout   │ → Scanned 50+ sources for signals on AI robotics
│  (5 min) │   market data, company filings, research reports
└────┬─────┘
     │ 8 sourced signals with evidence tiers
     ▼
┌─────────────────┐
│ Industry Analyst │ → 9-step structural methodology
│   (45 min)       │   value chain → bottlenecks → scenarios
└────┬─────────────┘
     │ 705-line structural analysis (explicit handoff threads)
     ▼
┌──────────────────┐
│Investment Analyst │ → 4-lens valuation framework
│   (45 min)        │   SIG/EV → adoption curves → comparables → stress test
└────┬──────────────┘
     │ 623-line investment thesis with watchlist + exit rules
     ▼
┌────────────────┐
│  Validation    │ → 10-test E2E verification
│  (10 min)      │   8 pass, 1 fail, 1 partial
└────────────────┘
```

**Total time:** ~2 hours across 2 sessions
**Total output:** 1,328 lines (~50 pages) across 2 artifacts + validation report
**Human input after the initial prompt:** Review and feedback between stages

## What you'd get without Agent Prime

~800 words of generic industry overview. No value chain decomposition, no bottleneck scoring, no scenario modeling, no stress testing, no evidence tiers.

See [comparison.md](comparison.md) for the side-by-side.
