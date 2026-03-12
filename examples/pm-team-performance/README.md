# Example Pipeline: PM Team Performance in the AI Era

> **Input:** 2 sentences.
> **Output:** 4 artifacts, ~30 pages of structural analysis + implementation plan.
> **Time:** 3 sessions (~4 hours). Without the system: months of consulting engagement.

## What this demonstrates

A VP of Product asked a simple question: "How do I make my 20-person PM team the best in the industry?" Agent Prime activated a four-stage pipeline that produced a structural thesis, team architecture, and week-by-week implementation plan — the kind of output that typically requires a management consulting engagement.

## The pipeline

| Stage | Agent | What it produced | Lines |
|-------|-------|-----------------|-------|
| 1 | **Scout** | Signal digest — 10 sourced signals from MIT, Stanford, HBS + Stripe, Figma, Linear, Notion | ~200 |
| 2 | **Synthesizer** | Structural thesis — "The PM Skill Stack is Inverting" with evidence, counter-arguments, self-critique | ~250 |
| 3 | **Planner** | Team Operating System design — 4-layer architecture, 3 adoption tiers, quality gates, metrics | ~300 |
| 4 | **Builder** | Implementation plan — 4 phases, week-by-week deliverables, risk register, Day 1 checklist | ~200 |

## Files in this example

| File | What it is |
|------|-----------|
| [input.md](input.md) | The 2-sentence prompt + pipeline flow diagram |
| [01-scout-signals.md](01-scout-signals.md) | Scout signal digest (10 signals, evidence-tiered) |
| [02-synthesis.md](02-synthesis.md) | Synthesizer thesis: "The PM Skill Stack is Inverting" |
| [03-team-design.md](03-team-design.md) | Planner output: Team Operating System design |
| [04-implementation.md](04-implementation.md) | Builder output: 8-week implementation plan |
| [comparison.md](comparison.md) | Side-by-side: raw AI vs Agent Prime on the same question |

## Key insight the system found

The core thesis — **the PM skill stack is inverting** — emerged from cross-signal synthesis, not from any single source:

1. **Execution skills are commoditizing.** AI makes any PM a competent spec writer, data analyst, and slide creator within 90% of the best human. The MIT and BCG/HBS studies quantify this: 43% faster on execution tasks, 0% better on judgment tasks.

2. **Judgment skills are the new differentiator.** Problem selection, customer empathy, stakeholder navigation, and taste show 10x variance in business outcomes (Stanford HAI, n=1,200). AI cannot replicate these skills. They become the only thing that separates great PMs from adequate ones.

3. **Knowledge compounding is the team-level unlock.** Individual AI usage helps linearly. Team-level knowledge compounding — where every PM's work improves every other PM's AI-assisted output — helps exponentially. Figma, Notion, and Stripe independently arrived at this architecture.

A raw AI response would tell the VP to "invest in AI tools and train the team." The pipeline found a structural thesis, designed an architecture around it, and produced a checklist the VP can hand to their PM lead tomorrow morning.

## How to read the artifacts

**5 minutes:** Read this README + the Executive Summary of [02-synthesis.md](02-synthesis.md). You'll have the core thesis.

**30 minutes:** Add [01-scout-signals.md](01-scout-signals.md) (Cross-Signal Patterns section) + [03-team-design.md](03-team-design.md) (Architecture + Adoption Tiers). You'll have the thesis + how to act on it.

**Full read (2 hours):** All 4 artifacts end-to-end. You'll have a complete, implementation-ready plan for transforming a PM team.

**By role:**
- **VP of Product:** README + Synthesis Executive Summary + Team Design (What Success Looks Like) + Implementation (Week 1 Checklist)
- **PM Lead / Manager:** All 4 artifacts, with focus on Implementation phases and Quality Gates
- **Individual PM:** Synthesis (Skill Stack Framework — plot yourself) + Team Design (Adoption Tiers — find your tier)

## What makes this different from asking ChatGPT

See [comparison.md](comparison.md) for the full side-by-side. The short version:

| Dimension | Raw AI | Agent Prime |
|-----------|--------|-------------|
| Output | ~600 words of advice | ~30 pages across 4 artifacts |
| Structure | List of tips | Thesis → Architecture → Implementation |
| Evidence | None cited | 10 signals, T1-T5, from named sources |
| Actionability | "Train your team on AI" | Week 1 checklist with day-by-day schedule |
| Self-critique | None | 3 counter-arguments + 4 adversarial weaknesses |
| Risks identified | 0 | 7 with mitigations and contingencies |
| Metrics defined | 0 | 13 specific metrics with targets |
| Reusable | No | Yes — architecture is implementable, metrics are trackable |

## Note on methodology

Every claim in the pipeline artifacts is annotated with an evidence tier (T1-T6). The system does not present research findings and practitioner anecdotes at the same confidence level. A peer-reviewed MIT study (T1) is treated differently from a CEO's podcast interview (T4). This evidence discipline is what allows the Synthesizer to build a defensible thesis rather than a collection of anecdotes.

The adversarial self-critique and counter-arguments sections are not performative. They identify genuine weaknesses — including the possibility that the entire thesis is based on survivorship bias from elite tech companies. A VP reading this can decide for themselves whether the evidence generalizes to their org.
