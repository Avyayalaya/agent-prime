---
name: discovery-research
description: "Use when synthesizing user research, analyzing interview data, conducting discovery sprints, evaluating evidence quality across sources, or building research-backed feature hypotheses"
version: "1.3.0"
type: "codex"
tags: ["Research", "Discovery", "Evidence"]
created: "2026-02-20"
valid_until: "2026-08-20"
derived_from: "original"
tested_with: ["Claude Sonnet 4.5", "Claude Opus 4.6"]
license: "MIT"
---

## Purpose

Produce a **Research Synthesis Brief** -- a structured, evidence-graded synthesis of user research from multiple sources that separates validated findings from hypotheses, grades every claim by evidence quality, and connects insights to product decisions. The core question this skill answers: "What does the evidence actually say?" This is not a research plan or a methodology guide -- it is a reasoning engine that takes raw research inputs and produces findings a PM can act on, with explicit confidence levels and evidence gaps that drive the next research cycle.

## When to Use / When NOT to Use

**Use this skill when:**
- Synthesizing findings from multiple user interviews into a coherent picture
- Evaluating whether research evidence is strong enough to support a product decision
- Running a discovery sprint and need to structure findings as they accumulate
- Analyzing qualitative data (interview transcripts, support tickets, forum posts) for patterns
- Building research-backed feature hypotheses before committing engineering resources
- Resolving conflicting signals across different research sources (surveys say X, interviews say Y, behavioral data says Z)
- Assessing what you still do NOT know and where evidence is dangerously thin

**Do NOT use this skill when:**
- You need competitive market analysis (-> Competitive & Market Analysis skill -- that is market-side structural analysis, this is demand-side primary research)
- You need to design metrics or experiments (-> Metric Design & Experimentation skill -- that is measurement, this is evidence gathering and synthesis)
- You need to write a product specification (-> Spec Writing skill -- use this skill's output as INPUT to spec writing)
- You need a research plan template without existing data to synthesize (this skill processes research, it does not design research methodology from scratch)
- You need statistical analysis of quantitative experiment results (-> Metric Design & Experimentation skill)

**Anti-inputs (what this skill does NOT handle):**
- Research methodology design (sampling strategy, interview guide creation -> research ops)
- Statistical hypothesis testing (-> Metric Design & Experimentation skill)
- Competitive intelligence gathering (-> Competitive & Market Analysis skill)
- Product specification decisions (-> Spec Writing skill)
- Dashboard or visualization design (-> BI tooling)

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are not style preferences -- they are quality enforcement mechanisms derived from the systematic failure modes of research synthesis.

1. **Take positions. Never hedge with weasel words.** "Likely," "may," "could," and "seems" are banned. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"Users abandon the onboarding flow at the permissions step because the value proposition is unclear before data access is granted (H)"* not *"Users may be confused by the onboarding flow."*

2. **Per-cell evidence tier annotation is mandatory in all comparison and finding matrices.** Every cell in a finding summary, source comparison, or insight classification table must carry an inline evidence tier tag: `(T1)`, `(T2)`, `(T3)` etc. Where evidence is absent: `(T6: inferred)`. A matrix with untagged cells is incomplete.

3. **The O->I->R->C->W cascade applies to ALL research-driven recommendations**, not just final sections. Format: Observation [evidence tier] -> Implication [mechanism] -> Response [specific action] -> Confidence [H/M/L + assumption] -> Watch Indicator [observable signal].

4. **Begin with Framework Selection (Step 0b)** before applying any framework. Identify the research question type; select the 3-5 load-bearing frameworks; note which to skip. Applying all 8 frameworks to an interview analysis question inflates length and dilutes signal.

5. **Contradictions between sources are signal, not noise.** When two research sources reach different conclusions (e.g., surveys show high satisfaction but interviews reveal deep frustration), surface the contradiction explicitly and state which to weight more heavily and why, citing the evidence hierarchy.

6. **Flag time-sensitive claims.** Any claim based on research older than 6 months must carry `[POTENTIALLY STALE -- verify before presenting]`. Evidence tier and recency are independent -- a T2 finding from 18 months ago may be less useful than a T4 report from last month if the market has shifted.

7. **Flag thin-evidence conclusions.** If a key finding rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

8. **Every framework reference gets a one-line contextual explanation the first time it appears.** Not "Evidence Triangulation" but "Triangulation -- converging multiple independent sources to validate a finding. When three weak signals from different methods agree, confidence increases multiplicatively, not additively." The reader needs to know why this lens matters for *their* decision.

9. **The document must be navigable by someone who didn't create it.** Include a reading guide (by time and by role), a notation key, and layered depth. A VP should be able to read only the Executive Summary and act. A PM should be able to read through Key Findings and skip the Deep Analysis. The full document is for the researcher.

---

## Output Template (Mandatory Document Skeleton)

Every Research Synthesis Brief MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was skipped in Step 0b, note "Skipped -- not load-bearing for this research question" in that section.

```markdown
# Research Synthesis Brief: [Subject -- e.g., "Enterprise User Onboarding Pain Points"]

> **Date:** [YYYY-MM-DD] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which key findings need revalidation] | **Sources synthesized:** [count and types]

---

## Executive Summary

[5 sentences max. A VP reads only this and makes a decision. No framework names, no jargon, no evidence tier tags. Plain language a non-PM exec can act on. Final sentence = the recommended action in bold.]

---

## How to Read This Document

**What this is:** A research evidence synthesis -- not a research report. It grades evidence quality, separates validated findings from hypotheses, and connects insights to product decisions.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | The key finding + recommended action |
| **15 min** | Executive Summary + Key Findings (sections 1-3) | Core evidence-graded conclusions with source quality |
| **30 min** | Full document through Recommendations | Complete synthesis with framework analysis and evidence gaps |
| **Deep dive** | Everything including Appendix | Full source analysis, methodology notes, adversarial critique |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Summary | Recommendations, Assumption Registry | Everything in between |
| PM Lead | Executive Summary | Key Findings (sections 2-5), Research Gap Map, Recommendations | Deep framework sections |
| Researcher / Analyst | Full document in order | Source Quality Assessment, Cross-Source Contradictions, Adversarial Self-Critique | Nothing -- this is your primary artifact |
| Designer | Executive Summary | User Need Patterns (section 3), Behavioral vs. Stated Findings | Evidence methodology sections |
| Engineer | Executive Summary | Validated Requirements (section 6), Signal vs. Noise summary | Research methodology |

---

## Notation Key

**Confidence levels** -- applied to every finding:
- **H (>70% confident)** -- Multiple independent sources converge. Act on it.
- **M (40-70%)** -- Direction is probable but evidence is mixed or thin. Validate before committing resources.
- **L (<40%)** -- This is a hypothesis, not a finding. Do not act without further evidence.

**Evidence tiers** -- how we know what we claim to know (tagged inline as T1-T6):
- **T1** -- Direct behavioral data: usage analytics, A/B results, usage logs (strongest -- what users DO)
- **T2** -- Primary qualitative research: your own interviews (n>=5 with consistent patterns), usability tests
- **T3** -- Secondary research with disclosed methodology: academic studies, well-sampled surveys
- **T4** -- Industry reports and analyst commentary: Gartner, Forrester, market surveys
- **T5** -- Anecdotal evidence: individual interviews (<5), forum posts, support tickets, app reviews
- **T6** -- Inference / expert opinion without data (weakest -- treat as starting hypothesis)

**Insight classification:**
- **VALIDATED** -- Multiple independent sources converge (>=2 tiers, >=3 sources)
- **EMERGING** -- Single strong signal or consistent pattern from one source type
- **HYPOTHESIS** -- Inference from patterns; plausible but not directly observed
- **CONTRADICTED** -- Conflicting evidence across sources; resolution required

**Recommendation format** (O->I->R->C->W):
- **O**bservation -- What the evidence shows (with evidence tier)
- **I**mplication -- Why it matters (the mechanism)
- **R**esponse -- What to do (specific action + owner + timeline)
- **C**onfidence -- How sure we are (H/M/L + key assumption)
- **W**atch -- How to know if we're wrong (observable signal)

**Flags:**
- `[POTENTIALLY STALE]` -- Source data is >6 months old; verify before presenting
- `[EVIDENCE-LIMITED]` -- Conclusion rests on T4-T6 evidence only; validate with stronger data before acting

---

## Step 0: Context Fitness Check

Before selecting frameworks, verify that a Research Synthesis Brief is the right artifact for this question.

| Question | If Yes | If No |
|---|---|---|
| **Is the core question about what users need, want, or do?** | Proceed to Framework Selection | A Research Synthesis Brief is the wrong artifact. Consider: Competitive War Map (market structure question), Measurement Framework (instrumentation question), or Problem Framing (problem definition question). |
| **Do you have multiple research sources to synthesize?** | Full synthesis -- apply Evidence Triangulation and Source Quality Assessment | Single-source analysis. Flag prominently: "This brief synthesizes a single source type. All findings are tentative until triangulated with independent sources." Cap findings at M confidence unless behavioral data (T1). |
| **Is the research about current or prospective users?** | Standard evidence hierarchy applies | Flag: "Research subjects are not current users. Stated preferences carry even less weight than usual. Behavioral proxies (competitor usage, adjacent product data) should be weighted above interview responses." |
| **Has the product shipped, or is this pre-product research?** | T1 behavioral data may be available -- prioritize it | No T1 data exists. Highest available tier is T2 (interviews). Flag: "Pre-product research -- no behavioral validation available. All findings are directional until validated post-launch." |

**If any answer triggers a "No" path:** State this prominently at the top of the Executive Summary.

---

## Step 0b: Framework Selection

| Research question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Interview synthesis"] | [e.g., Interview Analysis, Evidence Triangulation, Insight Classification] | [e.g., Signal vs. Noise, Research Gap Mapping] | [e.g., "Competitive Discovery -- no competitor data available"] |

---

## 1. Source Inventory & Quality Assessment

| Source | Type | Sample | Methodology | Tier | Recency | Key Bias Risk |
|---|---|---|---|---|---|---|
| [e.g., "User interviews (n=12)"] | Qualitative | n=12, enterprise segment | Semi-structured, 45 min | T2 | [date] | Self-selection, social desirability |
| [e.g., "Product analytics"] | Behavioral | N=22K DAU | Full population | T1 | [date] | Survivorship (churned users absent) |
| [e.g., "Gartner report"] | Industry | Unknown sample | Undisclosed | T4 | [date] | Vendor influence, category bias |

**Source coverage assessment:** [Which user segments, use cases, or questions have NO evidence? Flag these as research gaps.]

---

## 2. Key Findings (Evidence-Graded)

**Finding 1: [Insight Header -- conclusion, not topic]**
- **Classification:** VALIDATED / EMERGING / HYPOTHESIS / CONTRADICTED
- **Confidence:** H / M / L
- **Evidence:** [Source A (TX), Source B (TX), Source C (TX)]
- **Detail:** [2-3 sentences explaining the finding with specifics]
- **Implication:** [What this means for product decisions]

**Finding 2: [Insight Header]**
[Same structure]

**Finding 3: [Insight Header]**
[Same structure]

[Continue for all key findings. Minimum 5, maximum 12.]

---

## 3. User Need Patterns

| Need | Frequency (how many sources) | Intensity (how strongly expressed) | Behavioral Evidence? | Classification | Confidence |
|---|---|---|---|---|---|
| [need] | X/Y sources | High/Med/Low | Yes (T1) / No | VALIDATED/EMERGING/HYPOTHESIS | H/M/L |
| [need] | | | | | |

**Frequency vs. Intensity Matrix:**

| | Low Frequency | High Frequency |
|---|---|---|
| **High Intensity** | Niche but critical -- potential power-user feature or underserved segment | Core unmet need -- high-priority opportunity |
| **Low Intensity** | Noise -- deprioritize | Table stakes -- expected but not differentiating |

---

## 4. Stated vs. Revealed Preferences

| What Users SAY | What Users DO | Gap | Implication |
|---|---|---|---|
| [stated preference (TX)] | [observed behavior (TX)] | [description of gap] | [what the gap means for product decisions] |

**Evidence hierarchy reminder:** Behavioral data (T1) > Usability tests (T2) > Surveys (T3) > Interviews (T2-T5 depending on n) > Focus groups (T5). When stated and revealed preferences conflict, behavioral data wins unless you can identify a specific reason the behavioral data is misleading (e.g., the current product forces a behavior that doesn't reflect preference).

---

## 5. Signal vs. Noise Assessment

| Signal Candidate | Source | Frequency | Convergence | Structural? | Verdict |
|---|---|---|---|---|---|
| [signal] | [source (TX)] | Recurring/One-off | Converges with X other signals / Isolated | Structure change / Weather | SIGNAL / NOISE / INVESTIGATE |

---

## 6. Evidence Triangulation Summary

| Finding | Source 1 | Source 2 | Source 3 | Convergence? | Confidence After Triangulation |
|---|---|---|---|---|---|
| [finding] | [source (TX): supports/contradicts/silent] | [source (TX): ...] | [source (TX): ...] | Strong/Partial/Weak/Contradicted | H/M/L |

---

## 7. Research Gap Map

| Question We Cannot Answer | Why It Matters | What Evidence Would Answer It | Recommended Method | Priority |
|---|---|---|---|---|
| [unanswered question] | [product decision it blocks] | [what T1/T2 evidence would look like] | [interview/survey/analytics/prototype test] | Critical/High/Medium |

---

## 8. Cross-Source Contradictions

| Contradiction | Source A says | Source B says | Resolution / Which to weight |
|---|---|---|---|
| [e.g., "Satisfaction vs. churn"] | [Surveys: 85% satisfied (T3)] | [Analytics: 40% churn in 90 days (T1)] | [Behavioral data (T1) wins. Survey satisfaction likely reflects switching cost tolerance, not genuine satisfaction. Investigate further.] |

---

## 9. Competitive Discovery Findings (if applicable)

| Competitor | Source | Unmet Need Identified | Evidence Quality | Implication for Our Product |
|---|---|---|---|---|
| [competitor] | [reviews/forums/job postings (TX)] | [what their users want but don't get] | T4/T5 | [how we could address this] |

---

## 10. Strategic Recommendations (O->I->R->C->W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What the evidence shows]
- **Implication**: [Why it matters -- the mechanism]
- **Response**: [Specific action + owner + timeline]
- **Confidence**: [H/M/L] -- assumes [key assumption]
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

## Assumption Registry

| # | Assumption | Finding it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | | | H/M/L | (TX) | |
| 2 | | | H/M/L | (TX) | |
| 3 | | | H/M/L | (TX) | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[Steelmanned argument against the synthesis. What assumption is being made? What evidence would disprove it? Scenario where this recommendation is catastrophically wrong.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| [Observable event] | [Which findings break] | [When to check] |

---

## Sources

[All sources cited in the synthesis, with evidence tier and date.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Skipped -- [reason]" and move on.
2. **Every table cell with a finding or claim must have an evidence tier tag** -- `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "User Need Analysis") with insight headers (e.g., "Users Need Real-Time Collaboration, Not Better Dashboards") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **Findings are ordered by confidence, not by source.** Lead with VALIDATED findings, then EMERGING, then HYPOTHESIS. CONTRADICTED findings get their own section.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology -- not merely referenced. A PM using this skill produces research synthesis that requires these frameworks; without them, the output degrades to a summary of interview notes.

### Framework 1: Evidence Triangulation

The core analytical engine for validating findings across multiple sources. Triangulation is not "did three people say it?" -- it is "do three *independent methods* converge on the same conclusion?"

**The Triangulation Principle:**
A finding supported by a single source type is an observation. A finding supported by two independent source types is probable. A finding supported by three independent source types with different bias profiles is as close to validated as qualitative research gets.

**Why independence matters:** Five interviews from the same customer segment, conducted by the same researcher, with the same interview guide, are one source -- not five. Independence requires: different methods (interview vs. analytics vs. survey), different populations, or different time periods.

**Triangulation Types:**

| Type | Method | When to Use | Strength |
|---|---|---|---|
| **Method triangulation** | Same question, different research methods (interview + survey + analytics) | Default -- always try this first | Different methods have different biases; convergence across methods is the strongest validation |
| **Source triangulation** | Same method, different populations (enterprise users + SMB users + churned users) | When you need to test whether a finding generalizes | Reveals segment-specific vs. universal patterns |
| **Temporal triangulation** | Same question, different time periods (Q1 interviews vs. Q3 interviews) | When recency or trend direction matters | Distinguishes stable needs from transient reactions |
| **Investigator triangulation** | Same data, different analysts | When the finding is high-stakes and interpretation matters | Reduces single-analyst bias in qualitative coding |

**Convergence Scoring:**

| Convergence Level | Definition | Confidence Impact | Action |
|---|---|---|---|
| **Strong** | 3+ independent source types agree, no contradictions | Upgrade finding to H confidence | Act on this finding |
| **Partial** | 2 source types agree, 1 silent or ambiguous | M confidence | Usable for planning; validate before major commitment |
| **Weak** | 1 source type only, or 2 sources but same method | L confidence | Hypothesis only; design research to validate |
| **Contradicted** | Sources actively disagree | Flag explicitly | Do NOT average. Investigate why sources disagree -- the disagreement is often the most valuable insight |

**The "3 Weak Signals" Question:**
When do 3 weak signals (T5) equal 1 strong signal? **Only when they are independent.** Three forum posts from the same community are one signal repeated three times. Three signals from different channels (forum + support ticket + sales call note), about the same problem, from users in different segments -- that is genuine convergence.

When do 3 weak signals NOT equal 1 strong signal? When they share a common cause. If a tech blogger wrote about a problem, and then three users cited the same blog post in support tickets, the "three signals" are actually one signal amplified. **Always trace weak signals to their origin to check for shared roots.**

**Output format -- Triangulation Matrix:**
```
| Finding | Interviews (T2) | Analytics (T1) | Survey (T3) | Support (T5) | Convergence | Confidence |
|---------|:---:|:---:|:---:|:---:|---|---|
| [Finding 1] | Supports (n=8/12) | Supports (funnel data) | Silent | Supports (47 tickets) | Strong (3 types) | H |
| [Finding 2] | Supports (n=4/12) | Contradicts | Silent | Silent | Contradicted | Investigate |
```

---

### Framework 2: Interview Analysis Protocol

The systematic methodology for extracting reliable insights from qualitative interviews. The challenge: interviews are rich in detail and poor in reliability. This protocol converts unstructured qualitative data into structured, gradable evidence.

**The Core Problem with Interviews:**
Interviews are the most commonly used and most commonly misinterpreted research method. Users are unreliable narrators of their own behavior, preferences, and needs. They will tell you what they think you want to hear (social desirability bias), what sounds rational rather than what they actually did (post-hoc rationalization), and what happened most recently rather than what matters most (recency bias). Despite this, interviews are irreplaceable for discovering *why* behind behavioral patterns.

**Coding Protocol (Pattern Extraction from Transcripts):**

| Step | Action | Purpose |
|---|---|---|
| 1. **Open coding** | Read transcripts without a framework. Mark every statement that could be an insight, a need, a frustration, or a behavior. | Avoid confirmation bias -- let the data speak before imposing categories |
| 2. **Axial coding** | Group open codes into categories. Merge similar codes. Name the categories by the underlying need, not the surface statement. | "I want a dark mode" and "the screen hurts my eyes" are the same code: visual comfort need |
| 3. **Frequency count** | Count how many independent interviewees raised each coded category. | Frequency = breadth of need. Minimum 3/n to flag as a pattern (not a one-off) |
| 4. **Intensity scoring** | Rate each mention by emotional intensity: casual mention vs. unprompted frustration vs. "I would switch products for this." | Intensity = depth of need. A need mentioned by 2 users with extreme intensity may matter more than a need mentioned by 8 users in passing |
| 5. **Verbatim extraction** | Pull 2-3 direct quotes per coded category. Preserve exact language, not your paraphrase. | Verbatims are T2 evidence. Your interpretation is T6. Keep both, label both. |
| 6. **Interpretation layer** | Now overlay your interpretation. For each category: what is the underlying job-to-be-done? What is the user actually trying to accomplish? | Separate the data layer (verbatims, frequencies) from the interpretation layer (your inference about what it means). Readers should be able to disagree with your interpretation while accepting your data. |

**Frequency vs. Intensity Decision Table:**

| | Low Intensity (casual mention) | High Intensity (unprompted, emotional, "would switch for this") |
|---|---|---|
| **High Frequency (>=50% of n)** | Table stakes need -- users expect it but won't pay extra for it. Build it, but it won't differentiate. | Core unmet need -- highest priority. This is where product value lives. |
| **Low Frequency (<30% of n)** | Background noise -- deprioritize unless segment-specific analysis reveals a cluster. | Power-user or niche signal -- investigate whether this represents an underserved segment. Small n + high intensity = potential beachhead market. |

**Verbatim vs. Interpreted Claims:**

| Type | Example | Evidence Tier | How to Use |
|---|---|---|---|
| **Verbatim** | "I spend 45 minutes every Monday manually copying data from Salesforce into our dashboard." | T2 (if n>=5 with consistent pattern) or T5 (if isolated) | Present as primary evidence. Let the reader draw their own conclusion. |
| **Interpreted** | "Users experience significant friction in the data integration workflow." | T6 (your inference) | Present as your interpretation, explicitly labeled. Tie back to the verbatims that support it. |
| **Hybrid (best practice)** | "Users report spending 30-60 minutes per week on manual data integration (n=7/12 interviewees, unprompted). This suggests the integration workflow is a primary source of friction, not a minor inconvenience." | T2 + T6 (separated) | Data sentence is T2. Interpretation sentence is T6. Both are useful; conflating them is not. |

**Sample Size Guidance for Interview Research:**

| n | What You Can Claim | What You Cannot Claim |
|---|---|---|
| **1-4** | Individual perspectives; hypothesis generation | Patterns, prevalence, segment-level conclusions |
| **5-8** | Emerging patterns (if 60%+ consistency); directional themes | Definitive prevalence; confidence above M |
| **9-15** | Validated qualitative patterns (if 60%+ consistency); segment-level themes with careful scoping | Statistical prevalence; quantitative generalization |
| **16-30** | Robust qualitative saturation (when new interviews stop producing new codes); strong segment comparisons | Population-level statistics (that still requires quantitative methods) |
| **30+** | Thematic saturation is almost certain; quasi-quantitative prevalence claims become defensible | Nothing changes about the method's core limitation: you still cannot claim "X% of users feel Y" from interviews alone |

**Critical rule:** Never cite "12 out of 15 interviewees said X" as if it means "80% of users feel X." Interview samples are never representative in the statistical sense. The correct framing: "A clear pattern emerged across 12 of 15 interviewees, suggesting this is a widespread need in the [segment] population. Quantitative validation recommended before sizing the opportunity."

---

### Framework 3: Research Quality Assessment

The systematic methodology for evaluating whether a research source is trustworthy enough to inform product decisions. Not all evidence is created equal, and mixing T1 behavioral data with T5 anecdotes without distinguishing them is the most common research synthesis failure.

**Source Evaluation Rubric:**

| Dimension | Questions to Ask | Scoring |
|---|---|---|
| **Sample** | How many subjects? How selected? Representative of target population? | n>=30 quantitative = adequate; n>=8 qualitative with saturation = adequate; convenience sample = flag bias risk |
| **Methodology** | Disclosed? Replicable? Standard method or novel? Controls for known biases? | Disclosed + standard = trustworthy. Undisclosed = T4 at best. Novel without validation = treat as exploratory. |
| **Bias detection** | Who funded it? Who conducted it? What incentives exist to reach a specific conclusion? | Vendor-funded research about their own product = T5 regardless of methodology. Academic with disclosed funding = T3. |
| **Recency** | When was the data collected? Has the market changed since? | <6 months = current. 6-12 months = usable with `[POTENTIALLY STALE]`. >12 months = historical context only unless nothing has changed. |
| **Relevance** | Does this research study the same user population, use case, and context as your product? | Same population + same context = directly applicable. Adjacent population or different context = inference required (downgrade one tier). |

**The Relevance Trap:**
A beautifully designed, large-sample study about enterprise SaaS onboarding is T3 evidence for your enterprise SaaS onboarding question. The same study is T4-T5 evidence for your consumer mobile onboarding question, because the populations and contexts differ enough that findings may not transfer. **Always evaluate relevance to YOUR specific context, not just research quality in the abstract.**

**Source Quality Decision Table:**

| Quality Dimension | Strong | Adequate | Weak | Disqualifying |
|---|---|---|---|---|
| Sample size (quantitative) | n>=1000 | n>=100 | n=30-99 | n<30 |
| Sample size (qualitative) | n>=15 with saturation | n=8-14 | n=5-7 | n<5 (anecdotal) |
| Methodology disclosure | Full methodology + data available | Methodology described | "Survey" or "interviews" with no detail | No methodology mentioned |
| Bias risk | Independent researcher, no conflicts | Funded research with disclosed conflict | Vendor-funded | Vendor self-report as evidence |
| Recency | <6 months | 6-12 months | 12-24 months | >24 months without `[STALE]` flag |
| Relevance | Same population, same context | Same population, different context | Different population, similar context | Different population AND context |

**Tier Assignment Protocol:**
1. Start with the source type's default tier (T1-T6 from Evidence Standards below)
2. Apply quality assessment: strong on all dimensions = keep tier. Weak on any critical dimension (sample, methodology, relevance) = downgrade one tier.
3. Apply recency: >12 months = downgrade one tier or add `[POTENTIALLY STALE]`.
4. Apply relevance: different context = downgrade one tier.
5. Floor: No source drops below T6 regardless of downgrades. But T6 evidence should never be the sole basis for a finding.

---

### Framework 4: Signal vs. Noise Filter

The systematic methodology for distinguishing genuine user needs from noise: stated preferences that don't predict behavior, outlier opinions amplified by recency, feature requests that mask deeper problems, and the ever-present recency bias that makes the latest interview dominate all previous data.

**The Five-Filter Test:**

Apply these five filters to every candidate insight before elevating it to a finding:

| Filter | Question | If Yes -> Signal | If No -> Noise (or Investigate) |
|---|---|---|---|
| 1. **Frequency** | Has this appeared in >=3 independent sources? | Pattern, not one-off | One-off unless high-intensity (check Filter 2) |
| 2. **Intensity** | Did users express this unprompted, with emotion, or as a dealbreaker? | Even at low frequency, investigate as niche signal | Low-intensity + low-frequency = deprioritize |
| 3. **Behavioral corroboration** | Is there behavioral evidence (T1) that supports the stated need? | Validated signal | Stated-only. May be aspiration, not need. Flag for behavioral validation. |
| 4. **Structural significance** | Does this represent a change in market *structure* (durable) or market *weather* (temporary)? | Structural = high strategic weight | Weather = monitor but don't over-invest |
| 5. **Independence** | Are the sources genuinely independent, or could they share a common origin? | Independent convergence | Amplified signal -- trace to origin before counting |

**Common Noise Patterns:**

| Noise Type | What It Looks Like | Why It Fools You | How to Detect |
|---|---|---|---|
| **Feature request as proxy** | "I need a Gantt chart view" | The user is expressing a need for project visibility, not literally requesting Gantt charts. The request masks the job-to-be-done. | Ask "What would you do with that?" until you reach the underlying need. The fifth "why" reveals the real job. |
| **Recency bias** | The last 3 interviews all mentioned X; it must be critical | The last interviews are freshest in memory. The 20 previous interviews that didn't mention X are forgotten. | Always count frequency across the FULL dataset, not just recent additions. Weight by temporal triangulation, not by memory. |
| **Social desirability** | "I would definitely pay more for that feature" | In interviews, users overstate willingness to pay, understate price sensitivity, and agree with the interviewer's implied preferences. | Stated willingness to pay is T5 evidence. Only revealed behavior (T1) validates pricing. Never set price based on interview responses alone. |
| **Expert user bias** | "The API should support GraphQL" | Power users who agree to interviews are not representative of the full user base. Their needs are real but may be niche. | Segment findings by user sophistication. If a need only appears in expert-user interviews, it's a segment signal, not a market signal. |
| **Survivorship bias** | "Our users love the product!" | You're only interviewing users who stayed. The 40% who churned are absent from your research. | Include churned users and non-adopters in the research plan. If your sample is only active users, flag: "Survivorship bias: findings reflect retained users only." |

**The Noise Escalation Ladder:**
Not all noise should be discarded. Some noise deserves monitoring:

| Action | When |
|---|---|
| **Discard** | Failed all 5 filters. One person, one time, no corroboration, no structural significance. |
| **Monitor** | Failed 3-4 filters but passed one with high intensity or structural significance. Add to watch list for the next research cycle. |
| **Investigate** | Passed 2-3 filters. Not enough evidence to act, but too much to ignore. Design a targeted research probe. |
| **Elevate to Finding** | Passed 4-5 filters. This is signal. Classify and grade per the Insight Classification framework. |

---

### Framework 5: Insight Classification

The taxonomy for categorizing research findings by their evidence strength and actionability. Not all insights are created equal, and treating a hypothesis with the same weight as a validated finding is the core failure mode of research synthesis.

**Classification Taxonomy:**

| Classification | Definition | Evidence Requirement | Action Permission | Visual Marker |
|---|---|---|---|---|
| **VALIDATED** | Multiple independent sources converge; finding has been triangulated across methods | >=2 evidence tiers, >=3 independent sources, no unresolved contradictions | Act on this finding. Use for resource allocation, roadmap decisions, spec requirements. | Solid -- build on it |
| **EMERGING** | Single strong signal or consistent pattern from one source type; promising but not yet triangulated | 1 evidence tier with strong signal (e.g., 8/12 interviewees, or clear behavioral data) | Plan for this finding. Include in roadmap discussions but validate before committing major resources. | Directional -- plan with it |
| **HYPOTHESIS** | Inference from patterns; plausible interpretation of indirect evidence but not directly observed | Logical inference from validated or emerging findings; no direct evidence | Test this finding. Design a specific research probe or experiment. Do not build features based on hypotheses alone. | Unvalidated -- test it |
| **CONTRADICTED** | Conflicting evidence across sources; the finding status is genuinely uncertain | Two or more sources actively disagree; resolution requires additional research | Investigate, do not act. The contradiction itself is the most important finding -- it reveals something unexpected about user behavior or market structure. | Conflicted -- investigate it |

**Classification Decision Tree:**

```
Is there direct behavioral evidence (T1)?
  YES -> Is it corroborated by another source type?
    YES -> VALIDATED (H confidence)
    NO  -> EMERGING (M confidence) -- strong but single-method
  NO  -> Is there qualitative evidence from n>=5?
    YES -> Are there contradicting sources?
      YES -> CONTRADICTED -- investigate the gap
      NO  -> Is there a second independent source type that agrees?
        YES -> VALIDATED (M confidence, upgrade to H when behavioral data confirms)
        NO  -> EMERGING (M confidence)
    NO  -> Is the inference logically derived from validated/emerging findings?
      YES -> HYPOTHESIS (L confidence)
      NO  -> Not a finding. Discard or file as speculation.
```

**Classification Upgrade/Downgrade Triggers:**

| Trigger | Classification Change |
|---|---|
| New behavioral data (T1) confirms an EMERGING finding | EMERGING -> VALIDATED |
| A contradicting source appears for a VALIDATED finding | VALIDATED -> CONTRADICTED (investigate immediately) |
| Time passes without revalidation (>6 months) | Any classification gets `[POTENTIALLY STALE]` |
| The user population changes (new segment, new market) | All classifications from old population get relevance downgrade |
| An EMERGING finding fails a targeted validation test | EMERGING -> discard or HYPOTHESIS |

---

### Framework 6: Demand-Side Analysis

The framework for understanding what users actually do versus what they say -- the hierarchy of evidence for user needs, and how to resolve the inevitable conflicts between different evidence types.

**The Evidence Hierarchy for User Needs:**

| Rank | Evidence Type | What It Tells You | Reliability | Common Failure |
|---|---|---|---|---|
| 1 | **Behavioral data (analytics)** | What users actually do at scale | Highest -- behavior doesn't lie (but can be misinterpreted) | Observing behavior without understanding context. Users click X -- but why? |
| 2 | **Usability tests** | What users do in controlled settings with a specific task | High -- observed behavior, but in artificial conditions | Artificial task framing changes behavior. "Find the settings page" != natural navigation. |
| 3 | **Surveys (well-sampled)** | What users say they do and prefer, at scale | Moderate -- scale offsets self-report bias somewhat | Leading questions, response bias, survivorship in sample |
| 4 | **Interviews (n>=5)** | Why users do what they do; underlying motivations and frustrations | Moderate -- depth offsets small sample, but self-report bias remains | Social desirability, post-hoc rationalization, interviewer influence |
| 5 | **Focus groups** | How users talk about needs in social settings | Low-moderate -- group dynamics distort individual preferences | Dominant personalities drive consensus; social desirability amplified |
| 6 | **Expert opinion** | What experienced practitioners believe users need | Low -- expert prediction of user behavior is notoriously unreliable | Curse of knowledge: experts cannot accurately simulate non-expert experience |

**The Stated vs. Revealed Preference Gap:**
The most important and most underappreciated dynamic in user research. Users will tell you one thing and do another -- not because they're lying, but because:
- They don't have accurate introspective access to their own decision-making
- They describe their idealized self, not their actual self
- They anchor on recent experiences rather than stable preferences
- They want to be helpful and will agree with your implied hypothesis

**Resolution Protocol When Stated != Revealed:**

| Situation | Resolution | Rationale |
|---|---|---|
| Users SAY they want feature X; behavioral data shows they never use similar features | Weight behavioral data. Investigate why the gap exists (awareness? discoverability? mismatch between stated and actual job?) but do NOT build X based on stated preference alone. | What users do is more reliable than what users say, with rare exceptions. |
| Users SAY they're satisfied; behavioral data shows high churn | Weight behavioral data. Survey satisfaction likely reflects switching cost tolerance or question framing, not genuine satisfaction. | Satisfaction surveys are measuring something, but it may not be satisfaction. |
| Users SAY they wouldn't pay for X; behavioral data shows they use X heavily | Pricing research via stated preference is deeply unreliable. Use willingness-to-pay experiments (Van Westendorp, Conjoint) or behavioral pricing tests instead. | Stated price sensitivity is always higher than revealed price sensitivity. |
| Users SAY nothing about a problem; behavioral data shows a massive drop-off at a specific step | The absence of complaint is not the absence of a problem. Users who silently churn never appear in interview or survey data. | Behavioral data catches the silent majority that qualitative research misses. |

**Demand-Side Analysis Checklist:**
- [ ] Behavioral data reviewed BEFORE qualitative interpretation
- [ ] Churned/non-adopted users included in research sample (not just active users)
- [ ] Stated preferences checked against behavioral evidence where available
- [ ] Frequency and intensity scored independently (high frequency + low intensity = table stakes, not opportunity)
- [ ] The "do nothing" competitor identified (inertia is often the largest competitor)
- [ ] Non-consumers identified (people who COULD use the product but don't -- why?)

---

### Framework 7: Research Gap Mapping

The systematic identification of what you do NOT know and where the evidence is dangerously thin. This is the most commonly skipped and highest-value step in research synthesis. A research synthesis that only reports what you learned, without mapping what you failed to learn, gives false confidence.

**Gap Classification:**

| Gap Type | Definition | Risk Level | Example |
|---|---|---|---|
| **Critical gap** | A product decision is being made with no supporting evidence | Highest -- decision may be wrong | "We're building for enterprise, but all interviews were SMB users" |
| **Blind spot** | A user segment, use case, or question was not included in research scope | High -- you don't know what you don't know | "We never talked to churned users about why they left" |
| **Thin evidence** | Evidence exists but is single-source or low-tier | Moderate -- directional but not validated | "Only 2 interviewees mentioned this need, but both were very intense about it" |
| **Stale evidence** | Evidence was valid but is now outdated | Moderate -- may no longer reflect reality | "This finding is from a study 14 months ago; the product has changed significantly" |
| **Contradicted evidence** | Evidence exists but sources disagree | High -- acting on either side carries risk | "Survey says high satisfaction; churn data says the opposite" |

**Gap Mapping Protocol:**

1. **List every product decision** the research synthesis is intended to inform
2. For each decision, identify the **minimum evidence** required (what tier, what sample, what method)
3. Compare required evidence against **available evidence**
4. Flag every gap where available evidence falls short of required evidence
5. Prioritize gaps by **decision urgency x evidence shortfall**

**Gap Priority Matrix:**

| | Decision in <30 days | Decision in 30-90 days | Decision in >90 days |
|---|---|---|---|
| **No evidence at all** | CRITICAL -- halt decision or commission rapid research | HIGH -- schedule research sprint | MEDIUM -- add to next research cycle |
| **Single-source / low-tier evidence** | HIGH -- can proceed with explicit risk flag | MEDIUM -- schedule validation | LOW -- monitor |
| **Evidence exists but stale** | HIGH -- rapid re-validation needed | MEDIUM -- schedule re-validation | LOW -- flag for next cycle |

**Output format -- Research Gap Map:**
```
| Gap | Type | Decision It Blocks | Priority | Recommended Action | Timeline |
|-----|------|-------------------|----------|-------------------|----------|
| No churned user data | Blind spot | Churn reduction strategy | CRITICAL | Run 8-10 churn interviews | 2 weeks |
| Enterprise needs from SMB sample | Thin evidence | Enterprise roadmap | HIGH | 5 enterprise interviews | 3 weeks |
| Pricing sensitivity | Critical gap | Pricing model | HIGH | Van Westendorp survey (n=200) | 4 weeks |
```

---

### Framework 8: Competitive Discovery

What you can learn about unmet user needs from competitor user bases, without conducting primary research on your own users. This framework treats competitor data as a research source -- one with specific strengths and specific biases.

**Competitive Research Sources and Their Evidence Value:**

| Source | What It Reveals | Evidence Tier | Bias to Watch |
|---|---|---|---|
| **App store / G2 / Capterra reviews** | Unmet needs expressed by competitor users; common complaints; feature gaps | T5 (individual reviews) upgrading to T4 (if pattern across 50+ reviews) | Selection bias -- reviewers are extremes (very happy or very unhappy). The silent middle is absent. |
| **Competitor support forums** | Real usage problems at scale; workarounds users build; feature requests with community upvotes | T5 (individual posts) upgrading to T4 (if consistent across 20+ threads) | Power user bias -- forum participants are sophisticated. Their needs may not represent the mainstream. |
| **Competitor job postings** | Where competitors are investing (product areas, capabilities, markets) | T4 (signal of strategy) | Postings reflect intended investment, not guaranteed execution. 6-12 month leading indicator. |
| **Competitor documentation and changelogs** | Product direction, feature maturity, technical architecture decisions | T4 | What they ship reveals more than what they announce. But documentation may lag actual product. |
| **Social media and community discussion** | Sentiment, unmet expectations, emerging needs | T5 | Echo chamber effects. A vocal minority can dominate perception. Always check for independence. |
| **Sales team anecdotes about competitor mentions** | Which competitors appear in deals; what customers say about them | T5 | Sales attribution bias (see Win/Loss in Competitive Analysis skill). Hypothesis generation only. |

**Competitive Discovery Protocol:**

1. **Select 3-5 competitors** relevant to your user segment
2. For each competitor, **review 50+ recent reviews** (last 6 months) on G2, Capterra, App Store, or equivalent
3. **Code complaints** using the same open coding protocol as Interview Analysis (Framework 2)
4. **Identify patterns** across competitors -- if multiple competitors' users complain about the same thing, this is likely a category-level unmet need, not a competitor-specific problem
5. **Cross-reference** with your own user research -- do your users express the same needs?
6. **Flag** needs that appear in competitor research but are ABSENT from your own research -- these are potential blind spots

**The Non-Consumer Signal:**
The most valuable competitive discovery finding is not about competitor users -- it is about people who evaluated competitors and chose NONE of them. What are their objections? Why did they stay with the status quo (spreadsheets, manual processes, "doing nothing")? These non-consumers represent the largest untapped opportunity, and their reasons for non-adoption reveal the most fundamental unmet needs.

**Where to find non-consumer signals:**
- Reddit/community threads: "I tried [category] tools and went back to spreadsheets because..."
- Quora/StackExchange: "Is there a [category] tool that actually..."
- Support forums: "I wanted to use [product] but couldn't because..."
- Job postings: if companies are hiring for manual roles that your product should automate, non-adoption is the signal

---

## Evidence Standards

### Evidence Quality Tiers

| Tier | Source Type | Weight | Example | Key Limitation |
|---|---|---|---|---|
| **Tier 1** | Direct behavioral data (what people DO) | Highest | Usage analytics, A/B results, usage logs, conversion funnels | Shows what, not why. Survivorship bias (churned users disappear). |
| **Tier 2** | Primary qualitative research (your own, n>=5 with consistent patterns) | High | Your user interviews, usability tests, diary studies | Self-report bias, small sample, interviewer influence. Strong on "why," weak on "how many." |
| **Tier 3** | Secondary research with disclosed methodology | Medium-High | Academic studies, well-sampled industry surveys, published case studies with methodology | May not match your population or context. Check relevance. |
| **Tier 4** | Industry reports and analyst commentary | Medium | Gartner, Forrester, IDC, analyst blog posts with reasoning | Often vendor-influenced, category-biased, slow to update. Useful for sizing, less for insight. |
| **Tier 5** | Anecdotal evidence | Low-Medium | Individual interviews (n<5), forum posts, support tickets, app reviews, sales anecdotes | Not representative. Hypothesis generation only. Never for structural conclusions. |
| **Tier 6** | Inference / expert opinion without data | Low | PM intuition, first-principles reasoning, "I think users want..." | The most common evidence type in product decisions and the least reliable. Always label explicitly. |

**Triangulation Rule:** No research finding used for a product decision should rest on a single evidence tier. Minimum 2 tiers, ideally 3.

**Staleness Rule:** For every finding, note the source date. If no source newer than 6 months can be identified, flag as `[POTENTIALLY STALE]`. Evidence tier and recency are independent -- a T1 data point from 18 months ago may be less useful than a T3 study from last month if the market has shifted.

**Annotation Convention:** Use inline tags throughout -- not just footnotes or end-of-section summaries. Per-cell annotation in matrices: `Validated (T2, n=8)` or `Adequate (T4: Gartner)` or `Inferred (T6)`. A trailing evidence table supplements but does not substitute for inline tagging.

### The Evidence Escalation Ladder

When current evidence is insufficient for a decision, escalate:

| Current Evidence | Insufficient Because | Escalation Action | Timeline |
|---|---|---|---|
| T6 (opinion only) | No data of any kind | Run 5 user interviews (-> T2) or pull behavioral data (-> T1) | 1-2 weeks |
| T5 (anecdotal, n<5) | Too few sources to establish pattern | Expand to n>=8 interviews OR add behavioral data analysis | 2-3 weeks |
| T4 (industry report) | Not specific to your users/context | Run primary research with your users to validate | 2-4 weeks |
| T3 (secondary research) | Different population or context | Run primary research (interviews + analytics) with your specific users | 2-4 weeks |
| T2 (qualitative only) | No behavioral corroboration | Add T1 behavioral analysis to triangulate | 1-2 weeks |
| T1 (behavioral only) | Shows "what" but not "why" | Add T2 qualitative to explain behavioral patterns | 2-3 weeks |

---

## Application Method

### Step 0b: Route to Framework Subset

After passing the Context Fitness Check, identify the research question type and select load-bearing frameworks. Applying all 8 frameworks to every question inflates length, buries signal, and applies wrong-context frameworks.

| Question Type | Prompt Signals | Primary Frameworks | Frameworks to Skip |
|---|---|---|---|
| **Interview synthesis** | "analyze these interviews," "what did users say," "interview findings" | F2 (Interview Analysis), F1 (Triangulation), F5 (Insight Classification) | F8 (Competitive Discovery): skip unless competitor mentions appeared in interviews |
| **Multi-source synthesis** | "synthesize research," "combine findings," "what does the evidence say" | F1 (Triangulation), F3 (Research Quality), F5 (Insight Classification), F4 (Signal vs. Noise) | None -- this is the full-stack question |
| **Evidence evaluation** | "is this evidence strong enough," "can we act on this," "should we trust this data" | F3 (Research Quality), F1 (Triangulation), F7 (Gap Mapping) | F2 (Interview Analysis): skip unless evaluating interview data specifically |
| **Feature hypothesis validation** | "do users need X," "should we build X," "is there demand for X" | F4 (Signal vs. Noise), F6 (Demand-Side), F1 (Triangulation), F5 (Insight Classification) | F8 (Competitive Discovery): add only if competitive context matters |
| **Discovery sprint** | "what do we know," "what do we still need to learn," "research sprint" | All -- tier explicitly: F1, F5, F7 primary; rest supporting | None -- but label tiers |
| **Competitive user needs** | "what do competitor users want," "competitive research," "market needs" | F8 (Competitive Discovery), F1 (Triangulation), F4 (Signal vs. Noise) | F2 (Interview Analysis): skip unless you have your own interviews too |
| **Pre-decision evidence check** | "do we have enough evidence," "what's missing," "evidence gaps" | F7 (Gap Mapping), F3 (Research Quality), F1 (Triangulation) | F2, F6, F8: skip unless gaps are in those specific areas |

Apply primary frameworks fully. Apply supporting frameworks at reduced depth unless they surface a conflicting signal -- in which case surface the contradiction explicitly.

### Quick Version (10 steps for experienced practitioners)

0a. **Context Fitness Check** -- Verify a Research Synthesis Brief is the right artifact. Check: demand-side question? Multiple sources? Current vs. prospective users?
0b. **Route to framework subset** -- Identify question type from the table above. Select 3-5 primary frameworks.
1. **Inventory sources** -- List every research source with type, sample, methodology, tier, recency, and bias risk.
2. **Code qualitative data** -- Apply the 6-step coding protocol to interviews and open-ended responses. Extract verbatims.
3. **Grade every source** -- Apply the Research Quality Assessment rubric. Assign evidence tiers. Downgrade where warranted.
4. **Triangulate findings** -- For each candidate finding, check convergence across independent source types. Classify convergence strength.
5. **Filter signal from noise** -- Apply the 5-filter test to every insight. Discard/Monitor/Investigate/Elevate.
6. **Classify insights** -- VALIDATED / EMERGING / HYPOTHESIS / CONTRADICTED with confidence levels.
7. **Check stated vs. revealed** -- Where behavioral data exists, compare against stated preferences. Flag and resolve gaps.
8. **Map research gaps** -- What questions remain unanswered? What decisions lack sufficient evidence? Prioritize gaps.
9. **Cascade every finding to "So What"** -- Observation -> Implication -> Response -> Confidence -> Watch indicator.

### Full Version (detailed steps with decision points)

**Step 1: Source Inventory and Quality Assessment**

1. List every research source available for this synthesis
2. For each source, complete the Source Evaluation Rubric (Framework 3): sample, methodology, bias, recency, relevance
3. Assign initial evidence tier (T1-T6)
4. Apply quality downgrades where warranted (weak sample, undisclosed methodology, poor relevance)
5. Produce the Source Inventory table

**Quality checkpoint:** If >70% of sources are T4-T6, flag prominently: "This synthesis is primarily based on indirect evidence. All findings should be treated as hypotheses until validated with T1-T2 sources."

**Step 2: Code Qualitative Data**

For every qualitative source (interviews, open-ended survey responses, forum posts, support tickets):
1. Apply open coding -- read without a framework, mark every potential insight
2. Apply axial coding -- group codes into need categories
3. Count frequency per category across independent sources
4. Score intensity per category (casual mention vs. unprompted frustration vs. "would switch for this")
5. Extract 2-3 verbatim quotes per category
6. Overlay interpretation layer -- what is the underlying job-to-be-done?

**Quality checkpoint:** Are your categories named by the underlying need ("data integration friction") or by the surface request ("Gantt chart view")? If the latter, code deeper. Surface requests are symptoms; underlying needs are findings.

**Step 3: Triangulate Across Sources**

For each candidate finding from Step 2:
1. Check: does behavioral data (T1) support or contradict this finding?
2. Check: do independent qualitative sources (other interviews, different method) support or contradict?
3. Check: do secondary sources (reports, academic research) support or contradict?
4. Score convergence: Strong / Partial / Weak / Contradicted
5. Produce the Triangulation Summary table

**Quality checkpoint:** If any finding has "Strong convergence" based on multiple sources of the same type (e.g., 3 different interview rounds), it is not truly triangulated -- it is corroborated within a single method. True triangulation requires different methods.

**Step 4: Classify and Grade Findings**

1. Apply the Insight Classification decision tree to each triangulated finding
2. Assign classification: VALIDATED / EMERGING / HYPOTHESIS / CONTRADICTED
3. Assign confidence: H / M / L
4. For CONTRADICTED findings, create dedicated entries in the Cross-Source Contradictions section
5. Order findings by confidence (VALIDATED first, then EMERGING, then HYPOTHESIS)

**Quality checkpoint:** If >50% of findings are HYPOTHESIS, the research base is insufficient for product decisions. Redirect to Research Gap Mapping (Step 6) and recommend additional research before acting.

**Step 5: Apply Demand-Side Analysis**

1. For every finding where behavioral data (T1) exists alongside stated preference data (T2-T5):
   - Compare stated vs. revealed preferences
   - Where they diverge, document the gap and resolve per the Resolution Protocol
2. Check: have churned users or non-adopters been included in the research?
3. Check: has the "do nothing" competitor been identified?
4. Produce the Stated vs. Revealed Preferences table

**Quality checkpoint:** If no behavioral data exists for any finding, the entire synthesis rests on stated preferences. Flag this as a structural limitation.

**Step 6: Map Research Gaps**

1. List every product decision the synthesis is intended to inform
2. For each decision, identify the minimum evidence required
3. Compare available evidence against required evidence
4. Flag every gap and classify: Critical / Blind spot / Thin evidence / Stale / Contradicted
5. Prioritize by decision urgency x evidence shortfall
6. Recommend specific research actions to close priority gaps

**Quality checkpoint:** If there are zero research gaps, you haven't looked hard enough. Every research synthesis has gaps. Finding them is the point.

**Step 7: Cascade Findings to Recommendations**

For EVERY key finding, structure as:
```
OBSERVATION [evidence tier] -> IMPLICATION [mechanism] -> RESPONSE [specific action + owner + timeline] -> CONFIDENCE [H/M/L + key assumption] -> WATCH INDICATOR [observable signal]

"[n] of [total] users reported [specific behavior] [T2: user interviews],
which suggests [underlying need/problem] because [mechanism],
our response should be [specific product action + owner + timeline] because [reasoning],
confidence: H -- assumes [key assumption],
watch: [specific leading indicator]; if [threshold crossed], re-assess."
```

**Bad:** "Users want better collaboration features."

**Elite:** "9 of 12 enterprise users described spending 30-60 minutes weekly on manual data sharing between team members [T2: interviews, unprompted]. Product analytics confirm that the 'export to CSV' action is the 3rd most common action, used by 67% of teams weekly [T1: usage data]. This convergence (VALIDATED, H) indicates that the collaboration gap is a core workflow friction, not a nice-to-have feature request. Response: prioritize real-time data sharing in Q2 roadmap [PM Lead, 8-week delivery]. Assumes the need is for real-time access, not just easier export -- validate with 5 targeted interviews focused on the collaboration workflow before committing to architecture. Watch: if real-time sharing adoption is <15% within 30 days of launch, the stated need may have been an export-quality problem, not a collaboration problem."

---

## Mandatory Output Sections

These sections must appear in every output from this skill, regardless of question type. They are quality assurance mechanisms, not optional extras.

### Assumption Registry

A standalone table of every load-bearing assumption underpinning the research synthesis:

| # | Assumption | Finding it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|

Minimum 3 assumptions. Common load-bearing assumptions for research synthesis:
- "Interview participants are representative of the target user population" -- they almost never are; self-selection bias is endemic
- "Behavioral data reflects genuine preference, not product-forced behavior" -- users may click X because it's the only option, not because they prefer it
- "The need expressed by current users applies to prospective users" -- current users have already adopted; prospective users may have different barriers entirely

Any L-confidence assumption must be `[EVIDENCE-LIMITED]`-flagged inline.

### Adversarial Self-Critique

A mandatory final step: *"Identify >=3 genuine weaknesses in this research synthesis."*

Format per weakness:
- What assumption is being made?
- What evidence would disprove it?
- What is the watch indicator?
- Is there a scenario where acting on this synthesis is catastrophically wrong? (e.g., the validated finding is an artifact of survivorship bias; the "unmet need" is actually a feature discovery problem; the research captured a transient sentiment, not a stable need)

**Critical:** This is not the same as listing failure modes -- failure modes are general patterns. Adversarial self-critique argues against *your specific synthesis conclusions* as forcefully as possible.

### Revision Triggers

When should this Research Synthesis Brief be revisited? Specific, observable conditions:
- A product change fundamentally alters user behavior patterns relevant to these findings
- New behavioral data (T1) contradicts a VALIDATED finding
- Sample composition changes materially (new user segment enters, existing segment churns)
- A CONTRADICTED finding is resolved by new evidence
- More than 6 months pass without revalidation of any VALIDATED finding
- A critical research gap from the Gap Map remains unaddressed past its deadline
- A competitor launches a feature that directly addresses an unmet need identified in this synthesis

---

## Quality Gradients

### Intern Tier
- Lists interview quotes without pattern analysis
- No evidence tiering -- mixes behavioral data with individual opinions at equal weight
- Findings are summaries of what users said, not interpretations of what they need
- No stated vs. revealed preference analysis
- No research gaps identified -- treats what was learned as complete
- No confidence levels -- everything is presented with equal certainty
- Output: interview notes with a summary paragraph, not a research synthesis

### Consultant Tier
- Qualitative data coded with frequency and intensity scoring
- Evidence tiered -- distinguishes T1 behavioral data from T5 anecdotes
- Findings classified by evidence strength (VALIDATED, EMERGING, HYPOTHESIS)
- Triangulation attempted across at least 2 source types
- Stated vs. revealed preferences compared where behavioral data exists
- Research gaps identified with priority levels
- Every finding has a "So What" with product implication
- Missing: full triangulation rigor, demand-side analysis depth, competitive discovery, adversarial self-critique

### Elite Tier
- All 8 frameworks applied with scoring rubrics and decision tables
- Evidence triangulated across 3+ independent source types -- no finding on single tier
- Insight classification with explicit decision tree applied to every finding
- Stated vs. revealed preference analysis with gap resolution protocol
- Signal vs. noise filtering applied to every candidate insight -- the 5-filter test documented
- Research gap map with priority matrix, recommended methods, and timelines
- Competitive discovery: unmet needs from competitor user bases identified and cross-referenced
- Every recommendation in O->I->R->C->W cascade format
- Adversarial self-critique with 3+ genuine weaknesses steelmanned
- Uncommon knowledge ratio is high -- reader learns things they couldn't have known from reading the raw research
- Produces artifacts a PM cannot produce unaided -- evidence-graded findings with explicit confidence, gap maps, and contradiction analysis that require systematic frameworks, not intuition

---

## Failure Modes

**FM-1: Confirmation Bias (Cherry-Picking Evidence)**
*What it looks like:* Synthesis presents 8 supporting quotes and ignores 4 contradicting data points. Findings feel clean and unanimous. The researcher had a hypothesis before starting and found evidence for it.
*Why it happens:* Humans naturally weight evidence that confirms existing beliefs. In research synthesis, this manifests as selective quoting, ignoring contradictory sources, and framing ambiguous findings as supportive.
*Detection:* For each finding, ask: "What evidence AGAINST this finding exists in the data?" If the answer is "none," either the finding is truly universal (rare) or contradictory evidence was filtered out (common).
*Correction:* Mandate a "disconfirming evidence" check for every VALIDATED and EMERGING finding. If disconfirming evidence exists, the finding must either be downgraded or the contradiction must be surfaced in the Cross-Source Contradictions section.

**FM-2: Small-n Generalization (3 Interviews = Market Truth)**
*What it looks like:* "Users want X" based on 3 interviews. No qualification of sample size limitations. The finding is presented with the same confidence as a finding from 200 survey responses.
*Why it happens:* Qualitative data feels convincing because it's vivid. A single compelling user story can feel more persuasive than a large-sample survey. The researcher mistakes narrative power for statistical validity.
*Detection:* Check sample sizes on every finding. If n<5, the finding cannot be classified above HYPOTHESIS regardless of intensity. If n=5-8, maximum classification is EMERGING. These are hard limits, not guidelines.
*Correction:* Enforce the Sample Size Guidance table (Framework 2). Every finding must state its sample size explicitly. Claims that exceed what the sample size supports must be downgraded.

**FM-3: Stated vs. Revealed Preference Confusion**
*What it looks like:* "Users say they want real-time collaboration" is treated as equivalent to "users need real-time collaboration." No behavioral data is consulted. No check for whether users' stated preferences predict their actual behavior.
*Why it happens:* Stated preferences are easy to collect (just ask) and feel authoritative ("the user told us directly"). Behavioral data requires instrumentation, analysis, and often reveals uncomfortable truths.
*Detection:* For every finding based on stated preferences (interviews, surveys), ask: "Is there behavioral data that corroborates or contradicts this?" If no behavioral data was checked, the stated preference stands on its own -- which means it's T5 at best.
*Correction:* Apply the Demand-Side Analysis framework (Framework 6) to every major finding. Where behavioral data exists, it takes precedence. Where it doesn't, flag the finding as `[EVIDENCE-LIMITED: stated preference only -- validate behaviorally]`.

**FM-4: Recency Bias (Latest Interview Dominates)**
*What it looks like:* The synthesis gives disproportionate weight to findings from the most recent research round. Earlier research (6+ months ago) is mentioned but effectively discounted. The latest interview's vivid anecdote becomes the lead finding.
*Why it happens:* Recent information is cognitively available. The researcher remembers the last interview more vividly than the first. Additionally, there's a bias toward believing newer information is "more accurate" even when the older data has a larger sample.
*Detection:* Compare the weight given to findings by recency. If recent findings dominate despite smaller samples or weaker evidence, recency bias is active.
*Correction:* Weight findings by evidence quality (tier + triangulation), not by recency. Apply temporal triangulation (Framework 1): if a finding appears in both old and new research, it's more robust than a finding that only appears in the newest round.

**FM-5: Missing the Non-Consumer**
*What it looks like:* All research subjects are current users. The synthesis accurately describes what current users need but completely misses why non-users haven't adopted, why churned users left, and what the "do nothing" alternative looks like.
*Why it happens:* Current users are easy to recruit and eager to talk. Non-consumers, churned users, and people who evaluated and rejected the product are hard to find and often uninterested in participating.
*Detection:* Check the research sample composition. If 100% of subjects are current active users, the synthesis has a systematic blind spot. The largest opportunity (and the largest risk) is always in the population you didn't study.
*Correction:* Flag as a critical research gap. Recommend: 5-8 churned user interviews, non-consumer analysis via competitive discovery (Framework 8), and analysis of the "do nothing" alternative (inertia, manual workarounds, incumbent tools).

**FM-6: Evidence Laundering (T5 Anecdotes Presented as T2 Research)**
*What it looks like:* A finding cites "user research" but the underlying evidence is 3 individual support tickets and a sales team anecdote. The evidence tier is implicitly presented as T2 (primary research) when it is actually T5 (anecdotal).
*Why it happens:* Aggregating multiple T5 sources feels like upgrading the evidence quality. "We heard this from multiple sources" sounds more authoritative than "we have 3 anecdotes." The researcher conflates source count with source quality.
*Detection:* Trace every finding to its source evidence. Count independent sources AND evaluate each source's tier independently. Five T5 sources are still T5 evidence -- not T2 evidence.
*Correction:* Enforce per-cell evidence tier annotation (Format Rule 2). Every claim must carry its tier. When multiple low-tier sources converge, note the convergence but do NOT upgrade the tier. Instead: "Multiple T5 sources converge on this finding, suggesting it's worth investigating with T2 methods."

**FM-7: Insight Without Implication (Findings That Don't Connect to Decisions)**
*What it looks like:* "Users value simplicity." "Onboarding is confusing." "Power users want more customization." All true. None actionable. The synthesis describes the state of the world without connecting it to what the product team should DO.
*Why it happens:* Describing findings is easier than interpreting them. The researcher stops at the observation and doesn't cascade to implication, response, and confidence.
*Detection:* For each finding, ask: "If I removed this finding, would any product decision change?" If the answer is "no" or "I don't know," the finding lacks implication.
*Correction:* Apply the O->I->R->C->W cascade to every finding. If a finding cannot generate a specific Response with a specific Owner and Timeline, it is context, not insight. Relegate it to background or remove it.

**FM-8: Right Research, Wrong Question (Context Fitness Catch)**
*What it looks like:* A thorough, well-graded research synthesis that answers a question nobody is asking. The PM asked for "user research synthesis" but the actual problem is a competitive positioning question, a metric design question, or a spec writing question that happens to mention users.
*Why it happens:* The skill is triggered by any research-sounding prompt without checking whether a Research Synthesis Brief is the right artifact.
*Detection:* Ask: "What decision will this synthesis inform? Is the decision about what users need (-> this skill), or about competitive positioning (-> Competitive Analysis), or about what to measure (-> Metric Design), or about what to build (-> Spec Writing)?"
*Correction:* Run the Context Fitness Check (Step 0) before Framework Selection. If the core question isn't about user needs and evidence, redirect to the appropriate skill.

**FM-9: Expert-Only Document (Output Not Navigable by Non-Creators)**
*What it looks like:* Dense with framework names (Triangulation, Demand-Side Analysis, VALIDATED/EMERGING), notation (T1-T6, H/M/L, O->I->R->C->W), and methodology discussion that assumes the reader conducted the research. A VP cannot find the conclusions. A designer cannot find the user needs. The document serves the researcher and nobody else.
*Why it happens:* The skill optimizes for analytical rigor, not reader comprehension. The researcher knows all the notation; the reader doesn't.
*Detection:* Show the output to someone who didn't request it. If they need more than 60 seconds to find the key findings, or if they ask "what does T2 mean?", the document fails the reader test.
*Correction:* The output template mandates a "How to Read This Document" section and a Notation Key before the analysis begins. The Executive Summary uses zero research jargon -- plain language a non-PM exec can act on. Role-based reading guides direct each audience to the sections they need.

---

## What's Next

<- This skill works best after: **Problem Framing** (if available) -- a well-framed problem focuses research on the right questions and user segments
-> This skill's output feeds well into: **Competitive & Market Analysis** (validated user needs inform competitive positioning), **Spec Writing** (evidence-graded findings become spec requirements), **Metric Design & Experimentation** (evidence gaps drive experiment design)
+ **Start here if:** You have research data (interviews, surveys, analytics, reports) and need to know what it means for your product
! **For a full product cycle:** Problem Framing -> **[THIS SKILL]** -> Competitive & Market Analysis -> Spec Writing -> Metric Design & Experimentation -> ongoing measurement loop

**Chain interface:**
- **Receives:** Raw research inputs (interview transcripts, survey results, analytics data, reports), or a problem definition with research questions (from Problem Framing), or a specific product question requiring evidence evaluation
- **Produces:** Research Synthesis Brief with evidence-graded findings, insight classifications, research gap map, stated vs. revealed preference analysis, and research-backed recommendations with confidence levels
- **Handoff artifact:** The Research Synthesis Brief's "Key Findings" section maps directly to Competitive Analysis input (validated user needs inform competitive positioning), Spec Writing input (evidence-graded requirements), and Metric Design input (evidence gaps drive experiment design; validated needs inform metric selection)

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Fitness Check passed: question is about user needs/evidence, multiple sources available
- [ ] If single source type: flagged prominently; findings capped at M confidence
- [ ] If pre-product research: flagged prominently; no T1 data available
- [ ] How to Read This Document section present with role-based reading guide
- [ ] Notation Key present: H/M/L, T1-T6, VALIDATED/EMERGING/HYPOTHESIS/CONTRADICTED, O->I->R->C->W all explained
- [ ] Executive Summary uses zero research jargon -- plain language only
- [ ] Source inventory completed: every source assessed for sample, methodology, bias, recency, relevance
- [ ] Evidence tiers assigned to every source with quality downgrades where warranted
- [ ] Qualitative data coded: open coding -> axial coding -> frequency -> intensity -> verbatims -> interpretation
- [ ] Frequency vs. intensity scored independently for every need
- [ ] Triangulation attempted for every key finding -- convergence scored across independent source types
- [ ] Signal vs. noise filter applied: 5-filter test documented for candidate insights
- [ ] Insight classification applied: VALIDATED / EMERGING / HYPOTHESIS / CONTRADICTED with decision tree
- [ ] Stated vs. revealed preferences compared where behavioral data exists
- [ ] Behavioral data prioritized over stated preferences where they conflict
- [ ] Research gap map completed: unanswered questions, decision they block, recommended method, priority
- [ ] Cross-source contradictions surfaced explicitly (not resolved artificially)
- [ ] Competitive discovery findings included (if applicable): unmet needs from competitor user bases
- [ ] Non-consumer analysis included or flagged as a gap
- [ ] Churned user data included or flagged as a gap
- [ ] Every finding ordered by confidence (VALIDATED first), not by source order or recency

**Format Rules compliance:**
- [ ] Step 0b routing table applied -- only load-bearing frameworks for this question type selected
- [ ] H/M/L confidence used on all research findings (no weasel words)
- [ ] Per-cell evidence tier annotation applied in all finding and comparison tables (T1-T6 inline)
- [ ] Staleness flags applied to any finding based on data older than 6 months
- [ ] EVIDENCE-LIMITED flags applied to any key conclusion resting only on T4-T6 evidence
- [ ] Research recommendations use O->I->R->C->W cascade (not bare assertions)
- [ ] Contradictions between sources surfaced explicitly (not averaged or resolved artificially)
- [ ] Framework references get one-line contextual explanation on first use

**Mandatory output sections:**
- [ ] Assumption Registry completed -- minimum 3 load-bearing assumptions with confidence, evidence, and invalidation conditions
- [ ] L-confidence assumptions flagged [EVIDENCE-LIMITED] inline
- [ ] Adversarial Self-Critique completed -- >=3 genuine weaknesses in this specific synthesis identified with watch indicators
- [ ] Revision Triggers defined -- specific, observable conditions that would require synthesis update

---

## Worked Example

### Input

> "We just completed a research sprint for our B2B project management tool (TeamFlow). We have: 12 user interviews (enterprise segment, current users), 3 churned user interviews, NPS survey results (n=340), product analytics showing feature usage over the past 90 days, and 87 G2 reviews from the past 6 months. The PM lead wants to know: what should we build next quarter? Specifically, should we invest in (a) real-time collaboration, (b) advanced reporting, or (c) better integrations?"

---

### Output (abbreviated -- demonstrates key formats; a full Research Synthesis Brief covers all steps)

**Source Inventory & Quality Assessment:**

| Source | Type | Sample | Methodology | Tier | Recency | Key Bias Risk |
|---|---|---|---|---|---|---|
| User interviews (enterprise) | Qualitative | n=12, enterprise only | Semi-structured, 45 min | T2 | Feb 2026 | Self-selection; enterprise-only (no SMB voice); social desirability |
| Churned user interviews | Qualitative | n=3 | Semi-structured, 30 min | T5 | Feb 2026 | n<5: anecdotal only. Cannot establish patterns. |
| NPS survey | Quantitative | n=340 (28% response rate) | Standard NPS + open text | T3 | Jan 2026 | Response bias (satisfied users over-represented at 28% response rate); no behavioral context |
| Product analytics | Behavioral | N=8,200 WAU | Full population, 90-day window | T1 | Feb 2026 | Survivorship (churned users absent from 90-day window) |
| G2 reviews | Mixed | n=87 | Self-selected reviewers | T5 (individual) / T4 (pattern) | Aug 2025-Feb 2026 | Extreme selection (very happy or very unhappy); vendor solicitation may inflate positive) |

**Source coverage assessment:** No SMB user voice. No non-consumer data. Churned sample (n=3) is too small for patterns. Integration-specific behavioral data not broken out. These are flagged as research gaps.

---

**Key Findings (Evidence-Graded):**

**Finding 1: Integration Friction Is the Top Unmet Need, Not Collaboration**
- **Classification:** VALIDATED
- **Confidence:** H
- **Evidence:** Product analytics: "Export to CSV" is the 3rd most common action, used by 67% of teams weekly (T1). Interviews: 9/12 users described manual data transfer between tools as a major pain point, unprompted (T2). G2 reviews: "integrations" appears in 34/87 reviews, 28 negative (T4). NPS open text: 47 mentions of "integration" or "connect to [tool]" (T3).
- **Detail:** Users across all evidence sources consistently describe the need to move data between TeamFlow and other tools (Salesforce, Jira, Slack) as a primary friction point. The behavioral data (CSV export frequency) corroborates the stated need -- users are working around the integration gap.
- **Implication:** Integration investment has the highest evidence support. Collaboration features may also be needed, but the integration pain is validated while the collaboration need is emerging (see Finding 3).

**Finding 2: Advanced Reporting Is a Power-User Need, Not a Mainstream One**
- **Classification:** EMERGING
- **Confidence:** M
- **Evidence:** Interviews: 4/12 users mentioned reporting needs, all from the "admin" persona (T2). Product analytics: custom report builder used by only 12% of users, but those users have 2.3x higher retention (T1). NPS survey: 11 mentions of "reporting" (T3).
- **Detail:** Reporting is high-intensity for a small segment (admins/managers) but low-frequency across the broader user base. The retention correlation is strong (T1) but may reflect user sophistication, not reporting value -- caution warranted.
- **Implication:** Do not prioritize for Q2 mainline roadmap. Investigate whether reporting-heavy users retain because of reporting, or because they're more invested users who would retain anyway. Design a causal experiment before doubling down.

**Finding 3: Real-Time Collaboration Is Stated but Not Revealed**
- **Classification:** HYPOTHESIS
- **Confidence:** L
- **Evidence:** Interviews: 7/12 users said they "would love" real-time co-editing (T2, but stated preference -- not behavioral). Product analytics: only 23% of projects have >1 active editor; average concurrent editors = 1.1 (T1 -- contradicts stated preference). G2 reviews: 8 mentions of "collaboration," mixed sentiment (T5).
- **Detail:** Strong stated preference for collaboration, but behavioral data shows very low concurrent editing. The gap between stated and revealed preference is significant. Users may be requesting collaboration because it sounds valuable, not because their current workflow demands it. Alternatively, the current product may make collaboration difficult enough that users have adapted to serial workflows -- in which case the behavioral data reflects product constraints, not user preferences.
- **Implication:** [EVIDENCE-LIMITED: stated preference only -- behavioral data contradicts] Do NOT invest in real-time collaboration based on current evidence. Instead, run 5 targeted interviews focused specifically on collaboration workflows: "Walk me through the last time you needed input from a colleague on a project in TeamFlow. What did you actually do?" The answer will reveal whether the collaboration need is real (workflow demands it) or aspirational (sounds nice but serial workflows are fine).

---

**Stated vs. Revealed Preference Analysis:**

| What Users SAY | What Users DO | Gap | Implication |
|---|---|---|---|
| "We'd love real-time collaboration" (T2, 7/12 interviews) | Only 23% of projects have >1 editor; concurrent editing is 1.1 average (T1) | Massive: stated demand is high, revealed behavior is near-zero | Do not build based on stated preference. Investigate whether current product constrains collaboration (in which case demand is real but latent) or users don't actually collaborate on project plans (in which case demand is aspirational). |
| "Integrations are painful" (T2, 9/12 interviews) | CSV export is 3rd most common action; 67% of teams weekly (T1) | Small: stated pain aligns with behavioral workaround | Integrations are a validated need. Behavioral data corroborates stated preference. Act on this. |

---

**Research Gap Map (top 3):**

| Gap | Type | Decision It Blocks | Priority | Recommended Action | Timeline |
|---|---|---|---|---|---|
| No SMB user voice | Blind spot | Whether findings generalize beyond enterprise | HIGH | 8 SMB interviews | 3 weeks |
| Collaboration workflow unknown | Critical gap | Whether to invest in real-time features (Finding 3) | CRITICAL | 5 targeted collaboration-workflow interviews | 2 weeks |
| Churned user sample too small (n=3) | Thin evidence | Churn reduction strategy | HIGH | Expand to 8-10 churned user interviews | 3 weeks |

---

**Recommendation 1 (O->I->R->C->W):**
- **Observation** [T1 + T2 + T3 + T4]: Integration friction is the top validated unmet need across all evidence sources. Users work around it weekly via CSV export.
- **Implication**: Every manual export represents a workflow that could be automated. At 67% of teams doing this weekly, the addressable impact is 2/3 of the active user base.
- **Response**: Prioritize top-3 integration connections (Salesforce, Jira, Slack -- per interview frequency) in Q2 roadmap. PM Lead owns; 10-week delivery target for first integration.
- **Confidence**: H -- assumes integration friction drives retention risk. If churned user interviews (once expanded to n>=8) reveal a different churn driver, re-assess.
- **Watch**: Post-launch integration adoption rate. If <25% of teams activate within 30 days of availability, the stated need may be overstated or the implementation may miss the actual workflow.

---

### Why This Works

This output was produced by running Steps 1-4 and Step 7 of the Full Application Method: source inventory with quality assessment, qualitative coding with frequency and intensity scoring, triangulation across 4 independent source types, insight classification with decision tree, and the O->I->R->C->W cascade for recommendations. It satisfies the Elite Tier Quality Gradient: every finding has an explicit classification and confidence level; behavioral data takes precedence over stated preferences when they conflict (Finding 3); research gaps are named and prioritized (not ignored); and the recommendation is actionable with a specific owner, timeline, and watch indicator.

The most valuable output is the *non-recommendation*: the analysis prevented the team from investing in real-time collaboration (high stated demand, near-zero behavioral support) and redirected toward integrations (validated across all sources). A synthesis without the stated vs. revealed preference framework would have recommended collaboration -- leading to a quarter of engineering investment on a feature users asked for but may not use.

---

## References

**Framework Sources:**
- Norman K. Denzin, *The Research Act* (1970) -- Triangulation methodology
- Kathy Charmaz, *Constructing Grounded Theory* (2006) -- Open and axial coding protocols
- Johnny Saldana, *The Coding Manual for Qualitative Researchers* (2021) -- Coding methodology
- Daniel Kahneman, *Thinking, Fast and Slow* (2011) -- Stated vs. revealed preference, cognitive biases
- Clayton Christensen, *Competing Against Luck* (2016) -- Jobs-to-be-Done underlying demand-side analysis
- Teresa Torres, *Continuous Discovery Habits* (2021) -- Discovery sprint methodology, opportunity solution trees
- Erika Hall, *Just Enough Research* (2013) -- Research quality assessment, evidence grading
- Rob Fitzpatrick, *The Mom Test* (2013) -- Interview bias, separating signal from noise in user conversations
- Indi Young, *Mental Models* (2008) -- Demand-side analysis, understanding user behavior patterns

**Related Skills in PM Skills Arsenal:**
- Problem Framing -- upstream (defines what questions to research)
- Competitive & Market Analysis -- parallel (market-side structural analysis; this skill is demand-side)
- Spec Writing -- downstream (uses evidence-graded findings as requirements)
- Metric Design & Experimentation -- downstream (evidence gaps drive experiment design)

---

*Created: 2026-02-20 | PM Skills Arsenal v1.3.0 | BLD-004*
*Quality tier: Elite (>=800 lines, 8 encoded frameworks, quality gradients, 9 failure modes, reader navigation, context gate)*
*License: MIT*
