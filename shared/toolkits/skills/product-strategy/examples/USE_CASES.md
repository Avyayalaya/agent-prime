# Use Cases: Product Strategy

## Use Case 1: Annual Roadmap for a Growth-Stage B2B SaaS Platform

### Scenario
A Series C B2B analytics platform ($40M ARR, 120 employees, 35 engineers) needs to build its FY27 annual roadmap. The CEO wants to expand from mid-market into enterprise while maintaining growth in the core segment. The VP Engineering has flagged that the current architecture won't scale to enterprise-grade SLAs. The head of sales is pushing for 8 new features that enterprise prospects have requested. The PM needs to translate competing demands into a coherent strategy with explicit bets, sequencing, and resource allocation — not a feature backlog that appeases everyone.

### The Prompt
> We're a $40M ARR B2B analytics platform. We need our FY27 annual roadmap. Our CEO wants us to expand into enterprise, our VP Eng says the architecture needs rework for enterprise SLAs, and sales has a list of 8 features enterprise prospects want. We have 35 engineers. Help me build a strategy document.

### Without the Skill (Generic AI)
Here's a suggested FY27 roadmap for your enterprise expansion:

**Vision:** Become the leading analytics platform for mid-market and enterprise companies.

**Q1 Priorities:**
- Begin architecture rework for enterprise SLAs (high availability, SOC2)
- Build SSO and SCIM provisioning (top enterprise request)
- Start enterprise sales motion with 2 dedicated AEs

**Q2 Priorities:**
- Complete architecture migration
- Add role-based access control and audit logging
- Launch enterprise pricing tier

**Q3 Priorities:**
- Build advanced dashboard customization (enterprise request #3)
- Add data warehouse integrations (Snowflake, Databricks)
- Expand sales team to 5 enterprise AEs

**Q4 Priorities:**
- Custom reporting and white-labeling
- API rate limiting and enterprise SLAs
- Target 10 enterprise logos by year-end

**Key risks:**
- Architecture rework may take longer than expected
- Enterprise sales cycle is 6-9 months, so Q4 targets may be aggressive
- Splitting focus between mid-market and enterprise could hurt both

This plan balances technical foundation work with customer-facing features to support the enterprise motion.

### With the Skill

**Context Gate Assessment:**
- Problem defined? Partially. "Expand into enterprise" is a direction, not a problem. What specific enterprise pain point does our product solve that alternatives don't? (Context Gate flags a gap — this needs Problem Framing input, but we can proceed with caveats.)
- Market context? Yes — we know the competitive landscape and have enterprise prospect feedback (T5: sales team reports).
- Time horizon? Annual — appropriate.
- Resource constraints? Yes — 35 engineers, known architecture limitations.
- Company strategy alignment? Yes — CEO mandate for enterprise expansion.

**Vision Statement:**
"Become the analytics platform that mid-market companies adopt and enterprise companies can't rip out — 500+ enterprise customers and $80M ARR by FY28, with enterprise contributing >40% of new ARR by Q4 FY27."

**Falsification test:** If enterprise contributes <15% of new ARR by Q4 FY27, the enterprise expansion thesis is wrong and we should refocus on mid-market dominance.

**Strategic Bets (3 of 5 shown):**

**Bet 1: Platform Hardening (Core, H confidence)**
- **Hypothesis:** If we invest 40% of engineering capacity in architecture rework (HA, SOC2, enterprise SLAs), then we unlock the enterprise buyer who currently disqualifies us at security review, because 73% of lost enterprise deals cite infrastructure concerns (T3: sales team analysis).
- **Confidence:** H — the evidence that we lose deals on infrastructure is strong, and the technical scope is well-understood.
- **Investment:** 14 engineers x 2 quarters = 28 engineer-quarters (40% of annual capacity).
- **Kill criteria:** If architecture rework is not feature-complete by end of Q2, descope to minimum viable enterprise SLA and reassess.

**Bet 2: Enterprise Wedge Features (Adjacent, M confidence)**
- **Hypothesis:** If we build SSO/SCIM + RBAC + audit logging (the "enterprise trifecta"), then we convert 30% of pipeline prospects who passed on us for security/compliance reasons, because these 3 features appear in 85% of enterprise RFPs in our category (T2: RFP analysis).
- **Confidence:** M — we know these are table-stakes requirements, but converting prospects also depends on pricing, sales execution, and trust (brand) that features alone don't solve.
- **Investment:** 8 engineers x 3 quarters = 24 engineer-quarters (34% of annual capacity).
- **Kill criteria:** If <5 enterprise prospects enter pipeline specifically citing these features by end of Q2, the wedge isn't working — reassess whether the barrier is features or something else (pricing, brand, sales motion).

**Portfolio Balance Check:**

| Category | Count | % of investment | Target | Assessment |
|----------|:-----:|:---------------:|:------:|:----------:|
| Core (Platform Hardening) | 1 | 40% | 50-70% | 🟡 Below range — acceptable because the architecture is the prerequisite for everything else |
| Adjacent (Enterprise Wedge + Sales Motion) | 3 | 50% | 20-30% | 🟡 Above range — heavy enterprise bet. Acceptable if mid-market growth is self-sustaining. Risk: if mid-market slows, the strategy is doubly exposed. |
| Transformational | 1 | 10% | 5-15% | 🟢 Within range |

**Sequencing Rationale:**
Bet 1 (Platform Hardening) before Bet 2 (Enterprise Wedge Features) because enterprise features deployed on unreliable infrastructure will fail the enterprise buyer's POC — they'll see the feature checklist pass but the reliability evaluation fail. **Counterfactual:** If we shipped enterprise features first on current architecture, prospects would see the features but churn during POC when the platform drops below enterprise SLA thresholds. We'd burn the prospect relationship and have no second chance.

**NOT-Doing (2 of 4 shown):**

| Item | Category | Why not | What we lose | Reconsider if |
|------|----------|---------|-------------|---------------|
| Mobile app | Declined | Enterprise buyers evaluate on desktop. Mobile doesn't appear in any RFP. Sales has never lost a deal citing mobile. | Consumer-grade engagement metrics may suffer; some executive dashboard-glancing use cases unserved. | Mobile appears in >20% of enterprise RFPs in 2 consecutive quarters. |
| AI-powered insights | Deferred to FY28 | Requires the data infrastructure from Bet 1 to be complete. Building AI on unstable architecture creates technical debt and unreliable outputs. | Competitive differentiation gap vs. 2 competitors who shipped AI features this year. | Platform Hardening complete by Q2 AND a competitor's AI features start appearing in win/loss reasons. |

### What Changed
1. **Vision is falsifiable** — "500+ enterprise customers by FY28" with a specific failure test, vs. generic "become the leading platform"
2. **Bets have hypotheses and kill criteria** — each bet states what it assumes, how confident the team should be, and when to stop. The generic version has priorities with no stopping conditions.
3. **Sequencing is justified with counterfactuals** — "Platform before features because enterprise POCs will fail on unreliable infra" vs. implicit ordering by quarter.
4. **Portfolio balance is explicitly scored** — the skill flagged that 50% adjacent investment is above target range with a named risk (mid-market dependency). The generic version doesn't evaluate balance.
5. **NOT-Doing section names opportunity costs** — "Mobile declined because it's not in RFPs" with a reconsider-if trigger, vs. mobile not mentioned at all (leaving it ambiguous).
6. **Resource math is grounded** — 14 engineers x 2 quarters = specific capacity allocation, vs. "begin architecture rework" with no sizing.

---

## Use Case 2: Quarterly Pivot After a Failed Bet

*[To be completed with full before/after comparison]*

### Scenario
A product team shipped a major AI feature last quarter (Bet 2 from their annual plan). Usage data shows <5% adoption after 8 weeks. The quarterly gate criteria specified 20% adoption as the pass threshold. The PM needs to execute the kill decision, reallocate resources, and update the strategy — not pretend the bet is still working.

---

## Use Case 3: New Product Strategy (0-to-1)

*[To be completed with full before/after comparison]*

### Scenario
A platform company wants to launch a standalone product targeting a new market segment. The PM needs to build the initial strategy: vision, first 3 bets, sequencing for the first 2 quarters, and resource ask to present to leadership. No existing product, no existing customers, limited market data.
