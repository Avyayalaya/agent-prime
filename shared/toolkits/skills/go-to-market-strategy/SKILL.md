---
name: go-to-market-strategy
description: "Use when planning a product launch, market entry, or GTM strategy — segment selection, channel strategy, launch sequencing, pricing validation, competitive positioning, or launch readiness assessment. Encodes wedge identification, channel unit economics, launch gating, and failure criteria. Produces a GTM strategy document, not a launch checklist."
version: "1.0.0"
type: "codex"
tags: ["Strategy", "Launch", "Growth", "Market Entry"]
created: "2026-03-12"
valid_until: "2026-09-12"
derived_from: "original"
tested_with: []
license: "MIT"
capability_summary: "Produces a GTM strategy document with market entry thesis, wedge identification, segment prioritization with ICP scoring, channel strategy with unit economics, launch sequencing with gates and kill criteria, competitive positioning, and success/failure metrics."
input_schema:
  product: "string — product or feature being launched"
  market: "string — target market or category"
  stage: "enum[new_market_entry, existing_market_expansion, feature_launch, pivot] — determines framework depth"
  competitive_context: "string — optional, key competitors and current positioning"
  constraints: "string — optional, budget, timeline, team size, geographic constraints"
  existing_data: "array[string] — optional, any existing research, user interviews, or pilot data"
output_schema:
  executive_summary: "Zero-jargon GTM thesis, ≤300 words"
  market_entry_thesis: "Why this market, why now, what's the wedge"
  segment_selection: "Prioritized segments with ICP scoring and evidence tiers"
  channel_strategy: "Channel selection with unit economics per channel"
  launch_sequence: "Phased plan with gates, kill criteria, and timelines"
  positioning: "Positioning statement, battlecards, competitive differentiation"
  metrics: "Success metrics, failure criteria, review cadence"
  assumption_registry: "Load-bearing assumptions with confidence levels"
  self_critique: "≥3 genuine weaknesses in this strategy"
example_invocation: "examples/USE_CASES.md"
---

## Purpose

Produce an elite-tier go-to-market strategy document that identifies the market wedge, selects and scores beachhead segments, designs channel strategy with unit economics, sequences launch phases with gates and kill criteria, positions against competitors, and defines success metrics with explicit failure conditions — a GTM strategy a PM cannot produce unaided. The output is a GTM Strategy Document — not a launch checklist, but a structural argument for how to win the first customers and compound from there.

## When to Use / When NOT to Use

**Use this skill when:**
- Launching a new product or feature into a market (new or existing)
- Entering a new market with an existing product
- Pivoting an existing product's GTM motion (e.g., sales-led to product-led)
- Evaluating whether a market entry is viable (go/no-go decision)
- Designing channel strategy with unit economics constraints
- Planning launch sequencing with explicit gates and kill criteria
- Assessing launch readiness before committing budget

**Do NOT use this skill when:**
- You need a competitive analysis without a launch plan (use Competitive Market Analysis skill)
- You need a product specification (use Specification Writing skill)
- You need to validate a problem exists before solving it (use Problem Framing skill)
- You need to run experiments to validate assumptions (use Metric Design & Experimentation skill)
- You need a marketing campaign plan (this produces strategy, not execution assets)
- The product is already at scale and you need retention/growth optimization (this is for market entry, not market defense)

**Anti-inputs (what this skill does NOT handle):**
- Marketing copy, email sequences, or campaign assets (downstream of GTM strategy)
- Pricing model design in isolation (pricing is one dimension of channel economics here, not the sole output)
- Organizational design for GTM teams (team structure follows strategy, not the other way around)
- International expansion playbooks (this covers market entry logic; localization is a separate discipline)

---

## Context Gate (Step -1: Is GTM Strategy the Right Artifact?)

Before applying any framework, verify that a GTM strategy document is what the situation actually needs. The most common failure mode is producing an excellent GTM strategy for a product that shouldn't be launched yet.

**Run these checks BEFORE proceeding:**

| Check | Question | If NO → Redirect |
|-------|----------|-------------------|
| **Problem validated?** | Has the problem been validated with ≥5 target users? | → Problem Framing skill first. A GTM strategy for an unvalidated problem is a plan to efficiently deliver something nobody wants. |
| **Product exists or is specced?** | Is there a product, prototype, or detailed spec to launch? | → Specification Writing skill first. GTM without a product is strategy theater. |
| **Market is external?** | Is the target market external customers, not internal adoption? | → For internal rollout (enterprise feature adoption, internal tool deployment), GTM frameworks over-engineer the problem. Use a simpler adoption playbook. |
| **Competitive landscape known?** | Do you know who the alternatives are (including "do nothing")? | → Run Competitive Market Analysis skill first, or do lightweight competitor scan. GTM positioning requires knowing what you're positioning against. |
| **Decision authority exists?** | Is there someone who can act on this GTM strategy? | → If this is exploratory ("should we even consider this market?"), produce a market entry memo instead of a full GTM strategy. |

**If all checks pass:** Proceed to Framework Selection (Step 0).

**If 1-2 checks fail:** Note the gaps explicitly in the output header and proceed with caveats. Flag which sections are hypothetical.

**If 3+ checks fail:** Stop. The right artifact is not a GTM strategy. Recommend the upstream skill.

---

## Reader Navigation

### How to Read This Document

| Time Available | What to Read | What You'll Get |
|---------------|-------------|-----------------|
| **5 minutes** | Executive Summary + Segment Selection table + Failure Criteria table | Go/no-go signal, who to target first, when to stop |
| **15 minutes** | Above + Market Entry Thesis + Channel Strategy + Launch Sequence | Full strategic logic: why this market, how to reach customers, what order |
| **30 minutes** | Full document | Complete GTM strategy with all frameworks, unit economics, positioning, and self-critique |

| Your Role | Start Here | Focus On |
|-----------|-----------|----------|
| **VP/GM** | Executive Summary → Failure Criteria → Assumption Registry | Decision: fund this GTM or not. Kill criteria tell you when to pull the plug. |
| **PM** | Full document, sequentially | You own execution. Every section has specific actions, timelines, and gates. |
| **Marketing Lead** | Positioning section → Channel Strategy → Launch Sequence | Positioning statement, channel selection, launch phases and messaging per phase. |
| **Sales Lead** | Segment Selection → Channel Strategy (direct sales row) → Battlecards | Who to call, what to say, how to handle objections. |
| **Finance/Ops** | Channel Unit Economics → Launch Sequence (budget per phase) → Failure Criteria | CAC, payback period, budget gates, kill thresholds. |

### Notation Key

| Symbol | Meaning |
|--------|---------|
| **H / M / L** | Confidence level: H = >70% confident, M = 40-70%, L = <40% |
| **(T1)-(T6)** | Evidence tier: T1 = behavioral data, T2 = primary research, T3 = expert analysis, T4 = industry reports, T5 = executive statements, T6 = inference |
| **O→I→R→C→W** | Observation → Implication → Response → Confidence → Watch indicator (mandatory cascade for all recommendations) |
| `[POTENTIALLY STALE]` | Claim based on data >6 months old — verify before acting |
| `[EVIDENCE-LIMITED]` | Key conclusion rests on T4-T6 evidence only — validate with T1-T2 before committing budget |
| ████░░░░░░ | Progress bar showing relative strength (1-10 scale) |
| ✅ / ⚠️ / ❌ | Gate passed / gate at risk / gate failed |

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are quality enforcement mechanisms, not style preferences.

1. **Take positions. Never hedge with weasel words.** "Likely," "may," "could," and "seems" are banned from conclusions. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"The beachhead segment is 10-50 person design agencies hitting Figma collaboration limits (H)"* not *"SMBs could be a good target market."*

2. **Per-cell evidence tier annotation is mandatory in all comparison matrices.** Every cell in a segment scoring table, channel economics comparison, or positioning matrix must carry an inline evidence tier tag: `(T1)`, `(T2)`, `(T3)` etc. Where evidence is absent: `(T6: inferred)`. A matrix with untagged cells is incomplete.

3. **The O→I→R→C→W cascade applies to ALL strategic recommendations**, not just final sections. Format: Observation [evidence tier] → Implication [mechanism] → Response [specific action + owner + timeline] → Confidence [H/M/L + assumption] → Watch Indicator [observable signal + threshold].

4. **Begin with Framework Selection (Step 0)** before applying any framework. Identify the stage (new market entry, expansion, feature launch, pivot); select the 3-4 load-bearing frameworks; note which to skip.

5. **Contradictions between frameworks are signal, not noise.** When two frameworks reach different conclusions (e.g., segment scoring says enterprise but channel economics says PLG/SMB), surface the contradiction explicitly and state which to weight more heavily and why.

6. **Flag time-sensitive claims.** Any claim based on data older than 6 months must carry `[POTENTIALLY STALE — verify before presenting]`. Market conditions change faster than competitive positions.

7. **Flag thin-evidence conclusions.** If a key strategic conclusion rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

8. **First reference to any framework includes a one-line explanation.** Not everyone reading a GTM strategy knows what "PLG" or "CAC" or "beachhead" means. Example: *"Product-led growth (PLG) — users adopt the product through self-serve trial before any sales contact."* This makes the document navigable by non-creators.

9. **The Executive Summary uses zero framework jargon.** A VP who has never heard of "beachhead strategy" or "CAC payback period" must be able to read the Executive Summary and make a decision. Framework terms appear in the body, not the summary.

---

## Output Template (Mandatory Document Skeleton)

Every GTM Strategy Document MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was skipped in Step 0, note "Skipped — not load-bearing for this stage" in that section.

```markdown
# GTM Strategy: [Product — e.g., "Vanta Analytics Self-Serve Launch"]

> **Date:** [YYYY-MM-DD] | **Stage:** [new_market_entry / existing_market_expansion / feature_launch / pivot] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which key claims need revalidation]

---

## How to Read This Document

[Reader Navigation table — by time available and by role. See Reader Navigation section above.]

## Notation Key

[Symbol definitions table. See Notation Key above.]

---

## Executive Summary

[≤300 words. Zero jargon. A VP reads only this and decides whether to fund the GTM. Must answer: What are we launching? For whom? Why now? What's the entry point? What does success look like in 6 months? What kills this? Final sentence = the recommended action in bold.]

---

## Step 0: Framework Selection

| Stage | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "New market entry"] | [e.g., Market Entry Thesis, Segment Selection, Channel Strategy] | [e.g., Distribution & Growth Mechanics] | [e.g., "Competitive Positioning — no direct competitors yet"] |

---

## 1. Market Entry Thesis

### Why This Market

[Market selection rationale — size, growth, structural opportunity]

### Why Now (Timing Thesis)

| Timing Signal | Evidence | Confidence |
|--------------|----------|------------|
| [e.g., "Regulatory change creating demand"] | [specific evidence] (TX) | H/M/L |
| [e.g., "Incumbent distracted by platform migration"] | [specific evidence] (TX) | H/M/L |
| [e.g., "Cost curve crossing — AI makes X viable at Y price"] | [specific evidence] (TX) | H/M/L |

### The Wedge

[What is the specific gap in the incumbent's armor? What gives you disproportionate advantage in a specific segment? This is NOT "we're better" — it's "we can win THIS slice because of THIS structural advantage."]

### Wedge Defensibility Assessment

| Dimension | Assessment | Evidence |
|-----------|-----------|----------|
| Time to replicate | [months/years] | (TX) |
| Capital to replicate | [$X] | (TX) |
| Structural barrier | [what prevents copying — counter-positioning, data moat, regulatory, network effects] | (TX) |
| **Verdict** | [Durable moat / Temporary arbitrage / Speed-dependent] | H/M/L |

### Go/Wait/Pivot Decision Table

| Signal | Market Ready | Market NOT Ready |
|--------|-------------|-----------------|
| Product readiness | → **GO**: launch beachhead | → **WAIT**: build MVP, re-assess in [X weeks] |
| Product NOT ready | → **BUILD**: market is ready, accelerate product | → **PIVOT**: wrong market or wrong product |

---

## 2. Segment Selection & Prioritization

### Beachhead Candidates

| Segment | Description | Size (est.) | Evidence |
|---------|------------|-------------|----------|
| [Segment A] | [Specific enough to find 100 prospects by name] | [$ or # users] (TX) | [How you know this segment exists] |
| [Segment B] | [Same specificity] | [$ or #] (TX) | [Evidence] |
| [Segment C] | [Same specificity] | [$ or #] (TX) | [Evidence] |

### ICP Scoring Matrix

| Criterion | Weight | Segment A | Segment B | Segment C |
|-----------|:------:|:---------:|:---------:|:---------:|
| Acute pain (validated) | 25% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| Willingness to pay | 20% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| Accessibility (can you reach them?) | 20% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| Reference-ability (will they tell others?) | 15% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| Expansion potential (leads to adjacent segments?) | 10% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| Competitive vacuum (incumbents weak here?) | 10% | [1-5] (TX) | [1-5] (TX) | [1-5] (TX) |
| **Weighted Score** | | **[X.X]** | **[X.X]** | **[X.X]** |

### Expansion Path

[Beachhead → Adjacent Segment 1 → Adjacent Segment 2 → Mainstream]
[For each transition: what evidence or milestone triggers expansion? What do you carry from the previous segment (references, product features, channel)?]

---

## 3. Channel Strategy with Unit Economics

### Channel Selection Matrix

| Channel | Segment Fit | CAC (est.) | Payback (mo.) | LTV/CAC | Scalability | Evidence |
|---------|:-----------:|:----------:|:-------------:|:-------:|:-----------:|:--------:|
| [Direct sales] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |
| [PLG / self-serve] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |
| [Content/SEO] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |
| [Paid acquisition] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |
| [Partnership/channel] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |
| [Community] | [H/M/L] | [$X] (TX) | [X mo.] (TX) | [X:1] (TX) | [H/M/L] | [source] |

### Primary Channel Deep-Dive

[For the #1 selected channel: full conversion funnel, unit economics at each stage, evidence requirements before scaling budget]

### Channel Sequencing

| Phase | Channel | Budget | Success Criteria to Add Next Channel |
|-------|---------|--------|--------------------------------------|
| Phase 1 | [ONE channel] | [$X] | [Metric ≥ threshold, e.g., "CAC < $200 on 50+ conversions"] |
| Phase 2 | [Add second] | [$X] | [Metric ≥ threshold] |
| Phase 3 | [Add third] | [$X] | [Metric ≥ threshold] |

---

## 4. Launch Sequencing & Gating

### Phase Plan

| Phase | Duration | Audience | Gate Criteria (must ALL be true to proceed) | Kill Criteria (if ANY true, stop) |
|-------|----------|----------|----------------------------------------------|-----------------------------------|
| **Alpha** (internal) | [X weeks] | [Internal team, N users] | [List specific metrics] | [List specific thresholds] |
| **Closed Beta** (design partners) | [X weeks] | [N design partners] | [List specific metrics] | [List specific thresholds] |
| **Open Beta** (waitlist) | [X weeks] | [N users from waitlist] | [List specific metrics] | [List specific thresholds] |
| **GA** (general availability) | [X weeks] | [Target segment] | [List specific metrics] | [List specific thresholds] |
| **Scale** | [Ongoing] | [Expansion segments] | [List specific metrics] | [List specific thresholds] |

### Launch Risk Register

| Risk | Phase | Severity (1-5) | Probability (H/M/L) | Mitigation | Owner |
|------|-------|:--------------:|:--------------------:|------------|-------|
| [Risk 1] | [Phase] | [X] | [H/M/L] | [Specific action] | [Role] |
| [Risk 2] | [Phase] | [X] | [H/M/L] | [Specific action] | [Role] |

---

## 5. Competitive Positioning for Launch

### Positioning Statement

> For **[target customer]** who **[need/job-to-be-done]**, **[product]** is a **[market category]** that **[key benefit]**. Unlike **[primary alternative]**, we **[key differentiator]**.

### Battlecards (per competitor)

**vs. [Competitor A]:**
| They'll Say | You Say | Evidence |
|------------|---------|----------|
| "[Objection 1]" | "[Counter + proof point]" | (TX) |
| "[Objection 2]" | "[Counter + proof point]" | (TX) |

**vs. [Competitor B]:**
[Same structure]

### Positioning Validation Checklist

- [ ] Tested with ≥5 prospects before launch
- [ ] Positioning resonates with target segment (not just internal team)
- [ ] Differentiation is verifiable (not aspirational)
- [ ] Category choice is intentional (creating new vs. entering existing)

---

## 6. Success Metrics & Failure Criteria

### Leading Indicators (weekly review)

| Metric | Target | Goodhart Countermeasure | Antidote Metric |
|--------|--------|------------------------|-----------------|
| [e.g., Activation rate] | [≥X%] | [How it could be gamed] | [What to also watch] |
| [e.g., Time-to-value] | [≤X days] | [How it could be gamed] | [What to also watch] |

### Lagging Indicators (monthly review)

| Metric | Target (6-mo) | Target (12-mo) |
|--------|:-------------:|:--------------:|
| [e.g., Revenue] | [$X] | [$X] |
| [e.g., Retention] | [≥X%] | [≥X%] |

### Failure Criteria (HARD stops — not "reassess")

| Condition | Timeframe | Action |
|-----------|-----------|--------|
| [e.g., "<50 beta signups after 4 weeks of outreach"] | [By date] | **STOP:** [Specific action — pivot, kill, or redesign] |
| [e.g., "CAC >3x target after 100 conversions"] | [By date] | **STOP:** [Specific action] |
| [e.g., "NPS <20 from design partners"] | [By date] | **STOP:** [Specific action] |

### Review Cadence

| Cadence | What's Reviewed | Decision Authority | Escalation |
|---------|----------------|-------------------|------------|
| Weekly | Leading indicators | PM | Flag to VP if 2+ metrics miss for 2+ weeks |
| Monthly | Lagging indicators + gate criteria | PM + VP | Kill/pivot decision if failure criteria met |
| Quarterly | Full GTM strategy review | VP/GM | Strategy re-architecture if market conditions shift |

---

## 7. Distribution & Growth Mechanics

### Growth Model

| Model | Applicability | Evidence | Investment Required |
|-------|:------------:|----------|:-------------------:|
| Viral (user invites user) | [H/M/L/N/A] | [Why or why not] (TX) | [$X] |
| Content (SEO/thought leadership) | [H/M/L/N/A] | [Why or why not] (TX) | [$X] |
| Sales-led | [H/M/L/N/A] | [Why or why not] (TX) | [$X] |
| Product-led (PLG) | [H/M/L/N/A] | [Why or why not] (TX) | [$X] |
| Platform/marketplace | [H/M/L/N/A] | [Why or why not] (TX) | [$X] |

### Flywheel Design

[Which actions create compounding advantages? Draw the loop: More X → More Y → Better Z → More X]

### Reference Customer Strategy

| Slot | Target Profile | Selection Criteria | Storytelling Value |
|:----:|---------------|--------------------|--------------------|
| 1 | [Specific company type] | [Why this customer matters as a reference] | [What story they tell] |
| 2 | [Specific company type] | [Why] | [Story] |
| 3-5 | [Remaining slots] | [Criteria] | [Stories] |

---

## Strategic Recommendations (O→I→R→C→W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see]
- **Implication**: [Why it matters — the mechanism]
- **Response**: [Specific action + owner + timeline]
- **Confidence**: [H/M/L] — assumes [key assumption]
- **Watch**: [Observable signal]; if [threshold], re-assess

**Recommendation 2: [Title]**
[Same structure]

**Recommendation 3: [Title]**
[Same structure]

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---|---|---|---|
| [e.g., "Segment scoring vs. channel economics"] | [Segment A scores highest] | [Channel economics favor Segment B's motion] | [Which matters more and why] |

---

## Assumption Registry

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | | | H/M/L | (TX) | |
| 2 | | | H/M/L | (TX) | |
| 3 | | | H/M/L | (TX) | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[Steelmanned argument against this GTM strategy. What assumption is made? What evidence would disprove it? Scenario where this launch is catastrophically wrong.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| [Observable event — e.g., "Competitor launches competing product"] | [Which sections break] | [When to check] |
| [e.g., "Key assumption invalidated"] | [Which sections break] | [When to check] |

---

## Sources

[All sources cited in the strategy, with evidence tier and date.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Skipped — [reason]" and move on.
2. **Every table cell with a rating, estimate, or claim must have an evidence tier tag** — `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Channel Strategy") with insight headers (e.g., "PLG Is the Only Viable Channel — Direct Sales CAC Is 5x Too High") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **Failure Criteria must be specific and time-bound.** "Revenue is too low" is not a failure criterion. "<$50K ARR after 6 months with ≥$200K GTM spend" is.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology — not merely referenced. A PM using this skill produces a GTM strategy that requires these frameworks; without them, the output degrades to a generic launch plan.

### Framework 1: Market Entry Thesis

The structural argument for why this market, why now, and what gives you a disproportionate right to win a specific slice. Without a market entry thesis, a GTM strategy is a plan to spend money without a theory of why it will work.

**The Three Pillars:**

| Pillar | Question | What "Good" Looks Like | What "Bad" Looks Like |
|--------|----------|------------------------|-----------------------|
| **Why This Market** | Is there a structural opportunity, not just a large TAM? | "Regulatory change X creates $Y of newly addressable demand in segment Z" | "The market is $50B and growing" |
| **Why Now** | What timing signal makes this the right moment? | "Incumbent is mid-platform migration; 18-month window before they stabilize" | "AI is changing everything" |
| **What's the Wedge** | Where is the gap in the incumbent's armor? | "Design agencies with 15+ Figma users hit collaboration limits the incumbent can't fix without re-architecting" | "Our product is better" |

**Timing Thesis — The Four Forces:**

| Force | Signal | Example | Evidence Tier Needed |
|-------|--------|---------|---------------------|
| **Technology shift** | New capability makes previously impossible product viable at target price | "LLM costs dropped 90% in 12 months — AI-native analytics now viable at $50/user/mo" | T1-T2 (cost data, product benchmarks) |
| **Regulatory change** | New rules create demand or remove barriers | "GDPR created demand for privacy-first analytics; EU AI Act will do the same for explainable AI" | T1 (regulatory text, enforcement timeline) |
| **Behavior change** | User expectations shifted by adjacent products | "Users now expect natural language interfaces after ChatGPT — SQL-based tools feel broken" | T2-T3 (user research, adoption data) |
| **Cost curve crossing** | Economics that didn't work now work | "Cloud compute at $X means we can offer real-time analytics at SMB pricing" | T1 (pricing data, unit economics model) |

**Decision Table — Should We Enter?**

| Market Ready? | Product Ready? | Decision |
|:------------:|:--------------:|----------|
| ✅ Yes | ✅ Yes | **GO** — launch into beachhead segment |
| ✅ Yes | ❌ No | **BUILD** — market window is open; accelerate product; set deadline |
| ❌ No | ✅ Yes | **WAIT** — monitor timing signals; re-assess in [X weeks] |
| ❌ No | ❌ No | **PIVOT** — wrong market or wrong product; return to Problem Framing |

**Wedge Identification Method:**

A wedge is not "our product is better." A wedge is a structural advantage in a specific segment that incumbents cannot easily replicate. The wedge is what gets you the first 10 customers without competing on brand, distribution, or scale — advantages you don't have yet.

| Wedge Type | Mechanism | Example | Durability |
|-----------|-----------|---------|-----------|
| **Counter-positioning** | Incumbent can't copy you without cannibalizing their core | Canva vs. Adobe: self-serve design threatens Adobe's enterprise sales motion | High — structural |
| **Underserved segment** | Incumbent ignores a segment because it's too small or too different | Notion serving individual knowledge workers while Confluence focuses on enterprise IT | Medium — until segment grows large enough to attract attention |
| **Technology discontinuity** | New technology enables 10x better/cheaper solution in a niche | AI-native code review replacing manual reviewer workflows | Medium — until incumbents adopt the same technology |
| **Distribution advantage** | You can reach the segment cheaper than incumbents | Built-in marketplace distribution (Shopify apps, Salesforce AppExchange) | Low-Medium — marketplace rules change |
| **Regulatory arbitrage** | New regulation creates requirements incumbents aren't built to meet | GDPR-compliant analytics when incumbents are built on data collection | Medium — until incumbents adapt |

**Anti-pattern: "Large TAM Therefore Enter"**

The sentence "The market is $50B so even 1% = $500M" contains zero strategic content. It doesn't explain:
- Why you can capture any share at all
- Which segment of the TAM is accessible to you
- What your wedge is against players who already have distribution, brand, and scale
- Why now rather than 2 years ago or 2 years from now

If your market entry thesis is "big market + good product = success," you don't have a market entry thesis. You have a hope.

---

### Framework 2: Segment Selection & Prioritization

The single most consequential GTM decision: who to target first. Get this wrong and everything downstream fails — wrong channels, wrong messaging, wrong product priorities. A beachhead segment (the first market niche you dominate completely before expanding) must be specific enough to find 100 prospects by name.

**Segment Definition Rules:**

| Rule | Bad Example | Good Example | Why |
|------|-----------|-------------|-----|
| **Name 100 prospects** | "SMBs" | "10-50 person design agencies using Figma who hit collaboration limits at 15+ users" | If you can't name 100 companies that fit the definition, the segment is too vague to target |
| **Observable behavior** | "Companies that need better analytics" | "Companies posting Looker admin job postings while complaining about LookML complexity on forums" | Behavior is targetable; need-states are not |
| **Willingness to pay** | "Price-sensitive small businesses" | "Design agencies paying $15+/user/mo for Figma who would pay $10/user/mo for a collaboration add-on" | Willingness to pay must be specific enough to model unit economics |
| **Reachable** | "Enterprise companies globally" | "US-based mid-market SaaS companies whose Head of Data attends dbt community events" | You need a channel to actually reach these people |

**ICP Scoring Rubric:**

| Criterion | Weight | Score 5 | Score 3 | Score 1 |
|-----------|:------:|---------|---------|---------|
| **Acute pain** | 25% | Validated with ≥5 interviews; customers actively seeking solutions | Some evidence of pain from secondary sources | Assumed pain; no direct validation |
| **Willingness to pay** | 20% | Customers have budget allocated; comparable products exist at target price | Budget exists but not allocated; price sensitivity unclear | No evidence of willingness to pay |
| **Accessibility** | 20% | Clear channel exists; can reach 80%+ of segment through 1-2 channels | Reachable through 3+ channels, none dominant | No clear way to reach the segment efficiently |
| **Reference-ability** | 15% | Segment is vocal (conference speakers, bloggers, community participants) | Moderately connected; will provide references if asked | Private; won't be public references |
| **Expansion potential** | 10% | Adjacent segments are 5x+ larger and share buying criteria | Adjacent segments exist but different buying criteria | Dead-end segment; no expansion path |
| **Competitive vacuum** | 10% | No incumbent actively serving this segment | Incumbent serves it poorly; opportunity to displace | Strong incumbent with high switching costs |

**Decision Table — Beachhead Selection:**

| Weighted Score | Decision |
|:--------------:|----------|
| ≥4.0 | **Strong beachhead** — proceed to channel strategy |
| 3.0-3.9 | **Viable but risky** — validate the weakest scoring criterion before committing |
| <3.0 | **Weak beachhead** — find a better segment or return to Problem Framing |

**Expansion Path — Crossing the Chasm Connection:**

The beachhead is not the destination. It's the first pin in the bowling alley (Geoffrey Moore's metaphor for sequential niche domination that builds to mainstream adoption). Each segment transition must be planned:

| Transition | Trigger to Expand | What Carries Over | What Changes |
|-----------|-------------------|-------------------|--------------|
| Beachhead → Adjacent 1 | [Metric threshold — e.g., "50%+ share in beachhead, ≥10 references"] | [Product features, brand in adjacent community] | [Messaging, channel mix, possibly pricing] |
| Adjacent 1 → Adjacent 2 | [Next metric threshold] | [Broader product, more references] | [New channel, enterprise motion?] |
| Adjacent 2 → Mainstream | [Market pull — inbound exceeds outbound] | [Brand, product maturity, reference library] | [Everything — this is the chasm crossing] |

---

### Framework 3: Channel Strategy with Unit Economics

Channels are not "marketing tactics." Channels are the economic engine of your GTM. A channel that doesn't have viable unit economics is a way to lose money efficiently.

**Channel Taxonomy with Fit Indicators:**

| Channel | Best For | Worst For | Typical CAC Range | Time to Signal |
|---------|---------|-----------|:------------------:|:--------------:|
| **Direct sales** | Enterprise ($50K+ ACV), complex products, relationship-driven | SMB, self-serve products, price-sensitive segments | $5K-$50K | 3-6 months |
| **PLG (product-led growth)** | SMB, developer tools, prosumer products, low ACV with high volume | Enterprise (long sales cycles), regulated industries | $50-$500 | 1-3 months |
| **Content/SEO** | Considered purchases, educational buyers, long sales cycles | Impulse purchases, time-sensitive launches | $100-$2K | 6-18 months |
| **Paid acquisition** | Proven unit economics to scale, retargeting, brand awareness | Unproven products (too expensive to learn via paid), low-LTV products | $200-$5K | 1-4 weeks |
| **Partnership/channel** | Established ecosystems, marketplace distribution, co-selling | Products without clear partner value prop, early-stage products | $500-$5K | 3-12 months |
| **Community** | Developer tools, PLG products, identity-driven products | Enterprise B2B, transactional products | $200-$2K | 6-18 months |
| **Outbound** | Mid-market, defined ICP, products with clear ROI story | Mass-market consumer, products without clear buyer persona | $1K-$10K | 1-3 months |
| **Events/conferences** | Enterprise, relationship-driven sales, brand-building in niche | Broad consumer, low ACV, early-stage products without demo-ready product | $2K-$20K | 1-6 months |

**Per-Channel Unit Economics Template:**

For the primary channel, calculate:

```
Awareness → Interest → Trial/Demo → Activation → Paid Conversion → Retention → Expansion

Funnel Stage          | Volume    | Conversion | Cost/Stage  | Cumulative CAC
─────────────────────────────────────────────────────────────────────────────
Awareness (impressions)| [X]      | [X%]       | $[X]       | $[X]
Interest (clicks/signups)| [X]   | [X%]       | $[X]       | $[X]
Trial/Demo            | [X]      | [X%]       | $[X]       | $[X]
Activation            | [X]      | [X%]       | $[X]       | $[X]
Paid conversion       | [X]      | [X%]       | $[X]       | $[X] ← This is your CAC
─────────────────────────────────────────────────────────────────────────────
Payback period: [X months] = CAC / (Monthly revenue per customer)
LTV/CAC: [X:1] = (ARPU × Avg. lifetime months × Gross margin) / CAC
```

**Minimum Viable Channel Rule:**

Start with ONE channel. Prove it works (positive unit economics on ≥50 conversions). Then add a second. Multi-channel from day 1 is a failure mode — you learn nothing because no channel gets enough investment to produce statistically meaningful signal.

| Channel Count | Stage | Criteria |
|:------------:|-------|----------|
| 1 | Launch → Product-market fit | Primary channel producing repeatable conversions |
| 2 | Growth | Primary channel proven; second channel shows early positive signal |
| 3+ | Scale | First two channels have positive unit economics at scale |

**Evidence Requirements Before Scaling:**

| Evidence Level | What It Means | Budget Implication |
|:-------------:|--------------|-------------------|
| **Hypothesis** (no data) | You think this channel will work based on analogy or logic | $0 — don't spend until you have signal |
| **Signal** (<50 conversions) | Early data suggests viability but sample size is too small | Cap at 10% of GTM budget |
| **Proof** (50-200 conversions) | Unit economics are clear; conversion funnel is mapped | Scale to 30% of GTM budget |
| **Proven** (200+ conversions) | Repeatable, predictable, scalable | Unlimited (within LTV/CAC constraints) |

---

### Framework 4: Launch Sequencing & Gating

Every launch has phases. Every phase has gates. Every gate has kill criteria. A launch without gates is a launch without learning — you'll discover problems at GA that should have been caught in beta.

**Phase Taxonomy:**

| Phase | Purpose | Audience | Duration | What You Learn |
|-------|---------|----------|----------|----------------|
| **Alpha** | Internal validation | Internal team (10-50 users) | 2-4 weeks | Major bugs, UX failures, performance issues |
| **Closed Beta** | Design partner validation | 5-20 hand-picked customers | 4-8 weeks | Product-market fit signal, activation flow, early retention |
| **Open Beta** | Broader validation | 50-500 from waitlist | 4-8 weeks | Channel viability, support load, pricing validation |
| **GA** | Market launch | Target segment | Ongoing | Growth rate, unit economics, competitive response |
| **Scale** | Expansion | Adjacent segments | Ongoing | Cross-segment fit, channel economics at scale |

**Gate Criteria Rubric:**

Each phase transition requires ALL gates to pass. If any gate fails, you stay in the current phase, fix the issue, and re-evaluate.

| Gate Category | Alpha → Beta | Beta → Open Beta | Open Beta → GA | GA → Scale |
|--------------|:---:|:---:|:---:|:---:|
| **Usage** | ≥X DAU/WAU ratio | ≥X activation rate | ≥X retention (day 30) | ≥X retention (day 90) |
| **Satisfaction** | No P0 bugs open | NPS ≥X from design partners | NPS ≥X from open beta | NPS ≥X from GA cohort |
| **Economics** | N/A | Design partners willing to pay | CAC < $X on ≥50 conversions | LTV/CAC ≥ 3:1 |
| **Support** | <X tickets/user/week | <X tickets/user/week | Support scalable (self-serve ≥80%) | Support cost < X% of revenue |
| **Positioning** | N/A | Positioning tested with ≥5 prospects | Win rate ≥X% vs. primary alternative | Win rate stable or improving |

**Kill Criteria — Hard Stops:**

Kill criteria are not "reassess" criteria. They are specific, time-bound conditions that mean "stop spending money on this GTM." The purpose of kill criteria is to prevent sunk cost escalation — continuing a failing launch because you've already invested.

| Kill Signal | Threshold | What It Means | Action |
|-------------|-----------|--------------|--------|
| Zero activation | <5% of beta users complete core action after 30 days | Product doesn't deliver value quickly enough, or value prop is wrong | Kill or pivot product, not GTM |
| No willingness to pay | <10% of beta users willing to pay any amount | Product is useful but not valuable enough to pay for | Re-examine pricing or pivot to different monetization |
| CAC death spiral | CAC > LTV after 100+ conversions | Channel economics are fundamentally broken | Kill channel, try different channel, or reduce CAC via product improvement |
| Competitive wipeout | Primary competitor matches your wedge within beta period | Wedge was speed-dependent and you lost the race | Pivot to different wedge or different segment |

**Minimum Viable Launch (MVL):**

The MVL is the smallest launch that produces learning, not the biggest launch you can afford. The purpose of each phase is to answer a specific question:

| Phase | Question It Answers | MVL Size |
|-------|--------------------|---------:|
| Alpha | Does the product work? | 10-50 internal users |
| Beta | Do target customers want this? | 5-20 design partners |
| Open Beta | Can we acquire customers through our primary channel? | 50-200 users via primary channel |
| GA | Do unit economics work at scale? | 200+ customers |

---

### Framework 5: Competitive Positioning for Launch

Positioning is not messaging. Positioning is the strategic decision about what mental real estate you occupy in the buyer's mind relative to alternatives. Messaging is how you communicate that position. Get positioning wrong and no amount of brilliant messaging will fix it.

**April Dunford's Positioning Framework (adapted for GTM):**

| Element | Question | Output |
|---------|----------|--------|
| **Competitive alternatives** | What would customers use if your product didn't exist? (Include "do nothing" and "manual workaround") | List of 3-5 real alternatives |
| **Unique attributes** | What do you have that alternatives don't? (Be specific — "AI-powered" is not unique in 2026) | 2-3 genuinely differentiated capabilities |
| **Value for customer** | What does your unique capability enable the customer to do? (Customer language, not product language) | Value statement in customer's words |
| **Target customer** | Who cares most about this value? (This should match your beachhead segment) | Specific ICP definition |
| **Market category** | What frame of reference helps the customer understand what you are? | Category name — existing or new |

**Positioning Statement Template:**

> For **[target customer with specific pain]** who **[currently do X with Y limitations]**, **[product]** is a **[market category]** that **[delivers specific value]**. Unlike **[primary competitive alternative]**, **[product]** **[key differentiator that matters to this segment]**.

**Positioning Validation:**

Test positioning with ≥5 prospects from the target segment BEFORE launch. Iterate based on:

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Prospect immediately understands what you do | Category choice is correct | Proceed |
| Prospect says "oh, like [competitor]?" correctly | Positioning is clear relative to alternatives | Proceed |
| Prospect says "oh, like [wrong category]?" | Category choice is wrong | Reframe the category |
| Prospect doesn't understand why they'd switch from current solution | Value for customer is unclear or insufficient | Sharpen the differentiation |
| Prospect says "that's interesting but not for us" | Target customer is wrong, or you're talking to wrong person | Check segment selection |

**Battlecard Structure:**

For each primary competitor, build a battlecard that sales and marketing can use:

| Section | Content |
|---------|---------|
| **Quick take** | 2-sentence summary of how we win against this competitor |
| **Their pitch** | What they'll say about themselves (and what's true vs. marketing) |
| **Our wedge** | Where we're structurally better for this segment specifically |
| **Their attack** | What they'll say about us (and the honest counter) |
| **Landmines** | Topics to avoid because the competitor genuinely wins on them |
| **Proof points** | Customer quotes, data points, or demos that close the deal against this competitor |

**Anti-pattern: Positioning Against Yourself**

A common failure: comparing your new product to your OLD product or your internal status quo. Your customer doesn't care about your internal journey. They care about the competitive alternatives they're evaluating TODAY. Position against the alternative they'd choose if you didn't exist — which might be a competitor, a manual process, or doing nothing.

---

### Framework 6: Success Metrics & Failure Criteria

Metrics without failure criteria are vanity metrics. If you don't define the conditions under which you'd stop, you'll never stop — even when the GTM is failing. This framework encodes Goodhart's Law countermeasures into every metric (when a measure becomes a target, it ceases to be a good measure).

**Leading Indicators (review weekly):**

| Metric | What It Measures | Goodhart Risk | Antidote Metric |
|--------|-----------------|---------------|-----------------|
| **Activation rate** | % of signups who complete core action within X days | Team optimizes onboarding to count trivial actions as "activated" | Time-to-value (are activated users actually getting value?) |
| **Time-to-value** | Days from signup to first "aha moment" | Team removes friction without ensuring comprehension | Day-30 retention (did they come back?) |
| **Referral rate** | % of users who refer another user | Incentivize referrals with discounts → low-quality referred users | Referred user activation rate (are referrals actually good users?) |
| **Conversion rate** | % of free/trial users who become paid | Lower price to boost conversion → revenue per customer drops | Revenue per customer + LTV |
| **Pipeline velocity** | Average days from first touch to closed deal | Sales rushes deals → lower deal quality → higher churn | 90-day retention of closed deals |

**Lagging Indicators (review monthly):**

| Metric | Formula | Benchmark (varies by category) |
|--------|---------|-------------------------------|
| **Revenue** | MRR or ARR | [Target based on segment size and pricing] |
| **Market share** | Your revenue / Total segment revenue | Meaningful only after GA; track trend, not absolute |
| **Retention** | % of customers still active after X months | SaaS benchmark: >85% annual gross retention |
| **NPS** | Promoters - Detractors (as % of respondents) | >40 = strong; >60 = exceptional |
| **LTV/CAC** | Lifetime value / Customer acquisition cost | ≥3:1 for sustainable growth; ≥5:1 for venture-scale |

**Failure Criteria Design:**

Every failure criterion must pass the "SMART-K" test:

| Element | Requirement | Bad Example | Good Example |
|---------|-------------|-------------|-------------|
| **S**pecific | Names the exact metric | "Engagement is low" | "DAU/MAU < 15%" |
| **M**easurable | Can be pulled from a dashboard | "Users don't like the product" | "NPS < 10 from beta cohort" |
| **A**ctionable | Leads to a specific decision | "Reassess the strategy" | "Kill the self-serve channel; pivot to direct sales or kill GTM entirely" |
| **R**ealistic threshold | Not so high you always fail, not so low you never trigger | "<$1M ARR after 30 days" | "<$50K ARR after 6 months with ≥$200K GTM spend" |
| **T**ime-bound | Has a deadline | "Revenue isn't growing" | "MoM revenue growth <10% for 3 consecutive months after GA" |
| **K**ill-linked | Specifies what stops if triggered | "We need to think about this" | "STOP: no new channel investment; redirect team to [alternative]" |

**Review Cadence Design:**

| Cadence | Metrics | Decision Authority | Key Question |
|---------|---------|-------------------|-------------|
| **Weekly** (PM-led) | Activation, time-to-value, pipeline, conversion funnel | PM decides tactical adjustments | "Are we on track to hit this phase's gate criteria?" |
| **Monthly** (VP-level) | Revenue, retention, CAC, LTV/CAC, NPS | VP decides phase transitions and budget | "Should we proceed to next phase or stop?" |
| **Quarterly** (GM/Exec) | Market share, competitive position, GTM ROI | GM decides strategy-level changes | "Is this GTM fundamentally working?" |

---

### Framework 7: Distribution & Growth Mechanics

How the product spreads after initial launch. Distribution is not a post-launch afterthought — the growth model must be designed into the product and GTM from day 1.

**Growth Model Taxonomy:**

| Model | Mechanism | When It Works | When It Fails | Product Requirements |
|-------|-----------|--------------|---------------|---------------------|
| **Viral** | User invites user (inherent to product usage) | Collaborative products, communication tools, network-effect products | Single-player products, enterprise tools, regulated industries | Built-in sharing/invite flow, value increases with more users |
| **Content** | SEO, thought leadership, educational content | Considered purchases, long sales cycles, "how to" searches | Impulse purchases, products with no educational angle | Content team, 6-18 month investment horizon |
| **Sales-led** | Outbound sales, demos, relationship building | Enterprise, high ACV, complex products, regulated industries | SMB, low ACV, self-serve expectations | Sales team, CRM, demo environment |
| **Product-led (PLG)** | Free trial/freemium → paid conversion | Developer tools, prosumer products, products with fast time-to-value | Products requiring implementation, long time-to-value | Self-serve onboarding, usage-based or freemium pricing |
| **Platform/marketplace** | Distribution through existing platform (Shopify, Salesforce, etc.) | Products that enhance existing platforms, niche integrations | Standalone products, products competing with platform features | API integration, marketplace listing, platform compliance |

**Network Effects Assessment:**

| Question | If Yes | If No |
|----------|--------|-------|
| Does usage by one user make the product more valuable for others? | Genuine network effect — invest heavily in user acquisition | Not a network effect — don't confuse with scale economies |
| Can the effect be achieved at small scale (5-50 users)? | Local network effects — viable for beachhead | Requires critical mass — risky for early launch |
| Do users need to be in the same organization or can they be independent? | Same-side network effect — expansion within accounts | Cross-network effect — requires broader adoption |
| Can users get value from the product alone? | Network effect is additive (good) | Network effect is prerequisite (risky — chicken-and-egg) |

**Flywheel Design Method:**

Every sustainable growth engine has a flywheel — a self-reinforcing loop where the output of one stage feeds the input of another. Design yours explicitly:

```
[User action A] → produces [Asset B] → attracts [New users C] → increases [Value D] → drives more [User action A]

Example (Figma):
Designer creates in Figma → Shares design link with stakeholders → Stakeholders see Figma in action → Request Figma for their team → More designers create in Figma
```

**Flywheel Strength Assessment:**

| Dimension | Score 1 (Weak) | Score 3 (Moderate) | Score 5 (Strong) |
|-----------|----------------|-------------------|------------------|
| **Automaticity** | Requires deliberate user effort to trigger | Semi-automatic (sharing is natural but not required) | Fully automatic (product usage inherently creates distribution) |
| **Speed** | Takes months per cycle | Weeks per cycle | Days or real-time |
| **Compounding** | Linear growth per cycle | Modest compounding | Strong compounding (each cycle is larger than the last) |
| **Defensibility** | Easy to replicate | Requires data or network to replicate | Data + network + community moat |

**Reference Customer Strategy:**

The first 5-10 customers must be selected for storytelling value, not just revenue. These customers are the proof points that unlock the next 100 customers.

| Selection Criterion | Why It Matters |
|--------------------|---------------|
| **Recognizable brand in segment** | "If [Brand X] uses it, it must be good" — reduces perceived risk for prospects |
| **Vocal about tools/process** | They'll speak at conferences, write blog posts, share on social |
| **Acute pain + measurable outcome** | You need a before/after story with numbers, not a vague endorsement |
| **Adjacent to next segment** | Their endorsement should carry weight in the segment you expand to next |
| **Willing to be named** | Anonymous references have 80% less impact than named ones |

---

## Evidence Standards

### Evidence Quality Tiers

| Tier | Source Type | Weight | Example |
|------|-----------|--------|---------|
| **Tier 1** | Direct behavioral data (what people DO) | Highest | Usage analytics, conversion data, revenue, app store data, beta metrics |
| **Tier 2** | Primary research, credible methodology | High | Customer interviews (≥5), well-sampled surveys, usability tests |
| **Tier 3** | Expert analysis with disclosed reasoning | Medium-High | Industry analysts with methodology, experienced GTM operators with data |
| **Tier 4** | Industry reports from reputable firms | Medium | Gartner, IDC, Forrester (useful for market sizing, less for GTM tactics) |
| **Tier 5** | Executive statements and analogies | Low-Medium | "Slack did this" — analyze for strategic signaling, not as GTM evidence |
| **Tier 6** | Inference and analogy | Low | "Companies like ours typically..." — hypothesis generation only |

**Triangulation Rule:** No GTM decision (segment selection, channel choice, pricing) rests on a single evidence tier. Minimum 2 tiers, ideally 3.

**Annotation Convention:** Inline tags throughout — `(T1: beta conversion data)` or `(T5: competitor CEO interview)` or `(T6: inferred from analogous company)`. Per-cell annotation in all matrices.

---

## Application Method

### Step 0: Route to Framework Subset (Do This First)

Identify the launch stage and select load-bearing frameworks. Applying all 7 frameworks to a simple feature launch is overkill; applying only 3 to a new market entry is dangerous.

| Launch Stage | Prompt Signals | Primary Frameworks | Supporting | Skip |
|---|---|---|---|---|
| **New market entry** | "entering a new market", "no existing customers in this space", "greenfield" | Market Entry Thesis, Segment Selection, Channel Strategy, Launch Gating | Competitive Positioning, Metrics & Failure Criteria | Distribution Mechanics (premature until initial traction) |
| **Existing market expansion** | "new segment", "adjacent market", "upsell motion" | Segment Selection, Channel Strategy, Competitive Positioning | Launch Gating, Metrics | Market Entry Thesis (market is known), Distribution (refine existing) |
| **Feature launch** | "new feature", "product update", "GA of capability" | Launch Gating, Metrics & Failure Criteria, Competitive Positioning | Channel Strategy (existing channels, new tactics) | Market Entry Thesis, Segment Selection (already known) |
| **Pivot** | "changing direction", "GTM isn't working", "new motion" | Market Entry Thesis, Segment Selection, Channel Strategy | All others | None — a pivot needs full re-evaluation |

### Quick Version (8 steps for experienced practitioners)

0. **Route to framework subset** — Identify launch stage from the table above. Select 3-4 primary frameworks.
1. **Build the Market Entry Thesis** — Why this market, why now, what's the wedge. Complete the Go/Wait/Pivot decision table.
2. **Select and score segments** — Define 3+ candidate beachheads with ICP scoring. Choose the highest-scoring segment. Map the expansion path.
3. **Design channel strategy** — Select ONE primary channel with full unit economics. Define evidence thresholds for adding channels.
4. **Sequence the launch** — Alpha → Beta → Open Beta → GA → Scale. Set gate criteria and kill criteria per phase.
5. **Position against alternatives** — Dunford positioning framework. Build battlecards for top 2-3 competitors. Test with ≥5 prospects.
6. **Define metrics + failure criteria** — Leading (weekly) and lagging (monthly) indicators. Hard kill criteria that are SMART-K.
7. **Design the growth engine** — Growth model selection, flywheel design, reference customer strategy.
8. **Cascade every recommendation to O→I→R→C→W** — Observation → Implication → Response → Confidence → Watch indicator.

### Full Version (detailed steps with decision points)

**Step 1: Build the Market Entry Thesis**

The market entry thesis is the foundation. Everything else — segments, channels, positioning — depends on the structural argument for why this market, why now, and what's the wedge.

1. **Why this market:** Identify the structural opportunity. Not "big market" but "specific structural change creating X opportunity in Y segment." Use the Timing Thesis Four Forces table.
2. **Why now:** At least one timing signal must be present and supported by T1-T3 evidence. If no timing signal exists, question whether "now" is the right time — maybe you should wait.
3. **What's the wedge:** Identify the structural advantage using the Wedge Identification Method. The wedge must be specific to a segment, not a generic product superiority claim.
4. **Defensibility check:** Complete the Wedge Defensibility Assessment table. If the verdict is "Temporary arbitrage," acknowledge it — your GTM must be fast enough to build durable advantages before the arbitrage closes.

**Decision point:** Complete the Go/Wait/Pivot decision table. If the answer is not "GO," stop. The rest of the GTM strategy is premature.

**Step 2: Select and Score Segments**

1. Define 3+ candidate beachhead segments using the Segment Definition Rules. Each must pass the "name 100 prospects" test.
2. Score each segment using the ICP Scoring Matrix with evidence tiers per cell.
3. Select the highest-scoring segment as your beachhead. If two segments score within 0.5 points, choose the one with higher accessibility (easier to reach = faster learning).
4. Map the expansion path: beachhead → adjacent 1 → adjacent 2 → mainstream.

**Decision point:** If no segment scores ≥3.0, return to Problem Framing. Your product may not have a viable beachhead.

**Step 3: Design Channel Strategy**

1. For the selected beachhead segment, evaluate all channels using the Channel Selection Matrix.
2. Select ONE primary channel based on segment fit + unit economics viability.
3. Build the full conversion funnel for the primary channel with cost-per-stage estimates.
4. Calculate CAC, payback period, and LTV/CAC ratio.
5. Define evidence thresholds for adding a second channel.

**Decision point:** If no channel has estimated LTV/CAC ≥ 2:1, the unit economics may not work. Before proceeding, validate pricing (can you charge more?) or product costs (can you deliver cheaper?).

**Step 4: Sequence the Launch**

1. Define phases from the Phase Taxonomy.
2. Set specific gate criteria per phase using the Gate Criteria Rubric.
3. Set hard kill criteria per phase using the Kill Criteria framework.
4. Set time limits per phase — every phase has a deadline, not just success criteria.
5. Assign ownership for each gate review.

**Decision point:** If kill criteria trigger during any phase, execute the specified action. Do not negotiate with kill criteria — that's what they're for.

**Step 5: Position Against Alternatives**

1. Apply April Dunford's positioning framework to define competitive alternatives, unique attributes, value, target customer, and market category.
2. Write the positioning statement.
3. Build battlecards for the top 2-3 competitive alternatives (including "do nothing" if relevant).
4. Test positioning with ≥5 prospects from the target segment. Iterate based on the Positioning Validation signals.

**Decision point:** If positioning doesn't resonate after testing with 5+ prospects, the problem is likely segment selection (wrong audience) or wedge definition (insufficient differentiation), not messaging.

**Step 6: Define Metrics & Failure Criteria**

1. Select 3-5 leading indicators from the Leading Indicators table. For each, define the Goodhart countermeasure and antidote metric.
2. Select 3-5 lagging indicators. Set 6-month and 12-month targets.
3. Define ≥3 hard failure criteria using the SMART-K framework.
4. Design the review cadence: weekly (PM), monthly (VP), quarterly (GM).

**Step 7: Design the Growth Engine**

1. Assess each growth model from the taxonomy for applicability to your product and segment.
2. Design the flywheel explicitly. Diagram the self-reinforcing loop.
3. Score flywheel strength on the four dimensions (automaticity, speed, compounding, defensibility).
4. Select 5-10 target reference customers using the selection criteria.

**Step 8: Cascade to Recommendations**

For every major finding, apply the O→I→R→C→W cascade:

```
OBSERVATION [evidence tier] → IMPLICATION [mechanism] → RESPONSE [specific action + owner + timeline] → CONFIDENCE [H/M/L + key assumption] → WATCH INDICATOR [observable signal; if threshold crossed, re-assess]
```

**Bad:** "We should target design agencies through content marketing."

**Elite:** "Design agencies with 15+ Figma users spend $200+/mo on collaboration tools [T2: 8 customer interviews], creating a $12K+ ACV opportunity in a segment with <$500 CAC via targeted Figma community content [T6: estimated from analogous community channels]. Response: hire one content marketer focused exclusively on Figma community content — estimated 3-month payback at 5 conversions/month [owner: Head of Marketing, timeline: start within 2 weeks]. Confidence: M — assumes Figma community allows vendor content without backlash [check community guidelines before starting]. Watch: community engagement rate on first 3 posts; if <2% engagement or community pushback, pivot to partnership channel instead."

### Mandatory Output: Assumption Registry

Every GTM strategy must end with a standalone assumption registry. List every load-bearing assumption:

| Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|
| [e.g., "Design agencies will pay $10/user/mo for collaboration features"] | Segment Selection, Channel Economics | M | 8 interviews said "probably" | ≤2 of first 20 beta users convert to paid |
| [e.g., "Figma community content can produce $500 CAC"] | Channel Strategy | L | Analogous to dbt community results | CAC > $1,500 after 50 conversions |
| [e.g., "Primary competitor won't launch competing feature for 12+ months"] | Market Entry Thesis (timing) | M | No job postings, no patent filings | Competitor announces competing feature |

Minimum 3 assumptions. Any L-confidence assumption must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the strategy, execute this step before delivering output:

> *"Now identify ≥3 genuine weaknesses in this GTM strategy. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this launch is catastrophically wrong?"*

- If you cannot find real weaknesses, you haven't looked hard enough.
- Bear cases must be steelmanned — argued as forcefully as possible, not listed as probability-weighted caveats.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the risk register — it is a distinct, explicitly adversarial voice.

---

## Quality Gradients

### Intern Tier
- Lists a target market and some channels
- Uses "large TAM" as the primary rationale for market entry
- No segment selection — targets everyone broadly ("SMBs" or "enterprise")
- Channel selection based on familiarity, not unit economics
- No launch gates or kill criteria — "launch and see what happens"
- Metrics are vanity metrics (downloads, page views) without connection to business outcomes
- No competitive positioning beyond "we're better"
- Missing: wedge identification, unit economics, failure criteria, evidence tiers

### Consultant Tier
- Market entry thesis exists with some timing logic
- Segments are defined (though may lack the "name 100 prospects" specificity)
- Channel strategy includes basic unit economics (CAC, LTV/CAC)
- Launch has phases but gates may be vague ("good retention" instead of "≥40% day-30 retention")
- Competitive positioning uses a framework (Dunford or similar)
- Metrics exist with targets and some failure criteria
- Evidence is tiered — distinguishes customer interviews from analyst reports
- Missing: Goodhart countermeasures, expansion path design, flywheel mechanics, adversarial self-critique

### Elite Tier
- Market entry thesis with wedge identification, timing forces, and defensibility assessment
- Segments scored with ICP matrix, evidence tiers per cell, expansion path mapped
- Channel strategy with full conversion funnel unit economics, evidence thresholds for scaling
- Launch sequencing with phase-specific gate criteria AND hard kill criteria (SMART-K)
- Competitive positioning validated with ≥5 prospects, battlecards per competitor
- Metrics include Goodhart countermeasures and antidote metrics for every leading indicator
- Failure criteria are specific, time-bound, and linked to kill actions
- Growth engine designed with explicit flywheel and reference customer strategy
- Every recommendation follows O→I→R→C→W cascade with H/M/L confidence
- Assumption Registry with ≥3 load-bearing assumptions
- Adversarial self-critique with ≥3 steelmanned weaknesses
- Cross-framework contradictions surfaced explicitly
- Document is navigable by non-creators (Reader Navigation, Notation Key, zero-jargon Executive Summary)

---

## Failure Modes

**FM-1: TAM Fantasy**
*What it looks like:* "The market is $50B so even 1% = $500M." Strategy document leads with market size as the primary rationale. No wedge, no segment selection, no evidence of ability to capture any share.
*Why it happens:* Large TAM feels like a strong argument because it implies headroom. But TAM without a wedge is like saying "there's a lot of ocean, so we should be able to catch fish" without a net.
*Detection:* If the market entry thesis can be reduced to "big market + good product = success," it's TAM Fantasy.
*Correction:* Require a wedge (structural advantage in a specific segment) before any market sizing. Ask: "What specific thing about us makes us able to win 10 customers in this segment that [incumbent] can't easily match?"

**FM-2: Channel Spray**
*What it looks like:* "We'll run content marketing, paid ads, outbound sales, partnerships, and community simultaneously." All channels get thin investment. After 6 months, none has produced statistically significant signal.
*Why it happens:* Fear of missing out on the "right" channel. Desire to show investors a comprehensive plan. Confusion between strategy (choosing) and planning (listing).
*Detection:* If the channel strategy includes 3+ channels in Phase 1, or if no channel has a full unit economics breakdown, it's Channel Spray.
*Correction:* One channel in Phase 1. Prove it (50+ conversions with positive unit economics). Then add the second. The Minimum Viable Channel rule exists for this reason.

**FM-3: Positioning Without Wedge**
*What it looks like:* Clear value proposition ("we make analytics easy") but no explanation of how you get the first 10 customers. The positioning describes why you're good but not why you win against the specific alternative the customer is currently using.
*Why it happens:* Positioning work focuses on messaging rather than competitive displacement. "We're great" is not a wedge. "We solve X that [incumbent] can't solve without re-architecting" is a wedge.
*Detection:* If you can't complete the sentence "Customers will switch from [alternative] because [structural reason the alternative can't match]," there's no wedge behind the positioning.
*Correction:* Go back to Market Entry Thesis, specifically the Wedge Identification Method. Position against the alternative the customer would choose if you didn't exist.

**FM-4: Launch Without Gates**
*What it looks like:* GA launch without beta validation. No kill criteria. No "what must be true before we proceed" checkpoints. The launch plan is a Gantt chart of marketing activities, not a learning sequence.
*Why it happens:* Gates feel like delays. "We need to move fast" overrides "we need to learn before scaling." Pressure to show investor traction by a specific date.
*Detection:* If the launch plan has dates but no metrics-based gates between phases, it's a timeline without learning.
*Correction:* Add phase-specific gates using the Gate Criteria Rubric. Add hard kill criteria using the SMART-K framework. Every phase has a purpose (what question it answers) and a gate (what must be true to proceed).

**FM-5: GTM by Analogy**
*What it looks like:* "Slack did bottoms-up adoption, so we should too." "Zoom grew through PLG, and we're also a SaaS product." The GTM strategy is built on analogy to a successful company without examining whether the analogy transfers.
*Why it happens:* Analogies are compelling stories. Investors respond to "we're the Uber of X." But analogies fail when: the product is different, the market is different, the timing is different, or the distribution advantage is different.
*Detection:* If removing the analogy collapses the strategic rationale, the strategy is built on the analogy, not on evidence.
*Correction:* Every analogical claim must pass the transfer test: "What specific structural condition made this work for [Company], and do we have the same condition?" If you can't answer that, the analogy is decoration, not evidence.

**FM-6: Feature Launch Disguised as GTM**
*What it looks like:* A "GTM strategy" that's actually "build feature X, then blog about it." No channel economics, no segment selection, no competitive positioning. The entire strategy is: ship → announce → hope.
*Why it happens:* PMs who are strong on product and weak on GTM default to what they know (features) and bolt on a thin distribution layer.
*Detection:* If the strategy could be summarized as "build it and they will come," it's a feature launch, not a GTM strategy.
*Correction:* Apply the full framework set. Who is the segment? How will you reach them? What are the unit economics? What kills this? A GTM strategy without channel economics is not a strategy.

**FM-7: Segment Confusion**
*What it looks like:* Target customer is "enterprise companies" or "small businesses" or "people who need better analytics." You can't name 100 prospects that fit the definition. The segment is so broad that channel strategy, positioning, and pricing all become generic.
*Why it happens:* Fear of leaving revenue on the table by being specific. "What if we're wrong about the segment?" — but being vague about the segment guarantees you're wrong about everything else.
*Detection:* Apply the "name 100 prospects" test. If you can't, the segment is too vague.
*Correction:* Narrow using the Segment Definition Rules. Add observable behaviors, specific company attributes, and reachability criteria until you can generate a prospect list.

**FM-8: Metrics Without Failure Criteria**
*What it looks like:* Success metrics are defined ("1,000 users in 6 months") but no conditions under which you'd stop or pivot. Success is the only planned outcome. When metrics miss, the response is always "give it more time" or "invest more."
*Why it happens:* Failure criteria feel like planning to fail. Optimism bias. Organizational pressure to be "committed" rather than "disciplined."
*Detection:* If the metrics section doesn't include a table of hard stops with specific actions, failure criteria are missing.
*Correction:* Apply the SMART-K framework. For every success metric, define the failure threshold, the timeframe, and the action (kill, pivot, or redesign — not "reassess").

**FM-9: Expert-Only GTM Document**
*What it looks like:* Strategy document uses framework jargon (PLG, CAC, LTV/CAC, beachhead, bowling alley, JTBD) without explaining terms. Stakeholders who need to execute the strategy can't parse the document. A marketing lead reading "our PLG motion targets the beachhead via a content flywheel with 3:1 LTV/CAC" would need a glossary.
*Why it happens:* The strategist writes for themselves or for other strategists. The document becomes an internal artifact rather than an execution guide.
*Detection:* Give the document to someone who will execute it (sales lead, marketing lead, product engineer). If they need to ask "what does this mean?" more than twice, it's expert-only.
*Correction:* Reader Navigation section (How to Read + Notation Key), zero-jargon Executive Summary, and one-line explanations on first reference to every framework term (Format Rule 8).

---

## What's Next

← This skill works best after: **Problem Framing** (validates the problem exists before you plan to sell the solution) and **Competitive Market Analysis** (provides the competitive landscape the GTM must navigate)
→ This skill's output feeds well into: **Narrative Building** (uses positioning and wedge to build the product story), **Specification Writing** (GTM requirements inform product priorities), **Metric Design & Experimentation** (GTM metrics become experiment targets)
⊕ **Start here if:** You have a product ready to launch, a market to enter, or a GTM motion that isn't working
💡 **For a full product cycle:** Problem Framing → Discovery & Research → Competitive Market Analysis → **[THIS SKILL]** → Narrative Building → Spec Writing → Metric Design

**Chain interface:**
- **Receives:** Validated problem definition with target market (from Problem Framing), competitive landscape assessment (from Competitive Market Analysis), or raw context (product to launch, market to enter, GTM motion to design)
- **Produces:** GTM Strategy Document with market entry thesis, segment prioritization, channel strategy with unit economics, launch sequence with gates and kill criteria, competitive positioning, and success/failure metrics
- **Handoff artifact:** The GTM Strategy's "Positioning" section maps directly to Narrative Building's input. The "Metrics & Failure Criteria" section maps to Metric Design's input. The "Segment Selection" informs Spec Writing's audience definition.

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Gate passed: problem validated, product exists/specced, competitive landscape known
- [ ] Executive summary: ≤300 words, zero jargon, a VP can act on it alone
- [ ] Framework selection (Step 0) completed: primary frameworks identified, irrelevant frameworks skipped
- [ ] Market entry thesis present: why this market + why now (≥1 timing force with T1-T3 evidence) + what's the wedge
- [ ] Wedge defensibility assessed: time to replicate, capital to replicate, structural barrier
- [ ] Go/Wait/Pivot decision table completed with clear verdict
- [ ] Segments defined: ≥3 candidates, each passes "name 100 prospects" test
- [ ] ICP scoring matrix completed with evidence tiers per cell and weighted scores
- [ ] Beachhead selected with score ≥3.0
- [ ] Expansion path mapped: beachhead → adjacent 1 → adjacent 2 → mainstream with transition triggers
- [ ] Channel strategy: ONE primary channel with full unit economics (CAC, payback, LTV/CAC)
- [ ] Channel evidence thresholds defined: hypothesis → signal → proof → proven
- [ ] Launch phases defined: Alpha → Beta → Open Beta → GA → Scale
- [ ] Gate criteria per phase: specific metrics with specific thresholds
- [ ] Kill criteria per phase: SMART-K (specific, measurable, actionable, realistic, time-bound, kill-linked)
- [ ] Positioning statement completed using Dunford framework
- [ ] Battlecards built for top 2-3 competitors
- [ ] Positioning validated with ≥5 prospects (or flagged as unvalidated)
- [ ] Leading indicators defined with Goodhart countermeasures and antidote metrics
- [ ] Lagging indicators defined with 6-month and 12-month targets
- [ ] Failure criteria: ≥3 hard stops with SMART-K format
- [ ] Review cadence defined: weekly (PM), monthly (VP), quarterly (GM)
- [ ] Growth model selected from taxonomy with evidence
- [ ] Flywheel designed and scored on 4 dimensions
- [ ] Reference customer strategy: ≥5 target reference customers with selection criteria
- [ ] Per-cell evidence tier annotation in ALL comparison matrices (not just headline claims)
- [ ] O→I→R→C→W cascade applied to ALL recommendations (not just final section)
- [ ] H/M/L confidence levels explicit on every strategic conclusion — no weasel words
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source >6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key conclusion resting only on Tier 4-6 evidence
- [ ] Assumption Registry present with ≥3 load-bearing assumptions
- [ ] Adversarial Self-Critique section present with ≥3 genuine weaknesses (steelmanned, not listed)
- [ ] Cross-framework contradictions surfaced explicitly (not resolved artificially)
- [ ] Reader Navigation present: reading time guide + role-based guide
- [ ] Notation Key present: all symbols explained
- [ ] Zero-jargon Executive Summary (no framework terms)
- [ ] First reference to every framework includes one-line explanation

---

## Worked Example

### Input

> "We're launching Collab Canvas — a real-time collaborative whiteboarding tool designed for remote product teams. The core differentiator is AI-generated templates that auto-structure brainstorming sessions (competitive analysis, sprint retro, user journey mapping) based on the meeting context. Primary competitors: Miro, FigJam, Lucidspark. We're a seed-stage startup with $2M funding, 4-person team, and 6 months of runway. We need a GTM strategy to get our first 100 paying customers."

---

### Output (abbreviated — demonstrates key formats; a full GTM strategy would cover all sections)

**Executive Summary (≤300 words):**

Collab Canvas should target remote product teams at companies with 20-100 employees who currently use Miro's free tier and hit the 3-board limit during sprint planning. These teams spend 2-3 hours per week setting up whiteboards that AI templates could generate in 30 seconds — a time savings worth $200-400/month per team that Miro cannot easily match without cannibalizing their high-margin enterprise pricing model.

The entry point is Miro's free tier cliff: teams that need more than 3 boards but can't justify Miro's $8-16/user/month enterprise pricing for a tool they use 4-6 hours/week. Collab Canvas at $5/user/month with unlimited AI-generated boards targets this exact gap.

This is viable now because LLM costs dropped 85% in the past 12 months, making AI template generation feasible at SMB pricing — a cost structure that wasn't possible 18 months ago.

The primary channel is Product Hunt launch followed by product-led growth through the Figma and Slack integration ecosystems. Direct sales is not viable at seed stage with a 4-person team and $5/user/month pricing.

Launch sequence: 4-week closed beta with 15 design partners, 4-week open beta via Product Hunt, then GA. Kill criteria: if fewer than 10 of 15 design partners use the product weekly after 3 weeks, or if CAC exceeds $300 after 50 signups, stop and pivot the approach.

**The strategy's biggest risk: Miro adds AI templates as a feature within 6 months, neutralizing the wedge before Collab Canvas builds enough switching costs.** If Miro announces AI templates, immediately pivot positioning from "AI whiteboarding" to "the whiteboarding tool built for how remote teams actually work" — shifting the wedge from technology to workflow.

---

**Segment Selection — ICP Scoring:**

| Criterion | Weight | Remote product teams (20-100 emp.) | Design agencies (5-30 emp.) | Enterprise innovation labs (500+ emp.) |
|-----------|:------:|:---:|:---:|:---:|
| Acute pain | 25% | 5 (T2: 8 interviews) | 3 (T5: forum posts) | 4 (T3: analyst report) |
| Willingness to pay | 20% | 4 (T2: 6/8 said "probably") | 3 (T6: inferred) | 2 (T4: long procurement) |
| Accessibility | 20% | 5 (T6: Slack/ProductHunt) | 3 (T6: fragmented) | 1 (T6: gated by IT) |
| Reference-ability | 15% | 4 (T6: vocal on Twitter) | 5 (T6: portfolio-driven) | 2 (T6: NDA-restricted) |
| Expansion potential | 10% | 4 (T6: → larger teams) | 2 (T6: niche) | 5 (T6: → enterprise) |
| Competitive vacuum | 10% | 4 (T2: Miro free tier gap) | 2 (T3: FigJam dominates) | 1 (T3: Miro enterprise) |
| **Weighted Score** | | **4.3** | **3.0** | **2.4** |

**Decision:** Remote product teams (20-100 employees) score 4.3 — strong beachhead. Design agencies are a viable adjacent segment (3.0). Enterprise innovation labs score below threshold (2.4) — skip for now.

---

**Channel Unit Economics — PLG via Product Hunt + Slack Integration:**

```
Funnel Stage              | Volume    | Conversion | Cost/Stage  | Cumulative CAC
──────────────────────────────────────────────────────────────────────────────────
Product Hunt impressions  | 50,000    | 2%         | $500 (prep) | $0.01/impression
Landing page signups      | 1,000     | 25%        | $0           | $0.50/signup
Free trial starts         | 250       | 40%        | $0           | $2.00/trial
Activation (1 AI template)| 100       | 30%        | $0           | $5.00/activation
Paid conversion           | 30        | —          | $0           | $16.67/customer (T6: estimated)
```

Payback period: $16.67 CAC / ($5/user × 5 users avg = $25/mo) = **0.7 months (T6: estimated)**
LTV/CAC: ($25/mo × 18mo avg × 80% margin) / $16.67 = **21.6:1 (T6: estimated — optimistic)**

⚠️ `[EVIDENCE-LIMITED: All channel economics are T6 estimates. Actual numbers from beta will replace these. Do not commit budget based on these projections.]`

---

**Failure Criteria:**

| Condition | Timeframe | Action |
|-----------|-----------|--------|
| <10 of 15 design partners use product weekly after 3 weeks | Beta Week 3 | **STOP:** Product doesn't deliver value fast enough. Pivot to different core feature or different segment. |
| <30 free trial signups from Product Hunt launch | Open Beta Day 3 | **STOP:** Product Hunt channel failed. Pivot to Slack app directory or direct outbound to Miro free-tier users. |
| CAC > $300 after 50 paid conversions | GA Month 2 | **STOP:** Unit economics don't work at this price point. Raise price or reduce CAC before continuing. |
| Miro announces AI templates feature | Any phase | **PIVOT:** Immediately shift positioning from "AI whiteboarding" to workflow-first differentiation. Re-run competitive positioning framework. |

---

### Why This Works

This output was produced by running Steps 1-4 and Step 6 of the Full Application Method: Market Entry Thesis (wedge = Miro free tier gap + AI cost curve crossing), Segment Selection (ICP scoring with evidence tiers), Channel Strategy (PLG unit economics), Launch Sequencing (gated phases), and Failure Criteria (SMART-K format). It satisfies the Elite Tier Quality Gradient: every strategic conclusion has evidence tiers, H/M/L confidence, and O→I→R→C→W structure; the executive summary is zero-jargon; and failure criteria are specific, time-bound, and kill-linked. The biggest weakness (Miro adding AI templates) is named upfront, not buried.

---

## References

**Framework Sources:**
- April Dunford, *Obviously Awesome* (2019) — competitive positioning framework
- Geoffrey Moore, *Crossing the Chasm* (1991; 3rd ed. 2014) — beachhead strategy, bowling alley, whole product concept
- Hamilton Helmer, *7 Powers* (2016) — counter-positioning as wedge strategy
- Marc Andreessen, "The Only Thing That Matters" (pmarchive.com, 2007) — product-market fit as GTM prerequisite
- Brian Balfour, "The Three Fits" (Reforge, 2017) — market-product fit, product-channel fit, channel-model fit
- Andrew Chen, *The Cold Start Problem* (2021) — network effects, viral growth, marketplace dynamics
- Lenny Rachitsky, "How the Biggest Consumer Apps Got Their First 1,000 Users" (lennysnewsletter.com, 2021) — channel-specific early traction patterns
- Charles Goodhart, "Goodhart's Law" — metric gaming countermeasures

**Related Skills in PM Skills Arsenal:**
- Problem Framing — upstream (validates the problem before GTM planning)
- Competitive Market Analysis — upstream/parallel (provides competitive landscape)
- Discovery & Research — parallel (demand-side primary research for segment validation)
- Narrative Building — downstream (uses positioning and wedge for product story)
- Specification Writing — downstream (GTM requirements inform product priorities)
- Metric Design & Experimentation — downstream (GTM metrics become experiment targets)

---

*Created: 2026-03-12 | PM Skills Arsenal v1.0 | go-to-market-strategy*
*Quality tier: Elite (1200+ lines, 7 encoded frameworks, quality gradients, 9 failure modes)*
*License: MIT*
