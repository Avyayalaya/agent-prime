# Problem Definition Document: Figma's Strategic Position — Prosumer Erosion and Enterprise Lock-In

> **Date:** 2026-03-12 | **Confidence band:** M (40-70%) | **Staleness window:** 2026-09-12

---

## Executive Summary

Figma faces a two-front strategic problem. From below, Canva is pulling non-designer users out of Figma's prosumer tier with a simpler, cheaper tool that handles 80% of visual production tasks. From above, Adobe is leveraging enterprise procurement relationships and Creative Cloud bundling to lock design teams into a stack where Figma becomes optional. Figma's growth rate has decelerated from ~40% YoY (2022) to an estimated ~20% YoY (2025), and its $12.5B valuation must be justified by either expanding TAM or defending current share. The compounding risk: if Canva captures the "good enough" segment and Adobe captures enterprise, Figma's core — professional collaborative design — becomes a shrinking middle. **The recommended next step is a structured competitive analysis of Figma's defensible core, followed by discovery research into which user segments are actively considering alternatives.**

---

## How to Read This Document

**What this is:** A problem definition — not a solution proposal, not a strategy deck, not a brief. It answers "What exactly is Figma's strategic challenge and how big is it?" with evidence-graded confidence. It is the upstream artifact that feeds Competitive Analysis, Discovery Research, and Metric Design.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | The two-front problem, who's affected, and the recommended next step |
| **15 min** | Executive Summary + Problem Statement + Opportunity Sizing | The structured problem definition with TAM/SAM/SOM quantification |
| **30 min** | Full document through Recommendations | Complete decomposition with root cause, JTBD, constraints, and prioritization |
| **Deep dive** | Everything including Assumption Registry and Self-Critique | Full framework applications, load-bearing assumptions, and honest weaknesses |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Summary | Opportunity Sizing (section 5), Recommendations (section 10) | Root cause deep dive, JTBD consumption chain |
| PM Lead | Executive Summary | Problem Statement (section 1), Constraint Map (section 7), Prioritization (section 9) | Individual framework methodology notes |
| Researcher / Designer | Full document in order | Root Cause (section 3), JTBD Framing (section 4), Stakeholder Matrix (section 8) | Financial sizing details |
| Engineer | Executive Summary | Constraint Map (section 7), Problem Statement (section 1) | Stakeholder analysis, prioritization methodology |

---

## Notation Key

**Confidence levels** — applied to every conclusion:
- **H (>70% confident)** — Strong evidence supports this. Act on it.
- **M (40-70%)** — Direction is probable but evidence is mixed. Validate before committing.
- **L (<40%)** — Hypothesis, not finding. Do not act without further evidence.

**Evidence tiers** — how we know what we claim to know (tagged inline as T1-T6):
- **T1** — Direct behavioral data: usage analytics, churn data, revenue metrics
- **T2** — Primary user research: structured interviews, usability observations
- **T3** — Expert analysis with disclosed methodology: analyst reports, UX audits
- **T4** — Market/industry reports: Gartner, Forrester, industry surveys
- **T5** — Stakeholder assertions: internal claims, executive opinions, press statements
- **T6** — Assumptions/inference: first-principles reasoning, analogies from other domains

**Problem severity ratings:**
- **Critical** — Users cannot accomplish their goal; abandon or churn
- **Major** — Users accomplish the goal but with significant friction or workaround
- **Minor** — Annoyance that does not change behavior or outcomes

**Recommendation format (O->I->R->C->W):**
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

| Question | Answer | Implication |
|---|---|---|
| **Is the problem space genuinely unclear or contested?** | Yes. Figma's leadership faces competing narratives: "Canva is not a real threat" vs. "Canva is eating our bottom" and "Adobe partnership vs. Adobe competition." | Proceed with full problem framing. |
| **Do we have access to user behavioral data (T1) or primary research (T2)?** | No. This analysis is built from public filings, press, analyst reports, and inference (T3-T6). | Flag prominently: all problem severity claims are capped at M confidence. This is a hypothesis document until validated with internal data. |
| **Is the requester asking for a problem definition or already asking for a solution?** | Problem definition. The new PM lead needs the landscape before prescribing strategy. | Proceed normally. |
| **Are multiple stakeholders involved with potentially different views?** | Yes. Design team leads, product managers, sales (enterprise), and executive leadership each see different facets. | Stakeholder Impact Matrix is load-bearing. |
| **Is there time pressure to ship something immediately?** | No. This is a strategic framing exercise, not a fire drill. | Full version with all applicable frameworks. |

**`[EVIDENCE-LIMITED: This entire document is built from T3-T6 evidence. All problem statements are hypotheses. Validate with internal usage data (T1) and user research (T2) before committing to solutions.]`**

---

## Step 0b: Framework Selection

This is a "full problem definition" scenario — new PM lead, starting from scratch, needs the complete picture. All frameworks apply, tiered by relevance.

| Question type | Primary frameworks (full depth) | Supporting frameworks (scan depth) |
|---|---|---|
| Full strategic problem definition | F1 Problem Definition Canvas, F2 5 Whys, F3 JTBD Problem Framing, F4 Opportunity Sizing | F6 Constraint Map, F8 ICE/RICE Prioritization |

F5 Problem-Solution Fit is deferred — this document defines the problem; fit assessment comes after discovery. F7 Stakeholder Impact Matrix is applied at scan depth since we lack internal org data.

---

## 1. Problem Statement

**One-sentence problem statement:** Figma's product leadership faces simultaneous market erosion from below (Canva capturing prosumer/non-designer segments with simpler, cheaper tools) and lock-in pressure from above (Adobe leveraging enterprise procurement bundling), which together compress Figma's addressable core and threaten its ~20% YoY growth trajectory.

**Confidence:** M | **Evidence basis:** T3 (analyst estimates), T4 (market reports), T5 (press statements), T6 (inference)

**Problem type:** Existing problem worsening — Figma has been aware of both vectors since the failed Adobe acquisition (2022-2023), but the competitive dynamics have intensified.

---

## 2. Figma's Two-Front Problem Is Really a Middle-Market Squeeze

*Problem Definition Canvas — the foundational decomposition that forces seven questions most problem statements skip. Each cell is independently evidence-graded.*

| Dimension | Finding | Evidence | Confidence |
|---|---|---|---|
| **Who has this problem?** | Figma as a company, but specifically: (a) the prosumer/small-team segment losing users to Canva, and (b) enterprise design teams facing Adobe bundling pressure during procurement renewal cycles | (T4: Canva 200M+ monthly users vs. Figma ~4M as of late 2024; T5: Adobe Enterprise press) | M |
| **What are they trying to do?** | Maintain growth rate and justify $12.5B valuation by expanding design collaboration TAM, while defending existing segments from category-adjacent competitors | (T4: Figma's last known ARR ~$600M in 2023; T6: valuation math requires ~30% growth) | M |
| **What do they do today?** | Figma competes on collaboration UX and developer handoff (Figma-to-code). Canva competes on accessibility and template breadth. Adobe competes on enterprise bundling and end-to-end creative suite | (T3: product feature comparison; T5: company positioning statements) | H |
| **Why is that painful?** | Figma's differentiator (real-time multiplayer design) is now table stakes — Canva added it, Adobe added it. The moat has shifted from "collaboration" to "workflow integration" — a game Adobe plays better at enterprise scale | (T3: feature parity analysis; T6: platform dynamics inference) | M |
| **What triggers the pain?** | Enterprise procurement renewal cycles (annual), when Adobe offers Creative Cloud + Figma-equivalent at bundled pricing. For prosumers: the moment a non-designer needs to create marketing assets and discovers Canva does it in 5 minutes vs. Figma's steeper learning curve | (T6: procurement cycle inference; T4: Canva's ease-of-use positioning in market surveys) | L |
| **What does "good" look like?** | Figma owns a category that neither Canva nor Adobe can replicate — likely "design system infrastructure" or "product development workflow" rather than "visual design tool" | (T6: strategic inference from platform theory) | L |
| **How do they know it's solved?** | Net revenue retention >130%, prosumer-to-enterprise conversion rate increasing, and Canva churn-to-Figma rate stable or growing | (T6: metric inference; no internal data available) | L |

**Canvas assessment:** 0 cells at T1-T2, 3 cells at T3-T4, 4 cells at T5-T6. This is a **hypothesis-stage** canvas. Broad research needed before commitment. The "Who" and "What they do today" cells are reasonably grounded; the trigger, desired state, and verification cells are inference-heavy.

---

## 3. Figma's Growth Plateau Is a Category Definition Problem, Not a Product Problem

*5 Whys root cause analysis — Christensen's disruption framework applied: the surface symptom (slowing growth) peels back to a structural category question.*

**Presented problem:** "Figma's growth is decelerating and competitors are gaining ground."
**Root problem:** Figma defined its category as "collaborative design tool" — a category that is now contested from both ends and may not be defensible.

| Layer | Why? | Evidence | Tier |
|---|---|---|---|
| Surface symptom | Figma's YoY revenue growth has decelerated from ~40% (2022) to ~20% (2025 est.) | Analyst estimates, press reporting on post-Adobe-deal trajectory | T4 |
| Why 1 | New user acquisition in the prosumer segment is slowing — Canva captures the "I just need to make something" user before they ever consider Figma | Canva's growth to 200M+ MAU; Figma's ~4M MAU suggests the non-designer market chose Canva decisively | T4 |
| Why 2 | Figma's product complexity is calibrated for professional designers, which creates a floor on ease-of-use that repels casual users — but casual users are 10x the market | Product complexity comparison: Figma requires learning auto-layout, components, variants; Canva requires choosing a template | T3 |
| Why 3 | Figma built its moat around real-time collaboration for design teams, but "collaboration" is now a feature (every tool has it), not a category | Canva, Adobe XD, Sketch all added multiplayer; Google Docs-style collaboration is commodity infrastructure | T3 |
| Why 4 | The underlying category — "design tool" — is bifurcating into "visual production" (where Canva wins on volume) and "design systems infrastructure" (where Figma could win on depth) | Figma's Dev Mode, Variables, and design token features signal a bet on the infrastructure layer; Canva's AI features signal a bet on production automation | T6 |
| Why 5 (root) | Figma has not yet decisively chosen and communicated which category it owns. It is still positioned as "the collaborative design tool" — a category that is being squeezed from both directions. The root cause is category ambiguity, not product deficiency | Strategic inference from platform competition patterns; Figma's messaging still leads with "design" not "product development infrastructure" | T6 |

**Divergence check:** The presented problem (growth slowing) implies "get more users" or "defend against competitors." The root cause analysis says the problem is not competitive tactics but category strategy. If Figma defines a new category that Canva cannot enter (too shallow) and Adobe cannot bundle (too integrated), the tactical competitive problem dissolves. This is a critical reframe that will surprise stakeholders expecting a feature-by-feature competitive response.

**`[EVIDENCE-LIMITED: Why 4 and Why 5 rest entirely on T6 inference. The category bifurcation hypothesis needs validation through user research (T2) and internal usage data (T1) before it should drive strategic decisions.]`**

---

## 4. Users Hire Figma and Canva for Fundamentally Different Jobs

*Christensen's Jobs-to-be-Done framework applied at the problem level — understanding what functional, emotional, and social jobs users hire each tool for reveals the real competitive boundary.*

| Job Dimension | Figma Users | Canva Users | Gap |
|---|---|---|---|
| **Functional job** | "Design a coherent product interface with reusable components that my engineering team can implement precisely" (T3) | "Create a professional-looking visual asset in under 10 minutes without design training" (T3) | Different jobs. Overlap only in marketing collateral for small teams. |
| **Emotional job** | "Feel like a craftsperson — precise control, pixel-perfect output, professional tooling" (T6) | "Feel empowered — I don't need to wait for a designer or learn complex software" (T6) | Figma's emotional job requires expertise to unlock; Canva's requires none. |
| **Social job** | "Be seen as a serious design professional using industry-standard tools" (T6) | "Be seen as resourceful and self-sufficient — I made this myself" (T6) | Non-overlapping social signals. A designer using Canva loses status; a marketer using Figma gains nothing. |

**Consumption chain analysis:**

| Phase | Figma User | Canva User | Strategic Implication |
|---|---|---|---|
| Before (trigger) | Design sprint kicks off; PM writes requirements; designer opens Figma to create screens | Manager says "we need a social post by Friday"; non-designer opens Canva | Figma's trigger is workflow-embedded; Canva's is ad hoc. Different activation patterns. |
| During (active use) | Multi-hour sessions; component creation; design system maintenance; developer handoff setup | 5-30 minute sessions; template selection; brand kit application; export | Session depth differs 10x. Figma's engagement is deep and sticky; Canva's is shallow and frequent. |
| After (outcome) | Design specs in Dev Mode; design system tokens updated; stakeholder review in FigJam | PNG/PDF exported; posted to social/email; forgotten | Figma's output feeds a pipeline; Canva's output is terminal. |

**Competing "hires" for each job:**

| Job | Figma competes with | Canva competes with |
|---|---|---|
| Product interface design | Sketch (declining), Adobe XD (deprecated), Framer (rising), code-first tools (T3) | PowerPoint, Google Slides, freelance designers on Fiverr, doing nothing (T3) |
| Design system management | Code-based token systems (Style Dictionary), internal component libraries (T3) | N/A — Canva users don't manage design systems |
| Quick visual production | Canva, Adobe Express (T3) | Adobe Express, VistaCreate, free online editors, asking a designer (T3) |

**Critical insight:** Figma and Canva are not competing for the same job in most use cases. The strategic threat is not that Canva steals Figma's designers — it is that Canva captures the non-designer majority before Figma can expand into that segment. The ~200M vs. ~4M MAU gap is a job-market-size gap, not a product-quality gap.

---

## 5. The Market Is Large Enough to Justify Strategic Investment

*Opportunity sizing across TAM/SAM/SOM — quantifying how big the problem space is, not just the pain.*

| Dimension | Estimate | Evidence | Confidence |
|---|---|---|---|
| **TAM — Global design and visual creation tools** | ~$25-30B by 2027. Includes professional design, casual visual production, prototyping, and design systems | (T4: Grand View Research, Mordor Intelligence market sizing reports) `[POTENTIALLY STALE — based on 2024 projections]` | M |
| **SAM — Professional design collaboration + prosumer visual tools** | ~$10-12B. Figma's addressable slice: product design teams, UI/UX, design systems, plus adjacent prosumer creation | (T4: derived from design software market reports minus print/video/3D) | M |
| **SOM — Figma's realistic capture** | ~$2-4B ARR by 2028. Assumes Figma holds professional design (~60% share in UI/UX) and captures 5-10% of prosumer visual production through FigJam and simplified flows | (T6: inference from current ~$600M ARR, growth trajectory, and segment penetration estimates) | L |

**Problem-level opportunity scoring (1-5 scale):**

| Problem Area | Frequency | Severity | Breadth | Willingness | Score |
|---|---|---|---|---|---|
| Prosumer erosion to Canva | 4 — Daily (non-designers create content daily) (T4) | 3 — Major friction (Figma is too complex for casual use) (T3) | 4 — 25-50% of potential Figma users are non-designers who default to Canva (T6) | 3 — Would try if Figma offered a simpler mode (T6) | **144** |
| Enterprise lock-in by Adobe | 2 — Annual (procurement cycles) (T6) | 4 — Risk of forced migration away from Figma (T5) | 2 — 5-10% of enterprise accounts face active Adobe bundling pressure (T6) | 4 — Enterprise teams would switch tools if procurement mandates it (T6) | **64** |
| Category definition ambiguity | 5 — Constant (affects every positioning decision) (T6) | 3 — Major (unclear positioning bleeds into product, marketing, sales) (T6) | 5 — Affects entire company (T6) | 2 — Awareness of problem is low; most teams don't see it as a problem (T6) | **150** |

**Interpretation:** Category definition (150) and prosumer erosion (144) score highest. Enterprise lock-in (64) is significant but lower-frequency. The category problem compounds both tactical problems — if Figma picks the right category, prosumer defense and enterprise positioning become clearer.

---

## 6. Problem-Solution Fit Assessment

*Before any solution work begins — is this a real problem worth solving?*

| Test | Question | Finding | Verdict |
|---|---|---|---|
| **Existence test** | Do real users actually face these competitive pressures? | Canva's 200M+ MAU vs. Figma's ~4M confirms the prosumer gap exists. Adobe's enterprise bundling is documented in procurement press. (T4, T5) | PASS |
| **Severity test** | Is the problem painful enough to change behavior? | For prosumers: they never adopted Figma in the first place — the pain is Figma's (missed market), not the user's. For enterprise: forced migration is Critical severity. (T6) | PASS (enterprise) / UNVALIDATED (prosumer) |
| **Frequency test** | Does it occur often enough to justify investment? | Prosumer visual creation is daily. Enterprise procurement is annual but high-stakes. Category ambiguity is constant. (T4, T6) | PASS |
| **Willingness test** | Would users change behavior if Figma addressed this? | Unknown. Non-designers may not want a "simpler Figma" — they may want Canva. Enterprise teams may not have choice. (T6) | UNVALIDATED |
| **Solvability test** | Can Figma solve this within its constraints? | Category redefinition is within Figma's control. Prosumer simplification requires significant product investment. Enterprise defense requires sales/partnerships. (T6) | PASS (with caveats) |
| **Timing test** | Why now? | AI is reshaping both markets simultaneously. Canva's AI features (Magic Design) threaten to leapfrog traditional design workflows. Adobe's Firefly integration makes Creative Cloud stickier. The window for Figma to define its AI-era category is 12-18 months. (T4, T5) | PASS |

**Decision:** 2 UNVALIDATED tests (willingness, prosumer severity). This problem framing is a hypothesis document. Design research to validate willingness and severity before committing to strategic responses.

---

## 7. What Figma Can and Cannot Change

*Constraint map — verified limitations that bound the solution space. Constraints compound: platform + pricing + brand together define Figma's strategic corridor.*

| Constraint Type | Constraint | Impact on Solution Space | Negotiable? | Source |
|---|---|---|---|---|
| **Technical — Platform architecture** | Figma is browser-first, built on WebGL/WASM. This enables collaboration but limits performance on complex files vs. native apps | Eliminates solutions requiring GPU-native performance (e.g., competing with After Effects). Reinforces web-first collaboration advantage | N | (T3: product architecture) |
| **Business — Pricing model** | Figma charges per-editor-seat ($12-75/month). Canva charges per-user ($0-13/month). Adobe bundles at $55-80/month for full Creative Cloud | Figma cannot win a price war with Canva's freemium at scale. Must justify premium through workflow value, not tool access | Partially | (T1: published pricing) |
| **Business — Valuation pressure** | $12.5B valuation post-Adobe-deal-collapse requires sustained high growth. Cannot accept margin-diluting strategies that slow revenue growth | Constrains low-price prosumer plays; favors enterprise upsell and platform expansion | N | (T4: funding reports) |
| **Brand — Designer identity** | Figma's brand is built on professional design credibility. A "Canva-like" simplified mode risks alienating core users who chose Figma because it is not Canva | Constrains how far Figma can simplify without brand damage. Multi-product strategy (Figma + FigJam + new product) may be safer than simplifying core Figma | Partially | (T6: brand theory) |
| **Organizational — Team DNA** | Figma was built by and for designers and developers. Pivoting to serve non-designers requires hiring, culture shift, and new research competencies | Limits speed of prosumer expansion. Expect 12-18 month lag for org capability build | Partially | (T6: organizational inference) |
| **Market — AI timing** | AI-generated design is advancing rapidly. Within 2 years, text-to-UI and text-to-layout tools may commoditize the production layer of design | If AI commoditizes production, Figma's value shifts entirely to the system layer (design tokens, components, governance). Accelerates the category decision | N | (T4: AI industry reports, T5: company announcements) |

**Constraint interaction:** Valuation pressure + pricing model + brand identity = Figma cannot go down-market cheaply. The compound constraint forces an up-market or platform strategy. This is the single most important constraint interaction — it eliminates "build a simpler cheaper Figma" as a viable response.

---

## 8. Stakeholder Impact Matrix

*Applied at scan depth — we lack internal org data, so power/interest scores are inferred.*

| Stakeholder | Problem Impact | Power (1-5) | Interest (1-5) | Current Position | Action Needed |
|---|---|---|---|---|---|
| Figma CEO / executive team | Growth deceleration directly affects valuation, fundraising, and IPO timeline | 5 (T6) | 5 (T6) | Champion — aware of strategic challenge | Align on category definition before tactical responses |
| Design team leads (customers) | Risk of forced tool migration if Adobe bundling wins at their company | 3 (T6) | 4 (T6) | Supporter — prefer Figma, worried about procurement | Arm with ROI data to defend Figma in procurement conversations |
| Non-designer users (potential) | Currently not Figma users; hired Canva instead | 1 (T6) | 1 (T6) | Unaware — don't know Figma exists for their use case | Research needed: would they use Figma if it were simpler? |
| Enterprise procurement / IT | Control tool purchasing decisions; Adobe has existing relationship | 4 (T6) | 2 (T6) | Neutral to Resistant — Adobe is the default vendor | Enterprise sales strategy must engage procurement directly, not just designers |
| Figma product + engineering | Must execute whatever strategic direction is chosen | 3 (T6) | 4 (T6) | Supporter — but needs clarity on whether to build for designers or expand audience | Category decision is a prerequisite for product roadmap alignment |

---

## 9. Three Problems Ranked by Impact and Tractability

*ICE/RICE prioritization across the three identified problem areas.*

| Problem | Impact (1-5) | Confidence (1-5) | Ease (1-5) | ICE Score | Rank |
|---|---|---|---|---|---|
| **Category definition ambiguity** — Figma has not chosen between "design tool" and "product development infrastructure" | 5 (T6: affects all downstream decisions) | 3 (T6: hypothesis-stage, needs validation) | 3 (T6: requires exec alignment, not engineering) | **45** | **1** |
| **Prosumer erosion to Canva** — Non-designers default to Canva, shrinking Figma's growth ceiling | 4 (T4: 200M vs 4M MAU gap is real) | 3 (T6: unclear if Figma can/should compete here) | 2 (T6: requires new product, new audience, new capabilities) | **24** | **2** |
| **Enterprise lock-in by Adobe** — Adobe bundling Creative Cloud to force procurement decisions | 3 (T5: documented but limited breadth) | 2 (T6: actual enterprise churn data unavailable) | 2 (T6: requires sales investment, partnership strategy) | **12** | **3** |

**Prioritization rationale:** Category definition scores highest because it is the upstream decision that shapes the response to both tactical problems. If Figma defines itself as "product development infrastructure," the prosumer erosion becomes a feature (Canva handles visual production; Figma handles system design). If Figma defines itself as "design for everyone," the prosumer erosion becomes a crisis requiring a Canva-competitive product. The category decision must come first.

---

## 10. Recommendations (O->I->R->C->W Cascade)

**Recommendation 1: Resolve category definition before tactical competitive response**
- **Observation** [T6]: Figma's positioning ("collaborative design tool") is contested from both ends. Every tactical move (pricing, features, partnerships) depends on whether Figma is a design tool or a product development platform.
- **Implication**: Without category clarity, product investment is scattered — some features serve designers, some serve non-designers, some serve developers, and none decisively wins a category.
- **Response**: PM lead commissions a 4-week category definition sprint. Deliverables: (1) internal usage data analysis showing which user segments drive retention and expansion revenue, (2) 15-20 user interviews across designer, non-designer, and developer segments, (3) a one-page category definition with explicit "we are / we are not" boundaries. Owner: new PM lead. Timeline: 4 weeks.
- **Confidence**: M — assumes internal data will reveal a clear cluster, which may not be the case.
- **Watch**: If internal data shows revenue is evenly split across segments with no clear cluster, the category decision is harder. Escalate to CEO for a values-based (not data-based) decision.

**Recommendation 2: Validate prosumer erosion severity with actual switching data**
- **Observation** [T4]: The 200M vs. 4M MAU gap between Canva and Figma is dramatic but may be misleading — these may be fundamentally different user populations hiring for different jobs.
- **Implication**: If prosumer users were never going to use Figma (different job), "erosion" is a misnomer and Figma should not invest in a simpler product. If prosumer users tried Figma and left for Canva, it is a real product problem.
- **Response**: Analyze Figma's signup-to-activation funnel for non-designer personas. Key question: what percentage of Figma signups come from non-designers, and what is their 30-day retention vs. designer signups? Owner: data/analytics team. Timeline: 2 weeks.
- **Confidence**: M — assumes Figma has persona-level funnel data, which may not be segmented this way.
- **Watch**: If <5% of signups are non-designers, the "prosumer erosion" narrative is wrong — they were never Figma's market. Redirect investment to core designer experience.

**Recommendation 3: Build enterprise defense playbook against Adobe bundling**
- **Observation** [T5]: Adobe's enterprise motion leverages existing procurement relationships. When Creative Cloud renewals include "Figma-equivalent" features, procurement teams default to the bundle.
- **Implication**: Figma's enterprise defense is not a product problem — it is a sales and procurement problem. The best product in the world loses to "it's already in our contract."
- **Response**: Sales team develops a procurement defense kit: (1) ROI calculator showing Figma's collaboration value vs. Adobe XD, (2) case studies from enterprise design teams that successfully defended Figma in procurement, (3) direct procurement engagement playbook. Owner: enterprise sales lead. Timeline: 6 weeks.
- **Confidence**: L — assumes Adobe is actively bundling an XD replacement, which may have slowed after Adobe deprecated XD.
- **Watch**: If Adobe launches a direct Figma competitor (not just XD revival) with aggressive enterprise bundling, escalate to P0. If Adobe continues to deprioritize design tools, downgrade this problem.

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution |
|---|---|---|---|
| Problem severity vs. scope | 5 Whys: root cause is category ambiguity (an internal strategic problem, not a user problem) | Problem Definition Canvas: users face real competitive pressure from Canva and Adobe | Both are true at different levels. The user-level pain is real but the company-level response depends on the category decision. Solve the category question first, then address user-level pain within the chosen frame. |
| JTBD vs. Opportunity Sizing | JTBD: Figma and Canva serve fundamentally different jobs — they are not direct competitors | Opportunity Sizing: the prosumer market (Canva's territory) is 10x larger than professional design (Figma's territory) | The tension is real. Figma can accept a smaller TAM with higher ARPU (professional design infrastructure) or chase a larger TAM with lower ARPU (visual creation for everyone). The JTBD analysis suggests the former is more defensible; the Opportunity Sizing suggests the latter is more valuable. This is the core strategic trade-off. |
| Constraint Map vs. Prosumer opportunity | Constraints: valuation pressure + brand identity + pricing model make going down-market very difficult | Opportunity Sizing: prosumer erosion scores 144/625 — a significant problem | The constraint analysis says Figma probably cannot compete with Canva on Canva's terms. The opportunity sizing says the market is too big to ignore. Resolution: Figma needs to find a way to capture prosumer value without competing on Canva's terms — possibly through AI-assisted design that is simpler than Figma but more structured than Canva. This is a hypothesis, not a recommendation. |

---

## Assumption Registry

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | Figma's growth has decelerated to ~20% YoY | All — the entire problem framing assumes growth pressure | M | (T4: analyst estimates; no confirmed public revenue data post-2023) | If Figma's actual growth is >30% YoY, the urgency of this problem framing decreases substantially. The two-front squeeze may be a narrative, not a reality. |
| 2 | Canva and Figma serve fundamentally different jobs for most users | JTBD framing, Opportunity Sizing, Prioritization | M | (T3: product comparison; T6: job-level inference) | If Figma's internal data shows significant user overlap (users who actively use both tools for the same tasks), the JTBD separation is wrong and the competitive threat is more direct. |
| 3 | Adobe is actively pursuing enterprise bundling that threatens Figma | Constraint Map, Enterprise lock-in problem, Recommendation 3 | L | (T5: press reports; Adobe deprecated XD in late 2024) | If Adobe has effectively exited the UI design space (post-XD deprecation), the enterprise lock-in threat is overstated. Figma's enterprise challenge becomes retention and expansion, not competitive defense. |
| 4 | AI will commoditize the visual production layer of design within 2-3 years | Constraint Map (AI timing), Category definition urgency | M | (T4: AI industry reports; T5: Canva Magic Design, Adobe Firefly announcements) | If AI-generated design remains low-quality or niche, the production layer retains value and Figma's current positioning (professional design tool) remains defensible without category redefinition. |
| 5 | Figma's browser-first architecture is a constraint, not just an advantage | Constraint Map (technical) | H | (T3: product architecture is public and well-documented) | If browser performance improvements (WebGPU) close the gap with native apps, this constraint weakens. Figma's architecture becomes pure advantage. |

---

## Adversarial Self-Critique

**Weakness 1: The "two-front squeeze" may be a narrative, not a data-backed reality**

This entire document is built on the premise that Figma faces simultaneous pressure from Canva and Adobe. But the evidence is thin. Canva's 200M MAU and Figma's 4M MAU may simply reflect different markets — like comparing Microsoft Word's user count to Final Cut Pro's. They were never the same market. Adobe deprecated XD, which could mean the enterprise bundling threat is receding, not growing. A new PM lead who acts on this framing without internal data validation may over-invest in competitive defense when the real opportunity is deepening the core product for existing users. The strongest counter-argument: Figma's growth deceleration could be normal SaaS maturation (law of large numbers), not competitive pressure.

**Weakness 2: Category definition framing may be premature — Figma might not need to choose**

The root cause analysis concludes that Figma must define its category. But many successful companies occupy ambiguous categories for years. Salesforce was "CRM" and "platform" and "AI" simultaneously. Figma could continue as "collaborative design tool" while building platform capabilities and never formally declare a new category. The insistence on a category decision may create false urgency and force a premature commitment that closes off optionality. The counter-argument to this critique: Figma's internal teams need category clarity to make daily product decisions, even if the external positioning remains broad.

**Weakness 3: This analysis has zero T1-T2 evidence and should be treated as a hypothesis map, not a strategic input**

Every conclusion in this document is built from analyst reports (T4), press statements (T5), and inference (T6). No user behavioral data. No primary research. No internal metrics. A problem definition document without T1-T2 evidence is, by definition, speculation with structure. The risk is that the structure creates false confidence — a PM lead might present these frameworks as findings rather than hypotheses. The notation flags this repeatedly, but the structural formality of the document may override the epistemic warnings. This document should generate research questions, not strategy decisions.

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| Figma publishes revenue data (IPO filing, press) | All opportunity sizing; growth deceleration assumption | Monitor quarterly |
| Adobe launches a new design collaboration product | Enterprise lock-in section; upgrade to P0 | Within 1 week of announcement |
| Canva launches design system / developer handoff features | JTBD separation assumption; prosumer erosion section | Within 2 weeks of launch |
| Figma announces category-defining product (e.g., "Figma for product teams") | Category ambiguity root cause — may be resolved | Immediate re-assessment |
| AI-generated UI tools reach production quality | AI timing constraint; entire category framing | Monitor quarterly |

---

## Sources

1. Canva user count (~200M+ MAU) — Canva company announcements, 2024 (T5) `[POTENTIALLY STALE]`
2. Figma user count (~4M) — analyst estimates and press reports, late 2024 (T4) `[POTENTIALLY STALE]`
3. Figma ARR (~$600M) — reporting from 2023 funding round (T4) `[POTENTIALLY STALE]`
4. Figma $12.5B valuation — post-Adobe deal collapse, 2024 funding (T4)
5. Adobe XD deprecation — Adobe announcement, late 2024 (T5)
6. Design software market size ($25-30B by 2027) — Grand View Research, Mordor Intelligence (T4) `[POTENTIALLY STALE]`
7. Figma pricing ($12-75/seat/month) — Figma.com published pricing (T1)
8. Canva pricing ($0-13/user/month) — Canva.com published pricing (T1)
9. Adobe Creative Cloud pricing ($55-80/month) — Adobe.com published pricing (T1)
10. Canva Magic Design, Adobe Firefly — company announcements, 2024-2025 (T5)
11. Platform competition theory — Aggregation Theory (Ben Thompson), platform economics literature (T6)
