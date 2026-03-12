# Raw AI vs Agent Prime: Side-by-Side Comparison

## The Same Question, Two Different Systems

**Prompt:** "I'm the new PM lead for a design tool competing with Canva and Adobe. Build me a complete product strategy."

---

## What Raw AI Produces (~600 words)

Here is a representative response from a frontier AI model with no skill augmentation:

> **Product Strategy for a Design Tool Competing with Canva and Adobe**
>
> To compete with Canva and Adobe in the design tools market, you'll need a clear
> differentiation strategy. Here are the key elements:
>
> **Market Positioning:** Focus on a niche that neither Canva nor Adobe serves well.
> Canva targets casual users while Adobe targets professionals. Consider targeting
> mid-market users -- teams that need more than Canva but find Adobe too complex.
>
> **Key Features to Build:**
> - AI-powered design generation
> - Real-time collaboration
> - Template marketplace
> - Brand management tools
> - Easy export to multiple formats
>
> **Go-to-Market Strategy:** Start with a freemium model. Target small-to-medium
> businesses through content marketing and partnerships. Offer competitive pricing
> below Adobe but above Canva's free tier.
>
> **Metrics to Track:** MAU, paid conversion rate, NPS, time-to-first-design,
> and retention rates.
>
> **Competitive Advantages to Develop:** Focus on speed, AI integration, and
> a better collaboration experience than either competitor.
>
> **Pricing:** Consider a three-tier model -- Free, Pro ($12/mo), and Team ($20/seat/mo).
>
> This should give you a solid foundation for your product strategy. The key is to
> find your unique value proposition and execute quickly before the market shifts.

**Total: ~250 words of advice, 0 frameworks, 0 evidence, 0 actionable specifications.**

---

## What Agent Prime Produces (~2,400 lines across 6 artifacts)

| # | Artifact | Skill Used | What It Contains |
|---|----------|------------|------------------|
| 01 | Problem Framing | problem-framing | Problem Definition Canvas, 5 Whys analysis, JTBD Problem Framing, Opportunity Sizing, Constraint Map -- identifies that the real problem is "which job to own" not "how to beat Canva" |
| 02 | Discovery Research | discovery-research | Evidence Triangulation across earnings calls, user reviews, job postings, product analysis -- surfaces 70+ data points before any framework is applied |
| 03 | Competitive Analysis | competitive-market-analysis | 7 Powers heat map, Switching Cost Decomposition, JTBD mapping, Aggregation Theory, Blue Ocean ERRC grids -- with per-cell evidence tier annotations and O-I-R-C-W cascades |
| 04 | Metric Design | metric-design-experimentation | North Star Metric, Goodhart risk assessment, retention cohort design, HEART scorecard -- metrics built for the specific opportunity identified in stages 1-3 |
| 05 | Specification | specification-writing | Outcome-first spec, acceptance criteria taxonomy, scope boundary map, failure condition design -- zero-ambiguity spec an engineer could build from |
| 06 | Narrative | narrative-building | Narrative arc, positioning framework, Why Now argument, audience adaptation, objection anticipation -- ready for board presentation |

---

## The Contrast Table

| Dimension | Raw AI | Agent Prime |
|-----------|--------|-------------|
| **Output length** | ~250 words | ~2,400 lines (6 artifacts) |
| **Frameworks applied** | 0 | 30+ (7 Powers, JTBD, Aggregation Theory, Blue Ocean, Switching Cost Decomposition, Christensen Disruption, Wardley, NSM, Goodhart, HEART, Retention Cohorts, and more) |
| **Evidence citations** | 0 | 70+ (tier-annotated T1-T6) |
| **Confidence levels** | None ("you should...") | Every claim rated H/M/L with invalidation triggers |
| **Competitive players analyzed** | 2 (Canva, Adobe -- surface level) | 3 primary + 5 secondary + non-obvious competitors, with per-player moat scoring |
| **Switching cost analysis** | None | 6-dimension decomposition (financial, data, workflow, identity, learning, relational) scored 1-10 per player |
| **Jobs-to-be-Done mapping** | Vague ("mid-market users") | Functional + emotional + social jobs mapped per player, with consumption chain and over/under-served analysis |
| **Actionable specifications** | Feature wishlist | Zero-ambiguity spec with acceptance criteria, scope boundaries, and failure conditions |
| **Metrics** | 5 generic KPIs (MAU, NPS...) | North Star Metric designed for the specific opportunity, with Goodhart risk flags and retention cohort methodology |
| **Narrative / positioning** | None | Board-ready narrative with Why Now, audience adaptation, and objection pre-handling |
| **Assumption tracking** | None | 5 load-bearing assumptions with invalidation triggers |
| **Self-critique** | None | 3 adversarial weaknesses identified with evidence that would disprove the analysis |
| **Cross-artifact coherence** | N/A (single response) | Each artifact explicitly references and builds on the previous one |
| **Staleness awareness** | None | Claims >6mo flagged `[POTENTIALLY STALE]`; T6 inferences flagged `[EVIDENCE-LIMITED]` |

---

## What Changes Structurally

### 1. Framing Before Solving

Raw AI jumps straight to "focus on a niche." Agent Prime first asks: *Is competitive differentiation even the right frame?* The Problem Framing stage reveals that the real question is "which job should we own?" -- because Figma, Canva, and Adobe Express serve fundamentally different jobs. "Mid-market positioning" (the raw AI suggestion) would place you in no-man's-land between three entrenched players.

### 2. Evidence Before Opinion

Raw AI says "target small-to-medium businesses." Based on what? Agent Prime's Discovery Research surfaces actual data: Canva has 265M MAU with 8% paid conversion, Figma has 80-90% of UI/UX market share, Adobe Express is a Creative Cloud retention play (not a standalone business). These facts reshape every downstream recommendation.

### 3. Frameworks That Take Positions

Raw AI says "find your unique value proposition." Agent Prime's Competitive Analysis applies 7 Powers scoring and concludes: "Don't attack Figma in UI/UX (4-Power incumbent), don't attack Canva in mass-market templates (265M MAU aggregator), don't attack Adobe Express without owning the Creative Cloud ecosystem. The only contestable space is vertical-specific AI design." That is a position -- falsifiable, with evidence, with watch indicators for when it might be wrong.

### 4. Metrics That Match the Strategy

Raw AI lists "MAU, paid conversion rate, NPS" -- generic KPIs for any SaaS product. Agent Prime's Metric Design builds metrics specifically for the vertical AI design opportunity identified in stages 1-3, with Goodhart risk assessment (how each metric can be gamed) and retention cohort design (how to measure whether the moat is compounding).

### 5. Specifications an Engineer Can Build From

Raw AI lists features: "AI-powered design generation, real-time collaboration, template marketplace." Agent Prime's Specification stage produces acceptance criteria with the AC Taxonomy (functional, quality, edge case, negative), scope boundaries (what is explicitly out), and failure condition design (what happens when the AI generates a bad layout?). An engineering team could estimate and build from this spec without a single clarifying question.

### 6. A Narrative That Sells the Strategy

Raw AI has no narrative output. Agent Prime's Narrative stage produces a board-ready positioning with Why Now (AI-native design is under-served across all three incumbents), audience adaptation (different versions for the board, the engineering team, and potential customers), and pre-handled objections ("Why not just build a better Canva?").

---

## The Core Difference

Raw AI produces **advice**. Agent Prime produces **artifacts**.

Advice is generic, unfalsifiable, and requires the PM to do the actual analytical work. Artifacts are specific, evidence-backed, cross-referenced, and ready to use -- each one feeding the next in a coherent strategic pipeline.

The input was 1 sentence. The output was a complete product strategy across 6 interconnected documents. That is what skills do.
