# Competitive Analysis Toolkit

> **Purpose:** The complete analytical methodology for producing elite-tier competitive and market analysis. Frameworks, lenses, evidence standards, output quality markers. Everything an agent (or the user) needs to go from "list the competitors" to "$500K strategy engagement."
>
> **Source:** Synthesized from Stratechery (Thompson), 7 Powers (Helmer), Competing Against Luck (Christensen), Playing to Win (Martin/Lafley), NFX Network Effects Manual, kwokchain (Kwok), Wardley Mapping (Wardley), McKinsey SCQ-A framework (Minto Pyramid Principle). All publicly available published work.
>
> **How to use:** Don't dump this whole file into a conversation. Pick the frameworks relevant to the question. The distilled playbook version (~60 lines) lives in PLN-003_assets for demo purposes, but THIS file is the full reference.

---

## Part 1: Strategic Frameworks (Beyond Porter & SWOT)

### 1.1 Hamilton Helmer's 7 Powers

The gold standard for analyzing **durable competitive advantage**. Score every competitor against all 7:

| Power | Definition | Key Question |
|-------|-----------|--------------|
| **Scale Economies** | Per-unit cost declines as production volume increases | Does the incumbent's cost structure punish new entrants at lower scale? |
| **Network Effects** | Value to each user increases with the number of users | Is growth self-reinforcing? (See §3.3 for taxonomy) |
| **Counter-Positioning** | A newcomer adopts a business model an incumbent can't copy without damaging their existing business | Would matching our move cannibalize the incumbent's core revenue? |
| **Switching Costs** | The value loss a customer would experience by switching to an alternative | What would a customer lose — data, workflow, identity, integrations — by leaving? (See §3.4) |
| **Branding** | A durable attribution of higher value to an objectively identical product | Does the brand command a price premium or reduce customer acquisition cost? |
| **Cornered Resource** | Preferential access to a valuable asset — talent, IP, regulatory license — that cannot be replicated | What scarce input can't be bought on the open market? |
| **Process Power** | Organization embeddings and complex process superiority built over time | Is the advantage embedded in organizational culture/process rather than any single technology? |

**How to use it:** For every competitor (including yourself), map which Powers they hold, how strong each is (nascent → mature), and where the power is *accruing vs. eroding*. Critical insight: **power must exist before victory is won** — a company that wins without power will lose that position quickly.

---

### 1.2 Ben Thompson's Aggregation Theory

The definitive lens for understanding **Internet-era competitive dynamics**.

**The Value Chain Inversion:**
- Pre-Internet: Distribution was scarce → distributors integrated backward into supply → owned suppliers
- Post-Internet: Distribution is free → transaction costs zero → integrate forward into user relationship → commoditize suppliers

**Three Characteristics of Aggregators:**
1. Direct relationship with users (payment, account, or habitual usage)
2. Zero marginal costs for serving users
3. Demand-driven multi-sided networks with decreasing acquisition costs

**Aggregator Classification:**

| Level | Supply Relationship | Example |
|-------|-------------------|---------|
| Level 1 | Acquires supply (pays for it) | Netflix |
| Level 2 | Doesn't own supply, but incurs onboarding transaction costs | Uber |
| Level 3 | Doesn't own supply, zero supplier costs | Google |
| Super-Aggregator | Multi-sided, zero costs on all sides | Google, Meta |

**Analytical questions:**
- What is the scarce resource being distributed?
- Which component has become commoditized (and who's commoditizing it)?
- Who owns the user relationship, and is that ownership durable?
- Where is value shifting — toward supply or toward demand ownership?

---

### 1.3 Christensen's Disruption Theory — Applied

Not just "low-end disruption." The full toolkit:

**Disruption Vector Analysis:**
- **Low-end disruption:** "Good enough" product at dramatically lower cost to over-served customers
- **New-market disruption:** Serves non-consumers who couldn't access the market before
- **Hybrid disruption:** Enters low end AND expands the market simultaneously

**Conservation of Attractive Profits (COAP):**
> When one layer of a value chain becomes modularized and commoditized, an adjacent layer becomes integrated and earns outsized profits.

Most underused Christensen concept. For competitive analysis:
1. Identify each layer of the value chain
2. Which layers are becoming commoditized right now?
3. Where will profits shift as commoditization completes?
4. Is any player actively integrating the newly attractive layer?

**"Isn't Good Enough" / "More Than Good Enough" Test:**
- Product isn't good enough for most users → integrated architectures win (incumbent is safe)
- Product is more than good enough → modular architectures win (disruption incoming)

---

### 1.4 Roger Martin's "Where to Play / How to Win"

The strategy-as-choice cascade:

1. **What is our winning aspiration?** (Concrete market position, not mission statement)
2. **Where to play?** (Markets, segments, channels, geographies, customer types)
3. **How to win?** (Cost leadership? Differentiation? What specific capability advantage?)
4. **What capabilities must be in place?**
5. **What management systems are required?**

**Analytical application:** For each competitor, reverse-engineer their strategy cascade. Most companies' stated strategy doesn't match their revealed strategy. The gap between what they *say* and what their resource allocation *reveals* is where the insight lives.

---

### 1.5 Wardley Mapping

Plot every component of the value chain on two axes:
- **Y-axis (visibility):** How visible to the end user? (User needs at top → infrastructure at bottom)
- **X-axis (evolution):** Where on the evolution curve?

| Stage | Characteristics | Competitive Implications |
|-------|----------------|------------------------|
| Genesis | Novel, uncertain, high failure rate | First-mover possible but risky |
| Custom Build | Emerging understanding, bespoke | Differentiation opportunity |
| Product (+rental) | Increasingly understood, feature competition | Consolidation, M&A |
| Commodity (+utility) | Standardized, cost competition | Margin compression, shift to utility |

**Key insight:** Different components of the SAME product can be at different evolutionary stages. Don't custom-build what's commodity. Don't commoditize what's genesis.

**Competitive application:**
1. Map your product's components
2. Map each competitor on the same map
3. Where are they investing in genesis/custom? (Their bet on the future)
4. Where are they sourcing commodity? (What they've given up owning)
5. Spot mismatches: custom effort on commodity = waste; commoditizing genesis = unstable foundation

---

### 1.6 Jobs-to-be-Done Competitive Analysis

Customers don't buy products — they "hire" them for a job. Competition isn't between similar products; it's between anything hired for the same job.

**JTBD Structure:**
1. **Functional job:** What is the customer trying to accomplish?
2. **Emotional job:** How does the customer want to feel?
3. **Social job:** How does the customer want to be perceived?
4. **Consumption chain:** What happens before, during, and after? Where are the pain points?

**Competitive Landscape Map (JTBD version):**
- Don't list "products that look like ours"
- List "everything a customer might hire for this job" — including manual processes, workarounds, doing nothing
- Rate each on satisfaction of functional, emotional, and social jobs
- Identify: over-served jobs (ripe for disruption) vs. under-served jobs (growth opportunity)

---

### 1.7 Kevin Kwok's Data Content Loops

For markets where the competitive weapon is information disintermediation:

**The "Rich Barton Playbook":**
1. Identify an industry where intermediaries hoard information
2. Build a Data Content Loop: authoritative data → definitive page for every entity
3. Dominate search for every entity in the category
4. Own demand: users come to you first → you dictate terms to supply

**Loop mechanics:** Data → Content → SEO dominance → Traffic → More data → Better content → Stronger SEO → compounds

**Application:** Who controls the data-content-discovery loop? Who owns demand? What breaks the loop?

---

## Part 2: Research Methodology

### 2.1 Evidence Quality Tiers

| Tier | Source Type | Weight | Example |
|------|-----------|--------|---------|
| **Tier 1** | Direct behavioral data (what people DO) | Highest | Usage analytics, revenue, app store data, patent filings, SEC filings, job postings |
| **Tier 2** | Primary research, credible methodology | High | Well-sampled surveys, structured interviews, controlled experiments |
| **Tier 3** | Expert analysis with disclosed reasoning | Medium-High | Stratechery, a16z, McKinsey with disclosed data, academic papers |
| **Tier 4** | Industry reports from reputable firms | Medium | Gartner, IDC, Forrester (useful for sizing, less for insight) |
| **Tier 5** | Executive statements and press releases | Low-Medium | Strategic signaling, not factual reporting — analyze for what they reveal about strategy |
| **Tier 6** | Punditry, blog posts, social media | Low | Sentiment only; never for facts |

**Triangulation Rule:** No strategic conclusion rests on a single evidence tier. Minimum 2 tiers, ideally 3.

### 2.2 Leading vs. Lagging Indicators

| Category | Lagging (already happened) | Leading (about to happen) |
|----------|---------------------------|--------------------------|
| Product | Market share, revenue, margins | Job postings, patent filings, API changes, dev docs updates |
| Market | Industry revenue, installed base | Switching cost erosion rate, NPS velocity (direction, not absolute) |
| Competitive | Announced products, launched features | Acqui-hires, open-source contributions, research papers, keynote topics |
| User | Downloads, MAU, DAU | Cohort retention curves, time-to-value, feature adoption velocity |

### 2.3 Signal vs. Noise Filter

1. **Frequency:** Recurring or one-off?
2. **Source credibility:** Primary actor or secondary commentator?
3. **Falsifiability:** Could this signal be false? What would falsify it?
4. **Structural significance:** Change in market *structure* (durable) or market *weather* (temporary)?
5. **Convergence:** Do multiple independent signals point the same direction?

### 2.4 Source Structuring

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

## Part 3: Analytical Lenses

### 3.1 Demand-Side vs. Supply-Side

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

### 3.2 Value Chain Decomposition

```
[Raw capability] → [Platform/infra] → [Product] → [Distribution] → [Customer relationship] → [Monetization]
```

For each link:
- Who controls it? (Single player vs. fragmented)
- What's the margin? (High = value capture; low = commoditized)
- Moving toward integration or modularization? (Per Christensen's COAP)
- What would it take to disintermediate?
- Where is value migrating? (Most important — precedes market share shift)

**The Smile Curve:** Value accrues at the extremes — upstream (IP, platform, data) and downstream (brand, customer relationship). The middle (assembly, basic service) gets squeezed. Map where each competitor sits.

### 3.3 Network Effects Taxonomy

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

### 3.4 Switching Cost Decomposition

Never rate "high/medium/low." Decompose by type:

| Type | Description | Durability |
|------|-------------|-----------|
| **Financial** | Contractual penalties, repurchase costs | Low — money solves money problems |
| **Procedural/Learning** | Time and effort to learn new system | Moderate — degrades as UX improves |
| **Data/Migration** | Moving data, losing history, reconfiguring integrations | High — grows with usage duration |
| **Relational** | Loss of relationships, trust, accumulated reputation | Very high — can't be replicated |
| **Identity** | Product is part of self-image ("I'm an Apple person") | Very high — psychological, not rational |
| **Workflow/Integration** | Embedded in workflows, connected to other tools | Very high — compounds over time |
| **Contractual/Regulatory** | Legal or compliance barriers | Structural — not the company's moat but acts as one |

**Key insight:** The most durable switching costs are ones customers CREATE through use (data accumulation, workflow embedding, identity). Not the ones vendors impose (contracts). Companies relying on imposed switching costs sit on erosion-prone moats.

### 3.5 Asymmetric Competition

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

---

## Part 4: Output Quality Markers

### 4.1 The "So What" Cascade

Never write "Competitor X does Y." Structure every insight as:

```
OBSERVATION → IMPLICATION → STRATEGIC RESPONSE → CONFIDENCE LEVEL

"[Competitor] is [doing X],
which threatens [our position Y] because [mechanism Z],
our response should be [action] because [reasoning],
but this depends on [assumption] which we assess at [confidence]."
```

**Bad:** "Google is investing heavily in AI search."

**Elite:** "Google shipped AI Overviews to 100% of English queries (Tier 1: product data), threatening our content-based acquisition because AI Overviews absorb the click that went to our page (mechanism: zero-click cannibalizes referral traffic). Response: shift from search-dependent to direct-relationship channels — email and in-app loops — because retained users have 6x LTV of search-acquired (Tier 1: internal data). Assumes Google doesn't build product-specific answer cards (est. 60% probability within 18mo based on API trajectory)."

### 4.2 Counterfactual & Scenario Analysis

**"What if we're wrong?"** — for every strategic conclusion:
- State the key assumption
- State what would falsify it
- State the leading indicator to watch

**Three-Scenario Framework:**

| Scenario | Probability | Key Driver | Response |
|----------|------------|------------|----------|
| Base case | 50-60% | Current trends continue | [Actions] |
| Bull case | 15-25% | What goes right | [Capitalize] |
| Bear case | 15-25% | What goes wrong | [Mitigate] |

**Pre-Mortem:** "It's 18 months from now and our strategy failed. What happened?" Forces you to surface risks you're rationalizing away.

### 4.3 Quantified Impact Estimates

| Instead of | Write |
|-----------|-------|
| "Large market opportunity" | "$X B TAM, growing Y% CAGR, $Z B addressable given our distribution" |
| "Significant switching costs" | "~X hours config, Y integrations, Z months history; est. migration cost $W and T weeks productivity loss" |
| "Growing fast" | "X% MoM growth in [metric], reaching [milestone] by [date] at current trajectory" |
| "Strong position" | "X% share in segment Y, Z Powers from Helmer, net switching cost advantage of $W/seat" |

**Order of Magnitude Rule:** Even when imprecise, state $1M vs $10M vs $100M vs $1B. Getting magnitude right = 80% of value. "Large" = 0%.

### 4.4 Citation Patterns

| Generic | Elite |
|---------|-------|
| "According to Gartner..." (argument from authority) | Uses Gartner for sizing, applies own framework for conclusions |
| No sources | Every claim has source + date; every inference labeled as inference |
| Relies on secondary reporting | Goes to primary sources, draws own conclusions |
| Company PR as evidence | Company statements as strategic signaling — analyzes what signal reveals |
| Single framework | Multiple frameworks on same question; notes where they agree (confidence) and diverge (investigate) |

### 4.5 Board-Ready Quality Check

1. Does every section have a "so what"? If removable without changing a decision, remove it.
2. Key finding on page 1, not page 30? (Pyramid principle — lead with conclusion)
3. Recommendations actionable this quarter? ("invest in AI" is not actionable)
4. Distinguishes what we know / believe / guess? Labeled explicitly.
5. Names the decision it informs? Every analysis answers: "what do we do differently?"

---

## Part 5: Meta-Frameworks

### 5.1 The 3 Horizons Competition Map

| Horizon | Timeframe | Competitors | Approach |
|---------|----------|-------------|----------|
| H1: Current | 0-12 months | Direct (same category) | Share, features, churn, win/loss |
| H2: Adjacent | 12-36 months | Adjacent products expanding toward you | Bundle/unbundle, platform plays, JTBD overlap |
| H3: Paradigm | 36+ months | Different paradigm entirely | Scenario planning, disruption theory, tech curves |

Most analyses only do H1. By the time H3 is H1, it's too late.

### 5.2 SCQ-A (Minto Pyramid Principle)

1. **Situation:** Current market structure (size, growth, segmentation, value chain)
2. **Complication:** What is changing (tech shifts, regulation, new entrants, behavior changes)
3. **Question:** Given the complication, what should we do?
4. **Answer:** Recommendation supported by evidence and frameworks

Backbone of every top-tier strategy deck.

### 5.3 The Uncommon Knowledge Test

- Would a smart generalist already know this? → Context, not insight. Include minimally.
- Would a domain expert know this? → Domain knowledge. Include for completeness.
- Would neither know this? → THIS is insight. Lead with this.

Elite analyses have a high ratio of uncommon knowledge to table-stakes context. Context section = shortest. Insight section = longest.

---

## Part 6: Tactical Layers (Feature, GTM & Customer)

> **Purpose:** Strategic frameworks answer "who wins structurally." These tactical layers answer "where do we win/lose TODAY" and "what are customers actually saying." A leader needs BOTH. Strategy without tactics is philosophy. Tactics without strategy is noise.

### 6.1 Feature/Capability Comparison Matrix

The detailed product-level comparison. This is what a PM or engineer looks at to understand the ground truth beneath the strategy.

**Structure:**
- Rows = key capabilities relevant to the category (not a laundry list — pick the 10-15 that drive adoption/churn/differentiation)
- Columns = each competitor
- Rating per cell: ✅ shipped | 🔄 in preview/beta | 🚧 announced/roadmapped | ❌ absent
- REQUIRED: add a "Why It Matters" column explaining the strategic weight of each capability

**Example (AI copilot/assistant category):**

```
| Capability              | Microsoft Copilot | Google Gemini | Apple Intelligence | ChatGPT | Why It Matters |
|------------------------|:---:|:---:|:---:|:---:|---|
| On-device inference     | 🚧  | 🔄  | ✅  | ❌  | Privacy + offline = enterprise table stakes by 2027 |
| Enterprise admin/policy | ✅  | 🔄  | ❌  | 🚧  | IT buyer gate — no admin = no enterprise deal |
| Plugin/extension ecosystem | ✅ | 🔄 | ❌ | ✅ | Developer ecosystem = compounding moat |
| Multimodal input        | 🔄  | ✅  | ✅  | ✅  | Mobile-first interaction paradigm |
| Proactive suggestions   | 🔄  | 🔄  | ✅  | ❌  | This is where mobile AI wins or loses |
| Offline functionality   | ❌  | ❌  | ✅  | ❌  | Apple's structural advantage on mobile |
```

**Rules:**
- Don't list 50 features. Pick the ones that DRIVE switching or retention decisions.
- Flag where a feature gap is structural (hard to close) vs. tactical (just engineering time).
- Include the #1 feature gap — the capability where the biggest competitor lead exists.

### 6.2 GTM & Distribution Comparison

Strategy wins in the long run. GTM wins this quarter. A leader needs both.

```
| GTM Dimension        | Competitor A | Competitor B | Competitor C |
|---------------------|---|---|---|
| Pricing model        | ... | ... | ... |
| Price point           | ... | ... | ... |
| Free tier             | ✅/❌ | ... | ... |
| Enterprise motion     | ... | ... | ... |
| Distribution channel  | ... | ... | ... |
| Bundle leverage       | ... | ... | ... |
| Self-serve available? | ... | ... | ... |
```

**Why this matters:** A competitor with $0 marginal cost to distribute (Apple ships with every phone) has a structural GTM advantage that no sales team overcomes.

### 6.3 Customer & User Signal Analysis

What companies claim ≠ what users experience. Ground the analysis in reality.

**Sources (priority order):**
1. App store reviews at scale — themes, not individual reviews. Rating trends (direction > absolute).
2. NPS/CSAT signals if public.
3. Usage data — DAU/MAU ratio, retention curves, feature adoption rates.
4. Community/support forums — struggles reveal product-market fit gaps.
5. Social sentiment — directional only.
6. Churn/switching anecdotes — "I switched because..." is gold.

**Output format:**
```
| Signal                   | Competitor A | Competitor B | Competitor C |
|-------------------------|---|---|---|
| App store rating (trend) | ⬆️/➡️/⬇️ | ... | ... |
| Top praise               | "..." | "..." | "..." |
| Top complaint            | "..." | "..." | "..." |
| Engagement signal        | 📊 [source] | 📊 [source] | 📊 [source] |
```

### 6.4 Competitive Set Definition Framework

Don't let the AI randomly pick who to analyze.

**Three tiers:**
1. **Primary** (same category, direct substitutes) — full analysis: all 7 Powers, switching costs, feature matrix, GTM, customer signals. 3-5 competitors.
2. **Secondary** (adjacent, expanding toward you) — 7 Powers scan, JTBD overlap, timeline-to-direct-competition. 3-6 products.
3. **Non-obvious / paradigm threats** (H3) — scenario analysis, probability, leading indicators. Often forces, not products.

**Rule:** If the analysis only covers competitors the reader thinks about daily, it's not worth reading.

---

## Part 7: Visualization & Formatting for Maximum Impact

> **Purpose:** Text-based AI can produce visually structured output that reads like a strategy deck, not a wall of paragraphs. These formatting patterns turn good analysis into analysis that LOOKS elite at first glance.

### 6.1 Competitive Scorecard (7 Powers Heat Map)

Instruct the AI to produce a per-competitor scorecard with visual strength indicators:

```
| Power              | Google Gemini | Apple Intelligence | Microsoft Copilot | Notion AI |
|--------------------|:---:|:---:|:---:|:---:|
| Scale Economies    | 🟢 Strong     | 🟡 Moderate        | 🟢 Strong    | 🔴 Weak   |
| Network Effects    | 🟢 Data NE    | 🟡 Ecosystem       | 🟢 Graph     | 🟡 Collab  |
| Counter-Position   | 🔴 None       | 🟢 Privacy         | 🔴 None      | 🟡 Unbundle|
| Switching Costs    | 🔴 Low        | 🟢 Ecosystem       | 🟢 Enterprise | 🔴 Low    |
| Cornered Resource  | 🟢 TPUs/Talent| 🟢 Chips/Privacy   | 🟡 Graph     | 🔴 None   |
```

Key: 🟢 = accruing and durable, 🟡 = present but eroding or limited, 🔴 = absent or weak

**Why it works:** Audience can see competitive positioning in 3 seconds. A wall of text saying "Google has scale economies" doesn't register the same way.

### 6.2 Switching Cost Decomposition Matrix

Don't just say switching costs are "high" — show the breakdown visually:

```
| Switching Cost Type     | Microsoft Copilot | Google Gemini | Apple Intelligence |
|------------------------|:---:|:---:|:---:|
| Financial/Contractual   | ████████░░ 8/10 | ███░░░░░░░ 3/10 | █████░░░░░ 5/10 |
| Data/Migration          | █████████░ 9/10 | ████░░░░░░ 4/10 | ██████░░░░ 6/10 |
| Workflow/Integration    | █████████░ 9/10 | ██░░░░░░░░ 2/10 | ███████░░░ 7/10 |
| Identity ("I'm a ___ shop") | ████████░░ 8/10 | █████░░░░░ 5/10 | █████████░ 9/10 |
| Learning/Procedural     | ██████░░░░ 6/10 | ████░░░░░░ 4/10 | ███░░░░░░░ 3/10 |
| Relational/Trust        | ███████░░░ 7/10 | ███░░░░░░░ 3/10 | ████████░░ 8/10 |
```

**Progress bars (█░) show relative strength at a glance.** The audience sees which moats are deep and which are eroding without reading a single paragraph.

### 6.3 Asymmetric Competition Map

Format as a structured comparison that makes different competitive strategies visible:

```
## Competitive War Map — Who's Fighting What War?

### 🎯 Google Gemini
- **Optimizes for:** Consumer AI mindshare → "AI = Google"
- **Willing to sacrifice:** Enterprise margins, direct revenue
- **Time horizon:** 2-year growth play
- **Winning looks like:** AI assistants default to Google
- **Cost to add 1 user:** ~$0 (search + Android distribution)

### 🍎 Apple Intelligence  
- **Optimizes for:** Device ecosystem stickiness → "privacy-first AI"
- **Willing to sacrifice:** Cloud AI capability, developer platform
- **Time horizon:** 10-year platform bet
- **Winning looks like:** AI that only works on Apple devices
- **Cost to add 1 user:** ~$0 (on-device, ships with hardware)

### 🔷 Microsoft Copilot
- **Optimizes for:** Enterprise workflow embedding → "Copilot in every app"
- **Willing to sacrifice:** Consumer market, free tier
- **Time horizon:** 3-year enterprise platform cycle
- **Winning looks like:** Copilot indistinguishable from Office itself
- **Cost to add 1 user:** ~$30/seat/mo (premium tier)
```

**Why it works:** Shows competitors aren't fighting the same war. A feature comparison misses this entirely.

### 6.4 Three Horizons Threat Landscape

Visual timeline format that shows threats escalating:

```
┌─────────────────────────────────────────────────────────────────┐
│ COMPETITIVE THREAT TIMELINE                                     │
├──────────────┬──────────────────┬───────────────────────────────┤
│  H1 (0-12mo) │  H2 (12-36mo)    │  H3 (36mo+)                   │
│  Direct       │  Adjacent         │  Paradigm                     │
├──────────────┼──────────────────┼───────────────────────────────┤
│ Google Gemini │ Notion AI         │ AI assistants replace         │
│ feature parity│ expanding up      │ productivity suites entirely  │
│               │                   │                               │
│ ChatGPT       │ Slack AI          │ Open-source AI models make    │
│ mobile app    │ workflow AI       │ commercial copilots obsolete  │
│               │                   │                               │
│ Samsung AI    │ Zoom AI           │ OS-level AI (Android/iOS)     │
│ on-device     │ meeting→workflow  │ bypasses all apps             │
└──────────────┴──────────────────┴───────────────────────────────┘
```

### 6.5 Evidence-Tiered Claims

Inline evidence tagging makes claims visually verifiable:

```
- Google's TPU v5 investment suggests $4-6B annually in AI infrastructure
  📊 [Tier 1: Alphabet 10-K FY2025, CapEx breakdown]

- Developer adoption of Gemini API growing ~40% QoQ
  📊 [Tier 1: Google Cloud Next keynote, API usage data]

- Apple on-device AI performs comparably to cloud for common tasks
  📊 [Tier 3: AnandTech benchmarks, independent testing]

- Enterprise IT prefers Microsoft for AI governance controls  
  📊 [Tier 4: Gartner Magic Quadrant 2025, survey methodology]
  ⚠️ [Tier 5: Microsoft exec claim — treat as signaling]
```

### 6.6 Scenario Comparison Table

Structured scenario planning with visual probability weighting:

```
| Scenario | Probability | Key Driver | Impact on Microsoft Copilot | Our Response |
|----------|:-----------:|------------|----------------------|---------------|
| 🟢 Base  | 55%        | Current trends continue; enterprise AI adoption grows 30% YoY | Maintain #1 enterprise position | Double down on Graph + workflow |
| 🔵 Bull  | 20%        | Apple Intelligence underdelivers; enterprise consolidates on M365 | Expand TAM into mid-market | Accelerate SMB tier |
| 🔴 Bear  | 25%        | Google ships free enterprise Gemini; open-source closes gap | Price pressure, margin compression | Deepen switching costs, lock integration |
```

### 6.7 "So What" Cascade — Visual Chain

Format insight chains as clear visual progressions:

```
OBSERVATION
  Google shipped AI Overviews to 100% of English queries
  📊 Tier 1: Product data, Feb 2026
       ↓
IMPLICATION  
  Zero-click answers absorb traffic that drove enterprise discovery
  Threatens content-based customer acquisition for M365 ecosystem
       ↓
RESPONSE
  Shift from search-dependent to direct-relationship channels
  (email loops, in-app discovery, Teams-native recommendations)
       ↓  
CONFIDENCE: 70%
  Assumes Google doesn't build product-specific answer cards
  WATCH: Google Search API changes, click-through rate trends
  FALSIFIED IF: organic traffic to learn.microsoft.com increases (counter-trend)
```

### 6.8 Competitive Response Matrix

Action-response format for strategic planning:

```
| If competitor does... | Who | Impact (1-5) | Our best response | Timeline |
|----------------------|-----|:---:|------------------------------|----------|
| Ships free enterprise AI | Google | ⚠️ 5 | Deepen Graph integration moat | 0-6mo |
| On-device AI matches cloud | Apple | ⚠️ 4 | Hybrid cloud+edge architecture | 6-12mo |
| AI-native docs replace Office | Notion | ⚠️ 3 | Copilot becomes the creation surface | 12-24mo |
| Open-source matches GPT-4 | Meta/OSS | ⚠️ 4 | Differentiate on enterprise trust | 6-18mo |
```

### 6.9 Value Chain Smile Curve (ASCII)

Visual representation of where value accrues:

```
Value
  │
  █                                                    █ █
  █ █                                                █ █
  █ █                                              █ █
  █   █                                          █ █
  █     █                                      █ █
  █       █           █ █ █ █ █ █           █ █
  █         █     █ █             █ █     █ █
  █           █ █                     █ █
  └──────────────────────────────────────────────────────
  Data/IP    Platform    Assembly/     Distribution   Customer
  Models     Infra       Basic Service Channel        Relationship
  
  ← High value                Squeezed              High value →
```

### 6.10 Formatting Rules for AI Output

1. **Lead with tables, not paragraphs.** Every comparison should be a table. Prose explains the table, not replaces it.
2. **Use emoji as visual markers** — 🟢🟡🔴 for status, ⚠️ for risk, 📊 for evidence, 🎯 for target. Scannable.
3. **Progress bars for relative strength** — ████░░░░ is instantly readable. "7 out of 10" requires parsing.
4. **Callout boxes for key insights** — use > blockquotes for "so what" statements that a reader skimming should catch.
5. **Numbered/ordered lists for priorities** — if rank matters, use numbers. Bullets imply equal weight.
6. **Bold the mechanism, not the fact** — "Google's TPU investment is **$4-6B annually**" vs "**Google** is investing in TPUs." The number is the insight.
7. **Section headers as conclusions** — not "Market Analysis" but "Google Owns the Data Loop. Microsoft Owns the Workflow. Apple Owns the Device." The header IS the insight.
8. **White space between sections** — dense walls of text kill comprehension at presentation distance.
9. **Inline evidence tags** — [Tier 1: SEC filing] after every major claim. Shows rigor instantly.
10. **End every section with a decision trigger** — "This means we should..." or "Watch for..." Never leave analysis dangling.

---

## Appendix: Quick-Reference Checklist

- [ ] Feature/capability matrix with specific product-level comparisons
- [ ] GTM/distribution/pricing comparison across competitors
- [ ] Customer/user signals included (not just company claims)
- [ ] Competitive set defined: primary + secondary + non-obvious
- [ ] Executive summary: 5 sentences a VP could act on alone
- [ ] Value chain mapped — who controls each link? Where is margin?
- [ ] 7 Powers scored — for each major competitor, which Powers, how strong?
- [ ] Aggregation Theory applied — who owns user relationship? Who's commoditizing suppliers?
- [ ] JTBD mapped — what jobs being hired for? Over-served vs. under-served?
- [ ] Network effects decomposed — type, strength, asymptotic, multi-tenanting?
- [ ] Switching costs decomposed — by type, not just high/medium/low
- [ ] Asymmetric competition identified — anyone fighting a different war?
- [ ] Wardley Map plotted — genesis vs. commodity? Misallocation?
- [ ] Leading indicators identified — what to watch weekly?
- [ ] Disruption vectors assessed — low-end, new-market, or COAP?
- [ ] Three horizons covered — current, adjacent, paradigm?
- [ ] Counterfactuals stated — "what if we're wrong" for each conclusion?
- [ ] Quantified where possible — order of magnitude, not qualitative
- [ ] Evidence triangulated — no conclusion on single tier
- [ ] Uncommon knowledge ratio high — insight > context

---

*Created: 2026-02-15*
*Sources: Stratechery (Thompson), 7 Powers (Helmer), Competing Against Luck (Christensen/Hall/Dillon/Duncan), Playing to Win (Martin/Lafley), NFX Network Effects Manual, kwokchain (Kwok), Wardley Mapping (Wardley), SCQ-A (Minto Pyramid Principle).*
