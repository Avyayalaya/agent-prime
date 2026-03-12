# The Input

## The Prompt

> "I'm the new PM lead for a design tool competing with Canva and Adobe. Build me a complete product strategy."

That's it. One sentence. No frameworks specified. No deliverable format requested. No data provided.

---

## What Agent Prime Did With It

Agent Prime recognized this as a **multi-skill strategic question** -- not a single-artifact request. Instead of producing one long document, it routed the input through a 6-stage pipeline, where each skill's output feeds the next.

### The Pipeline

```
Stage 1: Problem Framing
   "What problem are we actually solving?"
         |
         v
Stage 2: Discovery Research
   "What does the evidence say?"
         |
         v
Stage 3: Competitive Analysis
   "Who are we fighting, and on what dimensions?"
         |
         v
Stage 4: Metric Design
   "How will we measure success?"
         |
         v
Stage 5: Specification Writing
   "What exactly are we building first?"
         |
         v
Stage 6: Narrative Building
   "How do we sell this internally and externally?"
```

### The Numbers

| Metric | Value |
|--------|-------|
| **Input** | 1 sentence (18 words) |
| **Output** | 6 interconnected artifacts |
| **Total lines** | ~2,400 |
| **Frameworks applied** | 30+ (across all 12 skills) |
| **Evidence citations** | 70+ (T1-T4 tier-annotated) |
| **Sessions** | 3 (problem framing + research, competitive + metrics, spec + narrative) |

### Why a Pipeline, Not a Single Document

A raw AI model would produce one 600-word response covering surface-level advice across all six areas. Agent Prime instead:

1. **Frames before solving** -- Problem Framing identifies that the real question is "which job should we own?" not "how do we beat Canva?"
2. **Researches before analyzing** -- Discovery Research surfaces evidence (user reviews, earnings data, job postings) before Competitive Analysis applies frameworks
3. **Analyzes before measuring** -- Competitive Analysis identifies the contestable space; Metric Design builds KPIs for *that specific space*
4. **Specifies before narrating** -- The spec defines what to build; the narrative sells *that specific thing* to stakeholders

Each artifact explicitly references the previous one. The competitive analysis cites discovery research findings. The metric design targets competitive gaps. The specification implements the metric-validated opportunity. The narrative positions the specified product.

---

## How to Reproduce This

```
You: "I'm the new PM lead for a design tool competing with Canva
     and Adobe. Build me a complete product strategy."

Agent Prime routes through:
  1. /problem-framing
  2. /discovery-research
  3. /competitive-market-analysis
  4. /metric-design-experimentation
  5. /specification-writing
  6. /narrative-building
```

The skills are available as a Claude Code plugin: [PM Skills Arsenal](https://github.com/Avyayalaya/pm-skills-arsenal)
