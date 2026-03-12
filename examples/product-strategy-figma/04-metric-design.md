# Measurement Framework: Figma Product Strategy — Full-Stack Metric System

> **Date:** 2026-03-12 | **Confidence band:** M (40-70%) | **Staleness window:** 2026-09-12

---

## Executive Summary

Figma's core business challenge is not user acquisition but deepening collaborative value delivery across its expanding surface area (Design, FigJam, Dev Mode, Slides). The right metric to organize the company around is **Weekly Collaborative Editors** -- the count of unique users who edit a file that at least one other person also edited in the same trailing 7-day window. This metric captures the collaboration multiplier that separates Figma from single-player tools, predicts both retention and expansion revenue, and resists gaming because inflating it requires producing real multi-user editing activity. The decomposition tree breaks this into four L1 drivers: new team activation, cross-product adoption breadth, collaboration depth, and enterprise seat expansion. Two experiments are designed to validate the highest-leverage interventions: (1) a guided team onboarding flow to lift activation, and (2) a cross-product nudge to increase multi-surface usage. **The single most important metric to watch is the Week-4 collaborative retention rate by signup cohort -- if it degrades while topline growth holds, Figma is acquiring users who do not stick.**

---

## How to Read This Document

**What this is:** A measurement engineering system for Figma's product strategy -- not a KPI dashboard or a list of numbers. It defines what to measure, how each metric connects to business value, what happens when metrics are gamed, and how to detect problems before they hit revenue.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | Whether the measurement plan is sound and the key metric to watch |
| **15 min** | Executive Summary + Metric Hierarchy (section 2) + Experiment Plan (section 5) | What we measure, how we test, and the decision rules |
| **30 min** | Full document through Recommendations | Complete metric system with counter-metrics, retention design, and interventions |
| **Deep dive** | Everything including Appendix | Statistical design details, gaming detection, assumption stress-testing |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Summary | Metric Hierarchy, Review Cadence | Statistical design, Goodhart details |
| PM Lead | Executive Summary | Sections 1-5 (NSM through Experiments), Recommendations | MAB details, statistical validity formulas |
| Data Scientist | Full document in order | Statistical Validity (section 5), Retention Cohorts (section 8), Adversarial Self-Critique | Framework theory context |
| Engineering Lead | Executive Summary | Instrumentation Feasibility, Experiment Plan (duration/sample/unit) | Framework selection rationale |

---

## Notation Key

**Confidence levels** -- applied to every metric design conclusion:
- **H (>70% confident)** -- Validated in own data or strong structural evidence. Act on it.
- **M (40-70%)** -- Based on comparable products or reasonable inference. Validate before committing.
- **L (<40%)** -- Hypothesis only. Must be tested before treating as a metric target.

**Evidence tiers** -- how we know what we claim to know (tagged inline as T1-T6):
- **T1** -- Direct internal behavioral data (Figma's own analytics)
- **T2** -- Primary research on Figma's users (surveys, interviews)
- **T3** -- Expert analysis with methodology (Reforge, Lenny's, published case studies)
- **T4** -- Industry benchmarks (SaaS/PLG averages, public reports)
- **T5** -- Comparable product claims (competitor announcements, teardowns)
- **T6** -- First-principles reasoning (weakest -- treat as starting hypothesis)

**Recommendation format (O->I->R->C->W):**
- **O**bservation -- What the data shows (with evidence tier)
- **I**mplication -- Why it matters (the mechanism)
- **R**esponse -- What to do (specific action + owner + timeline)
- **C**onfidence -- How sure we are (H/M/L + key assumption)
- **W**atch -- How to know if we are wrong (observable signal)

**Flags:**
- `[POTENTIALLY STALE]` -- Benchmark data >6 months old; verify before using as a target
- `[EVIDENCE-LIMITED]` -- Recommendation based on T4-T6 only; validate with your own data before acting

---

## Step 0: Context Fitness Check

| Question | Answer | Implication |
|---|---|---|
| **Do we have access to Figma's usage data?** | No -- this is an external framework design | All targets are industry benchmarks (T4) or first-principles reasoning (T6). Flag: "Replace all targets with validated thresholds from Figma's own data before operationalizing." |
| **Has the product been live long enough for retention data?** | Yes -- Figma launched in 2016, 10 years of product history | Retention cohort *design* is valid; specific benchmark *values* must come from internal data |
| **New product or existing?** | Existing with expanding surface area (Design, FigJam, Dev Mode, Slides) | Focus on NSM, Goodhart countermeasures, retention cohorts, and experiment design |
| **Who will operationalize?** | Figma has a mature data team (100+ eng/data staff based on public job postings (T5)) | Full statistical depth is appropriate |

**Context gate result:** Proceed with full Measurement Framework. All metric targets below are benchmarks or hypotheses -- Figma's data team must replace them with validated internal thresholds.

---

## Step 0b: Framework Selection

| Question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| Full-stack metric system for multi-product collaborative platform | F1 NSM + Decomposition, F2 Leading/Lagging, F3 Counter-Metrics (Goodhart), F4 Experiment Design, F6 Retention Cohorts, F8 HEART | F9 PMF Assessment | F7 MAB -- single-hypothesis experiments are more appropriate for the recommended tests; F9 PMF -- Figma has established PMF in core design, PMF question is relevant only for newer surfaces (Slides, Dev Mode) |

---

## 1. Figma's Value Moment and North Star Metric

**Value moment:** The instant a second person edits a file that someone else is already working in. This is the moment Figma delivers value that no offline or single-player tool can replicate -- real-time multiplayer collaboration on a design artifact.

**NSM Candidate Evaluation:**

| Candidate NSM | Value Reflection | Leading Nature | Influenceability | Simplicity | Non-Gameability | Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Weekly Active Editors (WAE)** | Partial -- counts solo editors who get no collaboration value | Moderate -- leads revenue by 1-2 quarters (T4) | High -- onboarding, activation, feature work all move it | High -- "users who edited something this week" | Low -- bot accounts or trivial edits can inflate | 3/5 |
| **Design System Adoption Rate** | Low -- many Figma users get value without design systems | Low -- lagging indicator of mature team usage | Low -- requires organizational process change, not product change | Medium -- requires defining "adoption" precisely | Medium | 2/5 |
| **Weekly Collaborative Editors (WCE)** | High -- directly measures the collaboration moment | High -- collaborative usage predicts retention 2.3x better than solo usage in PLG tools (T3, Reforge) | High -- onboarding, sharing flows, team features all move it | High -- "users who edited a file someone else also edited this week" | High -- requires real multi-user activity to inflate | 5/5 |
| **Weekly Active Teams** | High -- captures team-level value | Medium -- team count can grow without deepening engagement | Medium -- harder to influence directly, depends on sales + organic | Medium -- requires defining "active" and "team" | Medium -- shell teams can inflate | 3/5 |

**Selected NSM: Weekly Collaborative Editors (WCE)**

Definition: Count of unique users who, in a trailing 7-day window, made at least one edit to a file that at least one other user also edited within the same window. "Edit" = any object creation, modification, or deletion event (excludes view-only, comment-only).

**Why WCE over WAE:** Weekly Active Editors counts solo users who may be getting value from Figma-as-a-drawing-tool, but Figma's moat and pricing power come from collaboration. WCE isolates the behavior that differentiates Figma from Sketch, Adobe XD, and Canva. A user who edits alone could switch to any tool; a user embedded in a collaborative workflow has switching costs proportional to the number of collaborators. [Confidence: H -- structural argument grounded in network-effect economics (T3, T6)]

**GSM validation:**
- **Goal:** Designers and their cross-functional collaborators create and iterate on design work together in real time
- **Signal:** Multiple users editing the same file within a 7-day window
- **Metric:** Weekly Collaborative Editors = unique users with >= 1 edit on a file also edited by >= 1 other user in trailing 7 days

---

## 2. Metric Decomposition Tree

| Level | Metric | Definition | Owner | Cadence | Target | Counter-Metric |
|---|---|---|---|---|---|---|
| **NSM** | Weekly Collaborative Editors (WCE) | Unique users editing files also edited by others, trailing 7d | CPO | Monthly | Baseline + 15% YoY (T6) | Collaboration quality score (edits-per-session for collaborative files) |
| **L1** | New Team Activation Rate | % of new teams (org signup) reaching >= 3 collaborative editors within 14 days | VP Growth | Weekly | >= 40% (T4, PLG benchmark) | Time-to-activate (must not exceed 10 days median) |
| **L1** | Cross-Product Breadth | % of WCE who used >= 2 Figma surfaces (Design, FigJam, Dev Mode, Slides) in trailing 28 days | VP Product | Weekly | >= 30% (T6) | Per-surface session depth (no surface drops below 2 sessions/week) |
| **L1** | Collaboration Depth | Avg unique collaborators per active editor, trailing 28 days | PM Core | Weekly | >= 3.5 collaborators (T6) | Editor satisfaction (in-product survey >= 4.0/5) |
| **L1** | Enterprise Seat Expansion Rate | Net new paid seats per existing enterprise account, trailing quarter | VP Enterprise | Monthly | >= 8% quarterly net expansion (T4, SaaS benchmark) | Seat utilization rate (active seats / paid seats >= 70%) |
| **L2** | Onboarding Completion Rate | % of new signups completing core onboarding (create file + invite 1 person) within 7 days | PM Growth | Daily | >= 55% (T4) | Support ticket rate from new users |
| **L2** | File Sharing Rate | % of files created that are shared with >= 1 other user within 48 hours | PM Collaboration | Daily | >= 45% (T6) | Unwanted share / spam report rate |
| **L2** | Dev Mode Adoption | % of teams with >= 1 developer inspecting a design file in trailing 14 days | PM Dev Mode | Weekly | >= 25% of Pro/Org teams (T6) | Designer satisfaction with dev handoff quality |
| **L2** | FigJam-to-Design Conversion | % of FigJam sessions that result in a linked Design file within 7 days | PM FigJam | Weekly | >= 15% (T6) | FigJam standalone usage (must not decline) |
| **Input** | Invite Funnel Conversion | % of "invite teammate" prompts that result in accepted invite | Eng Growth | Per-deploy | >= 30% (T4) | Invite fatigue (dismiss rate on invite prompts) |
| **Input** | Editor Load Time (P95) | 95th percentile time-to-interactive for collaborative files | Eng Performance | Per-deploy | <= 3 seconds (T6) | Error rate on file open (must stay < 0.5%) |
| **Input** | Real-time Sync Reliability | % of collaborative editing sessions with zero sync conflicts | Eng Infra | Per-deploy | >= 99.5% (T6) | Data loss incidents (zero tolerance) |

**Causal chain check:**
- Invite Funnel Conversion -> Onboarding Completion -> New Team Activation -> WCE (3 steps, valid)
- Editor Load Time -> Collaboration Depth -> WCE (2 steps, valid)
- Dev Mode Adoption -> Cross-Product Breadth -> WCE (2 steps, valid)
- FigJam-to-Design -> Cross-Product Breadth -> WCE (2 steps, valid)
- Seat Expansion -> WCE (1 step, valid -- more paid seats in collaborative orgs directly feeds WCE)

No broken branches identified.

---

## 3. Leading / Lagging Indicator Pairs

| Lagging Metric | Leading Indicator | Temporal Lag | Correlation (est.) | Causal? | Alert Threshold |
|---|---|---|---|---|---|
| Quarterly NRR (net revenue retention) | WCE growth rate | 8-12 weeks (T4) | r ~ 0.75 (T6, modeled from PLG NRR drivers) | Hypothesis -- validate with internal regression | WCE growth < 5% QoQ for 2 consecutive months |
| Enterprise churn | Collaboration Depth decline per account | 4-8 weeks (T4) | r ~ 0.65 (T6) | Hypothesis | Avg collaborators/editor drops below 2.5 for an account |
| Monthly revenue | New Team Activation Rate | 6-10 weeks (T4) | r ~ 0.70 (T6) | Hypothesis | Activation rate drops below 35% for 3 consecutive weeks |
| WCE (itself lagging vs. inputs) | Onboarding Completion Rate | 2-3 weeks (T6) | r ~ 0.60 (T6) | Hypothesis | Completion rate drops below 45% |

**Activation Metric (Aha Moment Protocol):**

1. **Aha moment hypothesis:** A new user who shares a file with at least 1 other person AND that person edits the file within 7 days of signup. This is the moment the user experiences Figma's multiplayer value.
2. **Correlation check:** [EVIDENCE-LIMITED] Estimated r ~ 0.55-0.70 between "shared file edited by invitee within 7 days" and 90-day retention, based on PLG activation benchmarks (T4). Figma's data team must validate with internal cohort analysis.
3. **Threshold:** Share >= 1 file AND receive >= 1 collaborator edit within 7 days of signup = "activated"
4. **Causal validation plan:** Run experiment (see Experiment 1 below) -- guided team onboarding that nudges file sharing. If treatment group shows higher 90-day retention AND higher sharing rate, the causal link is supported. If sharing increases but retention does not, the activation metric is correlational only and must be revised.

---

## 4. Counter-Metric Design and Goodhart Vulnerability

| Primary Metric | Most Likely Goodhart Variant | What Goes Wrong | Counter-Metric | Threshold | Gaming Detection Pattern |
|---|---|---|---|---|---|
| **WCE (NSM)** | Regressional | Teams create "collaboration theater" -- opening files in multiplayer without meaningful edits. Bots or scripts auto-edit files. | Meaningful edit rate: % of collaborative sessions with >= 3 substantive object changes per user | Meaningful edit rate must stay >= 60% (T6) | Spike in sessions with exactly 1 trivial edit per user; editor-seconds-per-session declining while WCE rises |
| **New Team Activation Rate** | Causal | Growth team optimizes invite prompts so aggressively that teams "activate" on paper but never return. Forced onboarding flows inflate completion without real engagement. | Day-30 team retention rate (% of activated teams with >= 2 active editors at day 30) | Must stay >= 50% of activation rate (T6) | Activation rate rising while day-30 team retention is flat or declining |
| **Cross-Product Breadth** | Extremal | Product surfaces add low-friction "try it" nudges that get a single click but no sustained usage. Users touch FigJam once and never return. | Per-surface repeat usage: % of users who return to a secondary surface within 14 days | Must stay >= 40% return rate per surface (T6) | Breadth % rising while per-surface D14 retention is flat |
| **Enterprise Seat Expansion** | Adversarial | Sales team bulk-provisions seats to hit expansion targets without verifying end-user need. IT admins add seats preemptively. | Seat utilization rate: monthly active seats / total paid seats | Must stay >= 70% (T4, SaaS benchmark) | Seat count rising while utilization rate declining; large batches of seats added with zero logins in first 30 days |
| **Collaboration Depth** | Extremal | Product forces collaboration (e.g., requiring approvals, mandatory reviews) that inflates collaborator count without real collaborative intent. | Voluntary collaboration rate: % of multi-editor sessions initiated without system prompts or required workflows | Must stay >= 80% of total collaborative sessions (T6) | Collaboration depth rising after a mandatory-review feature ships; NPS declining concurrently |

**Quarterly Health Review Protocol:**
- **Cadence:** Every 13 weeks
- **Owner:** Head of Data Science
- **Decision framework:** For each primary-counter pair: Keep (proxy-outcome r > 0.5 and counter-metric healthy) / Recalibrate (r 0.3-0.5 or counter at threshold) / Replace (r < 0.3 or counter-metric consistently violated)

---

## 5. Experiment Plan

### Experiment 1: Guided Team Onboarding Flow

| Field | Value |
|---|---|
| **Hypothesis** | If we replace the current individual onboarding with a guided team onboarding (prompt to invite 2 teammates + pre-populated shared file template), new team activation rate will improve by >= 8 percentage points within 14 days of signup |
| **Primary metric** | New Team Activation Rate (>= 3 collaborative editors within 14 days) |
| **Secondary metrics** | Day-30 team retention, invite acceptance rate, time-to-first-collaboration (Bonferroni-corrected at alpha = 0.0167 for 3 secondary metrics) |
| **Guardrail metrics** | Individual onboarding completion rate must not drop > 5pp; support ticket rate from new users must not increase > 20%; solo-user satisfaction must not decline |
| **MDE** | 8pp (from estimated ~40% baseline to 48%). Business rationale: 8pp activation improvement at Figma's scale (~500K new team signups/quarter, T5 estimate) = ~40K additional activated teams/quarter, each worth ~$2K-5K ARR at Pro/Org pricing (T5). This is material at Figma's ~$600M ARR (T5, 2024 estimate). |
| **Alpha / Power** | 0.05 / 0.80 |
| **Sample size** | ~2,400 new teams per arm (4,800 total). Calculation: for 8pp MDE from 40% baseline, two-proportion z-test, alpha=0.05, power=0.80 yields n ~ 2,376 per arm. At ~500K new team signups/quarter, this requires < 1 week of traffic. [EVIDENCE-LIMITED: baseline activation rate is estimated (T6); recalculate with real baseline.] |
| **Duration** | 28 days minimum. Rationale: primary metric window is 14 days, so we need at least 14 days of enrollment + 14 days of observation for the last enrollee. Adding buffer for weekly seasonality. |
| **Randomization unit** | Organization (not user) -- collaboration is a team-level treatment, randomizing at user level creates contamination within teams |
| **Exclusions** | Solo signups (no team/org context), existing teams adding members, enterprise accounts with custom onboarding |
| **Decision rule** | Ship if: activation rate improves >= 8pp AND all guardrails hold AND day-30 retention signal is non-negative. Do NOT ship if: activation improves but day-30 retention declines (this means we are creating "activation theater"). Inconclusive if: effect is 3-8pp -- extend experiment duration to achieve power for smaller MDE. |

**Experiment Quality Score:** 6/6 (pre-registered hypothesis, single primary metric, guardrails declared, duration committed, sample size computed, segmentation planned)

### Experiment 2: Cross-Product Discovery Nudge

| Field | Value |
|---|---|
| **Hypothesis** | If we show a contextual nudge to FigJam users who have never opened Figma Design (and vice versa) -- recommending a related workflow in the other surface -- cross-product breadth will increase by >= 5pp within 28 days |
| **Primary metric** | Cross-Product Breadth (% of WCE using >= 2 surfaces in trailing 28 days) |
| **Secondary metrics** | Per-surface D14 return rate, FigJam-to-Design conversion rate (Bonferroni-corrected at alpha = 0.025) |
| **Guardrail metrics** | Primary surface engagement (session count, session duration) must not decline > 3%; nudge dismiss rate must stay below 70%; in-product NPS must not decline |
| **MDE** | 5pp (from estimated ~25% baseline to 30%). Business rationale: broader surface usage correlates with lower churn in multi-product PLG companies (T3, Reforge multi-product playbook). Even a 5pp lift represents meaningful cross-sell and retention improvement. |
| **Alpha / Power** | 0.05 / 0.80 |
| **Sample size** | ~3,200 users per arm (6,400 total). Calculation: for 5pp MDE from 25% baseline, two-proportion z-test, alpha=0.05, power=0.80 yields n ~ 3,150 per arm. At Figma's scale (4M+ paid users reported in 2024 (T5)), this is trivially achievable within days. |
| **Duration** | 35 days. Rationale: primary metric uses a 28-day window; need 7 days enrollment + 28 days observation for last enrollee. |
| **Randomization unit** | User -- cross-product usage is an individual behavior; team-level contamination risk is low |
| **Exclusions** | Users already using 2+ surfaces (they are already cross-product); free-tier users with limited surface access; users in Experiment 1 (avoid interaction effects) |
| **Decision rule** | Ship if: breadth improves >= 5pp AND per-surface return rate holds AND guardrails hold. Do NOT ship if: breadth improves but primary surface engagement declines (user is distracted, not expanded). Consider targeted rollout if: effect varies significantly by user segment (designers vs. PMs vs. developers). |

**Experiment Quality Score:** 6/6

**"When NOT to Experiment" Check:**
- [x] Both changes are reversible (UI nudges can be turned off instantly)
- [x] Sufficient traffic -- sample sizes achievable within 1-2 weeks at Figma's scale
- [x] Ethical bar met -- neither treatment withholds core functionality

---

## 6. HEART Framework

| Dimension | Goal | Signal | Metric | Target | Counter-Metric |
|---|---|---|---|---|---|
| **Happiness** | Users feel Figma accelerates their design work | Positive sentiment in feedback, high NPS, low complaint volume | In-product NPS (quarterly survey) (T4) | >= 50 NPS for collaborative users (T4, PLG top-quartile benchmark) | Response rate (must stay >= 15% to avoid selection bias) |
| **Engagement** | Users collaborate frequently and deeply | Multiple editors per file, high edit frequency, cross-surface usage | WCE (NSM) + Collaboration Depth (L1) | See decomposition tree targets | See Goodhart countermeasures above |
| **Adoption** | New users and teams reach collaborative value quickly | Team activation within 14 days, file sharing within 7 days | New Team Activation Rate (L1) + File Sharing Rate (L2) | >= 40% activation, >= 45% sharing (T4/T6) | Time-to-activate must not exceed 10 days |
| **Retention** | Activated teams continue collaborating over time | Sustained collaborative editing beyond initial activation | Week-4 Collaborative Retention: % of activated teams with >= 2 collaborative editors at week 4 (T6) | >= 65% (T4, PLG benchmark for activated cohorts) [POTENTIALLY STALE] | Revenue retention (NRR) -- if logo retention holds but NRR declines, we are retaining small teams and losing large ones |
| **Task Success** | Core design tasks are completed efficiently in multiplayer | File completion, export/handoff events, design-to-dev transitions | Design-to-Dev Handoff Rate: % of design files with >= 1 Dev Mode inspection within 14 days of last design edit (T6) | >= 30% for teams with Dev Mode access (T6) | Handoff quality (developer satisfaction survey >= 3.5/5) |

---

## 7. PMF Assessment

**Status:** Skipped for Figma's core design product (PMF established -- $600M+ ARR (T5), dominant market position in collaborative design). Relevant only for newer surfaces:

| Surface | PMF Signal | Assessment |
|---|---|---|
| Figma Design | Established (T5) | >= 40% "very disappointed" estimated based on market dominance and switching cost evidence |
| FigJam | Moderate (T5) | Competing with Miro, Mural; unclear if standalone PMF exists or if value is Figma-ecosystem bundling |
| Dev Mode | Early (T5) | Launched 2023; adoption data insufficient for PMF assessment; design-to-dev handoff is validated need but Dev Mode vs. Zeplin/Storybook not yet settled |
| Figma Slides | Very early (T5) | Launched 2024; direct competition with Google Slides, Keynote, PowerPoint; PMF unvalidated |

**Recommendation:** Run Ellis Test surveys ("How would you feel if you could no longer use [surface]?") segmented by surface. If FigJam or Slides score below 25%, reconsider investment level or reposition as ecosystem feature rather than standalone product.

---

## 8. Retention Cohort Design

**Primary cohort type:** Behavior-based (activated vs. non-activated teams), cross-cut with time-based (monthly signup cohorts).

**Retention Windows:**

| Window | Definition | Benchmark | Degradation Threshold |
|---|---|---|---|
| Day 1 | >= 1 edit on day after signup | ~60% for collaborative tools (T4) [POTENTIALLY STALE] | > 5pp decline vs. prior 4-week rolling average |
| Day 7 | >= 1 edit in days 5-9 (flexible window to handle weekday patterns) | ~45% (T4) | > 5pp decline |
| Day 14 | >= 1 edit in days 12-16 | ~38% (T4) | > 4pp decline |
| Day 30 | >= 1 edit in days 26-34 | ~30% (T4) | > 3pp decline |
| Day 60 | >= 1 edit in days 55-65 | ~25% (T4) | > 3pp decline |
| Day 90 | >= 1 edit in days 85-95 | ~22% (T4, SaaS/PLG average) | > 2pp decline sustained over 2 cohorts |

`[EVIDENCE-LIMITED: All benchmarks above are SaaS/PLG industry averages (T4). Figma's actual retention is likely higher for collaborative users given strong network effects. Replace with internal data.]`

**Cohort Cuts:**

- **Time-based:** Monthly signup cohorts. Compare each month's curve to prior 3-month average. Alert if any window degrades beyond threshold for 2 consecutive cohorts.
- **Behavior-based (critical):**
  - *Activated teams (>= 3 collaborative editors in 14 days)* vs. *non-activated teams* -- validates the activation metric. Expected: activated cohort retains 2-3x better at day 90 (T3).
  - *Solo users who later become collaborative* vs. *always-solo users* -- measures conversion-to-collaboration value. If solo-to-collaborative users retain at near-activated-team rates, invest in solo-to-team conversion flows.
- **Channel-based:** Organic signups vs. paid acquisition vs. sales-led enterprise. Detect if paid channels bring users who activate but do not retain (acquisition quality problem).
- **Product-surface-based:** Users who adopt 1 surface vs. 2+ surfaces. Expected: multi-surface users retain significantly better (T6, based on multi-product PLG patterns from Atlassian, Notion (T3)).

**Retention Curve Shape Interpretation:**
- **Smile curve** (early drop, then recovery): Healthy for PLG -- users explore, some leave, committed users come back. Watch the trough depth.
- **Flat curve** (steady-state after initial drop): Strong PMF signal. The floor is the sustainable user base.
- **Frown curve** (continuous degradation): Danger signal. Either the activation metric is wrong, or the product is not delivering sustained value. Trigger immediate investigation.

**Revenue vs. Logo:** Track both. Figma's seat-based pricing means expansion revenue (existing accounts buying more seats) can mask logo churn (accounts leaving entirely). If NRR stays strong (> 120%) but logo retention degrades, Figma is concentrating into fewer, larger accounts -- a concentration risk.

---

## 9. Metric Intervention Recommendations (O->I->R->C->W Cascade)

**Intervention 1: Accelerate Team Activation Through Guided Onboarding**
- **Observation** [T4, T6]: PLG benchmarks suggest 40-60% of new teams fail to reach collaborative activation within 14 days. Figma's current onboarding focuses on individual file creation, not team collaboration setup.
- **Implication**: Every unactivated team is a missed compounding opportunity -- they never experience Figma's multiplayer value, making them indistinguishable from Sketch/Adobe XD users and highly susceptible to churn.
- **Response**: Ship Experiment 1 (guided team onboarding). Owner: PM Growth. Timeline: experiment launch within 4 weeks, results within 8 weeks.
- **Confidence**: M -- assumes activation rate is the binding constraint on WCE growth, not product capability gaps. If teams activate but do not retain, the problem is downstream.
- **Watch**: Day-30 team retention rate for experiment cohort. If activation improves >= 8pp but day-30 retention does not improve, the intervention is cosmetic.

**Intervention 2: Drive Cross-Product Breadth to Reduce Churn Risk**
- **Observation** [T3]: Reforge and Lenny's Newsletter data on multi-product PLG companies (Atlassian, Notion, Airtable) shows that users on 2+ products churn at 30-50% lower rates than single-product users.
- **Implication**: Figma has four surfaces but most users likely touch only one. Each additional surface creates switching cost and increases the collaboration surface area -- a direct contributor to WCE.
- **Response**: Ship Experiment 2 (cross-product nudge). Owner: PM Product. Timeline: experiment launch within 6 weeks. If successful, build a permanent cross-product recommendation engine.
- **Confidence**: M -- assumes cross-product usage is causal for retention, not just correlated with power-user behavior. The experiment is designed to test this.
- **Watch**: Per-surface D14 return rate. If breadth increases but users bounce off secondary surfaces quickly, the nudge is driving low-quality trials.

**Intervention 3: Instrument Enterprise Seat Utilization Monitoring**
- **Observation** [T4]: Industry data shows 20-40% of enterprise SaaS seats are underutilized (Zylo 2024 SaaS Management Report). [POTENTIALLY STALE]
- **Implication**: If Figma's enterprise seat utilization is below 70%, expansion revenue is built on shelfware -- a procurement risk at renewal. CIOs increasingly audit seat utilization, and low-utilization seats are first to be cut in cost-reduction cycles.
- **Response**: Build a seat utilization dashboard visible to enterprise account teams. Flag accounts below 60% utilization for proactive outreach. Owner: VP Enterprise + Data team. Timeline: dashboard within 8 weeks.
- **Confidence**: H -- enterprise seat utilization is a well-documented retention risk across SaaS. The only question is magnitude for Figma specifically.
- **Watch**: Quarterly NRR for flagged-low-utilization accounts vs. healthy-utilization accounts. If NRR divergence exceeds 20pp, utilization monitoring is validated as a churn predictor.

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---|---|---|---|
| **WCE growth vs. solo-user value** | NSM framework says optimize for collaborative editors -- solo users are outside the NSM | HEART Adoption says Figma should lower barriers for all users, including solo users who may convert to collaborative later | Weight NSM: solo users matter only as a pipeline to collaborative users. Track solo-to-collaborative conversion rate as an L2 metric, but do not optimize solo experience at the expense of collaboration features. If solo-user count grows but WCE is flat, it is not success. |
| **Activation speed vs. activation quality** | Leading/Lagging framework says faster activation predicts better retention | Goodhart analysis says optimizing activation speed can create "activation theater" -- teams hit the threshold but do not truly collaborate | Weight Goodhart: pair activation rate with day-30 retention. If activation rate rises but day-30 retention does not follow within 2 cohort cycles, recalibrate the activation definition (e.g., increase the threshold from 3 collaborative editors to 5, or add a minimum edit depth requirement). |
| **Cross-product breadth vs. product focus** | Metric decomposition says breadth reduces churn | Retention cohort analysis may show that single-surface power users retain better than shallow multi-surface users | This is an empirical question that Experiment 2 will answer. If per-surface depth metrics degrade when breadth increases, the nudge strategy is wrong -- Figma should deepen single-surface mastery instead of broadening. Watch the counter-metric. |

---

## Instrumentation Feasibility

| Metric | Data exists? | Clean and reliable? | Timely (within cadence)? | >= 30 days history? | Status |
|---|:---:|:---:|:---:|:---:|---|
| Weekly Collaborative Editors (WCE) | Likely (T6) -- Figma tracks editing events | Unknown -- "collaborative" requires join logic across users | Requires batch job (acceptable for weekly cadence) | Yes (product is 10 years old) | Needs definition work -- agree on exact edit event taxonomy and collaboration window |
| New Team Activation Rate | Likely | Unknown -- depends on team/org entity modeling in analytics | Daily batch feasible | Yes | Needs work -- define "team" entity consistently across free/Pro/Org/Enterprise |
| Cross-Product Breadth | Likely -- surface usage is trackable | Likely clean -- surface boundaries are clear | Weekly batch feasible | Partial -- Slides launched 2024, Dev Mode 2023 | Ready for Design + FigJam; short history for Slides |
| Collaboration Depth | Likely | Unknown -- counting "unique collaborators per editor" requires sessionization | Weekly batch feasible | Yes | Needs definition work on sessionization and collaborator attribution |
| Enterprise Seat Expansion | Yes -- billing data | Yes -- billing is clean by necessity | Monthly cadence matches billing cycle | Yes | Ready |
| Meaningful Edit Rate (counter-metric) | Unknown -- depends on edit event granularity | Unknown | Needs investigation | Unknown | Blocked -- requires edit event taxonomy that distinguishes substantive from trivial edits |
| In-product NPS | Depends on existing survey infrastructure | Varies by survey implementation | Quarterly | Possibly | Needs work if not already instrumented |

---

## Review Cadence and Ownership

| Metric Level | Review Cadence | Owner | Escalation Trigger |
|---|---|---|---|
| NSM (WCE) | Monthly exec review | CPO | > 10% decline sustained 2 consecutive months |
| L1 metrics | Weekly product review | VP of each area | Misses target 3 consecutive weeks |
| L2 metrics | Daily team standup | Feature PM | Alert threshold crossed (defined per metric above) |
| Experiments | Per-experiment readout | PM + Data Science | Guardrail violated at any point during experiment |
| Counter-metrics | Bi-weekly audit | Head of Data Science | Any counter-metric crosses threshold for 2 consecutive periods |
| Quarterly health review | Every 13 weeks | Head of Data Science + CPO | Any proxy-outcome r < 0.5; any assumption registry item invalidated |

---

## Assumption Registry

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | Collaborative usage (multi-editor files) is the primary driver of Figma's retention and expansion, not solo design capability | NSM selection, entire decomposition tree | H | Network effects in PLG tools are well-documented (T3); Figma's pricing scales with seats, directly linking collaboration to revenue (T5) | Internal data showing solo-user retention >= collaborative-user retention. If solo users retain equally well, WCE is the wrong NSM -- revert to WAE. |
| 2 | Team activation within 14 days predicts long-term retention | L1 activation metric, Experiment 1 | M | PLG activation benchmarks suggest 7-14 day windows are standard (T4); no Figma-specific validation | Cohort analysis showing no retention difference between teams activated at day 14 vs. day 30. If the window does not matter, the activation metric needs a different definition. |
| 3 | Cross-product surface usage (Design + FigJam + Dev Mode + Slides) increases switching costs and reduces churn | L1 breadth metric, Experiment 2 | M | Multi-product PLG churn reduction documented at Atlassian, Notion (T3) | Experiment 2 showing breadth increase without retention improvement. Alternatively: Figma surfaces may not be complementary enough (FigJam competes with Miro, not with Figma Design). |
| 4 | Enterprise seat utilization below 70% is a leading churn indicator | L1 expansion metric, Intervention 3 | H | Zylo SaaS Management data (T4); standard enterprise procurement behavior | Figma-specific data showing low-utilization accounts renew at equal rates. Possible if Figma is "must-have" infrastructure where CIOs do not audit seats. |
| 5 | Figma's scale (~4M+ paid users, ~$600M ARR) makes all proposed experiments statistically feasible within 1-4 weeks | Experiment design (both experiments) | M | Public reporting and estimates (T5) | If Figma's new-team signup rate is significantly lower than estimated, Experiment 1 may require 4-8 weeks of enrollment. Recalculate sample size with real baseline. |

---

## Adversarial Self-Critique

**Weakness 1: No internal data means all targets are hypotheses.**
This entire framework is built on industry benchmarks (T4) and first-principles reasoning (T6). Not a single target in the decomposition tree is validated against Figma's actual data. The 40% activation target, the 65% retention target, the >= 3.5 collaborators depth target -- all are educated guesses. A Figma data scientist could look at this document and correctly say: "Your targets are directionally right but numerically wrong by 10-20pp in either direction." **Mitigation:** Every target is explicitly tagged with evidence tier. The first operational step is to replace all T4/T6 targets with T1 baselines from Figma's own analytics. The framework structure (which metrics to track, how they connect, what to pair them with) is the durable value; the specific numbers are placeholders.

**Weakness 2: WCE may penalize Figma's solo-user growth engine.**
By selecting Weekly Collaborative Editors as the NSM, we implicitly deprioritize solo designers -- freelancers, students, hobbyists -- who use Figma as an individual design tool. This is a large and growing user base (Figma's free tier is a massive funnel). If solo users are a significant revenue pipeline (free -> Pro conversions), optimizing WCE could lead to underinvestment in the solo experience. **Watch indicator:** Solo-to-paid conversion rate. If it declines after WCE becomes the organizational rallying metric, add "Solo User Activation Rate" as a separate L1 metric.

**Weakness 3: Collaboration Depth is hard to instrument and easy to miscount.**
"Average unique collaborators per active editor" sounds clean but is analytically messy. Does a commenter count as a collaborator? Does viewing (without editing) count? If someone opens a file, makes one cursor movement, and leaves -- are they a collaborator? The definition will be debated, and different definitions will produce wildly different numbers. **Watch indicator:** If the data team takes more than 4 weeks to agree on the Collaboration Depth definition, simplify to "files with >= 2 editors" (binary) rather than counting unique collaborators (continuous). Precision is less important than consistency and speed of instrumentation.

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| WCE-to-revenue correlation drops below r = 0.5 | NSM selection -- WCE may no longer predict business outcomes | Next quarterly review |
| Activation metric does not predict day-90 retention (r < 0.3) | Activation definition, "aha moment" hypothesis | Immediate investigation; redesign activation experiment |
| Any assumption registry item invalidated | Dependent framework sections (see registry) | Within 1 week |
| Retention curve shape changes from flat/smile to frown for 2+ consecutive cohorts | PMF assessment for affected surface; cohort design | Immediate escalation to CPO |
| Counter-metric threshold crossed 2+ consecutive periods | Primary metric gaming detection; review whether primary metric definition needs tightening | Immediate investigation |
| Figma launches a new product surface (e.g., Figma AI as standalone) | Cross-Product Breadth definition, decomposition tree | Add new surface within 2 weeks of launch |
| Competitor (Canva, Adobe) ships real-time collaboration at parity | WCE may no longer be differentiating; reassess NSM to focus on depth/quality rather than participation | Strategic review within 1 month |

---

## Sources

| Source | Evidence Tier | Date | Used for |
|---|---|---|---|
| Reforge Growth Series -- multi-product PLG playbook | T3 | 2024-2025 | Cross-product breadth impact on churn |
| Lenny's Newsletter -- activation metric benchmarks | T3-T4 | 2024-2025 | PLG activation rate norms |
| Zylo SaaS Management Report | T4 | 2024 | Enterprise seat utilization benchmarks [POTENTIALLY STALE] |
| Figma public announcements (Config 2024, blog posts) | T5 | 2024 | User count estimates, product surface launches, ARR estimates |
| Google HEART framework (Rodden, Hutchinson, Fu) | T3 | 2010 (foundational) | HEART dimension structure |
| Goodhart's Law -- Manheim & Garrabrant taxonomy | T3 | 2018 (foundational) | Four-variant counter-metric design |
| SaaS PLG benchmarks (OpenView, Bessemer) | T4 | 2024-2025 | Retention windows, NRR norms |
| First-principles reasoning | T6 | 2026-03-12 | Where no external data available |
