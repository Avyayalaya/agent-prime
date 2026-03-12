# Use Cases: Discovery & Research

## Use Case 1: The Say/Do Gap -- Users Love a Feature They Never Touch

### Scenario

A PM at a B2B analytics platform (DataPulse) just finished 15 user interviews for a discovery sprint on their "Insights Dashboard" feature. In every interview, users praised the dashboard as "really valuable" and "one of the main reasons I chose DataPulse." But the PM also pulled 90-day behavioral data and discovered that only 11% of users visit the Insights Dashboard more than once per month -- and the median session duration on that page is 8 seconds. The PM needs to decide whether to double down on the Insights Dashboard in the Q3 roadmap or redirect investment elsewhere.

### The Prompt

> We ran 15 user interviews for our analytics platform (DataPulse). All 15 users said the Insights Dashboard is highly valuable and a key reason they chose our product. But our behavioral data shows only 11% of users visit the dashboard more than once a month, and median session time is 8 seconds. We also have NPS data (n=520, score 42), 62 support tickets mentioning "insights" or "dashboard" over the past 90 days, and a Mixpanel funnel showing where users go after landing on the dashboard. Should we invest more in the Insights Dashboard for Q3?

### Without the Skill (Generic AI)

This is an interesting contradiction in your data. Here's how I'd think about it:

**What the interviews suggest:** Users clearly value the Insights Dashboard conceptually. All 15 interviewees mentioned it positively, which is a strong qualitative signal. The dashboard seems to be part of your product's brand promise and value proposition.

**What the behavioral data shows:** Usage is low -- only 11% visit more than once monthly, and 8-second sessions suggest users aren't engaging deeply. This could mean the dashboard isn't delivering on its promise, or users may get what they need in a quick glance.

**Possible explanations:**
- The dashboard may need better content or personalization to drive engagement
- Users might value knowing the dashboard exists (a safety net) even if they rarely use it
- The 8-second session could indicate users get what they need quickly (a good thing) or that they bounce immediately (a bad thing)
- There may be a discoverability issue -- users forget it's there between visits

**Recommendations:**
- Dig deeper into the 11% who do visit regularly -- what's different about them?
- Consider A/B testing dashboard improvements before a full rebuild
- Look at the support tickets for clues about what users expect vs. what they find
- Consider whether the dashboard's value is more about perception (marketing) than daily utility

**On the NPS score:** 42 is decent for B2B but not exceptional. It would be worth segmenting NPS by dashboard usage to see if there's a correlation.

Overall, I'd recommend investigating further before committing Q3 resources. The gap between stated value and actual usage is worth understanding before making a big bet either way.

### With the Skill

**Source Inventory & Quality Assessment:**

| Source | Type | Sample | Tier | Recency | Key Bias Risk |
|---|---|---|---|---|---|
| User interviews (n=15) | Qualitative | Active enterprise users, self-selected | T2 | Current | Social desirability bias: users praise features to a company interviewer. Survivorship: all 15 are active users -- churned users absent. |
| Mixpanel behavioral data | Behavioral | N=4,800 MAU, full population | T1 | 90-day window | Survivorship: users who churned before the 90-day window are absent. Shows what, not why. |
| NPS survey (n=520) | Quantitative | 520 respondents, unknown response rate | T3 | Current | Response bias: satisfied users likely over-represented. No behavioral context attached. |
| Support tickets (n=62) | Anecdotal | Self-selected (users with problems) | T5 | 90 days | Extreme negativity bias: support tickets capture failure, not satisfaction. |

**Key Findings (Evidence-Graded):**

**Finding 1: The Insights Dashboard has a massive stated-vs.-revealed preference gap (H)**
- **Classification:** CONTRADICTED
- **Evidence:** Interviews: 15/15 users praised the dashboard as "valuable" (T2, but stated preference under social desirability pressure). Behavioral data: 11% monthly revisit rate, 8-second median session duration (T1). Mixpanel funnel: 74% of users who land on the dashboard navigate away within one click to the raw data explorer (T1).
- **Resolution:** Behavioral data (T1) overrides stated preference (T2) per the evidence hierarchy. Users say the dashboard is valuable; their behavior says they do not use it. The 8-second session + immediate navigation to raw data explorer indicates bounce, not quick-glance-satisfaction. The dashboard is not meeting the user's actual job-to-be-done.
- **Implication:** The Insights Dashboard is a perceived-value feature (it looks good in demos and evaluations) but not a use-value feature (it does not serve the daily workflow). Doubling down on it will increase demo win rates but will not improve retention or engagement.

**Finding 2: Users want data they can act on, not pre-built summaries (M)**
- **Classification:** EMERGING
- **Evidence:** Mixpanel funnel: 74% navigate from Insights Dashboard to raw data explorer (T1). Support tickets: 38/62 dashboard-related tickets request "custom views" or "ability to drill down" -- not more pre-built insights (T5, but pattern across 38 tickets upgrades directional confidence). Interviews: when pressed on HOW they use the dashboard, 9/15 described checking a specific number and then switching to raw data for the actual decision (T2).
- **Implication:** The underlying need is not "better insights" but "faster path to actionable data." The dashboard is an obstacle between users and the data they actually use. Investment should target data explorer enhancements and custom view creation, not more dashboard widgets.

**Stated vs. Revealed Preference Analysis:**

| What Users SAY | What Users DO | Gap | Implication |
|---|---|---|---|
| "The Insights Dashboard is one of the main reasons I chose DataPulse" (T2, 15/15 interviews) | 11% monthly revisit; 8-second sessions; 74% immediately navigate to raw data explorer (T1) | Extreme: universal praise, near-zero engagement | The dashboard is a purchase driver but not a usage driver. This is a marketing/positioning asset, not a product investment priority. Invest in demo experience; do not invest in daily workflow improvements for a feature users do not use daily. |
| "I check the dashboard to see if anything changed" (T2, 9/15 interviews) | Median 8-second session; no interaction events beyond page load (T1) | Moderate: users describe a "glance" behavior that behavioral data confirms is real but trivially brief | The "check" behavior is real but does not require a full dashboard. A notification or digest email could serve this job-to-be-done at lower cost and higher engagement. |

**Research Gap Map:**

| Gap | Type | Decision It Blocks | Priority | Recommended Action | Timeline |
|---|---|---|---|---|---|
| No churned user data | Blind spot | Whether dashboard quality contributed to churn | CRITICAL | 8 churned user interviews focused on "what did you stop using first?" | 2 weeks |
| No segmentation of the 11% who DO revisit | Thin evidence | Whether to serve power users vs. mainstream | HIGH | Cohort analysis: who are the repeat visitors? Segment by role, company size, plan tier | 1 week |

**Recommendation (O->I->R->C->W):**
- **Observation** [T1 + T2]: The Insights Dashboard has universal stated approval and near-zero actual usage. 74% of users who reach it immediately leave for the raw data explorer.
- **Implication**: The dashboard serves a purchase-decision job (it looks impressive in evaluation) but not a daily-workflow job (users need raw, actionable data, not pre-built summaries). Investing in dashboard improvements will not move retention or engagement metrics.
- **Response**: Redirect Q3 investment from Insights Dashboard to data explorer enhancements (custom views, saved filters, drill-down from summary metrics). PM Lead owns; 8-week delivery for custom views. Separately, add a weekly digest email that serves the "quick glance" job-to-be-done without requiring a dashboard visit.
- **Confidence**: M -- assumes the 74% navigation-to-raw-data pattern reflects genuine preference, not poor dashboard UX. If a redesigned dashboard were tested and the navigation pattern persisted, confidence upgrades to H.
- **Watch**: If dashboard engagement increases >25% after data explorer improvements (indicating users were using the dashboard as a waypoint, not avoiding it), re-assess. Also watch: demo win rate. If removing dashboard emphasis from demos reduces conversion, the purchase-driver hypothesis is confirmed and the dashboard warrants investment as a sales tool, not a user tool.

### What Changed

- **Evidence grading exposed the say/do gap:** Generic AI noted the contradiction but treated interviews and behavioral data as equal inputs requiring further investigation. The skill applied the evidence hierarchy (T1 behavioral > T2 stated preference) and reached a definitive resolution: behavioral data wins, the dashboard is not serving a real workflow need.
- **Stated vs. revealed preference framework produced a specific product insight:** The skill distinguished between a purchase-driver (demos/evaluation) and a usage-driver (daily workflow), leading to a precise recommendation: invest in the data explorer, not the dashboard. Generic AI recommended "investigating further."
- **Triangulation across 4 sources created a coherent picture:** Support ticket patterns (T5), funnel data (T1), interview probing (T2), and NPS (T3) were each graded independently and then converged. The skill identified that even within interviews, users' described behavior (check one number, leave) contradicted their stated praise.
- **Research gaps were named and prioritized:** The skill identified two specific gaps (churned users, 11% power-user segmentation) with methods and timelines. Generic AI mentioned "dig deeper" without specifying what to dig into.
- **O->I->R->C->W cascade turned the finding into a decision:** The recommendation includes a specific action (data explorer custom views), owner (PM Lead), timeline (8 weeks), key assumption (navigation pattern = preference, not poor UX), and a watch indicator (monitor dashboard engagement post-change). Generic AI recommended "A/B testing" without specifying what to test or what outcome to measure.

---

## Use Case 2: Conflicting Signals -- NPS Is High but Churn Is Rising

### Scenario

A PM at a project management SaaS (FlowBoard) is getting contradictory signals. The latest NPS survey (n=480) came back at 58 -- the highest score in company history. But the finance team just flagged that 90-day net revenue retention dropped from 97% to 91% over the same period. The PM also has quarterly business reviews from the CS team noting that 3 enterprise accounts churned citing "doesn't fit our workflow anymore," plus 8 recent user interviews from a roadmap discovery sprint that were broadly positive. Leadership is confused: if users are this happy, why are they leaving?

### The Prompt

> Our NPS just hit 58 (highest ever, n=480) but our 90-day net revenue retention dropped from 97% to 91%. CS flagged 3 enterprise churns in the quarter -- they cited "doesn't fit our workflow anymore." We also have 8 recent user interviews that were mostly positive, product analytics for the quarter, and a segment-level retention breakdown. What is actually going on? Is our product healthy or not?

### Without the Skill (Generic AI)

This is a classic case of conflicting metrics, and it's more common than you might think. Here's a framework for thinking about it:

**Why NPS can be high while churn rises:**

1. **Survivorship bias in NPS**: Your NPS survey only reaches current users. The users who churned aren't in the survey. If the unhappy users leave and only satisfied users remain, NPS goes UP as churn goes UP -- they're measuring different populations.

2. **Segment-level dynamics**: The 3 enterprise churns may represent a small number of accounts but a disproportionate revenue share. NPS is per-user, but revenue retention is per-dollar. A few large accounts leaving can tank NRR while NPS stays high.

3. **Workflow evolution**: "Doesn't fit our workflow anymore" suggests these customers' needs evolved beyond your product, not that your product got worse. This is natural in a maturing market.

4. **Response bias**: Users who bother to respond to NPS surveys tend to be either very happy or very unhappy. If unhappy users churn before responding, the survey skews positive.

**What I'd recommend:**

- Segment NPS by account size and tenure to see if there's a hidden unhappy cohort
- Interview the 3 churned enterprise accounts in depth to understand what "workflow" changes drove the decision
- Look at product usage data for accounts that eventually churn -- is there a leading indicator (declining login frequency, feature abandonment)?
- Compare your NPS response rate to typical B2B benchmarks (30-40%). If your rate is low, the sample may not be representative
- Build a churn prediction model using behavioral signals rather than relying on NPS as a health metric

The good news: NPS at 58 suggests your core user base is genuinely satisfied. The bad news: satisfaction doesn't prevent churn when the underlying need changes. Focus on understanding the churned accounts and whether they represent a growing segment.

### With the Skill

**Source Inventory & Quality Assessment:**

| Source | Type | Sample | Tier | Recency | Key Bias Risk |
|---|---|---|---|---|---|
| NPS survey (n=480) | Quantitative | Current users only; 32% response rate | T3 | This quarter | **Critical bias: survivorship.** Churned users are absent from the sample. NPS measures the satisfaction of users who stayed, not the health of the user base. At 32% response, the 68% non-respondents are invisible. |
| Revenue retention data | Behavioral | Full customer base, dollar-weighted | T1 | 90-day rolling | Complete population coverage including churned accounts. Dollar-weighting means enterprise churn has outsized impact. |
| CS quarterly business reviews | Anecdotal | 3 churned enterprise accounts | T5 | This quarter | n=3 is anecdotal. However, these are direct churn reasons from the accounts themselves -- rare and high-value signal despite small n. CS may soften or reframe churn reasons. |
| User interviews (n=8) | Qualitative | Current users, roadmap discovery | T2 | This quarter | Survivorship: all 8 are current, active users recruited for roadmap input. Interview guide was forward-looking ("what should we build?"), not diagnostic ("what's broken?"). Positive framing biases toward positive responses. |
| Product analytics | Behavioral | Full user base | T1 | This quarter | Complete population. Can segment by churned-before-churn vs. retained cohorts. |
| Segment-level retention breakdown | Behavioral | Full customer base | T1 | This quarter | Reveals which segments are churning -- the most actionable data source available. |

**Key Findings (Evidence-Graded):**

**Finding 1: NPS and retention are measuring different populations -- the contradiction is an artifact, not a paradox (H)**
- **Classification:** VALIDATED
- **Confidence:** H
- **Evidence:** NPS sample = current users only (T3, confirmed by survey methodology). Revenue retention = full customer base including churned accounts (T1). Segment-level retention breakdown shows enterprise segment retention dropped to 84% while SMB retention held at 96% (T1). NPS respondent profile: 78% SMB, 22% enterprise (T1 from survey metadata) -- enterprise users are under-represented in the NPS sample relative to their revenue contribution.
- **Detail:** NPS is rising because the users who would have given low scores already left. The remaining population is genuinely more satisfied, but the base is shrinking. The NPS score is accurate for who it measures; it is misleading as a proxy for business health because it excludes the most important signal -- departing customers.
- **Implication:** NPS cannot be used as a health metric without adjusting for survivorship. The product is healthy for SMB users and deteriorating for enterprise users. These are two different products wearing one brand.

**Finding 2: Enterprise churn is a segment-specific structural problem, not random account loss (H)**
- **Classification:** EMERGING (upgrading to VALIDATED pending confirmation)
- **Confidence:** M -- evidence is strong directionally but the churn sample (n=3 interviews) is too small to confirm the mechanism
- **Evidence:** Segment retention: enterprise at 84% vs. SMB at 96% (T1). CS notes: all 3 churned accounts cited "workflow" mismatch -- specifically, they had adopted a cross-functional project methodology that FlowBoard's task-centric model doesn't support (T5, but consistent across all 3). Product analytics: enterprise accounts that churned showed a 60% decline in "board creation" activity in the 60 days before cancellation, while their "integration API calls" increased 3x -- suggesting they were migrating data out (T1).
- **Detail:** The 3 enterprise churns are not random. They share a pattern: cross-functional workflow needs that FlowBoard's task-board architecture cannot serve. The behavioral pre-churn signature (declining core usage + increasing API/export activity) is detectable in analytics and may be present in other at-risk enterprise accounts.
- **Implication:** This is structural (a durable architecture mismatch), not weather (a temporary dissatisfaction). Enterprise accounts are outgrowing FlowBoard's mental model. Without architectural investment, enterprise churn will accelerate as more accounts adopt cross-functional methodologies.

**Finding 3: The 8 positive user interviews are survivorship-biased and did not ask diagnostic questions (M)**
- **Classification:** EMERGING
- **Confidence:** M
- **Evidence:** Interview sample: 8 current, active users recruited for a roadmap discovery sprint (T2, but sample excludes churned/at-risk users). Interview guide: forward-looking questions ("what should we build next?") rather than diagnostic ("what's not working?") (T6: methodology assessment). No enterprise churned or at-risk accounts were included.
- **Detail:** The interviews accurately reflect the experience of retained, engaged users. They are not evidence of product health. The positive signal is real for SMB users; it is silent on the enterprise problem because no enterprise-at-risk users were interviewed.

**Cross-Source Contradictions:**

| Contradiction | Source A Says | Source B Says | Resolution |
|---|---|---|---|
| Product health | NPS at 58: highest ever (T3, current users only) | Revenue retention dropped from 97% to 91% (T1, full base) | **T1 wins.** NPS measures a shrinking, increasingly self-selected happy population. Revenue retention measures the full business reality. The product is healthy for its retained SMB base and failing its enterprise segment. Do not cite NPS as evidence of health without the survivorship caveat. |
| User satisfaction | 8 interviews: broadly positive (T2, current users) | 3 enterprise churns: "doesn't fit our workflow" (T5, churned users) | **Churned user signal outweighs retained user interviews for diagnosing churn.** Retained users are satisfied by definition (they stayed). The diagnostic signal is in the departing accounts. Despite T5 evidence tier (n=3), the churn interviews are more relevant to the retention question than the 8 positive interviews. |

**Signal vs. Noise Assessment:**

| Signal Candidate | Frequency | Behavioral Corroboration | Structural? | Verdict |
|---|---|---|---|---|
| "Workflow mismatch" (enterprise churn reason) | 3/3 churned accounts (T5) | Pre-churn behavioral signature: declining core usage + increasing export/API activity visible in analytics (T1) | Structural: reflects architecture limitation, not fixable with incremental features | **SIGNAL** -- investigate urgency with at-risk account scan |
| "NPS is at an all-time high" | n=480 (T3) | Contradicted by retention data (T1) | Artifact of survivorship bias | **NOISE** as a health metric. Useful only as a measure of retained-user satisfaction. |

**Research Gap Map:**

| Gap | Type | Decision It Blocks | Priority | Recommended Action | Timeline |
|---|---|---|---|---|---|
| Only 3 churned enterprise interviews | Thin evidence | Whether "workflow mismatch" is the dominant enterprise churn driver or one of several | CRITICAL | Expand to 8-10 churned enterprise interviews from the past 2 quarters | 3 weeks |
| No at-risk account identification | Blind spot | Which current enterprise accounts will churn next | CRITICAL | Build pre-churn behavioral model using the 60-day declining-usage + increasing-API-calls signature. Score all enterprise accounts. | 2 weeks |
| NPS not segmented by risk profile | Thin evidence | Whether low-NPS respondents correlate with pre-churn behavior | HIGH | Cross-reference NPS responses with behavioral health scores | 1 week |

**Recommendation 1 (O->I->R->C->W):**
- **Observation** [T1]: Enterprise segment retention dropped to 84% while SMB held at 96%. Pre-churn behavioral signature (declining board creation + increasing API export) is detectable 60 days before cancellation.
- **Implication**: Enterprise churn is predictable and accelerating. Each enterprise account lost represents 5-15x the revenue of an SMB account. The survivorship-inflated NPS is masking a revenue crisis.
- **Response**: (1) Build a pre-churn early warning model using the behavioral signature and score all enterprise accounts this week (Data team, 5-day sprint). (2) CS conducts proactive outreach to flagged accounts within 2 weeks. (3) Expand churned enterprise interviews to n=10 within 3 weeks to confirm the "workflow mismatch" hypothesis before committing to architectural changes.
- **Confidence**: H for the detection model (behavioral data is strong). M for the root cause (n=3 churn interviews is directional but not conclusive). Do not commit to major architecture changes until churn interviews reach n>=8 with consistent findings.
- **Watch**: If at-risk enterprise accounts flagged by the behavioral model have a >50% save rate after CS outreach, the problem may be relationship/support, not product architecture. If outreach has <10% save rate, the architectural hypothesis is confirmed and requires roadmap investment.

### What Changed

- **Source quality assessment revealed that NPS was actively misleading:** Generic AI correctly identified survivorship bias but treated it as one of several possible explanations. The skill graded NPS as T3 with a critical bias flag (survey excludes churned users), graded revenue retention as T1 (full population), and applied the evidence hierarchy to reach a definitive resolution: T1 overrides T3. The product is not healthy for enterprise.
- **Cross-source contradiction analysis turned the paradox into a diagnosis:** Instead of listing possible explanations, the skill surfaced the contradiction formally (NPS says healthy; retention says failing), resolved it using the evidence hierarchy (behavioral T1 > survey T3), and identified the mechanism (survivorship bias inflates NPS as unhappy users churn). The contradiction itself was the most valuable finding.
- **Signal vs. noise filtering reclassified NPS from "great news" to "noise":** The skill applied the 5-filter test and determined that the NPS score, despite being the highest ever, fails the behavioral corroboration filter. It is noise as a health metric and should not be cited in leadership updates without the survivorship caveat.
- **The research gap map identified the exact next steps with timelines:** Generic AI recommended "dig deeper into churned accounts." The skill specified: expand to 8-10 churned enterprise interviews within 3 weeks, build a pre-churn behavioral model within 5 days, and cross-reference NPS with behavioral health scores within 1 week. Each gap is tied to the specific decision it blocks.
- **The pre-churn behavioral signature was surfaced as an actionable detection tool:** The skill connected the analytics data (declining board creation + increasing API calls before churn) to a specific, buildable early-warning system. Generic AI mentioned "build a churn prediction model" as a general recommendation; the skill identified the specific behavioral features and an immediate implementation timeline.

---

## Use Case 3: Discovery Sprint Synthesis -- Four Sources Pointing in Four Directions

### Scenario

A PM at a healthcare scheduling platform (MedSync) is running a discovery sprint for a new patient self-scheduling product. The PM has collected four types of research data over the past month: a patient survey (n=312), 8 interviews with clinic administrators, 143 app reviews of three competitor scheduling products, and 3 months of support tickets (n=230) from the existing provider-facing product. Each source seems to suggest a different top priority -- the survey says patients want "faster booking," the admin interviews emphasize "insurance verification integration," the competitor reviews complain about "no real-time availability," and the support tickets are dominated by "appointment type confusion." The PM needs to synthesize these into a coherent research brief before the roadmap planning meeting in 10 days.

### The Prompt

> I'm running a discovery sprint for a new patient self-scheduling product at our healthcare scheduling platform (MedSync). I have: a patient survey (n=312) where "faster booking" was the top request, 8 admin interviews where insurance verification integration was the dominant theme, 143 competitor app reviews (Zocdoc, Solv, Nexhealth) where "no real-time availability" was the top complaint, and 230 support tickets from our existing provider-side product where "appointment type confusion" dominated. These all seem to point in different directions. What does the evidence actually say, and what should we build first?

### Without the Skill (Generic AI)

You have four rich data sources that appear to conflict, but they actually reveal different facets of the same problem space. Here's how I'd synthesize them:

**Theme 1: Speed and Friction in Booking**
The patient survey's "faster booking" and the competitor reviews' "no real-time availability" are two sides of the same coin. Patients want instant confirmation -- they don't want to request an appointment and wait for a callback. Real-time availability is the mechanism; faster booking is the outcome. This should be a core architectural decision for your product.

**Theme 2: Operational Integration**
Admin interviews emphasizing insurance verification makes sense -- admins deal with the downstream consequences of scheduling errors. If a patient books without verifying insurance, the clinic faces denied claims or awkward rescheduling conversations. Building insurance verification into the self-scheduling flow prevents downstream operational pain.

**Theme 3: Clarity and Categorization**
Support tickets about "appointment type confusion" suggest the current product's categorization is unclear. If patients can't tell the difference between a "new patient visit" and a "follow-up," they'll book the wrong slot, leading to scheduling conflicts and clinic frustration.

**Recommended prioritization:**
1. **Real-time availability engine** -- this is table stakes for patient self-scheduling. Without it, you're behind every competitor.
2. **Clear appointment type UX** -- if your existing product has this problem, your new product will inherit it. Fix the information architecture before launch.
3. **Insurance verification integration** -- important for admin adoption but can be phased in after initial launch since it's a provider-side concern.
4. **Speed optimizations** -- once the above are in place, optimize the booking flow for minimum clicks/taps.

**Additional thoughts:**
- Consider whether the admin interviews are biased toward operational concerns that patients don't experience directly
- The competitor reviews are valuable but remember reviewers are self-selected extremes
- Survey data gives you breadth but not depth -- consider follow-up interviews with patients who rated "faster booking" highly to understand what "faster" means to them

### With the Skill

**Step 0b: Framework Selection**

| Research Question Type | Primary Frameworks | Supporting Frameworks | Skipped |
|---|---|---|---|
| Discovery sprint (multi-source synthesis for a new product) | F1 (Evidence Triangulation), F3 (Research Quality Assessment), F4 (Signal vs. Noise), F5 (Insight Classification), F7 (Research Gap Mapping) | F6 (Demand-Side Analysis), F2 (Interview Analysis) | F8 (Competitive Discovery) -- partially applied; competitor reviews are included as a source but no full competitive discovery protocol since we have direct user data |

**Context Fitness Flag:** This is pre-product research. No T1 behavioral data exists for the patient self-scheduling product. Highest available evidence tier is T2 (admin interviews) and T3 (patient survey). All findings are directional until validated post-launch with behavioral data.

**Source Inventory & Quality Assessment:**

| Source | Type | Sample | Tier | Recency | Key Bias Risk |
|---|---|---|---|---|---|
| Patient survey (n=312) | Quantitative | Patients at existing MedSync clinics; unknown selection method | T3 | This month | **Critical: these are patients at provider-facing clinics, not self-scheduling users.** Their stated preferences about self-scheduling are speculative -- they have never used such a product. "Faster booking" may mean "faster than calling the front desk," not "faster than competitor self-scheduling apps." Relevance downgrade: T3 -> T4 for self-scheduling product decisions. |
| Admin interviews (n=8) | Qualitative | Clinic administrators at current MedSync clients | T2 | This month | Admin perspective, not patient perspective. Admins optimize for operational efficiency, not patient experience. Their priorities (insurance verification) are real but reflect a different stakeholder's job-to-be-done. |
| Competitor app reviews (n=143) | Mixed | Self-selected reviewers across Zocdoc (n=67), Solv (n=41), Nexhealth (n=35) | T5 individual, T4 pattern | Past 6 months | Extreme selection bias: reviewers are very happy or very frustrated. The silent majority of adequate-experience users is absent. However, consistent complaint patterns across 3 competitors signal category-level gaps, not competitor-specific issues. |
| Support tickets (n=230) | Anecdotal | Users of the existing provider-side product | T5 | 3 months | **Critical: these are from a different product** (provider-facing, not patient self-scheduling). Relevance to the new product depends on whether the appointment type taxonomy is shared. Support tickets capture failure states only -- the 95% of users who had no confusion are invisible. |

**Source coverage assessment:** No actual patient self-scheduling behavioral data exists (pre-product). No interviews with patients themselves (only a survey with closed-ended questions). No data from patients who use competitor self-scheduling products. No data from clinic staff who would manage the self-scheduling workflow (only admins). These are flagged as critical gaps.

**Key Findings (Evidence-Graded):**

**Finding 1: The four sources are not contradicting each other -- they represent four different stakeholders with four different jobs-to-be-done (H)**
- **Classification:** VALIDATED (via triangulation of source analysis, not via direct user evidence)
- **Confidence:** H (this is a structural observation about the data, not a user behavior claim)
- **Evidence:** Patient survey captures patient-stated preferences (T4, relevance-downgraded). Admin interviews capture operational workflow needs (T2). Competitor reviews capture experienced self-scheduling user frustrations (T4). Support tickets capture taxonomy/UX failures in a different product (T5).
- **Detail:** The apparent contradiction dissolves when you map each source to its stakeholder. Patients want speed. Admins want operational integrity. Competitor users want real-time accuracy. Support tickets reveal a UX debt in the existing system. These are four layers of the same product that must work simultaneously. The synthesis question is not "which one is right" but "which layer is the foundation that the others depend on."
- **Implication:** Prioritization should follow dependency order, not volume-of-mentions order. The correct question: which unmet need, if unresolved, makes the other three impossible to deliver?

**Finding 2: Real-time availability is the architectural foundation -- without it, "faster booking" is impossible and "appointment type confusion" gets worse (H)**
- **Classification:** EMERGING
- **Confidence:** M (no T1 data; inference from triangulation of T4 sources)
- **Evidence:** Competitor reviews: "no real-time availability" appears in 52/143 reviews across all 3 competitors, making it the single most frequent complaint in the category (T4). Patient survey: "faster booking" was the #1 request, but survey did not define "faster" -- cross-referencing with competitor reviews suggests "faster" = "instant confirmation without callback" (T4 + T4 triangulation). Support tickets: 89/230 "appointment type confusion" tickets resulted in double-bookings or wrong-slot bookings (T5) -- a problem that real-time availability with slot-type constraints would structurally prevent.
- **Detail:** Real-time availability is not a feature -- it is an architectural decision that determines whether the other three priorities are achievable. Without real-time slot data, "faster booking" means faster submission of a request that still requires manual confirmation. Without slot-type constraints in the real-time engine, appointment type confusion persists regardless of UX improvements.
- **Implication:** Real-time availability is the load-bearing architectural decision for the product. It must be decided first, not because users mentioned it most, but because the other three user needs depend on it structurally. `[EVIDENCE-LIMITED: no T1 behavioral data from actual self-scheduling usage. Conclusion is inferred from triangulation of T4 and T5 sources. Validate with prototype testing before committing architecture.]`

**Finding 3: Insurance verification is a necessary condition for admin adoption, but it is a Phase 2 integration, not a Phase 1 blocker (M)**
- **Classification:** EMERGING
- **Confidence:** M
- **Evidence:** Admin interviews: 7/8 admins named insurance verification as their top concern for self-scheduling adoption (T2, high frequency + high intensity -- multiple admins described it as a "dealbreaker"). Competitor reviews: insurance verification was mentioned in only 12/143 patient reviews (T4, low frequency from the patient perspective). Patient survey: insurance was not in the top 5 patient concerns (T4).
- **Detail:** Insurance verification is a high-intensity signal from admins and a low-frequency signal from patients. This is a classic stakeholder divergence. Admins care because they bear the operational cost of unverified bookings. Patients do not mention it because they assume verification happens behind the scenes. Both perspectives are valid; the question is sequencing.
- **Implication:** Insurance verification is required for admin buy-in (the B2B sale) but not for patient adoption (the B2C usage). A phased approach works: launch with basic scheduling + manual insurance verification by staff, then add automated verification in Phase 2. This gets the product to market faster while acknowledging the admin need.

**Finding 4: "Faster booking" is an ambiguous stated preference that masks at least 3 different underlying needs (M)**
- **Classification:** HYPOTHESIS
- **Confidence:** L
- **Evidence:** Patient survey: "faster booking" was #1 but the survey did not ask patients to define "faster" or describe their current booking experience (T4). No patient interviews exist to unpack the stated preference. Competitor reviews suggest "faster" may mean (a) real-time confirmation vs. callback, (b) fewer form fields, or (c) shorter time-to-next-available-appointment (T4, inferred from complaint categories).
- **Detail:** "Faster booking" is not a product requirement -- it is a proxy for at least 3 different needs, each requiring different product responses. Without patient interviews to disambiguate, this survey result cannot inform specific product decisions.
- **Implication:** `[EVIDENCE-LIMITED: stated preference from a survey with no behavioral context. The underlying need is ambiguous.]` Do not prioritize "speed optimizations" as a feature. Instead, run 8 patient interviews asking: "Tell me about the last time you booked a medical appointment. What took the longest? What was frustrating?" The answers will decompose "faster" into actionable requirements.

**Evidence Triangulation Summary:**

| Finding | Patient Survey (T4) | Admin Interviews (T2) | Competitor Reviews (T4) | Support Tickets (T5) | Convergence | Confidence |
|---|---|---|---|---|---|---|
| Real-time availability is foundational | Supports indirectly ("faster") (T4) | Silent | Supports directly (52/143 reviews) (T4) | Supports indirectly (double-bookings from lack of real-time constraints) (T5) | Partial (3 sources, but indirect for 2; no T1/T2 direct evidence) | M |
| Insurance verification needed for admin adoption | Silent | Strong support (7/8, unprompted) (T2) | Weak (12/143 mentions) (T4) | Silent | Weak (single stakeholder, single method) | M |
| Appointment type UX is broken | Silent | Silent | Silent | Strong (89/230 tickets) (T5) | Weak (single source, T5, different product) | L |
| "Faster booking" is the top patient need | Supports (T4, #1 request) | Silent | Supports indirectly (T4) | Silent | Weak (stated preference, no behavioral corroboration, ambiguous definition) | L |

**Research Gap Map:**

| Gap | Type | Decision It Blocks | Priority | Recommended Action | Timeline |
|---|---|---|---|---|---|
| No patient interviews | Critical gap | What "faster booking" actually means; which of 3 possible needs to address first | CRITICAL | 10 patient interviews focused on current booking journey and pain points | 2 weeks (before roadmap meeting if possible) |
| No behavioral data from competitor products | Blind spot | Whether real-time availability actually drives patient adoption and retention | HIGH | Analyze competitor conversion funnels (if available via partnerships or published case studies); prototype test with 15 patients | 3 weeks |
| No data from clinic staff (non-admin) | Blind spot | Operational feasibility of self-scheduling workflow; staff resistance risk | HIGH | 5 interviews with front-desk staff and medical assistants | 2 weeks |
| Support ticket data is from a different product | Thin evidence (relevance gap) | Whether appointment type confusion will transfer to the new product | MEDIUM | Confirm whether the new product shares the same appointment taxonomy; if yes, redesign taxonomy before launch | 1 week |

**Recommendation 1 (O->I->R->C->W):**
- **Observation** [T4 + T4 + T5, triangulated]: Real-time availability is the most frequent unmet need in competitor reviews (52/143), structurally enables "faster booking" (the top patient survey request), and would prevent the appointment type double-booking errors visible in support tickets (89/230). Three independent source types converge on this as the foundational capability.
- **Implication**: Real-time availability is not a feature to prioritize -- it is an architectural decision that determines the product's viability. Without it, the product competes with phone-based booking, not with modern self-scheduling tools.
- **Response**: Commit to real-time availability as the core architectural decision in the roadmap meeting. Engineering Lead owns architecture spike (2-week proof of concept). Do not finalize the full booking UX until the real-time data model is validated.
- **Confidence**: M -- assumes real-time availability is technically feasible with MedSync's existing provider data infrastructure. If the EHR integration does not support real-time slot queries, the architecture changes fundamentally. Also assumes patients will use self-scheduling if real-time slots are available -- this is `[EVIDENCE-LIMITED]` since no patient behavioral data exists.
- **Watch**: Prototype test with 15 patients within 4 weeks. If <60% of test participants complete a booking without assistance, the real-time availability alone is insufficient and the UX layer needs investment before architecture.

**Recommendation 2 (O->I->R->C->W):**
- **Observation** [T4]: "Faster booking" is the #1 stated patient preference, but the survey did not disambiguate the term. At least 3 possible underlying needs exist (real-time confirmation, fewer fields, shorter wait for availability), each requiring different product investments.
- **Implication**: Acting on "faster booking" as a product requirement is impossible without decomposing it. The roadmap meeting cannot make a specific commitment based on an ambiguous survey finding.
- **Response**: Run 10 patient interviews before the roadmap meeting (PM owns, 8-day sprint). Focus on the current booking journey, not on feature requests. Specific question: "Walk me through the last time you booked a medical appointment, step by step. What took the longest?" This decomposes "faster" into specific, addressable friction points.
- **Confidence**: H that this research is needed. L that any specific interpretation of "faster booking" is correct until the interviews are complete.
- **Watch**: If 7+ of 10 patients describe the same friction point, that single interpretation is an EMERGING finding strong enough for roadmap commitment. If the answers are dispersed across 3+ different frictions, the patient need is more fragmented than the survey suggested, and the product strategy should address the top friction rather than "speed" generically.

### What Changed

- **Source quality assessment revealed that the patient survey is weaker evidence than it appeared:** Generic AI treated the survey as strong quantitative data. The skill applied a relevance downgrade (patients at provider-facing clinics speculating about self-scheduling) and an ambiguity flag ("faster booking" is undefined), dropping it from T3 to T4. This prevented the most voluminous data source from dominating the synthesis by sheer sample size.
- **The four "conflicting" sources were reframed as four stakeholder perspectives:** Generic AI also noted this, but the skill formalized it through the source inventory (each source mapped to a stakeholder and a job-to-be-done), then applied a dependency analysis to determine sequencing. The insight was not "which source is right" but "which layer must be built first for the others to function."
- **Evidence triangulation revealed real-time availability as the convergence point across sources:** Generic AI recommended real-time availability as "table stakes." The skill demonstrated WHY through triangulation: it connects the patient's "faster" need, the competitor users' "real-time" complaint, and the support tickets' double-booking problem. Three independent sources, three different methods, converging on one architectural decision. That is a qualitatively different argument than "competitors have it, so you need it."
- **Research gap mapping identified that the most important research has not been done:** The single most critical gap -- no patient interviews about the actual booking journey -- was named, prioritized as CRITICAL, and given a specific method and timeline (10 interviews, 8-day sprint) that could be completed before the roadmap meeting. Generic AI mentioned "follow-up interviews" as a nice-to-have; the skill positioned it as a blocker for the roadmap decision.
- **The "faster booking" finding was downgraded from actionable insight to ambiguous hypothesis:** Generic AI treated "faster booking" as a clear patient need and recommended "speed optimizations." The skill identified that "faster" is a proxy masking at least 3 different needs, classified it as HYPOTHESIS (L confidence), and flagged it as `[EVIDENCE-LIMITED]`. This prevented the team from building "speed features" that might address the wrong underlying problem.
