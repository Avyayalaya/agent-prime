---
name: competitive-market-analysis
description: "Use when performing competitive analysis, market entry assessment, moat evaluation, positioning strategy, build/buy/partner decisions, or responding to a competitor move. Encodes 7 Powers, Aggregation Theory, Christensen Disruption, JTBD, Wardley Mapping, and evidence-tier standards. Produces a Competitive War Map artifact."
version: "1.3.0"
type: "codex"
tags: ["Analyze", "Strategy", "Market Intelligence"]
created: "2026-02-18"
valid_until: "2026-08-18"
derived_from: "shared/toolkits/competitive_analysis.md"
tested_with: ["Claude Sonnet 4", "Claude Opus 4"]
license: "MIT"
---

## Purpose

Produce an elite-tier competitive and market analysis that scores every competitor against 7+ strategic frameworks, decomposes moats by type, identifies disruption vectors with evidence-graded confidence, and delivers board-ready artifacts a PM cannot produce unaided. The output is a Competitive War Map — not a feature comparison, but a structural assessment of who wins, why, and what to do about it.

## When to Use / When NOT to Use

**Use this skill when:**
- Entering a new market or evaluating a competitive response
- Preparing a strategy review, board deck, or investment memo
- A competitor makes a significant move and you need structural analysis (not reactive commentary)
- Building a positioning strategy (feeds into Narrative Building skill)
- Evaluating build/buy/partner decisions where competitive dynamics matter
- Assessing moat durability for your own product or a competitor's

**Do NOT use this skill when:**
- You need a quick feature comparison table (just ask for one directly)
- The "competitor" is internal (use Problem Framing skill instead)
- You need pricing analysis only (this skill includes pricing but as one GTM dimension, not the sole output)
- You need user research (use Discovery & Research skill — that's demand-side primary research, this is market-side structural analysis)

**Anti-inputs (what this skill does NOT handle):**
- Customer interview synthesis (→ Discovery & Research skill)
- Product specification decisions (→ Spec Writing skill)
- Statistical analysis of experiment results (→ Outcome Measurement skill)
- Internal organizational strategy (this is external-facing competitive intelligence)

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are not style preferences — they are quality enforcement mechanisms derived from benchmarking against investment-grade analyst output.

1. **Take positions. Never hedge with weasel words.** "Likely," "may," "could," and "seems" are banned. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"Visier's free tier is a benchmark data flywheel play, not a price move (H)"* not *"Visier may be trying to build data advantages."*

2. **Per-cell evidence tier annotation is mandatory in all comparison matrices.** Every cell in a feature matrix, switching cost decomposition, or 7 Powers heat map must carry an inline evidence tier tag: `(T1)`, `(T2)`, `(T3)` etc. Where evidence is absent: `(T6: inferred)`. A matrix with untagged cells is incomplete.

3. **The O→I→R→C→W cascade applies to ALL strategic recommendations**, not just final sections. Format: Observation [evidence tier] → Implication [mechanism] → Response [specific action] → Confidence [H/M/L + assumption] → Watch Indicator [observable signal].

4. **Begin with Framework Selection (Step 0)** before applying any framework. Identify the question type; select the 3-4 load-bearing frameworks; note which to skip. Applying all 9 frameworks to a moat defense question dilutes signal and inflates length.

5. **Contradictions between frameworks are signal, not noise.** When two frameworks reach different conclusions (e.g., 7 Powers says moat is strong but COAP says profits are shifting away), surface the contradiction explicitly and state which to weight more heavily and why.

6. **Flag time-sensitive claims.** Any claim based on data older than 6 months must carry `[POTENTIALLY STALE — verify before presenting]`. Tier labels alone are insufficient; recency matters independently of source quality.

7. **Flag thin-evidence conclusions.** If a key strategic conclusion rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

8. **Every framework reference gets a one-line contextual explanation the first time it appears.** Not "Hamilton Helmer's 7 Powers" but "Helmer's framework for scoring 7 types of competitive moat — we use it here to assess which advantages are durable vs. eroding." The framework name is for the author's rigor. The reader needs to know why this lens matters for *their* decision.

9. **The document must be navigable by someone who didn't create it.** Include a reading guide (by time and by role), a notation key, and layered depth. A VP should be able to read only the Executive Summary and act. A PM should be able to read through Findings and skip Deep Analysis. The full document is for the analyst.

---

## Output Template (Mandatory Document Skeleton)

Every Competitive War Map MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was skipped in Step 0, note "Skipped — not load-bearing for this question type" in that section.

```markdown
# Competitive War Map: [Subject — e.g., "SMB HR Analytics Market Entry"]

> **Date:** [YYYY-MM-DD] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which key claims need revalidation]

---

## Executive Summary

[5 sentences max. A VP reads only this and makes a decision. No framework names, no jargon, no evidence tier tags. Plain language a non-PM exec can act on. Final sentence = the recommended action in bold.]

---

## How to Read This Document

**What this is:** A structural competitive assessment — not a feature comparison. It uses strategic frameworks to assess which advantages are durable, where value is migrating, and what to do about it.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | The decision + recommended action |
| **15 min** | Executive Summary + Findings (sections 1-4) | Key structural conclusions with evidence |
| **30 min** | Full document through Recommendations | Complete analysis with supporting frameworks |
| **Deep dive** | Everything including Appendix | Full framework applications, assumptions, self-critique |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Summary | Recommendations (section 10), Assumption Registry | Everything in between |
| PM Lead | Executive Summary | Findings (sections 2-5), Recommendations | Deep framework sections, Worked Examples |
| Strategy / Analyst | Full document in order | Cross-Framework Contradictions, Adversarial Self-Critique | Nothing — this is your primary artifact |
| Engineer / Designer | Executive Summary | Tactical Layer (section 8) for feature/capability matrix | Framework sections (unless building competitive tooling) |

---

## Notation Key

**Confidence levels** — applied to every strategic conclusion:
- **H (>70% confident)** — Strong evidence supports this conclusion. Act on it.
- **M (40-70%)** — Direction is probable but evidence is mixed. Validate before committing resources.
- **L (<40%)** — This is a hypothesis, not a finding. Do not act without further evidence.

**Evidence tiers** — how we know what we claim to know (tagged inline as T1-T6):
- **T1** — Direct behavioral data: usage analytics, revenue, SEC filings, job postings (strongest)
- **T2** — Primary research: well-sampled surveys, structured interviews
- **T3** — Expert analysis with disclosed reasoning: Stratechery, a16z, academic papers
- **T4** — Industry reports: Gartner, IDC, Forrester (useful for sizing, less for insight)
- **T5** — Executive statements and press releases (strategic signaling, not facts)
- **T6** — Punditry, blog posts, social media, or first-principles reasoning (weakest)

**Competitive power ratings:**
- 🟢 **Strong** — Mature, actively accruing, 3+ years to replicate
- 🟡 **Moderate** — Exists but nascent, eroding, or limited in scope
- 🔴 **Weak/Absent** — No meaningful competitive barrier

**Recommendation format** (O→I→R→C→W):
- **O**bservation — What we see (with evidence tier)
- **I**mplication — Why it matters (the mechanism)
- **R**esponse — What to do (specific action + owner + timeline)
- **C**onfidence — How sure we are (H/M/L + key assumption)
- **W**atch — How to know if we're wrong (observable signal)

**Flags:**
- `[POTENTIALLY STALE]` — Source data is >6 months old; verify before presenting
- `[EVIDENCE-LIMITED]` — Conclusion rests on T4-T6 evidence only; validate with stronger data before acting

---

## Step 0: Context Fitness Check

Before selecting frameworks, verify that a Competitive War Map is the right artifact for this question.

| Question | If Yes | If No |
|---|---|---|
| **Is the core problem external (competitive) or internal (activation/adoption)?** | Proceed to Framework Selection | A Competitive War Map is the wrong artifact. Consider: Activation Strategy Map (internal adoption problem), Metric Framework (measurement problem), or Problem Framing. |
| **Do you have access to internal behavioral data (T1-T2)?** | Analysis can produce H-confidence conclusions | Flag prominently: "External-view analysis only. All conclusions are hypotheses — validate against internal telemetry before acting." Cap confidence at M for structural claims. |
| **Is distribution through user choice or IT/enterprise provisioning?** | Standard competitive dynamics apply | Competitive set must include "do nothing," "existing workflow," and "the user's own inertia." Distribution competition is irrelevant — the battle is awareness → activation → habit. |
| **Is the product standalone or a feature of a larger platform?** | Analyze as independent product | The product inherits the platform's powers AND constraints. Competitive analysis must account for bundle dynamics, cross-subsidy, and the fact that the product may not need to "win" independently. |

**If any answer is "No":** State this prominently at the top of the Executive Summary. Example: *"Note: This analysis is produced from public sources only (T3-T5). All structural conclusions should be treated as hypotheses to be validated against internal data before strategic action."*

---

## Step 0b: Framework Selection

| Question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Market entry decision"] | [e.g., 7 Powers, COAP, JTBD] | [e.g., Blue Ocean, Wardley] | [e.g., "Win/Loss — no existing deals to analyze"] |

---

## 1. Competitive Set

| Tier | Competitors | Rationale |
|---|---|---|
| **Primary** (full analysis) | [3-5 names] | [Why these are direct substitutes] |
| **Secondary** (scan) | [3-6 names] | [Adjacent players expanding toward you] |
| **Non-obvious / H3** | [2-3 names] | [Different paradigm entirely] |

---

## 2. 7 Powers Heat Map

| Power | [Competitor A] | [Competitor B] | [Competitor C] | [Your Product] |
|---|:---:|:---:|:---:|:---:|
| Scale Economies | 🟢/🟡/🔴 (TX) | | | |
| Network Effects | | | | |
| Counter-Positioning | | | | |
| Switching Costs | | | | |
| Branding | | | | |
| Cornered Resource | | | | |
| Process Power | | | | |
| **Accruing / Eroding** | [direction] | [direction] | [direction] | [direction] |

📊 [Inline evidence citations for key ratings]

**Decision point:** [e.g., "No competitor holds >2 strong powers → market is structurally contestable."]

---

## 3. Switching Cost Decomposition

| Type | [Competitor A] | [Competitor B] | [Your Product] |
|---|:---:|:---:|:---:|
| Financial/Contractual | ████░░░░░░ X/10 (TX) | | |
| Data/Migration | | | |
| Workflow/Integration | | | |
| Identity | | | |
| Learning/Procedural | | | |
| Relational/Trust | | | |
| Social/Community | | | |

**Key insight:** [Customer-created vs. vendor-imposed distinction. Strategic implication.]

---

## 4. Aggregation & Disruption Analysis

**Aggregation Theory:**
| Question | Finding | Evidence |
|---|---|---|
| Who owns the user relationship? | | (TX) |
| Marginal costs approaching zero? | | (TX) |
| Which layers commoditizing? | | (TX) |

**Christensen COAP:**
| Test | Evidence | Assessment |
|---|---|---|
| Serves non-consumers? | | ✅/❌/⚠️ |
| "Good enough" for the job? | | ✅/❌/⚠️ |
| Incumbent can't respond? | | ✅/❌/⚠️ |
| Trajectory toward mainstream? | | ✅/❌/⚠️ |

**Decision point:** [Where are profits shifting? Who is vulnerable?]

---

## 5. Strategy Reverse-Engineering (Where to Play / How to Win)

| Competitor | Stated Strategy | Revealed Strategy | Gap |
|---|---|---|---|
| [A] | | | |
| [B] | | | |

**Wardley Map Findings:** [Key misallocations — custom effort on commodity, or commoditizing genesis.]

---

## 6. Blue Ocean Check

**Strategy Canvas:** [Describe or render the value curve comparison across key factors.]

**ERRC Grid:**
| Eliminate | Reduce | Raise | Create |
|---|---|---|---|
| [factors] | [factors] | [factors] | [factors] |

---

## 7. Adoption Stage Assessment

| Question | Finding |
|---|---|
| TAL position | [Innovators / Early Adopters / Early Majority / Late Majority] |
| Chasm status | [Pre-chasm / In the chasm / Crossed] |
| Whole product gap | [What's missing for mainstream adoption?] |
| Bowling alley head pin | [Specific beachhead segment + rationale] |

---

## 8. Tactical Layer

**Feature/Capability Matrix:**

| Capability | Strategic Weight | [Comp A] | [Comp B] | [Your Product] |
|---|:---:|:---:|:---:|:---:|
| [Capability 1] | H/M/L | ✅/🔄/🚧/❌ (TX) | | |
| [Capability 2] | | | | |

**GTM & Distribution Comparison:**

| Dimension | [Comp A] | [Comp B] | [Your Product] |
|---|---|---|---|
| Pricing model | | | |
| Free tier | | | |
| Enterprise motion | | | |
| Distribution channel | | | |
| Bundle leverage | | | |

**Customer & User Signals:**
- [Signal 1] 📊 (TX: source)
- [Signal 2] 📊 (TX: source)

---

## 9. Win/Loss Pattern Mapping

| Pattern | Structural Cause | Framework Attribution |
|---|---|---|
| [e.g., "Losing enterprise deals on security"] | [e.g., "Branding gap — no SOC2 narrative"] | 7 Powers: Branding |

---

## 10. Strategic Recommendations (O→I→R→C→W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see]
- **Implication**: [Why it matters — the mechanism]
- **Response**: [Specific action + owner + timeline]
- **Confidence**: [H/M/L] — assumes [key assumption]
- **Watch**: [Observable signal]; if [threshold], re-assess

**Recommendation 2: [Title]**
- **Observation** [TX]: ...
- **Implication**: ...
- **Response**: ...
- **Confidence**: ...
- **Watch**: ...

**Recommendation 3: [Title]**
[Same structure]

---

## Three Horizons Threat Landscape

| H1 (0-12mo) | H2 (12-36mo) | H3 (36mo+) |
|---|---|---|
| [Direct threats] | [Adjacent expansion] | [Paradigm shifts] |
| [Response] | [Response] | [Response] |

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---|---|---|---|
| [e.g., "Moat strength vs. profit trajectory"] | [7 Powers: strong moat] | [COAP: profits shifting away] | [Which matters more and why] |

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
[Steelmanned argument against the analysis. What assumption is made? What evidence would disprove it? Scenario where this recommendation is catastrophically wrong.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| [Observable event] | [Which sections break] | [When to check] |

---

## Sources

[All sources cited in the analysis, with evidence tier and date.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Skipped — [reason]" and move on.
2. **Every table cell with a rating or claim must have an evidence tier tag** — `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Switching Cost Analysis") with insight headers (e.g., "Looker's Lock-In Is Customer-Created — Ours Isn't") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **Progress bars** (`████░░░░░░`) are mandatory in the Switching Cost Decomposition. Do not substitute with text ratings.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology — not merely referenced. A PM using this skill produces analysis that requires these frameworks; without them, the output degrades to generic commentary.

### Framework 1: Hamilton Helmer's 7 Powers

The gold standard for analyzing **durable competitive advantage**. Score every competitor against all 7:

| Power | Definition | Key Question | Scoring Signal |
|-------|-----------|--------------|----------------|
| **Scale Economies** | Per-unit cost declines as production volume increases | Does the incumbent's cost structure punish new entrants at lower scale? | Compare unit economics at 10x vs. 1x scale |
| **Network Effects** | Value to each user increases with the number of users | Is growth self-reinforcing? (See Network Effects Taxonomy below) | DAU/MAU ratio trend, viral coefficient |
| **Counter-Positioning** | A newcomer adopts a business model an incumbent can't copy without damaging their existing business | Would matching our move cannibalize the incumbent's core revenue? | Revenue concentration in threatened line |
| **Switching Costs** | The value loss a customer would experience by switching to an alternative | What would a customer lose — data, workflow, identity, integrations — by leaving? (See Switching Cost Decomposition) | Churn rate at contract renewal, migration cost estimates |
| **Branding** | A durable attribution of higher value to an objectively identical product | Does the brand command a price premium or reduce customer acquisition cost? | Price premium vs. generic, unaided recall |
| **Cornered Resource** | Preferential access to a valuable asset — talent, IP, regulatory license — that cannot be replicated | What scarce input can't be bought on the open market? | Patent portfolio, exclusive data access, regulatory moat |
| **Process Power** | Organization embeddings and complex process superiority built over time | Is the advantage embedded in organizational culture/process rather than any single technology? | Years to replicate, institutional knowledge depth |

**Scoring Rubric:**

| Rating | Symbol | Criteria |
|--------|--------|----------|
| **Strong** | 🟢 | Power is mature, actively accruing, and would take a competitor 3+ years to replicate |
| **Moderate** | 🟡 | Power exists but is either nascent, eroding, or limited in scope |
| **Weak/Absent** | 🔴 | Power does not exist or provides no meaningful competitive barrier |

**Critical insight:** Power must exist BEFORE victory is won — a company that wins without power will lose that position quickly. When scoring, assess whether power is *accruing* (strengthening with time/usage) or *eroding* (weakening due to market shifts, commoditization, or competitor action).

**Output format — 7 Powers Heat Map:**
```
| Power              | Competitor A | Competitor B | Your Product | Competitor C |
|--------------------|:---:|:---:|:---:|:---:|
| Scale Economies    | 🟢 Strong     | 🟡 Moderate  | 🟡 Moderate  | 🔴 Weak      |
| Network Effects    | 🟢 Data NE    | 🟡 Ecosystem | 🔴 None      | 🟡 Collab    |
| Counter-Position   | 🔴 None       | 🟢 Privacy   | 🟢 Unbundle  | 🔴 None      |
| Switching Costs    | 🔴 Low        | 🟢 Ecosystem | 🟡 Data      | 🔴 Low       |
| Branding           | 🟢 Premium    | 🟢 Trust     | 🔴 Unknown   | 🟡 Niche     |
| Cornered Resource  | 🟢 TPUs       | 🟢 Chips     | 🔴 None      | 🟡 Talent    |
| Process Power      | 🟡 Moderate   | 🟢 Design    | 🔴 None      | 🔴 None      |
```

---

### Framework 2: Ben Thompson's Aggregation Theory

The definitive lens for understanding **Internet-era competitive dynamics** — who owns the user relationship, who gets commoditized, and where value migrates.

**The Value Chain Inversion:**
- Pre-Internet: Distribution was scarce → distributors integrated backward into supply → owned suppliers
- Post-Internet: Distribution is free → transaction costs zero → integrate forward into user relationship → commoditize suppliers

**Three Characteristics of Aggregators:**
1. Direct relationship with users (payment, account, or habitual usage)
2. Zero marginal costs for serving users
3. Demand-driven multi-sided networks with decreasing acquisition costs

**Aggregator Classification:**

| Level | Supply Relationship | Cost Structure | Example |
|-------|-------------------|----------------|---------|
| Level 1 | Acquires supply (pays for it) | Supply cost scales | Netflix |
| Level 2 | Doesn't own supply, but incurs onboarding transaction costs | Marginal supply cost | Uber |
| Level 3 | Doesn't own supply, zero supplier costs | Zero marginal cost | Google |
| Super-Aggregator | Multi-sided, zero costs on all sides | Pure demand economics | Google, Meta |

**Decision Table — Aggregation Analysis:**

| Question | If Yes | If No |
|----------|--------|-------|
| Does this player have a direct user relationship? | Potential aggregator | Supplier or infrastructure — vulnerable to commoditization |
| Are marginal costs near zero? | Can scale without proportional cost | Growth hits cost ceiling — look for margin compression |
| Are acquisition costs decreasing with scale? | Flywheel active — very dangerous competitor | Growth requires sustained spend — vulnerable to funding dry-up |
| Can suppliers multi-home? | Aggregator's moat is weaker than it appears | Strong lock-in on supply side — powerful position |

**Analytical questions to answer:**
- What is the scarce resource being distributed?
- Which component has become commoditized (and who's commoditizing it)?
- Who owns the user relationship, and is that ownership durable?
- Where is value shifting — toward supply or toward demand ownership?

---

### Framework 3: Christensen's Disruption Theory — Applied

Not just "low-end disruption." The complete analytical toolkit for identifying disruption vectors.

**Disruption Vector Analysis:**

| Vector | Mechanism | Detection Signal | Example |
|--------|-----------|-----------------|---------|
| **Low-end** | "Good enough" at dramatically lower cost to over-served customers | New entrant pricing at 30-70% discount; customers saying "I don't use half the features" | Google Docs vs. Microsoft Office (early) |
| **New-market** | Serves non-consumers who couldn't access the market before | Product reaching users who never bought the category; simpler UX, lower barrier | Canva vs. Adobe (designers who aren't designers) |
| **Hybrid** | Enters low end AND expands the market simultaneously | Both price disruption AND new user demographics | Notion (simpler than Confluence AND accessible to non-engineers) |

**Conservation of Attractive Profits (COAP) — Most Underused Christensen Concept:**

> When one layer of a value chain becomes modularized and commoditized, an adjacent layer becomes integrated and earns outsized profits.

**COAP Application Method:**
1. Identify each layer of the value chain
2. Which layers are becoming commoditized right now?
3. Where will profits shift as commoditization completes?
4. Is any player actively integrating the newly attractive layer?

**"Isn't Good Enough" / "More Than Good Enough" Decision Table:**

| Market State | Architecture That Wins | Implication |
|-------------|----------------------|-------------|
| Product isn't good enough for most users | Integrated architectures win | Incumbent is safe — customers need improvement, not disruption |
| Product is more than good enough | Modular architectures win | Disruption incoming — over-served customers will switch to cheaper/simpler |

---

### Framework 4: Roger Martin's "Where to Play / How to Win"

The strategy-as-choice cascade. Reverse-engineer every competitor's actual strategy (which often differs from their stated strategy).

**The Five Cascading Choices:**
1. **What is our winning aspiration?** (Concrete market position, not mission statement)
2. **Where to play?** (Markets, segments, channels, geographies, customer types)
3. **How to win?** (Cost leadership? Differentiation? What specific capability advantage?)
4. **What capabilities must be in place?**
5. **What management systems are required?**

**Competitive Application — The Revealed Strategy Test:**

| Dimension | What They SAY | What Resource Allocation REVEALS | Gap = Insight |
|-----------|---------------|--------------------------------|---------------|
| Where to play | "We serve everyone" | 80% revenue from enterprise | They're an enterprise company pretending to be horizontal |
| How to win | "Best product wins" | 60% spend on sales, 15% on R&D | They win on distribution, not product |
| Capabilities | "AI-first" | 3 ML engineers, 200 sales reps | Marketing positioning, not technical reality |

**Key insight:** The gap between what competitors SAY and what their resource allocation REVEALS is where the strategic insight lives. Annual reports, job postings, and org charts reveal strategy more honestly than press releases.

---

### Framework 5: Wardley Mapping

Plot every component of the value chain on two axes to identify strategic misallocations and evolutionary opportunities.

**Axes:**
- **Y-axis (visibility):** How visible to the end user? (User needs at top → infrastructure at bottom)
- **X-axis (evolution):** Where on the evolution curve?

| Stage | Characteristics | Competitive Implications | Investment Signal |
|-------|----------------|------------------------|-------------------|
| Genesis | Novel, uncertain, high failure rate | First-mover possible but risky | VC funding, research labs, patents |
| Custom Build | Emerging understanding, bespoke | Differentiation opportunity | Specialized teams, high salaries |
| Product (+rental) | Increasingly understood, feature competition | Consolidation, M&A wave | Product managers hired, feature parity race |
| Commodity (+utility) | Standardized, cost competition | Margin compression, shift to utility | Outsourcing, API-ification |

**Competitive Application Method:**
1. Map your product's components on the evolution axis
2. Map each competitor on the same map
3. Where are they investing in genesis/custom? (Their bet on the future)
4. Where are they sourcing commodity? (What they've given up owning)
5. Spot mismatches: custom effort on commodity = waste; commoditizing genesis = unstable foundation
6. Identify inertia: where is a competitor over-investing in a stage their component has evolved past?

**Decision trigger:** If a competitor is building custom what you can source as commodity → you have a cost advantage. If they're commoditizing what's still genesis for you → they're ahead on the evolution curve.

---

### Framework 6: Jobs-to-be-Done Competitive Analysis

Customers don't buy products — they "hire" them for a job. Competition isn't between similar products; it's between anything hired for the same job.

**JTBD Structure:**

| Job Dimension | Question | Why It Matters |
|--------------|----------|----------------|
| **Functional** | What is the customer trying to accomplish? | The task — but rarely the real reason for hiring |
| **Emotional** | How does the customer want to feel? | Often the actual purchase driver |
| **Social** | How does the customer want to be perceived? | Drives tool choice in collaborative settings |
| **Consumption chain** | What happens before, during, and after? | Where pain points and switching costs live |

**Competitive Landscape Map (JTBD version):**
- Don't list "products that look like ours"
- List "everything a customer might hire for this job" — including manual processes, workarounds, doing nothing
- Rate each on satisfaction of functional, emotional, and social jobs
- Identify: over-served jobs (ripe for disruption) vs. under-served jobs (growth opportunity)

**Decision Table — JTBD Competitive Assessment:**

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Customers hire multiple products for same job | Job is under-served; integration opportunity | Build the unified solution |
| Customers over-pay relative to job importance | Job is over-served; disruption risk | Unbundle or simplify |
| "Non-consumption" is the main competitor | New-market opportunity | Lower barriers to entry |
| Customers describe "workarounds" | Product-market fit gap | Address the workaround directly |

---

### Framework 7: Kevin Kwok's Data Content Loops

For markets where the competitive weapon is information disintermediation.

**The "Rich Barton Playbook":**
1. Identify an industry where intermediaries hoard information
2. Build a Data Content Loop: authoritative data → definitive page for every entity
3. Dominate search for every entity in the category
4. Own demand: users come to you first → you dictate terms to supply

**Loop mechanics:** Data → Content → SEO dominance → Traffic → More data → Better content → Stronger SEO → compounds

**Assessment questions:**
- Who controls the data-content-discovery loop?
- Who owns demand?
- What breaks the loop?
- Is the data proprietary or publicly available? (Proprietary = stronger moat)
- How many query variations does the loop cover? (More = harder to displace)

---

### Framework 8: Blue Ocean Strategy

Kim & Mauborgne's framework for **finding uncontested market space** rather than competing in existing markets. All preceding frameworks assume you're fighting in a defined arena. Blue Ocean asks whether you should be in that arena at all.

**Core Insight — Value Innovation:**
The simultaneous pursuit of differentiation *and* low cost. Traditional strategy assumes a tradeoff; Blue Ocean rejects it. Value innovation happens when you align utility, price, and cost in a way that makes the competition irrelevant.

**The Strategy Canvas:**

Plot every competitor on two axes — factors of competition (x) vs. offering level for each factor (y). When all players have similar curves, the industry is competing on the same dimensions and Blue Ocean opportunity exists.

```
Offering Level
High ─────────────────────────────────────────────────────
     │  Incumbent A ╭──╮ ╭──╮          Your target curve
     │   ╭──╮╭──╮╭──╯  ╰──╯  ╰──────────╮╭──╮
     │───╯  ╰╯  ╰╯                        ╰╯  ╰──
Low  ─┼─────────────────────────────────────────────────────
     │ Factor1 Factor2 Factor3 Factor4 Factor5 Factor6
```

**The Four Actions Framework (ERRC Grid):**

| Action | Question | Strategic Purpose |
|--------|----------|-------------------|
| **Eliminate** | Which factors the industry takes for granted should be removed entirely? | Cut costs and complexity customers don't actually value |
| **Reduce** | Which factors should be reduced well below the industry standard? | Right-size over-delivered factors |
| **Raise** | Which factors should be raised well above the industry standard? | Eliminate the compromises customers currently accept |
| **Create** | Which factors should be created that the industry has never offered? | Generate new value and new demand |

**Output format — ERRC Grid:**
```
| Factor                    | Eliminate | Reduce | Raise | Create |
|---------------------------|:---------:|:------:|:-----:|:------:|
| Sales complexity          | ✅        |        |       |        |
| Feature depth             |           | ✅     |       |        |
| Onboarding time           |           |        | ✅    |        |
| AI-generated first draft  |           |        |       | ✅     |
```

**Six Paths to Blue Oceans:**

| Path | Where to Look | Example |
|------|--------------|---------|
| 1. Alternative industries | Products/services that serve the same job but look different | Cirque du Soleil looked across circus AND theatre |
| 2. Strategic groups within the industry | Why do buyers trade up or down between tiers? | NetJets looked across commercial aviation AND private jets |
| 3. Chain of buyers | Who pays vs. who uses vs. who influences the decision? | Novo Nordisk targeted doctors, not patients |
| 4. Complementary products | What happens before, during, after product use? | Barnes & Noble added cafés |
| 5. Functional vs. emotional orientation | Functionally-oriented industry → add emotional; emotionally-oriented → strip to function | Swatch: watch as fashion, not tool |
| 6. Time | What trends are certain, irreversible, and still under-leveraged? | Apple: iPod in 2001 on music industry's paid download trend |

**When Blue Ocean beats 7 Powers analysis:**

| Situation | Use Blue Ocean | Use 7 Powers |
|-----------|---------------|--------------|
| Market is commoditizing — all players have similar Power ratings | ✅ | |
| New entrant choosing where to compete | ✅ | |
| Assessing moat durability of incumbents | | ✅ |
| Responding to a specific competitor move | | ✅ |
| Identifying whether to fight or reframe the competitive arena | ✅ | |

**Critical warning:** Blue Ocean is not a license to ignore competition. A Blue Ocean can be competed away once others see the opportunity. Pair Blue Ocean analysis with 7 Powers to identify which Blue Ocean moves can be defended.

---

### Framework 9: Technology Adoption Lifecycle & Crossing the Chasm

Geoffrey Moore's framework for understanding **how competitive dynamics shift as technology markets mature** — and why the rules that win early adopters fail against the mainstream.

**The Technology Adoption Lifecycle:**

| Segment | Share | Mindset | Purchase trigger | Competitive implication |
|---------|:-----:|---------|-----------------|------------------------|
| **Innovators** | 2.5% | Technologists | Access to latest tech | Risk-tolerant; buy broken products; not references |
| **Early Adopters** | 13.5% | Visionaries | Strategic advantage | Buy vision and potential, not references or proof |
| **Early Majority** | 34% | Pragmatists | Proven productivity gain | Buy references from people like themselves; need whole product |
| **Late Majority** | 34% | Conservatives | Cost reduction, safety | Buy commoditized, bundled solutions with strong support |
| **Laggards** | 16% | Skeptics | Forced/compliance | Don't voluntarily adopt; price-sensitive to the extreme |

**The Chasm — Why It Exists:**

Early Adopters buy on vision. Early Majority buy on references from people like themselves. Early Adopters are individualists who do not give referrals that satisfy pragmatists. The result: there is **no natural word-of-mouth bridge** between the two groups.

```
Innovators → Early Adopters → [THE CHASM] → Early Majority → Late Majority → Laggards
                                    ↑
                    Most B2B tech companies die here
```

**The Whole Product Concept:**

The "whole product" is everything required for the customer to achieve their full desired outcome — not just the core product.

| Buyer | What they accept | What you must deliver |
|-------|-----------------|----------------------|
| Early Adopter | Generic product + builds rest themselves | Core product + vision |
| Early Majority | Nothing unless whole product is delivered | Core + integrations + support + training + community + references |

**Whole Product Gap = The Chasm.** You have to build or partner for the whole product before the Early Majority will buy.

**Bowling Alley Strategy — Crossing the Chasm:**

Don't attack the whole mainstream market. Win one niche completely, then use it as a beachhead:

1. **Choose the head pin** — a niche with (a) acute pain, (b) reachable whole product, (c) accessible references, (d) adjacent to other niches
2. **Own the head pin completely** — 50%+ share in that niche before moving
3. **Knock the next pin** — adjacent niche where your head pin references carry weight
4. Repeat until mainstream momentum is self-sustaining

**Competitive Analysis Application:**

| Stage | Who's winning | What winning looks like | Strategic risk |
|-------|--------------|------------------------|----------------|
| **Innovation** | No clear winner | Prototype traction, developer interest | Building something nobody wants |
| **Early Adopter** | Most differentiated | Customer stories, visionary pilots | Burning runway without crossing the chasm |
| **Chasm** | Nobody yet — danger zone | Niche dominance + whole product | Diluting focus across too many niches |
| **Early Majority** | Whole product leader | References, integrations, channel | Incumbent lock-in before you arrive |
| **Late Majority** | Cost/distribution leader | Bundled offering, low TCO | Margin compression; feature parity becomes table stakes |
| **Laggards** | Commodity provider | Price, compliance, support SLAs | Stranded in a declining market |

**Assessment questions:**
1. Which adoption stage is this market currently in? (Look at: % of TAM that has bought anything in the category; whether buyers require references or will pioneer)
2. Where is each competitor positioned on the lifecycle?
3. Has any player successfully crossed the chasm? How? (Whole product + which niche?)
4. What is the whole product gap for your target segment in the next niche?
5. Which niche is the head pin for your bowling alley?

**Integration with other frameworks:**
- **Pre-chasm:** 7 Powers analysis matters less — moats are nascent. Focus on differentiation and vision.
- **At the chasm:** Wardley Mapping most useful — you need to see which components are commoditizing and which are still custom.
- **Post-chasm:** 7 Powers becomes decisive — who is accumulating Scale Economies, Switching Costs, Network Effects in the mainstream?

---

### Analytical Lenses (Applied Across All Frameworks)

#### Network Effects Taxonomy

| Category | Types | Strength | Vulnerability |
|----------|-------|----------|---------------|
| **Direct** | Physical, Protocol, Personal Utility, Market Network | Strongest | Requires critical mass; vulnerable before tipping |
| **2-Sided** | Marketplace, Platform, Asymptotic Marketplace | Strong but variable | Multi-tenanting weakens moat |
| **Data** | Data Network Effects | Often weaker than assumed | Asymptotic (5th data point adds more than 5000th) |
| **Tech Performance** | Performance improves with more users | Strong when genuine | Often confused with scale economies |
| **Social** | Language, Belief, Bandwagon, Tribal | Moderate (can fade) | Susceptible to cultural shifts |

**Critical questions:**
- Does the competitor *actually* have network effects, or merely scale effects? (Scale = costs decrease; NE = *value to users* increases)
- Same-side positive (rare, powerful — e.g., MS Office file sharing) or same-side negative (common — more sellers = more competition)?
- How asymptotic? (Uber: 4→2 min wait much less valuable than 8→4 min)
- Is multi-tenanting possible? If yes, moat is much weaker than it appears.

#### Switching Cost Decomposition

Never rate "high/medium/low." Decompose by type:

| Type | Description | Durability | Scoring Signal |
|------|-------------|-----------|----------------|
| **Financial** | Contractual penalties, repurchase costs | Low — money solves money problems | Contract terms, exit fees |
| **Procedural/Learning** | Time and effort to learn new system | Moderate — degrades as UX improves | Time-to-proficiency, training investment |
| **Data/Migration** | Moving data, losing history, reconfiguring integrations | High — grows with usage duration | Data volume, integration count, history depth |
| **Relational** | Loss of relationships, trust, accumulated reputation | Very high — can't be replicated | Relationship tenure, trust capital |
| **Identity** | Product is part of self-image ("I'm an Apple person") | Very high — psychological, not rational | Community participation, self-identification |
| **Workflow/Integration** | Embedded in workflows, connected to other tools | Very high — compounds over time | Integration count, workflow dependency depth |
| **Contractual/Regulatory** | Legal or compliance barriers | Structural — not the company's moat but acts as one | Regulatory requirements, compliance investment |

**Key insight:** The most durable switching costs are ones customers CREATE through use (data accumulation, workflow embedding, identity). Not the ones vendors impose (contracts). Companies relying on imposed switching costs sit on erosion-prone moats.

**Output format — Switching Cost Decomposition Matrix:**
```
| Switching Cost Type     | Competitor A | Competitor B | Your Product |
|------------------------|:---:|:---:|:---:|
| Financial/Contractual   | ████████░░ 8/10 | ███░░░░░░░ 3/10 | █████░░░░░ 5/10 |
| Data/Migration          | █████████░ 9/10 | ████░░░░░░ 4/10 | ██████░░░░ 6/10 |
| Workflow/Integration    | █████████░ 9/10 | ██░░░░░░░░ 2/10 | ███████░░░ 7/10 |
| Identity                | ████████░░ 8/10 | █████░░░░░ 5/10 | ███░░░░░░░ 3/10 |
| Learning/Procedural     | ██████░░░░ 6/10 | ████░░░░░░ 4/10 | █████░░░░░ 5/10 |
| Relational/Trust        | ███████░░░ 7/10 | ███░░░░░░░ 3/10 | ████░░░░░░ 4/10 |
```

#### Asymmetric Competition Analysis

**Core question:** Are competitors actually competing on the same dimension?

| Dimension | Map for each competitor |
|-----------|----------------------|
| What they optimize for | (Revenue per seat vs. user growth vs. ecosystem lock-in) |
| What they sacrifice | (Free tier vs. profitability vs. direct revenue) |
| Business model dependency | (This IS the product vs. feature of larger product vs. loss leader) |
| Time horizon | (Quarterly vs. 2-year vs. 10-year platform bet) |
| What "winning" looks like | (Market share vs. ecosystem adoption vs. standard-setting) |

**Bundle/Unbundle Asymmetry:**
- Some competitors give away free what you charge for (module in their bundle)
- Some charge more for a subset of what you offer (specialize, 10x quality on narrow slice)
- Map who has economic freedom to play differently

**Cost to Compete:**
- What does it cost each competitor to add 1 user? 1 feature? 1 market?
- Near-zero marginal cost to compete = structural advantage no amount of feature excellence overcomes

#### Demand-Side vs. Supply-Side Analysis

Most analyses default to supply-side ("what does each competitor offer?"). Start demand-side.

**Demand-Side First:**
1. What are the actual customer jobs-to-be-done?
2. How well-served is each job today? (Over-served → disruption risk; under-served → growth opportunity)
3. Willingness to pay for better solutions to each job?
4. Switching costs keeping customers in current solutions?
5. Adjacent jobs a competitor could expand into?

**Supply-Side Second:**
1. Capabilities of each competitor
2. Cost structure (fixed vs. variable ratio determines competitive behavior)
3. Resource allocation (where are they investing — actual strategy vs. stated)
4. Structural constraints (org structure, tech debt, regulatory limits)

#### Value Chain Decomposition

```
[Raw capability] → [Platform/infra] → [Product] → [Distribution] → [Customer relationship] → [Monetization]
```

For each link:
- Who controls it? (Single player vs. fragmented)
- What's the margin? (High = value capture; low = commoditized)
- Moving toward integration or modularization? (Per Christensen's COAP)
- What would it take to disintermediate?
- Where is value migrating? (Most important — precedes market share shift)

**The Smile Curve:** Value accrues at the extremes — upstream (IP, platform, data) and downstream (brand, customer relationship). The middle (assembly, basic service) gets squeezed.

#### Win/Loss Analysis

Win/loss analysis is the **primary source of Tier 1 behavioral evidence** for competitive conclusions. It is not a separate research track — it is the mechanism that validates or falsifies every structural conclusion in this codex. A 7 Powers heat map produced without win/loss data is a hypothesis. One anchored to win/loss patterns is an evidence-based finding.

**Why it's Tier 1:** Win/loss interviews capture what customers actually *did* (chose a competitor, stayed, churned) — not what they said they would do. Behavioral data, not stated preference.

**Data Source Hierarchy:**

| Source | Evidence Tier | Bias Level | When to Use |
|--------|--------------|------------|-------------|
| Customer interview ≤2 weeks post-decision | Tier 1 | Low — recent, unfiltered | Always; this is the gold standard |
| Churned customer exit interview | Tier 1 | Low — post-decision | Churn analysis; switching cost validation |
| Prospect survey after lost deal | Tier 2 | Moderate — structured but self-reported | When live interviews aren't feasible |
| CRM notes from sales team | Tier 3 | High — sales attribution bias | Signal only; never for structural conclusions |
| Anecdotal sales team feedback | Tier 5 | Very high | Hypothesis generation only |

**The Attribution Paradox — the most common win/loss mistake:**
Sales teams consistently misattribute. Wins get attributed to product quality; losses get attributed to price. Both are wrong most of the time. The real reasons cluster around: integration fit, switching cost perception, trust/brand, and reference availability — none of which show up in CRM notes because reps don't track them. **Never draw structural conclusions from CRM data alone.**

**Interview Question Bank:**

*For wins:*
- What problem were you trying to solve? (Surface the job-to-be-done, not the feature request)
- What alternatives did you evaluate? (Reveals the real competitive set — often different from the assumed one)
- What almost made you choose someone else? (The actual switching cost and risk perception)
- Why did you ultimately choose us? (Separate stated reasons from revealed reasons — probe beneath the first answer)
- What would we need to lose for you to reconsider at renewal? (Predicts future switching cost erosion)

*For losses:*
- What did you end up choosing, and why? (Direct; don't assume you know)
- Where did our product fall short for your specific situation? (Specific > general — "the integration with X didn't work" > "features weren't good enough")
- What could we have done differently — product, process, or commercial? (Separates product gaps from sales execution gaps)
- Would you reconsider us? Under what conditions? (Tests whether the loss is permanent or recoverable)
- Who championed the competitor internally? (Reveals the buyer chain dynamics — was this a champion problem or a product problem?)

**Segmentation Protocol — always disaggregate before concluding:**

| Segment | What it reveals |
|---------|----------------|
| Deal size (SMB vs. mid-market vs. enterprise) | Different competitive sets, different win rates, different reasons |
| New vs. expansion vs. renewal | Different switching cost dynamics — renewal losses signal moat erosion |
| Industry vertical | Incumbent advantages, compliance requirements, integration landscapes differ |
| Champion role (technical buyer vs. economic buyer vs. end user) | Who drove the decision changes the loss reason entirely |
| Competitive opponent (lost to A vs. lost to B) | Different opponents have different attack vectors; never aggregate |

**Win/Loss Pattern Taxonomy:**

| Pattern | What it sounds like | Framework implication |
|---------|--------------------|-----------------------|
| **Feature gap** | "They had X, you didn't" | L2 capability deficit; only matters if X is in a high-weight capability area |
| **Integration lock-in** | "They already had Y in our stack" | Competitor's Switching Cost (Workflow/Integration type) is the actual barrier — not your feature |
| **Reference gap** | "We needed to see it working in our industry" | Adoption stage problem — you're pre-chasm for this segment (Crossing the Chasm) |
| **Pricing structure mismatch** | "Your model didn't fit how we buy" | Not a price problem — a packaging/business model problem |
| **Brand/trust deficit** | "We went with the safer choice" | Competitor's Branding power is active; often appears as incumbent advantage |
| **Sales execution** | "Their team understood our problem better" | Non-product; but signals a whole-product gap (missing services, onboarding, support) |
| **Champion lost** | "Our contact left / got overruled" | Relational switching costs — deal was held by a person, not embedded in the product |

**Mapping Win/Loss Findings to Framework Conclusions:**

| Win/Loss finding | Updates which framework |
|-----------------|------------------------|
| "Lost consistently to X because their data integrates with Y" | 7 Powers: X's Switching Costs (Workflow) = 🟢; yours = 🟡 or 🔴 |
| "Won because customers said they couldn't imagine rebuilding their history elsewhere" | 7 Powers: Your Switching Costs (Data/Migration) = 🟢; customer-created, durable |
| "Lost to 'do nothing' more than to any competitor" | JTBD: job is under-served — customers don't recognize the pain enough to buy |
| "Reference customers in our industry only exist for Competitor A" | Crossing the Chasm: A has crossed the chasm in this vertical; you haven't |
| "They beat us on price because it's bundled into their platform" | Aggregation Theory: competitor is commoditizing your category from above |
| "Customers say they don't need most of our features" | Christensen: over-served segment — disruption risk from below |

**Win Rate Tracking:**

| Metric | Formula | Minimum viable tracking |
|--------|---------|------------------------|
| Competitive win rate vs. each opponent | Wins ÷ (Wins + Losses) where that competitor was present | Track quarterly; flag if declining >5pp |
| No-decision rate | No-decisions ÷ total deals entering eval stage | Rising no-decision = market education problem or demand-side issue |
| Churn competitive attribution | Churns citing competitor reason ÷ total churns | Separates product churn from competitive churn |

---

## Evidence Standards

### Evidence Quality Tiers

| Tier | Source Type | Weight | Example |
|------|-----------|--------|---------|
| **Tier 1** | Direct behavioral data (what people DO) | Highest | Usage analytics, revenue, app store data, patent filings, SEC filings, job postings |
| **Tier 2** | Primary research, credible methodology | High | Well-sampled surveys, structured interviews, controlled experiments |
| **Tier 3** | Expert analysis with disclosed reasoning | Medium-High | Stratechery, a16z, McKinsey with disclosed data, academic papers |
| **Tier 4** | Industry reports from reputable firms | Medium | Gartner, IDC, Forrester (useful for sizing, less for insight) |
| **Tier 5** | Executive statements and press releases | Low-Medium | Strategic signaling, not factual reporting — analyze for what they reveal about strategy |
| **Tier 6** | Punditry, blog posts, social media | Low | Sentiment only; never for facts |

**Triangulation Rule:** No strategic conclusion rests on a single evidence tier. Minimum 2 tiers, ideally 3.

**Staleness Rule:** For every claim, note the source date. If no source newer than 6 months can be identified, flag as `[POTENTIALLY STALE]`. Evidence tier and evidence recency are independent — a Tier 1 data point from 2 years ago may be less useful than a Tier 3 analysis from last month.

**Annotation Convention:** Use inline tags throughout — not just footnotes or end-of-section summaries. Per-cell annotation in matrices: `Strong (T2)` or `Adequate (T4: G2 reviews)` or `Unknown (T6: inferred)`. A trailing evidence table is a supplement, not a substitute for inline tagging.

### Leading vs. Lagging Indicators

| Category | Lagging (already happened) | Leading (about to happen) |
|----------|---------------------------|--------------------------|
| Product | Market share, revenue, margins | Job postings, patent filings, API changes, dev docs updates |
| Market | Industry revenue, installed base | Switching cost erosion rate, NPS velocity (direction, not absolute) |
| Competitive | Announced products, launched features | Acqui-hires, open-source contributions, research papers, keynote topics |
| User | Downloads, MAU, DAU | Cohort retention curves, time-to-value, feature adoption velocity |

### Signal vs. Noise Filter

Apply to every data point:
1. **Frequency:** Recurring or one-off?
2. **Source credibility:** Primary actor or secondary commentator?
3. **Falsifiability:** Could this signal be false? What would falsify it?
4. **Structural significance:** Change in market *structure* (durable) or market *weather* (temporary)?
5. **Convergence:** Do multiple independent signals point the same direction?

### Source Structuring

**Primary (highest weight):**
- SEC filings, 10-Ks, earnings Q&A (read the Q&A, not just prepared remarks)
- Job postings (reveals investment priorities 6-12 months ahead)
- API docs and developer changelogs (reveals technical direction)
- Patent filings (reveals research bets)
- App store reviews at scale (reveals unmet needs)
- User forums and support tickets (reveals actual vs. marketed experience)

**Structured Secondary:**
- Industry analyst reports (for sizing and segmentation)
- Academic research (for technology capability curves)
- Conference presentations by engineers/PMs (reveals architecture decisions)

**Inference-Based:**
- Competitive pricing analysis (reverse-engineer cost structures)
- LinkedIn employee analysis (team size, seniority, growth by function)
- GitHub/open source activity (technology choices, collaboration patterns)

---

## Application Method

### Step 0b: Route to Framework Subset

After passing the Context Fitness Check, identify the question type and select load-bearing frameworks. Applying all 9 frameworks to every question inflates length, buries signal, and applies wrong-context frameworks.

| Question Type | Prompt Signals | Primary Frameworks | Frameworks to Skip |
|---|---|---|---|
| **Moat assessment** | "how defensible are we", "how strong is our moat", "a big player just entered" | 7 Powers, Switching Cost, Aggregation Theory, Win/Loss | Blue Ocean, Crossing the Chasm |
| **Competitive response** | "competitor just did X", "how do we respond", "CEO meeting", "we're seeing churn" | 7 Powers, Disruption + COAP, Roger Martin, Win/Loss, Wardley | Blue Ocean, Crossing the Chasm |
| **Market entry** | "should we enter", "go/no-go", "new market", "new product line" | Where to Play, Blue Ocean, Crossing the Chasm, JTBD | Aggregation Theory (unless platform play) |
| **Positioning / why we lose** | "how do we position", "why are we losing deals", "differentiation" | JTBD, Blue Ocean, Roger Martin, Win/Loss | Wardley, Crossing the Chasm |
| **Full strategic synthesis** | "board meeting", "complete strategy", "where to play + how to win" | All — tier explicitly: 3 primary, rest supporting | None — but label tiers |
| **Build / buy / partner** | "should we build or buy", "partnership decision", "M&A" | JTBD, Where to Play, Aggregation Theory, Wardley | Blue Ocean |

Apply primary frameworks fully. Apply supporting frameworks at reduced depth unless they surface a conflicting signal — in which case surface the contradiction explicitly.

### Quick Version (10 steps for experienced practitioners)

0a. **Context Fitness Check** — Verify a Competitive War Map is the right artifact. Check: external vs. internal problem? Data access? Distribution model?
0b. **Route to framework subset** — Identify question type from the table above. Select 3-4 primary frameworks. Note which to skip.
1. **Define the competitive set** — Primary (3-5 direct), Secondary (3-6 adjacent), Non-obvious (2-3 paradigm threats)
2. **Score each competitor on 7 Powers** — Produce the heat map with 🟢🟡🔴 ratings and one-line justifications
3. **Decompose switching costs by type** — Don't say "high" — show the breakdown per cost category
4. **Run Aggregation Theory analysis** — Who owns the user relationship? Who's being commoditized? Where is value migrating?
5. **Apply disruption vector assessment** — Is the market over-served or under-served? Which disruption type is most likely?
6. **Run Blue Ocean check** — Plot the Strategy Canvas. Is everyone competing on the same dimensions? Complete the ERRC Grid for your product.
7. **Assess adoption stage** — Where is the market on the Technology Adoption Lifecycle? Has anyone crossed the chasm? What is the whole product gap?
8. **Map win/loss patterns to framework conclusions** — Don't report win/loss as a standalone section; trace each pattern to its structural cause (7 Powers, JTBD, Aggregation Theory, Chasm)
9. **Build the tactical layer** — Feature matrix, GTM comparison, customer signals with evidence tiers
10. **Cascade every insight to "So What"** — Observation → Implication → Response → Confidence → Watch indicator

### Full Version (detailed steps with decision points)

**Step 1: Define the Competitive Set**

Don't let intuition or the user randomly pick who to analyze. Use this framework:

| Tier | Description | Depth of Analysis | Count |
|------|------------|-------------------|-------|
| **Primary** | Same category, direct substitutes | Full analysis: all 7 Powers, switching costs, feature matrix, GTM, customer signals | 3-5 |
| **Secondary** | Adjacent products expanding toward you | 7 Powers scan, JTBD overlap, timeline-to-direct-competition | 3-6 |
| **Non-obvious / paradigm threats** | Different paradigm entirely (H3) | Scenario analysis, probability, leading indicators | 2-3 |

**Rule:** If the analysis only covers competitors the user thinks about daily, it's not worth reading. The value is in surfacing non-obvious threats.

**Step 2: Run the 7 Powers Assessment**

For EACH competitor in the primary set:
1. Score all 7 Powers using the rubric above
2. For each 🟢 rating, document the evidence (minimum Tier 2)
3. For each power, note whether it's *accruing* or *eroding*
4. Identify the 1-2 powers that are most decisive for this market
5. Produce the heat map visualization

**Decision point:** If no competitor holds >2 strong powers → market is structurally contestable. If one competitor holds 4+ strong powers → market has a likely long-term winner.

**Step 3: Decompose Switching Costs**

For each primary competitor:
1. Rate each of the 7 switching cost types (1-10 scale)
2. Produce the visual decomposition matrix
3. Identify which costs are customer-created (durable) vs. vendor-imposed (erodable)
4. Flag any competitor whose switching cost moat is primarily vendor-imposed — that's a vulnerability

**Step 4: Run Aggregation + Disruption Analysis**

Apply the Aggregation Theory decision table and Christensen's COAP:
1. Who owns the user relationship in this market?
2. Are marginal costs approaching zero for any player? (If yes → potential aggregator)
3. Which value chain layers are commoditizing? Where will profits shift?
4. Apply the "good enough" test — are customers over-served or under-served?

**Decision point:** If COAP analysis shows profits shifting to a layer a competitor doesn't own → strategic vulnerability, even if they currently dominate.

**Step 5: Reverse-Engineer Competitor Strategy**

Apply Martin's "Where to Play / How to Win" cascade:
1. For each primary competitor, fill in the Revealed Strategy Test table
2. Identify gaps between stated and revealed strategy
3. Map Wardley positions for key value chain components
4. Identify strategic misallocations (custom effort on commodity, or commoditizing genesis)

**Step 6: Build the Tactical Layer**

Produce three tactical assessments:
1. **Feature/Capability Matrix** — 10-15 capabilities that drive adoption/churn/differentiation, rated ✅/🔄/🚧/❌
2. **GTM & Distribution Comparison** — Pricing model, free tier, enterprise motion, distribution channel, bundle leverage
3. **Customer & User Signal Analysis** — App store trends, NPS signals, usage data, community feedback, churn anecdotes

**Step 7: Cascade to "So What"**

For EVERY major finding, structure as:
```
OBSERVATION [evidence tier] → IMPLICATION [mechanism] → STRATEGIC RESPONSE [specific action] → CONFIDENCE [H/M/L + key assumption] → WATCH INDICATOR [observable signal that tells you if this is wrong]

"[Competitor] is [doing X] [T2: customer interview data],
which threatens [our position Y] because [mechanism Z],
our response should be [specific action with owner and timeline] because [reasoning],
confidence: H — assumes [key assumption],
watch: [specific leading indicator]; if [threshold crossed], re-assess."
```

**Bad:** "Google is investing heavily in AI search."

**Elite:** "Google shipped AI Overviews to 100% of English queries [Tier 1: product data], threatening content-based acquisition because AI Overviews absorb the click that went to our page [mechanism: zero-click cannibalizes referral traffic]. Response: shift from search-dependent to direct-relationship channels — email and in-app loops — because retained users have 6x LTV of search-acquired [Tier 1: internal data]. Assumes Google doesn't build product-specific answer cards [est. 60% probability within 18mo based on API trajectory]."

### Mandatory Output: Assumption Registry

Every competitive war map must end with a standalone assumption registry. List every load-bearing assumption the analysis depends on:

| Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|
| [e.g., "Visier's free tier is funded to run at a loss for 18+ months"] | 7 Powers (Scale), Aggregation Theory | M | Funding round size, runway math | Visier raises less than $40M Series C in next 12 months |
| [e.g., "Our NLP advantage is defensible for 24 months"] | Counter-Positioning, Switching Cost | L | Team composition, patent filings | GPT-5 commoditizes document NLP accuracy by Q3 2026 |

Any assumption at L confidence must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the analysis, execute this step before delivering output:

> *"Now identify ≥3 genuine weaknesses in this analysis. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this recommendation is catastrophically wrong?"*

- If you cannot find real weaknesses, you haven't looked hard enough.
- Bear cases must be steelmanned — not just listed as probability-weighted scenarios but argued as forcefully as possible.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the scenario analysis — it is a distinct, explicitly adversarial voice.

---

## Meta-Frameworks

### The 3 Horizons Competition Map

| Horizon | Timeframe | Competitors | Approach |
|---------|----------|-------------|----------|
| H1: Current | 0-12 months | Direct (same category) | Share, features, churn, win/loss |
| H2: Adjacent | 12-36 months | Adjacent products expanding toward you | Bundle/unbundle, platform plays, JTBD overlap |
| H3: Paradigm | 36+ months | Different paradigm entirely | Scenario planning, disruption theory, tech curves |

Most analyses only do H1. By the time H3 is H1, it's too late.

### SCQ-A (Minto Pyramid Principle)

The backbone of every top-tier strategy deck:
1. **Situation:** Current market structure (size, growth, segmentation, value chain)
2. **Complication:** What is changing (tech shifts, regulation, new entrants, behavior changes)
3. **Question:** Given the complication, what should we do?
4. **Answer:** Recommendation supported by evidence and frameworks

### The Uncommon Knowledge Test

| Category | Definition | Action |
|----------|-----------|--------|
| **Common knowledge** | A smart generalist already knows this | Include minimally — context only |
| **Domain knowledge** | A domain expert knows this | Include for completeness |
| **Uncommon knowledge** | Neither would know this | Lead with this — THIS is insight |

Elite analyses have a high ratio of uncommon knowledge to table-stakes context.

### Counterfactual & Scenario Analysis

**"What if we're wrong?"** — for every strategic conclusion:
- State the key assumption
- State what would falsify it
- State the leading indicator to watch

**Three-Scenario Framework:**

| Scenario | Probability | Key Driver | Response |
|----------|:-----------:|------------|----------|
| 🟢 Base case | 50-60% | Current trends continue | [Actions] |
| 🔵 Bull case | 15-25% | What goes right | [Capitalize] |
| 🔴 Bear case | 15-25% | What goes wrong | [Mitigate] |

---

## Computation Requirements

⚠️ STRONGLY RECOMMENDED: For market sizing calculations, run:
```
python3 scripts/market_sizing.py --tam <total_addressable> --penetration <rate> --arpu <revenue_per_user>
```

⚠️ STRONGLY RECOMMENDED: For 7 Powers competitive scoring, run:
```
python3 scripts/competitive_scorer.py --competitors "CompA,CompB,CompC" --powers-json scores.json
```

If scripts are unavailable, state "Script not available — estimates below are approximate" and flag which numbers should be verified.

Do NOT estimate market sizing by reasoning alone when the script can provide precise arithmetic. Do NOT hand-calculate weighted competitive scores when the scorer can produce heat maps and moat durability indices.

---

## Output Quality Markers

### Quantified Impact Estimates

| Instead of | Write |
|-----------|-------|
| "Large market opportunity" | "$X B TAM, growing Y% CAGR, $Z B addressable given our distribution" |
| "Significant switching costs" | "~X hours config, Y integrations, Z months history; est. migration cost $W and T weeks productivity loss" |
| "Growing fast" | "X% MoM growth in [metric], reaching [milestone] by [date] at current trajectory" |
| "Strong position" | "X% share in segment Y, Z Powers from Helmer, net switching cost advantage of $W/seat" |

**Order of Magnitude Rule:** Even when imprecise, state $1M vs $10M vs $100M vs $1B. Getting magnitude right = 80% of value. "Large" = 0%.

### Citation Patterns

| Generic | Elite |
|---------|-------|
| "According to Gartner..." (argument from authority) | Uses Gartner for sizing, applies own framework for conclusions |
| No sources | Every claim has source + date; every inference labeled as inference |
| Relies on secondary reporting | Goes to primary sources, draws own conclusions |
| Company PR as evidence | Company statements as strategic signaling — analyzes what signal reveals |
| Single framework | Multiple frameworks on same question; notes where they agree (confidence) and diverge (investigate) |

### Board-Ready Quality Check

1. Does every section have a "so what"? If removable without changing a decision, remove it.
2. Key finding on page 1, not page 30? (Pyramid principle — lead with conclusion)
3. Recommendations actionable this quarter? ("invest in AI" is not actionable)
4. Distinguishes what we know / believe / guess? Labeled explicitly.
5. Names the decision it informs? Every analysis answers: "what do we do differently?"

---

## Visualization & Formatting

### Competitive War Map Format

When producing the final artifact, use these visualization patterns:

**7 Powers Heat Map** — per-competitor scorecard (see Framework 1 output format)

**Switching Cost Decomposition Matrix** — progress bars showing relative strength (see Switching Cost Decomposition output format)

**Asymmetric Competition Map** — structured comparison showing different competitive strategies:
```
### 🎯 Competitor A
- **Optimizes for:** [primary objective]
- **Willing to sacrifice:** [what they trade off]
- **Time horizon:** [investment timeframe]
- **Winning looks like:** [their definition of success]
- **Cost to add 1 user:** [marginal cost structure]
```

**Three Horizons Threat Landscape:**
```
┌──────────────┬──────────────────┬───────────────────────────────┐
│  H1 (0-12mo) │  H2 (12-36mo)    │  H3 (36mo+)                   │
│  Direct       │  Adjacent         │  Paradigm                     │
├──────────────┼──────────────────┼───────────────────────────────┤
│ [Competitor]  │ [Adjacent player] │ [Paradigm threat]             │
│ [threat type] │ [expansion vector]│ [disruption mechanism]        │
└──────────────┴──────────────────┴───────────────────────────────┘
```

**Evidence-Tiered Claims** — inline tagging:
```
- [Claim statement]
  📊 [Tier X: Source, date]
```

**Competitive Response Matrix:**
```
| If competitor does... | Who | Impact (1-5) | Our best response | Timeline |
```

### Formatting Rules

1. **Lead with tables, not paragraphs.** Every comparison should be a table. Prose explains the table, not replaces it.
2. **Use emoji as visual markers** — 🟢🟡🔴 for status, ⚠️ for risk, 📊 for evidence, 🎯 for target.
3. **Progress bars for relative strength** — ████░░░░ is instantly readable.
4. **Bold the mechanism, not the fact** — "Google's TPU investment is **$4-6B annually**" vs "**Google** is investing in TPUs." The number is the insight.
5. **Section headers as conclusions** — not "Market Analysis" but "Google Owns the Data Loop. Microsoft Owns the Workflow." The header IS the insight.
6. **Inline evidence tags** — [Tier 1: SEC filing] after every major claim.
7. **End every section with a decision trigger** — "This means we should..." or "Watch for..."

---

## Quality Gradients

### Intern Tier
- Lists competitors and their features
- Uses SWOT or Porter's Five Forces (surface level)
- No evidence tiers — mixes primary data with blog posts
- Conclusions are descriptive ("X is a strong competitor") without implications
- No quantification — relies on qualitative assessments ("large market")
- Missing: switching cost analysis, disruption vectors, moat assessment

### Consultant Tier
- Applies 3-4 frameworks systematically (7 Powers, Aggregation Theory, JTBD minimum)
- Evidence is tiered — distinguishes Tier 1 behavioral data from Tier 4 analyst reports
- Switching costs decomposed by type, not rated high/medium/low
- Every finding has a "So What" with strategic implication
- Quantified where possible (order of magnitude at minimum)
- Includes counterfactuals — "what if we're wrong" for major conclusions
- Covers H1 and H2 competitive threats
- Missing: elite-tier framework depth, full Wardley mapping, H3 paradigm analysis

### Elite Tier
- All 9 frameworks applied with scoring rubrics and decision tables
- Evidence triangulated — no conclusion on single source tier
- Reveals competitor's actual strategy via resource allocation analysis (not their PR)
- Identifies non-obvious competitive threats (H3 paradigm)
- Switching cost moat analysis distinguishes customer-created vs. vendor-imposed
- COAP analysis identifies where profits will shift before it happens
- Blue Ocean check: ERRC Grid completed; identifies whether the competitive arena itself should be reframed
- Adoption stage assessment: market position on lifecycle identified; whole product gap named for each stage
- Every recommendation is tied to a specific decision with timeline
- Uncommon knowledge ratio is high — reader learns things they couldn't have known
- Includes competitive response matrix with pre-planned counter-moves
- Produces artifacts a PM cannot produce unaided — this is the codex test

---

## Failure Modes

**FM-1: Framework Stuffing**
*What it looks like:* All 7 frameworks applied but superficially. Each gets 2-3 sentences. Looks comprehensive but reveals nothing.
*Why it happens:* Agent treats frameworks as a checklist rather than analytical tools. Breadth over depth.
*Detection:* If removing a framework section doesn't change any recommendation, it was stuffed.
*Correction:* Apply fewer frameworks more deeply. Each framework must change or support at least one recommendation.

**FM-2: The Feature Comparison Trap**
*What it looks like:* Output is a detailed feature matrix with no structural analysis. Lists who has what, but never asks "so what?" or "why does this matter?"
*Why it happens:* Features are easy to compare. Strategy requires judgment. Agent defaults to what's easier.
*Detection:* If the output could be produced by reading product websites without any frameworks, it's a feature comparison, not competitive analysis.
*Correction:* Start with 7 Powers and Aggregation Theory BEFORE touching features. Features are evidence for structural assessment, not the assessment itself.

**FM-3: Present-Tense Myopia**
*What it looks like:* Analysis describes the current competitive landscape accurately but identifies zero threats or opportunities that aren't already obvious.
*Why it happens:* Only H1 (0-12 month) competitors analyzed. No disruption vectors, no adjacency threats, no paradigm shifts.
*Detection:* If the analysis wouldn't surprise anyone in the industry, it's myopic.
*Correction:* Mandate H2 and H3 analysis. Use COAP to predict where profits will shift. Use leading indicators to spot moves before they're announced.

**FM-4: Source Laundering**
*What it looks like:* Claims presented as facts without evidence tiers. A Tier 5 executive statement treated with the same weight as Tier 1 behavioral data.
*Why it happens:* Evidence tiering is effortful. Agent takes the path of least resistance.
*Detection:* Look for inline evidence tags. If absent, or if all sources are the same tier, evidence standards have collapsed.
*Correction:* Every factual claim must have an inline evidence tag with tier. Every strategic conclusion must cite minimum 2 tiers.

**FM-5: The "Everyone Competes on Everything" Fallacy**
*What it looks like:* Analysis treats all competitors as if they're playing the same game. Identical dimensions compared across all players.
*Why it happens:* Failure to apply asymmetric competition analysis. Easier to compare apples to apples even when some competitors are oranges.
*Detection:* If the analysis doesn't surface that competitors are optimizing for different things and have different cost-to-compete structures, asymmetric analysis is missing.
*Correction:* Apply the Asymmetric Competition Map. Ask: "What does winning look like for THIS competitor?" If the answers differ, they're fighting different wars.

**FM-6: Missing the Moat Erosion**
*What it looks like:* Analysis scores a competitor's moat as strong based on historical data, but misses signals that the moat is eroding.
*Why it happens:* 7 Powers assessment done at a point in time rather than as a trajectory. Current state ≠ future state.
*Detection:* If switching cost analysis doesn't distinguish between "high today" and "rising vs. falling," erosion is being missed.
*Correction:* For every power rated 🟢, explicitly state whether it's accruing or eroding and cite the evidence for directionality.

**FM-7: Insight-Free Quantification**
*What it looks like:* Lots of numbers but no interpretation. "$50B TAM" stated without context (addressable? serviceable? growing or shrinking?). Market sizing without strategic implication.
*Why it happens:* Agent follows the "quantify" instruction literally without understanding that numbers serve strategy, not the other way around.
*Detection:* If you can remove all the numbers and the strategic conclusions don't change, quantification is decorative.
*Correction:* Every number must answer "so what?" — TAM connects to addressable opportunity. Growth rate connects to urgency. Share connects to competitive position.

**FM-8: Right Frameworks, Wrong Question**
*What it looks like:* Structurally excellent competitive analysis — all frameworks applied correctly, evidence tiered, recommendations cascaded — but the analysis answers a question nobody is asking. The output is a Competitive War Map for a product whose real problem is internal activation, not external competition.
*Why it happens:* The skill is triggered by any competitive-sounding prompt ("run competitive analysis for X") without checking whether a competitive war map is the right artifact. An enterprise product with low user awareness needs an activation strategy, not a market positioning analysis. A product embedded in a larger platform needs a bundle strategy, not an independent moat assessment.
*Detection:* Ask: "Would the primary stakeholder's first question about this product be about a competitor, or about their own users?" If about their own users, the analysis is solving the wrong problem.
*Correction:* Run the Context Fitness Check (Step 0) before Framework Selection (Step 0b). If the core problem is internal (activation, awareness, adoption), redirect to the appropriate artifact. If proceeding with a war map anyway (e.g., to inform a broader strategy), state explicitly in the Executive Summary what the analysis does and does not address.

**FM-9: The Expert-Only Document**
*What it looks like:* Output is dense with framework names (COAP, Aggregation Theory, Wardley), notation (T1-T6, H/M/L, O→I→R→C→W), and jargon that assumes the reader built the analysis. A VP or cross-functional stakeholder cannot extract the conclusions without a guided tour from the author.
*Why it happens:* The skill optimizes for analytical completeness, not reader comprehension. The author knows all the notation; the reader doesn't. No reading guide, no notation key, no layered depth.
*Detection:* Show the output to someone who didn't request it. If they need more than 60 seconds to find the conclusions, or if they ask "what does T2 mean?", the document fails the reader test.
*Correction:* The output template mandates a "How to Read This Document" section and a Notation Key before the analysis begins. The Executive Summary uses zero framework jargon — plain language a non-PM exec can act on.

---

## What's Next

← This skill works best after: **Problem Framing** (if available) — a well-framed problem focuses the competitive analysis on the right market and competitors
→ This skill's output feeds well into: **Narrative Building** (positioning strategy informed by competitive landscape), **Spec Writing** (competitive requirements and differentiation features)
⊕ **Start here if:** You have a competitive question, market entry decision, positioning challenge, or need to assess moat durability
💡 **For a full product cycle:** Problem Framing → Discovery & Research → **[THIS SKILL]** → Narrative Building → Spec Writing → Outcome Measurement

**Chain interface:**
- **Receives:** Problem definition with target market and customer segment (from Problem Framing), or raw context (competitive question, market entry scenario, competitor move to respond to)
- **Produces:** Competitive War Map with 7 Powers scoring, moat assessment, disruption vectors, GTM comparison, and strategic recommendations with confidence levels
- **Handoff artifact:** The Competitive War Map's "Strategic Recommendations" section maps directly to Narrative Building's input (positioning choices) and Spec Writing's input (competitive requirements)

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Fitness Check passed: problem is external/competitive, not internal/activation
- [ ] If external-only data: flagged prominently in Executive Summary; confidence capped at M
- [ ] How to Read This Document section present with role-based reading guide
- [ ] Notation Key present: H/M/L, T1-T6, 🟢🟡🔴, O→I→R→C→W all explained
- [ ] Executive Summary uses zero framework jargon — plain language only
- [ ] Competitive set defined: primary (3-5) + secondary (3-6) + non-obvious (2-3)
- [ ] Executive summary: 5 sentences a VP could act on alone
- [ ] 7 Powers scored for each primary competitor with evidence
- [ ] Switching costs decomposed by type (not high/medium/low)
- [ ] Aggregation Theory applied — who owns user relationship? Who's commoditized?
- [ ] JTBD mapped — what jobs hired for? Over-served vs. under-served?
- [ ] Network effects decomposed — type, strength, asymptotic, multi-tenanting?
- [ ] Disruption vectors assessed — low-end, new-market, or COAP?
- [ ] Value chain mapped — who controls each link? Where is margin?
- [ ] Wardley positions plotted — genesis vs. commodity? Misallocation?
- [ ] Feature/capability matrix with strategic weight per capability
- [ ] GTM/distribution/pricing comparison
- [ ] Customer/user signals included (not just company claims)
- [ ] Asymmetric competition identified — anyone fighting a different war?
- [ ] Blue Ocean check: Strategy Canvas plotted; ERRC Grid completed; arena reframe considered
- [ ] Adoption stage assessed: market position on Technology Adoption Lifecycle identified; chasm status evaluated; whole product gap named
- [ ] Win/Loss patterns mapped to framework conclusions: each pattern attributed to a specific 7 Powers, JTBD, Aggregation Theory, or Chasm finding
- [ ] Three horizons covered — current (H1), adjacent (H2), paradigm (H3)
- [ ] Leading indicators identified — what to watch weekly?
- [ ] Counterfactuals stated — "what if we're wrong" for each conclusion
- [ ] Quantified where possible — order of magnitude, not qualitative
- [ ] Evidence triangulated — no conclusion on single tier
- [ ] Uncommon knowledge ratio high — insight > context
- [ ] Every section ends with "So What" and decision trigger
- [ ] Framework selection routing done (Step 0) — primary frameworks identified, irrelevant frameworks skipped
- [ ] Per-cell evidence tier annotation in ALL comparison matrices (not just headline claims)
- [ ] O→I→R→C→W cascade applied to ALL recommendations (not just final section)
- [ ] H/M/L confidence levels explicit on every strategic conclusion — no weasel words
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source >6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key conclusion resting only on Tier 4-6 evidence
- [ ] Assumption Registry present with ≥3 load-bearing assumptions
- [ ] Adversarial Self-Critique section present with ≥3 genuine weaknesses
- [ ] Cross-framework contradictions surfaced explicitly (not resolved artificially)

---

## Worked Example

### Input

> "We're a Series B B2B analytics platform (Vanta Analytics) competing in the mid-market BI space. Primary competitors: Looker (now Google Cloud), Metabase, Mode Analytics. Concerned about two things: (1) Looker's Google acquisition giving them distribution advantages, and (2) an AI-native upstart called Cascade claiming 'no-code analytics for everyone.' We need a competitive war map to decide whether to prioritize enterprise motion or double down on self-serve."

---

### Output (abbreviated — demonstrates key formats; a full war map would cover all 7 steps)

**Executive Summary (5 sentences):**
Looker has locked in enterprise via Switching Cost + Scale Economies but its Google integration has created counter-positioning opportunities for products that don't require sales-led deployment. Metabase holds the self-serve segment through a strong Network Effects-adjacent community moat, but its open-source architecture creates a free tier dilution problem. Mode is commoditizing — it has no durable Power and is losing the data scientist segment to notebooks. Cascade represents a genuine H2 threat via new-market disruption: it targets the 80% of business users who never learned SQL, a segment Vanta Analytics isn't currently serving. **Decision: pursue self-serve motion targeting the "data-curious non-analyst" segment — this is the market Cascade will own in 24 months if Vanta doesn't.**

---

**7 Powers Heat Map:**

| Power | Looker | Metabase | Mode | Cascade | Vanta |
|---|:---:|:---:|:---:|:---:|:---:|
| Scale Economies | 🟢 Google infra | 🔴 None | 🔴 None | 🔴 None | 🟡 Growing |
| Network Effects | 🟡 Ecosystem | 🟢 OSS community | 🔴 None | 🟡 Data loops | 🔴 None |
| Counter-Positioning | 🔴 None | 🟡 OSS vs. paid | 🔴 None | 🟢 AI vs. SQL | 🟡 vs. Looker |
| Switching Costs | 🟢 LookML lock-in | 🟡 Moderate | 🔴 Low | 🔴 None yet | 🟡 Moderate |
| Branding | 🟢 Enterprise trust | 🟡 Dev brand | 🟡 Data science | 🔴 Nascent | 🔴 Unknown |
| Cornered Resource | 🟢 Google distribution | 🔴 None | 🔴 None | 🔴 None | 🔴 None |
| Process Power | 🟡 Sales motion | 🔴 None | 🔴 None | 🔴 None | 🔴 None |

📊 [Tier 1: LookML job postings show 3x growth post-Google acquisition — data.linkedin.com, Jan 2026] [Tier 1: Metabase GitHub stars 35K+ — github.com/metabase, Feb 2026] [Tier 5: Cascade "no-code AI analytics" launch blog post, Jan 2026]

**Decision point from heat map:** Looker holds 4 Powers (🟢🟢🟢🟡 across Scale, Switching Costs, Branding, Cornered Resource) → likely long-term enterprise winner. Vanta should NOT compete in enterprise-first motion against a 4-Power incumbent. Self-serve and mid-market are the only contestable spaces.

---

**Switching Cost Decomposition — Looker:**

| Type | Looker | Metabase | Vanta |
|---|:---:|:---:|:---:|
| Financial/Contractual | ██████████ 10/10 | ██░░░░░░░░ 2/10 | ████░░░░░░ 4/10 |
| Data/Migration | █████████░ 9/10 | █████░░░░░ 5/10 | █████░░░░░ 5/10 |
| Workflow/Integration | █████████░ 9/10 | ████░░░░░░ 4/10 | ██████░░░░ 6/10 |
| Identity | ████████░░ 8/10 | █████░░░░░ 5/10 | ██░░░░░░░░ 2/10 |
| Learning/Procedural | ████████░░ 8/10 | ████░░░░░░ 4/10 | ███░░░░░░░ 3/10 |
| Relational/Trust | ███████░░░ 7/10 | ███░░░░░░░ 3/10 | ██░░░░░░░░ 2/10 |

**Key insight:** Looker's switching costs are primarily *customer-created* (LookML models accumulate over time, 100+ dashboards built on LookML syntax) — this is the most durable moat type. Vanta's switching costs are primarily vendor-imposed (contracts) — which is the weakest moat type. **Strategic implication: Vanta must generate customer-created switching costs quickly. The path is workflow integration depth (connect to their data stack) not contractual lock-in.**

---

**Cascade Disruption Assessment (New-Market Vector):**

| Christensen Test | Evidence | Assessment |
|---|---|---|
| Serves non-consumers? | Business users who said "I'll never learn SQL" | ✅ Yes — this is non-consumption |
| "Good enough" for the job? | NPS 62 from non-technical beta users [Tier 5: launch post] | ✅ Yes for simple queries |
| Incumbent can't respond? | Looker's identity is SQL-based; switching would cannibalise LookML customers | ✅ Counter-positioning exists |
| Trajectory toward mainstream? | Q3 2026 launch: "AI that writes SQL from English" — moving up-market | ⚠️ Watch indicator |

**So What:**
"Cascade is entering via new-market disruption [Tier 5, corroborated by product trajectory], targeting business users who were never Vanta customers [non-consumption]. Our risk is not that Cascade takes existing customers — it's that Cascade *expands* the market and owns the segment Vanta hasn't captured yet [Aggregation Theory: they'll own the user relationship for a fast-growing segment]. Response: ship a no-code natural language query interface within 6 months, before Cascade's user base becomes an entrenched community moat [est. $800K eng cost vs. $5M+ CAC to win back lost segment]. This assumes Cascade doesn't raise a large round and accelerate their roadmap [est. 40% probability within 12 months, based on current traction signals]."

---

### Why This Works

This output was produced by running steps 2, 3, and 4 of the Full Application Method: 7 Powers heat map with evidence tiers, switching cost decomposition distinguishing customer-created vs. vendor-imposed costs, and the new-market disruption test applied to Cascade. It satisfies the Elite Tier Quality Gradient: every structural conclusion has a "So What" with mechanism, response, and confidence level; uncommon knowledge (Cascade's non-consumption angle) is foregrounded over obvious observations; and the executive summary alone is actionable for a board decision.

---

## References

**Framework Sources:**
- Hamilton Helmer, *7 Powers: The Foundations of Business Strategy* (2016)
- Ben Thompson, *Stratechery* — Aggregation Theory series (2015-present)
- Clayton Christensen et al., *Competing Against Luck* (2016); *The Innovator's Dilemma* (1997)
- Roger Martin & A.G. Lafley, *Playing to Win* (2013)
- Simon Wardley, *Wardley Maps* (CC-BY-SA, wardleymaps.com)
- Clayton Christensen, *The Law of Conservation of Attractive Profits* (Harvard Business Review, 2004)
- NFX, *The Network Effects Manual* (nfx.com)
- Kevin Kwok, *kwokchain* — Data Content Loops, Rich Barton Playbook (kwokchain.com)
- Barbara Minto, *The Pyramid Principle* (1987) — SCQ-A framework

**Related Skills in PM Skills Arsenal:**
- Problem Framing — upstream (defines what market to analyze)
- Discovery & Research — parallel (demand-side primary research)
- Narrative Building — downstream (uses competitive positioning)
- Spec Writing — downstream (competitive requirements)
- Outcome Measurement — downstream (competitive metrics tracking)

---

*Created: 2026-02-18 | PM Skills Arsenal v1.0 | BLD-003*
*Quality tier: Elite (≥600 lines, 7+ encoded frameworks, quality gradients, 9 failure modes, reader navigation, context gate)*
*License: MIT*
