---
name: pricing-packaging
description: "Use when designing pricing strategy, packaging tiers, monetization models, or evaluating pricing changes — pricing model selection, willingness-to-pay analysis, competitive pricing maps, package architecture, freemium conversion, usage-based pricing design, or price change impact assessment."
version: "1.0.0"
type: "codex"
tags: ["Monetization", "Strategy", "Growth", "Business Model"]
created: "2026-03-12"
valid_until: "2026-09-12"
derived_from: "original"
tested_with: []
license: "MIT"
capability_summary: "Produces a pricing and packaging strategy document with model selection routing, willingness-to-pay assessment with evidence tiers, competitive pricing map, Good/Better/Best package architecture, sensitivity analysis with revenue impact modeling, and AI/SaaS-specific pricing patterns."
input_schema:
  product: "string — product or feature being priced"
  pricing_context: "enum[new_product, price_change, packaging_redesign, competitive_response, expansion_pricing] — determines framework depth"
  current_pricing: "string — optional, existing pricing if this is a change"
  target_segments: "array[string] — optional, customer segments"
  cost_structure: "string — optional, marginal cost per user/unit, infrastructure costs"
  competitive_pricing: "array[{competitor: string, price: string, model: string}] — optional, known competitor pricing"
output_schema:
  executive_summary: "Zero-jargon pricing recommendation, <=300 words"
  model_selection: "Recommended pricing model with selection rationale"
  wtp_assessment: "Willingness-to-pay range with evidence quality flags"
  competitive_map: "Price-value positioning relative to alternatives"
  package_architecture: "Tier structure with feature allocation rationale"
  sensitivity_analysis: "Revenue impact at +/-10/20/30% from recommendation"
  implementation_plan: "Rollout timeline, grandfathering, communication"
  assumption_registry: "Load-bearing assumptions with confidence levels"
  self_critique: ">=3 genuine weaknesses in this pricing strategy"
example_invocation: "examples/USE_CASES.md"
---

## Purpose

Produce an elite-tier pricing and packaging strategy document that selects the right monetization model, quantifies willingness-to-pay with evidence-graded confidence, maps competitive pricing positions, architects package tiers with conversion-optimized feature allocation, stress-tests revenue sensitivity, and models the impact of pricing changes on existing customers. The output is a Pricing Strategy Document — not a price list, but a structural assessment of what to charge, why, and what breaks if you are wrong.

## When to Use / When NOT to Use

**Use this skill when:**
- Launching a new product and setting initial pricing
- Redesigning packaging tiers or feature allocation across plans
- Evaluating a price increase or decrease on existing customers
- Responding to a competitor's pricing move
- Designing usage-based or hybrid pricing for AI/SaaS products
- Assessing freemium conversion strategy and free-tier boundaries
- Preparing a pricing recommendation for leadership review

**Do NOT use this skill when:**
- You need a competitive landscape analysis (use Competitive Market Analysis skill — this skill includes competitive pricing but as one input, not the sole output)
- You need a full go-to-market strategy (pricing is one dimension; GTM includes channels, messaging, launch sequencing)
- You need financial modeling or P&L projections (this skill produces pricing recommendations with revenue sensitivity, not a financial model)
- You need customer research methodology (use Discovery & Research skill — then feed WTP findings into this skill)

**Anti-inputs (what this skill does NOT handle):**
- Detailed financial modeling or unit economics spreadsheets (this skill produces the pricing strategy that feeds financial models)
- Sales compensation design (adjacent to pricing but separate discipline)
- Contract negotiation tactics (this skill sets the pricing floor and ceiling; negotiation is execution)
- Transfer pricing or internal cost allocation (finance domain, not product pricing)

---

## Context Gate (Step -1)

Before applying any pricing framework, verify that pricing strategy is the right artifact for this problem. Wrong-artifact analysis is more dangerous than wrong-framework analysis.

**Gate questions — answer all four before proceeding:**

| # | Question | If NO | If YES |
|---|----------|-------|--------|
| 1 | Is the core problem actually about pricing/monetization? | STOP. If the problem is adoption, activation, or retention unrelated to price, use Problem Framing or Discovery Research instead. Price changes mask product problems. | Proceed. |
| 2 | Do you have evidence about what customers value? | Flag as `[WTP-EVIDENCE-LIMITED]`. You can still produce a pricing strategy, but WTP ranges will be wide and confidence will be L. Recommend running Discovery Research first. | Proceed with available evidence. |
| 3 | Do you know your cost structure (marginal cost per user/unit)? | Flag as `[COST-STRUCTURE-UNKNOWN]`. Usage-based and hybrid models cannot be responsibly recommended without cost data. Default to seat-based or tiered flat-rate. | Proceed. |
| 4 | Is this a pricing decision or a positioning decision? | If positioning: the real question is "where do we sit relative to alternatives?" — pricing is downstream of that answer. Run Competitive Market Analysis first, then return here with a positioning choice. | Proceed. |

**Context Fitness Check:**

| Pricing Context | Framework Depth | Recommended Output Length |
|----------------|----------------|--------------------------|
| New product pricing | Full (all 7 frameworks) | 3,000-5,000 words |
| Price change evaluation | Focus on Sensitivity + Revenue Impact + Competitive Map | 2,000-3,500 words |
| Packaging redesign | Focus on Package Architecture + WTP + Competitive Map | 2,500-4,000 words |
| Competitive response | Focus on Competitive Map + Sensitivity + Model Selection | 2,000-3,000 words |
| Expansion pricing (new tier/add-on) | Focus on WTP + Package Architecture + Revenue Impact | 2,000-3,000 words |

---

## Reader Navigation

### How to Read This Document

**By time available:**
- **5 minutes:** Read the Executive Summary and the Recommended Pricing Table only. The recommendation and its confidence level are there.
- **15 minutes:** Add Model Selection rationale, Package Architecture summary, and Sensitivity Analysis table. You now understand the what, why, and risk.
- **30+ minutes:** Read the full document. Cross-framework contradictions, assumption registry, and adversarial self-critique give you the complete picture.

**By role:**
- **VP/GM:** Executive Summary + Sensitivity Analysis + Implementation Plan. You need the recommendation, the revenue impact range, and the rollout timeline.
- **PM:** Full document. Every framework application and the package architecture rationale inform your execution decisions.
- **Finance/Rev Ops:** Sensitivity Analysis + Revenue Impact Modeling + Assumption Registry. Validate the numbers and stress-test the assumptions.
- **Sales leadership:** Competitive Pricing Map + Package Architecture + Implementation Plan. You need to know how to position against alternatives and what changes for existing customers.
- **Engineering:** Package Architecture (feature allocation) + AI/SaaS Pricing Patterns (metering requirements). You need to know what to build for billing and usage tracking.

### Notation Key

| Symbol | Meaning |
|--------|---------|
| **H/M/L** | Confidence level: H (>70%), M (40-70%), L (<40%) |
| **(T1)-(T6)** | Evidence tier: T1 = transaction data, T2 = primary research n>=100, T3 = interviews n>=10, T4 = competitive inference, T5 = expert estimation, T6 = model inference |
| **O->I->R->C->W** | Observation -> Implication -> Response -> Confidence -> Watch Indicator |
| `[EVIDENCE-LIMITED]` | Key conclusion rests on T4-T6 evidence only |
| `[POTENTIALLY STALE]` | Source data >6 months old |
| `[WTP-EVIDENCE-LIMITED]` | Willingness-to-pay range based on inference, not direct measurement |
| `[COST-STRUCTURE-UNKNOWN]` | Marginal cost data unavailable; unit economics unverified |
| ████░░░░░░ | Progress bar — visual relative strength (X/10 scale) |

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are quality enforcement mechanisms, not style preferences.

1. **Take positions on price points and models. Never hedge.** "Likely," "may," "could," and "seems" are banned from pricing conclusions. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"The optimal price point is $49/seat/month for the Pro tier (M — assumes mid-market WTP of $40-65 based on T3 interview data)"* not *"The price could be somewhere between $30 and $80."*

2. **Per-cell evidence tier annotation is mandatory in all comparison matrices.** Every cell in a competitive pricing matrix, WTP range table, or feature allocation grid must carry an inline evidence tier tag: `(T1)`, `(T2)`, `(T3)` etc. Where evidence is absent: `(T6: inferred)`. A matrix with untagged cells is incomplete.

3. **The O->I->R->C->W cascade applies to ALL pricing recommendations**, not just final sections. Format: Observation [evidence tier] -> Implication [mechanism] -> Response [specific pricing action] -> Confidence [H/M/L + assumption] -> Watch Indicator [observable signal].

4. **Begin with Model Selection (Step 0) before setting any prices.** Choosing the pricing model is a structural decision that constrains everything downstream. Setting prices before choosing the model is like designing rooms before choosing the building's foundation.

5. **Every price recommendation must include a sensitivity range.** A single price point without "what happens at +/-20%" is a guess, not a strategy. The sensitivity table is mandatory.

6. **Flag time-sensitive claims.** Any competitive pricing data older than 6 months must carry `[POTENTIALLY STALE — verify before acting]`. Competitor pricing changes frequently. Staleness in pricing intelligence is higher-risk than in most other competitive data.

7. **Flag thin-evidence conclusions.** If a WTP estimate or pricing recommendation rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

8. **First reference to any framework includes a one-line contextual explanation.** "Van Westendorp Price Sensitivity Meter — the four-question method for finding the acceptable price range" not just "Van Westendorp."

9. **The Executive Summary uses zero framework jargon.** A VP who has never heard of Van Westendorp, Gabor-Granger, or ERRC must be able to read the summary and make a decision.

---

## Output Template (Mandatory Document Skeleton)

Every Pricing Strategy Document MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was deprioritized in the Context Fitness Check, note "Deprioritized — not primary for this pricing context" in that section.

```markdown
# Pricing Strategy: [Product/Feature Name]

> **Date:** [YYYY-MM-DD] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which competitive pricing data needs revalidation]

---

## Executive Summary

[5 sentences max. Zero jargon. A VP reads only this and approves a pricing decision. Final sentence = the recommended pricing action in bold.]

---

## How to Read This Document

[Reader Navigation block — by time and by role. Copy from the skill's Reader Navigation section and customize for this specific document.]

---

## Step 0: Pricing Model Selection

| Criterion | Assessment | Recommended Model |
|-----------|-----------|-------------------|
| Customer type | [Enterprise / SMB / Consumer / Mixed] | |
| Value delivery | [Per-user / Per-usage / Per-outcome] | |
| Cost structure | [Fixed-heavy / Variable-heavy / Mixed] | |
| Competitive norms | [What model do alternatives use?] | |
| Expansion mechanics | [How does revenue grow within accounts?] | |

**Selected model:** [Model name] because [1-2 sentence rationale].

**Rejected alternatives:** [Which models were considered and why they were rejected.]

---

## 1. Willingness-to-Pay Assessment

**WTP Range:**

| Segment | Floor | Sweet Spot | Ceiling | Evidence | Confidence |
|---------|-------|------------|---------|----------|------------|
| [Segment A] | $X | $Y | $Z | (TX: source) | H/M/L |
| [Segment B] | $X | $Y | $Z | (TX: source) | H/M/L |

**Method used:** [Van Westendorp / Gabor-Granger / Conjoint / Competitive inference / Expert estimation]

**Key finding:** [One sentence — what does the WTP data tell us about pricing power?]

---

## 2. Competitive Pricing Map

| Competitor | Model | Entry Price | Mid Tier | Top Tier | Positioning | Evidence |
|-----------|-------|-------------|----------|----------|-------------|----------|
| [Comp A] | [model] | $X | $Y | $Z | [premium/parity/penetration] | (TX) |
| [Comp B] | [model] | $X | $Y | $Z | [positioning] | (TX) |
| **[Your Product]** | [model] | **$X** | **$Y** | **$Z** | **[positioning]** | |

**Price-Value Position Map:**
[Describe or render: competitors plotted on price (y) x perceived value (x). Identify gaps.]

**Reference price effect:** [What price do customers expect before seeing yours? Why?]

---

## 3. Package Architecture

### Tier Structure

| Dimension | Free / Starter | Pro / Growth | Enterprise |
|-----------|---------------|-------------|------------|
| Target persona | [who] | [who] | [who] |
| Core value proposition | [what job it does] | [what job it does] | [what job it does] |
| Key features | [list] | [list] | [list] |
| Usage limits | [limits] | [limits] | [limits or unlimited] |
| Price | [price] | [price] | [price or "Contact sales"] |
| Upgrade trigger | N/A | [what behavior signals upgrade] | [what behavior signals upgrade] |

### Feature Allocation Rationale

[For each feature placed in a specific tier: WHY it is there, not just THAT it is there. Link to WTP data or conversion incentive logic.]

### Add-On Strategy

| Add-on | Price | Why separate | Target buyer |
|--------|-------|-------------|-------------|
| [Add-on 1] | $X | [rationale] | [who buys this] |

---

## 4. AI/SaaS-Specific Pricing Patterns

[Apply only if relevant. If not an AI or SaaS product, write "Not applicable — [product type] pricing patterns applied instead."]

| Pattern | Assessment | Recommendation |
|---------|-----------|----------------|
| Value metric alignment | [Does price scale with value?] | |
| Marginal cost structure | [Cost per unit at scale] | |
| Usage metering approach | [Per-request / Per-token / Per-outcome] | |
| Bundle vs. unbundle | [Bundle AI into existing? Sell separately?] | |

---

## 5. Sensitivity Analysis

### Revenue Impact at Price Variations

| Scenario | Price | Est. Volume | Conversion Rate | Revenue/Mo | vs. Base |
|----------|-------|-------------|-----------------|------------|----------|
| -30% | $X | [vol] | [rate] | $R | [+/-]% |
| -20% | $X | [vol] | [rate] | $R | [+/-]% |
| -10% | $X | [vol] | [rate] | $R | [+/-]% |
| **Base (recommended)** | **$X** | **[vol]** | **[rate]** | **$R** | **--** |
| +10% | $X | [vol] | [rate] | $R | [+/-]% |
| +20% | $X | [vol] | [rate] | $R | [+/-]% |
| +30% | $X | [vol] | [rate] | $R | [+/-]% |

### Key Variable Sensitivity

| Variable | If wrong by 20% | Impact on recommendation |
|----------|-----------------|------------------------|
| [WTP estimate] | [what changes] | [does the recommended price change?] |
| [Conversion rate] | [what changes] | [does the tier structure change?] |
| [Marginal cost] | [what changes] | [does the model selection change?] |
| [Churn rate] | [what changes] | [does the grandfathering strategy change?] |

---

## 6. Revenue Impact Modeling (for price changes on existing products)

[If new product, write "New product — no existing customer base. Skip to Implementation Plan."]

| Impact Dimension | Estimate | Confidence | Evidence |
|-----------------|----------|-----------|----------|
| Existing customer churn risk | [X% at-risk] | H/M/L | (TX) |
| Grandfathering cost | [$X/mo revenue deferred] | H/M/L | (TX) |
| Expansion revenue uplift | [$X/mo from upgrades] | H/M/L | (TX) |
| Net revenue impact (12-month) | [$X] | H/M/L | |
| Competitive response likelihood | [H/M/L] | H/M/L | (TX) |

---

## 7. Strategic Recommendations (O->I->R->C->W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see]
- **Implication**: [Why it matters — the pricing mechanism]
- **Response**: [Specific pricing action + owner + timeline]
- **Confidence**: [H/M/L] — assumes [key assumption]
- **Watch**: [Observable signal]; if [threshold], re-assess

**Recommendation 2: [Title]**
[Same structure]

**Recommendation 3: [Title]**
[Same structure]

---

## Implementation Plan

| Phase | Timeline | Action | Owner | Risk |
|-------|----------|--------|-------|------|
| Announce | [date] | [what to communicate] | [who] | [risk] |
| Existing customers | [date] | [grandfathering / phase-in / immediate] | [who] | [risk] |
| New customers | [date] | [when new pricing takes effect] | [who] | [risk] |
| Monitor | [date+30d] | [what metrics to track] | [who] | |

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---------------|-----------------|-----------------|------------------------------|
| [e.g., "WTP vs. competitive map"] | [WTP suggests $X] | [Competitive map suggests $Y] | [Which matters more and why] |

---

## Assumption Registry

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|-----------|----------------------|-----------|----------|---------------------------|
| 1 | | | H/M/L | (TX) | |
| 2 | | | H/M/L | (TX) | |
| 3 | | | H/M/L | (TX) | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[Steelmanned argument against this pricing strategy. What assumption is made? What evidence would disprove it? Scenario where this pricing is catastrophically wrong.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---------|-------------------|----------|
| [Observable event] | [Which sections break] | [When to check] |

---

## Sources

[All sources cited in the analysis, with evidence tier and date.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section is not applicable, write "Not applicable — [reason]" and move on.
2. **Every table cell with a price, rate, or claim must have an evidence tier tag** — `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Willingness-to-Pay Analysis") with insight headers (e.g., "Mid-Market WTP Is 2x What We Charge — We Are Leaving Money on the Table") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **The Sensitivity Analysis table is mandatory.** A pricing recommendation without a sensitivity range is a guess.

---

## Domain Frameworks

> This section IS the pricing codex. Each framework is encoded with its scoring rubrics, decision tables, and application methodology — not merely referenced. A PM using this skill produces pricing strategy that requires these frameworks; without them, the output degrades to intuition-based price setting.

### Framework 1: Pricing Model Selection

The foundational decision — choosing the right pricing model constrains every downstream pricing choice. Choose the model BEFORE setting any price points.

**Model Taxonomy:**

| Model | Mechanism | Revenue Predictability | Buyer Predictability | Expansion Mechanic | Best For |
|-------|-----------|----------------------|---------------------|--------------------|----------|
| **Per-Seat** | Charge per named user per period | High (seats x price) | High (fixed monthly cost) | Add more seats | Value scales with users; enterprise procurement-friendly |
| **Usage-Based** | Charge per unit of consumption | Low (variable usage) | Low (unpredictable bills) | More usage = more revenue | Value scales with consumption; API, infrastructure, AI inference |
| **Hybrid (Seat + Usage)** | Base platform fee + consumption overage | Medium | Medium | Both seat expansion and usage growth | Complex products with both user access and variable consumption (AI tools) |
| **Freemium** | Free tier + paid upgrades | Low initially, high at scale | High (free is predictable) | Conversion to paid | Network effects, viral loops, high marginal user cost is LOW |
| **Tiered Flat-Rate** | Fixed price per tier | High | High | Upgrade to higher tier | Clear value steps; SMB self-serve; simple to explain |
| **Marketplace Commission** | % of transaction value | Medium (scales with GMV) | Low (transaction dependent) | GMV growth | Two-sided marketplaces |
| **Outcome-Based** | Charge per outcome delivered | Low (depends on outcomes) | Low (hard to predict) | More outcomes = more revenue | Measurable ROI products; "pay for results" positioning |
| **Enterprise Negotiated** | Custom pricing per deal | Low (deal-dependent) | Low for buyer (opaque) | Annual expansion and renegotiation | High-ACV products; complex value delivery |

**Model Selection Matrix — use this decision table:**

| If your product... | AND your cost structure is... | AND customers are... | THEN consider... |
|--------------------|------------------------------|---------------------|-----------------|
| Delivers value per user (collaboration, productivity) | Fixed-cost heavy | Enterprise buyers who need budget certainty | **Per-Seat** |
| Delivers value per action (API calls, generations, queries) | Variable-cost heavy | Developers or technical buyers comfortable with metering | **Usage-Based** |
| Has both user access value AND variable consumption | Mixed (platform cost + marginal cost per action) | Enterprise/mid-market with both platform and consumption needs | **Hybrid** |
| Has network effects or viral distribution | Near-zero marginal cost per user | Consumer or prosumer, high volume, low barrier | **Freemium** |
| Has clearly distinct value levels | Fixed-cost heavy | SMBs who self-serve and want simplicity | **Tiered Flat-Rate** |
| Facilitates transactions between parties | Transaction-dependent | Marketplace participants | **Marketplace Commission** |
| Delivers measurable, attributable ROI | Outcome-dependent | Results-oriented buyers willing to pay premium | **Outcome-Based** |

**AI-Specific Model Considerations:**

| Factor | Implication | Decision Rule |
|--------|------------|---------------|
| Marginal cost per inference/generation | AI products have non-trivial per-request costs (GPU, token processing) | If marginal cost > 5% of price per unit, usage-based or hybrid is required — pure per-seat creates margin risk at high usage |
| Token-based pricing | Transparent but confusing for non-technical buyers | Use token-based for developer/API products; translate to outcomes or actions for business buyers |
| GPU cost volatility | Costs may decrease 30-50% annually as hardware improves | Build pricing that can capture cost improvements as margin, not auto-pass-through |
| Value attribution | AI value is hard to measure per-unit; output quality varies | Outcome-based pricing works only if outcomes are measurable and attributable |

**Scoring Rubric — Model Fit:**

| Rating | Symbol | Criteria |
|--------|--------|----------|
| **Strong Fit** | 🟢 | Model aligns with value delivery, cost structure, buyer expectations, and competitive norms. No structural conflicts. |
| **Workable** | 🟡 | Model works but has friction points — e.g., usage-based for enterprise buyers who need budget predictability. Mitigations exist. |
| **Poor Fit** | 🔴 | Structural mismatch — e.g., per-seat pricing when value is per-transaction; freemium when marginal cost is high. Do not select. |

**Anti-pattern: Competitor Mimicry.** Choosing a model because the market leader uses it, without analyzing whether your cost structure and value delivery support it. Slack charges per-seat because collaboration value scales with users. An AI analytics tool charging per-seat when value is per-query will either underprice power users or overprice light users.

---

### Framework 2: Willingness-to-Pay Assessment

What customers will actually pay — measured, not guessed. The WTP assessment is the empirical anchor for every price point in the strategy.

**WTP Research Methods (ranked by evidence tier):**

| Method | Evidence Tier | Sample Size | Output | When to Use |
|--------|--------------|-------------|--------|-------------|
| **Transaction data analysis** | T1 | N/A (behavioral) | Revealed price acceptance; conversion by price point | You have existing pricing data or A/B test results |
| **Conjoint analysis** | T2 (if n>=100) | 100-500+ | Trade-off curves: feature importance vs. price | New product with defined feature set; need feature-price trade-offs |
| **Van Westendorp PSM** | T2 (if n>=100) | 100-300+ | Acceptable price range (floor, sweet spot, ceiling) | Need quick WTP range; works for any product |
| **Gabor-Granger** | T2 (if n>=50) | 50-200+ | Demand curve at specific price points | Need price elasticity estimate; fewer questions than conjoint |
| **Customer interviews** | T3 (if n>=10) | 10-30 | Qualitative WTP signals; pain thresholds | Early-stage; need context behind the numbers |
| **Competitive price inference** | T4 | N/A | Implied WTP from competitor pricing | No direct customer data; competitors have validated prices |
| **Expert estimation** | T5 | N/A | Informed guess | No data at all; last resort |
| **Model inference** | T6 | N/A | AI-generated estimate | No other source available |

**Van Westendorp Price Sensitivity Meter — Four Questions:**

1. At what price would this product be **so cheap** you would question its quality? -> **Too Cheap** threshold
2. At what price would this product be a **bargain** — great value for money? -> **Cheap/Good Value** threshold
3. At what price would this product start to feel **expensive** — you'd have to think carefully? -> **Expensive** threshold
4. At what price would this product be **so expensive** you would never consider it? -> **Too Expensive** threshold

**Output — Van Westendorp Range:**

| Metric | Definition | What It Tells You |
|--------|-----------|-------------------|
| **Point of Marginal Cheapness** | Intersection of Too Cheap and Expensive curves | Price floor — below this, perceived quality suffers |
| **Optimal Price Point (OPP)** | Intersection of Too Cheap and Too Expensive curves | Least resistance point — where equal numbers find it too cheap vs. too expensive |
| **Indifference Price Point (IDP)** | Intersection of Cheap and Expensive curves | Normative price — what the market considers "the going rate" |
| **Point of Marginal Expensiveness** | Intersection of Cheap and Too Expensive curves | Price ceiling — above this, demand drops sharply |

**Decision Table — WTP Evidence Quality:**

| Evidence Quality | WTP Range Width | Confidence | Pricing Action |
|-----------------|-----------------|-----------|----------------|
| T1-T2 data (n>=100) | Narrow (+/-10% from sweet spot) | H | Price within sweet spot range; A/B test for optimization |
| T2-T3 data (n>=10-99) | Moderate (+/-20%) | M | Price at lower end of range; plan validation study |
| T4-T5 data (inference/estimation) | Wide (+/-30-40%) | L | `[WTP-EVIDENCE-LIMITED]` — price conservatively; invest in WTP research before committing |
| T6 only (model inference) | Very wide | L | Do not set final pricing on this basis. Use as hypothesis only. |

**Segment-Specific WTP — The One-Price Trap:**

Never assume one price fits all segments. Different customers derive different value and have different alternatives.

| Segment Dimension | Why WTP Differs | How to Measure |
|-------------------|----------------|----------------|
| Company size | Larger companies have higher WTP but also more alternatives and negotiation leverage | Segment Van Westendorp by company size bands |
| Use case | A product used for revenue generation has higher WTP than one used for cost savings | Ask "what would you do without this product?" — the alternative cost IS the WTP ceiling |
| Technical sophistication | Technical users often have lower WTP because they can build alternatives; non-technical users have higher WTP | Compare WTP between self-serve vs. sales-assisted segments |
| Switching position | Customers already invested in a competitor have lower effective WTP (switching cost drag) | Add switching cost estimate to WTP analysis |

---

### Framework 3: Competitive Pricing Map

Where you sit relative to alternatives — and what that positioning implies for your pricing power.

**Competitive Pricing Matrix:**

| Dimension | Competitor A | Competitor B | Competitor C | Your Product |
|-----------|-------------|-------------|-------------|-------------|
| Pricing model | [model] (TX) | [model] (TX) | [model] (TX) | [model] |
| Entry price | $X/mo (TX) | $X/mo (TX) | $X/mo (TX) | $X/mo |
| Mid tier | $X/mo (TX) | $X/mo (TX) | $X/mo (TX) | $X/mo |
| Top tier | $X/mo (TX) | $X/mo (TX) | $X/mo (TX) | $X/mo |
| Free tier? | Yes/No (TX) | Yes/No (TX) | Yes/No (TX) | Yes/No |
| Usage limits | [limits] (TX) | [limits] (TX) | [limits] (TX) | [limits] |
| Annual discount | X% (TX) | X% (TX) | X% (TX) | X% |
| Enterprise pricing | [approach] (TX) | [approach] (TX) | [approach] (TX) | [approach] |

**Price-Value Positioning Map:**

Plot every competitor on two axes:
- **Y-axis: Price** (monthly or annual cost for comparable usage)
- **X-axis: Perceived Value** (feature depth x quality x brand trust)

```
Price ($/mo)
High ───────────────────────────────────────────
     │                          ● Premium Player
     │                 ● Good Value (TARGET ZONE)
     │  ● Overpriced
     │                              ● Enterprise
     │        ● YOUR PRODUCT (current)
     │  ● Bargain/Penetration
Low  ─┼─────────────────────────────────────────
     Low              Perceived Value            High
```

**Positioning Archetypes:**

| Archetype | Price vs. Market | When It Works | When It Fails |
|-----------|-----------------|---------------|---------------|
| **Premium** | 20-50% above market | Strong differentiation, brand, or unique capability | No defensible differentiation; competitor can match and undercut |
| **Parity** | Within 10% of market | Similar value delivery; compete on experience or support | Race to bottom; no margin for investment |
| **Penetration** | 20-40% below market | Land-grab phase; low marginal cost; plan to raise later | Anchors low price expectation; hard to raise; signals low quality |
| **Freemium** | Free entry + paid upgrade | Network effects; viral distribution; low marginal cost | Free tier too generous (no conversion); high marginal cost per free user |

**Reference Price Effect:**

The price customers have in their head before they see yours is the most powerful force in pricing. It is almost always the incumbent's price or the price of the closest substitute.

| Source of Reference Price | Implication | Action |
|--------------------------|------------|--------|
| Incumbent's published pricing | Your price is evaluated relative to theirs, not in absolute terms | If pricing above: justify the premium explicitly. If below: explain why without suggesting lower quality |
| Free alternative exists | WTP is anchored to zero for the base job | You must price the *incremental* value above the free alternative, not the total value |
| Customer's current spend on workarounds | Often hidden but real — spreadsheet time, manual processes, consultant fees | Quantify the workaround cost. Your price should be < workaround cost with room for adoption friction |
| No existing reference | Rare but happens with new categories | You ARE setting the reference price. Choose carefully — it will anchor the entire market |

**Anchoring Decision:** If your product is genuinely 5x better than alternatives, do not price at 2x. You are anchoring to the old product's value delivery. Price at 3-4x and justify the premium with value quantification. Pricing at 2x leaves money on the table AND signals that your product is only incrementally better.

---

### Framework 4: Package Architecture (Good/Better/Best)

Designing tiers and bundles that guide customers toward the tier you want them to buy. Package architecture is conversion engineering, not feature listing.

**The Good/Better/Best Framework:**

| Tier | Purpose | Design Rule | Common Mistake |
|------|---------|-------------|----------------|
| **Good (Free/Starter)** | Acquisition. Experience core value. Create habit. | Enough to accomplish a limited version of the job, not enough for the full job. The limit should be VISIBLE — user hits the wall and understands what upgrade unlocks. | Too generous (no conversion incentive) or too restrictive (no value experienced, user leaves) |
| **Better (Pro/Growth)** | Conversion target. Complete solution for primary use case. | THIS is the tier you want 60-70% of paid customers on. Design the other tiers to make this one look like the obvious choice. | Feature parity with top tier (no reason to upgrade) or missing key features that force users to top tier |
| **Best (Enterprise/Premium)** | Expansion and ARPU. Admin, security, scale, support. | Everything in Better + governance/compliance + premium support + unlimited usage. Price at 2-3x Better tier. | Stuffing features here that belong in Better; creating a "feature hostage" situation |

**Feature Allocation Decision Table:**

For each feature, answer these questions to determine tier placement:

| Question | If YES -> | If NO -> |
|----------|----------|---------|
| Is this required to experience any core value? | Free tier | Move to next question |
| Is this required to complete the primary job-to-be-done? | Pro/Better tier | Move to next question |
| Is this an admin, security, compliance, or governance feature? | Enterprise tier | Move to next question |
| Does this feature primarily benefit power users or teams? | Pro or Enterprise (depends on team vs. individual) | Move to next question |
| Is this a differentiator that justifies premium pricing? | Enterprise or Add-on | Consider removing it — if it is not needed anywhere, it may not be needed at all |

**Upgrade Trigger Design:**

| Trigger Type | Mechanism | Example | Measurement |
|-------------|-----------|---------|-------------|
| **Usage limit** | User hits a quantitative ceiling | 100 queries/mo free, 1000 on Pro | Track % of free users hitting limit monthly |
| **Feature gate** | User attempts action available only on higher tier | "Export to PDF" requires Pro | Track feature-gate encounters per user |
| **Team size** | Collaboration needs exceed free tier | Free = 1 user, Pro = up to 10 | Track invitation attempts by free users |
| **Quality gate** | Free tier has lower quality/speed | Free = standard model, Pro = advanced model | Track quality complaints or upgrade requests citing quality |
| **Time limit** | Trial expires after fixed period | 14-day trial of Pro features | Track conversion rate at trial end |

**Package Naming Conventions:**

| Convention | When to Use | Examples |
|-----------|------------|---------|
| **Functional** (what you get) | B2B SaaS, clarity over personality | Starter / Professional / Enterprise |
| **Persona** (who you are) | When segments map cleanly to tiers | Individual / Team / Organization |
| **Metaphor** (aspiration) | Consumer, brand-forward products | Free / Plus / Premium / Ultra |
| **Size-based** (scale signal) | Usage-based or infrastructure products | Small / Medium / Large / Custom |

**Package Quality Scoring Rubric:**

| Rating | Symbol | Criteria |
|--------|--------|----------|
| **Well-Designed** | 🟢 | Clear upgrade path; 60%+ of paid users on target tier; free-to-paid conversion > 3%; minimal "wrong tier" support tickets |
| **Functional** | 🟡 | Users find the right tier but with friction; some confusion about what is in each tier; conversion rate 1-3% |
| **Broken** | 🔴 | Users cluster on free (too generous) or skip to enterprise (middle tier is hollow); feature allocation creates confusion or resentment |

**Common Package Architecture Failures:**

| Failure | Symptom | Fix |
|---------|---------|-----|
| **Too many tiers** (>4) | Decision paralysis; users don't understand differences | Consolidate to 3 tiers. Use add-ons for edge cases. |
| **Feature parity** | No material difference between adjacent tiers | Move 2-3 high-value features from lower to upper tier |
| **Free tier too generous** | <1% conversion; free users accomplish full job | Reduce free tier scope. Add visible usage limit. |
| **"Feature hostage"** | Essential features locked in top tier to force upgrades | Move essential features to middle tier. Lock only governance/admin/scale in top tier. Users resent hostage pricing; it generates negative WOM. |
| **Price gap too wide** | Users jump from free to nothing — intermediate tier price is 10x free | Create a stepping-stone tier at 2-3x the lower tier |

---

### Framework 5: Sensitivity Analysis & Revenue Modeling

How robust is this pricing? A pricing recommendation without stress-testing is a bet, not a strategy.

**Price Elasticity Estimation:**

| Elasticity | Meaning | Pricing Implication |
|-----------|---------|---------------------|
| **Inelastic** (elasticity < 1) | Demand changes less than proportionally to price changes | You have pricing power. Price increases yield net revenue gains. |
| **Unit elastic** (elasticity = 1) | Demand changes proportionally | Revenue is stable across price changes. Compete on value, not price. |
| **Elastic** (elasticity > 1) | Demand changes more than proportionally | Price sensitivity is high. Small increases cause disproportionate volume loss. |

**Elasticity Estimation Methods (when you lack transaction data):**

| Method | Approach | Reliability |
|--------|---------|-------------|
| Competitor switching data | If 10% price increase causes 15% churn to competitor, elasticity > 1 | T2-T3 |
| Van Westendorp range width | Narrow range = inelastic; wide range = elastic | T2-T3 |
| Customer interview coding | Code responses to "would you still buy at $X+20%?" | T3 |
| Category benchmarks | SaaS averages: -1.0 to -1.5 for horizontal tools; -0.5 to -0.8 for vertical/specialized | T4-T5 |
| Analogous product data | Use elasticity data from similar products in adjacent categories | T4-T5 |

**Revenue Modeling Framework:**

```
Revenue = Price x Volume x Conversion Rate x (1 - Churn Rate)

Per-segment:
Revenue_segment = Price_segment x TAM_segment x Penetration_segment x Conv_segment x (1 - Churn_segment)

Total Revenue = Sum(Revenue_segment) for all segments
```

**Scenario Analysis Table:**

| Scenario | Probability | Revenue Driver | Revenue Impact | Strategic Response |
|----------|:-----------:|---------------|----------------|-------------------|
| 🟢 **Base case** | 50-60% | [Current trends continue] | $X/mo | [Recommended pricing] |
| 🔵 **Bull case** | 15-25% | [What goes right: higher WTP, lower churn, faster adoption] | $Y/mo | [Capture upside: raise prices or expand tiers] |
| 🔴 **Bear case** | 15-25% | [What goes wrong: competitor undercuts, higher churn, lower conversion] | $Z/mo | [Protect: consider grandfathering, add value, delay increase] |

**Break-Even Analysis:**

| Metric | Formula | Decision Rule |
|--------|---------|---------------|
| Break-even volume | Fixed costs / (Price - Variable cost per unit) | If break-even volume > reasonable market penetration, pricing is unsustainable |
| Break-even time | Months to recover CAC at given price and churn rate | If > 18 months for SMB or > 24 months for enterprise, pricing or cost structure needs adjustment |
| Margin per unit | Price - marginal cost (including COGS, hosting, support allocation) | If margin < 60% for SaaS or < 40% for AI products, model may not support growth investment |

**Key Variables Sensitivity — the "What If We Are Wrong?" Test:**

For each variable in the revenue model, test: "If this assumption is wrong by 20%, does the recommendation change?"

| Variable | Base Assumption | If 20% Worse | Changes Recommendation? |
|----------|----------------|-------------|------------------------|
| WTP sweet spot | $X/mo | WTP is actually $0.8X | [Yes/No + what changes] |
| Conversion rate | X% | Conversion is 0.8X% | [Yes/No + what changes] |
| Churn rate | X%/mo | Churn is 1.2X%/mo | [Yes/No + what changes] |
| Marginal cost/user | $X | Cost is $1.2X | [Yes/No + what changes] |
| Addressable market | X users | Market is 0.8X | [Yes/No + what changes] |

**Decision rule:** If 2+ variables being wrong by 20% changes the recommendation, the strategy is fragile. Widen the confidence band and recommend phased rollout with monitoring gates.

---

### Framework 6: Revenue Impact Modeling (Price Changes)

What happens when you change prices on an existing product with existing customers. This framework is not needed for new product pricing — use Sensitivity Analysis instead.

**Existing Customer Impact Decision Framework:**

| Strategy | Mechanism | When to Use | Risk |
|----------|-----------|------------|------|
| **Grandfathering** | Existing customers keep old price indefinitely | Price increase > 30%; loyal customer base; churn is more costly than deferred revenue | Revenue uplift is slow; creates two pricing tiers to manage; new customers subsidize old |
| **Phase-in** | Existing customers migrate to new price over 6-12 months | Moderate increase (10-30%); relationship matters; customers need time to budget | Still causes churn at phase-in date; delays full revenue capture |
| **Immediate** | All customers move to new price at renewal | Small increase (<10%); competitive position demands it; product value has increased materially | Churn spike at renewal; negative sentiment; support ticket surge |
| **Value-add** | Increase price but add features/value to justify it | Any increase size; strongest when you have new capabilities to bundle | If added value is not perceived as valuable by customers, they see through it |

**Churn Risk Assessment:**

| Signal | Churn Risk Level | Pricing Action |
|--------|-----------------|----------------|
| NPS > 50 AND low competitive alternatives | Low (< 5% incremental churn) | Proceed with increase; monitor monthly |
| NPS 30-50 OR moderate competitive alternatives | Medium (5-15% incremental churn) | Phase-in or value-add; do not go immediate |
| NPS < 30 OR strong competitive alternatives at lower price | High (> 15% incremental churn) | Grandfather or delay; fix product/value perception first |

**Net Revenue Impact Formula:**

```
Net Impact = (New Revenue from Increase) - (Lost Revenue from Churn) - (Grandfathering Cost)

Where:
- New Revenue = (New Price - Old Price) x Remaining Customers
- Lost Revenue = Old Price x Churned Customers x Remaining Contract Months
- Grandfathering Cost = (New Price - Old Price) x Grandfathered Customers x Grandfathering Duration
```

**If Net Impact is Negative:** The price increase destroys more value than it creates. Either: (a) the increase is too large, (b) the product's value perception does not support the new price, or (c) competitive alternatives are too strong at the lower price. Do not proceed.

**Expansion Revenue Assessment:**

| Expansion Mechanic | How It Works | Metric |
|-------------------|-------------|--------|
| Seat expansion | More users in existing accounts | Net seat growth rate (new seats - churned seats) |
| Usage growth | Existing users consume more | Usage growth rate per account |
| Tier upgrades | Users move to higher tiers | Upgrade rate (% of users upgrading per quarter) |
| Add-on attach | Users buy additional modules | Attach rate (% of users with add-ons) |
| Price increase | Higher price on same product | Net dollar retention after price change |

**Net Dollar Retention (NDR) Target:**

| NDR | Interpretation | Pricing Health |
|-----|---------------|----------------|
| > 130% | Revenue from existing customers grows 30%+ annually without new customers | 🟢 Pricing supports excellent expansion. Likely room to raise prices. |
| 110-130% | Healthy expansion — growth from upsell and usage offsets churn | 🟢 Pricing is working. Monitor for churn acceleration. |
| 100-110% | Expansion roughly offsets churn | 🟡 Pricing is neutral. Look for expansion mechanic improvements. |
| < 100% | Losing revenue from existing customers | 🔴 Pricing or product problem. Do NOT raise prices. Fix retention first. |

---

### Framework 7: AI/SaaS-Specific Pricing Patterns

Modern pricing challenges for products with AI inference costs, usage-based value delivery, and rapid capability evolution.

**Usage Metering Decision Table:**

| Metering Approach | Best For | Buyer Experience | Implementation Complexity |
|------------------|---------|------------------|--------------------------|
| **Per-request** | API products; discrete actions (generate image, run query) | Simple to understand; easy to estimate cost | Low — count requests |
| **Per-token (input + output)** | LLM-based products; text generation | Technical buyers understand; non-technical buyers confused | Medium — need token counting |
| **Per-outcome** | Products where output quality varies (code generation, analysis) | Best buyer experience but hard to define "outcome" | High — need outcome measurement |
| **Per-seat + usage cap** | Products with both access value and consumption value | Predictable base cost; clear on overages | Medium — billing combines fixed + variable |
| **Credit-based** | Products with multiple action types at different costs | Flexible; abstracts underlying costs | Medium — need credit exchange rates |

**Value Metric Alignment Rule:**

The price metric should scale with the value the customer receives. If the customer gets 10x more value, they should pay approximately 3-5x more (not 10x — you share the surplus to maintain adoption).

| Alignment Test | Question | If Misaligned |
|---------------|---------|---------------|
| Does price increase when value increases? | "If a customer gets 2x more value from our product next month, do they pay more?" | If no: you have flat pricing on a variable-value product. Revenue will not scale with customer success. |
| Does price decrease when value decreases? | "If a customer gets less value one month, do they pay less?" | If no: you are overcharging underserved customers. Churn risk. |
| Can the customer predict their bill? | "Can a buyer estimate next month's cost within 20%?" | If no: usage-based pricing creates "bill shock." Add spending caps, alerts, or committed-use discounts. |

**Freemium Conversion Benchmarks:**

| Metric | Benchmark (SaaS industry) | Interpretation |
|--------|--------------------------|----------------|
| Free-to-paid conversion rate | 2-5% (median 3%) | Below 2% = free tier too generous or paid value unclear. Above 5% = strong upgrade triggers. |
| Time to conversion | 14-60 days (median 30) | > 60 days = free tier allows too much exploration without hitting a wall |
| Revenue per free user (RPFU) | $0 (but track for viral/referral value) | Free users who refer paid users have quantifiable value |
| Free user marginal cost | < $1/user/month ideally | If > $3/user/month, freemium model may be uneconomical |

**Cost Transparency Decision:**

| Model | Transparency Level | Why |
|-------|-------------------|-----|
| Usage-based | High — show cost structure openly | Buyers expect to understand what drives their bill; opacity creates distrust |
| Seat-based | Low — price is the price | Buyers expect fixed pricing; exposing cost structure invites negotiation |
| Enterprise | Medium — show value drivers, not cost | Enterprise buyers care about ROI, not your margins |

**Bundle vs. Unbundle Decision:**

| Scenario | Bundle | Unbundle |
|----------|--------|----------|
| AI feature adds clear value to existing product | 🟢 Bundle into existing tiers; justify price increase | 🔴 Unbundling a core improvement feels like nickel-and-diming |
| AI feature serves a different use case/persona | 🔴 Bundling dilutes the new capability's value | 🟢 Sell separately; capture full WTP for the new use case |
| AI feature has high marginal cost per use | 🔴 Bundling creates margin risk — heavy users subsidized by light users | 🟢 Usage-based pricing aligns cost and revenue |
| AI feature is table stakes (every competitor has it) | 🟢 Bundle — don't let it become a negotiation point | 🔴 Unbundling table stakes looks like a money grab |

**Enterprise Pricing Floor:**

| Input | How It Sets the Floor |
|-------|----------------------|
| Marginal cost per enterprise user | Floor >= marginal cost x 3 (need margin for R&D, sales, support) |
| Total deal economics | Floor = (CAC + implementation cost + support cost) / (expected contract months x users) |
| Competitive enterprise pricing | Floor >= 70% of lowest enterprise competitor (below this, perceived as unserious) |
| Internal precedent | Floor >= highest existing enterprise deal price (never anchor backward) |

---

### Analytical Lenses (Applied Across All Frameworks)

#### Price Elasticity by Segment

Never assume uniform elasticity. Different segments respond differently to price changes.

| Segment | Typical Elasticity | Pricing Implication |
|---------|-------------------|---------------------|
| Enterprise (>1000 employees) | Low elasticity (0.3-0.7) | Pricing power; can charge premium; buyers negotiate on terms, not price |
| Mid-market (100-1000) | Moderate (0.7-1.2) | Price-sensitive but value-aware; package architecture matters most |
| SMB (<100 employees) | High (1.2-2.0) | Very price-sensitive; self-serve pricing must be simple and competitive |
| Developer/technical | Variable (0.5-1.5) | Will pay for quality but resent opaque pricing; respect transparency |
| Consumer | High (1.5-3.0) | Extreme price sensitivity; free alternatives always an option |

#### The Value Metric Ladder

Map how value delivery connects to price across the product lifecycle:

```
[Free: Experience core value] -> [Starter: Accomplish basic job] -> [Pro: Complete primary job] -> [Enterprise: Scale, govern, customize]
                                     |                                    |                              |
                                   $X/mo                              $Y/mo                          $Z/mo or custom
                                     |                                    |                              |
                               Upgrade trigger:                    Upgrade trigger:               Upgrade trigger:
                               Usage limit hit                     Team size or                   Compliance, SSO,
                                                                   advanced features              audit, custom SLAs
```

#### Pricing Psychology Principles

| Principle | Mechanism | Application |
|-----------|-----------|-------------|
| **Charm pricing** | $49 feels significantly cheaper than $50 | Use .99 or .95 endings for self-serve; use round numbers for enterprise (signals confidence) |
| **Anchoring** | First number seen sets the reference point | Show highest tier first on pricing page; enterprise → pro → starter |
| **Decoy effect** | A less attractive option makes the target option look better | If you want buyers on Pro, make the Starter tier slightly less attractive per dollar |
| **Loss aversion** | Losing $X feels 2x worse than gaining $X | Frame price increases as "keeping current features" not "paying more"; frame discounts as "saving" not "getting less" |
| **Round number bias** | Buyers allocate budget in round numbers | Price at $49, $99, $199 — just under the round number budget threshold |

---

## Evidence Standards

### Evidence Quality Tiers for Pricing

| Tier | Source Type | Weight | Example |
|------|-----------|--------|---------|
| **Tier 1** | Transaction data — what customers actually paid | Highest | Conversion rates by price point, A/B test results, actual deal sizes, churn after price change |
| **Tier 2** | Primary WTP research with adequate sample | High | Van Westendorp n>=100, conjoint analysis, Gabor-Granger studies |
| **Tier 3** | Customer interviews, small-sample research | Medium-High | 10-30 customer interviews about pricing, sales team win/loss data on pricing |
| **Tier 4** | Competitive pricing data, industry reports | Medium | Published competitor pricing pages, analyst reports on market pricing |
| **Tier 5** | Expert estimation, executive judgment | Low-Medium | PM's estimate based on domain experience, advisor input |
| **Tier 6** | Model inference, no direct evidence | Low | AI-generated pricing estimate with no grounding data |

**Triangulation Rule:** No pricing recommendation rests on a single evidence tier. Minimum 2 tiers, ideally 3. A recommendation based only on competitive pricing (T4) without any WTP data (T2-T3) is a competitive copy, not a pricing strategy.

---

## Application Method

### Step 0: Route to Framework Subset (Do This First)

Identify the pricing context and select load-bearing frameworks before applying any.

| Pricing Context | Prompt Signals | Primary Frameworks | Frameworks to Deprioritize |
|----------------|---------------|-------------------|---------------------------|
| **New product pricing** | "launching new product", "what to charge", "initial pricing" | Model Selection, WTP, Competitive Map, Package Architecture | Revenue Impact (no existing customers) |
| **Price change** | "raise prices", "reduce price", "repricing" | WTP, Sensitivity, Revenue Impact, Competitive Map | Model Selection (model is already chosen) |
| **Packaging redesign** | "redesign tiers", "new packages", "feature allocation" | Package Architecture, WTP, Competitive Map | Revenue Impact (if only structure changes, not price) |
| **Competitive response** | "competitor lowered price", "new competitor pricing" | Competitive Map, Sensitivity, WTP, Model Selection | Package Architecture (unless competitor's packaging is the threat) |
| **Expansion pricing** | "new tier", "add-on pricing", "enterprise tier" | WTP, Package Architecture, Competitive Map, AI/SaaS Patterns | Revenue Impact (unless cannibalizing existing tiers) |

### Quick Version (8 steps for experienced practitioners)

0. **Run Context Gate** — Verify pricing is the right artifact. Check evidence availability. Set confidence band.
1. **Select pricing model** — Use the Model Selection Matrix. Choose the model before setting any price.
2. **Assess willingness-to-pay** — Apply the best available WTP method. Flag evidence tier. Produce WTP range per segment.
3. **Map competitive pricing** — Build the Competitive Pricing Matrix. Plot the Price-Value Position Map. Identify the reference price.
4. **Design package architecture** — Apply Good/Better/Best. Allocate features using the Decision Table. Design upgrade triggers.
5. **Apply AI/SaaS patterns** — If applicable: check value metric alignment, metering approach, bundle/unbundle, cost transparency.
6. **Run sensitivity analysis** — Build the revenue impact table at +/-10/20/30%. Test key variable sensitivity. Identify fragile assumptions.
7. **Model revenue impact** — For price changes: assess churn risk, grandfathering cost, expansion revenue. Calculate net impact.
8. **Cascade every finding to a recommendation** — O->I->R->C->W for each pricing action.

### Full Version (detailed steps with decision points)

**Step 1: Select Pricing Model**

Do not set prices before choosing the model. The model constrains every downstream decision.

1. Identify your product's value delivery pattern (per-user, per-usage, per-outcome)
2. Identify your cost structure (fixed-heavy, variable-heavy, mixed)
3. Identify your buyer type (enterprise procurement, SMB self-serve, developer, consumer)
4. Check competitive norms (what model do alternatives use? deviation from norms requires justification)
5. Apply the Model Selection Matrix
6. Score each candidate model using the Fit Rubric (Strong/Workable/Poor)
7. Select the model with the highest fit. If two models score equally, choose the simpler one.

**Decision point:** If the highest-scoring model is 🟡 (Workable) rather than 🟢 (Strong Fit), document the friction points and mitigation plan. If all models score 🟡 or 🔴, the product's value delivery may not be well-defined — return to Problem Framing.

**Step 2: Assess Willingness-to-Pay**

1. Inventory available evidence by tier (T1 transaction data? T2 research? T3 interviews? T4+ inference?)
2. Apply the highest-tier WTP method available (see the methods table)
3. Produce segment-specific WTP ranges: floor, sweet spot, ceiling per segment
4. Flag evidence quality: narrow range (H confidence) vs. wide range (L confidence)
5. If WTP evidence is T4+ only, flag the entire WTP section as `[WTP-EVIDENCE-LIMITED]`

**Decision point:** If WTP floor > competitive pricing ceiling, you have strong pricing power — price for value capture. If WTP ceiling < competitive pricing floor, you are in a commodity position — price for volume and differentiate on other dimensions.

**Step 3: Map Competitive Pricing**

1. Collect pricing data for 3-5 primary competitors (use published pricing pages, sales intel, industry reports)
2. For each competitor: model, entry price, mid tier, top tier, free tier, usage limits, annual discount, enterprise approach
3. Tag every data point with evidence tier and date
4. Plot the Price-Value Position Map
5. Identify the reference price (the number in the buyer's head before they see yours)
6. Determine your positioning archetype: premium, parity, penetration, or freemium

**Decision point:** If your WTP sweet spot is 20%+ above the highest competitor's comparable tier, you have a value premium. If your WTP sweet spot is within 10% of the market average, you are in parity — differentiate on packaging, not price.

**Step 4: Design Package Architecture**

1. Define 3 tiers using Good/Better/Best
2. For each feature, apply the Feature Allocation Decision Table
3. Design upgrade triggers for each tier transition
4. Check for common failures (too many tiers, feature parity, free tier too generous, feature hostage, price gap too wide)
5. Name the tiers using the appropriate convention (functional, persona, metaphor, or size-based)
6. Score the package architecture against the Package Quality Rubric

**Decision point:** If 60%+ of expected paid customers would rationally choose the top tier (not the middle tier), the middle tier is underdesigned. Redistribute features to make the middle tier the clear choice.

**Step 5: Run Sensitivity Analysis**

1. Build the revenue table at -30%, -20%, -10%, base, +10%, +20%, +30%
2. For each price variation, estimate: volume impact, conversion rate impact, churn impact
3. Calculate revenue per scenario
4. Identify the price point that maximizes revenue (not the price point that maximizes conversion — these are usually different)
5. Run the Key Variables Sensitivity test: for each assumption, check "if wrong by 20%, does the recommendation change?"
6. If 2+ variables being wrong by 20% changes the recommendation, widen the confidence band

**Step 6: Cascade to Recommendations**

For EVERY pricing finding, structure as O->I->R->C->W:

```
OBSERVATION [evidence tier] -> IMPLICATION [pricing mechanism] -> RESPONSE [specific pricing action + owner + timeline] -> CONFIDENCE [H/M/L + key assumption] -> WATCH INDICATOR [observable signal that tells you if this is wrong]
```

**Bad:** "We should raise our price."

**Elite:** "Mid-market customers report WTP of $45-65/seat/month [T3: 22 customer interviews, Jan 2026], 40% above our current $35/seat pricing, because they quantify time savings at 5+ hours/week per analyst [mechanism: value-based WTP exceeds cost-based pricing]. Response: raise Pro tier to $49/seat/month effective Q3 2026, with 90-day grandfather window for existing annual contracts [specific action + timeline]. Confidence: M — assumes competitive pricing remains stable [Tableau at $70, Looker at $60]; if either drops below $45 within 6 months, re-assess. Watch: competitor pricing page changes; if any primary competitor drops below $45, trigger competitive response analysis within 48 hours."

### Mandatory Output: Assumption Registry

Every pricing strategy document must end with a standalone assumption registry:

| Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|-----------|----------------------|-----------|----------|---------------------------|
| [e.g., "Enterprise WTP is $80-120/seat based on 15 interviews"] | WTP Assessment, Package Architecture | M | T3: 15 interviews | New competitor enters at $40/seat with comparable features |
| [e.g., "Marginal cost per AI inference stays below $0.02 for 12 months"] | Model Selection, Sensitivity | M | T4: GPU cost trends | GPU costs increase due to supply constraints or model size growth |

Any assumption at L confidence must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the analysis, execute this step before delivering output:

> *"Now identify >=3 genuine weaknesses in this pricing strategy. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this pricing is catastrophically wrong?"*

- If you cannot find real weaknesses, you have not looked hard enough.
- Bear cases must be steelmanned — argued as forcefully as possible.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the sensitivity analysis.

---

## Quality Gradients

### Intern Tier
- Lists competitor prices and suggests "we should be somewhere in the range"
- No evidence tiers — treats competitor pricing pages and executive guesses equally
- One-price-fits-all — no segment-specific analysis
- No sensitivity analysis — single price recommendation with no stress testing
- Missing: WTP assessment, package architecture rationale, revenue impact modeling
- Feature allocation by gut feel — no decision framework for what goes in which tier

### Consultant Tier
- Applies WTP methodology (Van Westendorp or similar) with documented sample
- Competitive pricing mapped with model and tier breakdown
- Package architecture with clear Good/Better/Best rationale
- Sensitivity analysis at +/-20% with revenue impact estimates
- Segment-specific pricing where segments have different WTP
- Evidence tiered — distinguishes interview data from competitive inference
- Includes counterfactuals — "what if we're wrong" for major assumptions
- Missing: AI/SaaS-specific patterns, per-cell evidence annotation, O->I->R->C->W cascades, adversarial self-critique

### Elite Tier
- All 7 frameworks applied with scoring rubrics and decision tables
- Per-cell evidence annotation in every matrix
- WTP assessment with explicit method, sample size, and confidence band per segment
- Model selection with structural rationale (not competitor mimicry)
- Package architecture with feature allocation decision table applied to every feature
- AI/SaaS-specific patterns applied (metering, value metric alignment, bundle/unbundle, cost transparency)
- Sensitivity analysis at +/-10/20/30% with key variable testing
- Revenue impact modeling with churn risk, grandfathering, and expansion revenue
- Every recommendation in O->I->R->C->W cascade with H/M/L confidence
- Adversarial self-critique with >=3 steelmanned weaknesses
- Assumption registry with >=3 load-bearing assumptions and invalidation conditions
- Cross-framework contradictions surfaced (e.g., WTP says price up but competitive map says market won't bear it)
- Revision triggers with specific observable events
- Produces pricing strategy a PM cannot produce unaided — this is the codex test

---

## Failure Modes

**FM-1: Cost-Plus Pricing**
*What it looks like:* Price set by calculating costs + desired margin. "$15 cost + 60% margin = $24 price." No WTP assessment, no competitive context, no value-based reasoning.
*Why it happens:* Cost data is available; WTP data is not. Agent defaults to what it can calculate.
*Detection:* If the pricing recommendation does not reference willingness-to-pay or competitive alternatives, it is cost-plus.
*Correction:* Always start with WTP and competitive map. Cost is a floor (price must exceed cost), not a ceiling or a formula. The question is not "what does this cost to deliver?" but "what is this worth to the customer?"

**FM-2: Competitor Mimicry**
*What it looks like:* "Slack charges $12.50/seat, so we should charge $10-15/seat." Pricing model and price points copied from a competitor without analyzing whether your cost structure, value delivery, and customer base support it.
*Why it happens:* Competitor pricing is visible and feels like market validation. Designing from first principles is harder.
*Detection:* If the model selection rationale is "because [competitor] uses this model" without structural analysis, it is mimicry.
*Correction:* Apply the Model Selection Matrix. A competitor's pricing reflects their cost structure, scale, and strategic intent — not yours. Slack charges per-seat because collaboration value scales linearly with users. If your value scales with usage, per-seat pricing will misalign.

**FM-3: WTP Without Evidence**
*What it looks like:* "We think customers will pay $50/month" with no methodology, no sample, no research. The WTP estimate is an executive guess treated as a data point.
*Why it happens:* WTP research takes time and budget. The pressure to "just set a price" is real.
*Detection:* If the WTP section does not cite a methodology and sample size, it is an unsupported guess.
*Correction:* Flag as `[WTP-EVIDENCE-LIMITED]`. At minimum, run 10 customer interviews (T3 evidence). Never present a T5-T6 estimate as a T2 finding.

**FM-4: One-Price-Fits-All**
*What it looks like:* Same price for all customers despite different segments having different WTP, different use cases, and different alternatives. "$29/month for everyone."
*Why it happens:* Segmented pricing is complex to implement and explain. Single pricing feels simpler.
*Detection:* If the WTP assessment does not segment by company size, use case, or buyer type, segmentation is missing.
*Correction:* At minimum, segment WTP by company size (SMB/mid-market/enterprise). If WTP varies by > 2x between segments, tiered or segment-specific pricing is required.

**FM-5: Free Tier Too Generous**
*What it looks like:* Free tier covers the complete primary use case. Users accomplish their full job without paying. Conversion rate < 1%.
*Why it happens:* Product team wants maximum adoption. "If we just get users, monetization will follow." It rarely does when the free tier solves the whole problem.
*Detection:* If a free user can accomplish the primary job-to-be-done without hitting a visible limit or feature gate, the free tier is too generous.
*Correction:* Identify the upgrade trigger — what specific limit or feature gate makes a free user want to pay? If no clear trigger exists, the free tier needs to be reduced.

**FM-6: Price-Value Misalignment**
*What it looks like:* Product delivers 10x value (measured by time savings, revenue impact, or alternative cost) but charges 1x. Or charges 10x but delivers 3x. Both are failures — the first leaves money on the table, the second drives churn.
*Why it happens:* Value quantification is skipped. Pricing is set based on "what feels right" or competitor anchoring without measuring the actual value delivered.
*Detection:* If the analysis does not quantify the value the product delivers (in dollars or hours saved) and compare it to the price, value alignment is unchecked.
*Correction:* Always calculate the value ratio: (value delivered) / (price charged). Target 3-10x value/price ratio. Below 3x: pricing is too aggressive. Above 10x: pricing is too conservative.

**FM-7: Missing Sensitivity Analysis**
*What it looks like:* Pricing recommendation of "$49/month" with no analysis of what happens at $39 or $59. No stress testing, no scenario analysis, no "what if we're wrong."
*Why it happens:* Agent produces a point estimate and declares it the recommendation. Sensitivity testing requires additional analysis.
*Detection:* If the output has a single recommended price without a range or sensitivity table, this failure mode is active.
*Correction:* Mandatory sensitivity table at +/-10/20/30% from recommended price. Mandatory key variable sensitivity test.

**FM-8: Ignoring Marginal Costs**
*What it looks like:* AI product priced at $20/month when marginal cost per user is $18/month. At scale, the unit economics are $2/user — not enough to cover CAC, R&D, or support.
*Why it happens:* AI products have deceptively high marginal costs (GPU inference, token processing). Traditional SaaS pricing intuition (near-zero marginal cost) does not apply.
*Detection:* If the pricing recommendation does not include a margin-per-unit calculation that accounts for AI/inference costs, this failure mode is active.
*Correction:* Calculate margin per unit at scale. If margin < 40% for AI products, either raise the price or move to usage-based pricing that passes variable costs through.

**FM-9: Price Change Without Churn Modeling**
*What it looks like:* "Raise prices 25% effective immediately." No churn risk assessment, no grandfathering analysis, no net revenue impact calculation. Just the increase.
*Why it happens:* Revenue pressure drives the price increase. The assumption is "customers won't leave." They will.
*Detection:* If a price change recommendation does not include: (a) churn risk estimate, (b) grandfathering strategy decision, and (c) net revenue impact, it is incomplete.
*Correction:* Apply the Revenue Impact Modeling framework. Calculate: will the increase yield net-positive revenue after accounting for churn? If not, either reduce the increase or improve the value proposition first.

---

## What's Next

<- This skill works best after: **Problem Framing** (defines the market and customer segments), **Discovery & Research** (provides WTP data from customer interviews), **Competitive Market Analysis** (provides competitive landscape and positioning context)
-> This skill's output feeds well into: **Narrative Building** (pricing positioning for launch communications), **Specification Writing** (billing system requirements, tier logic), **Metric Design** (pricing experiment setup, conversion metrics)
+ **Start here if:** You need to set or change pricing, design packages, or evaluate a monetization model
💡 **For a full product cycle:** Problem Framing -> Discovery & Research -> Competitive Market Analysis -> **[THIS SKILL]** -> Spec Writing -> Metric Design

**Chain interface:**
- **Receives:** Product definition with target segments and value proposition (from Problem Framing), WTP interview data (from Discovery Research), competitive landscape with positioning choices (from Competitive Market Analysis), or raw pricing question
- **Produces:** Pricing Strategy Document with model selection, WTP-grounded price points, package architecture, sensitivity analysis, and implementation plan
- **Handoff artifact:** The Pricing Strategy's "Package Architecture" section maps directly to Spec Writing's input (billing system requirements). The "Strategic Recommendations" section maps to Narrative Building's input (pricing positioning for launch). The "Sensitivity Analysis" feeds Metric Design's input (A/B test design for pricing experiments).

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Gate passed — pricing is the right artifact for this problem
- [ ] Pricing model selected with structural rationale (not competitor mimicry)
- [ ] WTP assessed with methodology, sample size, and confidence band per segment
- [ ] WTP range includes floor, sweet spot, and ceiling — not a single point estimate
- [ ] Competitive pricing mapped: model, tiers, pricing, positioning for 3-5 competitors
- [ ] Price-Value Position Map plotted — gaps and positioning identified
- [ ] Reference price effect identified — what buyers expect before seeing your price
- [ ] Package architecture designed with Good/Better/Best rationale
- [ ] Feature allocation uses decision framework (not gut feel)
- [ ] Upgrade triggers defined for each tier transition
- [ ] Add-on strategy included (what stays outside all tiers)
- [ ] AI/SaaS patterns applied if relevant: metering, value metric alignment, bundle/unbundle
- [ ] Sensitivity analysis at +/-10/20/30% from recommended price
- [ ] Key variable sensitivity tested: "if wrong by 20%, does recommendation change?"
- [ ] Revenue impact modeled for price changes: churn risk, grandfathering cost, net impact
- [ ] Expansion revenue mechanics identified (seat, usage, tier upgrade, add-on)
- [ ] Implementation plan: timeline, grandfathering strategy, communication plan
- [ ] Executive summary: 5 sentences, zero jargon, VP can act on it alone
- [ ] Every recommendation uses O->I->R->C->W cascade
- [ ] Per-cell evidence tier annotation in ALL comparison matrices
- [ ] H/M/L confidence levels explicit on every pricing conclusion — no weasel words
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source > 6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any pricing conclusion resting only on Tier 4-6
- [ ] Assumption Registry present with >=3 load-bearing assumptions
- [ ] Adversarial Self-Critique present with >=3 genuine weaknesses
- [ ] Cross-framework contradictions surfaced (e.g., WTP vs. competitive map disagree)
- [ ] Revision Triggers present with specific observable events
- [ ] Reader Navigation included (by time and by role)
- [ ] Notation Key included

---

## Worked Example

### Input

> "We're building an AI-powered code review tool (CodeLens AI) for mid-market engineering teams. Currently in beta with 200 users at $0/month. Competitors: GitHub Copilot ($19/seat/month), Sourcery ($15/seat/month for teams), CodeRabbit ($15-39/seat/month). Our marginal cost per user is approximately $8/month (GPU inference for code analysis). We need to set initial pricing and package tiers for GA launch."

---

### Output (abbreviated — demonstrates key formats; a full pricing strategy would cover all 7 frameworks)

**Executive Summary (5 sentences):**
CodeLens AI should launch with three tiers — Free (5 reviews/week), Pro at $24/seat/month, and Enterprise at $49/seat/month — positioning as the premium AI code review tool that catches structural issues, not just style violations. The $24 Pro price sits above Sourcery ($15) and below Copilot ($19 for broader functionality) because CodeLens delivers specialized value that merits a premium over code-review-only tools but competes on a narrower scope than full AI coding assistants. Mid-market engineering leads report WTP of $20-35/seat/month for tools that reduce review cycle time by 40%+ (based on 18 beta user interviews), and our $24 price sits in the sweet spot of that range. The free tier is deliberately limited to 5 reviews/week — enough to experience the "aha moment" of an AI catching a real bug, not enough to replace human reviewers for a team. **Launch at $24/seat/month (Pro) with a 6-month introductory rate of $19 for beta participants transitioning to paid.**

---

**Pricing Model Selection:**

| Criterion | Assessment | Score |
|-----------|-----------|-------|
| Value delivery | Per-review (each review is a discrete value unit) but teams buy per-seat | 🟡 Hybrid possible |
| Cost structure | $8/user/month marginal (GPU) — high for SaaS | 🔴 Per-seat risk if heavy users |
| Buyer expectation | Dev tools market uses per-seat; teams budget per-developer | 🟢 Per-seat aligned |
| Competitive norms | Copilot, Sourcery, CodeRabbit all per-seat | 🟢 Per-seat is norm |
| Expansion mechanic | More developers = more seats | 🟢 Per-seat natural |

**Selected model:** Per-seat with usage guardrails (review volume cap per tier) because competitive norms and buyer expectations strongly favor per-seat, but the $8/month marginal cost requires usage limits to prevent margin erosion from power users (H).

**Rejected: Pure usage-based** — developer tool buyers expect predictable costs; usage-based creates budget anxiety for engineering managers. **Rejected: Pure freemium** — $8/user marginal cost makes unlimited free tier uneconomical.

---

**Competitive Pricing Map:**

| Dimension | GitHub Copilot | Sourcery | CodeRabbit | **CodeLens AI** |
|-----------|:---:|:---:|:---:|:---:|
| Model | Per-seat (T1) | Per-seat (T1) | Per-seat (T1) | **Per-seat** |
| Individual | $10/mo (T1) | Free (T1) | $15/mo (T1) | **Free (5 rev/wk)** |
| Team/Pro | $19/mo (T1) | $15/mo (T1) | $15-24/mo (T1) | **$24/mo** |
| Enterprise | $39/mo (T1) | Custom (T4) | $39/mo (T1) | **$49/mo** |
| Free tier scope | Code completion (T1) | Individual only (T1) | None (T1) | **5 reviews/wk** |
| Key differentiator | Broad AI coding assist (T1) | Python-focused auto-refactor (T1) | AI PR review (T1) | **Structural issue detection** |

**Reference price effect:** Engineering managers comparing CodeLens to Copilot will anchor to $19/seat. Our $24 premium requires explicit justification: "CodeLens catches architectural issues Copilot misses" — this is the positioning narrative, not "we're $5 more expensive."

---

**Package Architecture:**

| Dimension | Free | Pro ($24/seat/mo) | Enterprise ($49/seat/mo) |
|-----------|------|------|------|
| Target | Individual devs evaluating | Engineering teams 5-50 | Engineering orgs 50+ |
| Reviews/week | 5 | 200 | Unlimited |
| Upgrade trigger | Hits 5-review wall by day 3 | Team admin features, SSO | Compliance, audit logs, SLA |
| Key features | Core review, 3 languages | All languages, team dashboard, Jira integration | SSO, SAML, audit log, custom rules, dedicated support |

**Feature allocation rationale:** The free tier's 5-review/week limit is calibrated to $8/user marginal cost economics — at 5 reviews/week, estimated cost is ~$2/user/month, acceptable for acquisition. The Pro tier's 200 reviews/week covers 95th percentile usage (T3: beta usage data shows median 40 reviews/week, P95 at 180) so most Pro users never hit the cap.

---

**Sensitivity Analysis:**

| Scenario | Price | Est. Users (12-mo) | Conversion | Revenue/Mo | vs. Base |
|----------|-------|---------------------|-----------|------------|----------|
| -30% | $17/seat | 800 | 8% (T5) | $1,088 | -27% |
| -20% | $19/seat | 700 | 7% (T5) | $931 | -38% |
| **Base** | **$24/seat** | **600** | **5% (T5)** | **$720** | **--** |
| +20% | $29/seat | 450 | 4% (T5) | $522 | -28% |
| +30% | $31/seat | 380 | 3% (T5) | $353 | -51% |

**Key finding:** Revenue maximizes at the lower price points (high conversion volume), but margin maximizes at $24+ due to the $8 marginal cost. At $17/seat, margin is only $9/seat — insufficient to cover CAC. **The $24 price is the margin-optimized choice, not the revenue-maximized choice (M).**

---

### Why This Works

This output was produced by running Steps 1 (Model Selection), 3 (Competitive Map), 4 (Package Architecture), and 5 (Sensitivity Analysis) of the Full Application Method. It satisfies the Elite Tier Quality Gradient: WTP is grounded in evidence (T3 beta interviews) with explicit confidence bands, the competitive map has per-cell evidence tier annotations, the package architecture uses the feature allocation decision framework rather than gut feel, and the sensitivity analysis reveals that $24 optimizes for margin (not revenue) — an uncommon-knowledge finding that requires the framework to surface.

---

## References

**Framework Sources:**
- Thomas Nagle & Georg Muller, *The Strategy and Tactics of Pricing* (6th edition) — pricing strategy foundations
- Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016) — WTP assessment, packaging design
- Peter van Westendorp, "NSS Price Sensitivity Meter" (1976) — Van Westendorp method
- Andre Gabor & Clive Granger, "Price as an Indicator of Quality" (Economica, 1966) — Gabor-Granger method
- Patrick Campbell (ProfitWell/Paddle), pricing research methodology and SaaS benchmarks
- Kyle Poyar (OpenView Partners), usage-based pricing research and benchmarks
- Steven Forth (Ibbaka), value-based pricing frameworks
- NFX, *The Network Effects Manual* — network effects impact on freemium viability

**Related Skills in PM Skills Arsenal:**
- Competitive Market Analysis — upstream (provides competitive landscape and positioning)
- Discovery & Research — upstream (provides WTP data from customer interviews)
- Problem Framing — upstream (defines market and customer segments)
- Narrative Building — downstream (uses pricing positioning for launch)
- Specification Writing — downstream (billing system requirements)
- Metric Design & Experimentation — downstream (pricing experiment design)

---

*Created: 2026-03-12 | PM Skills Arsenal v1.0.0*
*Quality tier: Elite (1200+ lines, 7 encoded frameworks, quality gradients, 9 failure modes)*
*License: MIT*
