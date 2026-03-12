---
name: product-strategy
description: "Use when building product strategy, roadmaps, or strategic plans — vision articulation, strategic bet definition, roadmap sequencing, resource allocation, portfolio planning, or quarterly/annual planning. Encodes bet-sizing, option-value sequencing, strategic tension surfacing, and explicit deprioritization. Produces a strategy document, not a feature backlog."
version: "1.0.0"
type: "codex"
tags: ["Strategy", "Planning", "Roadmap", "Leadership"]
created: "2026-03-12"
valid_until: "2026-09-12"
derived_from: "agents/planner/prompt.md"
tested_with: []
license: "MIT"
capability_summary: "Produces a strategic product roadmap with vision-to-bet cascade, confidence-rated strategic bets, option-value sequencing rationale, resource allocation, strategic tension analysis, explicit deprioritization with opportunity costs, and quarterly gate structure."
input_schema:
  product_or_area: "string — product, team, or strategic area"
  time_horizon: "enum[quarterly, half_year, annual, multi_year] — planning horizon"
  vision: "string — optional, existing vision statement if available"
  constraints: "string — optional, team size, budget, dependencies, strategic mandates"
  current_state: "string — optional, current product state, recent performance, market context"
  strategic_context: "string — optional, company strategy, competitive dynamics, market shifts"
output_schema:
  executive_summary: "Zero-jargon strategy thesis, ≤300 words"
  vision_statement: "Aspirational but falsifiable, 1-2 sentences"
  strategic_bets: "Confidence-rated bets with hypotheses and investment sizing"
  sequencing_rationale: "Why this order, with counterfactuals"
  not_doing_section: "Explicit deprioritization with opportunity costs"
  resource_plan: "Team allocation per bet with capacity check"
  strategic_tensions: "Where bets compete, how resolved"
  quarterly_gates: "Checkpoint criteria per quarter"
  assumption_registry: "Load-bearing assumptions with confidence levels"
  self_critique: "≥3 genuine weaknesses in this strategy"
example_invocation: "examples/USE_CASES.md"
---

## Purpose

Produce an elite-tier strategic product roadmap that articulates a falsifiable vision, sizes and sequences strategic bets with explicit confidence levels, surfaces tensions between competing priorities, names what you are NOT doing and what that costs, allocates resources against capacity constraints, and sets quarterly gates with kill criteria. The output is a Strategy Document — not a feature backlog, not a Gantt chart, but a decision architecture that tells a team what to build, in what order, why, and what to stop doing.

## When to Use / When NOT to Use

**Use this skill when:**
- Building or revising a product roadmap for a quarter, half, or year
- Articulating product vision and translating it to executable strategy
- Running annual or quarterly planning exercises
- Making portfolio allocation decisions across multiple investment areas
- A leadership review requires a strategy document with clear bets and sequencing rationale
- You need to explicitly communicate what you are NOT doing and why

**Do NOT use this skill when:**
- You need competitive intelligence to inform the strategy (use Competitive Market Analysis skill first — its output feeds this skill)
- You need to write a specification for a specific feature (use Specification Writing skill — this skill's output feeds that one)
- You need to define metrics for measuring success of shipped features (use Metric Design & Experimentation skill)
- You need to understand a problem before deciding what to build (use Problem Framing skill — that comes upstream)
- You need a project plan with task-level assignments and sprint breakdowns (this is strategy, not project management)

**Anti-inputs (what this skill does NOT handle):**
- Feature specifications or PRDs (downstream: Specification Writing skill)
- Sprint planning or task decomposition (execution layer, not strategy layer)
- Competitive analysis (upstream: Competitive Market Analysis skill)
- User research synthesis (upstream: Discovery Research skill)
- OKR writing (adjacent but distinct — this skill produces the strategy that OKRs measure)

---

## Context Gate (Step -1: Is a Strategy Document the Right Artifact?)

Before applying any frameworks, verify that a strategy document is what the situation actually requires. The most common waste is building a rigorous strategy when the real need is simpler — or more fundamental.

| Check | If YES | If NO |
|-------|--------|-------|
| **Is the problem defined?** Do you know what customer problem you're solving and for whom? | Proceed to vision articulation | STOP. Use Problem Framing skill first. Strategy without a defined problem is a solution in search of one. |
| **Do you have market context?** Do you know who competes, what customers want, and where the market is heading? | Proceed to bet-sizing | Use Competitive Market Analysis and/or Discovery Research first. Strategy without market context is guesswork. |
| **Is this actually a strategy question?** Or is someone asking for a feature list with dates? | Proceed — you're building a decision architecture | Clarify scope. If the ask is "when will feature X ship," that's a project management question, not a strategy question. |
| **Is the time horizon appropriate?** Strategy requires ≥1 quarter. Anything shorter is execution planning. | Proceed with appropriate horizon | Redirect to sprint/milestone planning. Strategy doesn't operate at 2-week increments. |
| **Do you have resource constraints?** Team size, budget, dependencies, or hiring timelines? | Proceed — constraints make strategy real | Flag `[RESOURCE-UNCONSTRAINED]` — the strategy will be aspirational, not executable. Get constraints before finalizing. |
| **Is there a company-level strategy this must align with?** | Reference it explicitly in vision articulation | Proceed, but flag that this product strategy lacks a company-level anchor — may need realignment later. |

**Context Gate outcome:** If 2+ checks fail, this skill will produce a less useful artifact. Note the gaps in the output header and proceed with caveats, or pause to gather upstream inputs.

---

## Reader Navigation

### How to Read This Document

| Time Available | What to Read | What You'll Get |
|---------------|-------------|-----------------|
| **5 minutes** | Executive Summary + Vision Statement + Strategic Bets table (names and confidence only) | The thesis: what we're betting on, how confident we are, and the recommended action |
| **15 minutes** | Above + Sequencing Rationale + NOT-Doing Section + Strategic Tensions | The decision architecture: why this order, what we're sacrificing, where bets compete |
| **30 minutes** | Full document | Complete strategy with resource plans, quarterly gates, assumptions, and self-critique |

| Your Role | Start Here | Focus On |
|-----------|-----------|----------|
| **Executive / VP** | Executive Summary → Strategic Bets → NOT-Doing Section | Are we betting on the right things? What are we giving up? |
| **PM / Strategy Lead** | Full document, front to back | Sequencing logic, tension resolution, quarterly gates |
| **Engineering Lead** | Resource Plan → Sequencing Rationale → Quarterly Gates | Team allocation, dependency chains, checkpoint criteria |
| **Designer** | Vision Statement → Strategic Bets (hypothesis details) → Quarterly Gates | User outcomes per bet, success criteria, adaptation points |
| **Finance / Ops** | Resource Plan → Strategic Bets (investment sizing) → Assumption Registry | Cost, headcount, hiring timelines, load-bearing assumptions |

### Notation Key

| Symbol | Meaning |
|--------|---------|
| **H / M / L** | Confidence level: H (>70%), M (40-70%), L (<40%) |
| **T1-T6** | Evidence tier: T1 (behavioral data) through T6 (punditry/inference) |
| **O→I→R→C→W** | Observation → Implication → Response → Confidence → Watch indicator |
| `[EVIDENCE-LIMITED]` | Key conclusion rests on Tier 4-6 evidence — validate before committing resources |
| `[POTENTIALLY STALE]` | Claim based on data >6 months old — verify before presenting |
| `[RESOURCE-UNCONSTRAINED]` | Strategy was built without confirmed resource constraints |
| Core / Adjacent / Transformational | Bet categories: Core protects base (H confidence), Adjacent expands (M), Transformational creates new (L) |
| **Deferred / Declined / Deprecated** | NOT-Doing taxonomy: doing later / decided against / actively stopping |

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are quality enforcement mechanisms, not style preferences.

1. **Take positions. Never hedge with weasel words.** "Likely," "may," "could," and "seems" are banned from strategic conclusions. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"This bet will capture the underserved mid-market segment within 3 quarters (M)"* — not *"This bet may help us reach new customers."*

2. **Every strategic bet carries a hypothesis, confidence level, and investment size.** A bet without a hypothesis is a wish. A bet without a confidence level is a assertion. A bet without an investment size is a fantasy.

3. **The O→I→R→C→W cascade applies to ALL strategic recommendations**, not just final sections. Observation [evidence tier] → Implication [mechanism] → Response [specific action] → Confidence [H/M/L + assumption] → Watch Indicator [observable signal].

4. **Begin with Framework Selection (Step 0)** before applying any framework. Identify the strategy question type; select 3-4 load-bearing frameworks; note which to skip.

5. **Contradictions between bets or frameworks are signal, not noise.** When two strategic bets pull in different directions, or when sequencing logic conflicts, surface the tension explicitly and state the resolution rationale.

6. **Flag time-sensitive claims.** Any claim based on data older than 6 months must carry `[POTENTIALLY STALE — verify before presenting]`.

7. **Flag thin-evidence conclusions.** If a key strategic bet rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before committing resources]`.

8. **Every sequencing decision states the counterfactual.** "We do A before B because..." must include "If we did B first, [specific consequence]." Sequencing without counterfactuals is assertion, not reasoning.

9. **Framework references include one-line contextual explanations.** First reference to any framework includes a parenthetical explaining why it matters for this strategy decision. The strategy document must be navigable by non-creators.

---

## Output Template (Mandatory Document Skeleton)

Every Strategy Document MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections.

```markdown
# Strategy Document: [Product/Area — e.g., "M365 Copilot Mobile — FY27 H1"]

> **Date:** [YYYY-MM-DD] | **Time horizon:** [quarterly/half/annual/multi-year] | **Confidence band:** [Overall H/M/L] | **Next review:** [Date]

---

## Executive Summary

[≤300 words. Zero jargon. A VP reads only this and makes a resource allocation decision. Final sentence = the recommended strategic direction in bold. Written LAST, appears FIRST.]

---

## Step 0: Framework Selection

| Strategy question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Annual roadmap for established product"] | [e.g., Vision-to-Roadmap Cascade, Strategic Bet-Sizing, Option-Value Sequencing] | [e.g., Resource Allocation, Roadmap Communication] | [e.g., "N/A — all frameworks load-bearing for annual planning"] |

---

## 1. Vision Statement

[1-2 sentences. Aspirational but falsifiable. Not "be the best" but "become the default X for Y in Z timeframe."]

**Falsification test:** [What observable outcome in what timeframe would prove this vision wrong?]

---

## 2. Strategy Pillars

| # | Pillar | Strategic intent | Maps to vision how |
|---|--------|-----------------|-------------------|
| P1 | [Theme name — not a feature, not an initiative] | [What this pillar achieves strategically] | [How it advances the vision] |
| P2 | | | |
| P3 | | | |

---

## 3. Strategic Bets

### Bet 1: [Name]
- **Pillar:** [Which pillar this serves]
- **Category:** Core / Adjacent / Transformational
- **Hypothesis:** If we [specific investment], then [measurable outcome] because [mechanism]
- **Confidence:** [H/M/L] — based on [evidence summary with tier]
- **Investment:** [X engineers, Y designers, Z months] = [% of total capacity]
- **Success criteria:** [Specific, measurable, time-bound]
- **Kill criteria:** [What observable outcome at what checkpoint tells us to stop]
- **Key assumption:** [The one thing that must be true for this bet to pay off]

### Bet 2: [Name]
[Same structure]

### Bet 3: [Name]
[Same structure]

**Portfolio Balance Check:**

| Category | Count | % of investment | Target range | Assessment |
|----------|:-----:|:---------------:|:------------:|:----------:|
| Core | | | 50-70% | |
| Adjacent | | | 20-30% | |
| Transformational | | | 5-15% | |

---

## 4. Sequencing Rationale

| Sequence | Bet | Rationale type | Counterfactual |
|:--------:|-----|---------------|----------------|
| 1st | [Bet name] | [Dependency / Information / Option-value / Risk / Revenue] | If we did [other bet] first, [specific consequence] |
| 2nd | | | |
| 3rd | | | |

**Critical path:** [Which bet, if delayed, delays everything else]

**Information gates:** [Which bets reveal information that changes other bets' value]

---

## 5. Strategic Tensions

| Tension | Bet A | Bet B | Type | Resolution | What we lose |
|---------|-------|-------|------|------------|--------------|
| [Name] | [Bet] | [Bet] | Resource / Strategic / Timing | [How resolved + rationale] | [Cost of this resolution] |

**Strategic debt created:** [What speed/quality/scope tradeoff creates debt that must be repaid, and when]

---

## 6. What We Are NOT Doing

| # | Item | Category | Why not | What we lose | Reconsider if |
|---|------|----------|---------|-------------|---------------|
| 1 | [Specific initiative/feature/market] | Deferred / Declined / Deprecated | [Reasoning] | [Opportunity cost — not zero] | [Observable condition] |
| 2 | | | | | |
| 3 | | | | | |

**Stakeholder communication:** [How to explain the NOT-doing decisions to affected teams/customers without demoralizing or angering]

---

## 7. Resource Plan

**Capacity model:**

| Team/Function | Total headcount | Planned (70%) | Reactive (20%) | Exploration (10%) | Override? |
|--------------|:---------------:|:-------------:|:---------------:|:-----------------:|:---------:|
| Engineering | | | | | |
| Design | | | | | |
| PM | | | | | |

**Per-bet allocation:**

| Bet | Eng | Design | PM | Duration | Monthly burn | Dependencies on other teams |
|-----|:---:|:------:|:--:|:--------:|:------------:|:-------------------------:|
| [Bet 1] | | | | | | |
| [Bet 2] | | | | | | |

**Hiring implications:** [Which bets require hiring? Lead time? What happens if hiring is delayed?]

**Capacity check:** [Does the sum of all allocations exceed 70% planned capacity? If yes, something must be cut or deferred.]

---

## 8. Quarterly Gates

| Quarter | Primary bet focus | Gate criteria (pass/fail) | Adaptation triggers | Kill criteria |
|---------|------------------|--------------------------|--------------------|--------------|
| Q1 | [Bet name] | [Specific, measurable criteria] | [What signal tells us to adjust scope/direction] | [What tells us to stop entirely] |
| Q2 | | | | |
| Q3 | | | | |
| Q4 | | | | |

**Replanning protocol:** [How and when the strategy gets revised — monthly check-ins, quarterly deep-dives, trigger-based emergency reviews]

---

## 9. Roadmap Communication Views

| Audience | View | Emphasis | Omit |
|----------|------|----------|------|
| Executive | Bets + business outcomes + confidence | Investment sizing, portfolio balance | Technical details, sprint-level scope |
| Engineering | Dependencies + technical architecture + sequencing | Build sequence, integration points | Business rationale beyond what's needed for decisions |
| Design | User outcomes per bet + experience evolution | Success criteria from user perspective | Resource math, financial projections |
| Sales/GTM | Customer-facing capabilities + competitive positioning | Timeline for customer-visible features | Internal bets, platform investments |

---

## 10. Strategic Recommendations (O→I→R→C→W Cascade)

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

## Assumption Registry

| # | Assumption | Bets it underpins | Confidence | Evidence | What would invalidate this |
|---|-----------|-------------------|:----------:|----------|----------------------------|
| 1 | | | H/M/L | (TX) | |
| 2 | | | H/M/L | (TX) | |
| 3 | | | H/M/L | (TX) | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[What assumption is being made? What evidence would disprove it? Scenario where this strategy is catastrophically wrong.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---------|-------------------|----------|
| [Observable event] | [Which bets/sections break] | [When to check] |

---

## Sources

[All sources cited in the analysis, with evidence tier and date.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Skipped — [reason]" and move on.
2. **Every strategic bet must have a hypothesis, confidence level, AND investment size** — no exceptions.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Q2 Gate") with insight headers (e.g., "Q2: Kill or Double Down on Enterprise Expansion") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **The NOT-Doing section must contain ≥3 items.** An empty NOT-Doing section means no hard decisions were made.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology — not merely referenced. A PM using this skill produces a strategy document that requires these frameworks; without them, the output degrades to a feature backlog with dates.

### Framework 1: Vision-to-Roadmap Cascade

The structural bridge from aspiration to execution. Most strategies fail at one of two gaps: (1) vision that never translates to bets, or (2) bets that don't trace back to a coherent vision. The cascade makes both gaps impossible to hide.

**The Five Levels:**

| Level | What it is | What it is NOT | Quality test |
|-------|-----------|---------------|-------------|
| **Vision** | 1-2 sentences. Aspirational but falsifiable. Defines what winning looks like in a specific timeframe. | A mission statement. "Be the best" is not a vision — it's a bumper sticker. | Can you name a specific observable outcome in a specific timeframe that would prove the vision wrong? If not, it's not falsifiable. |
| **Strategy Pillars** | 3-5 themes that bridge vision to execution. Each pillar is a strategic direction, not an initiative. | Feature areas. "AI-powered search" is a pillar. "Add vector search to API" is an initiative. | Remove one pillar. Does the vision become unreachable? If not, the pillar isn't load-bearing — cut it. |
| **Strategic Bets** | Specific investments under each pillar, each with a hypothesis, confidence level, and investment size. | Tasks. "Hire 3 engineers" is a resource action. "Win the mid-market analytics segment by building self-serve onboarding" is a bet. | Does each bet have a testable hypothesis? An explicit confidence level? A named investment? If any are missing, it's a wish, not a bet. |
| **Sequencing** | Which bets first, which later, and why. Dependency logic, information value, option preservation. | Gut priority. "We feel this is more important" is not sequencing. "A must come before B because A's outcome determines whether B is worth doing" is sequencing. | Every sequence decision states the counterfactual. "If we did B first, [consequence]." |
| **Quarterly Translation** | How the 12-month roadmap becomes this quarter's focus. What's in scope, what's deferred, what gates exist. | A sprint plan. Quarterly translation sets direction and success criteria. It does not assign story points. | At the end of the quarter, can you definitively say pass/fail against the gate criteria? If criteria are fuzzy, translation failed. |

**Vision Quality Rubric:**

| Rating | Criteria | Example |
|--------|----------|---------|
| 🟢 **Strong** | Falsifiable, time-bound, specific about the target state. A team member can explain what we're building toward without asking. | "Become the default analytics tool for mid-market SaaS companies (500-5000 employees) by FY28, measured by >25% market share in that segment." |
| 🟡 **Moderate** | Directional but not falsifiable. Points toward the right mountain but doesn't name the summit. | "Be the leading analytics platform for growing companies." |
| 🔴 **Weak** | Inspirational mush. Could apply to any company in any industry. No team member can derive what to build from it. | "Empower teams with data-driven insights to make better decisions." |

**Decision Table — Vision Clarity x Execution Certainty:**

| | Execution certainty HIGH | Execution certainty LOW |
|---|---|---|
| **Vision clarity HIGH** | **Execution Roadmap.** Clear bets, aggressive timelines, detailed resource plans. The strategy is a commitment. | **Exploration Roadmap.** Clear destination, uncertain path. Strategy emphasizes information-gathering bets and option preservation. Quarterly gates are adaptation points, not accountability checkpoints. |
| **Vision clarity LOW** | **Pivot Roadmap.** You can build but don't know what to build toward. Strategy is a series of validated experiments, each narrowing the vision. Time-boxed: 1-2 quarters max before vision must crystallize or the initiative gets killed. | **Discovery Mode.** Neither destination nor path is clear. This is not a strategy question — it's a Problem Framing question. Use Problem Framing skill instead. Do not build a roadmap on sand. |

---

### Framework 2: Strategic Bet-Sizing

Making explicit what you're betting on — the anatomy of a strategic investment with enough rigor that a board member could evaluate the portfolio.

**Bet Anatomy (every bet must have all 6 components):**

| Component | Description | Missing = |
|-----------|-------------|-----------|
| **Hypothesis** | If we do [specific investment], then [measurable outcome] because [mechanism] | A feature request, not a bet |
| **Expected outcome** | Quantified where possible: revenue, users, market share, engagement, cost reduction | Aspirational hand-waving |
| **Evidence quality** | What data supports this hypothesis? Cite evidence tier. | Faith-based strategy |
| **Confidence level** | H (>70%), M (40-70%), L (<40%) — how sure are we this bet pays off? | False certainty |
| **Investment size** | People (engineers, designers, PMs), time (months/quarters), money (if applicable) | A fantasy disconnected from reality |
| **Kill criteria** | What observable outcome at what checkpoint tells us this bet is failing and should be stopped? | Zombie initiative that never dies |

**Bet Categories — The Three Horizons of Investment:**

| Category | Definition | Confidence range | Portfolio target | Risk profile |
|----------|-----------|:----------------:|:----------------:|-------------|
| **Core** | Protect and grow existing business. Incremental improvements to established products/features. | H (>70%) | 50-70% of investment | Low risk, predictable returns. Failure mode: under-investing here starves the cash cow. |
| **Adjacent** | Extend into new segments, geographies, or use cases that leverage existing capabilities. | M (40-70%) | 20-30% of investment | Medium risk, uncertain returns. This is where growth comes from. Failure mode: spreading too thin across too many adjacencies. |
| **Transformational** | Create fundamentally new capabilities, markets, or business models. | L (<40%) | 5-15% of investment | High risk, potentially outsized returns. Failure mode: either zero investment (no strategic upside) or treating transformational bets with core-bet accountability (killing them too early). |

**Portfolio Balance Scoring Rubric:**

| Portfolio composition | Assessment | Action |
|-----------------------|-----------|--------|
| All bets are Core | 🔴 **Strategic stagnation.** No risk = no future growth. You're optimizing the present at the expense of the future. | Add ≥1 Adjacent bet and ≥1 Transformational bet. If leadership resists, name the risk: "We are betting 100% that the current market structure persists." |
| Core >70%, no Transformational | 🟡 **Conservative.** Safe but vulnerable to disruption. | Acceptable for 1-2 quarters during execution crunch. Unsustainable for annual planning. |
| Core 50-70%, Adjacent 20-30%, Transformational 5-15% | 🟢 **Balanced.** Protects base while investing in growth and future optionality. | Monitor quarterly. Rebalance if Core bets are failing (shift more to Core) or succeeding beyond expectations (shift more to Adjacent/Transformational). |
| Adjacent + Transformational >50% | 🟡 **Aggressive.** High upside but fragile — if the core business weakens, the entire strategy collapses because there's nothing generating stable returns. | Acceptable only if core business is strong and self-sustaining. Requires explicit "what if core weakens" contingency. |
| All bets are Transformational | 🔴 **Startup mentality in an established product.** Either the product is genuinely pivoting (valid) or someone confused ambition with strategy. | Verify this is intentional. If yes, relabel as a pivot strategy with explicit runway calculation. If no, rebalance. |

**Bet Scoring Matrix — Strategic Importance x Confidence:**

| | Confidence HIGH | Confidence MEDIUM | Confidence LOW |
|---|:---:|:---:|:---:|
| **Strategic importance HIGH** | **Fund fully, execute aggressively.** This is the core of your strategy. Resource generously. | **Fund and de-risk.** Invest, but structure the bet to resolve uncertainty early. Front-load the information-generating work. | **Explore, don't commit.** High potential but low certainty. Run a time-boxed experiment (1 quarter max) before committing full resources. |
| **Strategic importance MEDIUM** | **Fund efficiently.** Worth doing but not worth over-investing in. Lean team, clear kill criteria. | **Conditional fund.** Invest only if a higher-priority bet doesn't need the resources. First to be cut in a trade-off. | **Park.** Not enough confidence to justify investment against medium strategic value. Revisit if evidence improves. |
| **Strategic importance LOW** | **Maintenance mode.** Keep the lights on but don't invest in growth. | **Deprioritize.** Candidate for the NOT-Doing section. | **Kill or ignore.** This is strategic noise. |

---

### Framework 3: Option-Value Sequencing

The most underused concept in product strategy: the order in which you do things changes the value of everything you do. This framework makes sequencing a strategic decision, not a priority-ranking exercise.

**Five Sequencing Logics:**

| Logic | Mechanism | When to use | Decision signal |
|-------|-----------|-------------|-----------------|
| **Dependency** | A must come before B because B literally cannot be built/delivered without A's output. | Technical dependencies, platform investments that enable downstream features. | "Can we build B without A?" If no → A first. Hard dependency. |
| **Information** | A should come before B because A's outcome reveals information that changes B's expected value. | When B is a large investment with uncertain payoff, and A is a smaller bet that tests the key assumption. | "Does A's result change whether we'd do B at all?" If yes → A first. |
| **Option-value** | A preserves more future options than B. Even if B has higher immediate expected value, A keeps more doors open. | When the market is volatile, technology is shifting, or you face irreversible decisions. | "If A succeeds, how many paths forward do we have? If B succeeds?" Choose the bet that maximizes paths. |
| **Risk** | The highest-uncertainty bet should come first to fail fast. If it fails, it changes everything downstream. | When one bet carries disproportionate uncertainty and downstream bets depend on its assumptions. | "If this bet fails, do we need to rethink the entire strategy?" If yes → do it first. |
| **Revenue** | Revenue-generating bets before cost-center bets. Cash flow timing matters — unfunded strategy is a thought experiment. | When runway matters, when the business is under financial pressure, or when revenue funds the rest of the roadmap. | "Does this bet generate revenue that funds other bets?" If yes → sequence it earlier. |

**Sequencing Decision Table:**

| Uncertainty | Dependency structure | Time pressure | → Sequencing strategy |
|:-----------:|:-------------------:|:-------------:|:---------------------:|
| HIGH | Few dependencies | LOW | **Information-first.** Run the highest-uncertainty bet first. Its outcome determines the rest. |
| HIGH | Few dependencies | HIGH | **Risk-first.** Fail fast on the biggest risk. Don't invest 6 months before discovering the strategy is broken. |
| HIGH | Many dependencies | Any | **Platform-then-explore.** Build the shared dependency first (even if boring), then fan out to uncertain bets in parallel. |
| LOW | Few dependencies | LOW | **Value-first.** Do the highest-impact bet first. With low uncertainty, expected value is a reliable guide. |
| LOW | Few dependencies | HIGH | **Revenue-first.** Generate cash flow to fund the rest. Quick wins before ambitious bets. |
| LOW | Many dependencies | Any | **Critical-path-first.** Sequence by the longest dependency chain. Parallelize everything else. |

**The Counterfactual Test (mandatory for every sequence decision):**

For every "A before B" decision, state:

> "If we did B first instead of A, the consequence would be [specific outcome]. We accept this risk / We cannot accept this risk because [reason]."

A sequence without counterfactuals is not a decision — it's a gut feeling with a timeline attached.

**Option-Value Scoring:**

| Bet | Paths preserved if succeeds | Paths closed if fails | Irreversibility | Option-value score |
|-----|:---------------------------:|:---------------------:|:---------------:|:-----------------:|
| [Bet A] | [count or description] | [count or description] | High / Medium / Low | H/M/L |
| [Bet B] | | | | |

Sequence high option-value bets before low option-value bets when other factors are roughly equal. The bet that preserves the most strategic flexibility should come first.

---

### Framework 4: Strategic Tension Surfacing

The uncomfortable truth about strategy: a roadmap where everything coexists peacefully is a sign that hard decisions were avoided, not that hard decisions were unnecessary. This framework forces tensions into the open.

**Tension Identification Protocol:**

| Question | What it surfaces |
|----------|-----------------|
| Do any two bets need the same senior engineer / designer / PM? | Resource tension |
| Do any two bets pull the product in different strategic directions? (e.g., one bet targets enterprise, another targets self-serve) | Strategic tension |
| Do any two bets both need to be first in the sequence? | Timing tension |
| Does any bet's success make another bet less valuable? | Cannibalization tension |
| Does any bet require a technical architecture decision that constrains another bet? | Platform tension |

**Tension Types and Resolution Patterns:**

| Type | Definition | Resolution options | Anti-pattern |
|------|-----------|-------------------|-------------|
| **Resource tension** | Can't do both with available capacity. Two bets compete for the same people, time, or budget. | (1) Sequence — do one first, (2) Reduce scope on one or both, (3) Hire to relieve the constraint (but name the lead time) | "We'll do both" — without naming what gives. |
| **Strategic tension** | Bets pull in different directions. Pursuing both sends mixed signals to the market, customers, or team. | (1) Choose one direction and defer the other, (2) Segment — pursue both but for different customer segments, (3) Time-box — pursue direction A for 2 quarters, then evaluate direction B | Pretending the tension doesn't exist. |
| **Timing tension** | Both need to go first. Each has a legitimate claim to priority. | (1) Decompose — can a smaller version of one bet run in parallel? (2) Information-first — which one resolves more uncertainty? (3) External forcing function — does a market deadline or competitive move dictate timing? | Alphabetical ordering or "whoever yelled loudest." |
| **Cannibalization tension** | One bet's success undermines another bet's value. New product threatens existing revenue. | (1) Cannibalize yourself — better you than a competitor, (2) Migrate — plan the transition from old to new, (3) Segment — old product for segment A, new for segment B | Refusing to cannibalize yourself, thereby letting competitors do it. |
| **Platform tension** | Architecture decisions for one bet constrain options for another. | (1) Abstract — build a platform layer that serves both, (2) Prioritize — which bet is strategically more important? Build the architecture for that one. (3) Parallel architectures — accept the tech debt if both bets are must-do. | Making an irreversible architecture decision without naming the constraint it creates. |

**Strategic Debt — The Hidden Cost of Tension Resolution:**

Every tension resolution creates strategic debt. Name it.

| Resolution decision | Debt created | Repayment timeline | Cost if not repaid |
|--------------------|-------------|--------------------|--------------------|
| [e.g., "Ship with manual onboarding to hit Q2 deadline"] | [e.g., "Must build self-serve onboarding before scaling beyond 50 customers"] | [e.g., "Q3 — latest Q4 before customer success team is overwhelmed"] | [e.g., "CAC spikes, support costs consume margin, NPS drops below 30"] |

**Anti-pattern detection:**

| Signal | Diagnosis |
|--------|-----------|
| The roadmap contains 0 tensions | Hard decisions were avoided. Probe: "Which two bets compete for the same resources?" If the answer is "none," either the roadmap is under-ambitious or someone is lying about capacity. |
| Every tension is "resolved" by doing both things | Resource fantasy (FM-8). Someone is planning to 120% capacity. |
| Tensions are listed but not resolved | Strategy is incomplete. A tension without a resolution is a decision that hasn't been made — and will be made by default (poorly) during execution. |

---

### Framework 5: The NOT-Doing Section

The most important section of any strategy document. Every roadmap is an implicit claim about what's NOT worth doing — this framework makes that claim explicit.

**NOT-Doing Taxonomy:**

| Category | Definition | Communication frame | Review cadence |
|----------|-----------|--------------------|--------------------|
| **Deferred** | We will do this, but not now. Explicitly scheduled for a future period or gated on a condition. | "This is on our roadmap for [period], contingent on [condition]." | Each quarterly gate. If the condition is met, promote to active. If the condition becomes impossible, move to Declined. |
| **Declined** | We considered this and decided against it. Not on any future roadmap. | "We evaluated this and chose [alternative/nothing] because [reason]. Here's what we'd need to see to reconsider." | Annual strategy review. Only re-open if the "reconsider if" trigger fires. |
| **Deprecated** | We are actively stopping something we currently do. Removing a feature, shutting down a product line, exiting a market. | "We are winding down [X] because [reason]. Migration path is [Y]. Timeline is [Z]." | Monthly until complete. Track customer impact and migration progress. |

**Per-Item Requirements (every NOT-Doing item must have all 5):**

| Component | Why required |
|-----------|-------------|
| **What it is** | Specific enough that any team member knows what's off the table. "Mobile app" not "growth initiatives." |
| **Category** | Deferred, Declined, or Deprecated. Each has different communication and review implications. |
| **Why it's not on the roadmap** | The strategic reasoning. Not "no bandwidth" (that's a resource excuse, not a strategy). The real answer: "This doesn't serve our strategic bets because [reason]." |
| **What we lose by not doing it** | Opportunity cost is not zero. Name the revenue, market position, customer satisfaction, or strategic optionality we forfeit. If the opportunity cost is genuinely zero, it shouldn't even be listed. |
| **Reconsider-if trigger** | An observable condition that would cause us to re-evaluate. This transforms a static "no" into a contingent decision with a watch indicator. |

**Opportunity Cost Assessment:**

| NOT-Doing item | Revenue at stake | Customers affected | Competitive risk | Strategic optionality lost | Total opportunity cost |
|----------------|:----------------:|:------------------:|:----------------:|:-------------------------:|:---------------------:|
| [Item] | $X / unknown | [count/segment] | H/M/L | [description] | H/M/L |

**Decision Table — When to Defer vs. Decline vs. Deprecate:**

| Signal | → Category |
|--------|:----------:|
| "We'd do this if we had more engineers" | Deferred (resource-gated) — schedule for when resources free up, or explicitly decide to never free them up (= Declined) |
| "This doesn't align with our strategic pillars" | Declined — it's not a capacity problem, it's a direction problem |
| "Our data shows no one uses this feature" | Deprecated — actively remove it to reduce maintenance burden and focus |
| "The market isn't ready for this yet" | Deferred (market-gated) — define the market signal that triggers reconsideration |
| "A competitor does this better and we can't differentiate" | Declined — competing on a dimension where you can't win is worse than not competing |
| "We built this for a customer segment we're exiting" | Deprecated — wind down intentionally, don't let it rot |

**Anti-pattern: The Empty NOT-Doing Section**

If the NOT-Doing section contains <3 items, one of three things is true:
1. The team hasn't received enough requests/ideas to say no to (unlikely — probe harder)
2. The roadmap claims to do everything (resource fantasy)
3. The PM avoided the hard decisions and is implicitly deprioritizing by not resourcing, which is worse — it creates false expectations without the honest communication

---

### Framework 6: Resource Allocation & Capacity Planning

The framework that makes strategy real — or exposes it as fantasy. Every strategic bet must be backed by specific people, time, and budget. A bet without resources is a wish.

**The Capacity Model:**

| Allocation bucket | % of total | Purpose | Override rule |
|-------------------|:---------:|---------|---------------|
| **Planned** | 70% | Strategic bets from the roadmap | Core default. Can be overridden to 80% if reactive load is historically low and documented. |
| **Reactive** | 20% | Bugs, customer escalations, operational issues, tech debt | Never less than 15%. If you plan to 85%, a single incident derails a bet. |
| **Exploration** | 10% | Hack weeks, proof-of-concepts, research spikes, emerging opportunities | Can be reduced to 5% during execution crunch. Cannot be 0% for >1 quarter without VP approval. |

**Per-Bet Resource Sizing:**

| Sizing dimension | What to include | Common mistake |
|------------------|----------------|----------------|
| **Engineering** | FTEs, not just headcount. A senior engineer at 50% ≠ a junior at 100%. | Counting headcount without considering seniority mix or ramp time for new hires. |
| **Design** | Include research time, not just production design. Discovery research is a cost, not free. | Assuming design can happen "in parallel" with zero lead time. |
| **PM** | Include cross-functional coordination overhead. A PM on 3 bets is on 0 bets. | Assigning 1 PM to 4 bets and calling each "25% of their time." |
| **Duration** | Estimate in months, not sprints. Strategy operates at month/quarter granularity. | Using sprint estimates that assume zero interruption. |
| **Dependencies** | Other teams whose capacity you need. Name the team, the ask, and the negotiation status. | Assuming cross-team dependencies will "work out." |

**Hiring Lead Time Table:**

| Role level | Time to hire | Time to ramp | Productive capacity | Total lead time |
|-----------|:-----------:|:-----------:|:------------------:|:--------------:|
| Junior engineer | 4-8 weeks | 2-4 weeks | 50% at month 2, 80% by month 4 | 3-5 months |
| Senior engineer | 8-16 weeks | 1-3 weeks | 70% at month 1 | 3-5 months |
| Staff engineer | 12-24 weeks | 2-4 weeks | 70% at month 2 | 4-7 months |
| Product designer | 8-14 weeks | 3-6 weeks | 60% at month 2 | 3-5 months |
| Product manager | 8-16 weeks | 4-8 weeks | 50% at month 2, 80% by month 4 | 4-6 months |

**Key insight:** If a bet requires a new hire and the bet starts in Q1, the hire must be approved and started no later than the prior Q3. A roadmap that says "hire in Q1, ship in Q2" is a fiction.

**Capacity Integrity Check:**

| Check | Pass | Fail |
|-------|------|------|
| Sum of all bet allocations ≤ 70% of total capacity | ✅ Roadmap is executable | ❌ Resource fantasy. Cut scope or defer bets until math works. |
| No individual is allocated >100% across bets | ✅ People are real humans | ❌ Someone is being planned to burnout. Redistribute. |
| Every cross-team dependency has a named contact and agreement status | ✅ Dependencies are managed | ❌ Dependencies are assumed. Get agreements before committing. |
| Hiring-dependent bets include lead time buffer | ✅ Timeline is realistic | ❌ The bet will start late and blame hiring. |

---

### Framework 7: Roadmap Communication & Alignment

Strategy that lives in one person's head isn't strategy — it's a secret. This framework ensures the strategy is communicable to every audience that needs to act on it.

**Audience-Specific Views:**

| Audience | What they need | What to show | What to omit | Confidence framing |
|----------|---------------|-------------|-------------|-------------------|
| **Executive / VP** | Portfolio-level decision. "Are we betting on the right things?" | Strategic bets, portfolio balance, NOT-Doing list, business outcomes, resource asks | Sprint-level scope, technical architecture, design details | Full H/M/L transparency. Executives can handle uncertainty — what they can't handle is being surprised. |
| **Engineering lead** | Technical feasibility and build sequence. "Can we actually build this? In what order?" | Technical dependencies, architecture decisions, team allocation, timeline with milestones | Business strategy rationale beyond what's needed for technical decisions | Frame confidence as technical risk. H = we know how to build this. M = we need a spike. L = research required. |
| **Design lead** | User experience vision and outcomes. "What does the user's world look like when this succeeds?" | User outcomes per bet, experience evolution, research needs, success criteria from user perspective | Resource math, financial projections, competitive intelligence | Frame confidence as user insight confidence. H = validated by research. M = hypothesis from signals. L = assumption to test. |
| **Sales / GTM** | Customer-facing capabilities and competitive positioning. "What can I tell customers? When?" | Customer-visible features, competitive differentiation, timeline for customer-facing capabilities | Internal platform investments, exploration bets, organizational changes | Never give sales an L-confidence feature date. Only share H/M bets with explicit caveats on M. |
| **The team building it** | Clear direction, purpose, and connection to outcomes. "Why are we doing this?" | Vision, the specific bet they own, hypothesis, success criteria, kill criteria, how this fits the bigger picture | Other teams' allocations, executive politics, financial targets they can't influence | Full transparency. The team needs to know when the bet is uncertain — it changes how they build (more flexibility, faster iteration). |

**Alignment Checkpoint Protocol:**

| Cadence | Forum | Purpose | Participants | Output |
|---------|-------|---------|-------------|--------|
| **Monthly** | Strategy check-in | Are we on track? Have signals changed? | PM + eng lead + design lead | Updated confidence levels per bet. Flag any bets where confidence dropped. |
| **Quarterly** | Strategy review | Gate review. Pass/fail against criteria. Rebalance if needed. | PM + leadership + cross-functional leads | Gate decision (continue/pivot/kill per bet). Updated resource allocation if rebalanced. |
| **Trigger-based** | Emergency review | A revision trigger fired. Something changed that breaks a key assumption. | PM + whoever the trigger affects | Decision: revise strategy or absorb the impact. Document the change. |

**Change Management — How the Roadmap Evolves:**

| Change type | Process | Communication |
|-------------|---------|--------------|
| **New information changes a bet's confidence** | Update confidence level. If dropped from H to L, trigger quarterly review early. | Notify affected teams within 48 hours. Explain what changed and what it means. |
| **A bet gets killed at a gate** | Document the kill decision and reasoning. Reallocate resources. Update the NOT-Doing section. | Team-wide communication. Frame as strategic discipline, not failure. Name what the team learned. |
| **A new opportunity emerges mid-quarter** | Evaluate against existing bets using the Bet Scoring Matrix. If it scores higher than an existing bet, propose a swap at the next checkpoint — not mid-sprint. | Don't inject new bets silently. Every addition is a subtraction from something else. Name the trade-off. |
| **External shock (competitor move, market shift, regulation)** | Trigger emergency review. Re-run the relevant section of the strategy (competitive response, regulatory impact). | Fast communication with high signal. "Here's what changed, here's what it means, here's what we're evaluating." |

---

## Evidence Standards

### Evidence Quality Tiers (Strategy-Specific)

| Tier | Source Type | Weight | Strategy example |
|------|-----------|--------|-----------------|
| **Tier 1** | Direct behavioral data from your product or customers | Highest | Usage analytics, revenue data, churn data, A/B test results, customer behavior patterns |
| **Tier 2** | Primary research with credible methodology | High | Customer interviews, structured surveys, win/loss analysis, user research |
| **Tier 3** | Expert analysis with disclosed reasoning | Medium-High | Strategy consultants with data, industry analysis with methodology, academic research |
| **Tier 4** | Industry reports from reputable firms | Medium | Gartner, IDC, Forrester — useful for market sizing, less reliable for strategic insight |
| **Tier 5** | Executive statements, press releases, competitor announcements | Low-Medium | Strategic signaling — analyze what it reveals about their strategy, don't take claims at face value |
| **Tier 6** | Internal assumptions, analogies, inference from limited data | Low | "Based on our experience with product X, we assume..." — useful for hypothesis generation, dangerous for bet-sizing |

**Triangulation Rule for Strategy:** No strategic bet with >20% of total investment should rest on a single evidence tier. Major bets require minimum 2 tiers, ideally 3.

**Strategy-Specific Staleness:** Market strategy evidence degrades faster than competitive intelligence. For fast-moving markets (AI, developer tools, consumer social), evidence >3 months old should be flagged. For stable markets (enterprise infrastructure, healthcare IT), the standard 6-month window applies.

### Leading vs. Lagging Indicators for Strategy

| Category | Lagging (validates past bets) | Leading (informs future bets) |
|----------|-------------------------------|-------------------------------|
| Product | Revenue, MAU, feature adoption rates | Activation velocity of new features, time-to-value for new users, retention cohort slopes |
| Market | Market share, industry revenue | Customer job-to-be-done shift signals, adjacent market growth rates, regulatory movement |
| Team | Velocity, sprint completion rates | Engineering satisfaction surveys, attrition signals, cross-team dependency resolution time |
| Strategic | Bet outcome (success/fail), portfolio ROI | Assumption invalidation rate, gate criteria trending, competitive move frequency |

**Strategy-specific rule:** Leading indicators determine whether to continue a bet. Lagging indicators determine whether the bet paid off. Never use lagging indicators to make forward-looking decisions — by the time revenue data confirms a bet failed, you've spent 2-3 quarters of resources.

### Signal vs. Noise Filter for Strategic Inputs

Before incorporating any market signal, competitive move, or stakeholder request into the strategy:

1. **Frequency:** Is this a recurring signal or a one-off? A single customer request is noise. Five customers requesting the same thing independently is signal.
2. **Source credibility:** Is this from a user who will actually pay/adopt, or from a commentator? Sales team escalations are signal-adjacent (they reflect real conversations but carry attribution bias).
3. **Strategic significance:** Does this change market *structure* (durable — e.g., a new regulation) or market *weather* (temporary — e.g., a competitor's PR stunt)?
4. **Portfolio impact:** If this signal is real, which bets does it affect? If it affects zero existing bets, it's either noise or a signal for a bet you haven't considered yet.
5. **Reversibility:** Can you act on this signal later without penalty? If yes, it can wait for the next quarterly gate. If the window closes, it needs immediate evaluation.

---

## Meta-Frameworks

### The Strategy Stack — Levels of Strategic Decision

Most strategy failures happen because the PM is answering the question at the wrong level. Before building the roadmap, identify which level the decision actually sits at:

| Level | Question | Artifact | Cadence | Who decides |
|-------|----------|----------|---------|-------------|
| **Company strategy** | "What business are we in? What markets do we serve?" | Company strategy memo | Annual | CEO / Board |
| **Product strategy** | "For our product, what do we bet on and in what order?" | Strategy Document (this skill's output) | Annual with quarterly gates | VP Product / PM Lead |
| **Roadmap** | "What do we build this quarter?" | Quarterly roadmap | Quarterly | PM + Eng Lead |
| **Specification** | "How exactly do we build this feature?" | PRD / Spec | Per feature | PM |

**Rule:** This skill operates at Level 2 (Product Strategy). If you're being asked a Level 1 question (company strategy), this skill's frameworks still apply but the stakeholder set and decision authority are different — flag it. If you're being asked a Level 3 or 4 question, this skill is too heavy — redirect to the Specification Writing skill.

### The Strategy Paradox — The Better the Strategy, the Greater the Risk

From Michael Raynor: the best strategies involve the most commitment to a specific path, but commitment is what makes strategies risky. Hedged strategies perform moderately under all scenarios. Committed strategies perform brilliantly if right and catastrophically if wrong.

**Implication for roadmap building:**

| Strategy commitment level | Characteristics | When appropriate | Risk profile |
|--------------------------|----------------|-----------------|-------------|
| **High commitment** | Concentrated bets. >60% of resources on 1-2 bets. Clear direction, minimal hedging. | Vision is validated (H confidence). Market is stable or well-understood. Execution certainty is high. | Highest upside AND highest downside. Kill criteria and quarterly gates are essential insurance. |
| **Moderate commitment** | Balanced portfolio. 40-60% on core, 20-30% on adjacent, 10-15% on transformational. | Vision is directionally right but specifics are uncertain (M confidence). Market is evolving. | Moderate upside, moderate downside. Standard strategy approach for most products. |
| **Low commitment** | Diversified experiments. Many small bets, none commanding >25% of resources. Lots of exploration. | Vision is unclear (L confidence). Market is volatile. Technology is shifting. | Low downside but also low upside per bet. Appropriate for 1-2 quarters during pivots; unsustainable long-term. |

**Decision table — Commitment Level Selection:**

| Vision confidence | Market stability | → Commitment level |
|:-----------------:|:----------------:|:------------------:|
| H | Stable | High commitment — go big on your best bets |
| H | Volatile | Moderate commitment — directionally right but need flexibility |
| M | Stable | Moderate commitment — standard balanced portfolio |
| M | Volatile | Low commitment — explore before committing |
| L | Any | Low commitment — you're in discovery mode, not strategy mode |

### The Roadmap as a Communication Artifact vs. Decision Artifact

A roadmap serves two fundamentally different purposes, and conflating them is a failure mode:

| Purpose | What it optimizes for | Audience | Update cadence | Danger |
|---------|----------------------|----------|---------------|--------|
| **Decision artifact** | Clarity of strategic logic. Bets, sequencing, tensions, kill criteria. Changes when assumptions change. | PM team, eng leads, product leadership | Continuously — the strategy is a living document | If treated as a communication artifact, changes look like "strategy churn" |
| **Communication artifact** | Stakeholder alignment. Timeline expectations, feature commitments, team direction. Changes only at planned gates. | All stakeholders, customers, sales, executive | Quarterly — stability builds trust | If treated as a decision artifact, it becomes rigid and resists adaptation |

**Resolution:** Maintain both. The Strategy Document (this skill's output) is the decision artifact — internal, living, updated as assumptions change. The external roadmap views (audience-specific, from Framework 7) are communication artifacts — updated at quarterly gates, stable between gates, versioned and change-logged.

### Quantified Impact Estimates

| Instead of | Write | Why |
|-----------|-------|-----|
| "Large market opportunity" | "$X B TAM, $Y M addressable given our distribution, Z% CAGR" | Order of magnitude matters. "Large" = 0% information content. |
| "This bet is important" | "This bet targets $X M in incremental ARR with M confidence" | Investment decisions require quantified expected returns, not adjectives. |
| "We need more engineers" | "This bet requires 6 FTEs for 3 quarters = 18 engineer-quarters at ~$X K/quarter loaded cost" | Resource requests without quantification get rejected or granted based on politics, not merit. |
| "We'll ship it in Q3" | "Estimated delivery: late Q3 (P50), end of Q4 (P80), assuming no critical dependency delays" | Single-point estimates are always wrong. Range estimates with probability are actionable. |
| "Good user engagement" | "Target: 30% WAU/MAU ratio by week 8 post-launch, based on [comparable feature launch that achieved 25%]" | Engagement without a benchmark and timeline is meaningless. |

---

## Computation Requirements

⚠️ STRONGLY RECOMMENDED: For portfolio balance calculations:
```
Calculate: Sum(bet_investment) per category / Total_investment = actual percentage
Compare: actual vs. target range (Core 50-70%, Adjacent 20-30%, Transformational 5-15%)
Flag: any category outside target range with deviation magnitude
```

⚠️ STRONGLY RECOMMENDED: For capacity integrity checks:
```
Calculate: Sum(all bet FTE allocations) / Total available FTEs = utilization percentage
Threshold: Must be ≤ 70% (or ≤ 80% with explicit override reasoning)
Flag: any individual allocated > 100%, any bet without named resources
```

If calculation tools are unavailable, state "Manual calculation — verify arithmetic before presenting" and flag which numbers should be double-checked. Do NOT estimate capacity utilization by feel — it is simple arithmetic and must be precise. A 5% error in capacity math is the difference between an executable roadmap and a resource fantasy.

---

## Application Method

### Step 0: Route to Framework Subset (Do This First)

Identify the strategy question type and select load-bearing frameworks before applying any.

| Strategy Question | Prompt Signals | Primary Frameworks | Supporting Frameworks | Skip |
|---|---|---|---|---|
| **Annual/half roadmap** | "annual plan," "FY27 strategy," "H1 roadmap" | Vision-to-Roadmap Cascade, Bet-Sizing, Option-Value Sequencing | Resource Allocation, Communication | — |
| **Quarterly planning** | "Q2 priorities," "this quarter's focus," "what to build next" | Bet-Sizing, Option-Value Sequencing, Resource Allocation | NOT-Doing, Tension Surfacing | Vision-to-Roadmap (vision already set) |
| **Portfolio review** | "rebalance," "are we betting right," "too many initiatives" | Bet-Sizing (Portfolio Balance), Tension Surfacing, NOT-Doing | Resource Allocation | Option-Value Sequencing (reviewing, not sequencing) |
| **New product strategy** | "new product," "0-to-1," "should we build" | Vision-to-Roadmap Cascade, Bet-Sizing, Option-Value Sequencing | ALL — new products need all frameworks | — |
| **Strategic pivot** | "pivot," "strategy isn't working," "need to change direction" | Vision-to-Roadmap (re-vision), Tension Surfacing, NOT-Doing (deprecation) | Bet-Sizing (re-evaluate portfolio) | Communication (communicate after deciding) |
| **Executive review prep** | "board meeting," "leadership review," "strategy presentation" | Communication & Alignment, Portfolio Balance Check | ALL as supporting reference | — (but emphasize Communication framework) |

### Quick Version (8 steps for experienced practitioners)

0. **Route to framework subset** — Identify strategy question type from the table above. Select 3-4 primary frameworks.
1. **Articulate the vision** — 1-2 sentences, falsifiable, time-bound. Apply the Vision Quality Rubric. If vision is 🔴, stop and fix before continuing.
2. **Define 3-5 strategy pillars** — Themes, not features. Each must be load-bearing (remove one → vision becomes unreachable).
3. **Size strategic bets** — For each bet: hypothesis, confidence (H/M/L), investment size, kill criteria. Run Portfolio Balance Check.
4. **Sequence the bets** — Apply the appropriate sequencing logic. State the counterfactual for every sequence decision.
5. **Surface tensions** — Where do bets compete? Apply Tension Identification Protocol. Resolve each tension explicitly.
6. **Write the NOT-Doing section** — ≥3 items, each with category, reasoning, opportunity cost, and reconsider-if trigger.
7. **Build the resource plan** — Per-bet allocation, capacity integrity check, hiring implications. If math doesn't work, go back to step 6 and cut more.
8. **Set quarterly gates** — Per-quarter criteria, adaptation triggers, kill criteria. Write the Executive Summary last.

### Full Version (detailed steps with decision points)

**Step 1: Articulate the Vision**

1. Write a 1-2 sentence vision statement for the product/area over the specified time horizon.
2. Apply the Vision Quality Rubric. Is it 🟢 (falsifiable, time-bound, specific)? If 🟡 or 🔴, iterate until 🟢.
3. State the falsification test: "This vision is wrong if [observable outcome] by [timeframe]."
4. Check the Vision Clarity x Execution Certainty decision table. This determines what type of roadmap you're building.

**Decision point:** If Vision Clarity is LOW, you should not be building a strategy document. Use Problem Framing skill to clarify the vision first.

**Step 2: Define Strategy Pillars**

1. Identify 3-5 themes that bridge the vision to executable work. Pillars are strategic directions, not features or initiatives.
2. Apply the load-bearing test: remove each pillar one at a time. If the vision is still achievable without it, the pillar isn't load-bearing — cut it or merge it.
3. Check for coverage: do the pillars together cover the full scope of the vision? If there's a gap, add a pillar or broaden an existing one.

**Decision point:** If you have >5 pillars, the strategy is too broad. Force-rank and cut to 5 or merge related pillars.

**Step 3: Size Strategic Bets**

For each bet under each pillar:
1. Write the hypothesis: "If we [invest X], then [outcome Y] because [mechanism Z]."
2. Assign confidence (H/M/L) with evidence. Cite evidence tier for the key supporting data.
3. Size the investment: engineers, designers, PMs, months, and monthly burn rate.
4. Define success criteria (specific, measurable, time-bound).
5. Define kill criteria (what observable outcome at what checkpoint means stop).
6. Categorize: Core, Adjacent, or Transformational.
7. Run the Portfolio Balance Check. If the composition is 🟡 or 🔴, rebalance before proceeding.

**Decision point:** If >50% of bets are at L confidence, the strategy is speculative. Consider whether you need more information (Discovery Research, Problem Framing) before committing resources.

**Step 4: Sequence the Bets**

1. Identify dependencies (A must come before B).
2. For non-dependent bets, apply the Sequencing Decision Table based on uncertainty level, dependency structure, and time pressure.
3. For each sequence decision, write the counterfactual.
4. Identify the critical path (longest chain of hard dependencies).
5. Identify information gates (bets whose outcome changes other bets' value).

**Decision point:** If the critical path exceeds the planning horizon, the roadmap has too many sequential dependencies. Parallelize or cut scope.

**Quality checkpoint:** After sequencing, verify: (a) every bet has a clear "start after" condition, (b) no bet is sequenced purely by gut, (c) at least one bet is sequenced for information-generation reasons (not just dependency), (d) the first bet in the sequence is either the highest-risk (to fail fast) or the highest-dependency (to unblock others).

**Step 5: Surface and Resolve Tensions**

1. Run the Tension Identification Protocol (5 questions) against every pair of bets.
2. For each tension found, classify the type (resource, strategic, timing, cannibalization, platform).
3. Apply the resolution pattern for that type. Document the rationale.
4. Name the strategic debt created by each resolution — what did the resolution sacrifice, and when must that debt be repaid?
5. Check for anti-patterns:
   - Zero tensions found → Hard decisions were avoided. Probe: "Which two bets compete for the same resources?"
   - All tensions resolved by "do both" → Resource fantasy. Someone is planning to >100% capacity.
   - Tensions listed but unresolved → Strategy is incomplete. An unresolved tension will be resolved by default (poorly) during execution.

**Decision point:** If a tension is genuinely unresolvable with current information, mark it as an open decision in the strategy document with a deadline for resolution. Do not leave it hanging.

**Step 6: Write the NOT-Doing Section**

1. List every significant request, initiative, direction, or opportunity that was considered but is NOT on the roadmap.
2. Sources for NOT-Doing items: stakeholder requests, competitive gaps, customer feature requests, internal ideas, prior roadmap items that were bumped.
3. For each, assign a category (Deferred, Declined, Deprecated) using the decision table.
4. For each, write: (a) what it is, (b) why it's not on the roadmap — the strategic reasoning, not "no bandwidth," (c) what we lose — the opportunity cost, (d) reconsider-if trigger — what would change our mind.
5. Minimum 3 items. If you can't find 3, you haven't probed hard enough.

**Quality checkpoint:** Read each NOT-Doing item and ask: "Is this item actually higher value than the lowest-value bet on the roadmap?" If yes, swap them. The NOT-Doing section is a strategic integrity check, not a consolation prize for cut features.

**Decision point:** If the NOT-Doing section contains items that are higher-value than items on the roadmap, the roadmap is wrong. Swap them.

**Step 7: Build the Resource Plan**

1. Set the capacity model (70/20/10 or explicit override with reasoning). Document any override: "We are planning to 80% because [specific reason]; the risk is [what happens if reactive load exceeds 20%]."
2. Allocate resources per bet: engineering (with seniority mix), design (including research time), PM (including coordination overhead), duration (months, not sprints).
3. Run the Capacity Integrity Check — all 4 checks must pass:
   - Total allocation ≤ 70% of capacity (or ≤ 80% with documented override)
   - No individual >100% across bets
   - All cross-team dependencies have named contacts and agreements
   - All hiring-dependent bets include lead time buffers
4. Identify hiring needs and apply the Hiring Lead Time Table. If a bet requires a hire and the bet starts in Q1, the hiring process must have started in Q3 of the prior year.
5. List cross-team dependencies with named contacts, agreement status, and fallback if the dependency isn't met.

**Quality checkpoint:** Sum all bet allocations and divide by total available capacity. Show the math in the strategy document. If someone can't verify the capacity check from the numbers in the document, the resource plan is incomplete.

**Decision point:** If the Capacity Integrity Check fails, go back to Steps 3 and 6. Either cut a bet, reduce its scope, or defer it to the NOT-Doing section. Do not proceed with a resource-fantasy roadmap. A strategy that fails the capacity check is a wish list.

**Step 8: Set Quarterly Gates and Write Executive Summary**

1. For each quarter in the planning horizon, define:
   - **Primary bet focus:** Which bet(s) are the priority this quarter?
   - **Pass/fail gate criteria:** Specific, measurable conditions. "Did we achieve X by date Y?" — not "is it going well?"
   - **Adaptation triggers:** What signals tell us to adjust scope or direction mid-quarter (without waiting for the gate)?
   - **Kill criteria:** What observable outcome tells us to stop the bet entirely? This is the most uncomfortable and most important criterion to define.
2. Define the replanning protocol:
   - Monthly strategy check-in: confidence levels updated, signals reviewed
   - Quarterly strategy review: gate decisions, portfolio rebalance, resource reallocation
   - Trigger-based emergency review: a revision trigger fires, forcing immediate re-evaluation
3. Set up audience-specific communication views (see Framework 7).
4. Write the Executive Summary LAST. ≤300 words, zero jargon, final sentence = recommended strategic direction in bold.

**Quality checkpoint:** For each quarterly gate, verify: (a) criteria are specific enough that two people would agree on pass/fail, (b) kill criteria exist — if they don't, the bet can never die, (c) adaptation triggers are observable signals, not vibes.

### Mandatory Output: Assumption Registry

Every strategy document must include a standalone assumption registry. List every load-bearing assumption:

| Assumption | Bets it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|
| [e.g., "Mid-market SaaS will grow 15% YoY for 3 years"] | Bet 1, Bet 3 | M | T4: Gartner forecast | Market growth drops below 8% for 2 consecutive quarters |
| [e.g., "We can hire 4 senior engineers by Q2"] | Bet 2 | M | T6: hiring plan assumption | Fewer than 2 hired by end of Q1 |

Any assumption at L confidence must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the strategy, execute this step before delivering output:

> *"Now identify ≥3 genuine weaknesses in this strategy. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this strategy is catastrophically wrong?"*

- If you cannot find real weaknesses, you haven't looked hard enough.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the scenario analysis — it is a distinct, explicitly adversarial voice.
- Address structural vulnerabilities, not cosmetic risks. "The timeline might slip" is not a weakness. "The entire strategy assumes the mid-market is underserved, but if enterprise customers expand downmarket faster than we grow upmarket, all three bets become irrelevant" is a weakness.

---

## Quality Gradients

### Intern Tier
- A feature backlog with estimated dates
- No strategic logic connecting features to business outcomes
- No confidence levels — everything is stated with equal certainty
- No sequencing rationale — priority is either gut feeling or "loudest stakeholder"
- No NOT-Doing section — the roadmap claims to do everything
- No resource plan — assumes unlimited capacity
- Missing: vision, strategic bets, tensions, quarterly gates, kill criteria

### Consultant Tier
- Clear vision and 3-5 strategy pillars connected to business outcomes
- Bets defined with hypotheses and some confidence indication
- Sequencing based on dependencies but missing option-value reasoning
- Resource plan exists but may not pass the Capacity Integrity Check
- NOT-Doing section exists but may lack opportunity cost quantification
- Quarterly checkpoints defined but kill criteria are vague
- Evidence used but not tiered — Tier 1 data treated same as Tier 5 assumptions
- Missing: counterfactuals, tension surfacing, portfolio balance scoring, adversarial self-critique

### Elite Tier
- Falsifiable vision with explicit falsification test
- Strategic bets with full anatomy: hypothesis, confidence (H/M/L), investment size, kill criteria, evidence tier
- Portfolio Balance Check scored with assessment and action
- Sequencing with counterfactuals for every decision — reader understands why this order AND what would happen if different
- All tensions surfaced, typed, resolved with strategic debt named
- NOT-Doing section with ≥3 items, each carrying category, reasoning, opportunity cost, and reconsider-if trigger
- Resource plan passes all 4 Capacity Integrity Checks
- Quarterly gates with specific pass/fail criteria and kill conditions
- Audience-specific communication views
- Assumption Registry with ≥3 load-bearing assumptions
- Adversarial Self-Critique with ≥3 structural weaknesses
- Revision triggers tied to observable events
- O→I→R→C→W cascades on all strategic recommendations
- H/M/L confidence levels throughout — no weasel words
- Evidence tiered inline — reader knows the quality of every claim's foundation
- Produces an artifact a PM cannot produce unaided — this is the codex test

---

## Failure Modes

**FM-1: Feature Backlog Disguised as Roadmap**
*What it looks like:* A list of features with estimated delivery dates. No strategic logic, no sequencing rationale, no bets with hypotheses. Looks like a roadmap but is actually a project plan.
*Why it happens:* Features are concrete and comfortable. Strategy requires judgment and position-taking. The PM defaults to what they can control (feature scope) rather than what they should decide (strategic direction).
*Detection:* Can you remove 3 items from the roadmap and the "strategy" still makes sense? If yes, there's no strategic logic — the items are independent features, not interdependent bets.
*Correction:* Start with vision and pillars. Derive bets from pillars. Features are evidence that bets are being executed, not the strategy itself.

**FM-2: Vision Without Sequencing**
*What it looks like:* A compelling vision and clear strategic bets, but no answer to "in what order?" The roadmap reads like a shopping list — everything is equally important, nothing has a dependency chain, and the team doesn't know what to build first.
*Why it happens:* Sequencing requires saying "A is more important than B right now," which creates conflict. Avoiding the sequence avoids the conflict.
*Detection:* Ask "which bet do we start if we can only start one?" If the answer requires a meeting, sequencing failed.
*Correction:* Apply the Sequencing Decision Table. Force-rank bets. State counterfactuals for every sequence choice.

**FM-3: Roadmap by Committee**
*What it looks like:* Every stakeholder's priority is on the roadmap. Everything is P0. No hard decisions were made. The roadmap is a political compromise, not a strategic choice.
*Why it happens:* The PM optimized for alignment (no one is upset) rather than strategy (some people should be upset because their thing was cut).
*Detection:* Count the P0s. If >3 items are P0, nothing is P0. Also check: is the NOT-Doing section empty or perfunctory?
*Correction:* Force a portfolio balance. Apply Bet-Sizing with explicit investment percentages. If Core + Adjacent + Transformational must sum to 100%, something has to give. Name what gives.

**FM-4: Priority Inflation**
*What it looks like:* Every bet is "critical" or "strategic." No differentiation between Core (protecting the base), Adjacent (expanding), and Transformational (creating new). All bets carry the same urgency language.
*Why it happens:* Fear of having a bet deprioritized. If everything is critical, nothing can be cut.
*Detection:* Apply the Portfolio Balance Check. If all bets are Core, there's no strategic risk — and no strategic upside. If all bets are labeled "high strategic importance," the scoring rubric wasn't applied honestly.
*Correction:* Use the Bet Scoring Matrix. Force every bet into a cell. Accept that some bets are medium or low importance — that's not a failure, it's strategy.

**FM-5: Missing Counterfactuals**
*What it looks like:* Sequencing is stated but not justified. "We'll do A first, then B" without explaining what would happen if B went first. The sequence feels arbitrary because there's no reasoning behind it.
*Why it happens:* Counterfactual reasoning is cognitively expensive. It's easier to state a preference than to argue why the alternative is worse.
*Detection:* For each sequence decision, ask "why not the reverse?" If the PM can't articulate the consequence, the sequence isn't reasoned.
*Correction:* Apply the Counterfactual Test to every sequence decision. "If we did B first instead of A, the consequence would be [specific outcome]."

**FM-6: Empty NOT-Doing Section**
*What it looks like:* No explicit deprioritization. Either the roadmap claims to do everything (impossible) or the PM avoided naming what's being cut (cowardly). Teams and stakeholders discover their projects were deprioritized when resources never materialize.
*Why it happens:* Saying "no" is politically costly. The PM delays the conflict by being ambiguous about what's not happening.
*Detection:* If the NOT-Doing section has <3 items, the PM didn't try hard enough. If the section is missing entirely, the strategy is incomplete.
*Correction:* For every bet ON the roadmap, ask "what did we choose NOT to do that this bet displaces?" Every yes is an implicit no — make the no explicit.

**FM-7: Annual Plan Without Quarterly Gates**
*What it looks like:* A 12-month roadmap presented as a fixed commitment. No checkpoints, no adaptation points, no kill criteria. The roadmap assumes the world won't change for 12 months.
*Why it happens:* Gates create accountability and the possibility of killing something. Both are uncomfortable. It's easier to set a direction and not look back.
*Detection:* Ask "at what point would we stop pursuing Bet 2?" If the answer is "we wouldn't" or "at the end of the year," there are no gates.
*Correction:* Set quarterly gates with specific pass/fail criteria and kill conditions. Strategy is a series of decisions, not a single decision repeated for 12 months.

**FM-8: Resource Fantasy**
*What it looks like:* The roadmap assumes more engineering capacity than exists, ignores hiring timelines, or plans to 100%+ of available capacity. Every bet is "fully resourced" but the math doesn't add up.
*Why it happens:* Resource constraints are the most common reason bets get cut. The PM avoids the constraint to avoid cutting bets.
*Detection:* Run the Capacity Integrity Check. Sum all bet allocations. If they exceed 70% of total capacity (or 80% with explicit override reasoning), it's a fantasy.
*Correction:* Do the math before presenting the strategy. If it doesn't add up, go back to the NOT-Doing section and cut until it does.

**FM-9: Static Strategy**
*What it looks like:* A roadmap presented as final and fixed when market conditions are volatile. No revision triggers, no adaptation mechanisms, no acknowledgment that assumptions might be wrong.
*Why it happens:* Presenting uncertainty is hard. "Here's our plan, and it might be completely wrong" doesn't inspire confidence. The PM presents false certainty rather than honest uncertainty.
*Detection:* Does the strategy include revision triggers? An assumption registry? Adversarial self-critique? If none of these exist, the strategy claims certainty it doesn't have.
*Correction:* Add the Assumption Registry, Revision Triggers, and Adversarial Self-Critique. These aren't admissions of weakness — they're signs of strategic maturity. A strategy that acknowledges its own assumptions is more trustworthy than one that pretends to be certain.

---

## Visualization & Formatting

### Strategy Document Format Patterns

**Portfolio Balance Visualization:**
```
| Category          | % Investment | Visual              | Target   | Status |
|-------------------|:------------:|---------------------|:--------:|:------:|
| Core              | 55%          | ██████████████░░░░░ | 50-70%   | 🟢     |
| Adjacent          | 30%          | ████████░░░░░░░░░░░ | 20-30%   | 🟢     |
| Transformational  | 15%          | ████░░░░░░░░░░░░░░░ | 5-15%    | 🟢     |
```

**Bet Confidence Visualization:**
```
### 🎯 Bet 1: [Name] — Confidence: H
- **Hypothesis:** [If/then/because]
- **Investment:** [X engineers × Y months]
- **Kill criteria:** [Observable condition at checkpoint]
- **Category:** Core / Adjacent / Transformational
```

**Sequencing Timeline:**
```
Q1          Q2          Q3          Q4
├───────────┼───────────┼───────────┤
│ Bet 1 ████████████│            │            │  (Dependency: unblocks Bet 2)
│           │ Bet 2 ██████████████████│        │  (Info gate: determines Bet 3 scope)
│ Bet 3a ████│          │            │            │  (Exploration: parallel with Bet 1)
│           │           │ Bet 3b ███████████████│  (Conditional on Bet 3a results)
```

**Tension Map:**
```
Bet 1 ←──Resource tension──→ Bet 2
  │                              │
  └──Strategic tension──→ Bet 3

Resolution: Bet 1 and Bet 2 share senior engineer pool.
Decision: Bet 1 gets priority Q1-Q2; Bet 2 starts Q2 with remaining capacity.
Strategic debt: Bet 2 ships 1 quarter late. Must not slip further or Q4 gate is at risk.
```

### Formatting Rules

1. **Lead with tables, not paragraphs.** Every comparison (bets, sequencing, tensions, NOT-Doing) should be a table. Prose explains the table.
2. **Use emoji as visual markers** — 🟢🟡🔴 for portfolio balance assessment, 🎯 for bet headers, ⚠️ for risk flags.
3. **Bold the decision, not the context** — "We are **betting 55% of capacity on enterprise expansion** because..." The bet is the insight, not the background.
4. **Section headers as conclusions** — not "Sequencing" but "Platform Before Features — Architecture Is the Prerequisite." The header IS the strategic conclusion.
5. **Inline evidence tags** — [T2: customer interviews] after every major strategic claim.
6. **End every section with a decision trigger** — "This means we should..." or "Watch for..."
7. **Confidence-coded language** — H-confidence conclusions are stated as decisions. M-confidence as hypotheses. L-confidence as experiments. Never mix confidence levels with assertion levels.

---

## What's Next

← This skill works best after: **Problem Framing** (defines the problem space and customer need) and/or **Competitive Market Analysis** (maps the competitive landscape and market dynamics) and/or **Discovery Research** (provides user evidence and demand-side insights)
→ This skill's output feeds well into: **Specification Writing** (translates strategic bets into specific feature specs), **Narrative Building** (translates strategy into positioning and messaging), **Metric Design & Experimentation** (defines success metrics for strategic bets)
⊕ **Start here if:** You have a defined problem, market context, and need to translate them into an executable roadmap with explicit bets, sequencing, and resource allocation
💡 **For a full product cycle:** Problem Framing → Discovery Research → Competitive Market Analysis → **[THIS SKILL]** → Specification Writing → Metric Design & Experimentation

**Chain interface:**
- **Receives:** Problem definition with customer segment (from Problem Framing), competitive landscape and market dynamics (from Competitive Market Analysis), user evidence and demand signals (from Discovery Research), or raw strategic context (vision, constraints, current state)
- **Produces:** Strategy Document with falsifiable vision, confidence-rated strategic bets, sequenced roadmap with counterfactuals, resource plan, explicit deprioritization, quarterly gates, and assumption registry
- **Handoff artifact:** The Strategy Document's "Strategic Bets" section maps directly to Specification Writing's input (what to spec), Narrative Building's input (what to position), and Metric Design's input (what to measure)

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Gate passed: problem defined, market context available, time horizon appropriate
- [ ] Framework selection done (Step 0) — primary frameworks identified for this question type
- [ ] Vision statement: 1-2 sentences, falsifiable, with explicit falsification test
- [ ] Strategy pillars: 3-5 themes, each load-bearing (remove one → vision unreachable)
- [ ] Strategic bets: each has hypothesis, confidence (H/M/L), investment size, kill criteria
- [ ] Portfolio Balance Check: Core/Adjacent/Transformational composition scored and assessed
- [ ] Sequencing rationale: every sequence decision has a stated counterfactual
- [ ] Critical path identified: which bet, if delayed, delays everything
- [ ] Information gates identified: which bets reveal information that changes other bets' value
- [ ] Strategic tensions surfaced: resource, strategic, timing, cannibalization, platform
- [ ] Each tension resolved with rationale and strategic debt named
- [ ] NOT-Doing section: ≥3 items, each with category, reasoning, opportunity cost, reconsider-if trigger
- [ ] Resource plan: per-bet allocation, capacity model (70/20/10 or override)
- [ ] Capacity Integrity Check: all 4 checks pass
- [ ] Hiring implications stated with lead time buffer
- [ ] Cross-team dependencies named with agreement status
- [ ] Quarterly gates: per-quarter criteria, adaptation triggers, kill criteria
- [ ] Replanning protocol defined (cadence + trigger-based)
- [ ] Communication views: audience-specific emphasis for executive, engineering, design, sales
- [ ] Executive summary: ≤300 words, zero jargon, written LAST, recommended action in bold
- [ ] O→I→R→C→W cascade applied to ALL strategic recommendations
- [ ] H/M/L confidence levels explicit on every strategic bet and conclusion — no weasel words
- [ ] Evidence tiered inline — reader knows the quality of every claim's foundation
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source >6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key bet resting only on Tier 4-6 evidence
- [ ] Assumption Registry present with ≥3 load-bearing assumptions
- [ ] Adversarial Self-Critique section present with ≥3 genuine structural weaknesses
- [ ] Revision Triggers defined with observable events and re-assessment scope
- [ ] Contradictions between bets or frameworks surfaced explicitly, not hidden
- [ ] Reader Navigation section present: How to Read + Notation Key + role-based guide
