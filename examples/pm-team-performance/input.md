# Pipeline Input

## The prompt

> "I have a team of 20 PMs. AI is changing everything about how product work gets done. How do I make this team the best in the industry?"

That's it. Two sentences of context, one question. No org chart, no capability assessment, no budget.

## What happened next

Agent Prime's orchestrator read the input and activated the **Team Strategy** pipeline:

```
Input (2 sentences)
     │
     ▼
┌──────────┐
│  Scout    │ → Scanned research, company blogs, team practice reports
│  (10 min) │   MIT, Stanford, HBS + Stripe, Figma, Linear, Notion
└────┬──────┘
     │ 10 sourced signals with evidence tiers
     ▼
┌──────────────┐
│ Synthesizer  │ → Cross-signal pattern recognition
│  (30 min)    │   "The PM Skill Stack is Inverting" thesis
└────┬─────────┘
     │ Structural thesis + 3 shifts + counter-arguments
     ▼
┌──────────┐
│ Planner  │ → Team Operating System design
│ (45 min) │   4-layer architecture + 3 adoption tiers + rollout plan
└────┬─────┘
     │ Operational blueprint with metrics and quality gates
     ▼
┌──────────┐
│ Builder  │ → Implementation plan
│ (30 min) │   4 phases, specific deliverables, risk register
└──────────┘
```

**Total time:** 3 sessions (~4 hours)
**Total output:** ~30 pages across 4 artifacts
**Human input after the initial prompt:** Review and steering between stages

## What you'd get without Agent Prime

~600 words of generic advice: "Invest in AI tools, train your team, foster a culture of experimentation." No structural thesis, no architectural design, no implementation plan, no quality gates.

See [comparison.md](comparison.md) for the side-by-side.
