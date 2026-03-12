# Use Cases: Problem Framing

## Use Case 1: The CEO Says "We Need a Mobile App"

### Scenario
The CEO of a B2B SaaS analytics platform (2,000 enterprise customers, $40M ARR) tells the VP Product: "Our competitors all have mobile apps. We need one by Q3." The PM inherits this mandate and needs to determine whether a mobile app actually solves a real problem -- or whether the CEO is prescribing a solution before anyone has diagnosed the disease. No user research has been done; the directive is based on a board meeting where a competitor's mobile app was mentioned.

### The Prompt
> Our CEO says we need to build a mobile app because our competitors have them. We're a B2B analytics platform. I need to figure out if this is the right thing to build and what problem it would actually solve. What should I do?

### Without the Skill (Generic AI)
Building a mobile app for your B2B analytics platform is a significant undertaking, but it can drive real value. Here's a framework for approaching this:

**Why a mobile app could make sense:**
- Executives and managers increasingly want to check dashboards on the go
- Mobile access can improve engagement and daily active usage
- Competitors offering mobile create a perception gap in sales conversations
- Mobile push notifications can drive re-engagement with key metrics

**Key considerations before building:**
1. **Target audience:** Focus on executives and managers who need quick access to KPIs, not analysts who need deep data manipulation
2. **Core features:** Start with a read-only dashboard viewer, push alerts for metric thresholds, and a simple commenting/annotation feature
3. **Platform choice:** iOS first if your customers skew enterprise; consider React Native for cross-platform efficiency
4. **MVP scope:** A 12-week sprint could deliver a dashboard viewer with SSO and push notifications

**Recommended approach:**
- Survey your top 20 customers to gauge interest
- Build a lightweight MVP focused on dashboard viewing
- Measure adoption over 90 days before investing in deeper features
- Use the mobile app as a differentiator in sales demos

**Risks to manage:**
- Security requirements for mobile are higher in enterprise
- Low adoption could waste 3-6 months of engineering time
- Maintaining a separate mobile codebase increases ongoing cost

The mobile app can be a strong competitive move if scoped correctly. Start small, measure adoption, and iterate based on usage data.

### With the Skill

**Step 0: Context Fitness Check -- This Is a Solution, Not a Problem**

The CEO's directive -- "build a mobile app" -- is a solution masquerading as a problem (Failure Mode FM-1). Before any scoping, feature listing, or technical planning, we need to define the actual problem. The question is not "should we build a mobile app?" The question is "what problem are our users experiencing that a mobile app might -- or might not -- solve?"

**Problem Definition Canvas (Framework 1)**

| Dimension | Finding | Evidence | Confidence |
|---|---|---|---|
| **Who has this problem?** | Unknown. CEO cited "our customers" but no specific segment identified. Could be: (a) executives wanting KPI glances, (b) field sales needing client data in meetings, (c) on-call analysts needing alert triage. Each is a different problem. | (T5: CEO assertion based on board meeting) | L |
| **What are they trying to do?** | Unknown. "Access analytics on mobile" is a solution description. The underlying goal has not been articulated by any user. | (T6: inferred from competitor feature) | L |
| **What do they do today?** | Unknown. No data on whether users attempt to access the platform on mobile browsers, request mobile access in support tickets, or use workarounds (screenshots, exported PDFs, email digests). | (T6: no behavioral data collected) | L |
| **Why is that painful?** | Unvalidated. The assumption is that lack of mobile access is painful, but no evidence of pain -- no support tickets, no churn exit interviews citing mobile, no workaround behavior observed. | (T6: assumed based on competitor parity logic) | L |
| **What triggers the pain?** | Unspecified. If the trigger is "board meetings where competitors are mentioned," that is the CEO's pain (competitive positioning), not the user's pain. | (T5: CEO's board meeting experience) | L |
| **What does "good" look like?** | Undefined by users. The CEO's "good" is competitive parity. Users have not been asked. | (T5: CEO framing) | L |
| **How do they know it's solved?** | No user-defined success criteria exist. | (T6: none established) | L |

**Canvas Assessment: 0 cells at T1-T2, 0 at T3-T4, 7 at T5-T6 = SPECULATION.** This is not a problem definition -- it is an untested assumption. The Canvas itself becomes the research brief: every cell is a question that must be answered before committing engineering resources.

`[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`

**Root Cause Analysis (Framework 2 -- 5 Whys)**

```
Symptom: CEO says "we need a mobile app"
|
+-- Why 1: Competitor was featured at a board meeting for having a mobile app (T5: CEO report)
    |
    +-- Why 2: Board members questioned whether our platform is falling behind (T5: CEO interpretation)
        |
        +-- Why 3a: Our sales team may be losing deals due to perceived feature gap (T5: unvalidated -- no win/loss data cited)
        |   |
        |   +-- ROOT CAUSE A: Competitive positioning gap in sales conversations (T5) -- [EVIDENCE-LIMITED]
        |
        +-- Why 3b: Users may genuinely need mobile access for specific workflows (T6: assumed, zero user evidence)
            |
            +-- ROOT CAUSE B: Unidentified user workflow gap (T6) -- [EVIDENCE-LIMITED]
```

**Divergence check:** The root cause diverges dramatically from the presented problem. The CEO framed this as a product gap ("we need a mobile app"). The 5 Whys reveal two possible root problems: (a) a sales/positioning problem, or (b) an unvalidated user workflow problem. These require completely different solutions. A sales positioning problem might be solved by a demo-ready prototype or a roadmap slide. A user workflow problem requires Discovery research to even define.

**Opportunity Sizing (Framework 4)**

| Dimension | Score | Evidence | Confidence |
|---|---|---|---|
| **Frequency** | ? -- Cannot score | No data on how often users need mobile access (T6) | L |
| **Severity** | ? -- Cannot score | No evidence users are blocked, frustrated, or churning due to lack of mobile (T6) | L |
| **Breadth** | ? -- Cannot score | No data on what % of the 2,000 customers would use a mobile app (T6) | L |
| **Willingness** | 2 -- No evidence of workaround investment | No users are paying for mobile workarounds, building mobile dashboards elsewhere, or requesting mobile in support tickets (T6: absence of signal) | L |

**Opportunity Score: Unscorable.** Every dimension lacks the evidence needed to produce a meaningful score. Committing 3-6 months of engineering to an unscorable opportunity is the definition of building on assumption.

**Recommendation (O-I-R-C-W Cascade)**

- **Observation** [T5/T6]: The CEO's mobile app directive is based on competitive parity logic from a board meeting. Zero user behavioral data (T1) or primary research (T2) supports the existence of a mobile access problem.
- **Implication**: Building a mobile app without validated problem evidence risks 3-6 months of engineering investment ($300K-$600K fully loaded) on a solution to a problem that may not exist for users. The real problem may be competitive positioning in sales conversations -- a fundamentally different problem with fundamentally different solutions.
- **Response**: Before any mobile app work, run a 2-week problem validation sprint: (1) Pull mobile browser access logs to check if users are attempting mobile access today (T1, 2 days), (2) Analyze support tickets and churn exit interviews for mobile-related requests (T1, 2 days), (3) Interview 8-10 users across 3 segments -- executives, field sales users, on-call analysts -- about their out-of-office analytics workflows (T2, 1 week). Owner: PM. Timeline: 2 weeks.
- **Confidence**: M -- assumes that 2 weeks of research will produce enough signal to either validate or invalidate the mobile problem. If the user base is too small or too disengaged for meaningful signal, additional research is needed.
- **Watch**: If mobile browser access logs show >5% of DAU attempting mobile access, or if >3 of 10 interviewees describe a specific mobile workflow pain, the problem may be real. If neither signal appears, the problem is a stakeholder projection, not a user need.

### What Changed
- **Solution-as-problem detected and redirected.** The generic output accepted "build a mobile app" as the starting point and immediately began scoping features. The skill recognized this as FM-1 (Solution Masquerading as Problem) and redirected to problem definition before any solution work.
- **Problem Definition Canvas exposed total evidence vacuum.** All 7 dimensions scored at T5-T6 with L confidence, producing a SPECULATION assessment. This makes the evidence gap viscerally clear to any stakeholder reading the document -- including the CEO.
- **Root cause analysis revealed two fundamentally different problems.** The 5 Whys branched at Why 3 into a sales positioning problem (solvable without a mobile app) and an unvalidated user workflow problem (requires research to even define). The generic output conflated these.
- **Opportunity sizing was honestly declared unscorable.** Rather than fabricating a plausible-sounding estimate, the skill flagged that every dimension lacked evidence to score -- making the case for research before commitment.
- **Concrete next action with timeline and success criteria.** Instead of "survey your top 20 customers," the skill prescribed a specific 2-week validation sprint with T1 data pulls and T2 interviews, with explicit watch indicators that determine whether to proceed.

---

## Use Case 2: Retention Is Declining 3% Month-Over-Month and Everyone Has a Theory

### Scenario
A consumer SaaS product (photo editing tool, 800K MAU, freemium model) has seen 30-day retention drop from 42% to 33% over 4 months. The Head of Growth blames onboarding changes made in Q1. The Design Lead thinks the new editor UI is confusing power users. Engineering believes performance degradation on lower-end devices is the issue. Customer Support says users are leaving for a competitor that launched AI features. The PM needs to cut through competing narratives and identify the actual root cause -- or causes -- before the team spends a quarter building the wrong fix.

### The Prompt
> Our 30-day retention has dropped from 42% to 33% over 4 months. Growth thinks it's onboarding, Design thinks it's the new UI, Engineering thinks it's performance, and Support thinks users are leaving for a competitor with AI features. How do I figure out what's actually going on and what to fix first?

### Without the Skill (Generic AI)
A 9-percentage-point retention drop over 4 months is a serious problem that needs immediate investigation. Here's how to approach this systematically:

**Step 1: Data Analysis**
First, segment your retention data to identify where the drop is concentrated:
- Cohort analysis by signup date to see if the decline started with a specific cohort
- Segment by user type (free vs. paid, new vs. returning, power user vs. casual)
- Check if the drop is uniform across platforms (web, iOS, Android)

**Step 2: Evaluate Each Theory**
- **Onboarding (Growth's theory):** Compare retention of users who went through old vs. new onboarding. If new onboarding cohorts retain worse, this is a signal.
- **UI confusion (Design's theory):** Look at engagement metrics for power users specifically. Are they using the new editor less? Are they completing fewer projects?
- **Performance (Engineering's theory):** Check crash rates, load times, and error rates by device tier. If low-end devices show higher churn, performance is a factor.
- **Competitor (Support's theory):** Monitor competitor mentions in cancellation surveys and social media. Check if churn correlates with the competitor's launch date.

**Step 3: Prioritize Fixes**
Based on your findings, use an impact-effort matrix:
- **Quick wins:** Performance optimizations that improve experience across the board
- **High impact:** Onboarding improvements if cohort data confirms the theory
- **Strategic:** AI feature development if competitor threat is validated

**Step 4: Run Experiments**
- A/B test a revised onboarding flow
- Roll back UI changes for a subset of power users to measure impact
- Implement performance improvements and measure retention lift

**Recommended timeline:**
- Week 1-2: Data analysis and segmentation
- Week 3-4: Targeted fixes for the highest-signal theory
- Month 2-3: Deeper investments based on validated findings

The key is letting data, not opinions, drive the decision. Start with the analysis, then act on what the numbers tell you.

### With the Skill

**Step 0b: Framework Selection**

Question type: **Root cause investigation** -- "why is this happening?" with multiple competing theories.
- Primary frameworks: F2 5 Whys Root Cause Analysis, F1 Problem Definition Canvas, F6 Constraint Mapping
- Supporting: F4 Opportunity Sizing (to quantify which root cause matters most), F7 Stakeholder Impact Matrix (to manage the four competing narratives)
- Skipped: F8 ICE/RICE -- premature until root causes are identified. F3 JTBD -- this is a diagnosis problem, not a "what job" problem.

**Problem Statement**

Retained users of a freemium photo editing tool (800K MAU) are churning at an accelerating rate -- 30-day retention declined from 42% to 33% over 4 months -- resulting in an estimated loss of ~72,000 monthly active users per cohort and projected revenue impact of $180K-$360K/quarter on conversion pipeline. **Confidence: H** (T1: retention data from product analytics).

The problem statement is high-confidence on the *symptom*. The root cause is where confidence drops.

**Root Cause Analysis (Framework 2 -- 5 Whys with Branching)**

```
Symptom: 30-day retention dropped from 42% to 33% over 4 months (T1: product analytics)
|
+-- Why 1: More users are disengaging within the first 30 days than 4 months ago (T1: cohort data)
    |
    +-- Why 2a: ONBOARDING BRANCH -- New onboarding flow (shipped Q1) may be failing to activate users
    |   |
    |   Evidence check: Compare retention of Q1 onboarding cohort vs. pre-Q1 cohort (T1)
    |   STATUS: [EVIDENCE AVAILABLE -- REQUIRES ANALYSIS]
    |   If pre/post cohort retention diverges by >3pp, this branch is validated.
    |   If retention decline appears in BOTH cohorts, onboarding is not the root cause.
    |   |
    |   +-- Why 3a: New onboarding removed the guided project flow that previously drove first-session completion (T5: Growth team's assertion)
    |       |
    |       +-- ROOT CAUSE A: Activation metric (first project completion) regressed due to onboarding redesign (T5 -- requires T1 validation)
    |           [EVIDENCE-LIMITED: validate by pulling first-project-completion rates pre/post Q1]
    |
    +-- Why 2b: UI BRANCH -- Users who previously completed tasks are now struggling or abandoning
    |   |
    |   Evidence check: Task completion rates and session depth for returning users on new vs. old editor (T1)
    |   STATUS: [EVIDENCE AVAILABLE -- REQUIRES ANALYSIS]
    |   If returning-user task completion dropped post-UI change, this branch is validated.
    |   If new users also struggle equally, the problem is broader than power-user confusion.
    |   |
    |   +-- Why 3b: New editor UI reorganized tool placement without user testing (T5: Design lead's admission)
    |       |
    |       +-- ROOT CAUSE B: Learned workflows disrupted for existing users, increasing cognitive load per session (T5 + T6)
    |           [EVIDENCE-LIMITED: validate with session recordings and task-completion-time analysis]
    |
    +-- Why 2c: PERFORMANCE BRANCH -- Users on lower-end devices experiencing degraded performance
    |   |
    |   Evidence check: Retention segmented by device tier; crash rates and load times by device (T1)
    |   STATUS: [EVIDENCE AVAILABLE -- REQUIRES ANALYSIS]
    |   If low-end device retention dropped disproportionately, this branch is validated.
    |   If retention dropped equally across device tiers, performance is not the primary driver.
    |   |
    |   +-- Why 3c: New editor introduced WebGL rendering that requires more GPU memory (T3: engineering assessment)
    |       |
    |       +-- ROOT CAUSE C: Technology choice in new editor excludes ~25% of user base on lower-end hardware (T3 + T6)
    |           [Partial evidence: engineering confirms WebGL requirements. User impact unquantified.]
    |
    +-- Why 2d: COMPETITIVE BRANCH -- Users leaving for a competitor with AI-powered features
        |
        Evidence check: Churn exit survey mentions of competitor; timing correlation with competitor launch (T1 + T2)
        STATUS: [EVIDENCE PARTIALLY AVAILABLE -- exit surveys exist but sample is small]
        If competitor mentions spiked in exit surveys post-launch, this branch is validated.
        If churn increase predates competitor launch, competitive pressure is not the primary driver.
        |
        +-- Why 3d: Competitor launched AI background removal and auto-enhancement that our tool lacks (T5: Support team reports from user conversations)
            |
            +-- ROOT CAUSE D: Value proposition gap -- competitor offers capability our users want but we do not provide (T5)
                [EVIDENCE-LIMITED: Support anecdotes are T5. Need exit survey data (T2) and competitor adoption data (T4).]
```

**The Critical Insight: This Is Probably Multi-Factorial**

A 9pp retention decline over 4 months is unlikely to have a single cause. The timing suggests compounding factors: Q1 onboarding change + Q1 UI redesign + gradual performance degradation + competitor launch. The 5 Whys analysis deliberately branches because single-threading would produce a false diagnosis.

**Opportunity Sizing Per Root Cause (Framework 4 -- Comparative)**

| Root Cause | Frequency | Severity | Breadth | Willingness | Score | Evidence Quality | Confidence |
|---|---|---|---|---|---|---|---|
| **A: Onboarding regression** | 5 -- every new user (T1) | 3-4 -- fails to activate but does not block entirely (T5) | 4 -- 100% of new signups (T1) | 3 -- users who don't activate rarely return (T1) | 180-240 | Mixed: T1 frequency/breadth, T5 severity | M |
| **B: UI disruption** | 3 -- every editing session for returning users (T6) | 3 -- workaround exists (relearn) but friction is high (T5) | 2-3 -- affects returning users who learned old UI (T6) | 3 -- would stay if friction removed (T6) | 54-81 | Weak: mostly T5-T6 | L |
| **C: Performance on low-end devices** | 4 -- every session on affected devices (T3) | 4 -- app crashes or runs unusably slow (T3) | 2 -- ~25% of user base on low-end devices (T6) | 4 -- users leave immediately when app is unusable (T6) | 128 | Partial: T3 technical, T6 breadth | M |
| **D: Competitor AI features** | 2 -- relevant only when user needs specific AI capability (T5) | 2 -- can still edit photos, just lacks one capability (T5) | 2 -- subset of users who need AI features (T5) | 3 -- some users willing to switch (T5) | 24 | Weak: all T5 | L |

**Cross-Framework Contradiction (Mandatory)**

| Contradiction | Analysis A says | Analysis B says | Resolution |
|---|---|---|---|
| Onboarding vs. UI as primary driver | Root Cause A (onboarding) affects all new users -- highest breadth | Root Cause B (UI) affects returning users -- the cohort with highest LTV | Both could be true simultaneously. The retention decline may be a new-user activation problem AND a returning-user engagement problem. Segmented cohort analysis (new vs. returning user retention) is the discriminating test. |
| Performance vs. Competitive pressure | Root Cause C suggests users leave because the app is broken for them | Root Cause D suggests users leave because a competitor is better | For low-end device users, both may compound: degraded performance + attractive alternative = accelerated churn. Check if competitor mentions are disproportionately high among low-end device users. |

**Recommendations (O-I-R-C-W Cascade)**

**Recommendation 1: Run the Discriminating Analysis Before Committing to Any Fix**

- **Observation** [T1]: Four competing root cause theories exist, each championed by a different team. All four are plausible. None have been validated against behavioral data that already exists in the product analytics system.
- **Implication**: Committing to any single fix without discriminating analysis risks spending a quarter solving 25% of the problem while 75% continues unchecked. Worse, each team will interpret any improvement (or lack thereof) as confirmation of their theory.
- **Response**: Before any fix is built, run a 1-week data analysis sprint with four specific queries: (1) Retention by cohort, pre/post Q1 onboarding change. (2) Returning-user task completion rates, pre/post UI redesign. (3) Retention segmented by device tier with crash/load-time correlation. (4) Exit survey competitive mentions over time, correlated with competitor launch date. Owner: PM + Data Analyst. Timeline: 5 business days. Deliverable: A validated root cause ranking that replaces opinion with data.
- **Confidence**: H -- the data to discriminate between theories already exists. This is not a research problem; it is an analysis problem.
- **Watch**: If the data analysis shows roughly equal contribution from all four causes, the problem is systemic (cumulative quality regression), not attributable to a single root cause. This changes the response from "fix the root cause" to "halt new feature work and run a quality sprint."

**Recommendation 2: Instrument the Activation Funnel Immediately**

- **Observation** [T5]: Growth's theory (onboarding regression) has the highest potential opportunity score (180-240) but severity is unvalidated.
- **Implication**: If first-project-completion rate dropped post-Q1, the onboarding change is destroying value at the widest point of the funnel. Every day without data is a day of compounding loss.
- **Response**: Add activation funnel instrumentation (onboarding step completion, first project start, first project completion, first export) if not already tracked at step-level granularity. Owner: Engineering + Growth. Timeline: 2-3 days.
- **Confidence**: H -- assumes onboarding step tracking is technically straightforward. If the onboarding flow is not instrumented at step level, this is itself a problem.
- **Watch**: If first-project-completion rate is stable pre/post Q1, onboarding is not the cause. Redirect investigation to Root Causes B and C.

**Assumption Registry**

| # | Assumption | Framework | Confidence | Evidence | Invalidation |
|---|---|---|---|---|---|
| 1 | The 4-month retention decline has identifiable, discrete root causes rather than being diffuse quality regression | F2 Root Cause Analysis | M | T6: assumes the 5 Whys branching model applies; some retention declines are death-by-a-thousand-cuts | If the discriminating analysis shows no single cause explains >3pp of the 9pp drop, the problem is systemic, not attributable |
| 2 | Existing product analytics data is sufficient to discriminate between the four theories | Recommendation 1 | M | T6: assumes instrumentation exists for cohort comparison, device segmentation, and task completion tracking | If key events are not tracked (e.g., onboarding steps, task completion), the 1-week analysis sprint becomes a 3-week instrumentation + analysis sprint |
| 3 | The four theories from internal stakeholders cover the actual root causes | F2 Root Cause Analysis | L | T5: assumes the Growth, Design, Engineering, and Support teams have collectively identified all plausible causes | A cause not represented by any internal team (e.g., pricing change by a partner, SEO channel shift bringing lower-intent users, seasonal effect) could be the real driver. The discriminating analysis should include a "none of the above" check. `[EVIDENCE-LIMITED]` |

**Adversarial Self-Critique**

**Weakness 1: The Framework Assumes the Problem Is Diagnosable from Existing Data.** If the product lacks granular event tracking -- a common state for 800K-MAU consumer tools that grew quickly -- the "1-week analysis sprint" recommendation falls apart. The PM would need 3-4 weeks of instrumentation before analysis can begin, during which retention continues to erode. The skill should have assessed data infrastructure maturity as a constraint (F6) before prescribing data-driven diagnosis.

**Weakness 2: Stakeholder Theories May Be a Subset of Reality.** The analysis takes the four internal theories as the universe of possible causes and structures the entire root cause tree around them. But retention declines can be driven by factors no internal team surfaces: changes in acquisition channel mix bringing lower-quality users, seasonal effects, a pricing or billing change, or even an external event (competitor free tier, viral social media criticism). The "none of the above" scenario is listed in the Assumption Registry but insufficiently investigated.

**Weakness 3: Multi-Factorial Framing May Paralyze Rather Than Clarify.** By acknowledging that all four causes might be real simultaneously, the analysis risks producing a "fix everything" recommendation that is operationally equivalent to no recommendation. A PM with four validated root causes and limited engineering capacity still needs to pick one to fix first -- and this analysis defers that decision to the discriminating data analysis rather than providing a decision framework for the post-analysis moment.

### What Changed
- **Root cause analysis branched into four parallel tracks with explicit validation criteria for each.** The generic output listed "evaluate each theory" as a step; the skill structured each theory as a 5 Whys branch with specific T1 data queries that would confirm or eliminate it, including the exact conditional logic ("if X, this branch is validated; if Y, it is eliminated").
- **Opportunity sizing was applied per root cause, exposing which theories matter most even before validation.** The generic output treated all four theories as equal candidates. The skill scored each on Frequency x Severity x Breadth x Willingness, revealing that onboarding regression (score 180-240) dwarfs competitive pressure (score 24) in potential impact -- changing the investigation priority order.
- **Cross-framework contradictions surfaced compound effects.** The skill identified that performance degradation + competitive pressure may compound specifically for low-end device users -- a non-obvious interaction that none of the four teams would see from their individual vantage points.
- **Assumption Registry exposed the meta-risk.** The third assumption -- that the four internal theories cover reality -- is the most dangerous blind spot. The skill flagged it at L confidence with a specific invalidation test, preventing the PM from treating stakeholder theories as the complete universe of possibilities.
- **Adversarial self-critique identified three genuine weaknesses in the analysis itself**, including the risk that the "analyze first" recommendation may be impossible if instrumentation is inadequate, and that the multi-factorial framing could paralyze rather than clarify.

---

## Use Case 3: Five Stakeholders, Five "Urgent" Feature Requests, One Platform Team

### Scenario
A platform team at a mid-stage B2B company (internal developer platform, ~200 internal engineer users across 5 product teams) receives five simultaneous feature requests, each marked "urgent" and each from a different engineering team lead. Team A wants a self-service database provisioning tool. Team B wants CI/CD pipeline templates. Team C wants better observability dashboards. Team D wants an internal API gateway. Team E wants improved developer onboarding documentation. The platform PM has capacity for one major initiative this quarter. Each requester frames their request as the most critical blocker. The PM needs to identify the underlying problems, determine which are real and which are perceived, and make a defensible prioritization decision.

### The Prompt
> I'm a platform PM and I just got 5 "urgent" feature requests from 5 different team leads: self-service DB provisioning, CI/CD templates, observability dashboards, API gateway, and better dev onboarding docs. I can only do one this quarter. How do I figure out which one to actually build?

### Without the Skill (Generic AI)
This is a classic prioritization challenge. Here's a structured approach to pick the right initiative:

**Step 1: Gather Context on Each Request**
Set up 30-minute conversations with each team lead to understand:
- What specific problem does this solve for their team?
- How much time are they spending on the current workaround?
- What happens if this doesn't get built this quarter?
- How many engineers on their team would benefit?

**Step 2: Score Using RICE Framework**
For each request, estimate:
- **Reach:** How many of the 200 engineers would use this?
- **Impact:** How much would it improve their productivity? (3=massive, 2=high, 1=medium, 0.5=low)
- **Confidence:** How confident are you in your estimates?
- **Effort:** How many person-weeks to build?

| Request | Reach | Impact | Confidence | Effort | RICE Score |
|---|---|---|---|---|---|
| DB provisioning | 40 | 2 | 80% | 8 weeks | 8.0 |
| CI/CD templates | 150 | 2 | 80% | 6 weeks | 40.0 |
| Observability | 100 | 1 | 60% | 10 weeks | 6.0 |
| API gateway | 60 | 2 | 50% | 12 weeks | 5.0 |
| Dev onboarding | 30 | 1 | 70% | 4 weeks | 5.3 |

**Step 3: Consider Strategic Factors**
Beyond the RICE scores:
- Which request aligns with company OKRs this quarter?
- Are any of these blocking revenue-generating work?
- Is there a dependency chain (e.g., API gateway enables other teams)?
- Which builds platform capabilities that compound over time?

**Step 4: Make the Call**
Based on this analysis, CI/CD templates likely win: highest reach, reasonable effort, and high confidence. It benefits 75% of your engineering org and can be delivered within a quarter.

**Recommended approach:**
1. Build CI/CD templates as the Q2 initiative
2. Create lightweight self-service guides for DB provisioning as a stopgap
3. Add observability and API gateway to the H2 roadmap
4. Assign dev onboarding docs to a tech writer rather than the platform team

This gives you the highest-impact investment while showing each team lead their request is on the roadmap.

### With the Skill

**Step 0: Context Fitness Check**

Five feature requests from five stakeholders are five *solutions*, not five *problems*. Before any prioritization scoring, the PM must peel each request back to the underlying problem. Prioritizing solutions before understanding problems is how platform teams build the wrong thing with perfect RICE scores. This is a **Stakeholder alignment + Prioritize across problems** question type.

**Step 0b: Framework Selection**
- Primary: F7 Stakeholder Impact Matrix, F1 Problem Definition Canvas (per request), F8 ICE/RICE Prioritization, F4 Opportunity Sizing
- Supporting: F2 5 Whys (applied per request to peel solution back to problem), F5 Problem-Solution Fit
- Skipped: F3 JTBD (internal tooling -- functional job dominates; emotional/social secondary), F6 Constraint Mapping (apply after selection, not across all 5)

**Peeling Solutions to Problems (Framework 1 + Framework 2, Applied Per Request)**

| Request (Solution) | Presented Problem | 5 Whys Root Problem | Evidence | Confidence |
|---|---|---|---|---|
| **A: Self-service DB provisioning** | "It takes 2 weeks to get a new database" | Engineers cannot iterate on data model changes during development because DB provisioning requires a Jira ticket, DBA review, and manual setup -- creating a 2-week bottleneck in every project that needs a new data store. Root problem: **DBA team is a serial bottleneck for a parallelizable task.** | (T5: Team A lead assertion. T1 data available: Jira ticket lead times for DB requests.) | M -- lead time is verifiable from Jira; actual developer impact is T5 |
| **B: CI/CD templates** | "Every team builds CI/CD from scratch" | Engineers spend 2-3 days per project configuring CI/CD pipelines because no standard templates exist, leading to inconsistent deployment practices and ~4 production incidents/quarter traced to misconfigured pipelines. Root problem: **Lack of standardized deployment infrastructure causes both waste (setup time) and risk (incidents).** | (T5: Team B lead assertion. T1 partially available: incident post-mortems may confirm pipeline-related incidents.) | M -- incident data is T1 if post-mortems exist; setup time is T5 |
| **C: Observability dashboards** | "We can't see what's happening in production" | When production issues occur, engineers spend 30-60 minutes assembling context from 4 different logging/monitoring tools before they can begin debugging, extending MTTR and increasing customer impact. Root problem: **Fragmented observability tooling extends incident response time.** | (T5: Team C lead assertion. T1 available: MTTR data from incident management system.) | M -- MTTR is measurable; the attribution to tooling fragmentation is T5 |
| **D: API gateway** | "Inter-service communication is a mess" | Teams building integrations between internal services must negotiate ad-hoc contracts, handle auth independently, and manage versioning manually -- resulting in brittle integrations that break during deployments. Root problem: **No internal API contract standard, causing integration fragility.** | (T5: Team D lead assertion. T1 partially available: deployment-related incidents involving service integration.) | L -- "mess" is vague; severity depends on integration volume and incident frequency |
| **E: Dev onboarding docs** | "New hires take 3 months to be productive" | New engineers cannot find authoritative documentation on internal systems, so they rely on asking teammates (interrupting them) or reading source code (slow and error-prone), extending time-to-productivity. Root problem: **Tribal knowledge dependency -- institutional knowledge exists only in people's heads.** | (T5: Team E lead assertion. T1 partially available: time-to-first-commit for new hires.) | L -- "3 months" is an assertion; time-to-productivity is hard to measure without baseline |

**Key Insight from Problem Peeling:** Requests A, B, and D share a common meta-problem -- **the platform lacks self-service primitives, forcing engineers into ticket-based workflows that create bottlenecks.** Solving any one in isolation helps one team; solving the meta-problem (self-service platform capabilities) helps all five. This reframing changes the prioritization entirely.

**Stakeholder Impact Matrix (Framework 7)**

| Stakeholder | Problem Impact | Power (1-5) | Interest (1-5) | Position | Key Insight |
|---|---|---|---|---|---|
| Team A lead (DB provisioning) | 2-week bottleneck per project (T5) | 2 -- peer influence only (T6) | 5 -- directly blocked (T5) | Champion | High interest, low power. Loudest voice but cannot approve/block. |
| Team B lead (CI/CD) | 2-3 days per project + incident risk (T5) | 3 -- leads largest team (T6) | 4 -- significant friction (T5) | Champion | Broad impact claim. Verify with incident data. |
| Team C lead (Observability) | Extended MTTR (T5) | 3 -- owns on-call for critical service (T5) | 4 -- affects incident response (T5) | Champion | MTTR impact is measurable and visible to leadership. |
| Team D lead (API gateway) | Integration fragility (T5) | 2 -- smaller team (T6) | 3 -- painful but intermittent (T5) | Supporter | Problem is real but frequency may be low. |
| Team E lead (Dev onboarding) | Slow ramp-up (T5) | 2 -- newest team lead (T6) | 3 -- affects team capacity (T5) | Supporter | Long-term payoff but low urgency signal. |
| **VP Engineering** | All five problems affect eng velocity, which affects roadmap delivery | 5 -- approves platform roadmap (T5) | 4 -- cares about aggregate eng productivity (T6) | Neutral -- has not weighed in | **This is the decision-maker.** Frame the recommendation in terms of aggregate eng velocity impact, not individual team requests. |
| **DBA team** (affected bystander for Request A) | Self-service DB provisioning would reduce their workload but also reduce their gatekeeping role | 3 -- can slow-roll adoption (T6) | 3 -- mixed: less work but less control (T6) | Potentially Resistant | Hidden stakeholder. If they resist, DB provisioning adoption stalls regardless of build quality. |

**Proxy Stakeholder Alert:** All five requests come from team leads (T5 sources) speaking on behalf of their engineers. None of the requests include direct engineer input (T2) or behavioral data (T1). The team leads' framing may reflect their priorities, not their team's actual pain points. A 30-minute survey of 20 engineers across all 5 teams (T2, 3 days) would upgrade the evidence base for all five problems simultaneously.

**Problem Prioritization (Framework 8 -- ICE Scoring with Evidence Tiers)**

| Rank | Problem (not solution) | Impact (1-5) | Confidence (1-5) | Ease (1-5) | ICE Score | Evidence Quality | Recommended Action |
|---|---|---|---|---|---|---|---|
| 1 | **Lack of standardized CI/CD causes waste + incidents** | 4 (T5: broad impact claim; T1: incident data may confirm) | 3 (T5 primary; T1 available but unanalyzed) | 3 (6-week estimate, within quarter; T5: eng lead estimate) | 36 | 33% T1-accessible, 67% T5 | **Investigate** -- pull incident post-mortems and CI/CD setup time estimates before committing |
| 2 | **DBA bottleneck blocks iteration velocity** | 4 (T5: 2-week lead time claim; T1: Jira data available) | 3 (T5 primary; T1 available via Jira) | 2 (8-week estimate; requires DBA team buy-in -- hidden constraint) | 24 | 33% T1-accessible, 67% T5 | **Investigate** -- verify lead time from Jira; assess DBA team alignment |
| 3 | **Fragmented observability extends MTTR** | 3 (T5: affects incident response; T1: MTTR data exists) | 3 (T5 primary; T1 via incident mgmt) | 2 (10-week estimate; scope risk is high) | 18 | 33% T1-accessible, 67% T5 | **Investigate** -- pull MTTR trends and tool fragmentation data |
| 4 | **No API contract standard causes integration fragility** | 2 (T5: "mess" is vague; frequency unclear) | 2 (T5 only; no T1 data path identified) | 1 (12 weeks; architectural change with adoption risk) | 4 | 0% T1, 100% T5 | **Deprioritize** -- evidence too weak and effort too high for this quarter |
| 5 | **Tribal knowledge dependency slows onboarding** | 2 (T5: "3 months" unverified; long-term impact) | 2 (T5 only; time-to-productivity hard to measure) | 4 (4 weeks; docs are lower-effort) | 16 | 0% T1, 100% T5 | **Deprioritize as platform initiative** -- reassign to eng managers + tech writers |

**Anti-gaming note:** All Impact and Confidence scores are capped because no problem has been validated with T1-T2 evidence. The top-ranked problem (CI/CD) scores highest not because of certainty but because it has the best combination of claimed breadth (150/200 engineers) and available T1 validation path (incident post-mortems). Any score would change with actual data.

**Recommendations (O-I-R-C-W Cascade)**

**Recommendation 1: Do Not Prioritize Yet -- Run a 1-Week Evidence Sprint First**

- **Observation** [T5]: All five problems are scored using team lead assertions (T5). No problem has T1-T2 validation. The current ICE ranking is a hypothesis, not a finding.
- **Implication**: Committing a quarter of platform capacity based on T5 evidence risks building for the loudest stakeholder rather than the most impactful problem. The difference between a correct and incorrect prioritization decision is ~$150K in engineering time (one quarter of a 4-person platform team).
- **Response**: Before committing to any initiative, run a 5-day evidence sprint: (1) Pull Jira lead times for DB provisioning requests -- validates Problem 2 (1 day, T1). (2) Review last 8 incident post-mortems for CI/CD and integration root causes -- validates Problems 1 and 4 (1 day, T1). (3) Pull MTTR data and correlate with observability tooling gaps -- validates Problem 3 (1 day, T1). (4) Survey 20 engineers across all 5 teams: "What wastes the most time in your development workflow?" Open-ended, not leading (2 days, T2). Owner: Platform PM. Timeline: 5 business days.
- **Confidence**: H -- all four data sources exist and are accessible. The survey requires coordination but not new tooling.
- **Watch**: If the survey reveals a problem that none of the five team leads raised, the entire prioritization changes. This is the "none of the above" scenario and it is common in internal platform work where team leads advocate for their own pain points but miss cross-cutting issues.

**Recommendation 2: Frame the Quarterly Decision as "Meta-Problem" vs. "Point Solution"**

- **Observation** [T5 + T6]: Problems 1, 2, and 4 share a meta-problem -- the platform lacks self-service primitives, forcing engineers into ticket-based workflows. Problems 3 and 5 are different in kind (tooling fragmentation and knowledge management).
- **Implication**: Solving the meta-problem (self-service platform capability) could address 3 of 5 requests partially, rather than solving 1 of 5 fully. This reframing changes the build vs. not-build decision for the VP Engineering -- who cares about aggregate eng velocity, not individual team requests.
- **Response**: After the evidence sprint, present two options to VP Engineering: (a) One deep solution for the highest-scoring problem, or (b) A self-service platform foundation that partially addresses Problems 1, 2, and 4 with a common infrastructure layer. Include validated ICE scores for both options. Owner: Platform PM. Timeline: Present in Week 2, after evidence sprint.
- **Confidence**: M -- the meta-problem framing is T6 (inferred pattern). It may not hold if the three problems are more different than they appear. The evidence sprint will clarify.
- **Watch**: If engineers in the survey do not describe "ticket-based workflows" or "waiting for other teams" as a top pain point, the meta-problem framing is wrong. Revert to point-solution prioritization.

**Assumption Registry**

| # | Assumption | Framework | Confidence | Evidence | Invalidation |
|---|---|---|---|---|---|
| 1 | Team leads' assertions about their teams' problems accurately reflect reality | All frameworks -- every problem definition is sourced from T5 | L | T5: team lead interviews only. No direct engineer input. | The 20-engineer survey (T2) reveals different top problems than what team leads reported. `[EVIDENCE-LIMITED]` |
| 2 | The five requests cover the most important platform problems | F8 Prioritization -- assumes the candidate set is complete | L | T5: only problems surfaced by team leads who submitted requests. Engineers who did not escalate may have worse problems. | Survey reveals a problem not on any team lead's list. `[EVIDENCE-LIMITED]` |
| 3 | ICE scores will meaningfully change after the evidence sprint | Recommendation 1 -- the sprint's value depends on data availability | M | T6: assumes incident post-mortems, Jira data, and MTTR data are accessible and granular enough to discriminate | If data systems are too coarse (e.g., incident post-mortems do not attribute root cause to CI/CD vs. other factors), the evidence sprint produces ambiguous results. |

**Adversarial Self-Critique**

**Weakness 1: The "Evidence Sprint First" Recommendation May Be a Delay Tactic.** From the stakeholders' perspective, the PM received five urgent requests and responded with "let me do a week of analysis before deciding." If any of the five problems is genuinely urgent -- for example, if CI/CD misconfiguration caused a production outage last week -- a 1-week delay has real cost. The skill biases toward evidence completeness over speed, which is correct on average but may be wrong in specific high-urgency situations. The PM should check: has any of these problems caused a Sev-1 incident in the last 30 days? If yes, that problem gets fast-tracked regardless of ICE score.

**Weakness 2: The Meta-Problem Framing May Be Intellectually Elegant but Operationally Unshippable.** Identifying that Problems 1, 2, and 4 share a "self-service primitives" meta-problem is an analytical insight. But building a "self-service platform foundation" in one quarter may be architecturally impossible -- it could require foundational infrastructure work that delivers value in Q3-Q4 but nothing shippable in Q2. The team leads need relief now, not an architectural vision. The analysis should have assessed whether the meta-solution is buildable within the quarter's constraints before recommending it as an option.

**Weakness 3: Internal Platform Prioritization Has Political Dynamics the Framework Underweights.** The Stakeholder Impact Matrix identifies the VP Engineering as the real decision-maker, but platform teams also depend on adoption. Building CI/CD templates that Team B champions but Team A ignores does not solve the platform's problem. The ICE framework scores impact by reach, but internal platform reach depends on voluntary adoption, which depends on the relationship between the platform team and each product team. A platform PM who picks CI/CD over DB provisioning may gain Team B's loyalty but lose Team A's trust and future adoption. The prioritization framework captures impact but not the second-order political consequences of the selection.

### What Changed
- **Five solutions were peeled back to five problems -- and a meta-problem emerged.** The generic output accepted the five feature requests at face value and scored them directly. The skill applied the Problem Definition Canvas and 5 Whys to each request, revealing that three of the five (DB provisioning, CI/CD, API gateway) share a root cause: the platform lacks self-service primitives. This reframing changes the entire quarterly decision.
- **Every score was tagged with evidence tier, exposing that all five problems are T5-only.** The generic output produced confident RICE scores (e.g., "CI/CD templates: Reach 150, Impact 2, Confidence 80%") without disclosing that every number was a team lead's assertion. The skill flagged that zero problems have T1-T2 validation, capping confidence and prescribing a 1-week evidence sprint before commitment.
- **Hidden stakeholders were identified.** The generic output addressed only the five requesting team leads. The skill identified the VP Engineering as the actual decision-maker (who should be the audience for the prioritization) and the DBA team as a potential blocker for the DB provisioning initiative -- a hidden constraint that would cause adoption failure even if the tool is built perfectly.
- **Proxy stakeholder problem was flagged explicitly.** The skill noted that all five requests come from team leads speaking for their engineers, and prescribed a direct engineer survey to check whether the leads' framing matches reality. The generic output took the team leads' framing as ground truth.
- **Adversarial self-critique identified three genuine risks**, including that the "evidence sprint" recommendation may function as a delay tactic when urgency is real, that the meta-problem framing may not be buildable in one quarter, and that internal platform prioritization has political adoption dynamics that ICE/RICE does not capture.
