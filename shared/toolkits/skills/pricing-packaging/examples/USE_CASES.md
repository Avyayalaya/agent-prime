# Pricing & Packaging — Use Cases

> Three real-world pricing scenarios demonstrating the skill's framework application depth. Each shows a before (generic AI output) vs. after (skill-powered output) comparison.

---

## Use Case 1: AI Code Review Tool — New Product Pricing

**Scenario:** CodeLens AI, an AI-powered code review tool for mid-market engineering teams, needs initial pricing and package tiers for GA launch. Competitors: GitHub Copilot ($19/seat/month), Sourcery ($15/seat/month), CodeRabbit ($15-39/seat/month). Marginal cost per user: ~$8/month (GPU inference).

**Before (Generic AI, ~250 words):**
> "For CodeLens AI, I'd recommend pricing between $15-25/month per seat, which is competitive with GitHub Copilot and CodeRabbit. Consider offering a free tier to drive adoption, a Pro tier around $20/month, and an Enterprise tier at $40-50/month. The free tier should include basic features, Pro should include all features, and Enterprise should add admin and security. You might also consider usage-based pricing since AI inference has variable costs. Make sure to monitor competitor pricing and adjust accordingly."

**After (Skill-Powered, ~500 words):**
> **Model Selection:** Per-seat with usage guardrails selected over pure usage-based (developer buyers expect predictable costs) and pure freemium ($8/user marginal cost makes unlimited free tier uneconomical at scale) (H).
>
> **WTP Assessment:** 18 beta user interviews (T3) reveal mid-market engineering leads value review cycle time reduction at $20-35/seat/month. Floor: $18 (below which quality perception suffers). Sweet spot: $22-28. Ceiling: $38 (above which they evaluate Copilot's broader scope as better value). `[WTP range is M confidence — T3 data with n=18; recommend Van Westendorp study at n=100+ before price lock]`.
>
> **Package Architecture:** Free (5 reviews/week, 3 languages) -> Pro $24/seat/mo (200 reviews/week, all languages, team dashboard, Jira integration) -> Enterprise $49/seat/mo (unlimited, SSO, SAML, audit log, custom rules, dedicated support). Free tier's 5-review cap calibrated to $2/user/month cost (economically sustainable for acquisition). Pro's 200/week covers P95 usage (T1: beta analytics show median 40, P95 at 180).
>
> **Sensitivity:** At $24, margin is $16/seat (67%) — sufficient for CAC recovery in 8 months. At $19 (competitor parity), margin drops to $11/seat (58%) — CAC recovery extends to 13 months, borderline for mid-market SaaS. Revenue maximizes at lower prices (volume) but margin maximizes at $24+ (unit economics). The $24 price is the margin-optimized choice (M).
>
> **Recommendation (O->I->R->C->W):** Mid-market WTP sweet spot of $22-28 [T3] with $8 marginal cost -> per-seat with usage cap is the only model that balances buyer predictability with margin protection -> launch Pro at $24/seat/month with 6-month intro rate of $19 for beta converts -> Confidence M (assumes competitive pricing stable; if Copilot drops below $15/seat, our value premium erodes) -> Watch: Copilot pricing page, quarterly; CodeRabbit Series A announcement (may trigger price war).

**What Changed:**
- Model selection is a structural decision with rejected alternatives, not an afterthought
- WTP is grounded in T3 evidence with explicit sample size, method, and confidence band
- Package tiers have feature allocation rationale tied to usage data and cost economics
- Sensitivity analysis reveals margin-vs-revenue trade-off (uncommon knowledge)
- Recommendation uses O->I->R->C->W cascade with specific watch indicators

---

## Use Case 2: SaaS Platform — Price Increase on Existing Customers

**Scenario:** DataVault, a mid-market data analytics platform with 2,400 paying customers at $35/seat/month (Pro tier), wants to raise prices 25% to $44/seat/month. NPS is 42. Primary competitor Looker charges $60/seat/month. Annual churn rate is 8%.

*[Full use case to be developed after skill benchmarking]*

---

## Use Case 3: AI Writing Assistant — Freemium Packaging Redesign

**Scenario:** ProseAI, a consumer/prosumer AI writing assistant with 500K free users and 12K paid users ($12/month), has a 2.4% conversion rate. The free tier includes 50 AI generations/day. Leadership wants to redesign packaging to improve conversion without killing acquisition.

*[Full use case to be developed after skill benchmarking]*

---

*Created: 2026-03-12 | PM Skills Arsenal*
