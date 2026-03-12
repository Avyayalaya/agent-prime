# Competitive & Market Analysis

> **Part of the PM Skills Arsenal** | [MIT License](../../LICENSE)

## What This Does

Produces an elite-tier **Competitive War Map** — not a feature comparison, but a structural assessment of who wins, why, and what to do about it. Encodes 7+ strategic frameworks (7 Powers, Aggregation Theory, Christensen, Martin, Wardley, JTBD, Kwok) with scoring rubrics and decision tables.

## When to Use

- Entering a new market or evaluating a competitive response
- Preparing a strategy review, board deck, or investment memo
- A competitor makes a significant move
- Building a positioning strategy
- Evaluating build/buy/partner decisions
- Assessing moat durability

## What It Produces

| Output | Description |
|--------|-------------|
| **7 Powers Heat Map** | Per-competitor scoring with 🟢🟡🔴 ratings and evidence |
| **Switching Cost Matrix** | Decomposed by 7 cost types with visual progress bars |
| **Aggregation Analysis** | Who owns the user relationship, who's being commoditized |
| **Disruption Assessment** | Low-end, new-market, and COAP vectors with detection signals |
| **3 Horizons Threat Map** | Current, adjacent, and paradigm threats |
| **Strategic Recommendations** | Every insight cascaded to "So What" → action → confidence |

## Quick Start

1. Load `SKILL.md` into your AI agent's context
2. Provide: your product, target market, and 3-5 known competitors
3. The skill guides the agent through 7+ frameworks automatically
4. Output: Complete Competitive War Map at consultant or elite tier

## Quality Tiers

| Tier | What You Get |
|------|-------------|
| **Intern** | Feature comparison, SWOT, no evidence tiers |
| **Consultant** | 3-4 frameworks applied, evidence tiered, "So What" cascades, quantified |
| **Elite** | All 7+ frameworks, resource allocation reveals strategy, H3 paradigm analysis, uncommon knowledge, moat erosion detection |

## Scripts (Optional but Recommended)

| Script | Purpose | Dependencies |
|--------|---------|-------------|
| `market_sizing.py` | TAM/SAM/SOM arithmetic | stdlib only |
| `competitive_scorer.py` | 7 Powers scoring matrix with moat durability index | numpy |

```bash
pip install -r requirements.txt
python scripts/market_sizing.py --help
python scripts/competitive_scorer.py --help
```

## Chain Position

```
Problem Framing → Discovery & Research → [THIS SKILL] → Narrative Building → Spec Writing → Outcome Measurement
```

Works best after Problem Framing, but can start standalone with any competitive question.

---

*PM Skills Arsenal v1.0 | Created 2026-02-18 | MIT License*
