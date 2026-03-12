---
name: problem-framing
description: "Use when decomposing a vague problem into a structured problem statement, identifying who has the problem and why it matters, sizing the opportunity, mapping constraints, prioritizing across multiple problems, or producing a Problem Definition Document that feeds into Discovery, Competitive Analysis, or Spec Writing. Encodes Problem Definition Canvas, 5 Whys Root Cause, JTBD Problem Framing, Opportunity Sizing, Problem-Solution Fit Assessment, Constraint Mapping, Stakeholder Impact Matrix, and ICE/RICE Prioritization."
version: "1.3.0"
type: "codex"
tags: ["Problem Shaping", "Strategy", "Upstream"]
created: "2026-02-20"
valid_until: "2026-08-20"
derived_from: "original"
tested_with: ["Claude Sonnet 4.6", "Claude Opus 4.6"]
license: "MIT"
---

## Purpose

Produce a **Problem Definition Document** — a structured artifact that decomposes a vague or assumed problem into an evidence-graded problem statement with identified stakeholders, quantified opportunity size, mapped constraints, and prioritized sub-problems. This is the upstream skill that feeds every downstream PM activity: Discovery, Competitive Analysis, Spec Writing, and Metric Design. The output is not a brief or a pitch — it is a rigorous decomposition that forces the question "What exactly are we solving and for whom?" to be answered with evidence, not assumption.

## When to Use / When NOT to Use

**Use this skill when:**
- A stakeholder says "we should build X" and you need to determine whether X solves a real problem
- You have a vague problem area ("user retention is bad") that needs decomposition into solvable sub-problems
- Multiple teams disagree on what the real problem is — you need a shared, evidence-graded definition
- You are starting a new product initiative and need to define the problem space before Discovery or Competitive Analysis
- A feature request arrives disguised as a problem statement and you need to peel back to the actual user pain
- You need to prioritize across multiple candidate problems with limited resources
- An existing product is underperforming and nobody agrees on why

**Do NOT use this skill when:**
- The problem is already well-defined and validated — you need a spec, not more framing (use Spec Writing)
- You need to understand the competitive landscape (use Competitive & Market Analysis — that skill consumes this one's output)
- You need to design metrics for an already-defined feature (use Metric Design & Experimentation)
- You need to run user research — this skill identifies what research to do, not how to do it (use Discovery & Research)
- The "problem" is a technical bug with a known root cause (use your bug tracker)

**Anti-inputs (what this skill does NOT handle):**
- Solution design or feature specification (-> Spec Writing skill)
- User research methodology and interview design (-> Discovery & Research skill)
- Competitive positioning (-> Competitive & Market Analysis skill)
- Metric hierarchy and experiment design (-> Metric Design & Experimentation skill)
- Organizational change management (this is product problem framing, not org design)

---

## Format Rules

These rules govern every output produced by this codex. They are quality enforcement mechanisms derived from benchmarking against investment-grade problem definitions. They are mandatory, not optional.

### Rule 1: Take Positions with Calibrated Confidence
Never use weasel words in conclusions. Replace "likely," "may," "could," "seems" with explicit confidence levels:
- **H (>70%)** — Strong evidence supports this conclusion. Act on it.
- **M (40-70%)** — Direction is probable but evidence is mixed. Validate before committing resources.
- **L (<40%)** — This is a hypothesis, not a finding. Do not act without further evidence.

*Why:* A problem statement grounded in validated behavioral data (H) requires a different response than one built from stakeholder assertions (L). Undifferentiated confidence obscures the distinction between "we know this hurts" and "someone told us this hurts."

### Rule 2: Per-Cell Evidence Tier Annotation in All Tables
Every table cell making a substantive claim carries an inline evidence tier tag:
- `Validated (T1)` — grounded in behavioral data from affected users
- `Researched (T2)` — grounded in primary user research (interviews, observations)
- `Inferred (T6)` — based on reasoning or assumption

*Why:* A problem severity score based on user behavioral data (T1) carries different weight than one inferred from a stakeholder meeting (T5). Conflating them produces false confidence in the problem definition.

### Rule 3: The O->I->R->C->W Cascade Applies to All Recommendations
Every problem framing recommendation or intervention follows:
```
OBSERVATION [evidence tier] -> IMPLICATION [mechanism] -> RESPONSE [specific action + owner] -> CONFIDENCE [H/M/L + key assumption] -> WATCH INDICATOR [observable signal]
```
*Why:* The most common problem framing failure is disconnected findings — "users struggle with onboarding" without specifying the mechanism, the recommended investigation, or the observable signal that confirms the problem is real and worth solving.

### Rule 4: Framework Selection Before Application (Step 0)
Different problem types require different framework subsets. Always apply the Step 0b routing table before selecting which of the 8 frameworks to use.

*Why:* Applying all 8 frameworks to every problem inflates output 2-3x without improving decision quality. A prioritization question does not need 5 Whys root cause analysis; a root cause investigation does not need opportunity sizing.

### Rule 5: Surface Contradictions Between Frameworks
When the Problem Definition Canvas and 5 Whys reach different conclusions about the root problem, or when Opportunity Sizing suggests high value but Problem-Solution Fit Assessment says the problem is not painful enough, surface the contradiction explicitly. Do not resolve artificially.

*Why:* Contradictions are the most valuable signals. A problem that scores high on opportunity size but low on validated severity is a hypothesis, not a finding — and that distinction changes the next action entirely.

### Rule 6: Staleness Flags
Any claim based on data older than 6 months must carry `[POTENTIALLY STALE -- verify before presenting]`.

*Why:* Problem landscapes shift. A pain point validated 12 months ago may have been solved by a competitor, a workaround, or a market shift. Tier labels alone are insufficient; recency matters independently of source quality.

### Rule 7: Evidence-Limited Flags
If a key problem framing conclusion rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

*Why:* A problem statement built entirely on stakeholder assertions (T5) and inference (T6) is a hypothesis document. Treating it as a validated problem definition is the single most expensive upstream mistake in product development.

### Rule 8: Framework References Get One-Line Context
Not "Jobs-to-be-Done analysis" but "Christensen's framework for understanding why customers 'hire' products — we use it here to identify what functional, emotional, and social jobs the user is trying to accomplish, which reveals the real problem underneath the stated feature request." The reader needs to understand why a framework matters for *their* decision.

### Rule 9: The Document Must Be Navigable by Non-Creators
Include a reading guide (by time and by role), a notation key, and layered depth. A VP should be able to read only the Executive Summary and understand the problem. A PM should be able to read through Findings and skip Deep Analysis. The full document is for the analyst or researcher who will design the next investigation. No reader should encounter unexplained notation.

---

## Output Template (Mandatory Document Skeleton)

Every Problem Definition Document MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was skipped in Step 0b, note "Skipped -- not load-bearing for this question type" in that section.

```markdown
# Problem Definition Document: [Subject -- e.g., "Enterprise Onboarding Drop-Off"]

> **Date:** [YYYY-MM-DD] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which key claims need revalidation]

---

## Executive Summary

[5 sentences max. A VP reads only this and understands: what the problem is, who has it, how big it is, why it matters now, and what the recommended next step is. No framework names, no jargon, no evidence tier tags. Plain language a non-PM exec can act on. Final sentence = the recommended next action in bold.]

---

## How to Read This Document

**What this is:** A problem definition -- not a solution proposal, not a spec, not a brief. It answers "What exactly are we solving and for whom?" with evidence-graded confidence. It is the upstream artifact that feeds Discovery, Competitive Analysis, and Spec Writing.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | The problem, who has it, how big it is, and the recommended next step |
| **15 min** | Executive Summary + Problem Statement + Opportunity Sizing | The structured problem definition with quantified impact |
| **30 min** | Full document through Recommendations | Complete problem decomposition with constraints, stakeholders, and prioritization |
| **Deep dive** | Everything including Appendix | Full framework applications, assumptions, adversarial self-critique |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Summary | Opportunity Sizing (section 5), Recommendations (section 10) | Framework sections, deep root cause analysis |
| PM Lead | Executive Summary | Problem Statement (section 2), Constraint Map (section 7), Prioritization (section 9) | Individual framework deep dives |
| Researcher / Designer | Full document in order | Root Cause (section 3), JTBD Framing (section 4), Stakeholder Matrix (section 8) | Opportunity Sizing financial details |
| Engineer | Executive Summary | Constraint Map (section 7), Problem Statement (section 2) | Stakeholder analysis, prioritization methodology |

---

## Notation Key

**Confidence levels** -- applied to every problem framing conclusion:
- **H (>70% confident)** -- Strong evidence supports this conclusion. Act on it.
- **M (40-70%)** -- Direction is probable but evidence is mixed. Validate before committing resources.
- **L (<40%)** -- This is a hypothesis, not a finding. Do not act without further evidence.

**Evidence tiers** -- how we know what we claim to know (tagged inline as T1-T6):
- **T1** -- Direct user behavioral data: what people DO (usage analytics, support tickets, churn data, session recordings)
- **T2** -- Primary user research: structured interviews, contextual inquiry, usability observations
- **T3** -- Expert analysis with disclosed methodology: UX research reports, domain expert assessments
- **T4** -- Market/industry reports: Gartner, Forrester, industry surveys (useful for sizing, less for problem specifics)
- **T5** -- Stakeholder assertions: internal claims, executive opinions, sales team anecdotes
- **T6** -- Assumptions/inference: first-principles reasoning, analogies from other domains (weakest)

**Problem severity ratings:**
- **Critical** -- Users cannot accomplish their goal; abandon or churn
- **Major** -- Users accomplish the goal but with significant friction or workaround
- **Minor** -- Annoyance that does not change behavior or outcomes

**Recommendation format** (O->I->R->C->W):
- **O**bservation -- What we see (with evidence tier)
- **I**mplication -- Why it matters (the mechanism)
- **R**esponse -- What to do (specific action + owner + timeline)
- **C**onfidence -- How sure we are (H/M/L + key assumption)
- **W**atch -- How to know if we're wrong (observable signal)

**Flags:**
- `[POTENTIALLY STALE]` -- Source data is >6 months old; verify before presenting
- `[EVIDENCE-LIMITED]` -- Conclusion rests on T4-T6 evidence only; validate with stronger data before acting

---

## Step 0: Context Fitness Check

Before selecting frameworks, verify that a Problem Definition Document is the right artifact.

| Question | If Yes | If No |
|---|---|---|
| **Is the problem space genuinely unclear or contested?** | Proceed to Problem Framing. This is exactly when you need it. | If the problem is already well-defined and validated, skip to Spec Writing or Discovery. A Problem Definition Document for an already-validated problem is overhead. |
| **Do you have access to user behavioral data (T1) or primary research (T2)?** | Problem definition can produce H-confidence conclusions. | Flag prominently: "This problem definition is built from stakeholder input and inference (T5-T6). All problem statements are hypotheses -- validate with user research before committing to solutions." Cap confidence at M for problem severity claims. |
| **Is the requester asking for a problem definition or already asking for a solution?** | Proceed normally. | The requester may need to be redirected. A Problem Definition Document that arrives when the team expects a feature spec will frustrate. Clarify the purpose: "This document defines WHAT to solve. The next step is HOW." |
| **Are multiple stakeholders involved with potentially different views of the problem?** | Stakeholder Impact Matrix (F7) is load-bearing. Apply it. | If single stakeholder, Stakeholder Impact Matrix can be simplified or skipped. |
| **Is there time pressure to ship something immediately?** | Produce a Quick Version (10-step) problem definition; flag gaps for later validation. | Full Version with all applicable frameworks. |

**If the core answer is "the problem is already clear":** State this prominently. Recommend the appropriate downstream skill instead. A Problem Definition Document for a validated problem is waste.

---

## Step 0b: Framework Selection

| Question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Decompose a vague problem"] | [e.g., F1 Problem Definition Canvas, F2 5 Whys, F3 JTBD Problem Framing] | [e.g., F5 Problem-Solution Fit, F7 Stakeholder Matrix] | [e.g., "F8 ICE/RICE -- single problem, no prioritization needed"] |

**Framework Selection Routing Table:**

| Question Type | Prompt Signals | Primary Frameworks | Frameworks to Skip |
|---|---|---|---|
| **Decompose a vague problem** | "what's the real problem", "users are struggling", "something is broken" | F1 Problem Definition Canvas, F2 5 Whys, F3 JTBD Problem Framing | F4 Opportunity Sizing (premature), F8 ICE/RICE (single problem) |
| **Quantify a known problem** | "how big is this", "should we invest", "is this worth solving" | F4 Opportunity Sizing, F5 Problem-Solution Fit, F7 Stakeholder Impact | F2 5 Whys (root cause already known), F6 Constraint Mapping (premature) |
| **Prioritize across problems** | "which problem first", "where to focus", "rank these" | F4 Opportunity Sizing, F8 ICE/RICE Prioritization, F5 Problem-Solution Fit | F2 5 Whys (apply per-problem, not across set), F6 Constraint Mapping (apply after selection) |
| **Root cause investigation** | "why is this happening", "symptoms vs. cause", "keeps recurring" | F2 5 Whys, F1 Problem Definition Canvas, F6 Constraint Mapping | F4 Opportunity Sizing (premature), F8 ICE/RICE (single problem) |
| **Stakeholder alignment** | "everyone disagrees", "leadership wants X but users need Y", "political" | F7 Stakeholder Impact Matrix, F1 Problem Definition Canvas, F3 JTBD | F8 ICE/RICE (not a prioritization problem), F4 Opportunity Sizing (secondary) |
| **Constraint discovery** | "what can we actually do", "regulatory limits", "tech debt", "timeline" | F6 Constraint Mapping, F1 Problem Definition Canvas, F5 Problem-Solution Fit | F2 5 Whys (not a root cause problem), F8 ICE/RICE (not a prioritization problem) |
| **Full problem definition** | "define the problem space", "new initiative", "starting from scratch" | All -- tier explicitly: 4 primary, rest supporting | None -- but label tiers and apply primary frameworks at full depth, supporting at scan depth |

---

## 1. Problem Statement

**One-sentence problem statement:** [Who] experiences [what pain] when [trigger/context], resulting in [measurable consequence].

**Confidence:** [H/M/L] | **Evidence basis:** [T1/T2/.../T6]

**Problem type:** [New problem / Existing problem worsening / Existing problem newly visible / Assumed problem needing validation]

---

## 2. Problem Definition Canvas

| Dimension | Finding | Evidence | Confidence |
|---|---|---|---|
| **Who has this problem?** | [Specific user segment, not "users"] | (TX: source) | H/M/L |
| **What are they trying to do?** | [The goal, not the feature they want] | (TX: source) | H/M/L |
| **What do they do today?** | [Current behavior including workarounds] | (TX: source) | H/M/L |
| **Why is that painful?** | [Specific friction, cost, risk, or failure] | (TX: source) | H/M/L |
| **What triggers the pain?** | [The moment or context where pain is acute] | (TX: source) | H/M/L |
| **What does "good" look like?** | [Desired end state in the user's words] | (TX: source) | H/M/L |
| **How do they know it's solved?** | [Observable success criteria from user perspective] | (TX: source) | H/M/L |

---

## 3. Root Cause Analysis

**Presented problem:** [What the stakeholder or user SAID the problem is]
**Root problem:** [What the 5 Whys analysis reveals the actual problem is]

| Layer | Why? | Evidence | Tier |
|---|---|---|---|
| Surface symptom | [Presented complaint] | (TX: source) | TX |
| Why 1 | [First layer cause] | | |
| Why 2 | [Deeper cause] | | |
| Why 3 | [Structural cause] | | |
| Why 4 | [System-level cause] | | |
| Why 5 (root) | [Root cause] | | |

**Divergence check:** Does the root cause match the presented problem? If not, flag the gap explicitly. The stakeholder expects you to solve the surface symptom; the analysis says the root is elsewhere. This is a critical communication moment.

---

## 4. JTBD Problem Framing

| Job Dimension | Finding | Evidence | Unmet? |
|---|---|---|---|
| **Functional job** | [What they're trying to accomplish] | (TX) | Over-served / Under-served / Unserved |
| **Emotional job** | [How they want to feel] | (TX) | Over-served / Under-served / Unserved |
| **Social job** | [How they want to be perceived] | (TX) | Over-served / Under-served / Unserved |

**Consumption chain analysis:**

| Phase | Current behavior | Pain points | Opportunity |
|---|---|---|---|
| Before (trigger/discovery) | | | |
| During (active use) | | | |
| After (outcome/follow-up) | | | |

**Competing "hires":** [What else does the user "hire" for this job? Include manual processes, workarounds, doing nothing, and competitor products.]

---

## 5. Opportunity Sizing

| Dimension | Estimate | Evidence | Confidence |
|---|---|---|---|
| **Frequency** -- How often does this problem occur? | [X times per user per week/month] | (TX) | H/M/L |
| **Severity** -- How painful is each occurrence? | [Critical/Major/Minor + user impact] | (TX) | H/M/L |
| **Breadth** -- How many users are affected? | [N users or % of base] | (TX) | H/M/L |
| **Willingness to pay/switch** -- Would they change behavior? | [Evidence of switching, payment, workaround investment] | (TX) | H/M/L |

**Opportunity Score:** Frequency x Severity x Breadth x Willingness = [Composite score with calculation shown]

**Scoring rubric for each dimension (1-5 scale):**

| Score | Frequency | Severity | Breadth | Willingness |
|---|---|---|---|---|
| **5** | Multiple times daily | Cannot complete goal; churns | >50% of user base | Actively paying for workarounds |
| **4** | Daily | Significant time/effort wasted | 25-50% of user base | Would switch products for this |
| **3** | Weekly | Noticeable friction, uses workaround | 10-25% of user base | Would try a solution if easy |
| **2** | Monthly | Minor annoyance | 5-10% of user base | Aware of pain but not acting |
| **1** | Rarely | Barely notices | <5% of user base | Does not recognize the pain |

**Composite score interpretation:**
- **80-125** (5x5x5x1 to 5x5x5x1): Severe, widespread, frequent -- high-priority problem
- **40-79**: Significant problem worth investigating further
- **15-39**: Moderate problem -- validate severity and willingness before committing
- **<15**: Likely not worth dedicated investment unless strategic

---

## 6. Problem-Solution Fit Assessment

Before any solution work begins, assess whether this is a real problem worth solving.

| Test | Question | Finding | Pass/Fail |
|---|---|---|---|
| **Existence test** | Do real users actually have this problem? (Not: do stakeholders believe they do?) | [Finding + evidence tier] | PASS / FAIL / UNVALIDATED |
| **Severity test** | Is the problem painful enough to change behavior? | [Finding] | PASS / FAIL / UNVALIDATED |
| **Frequency test** | Does it occur often enough to justify a persistent solution? | [Finding] | PASS / FAIL / UNVALIDATED |
| **Willingness test** | Would users adopt a solution? (Pay, switch, learn, change workflow) | [Finding] | PASS / FAIL / UNVALIDATED |
| **Solvability test** | Can this problem be solved within our constraints? | [Finding] | PASS / FAIL / UNVALIDATED |
| **Timing test** | Why now? What has changed that makes this problem newly solvable or newly urgent? | [Finding] | PASS / FAIL / UNVALIDATED |

**Decision rule:**
- **All 6 PASS**: Problem is validated. Proceed to Discovery and/or Spec Writing.
- **1-2 FAIL**: Investigate the failing dimensions. The problem may be real but the framing may be wrong.
- **3+ FAIL**: This is not a problem worth solving in its current framing. Re-frame or deprioritize.
- **Any UNVALIDATED**: This is a hypothesis, not a validated problem. Design research to validate before committing resources. Flag as `[EVIDENCE-LIMITED]`.

---

## 7. Constraint Map

| Constraint Type | Constraint | Impact on Solution Space | Negotiable? | Source |
|---|---|---|---|---|
| **Technical** | [e.g., "Legacy API cannot handle real-time events"] | [Eliminates solution class X] | Y/N | (TX) |
| **Business** | [e.g., "Cannot increase pricing this quarter"] | [Constrains monetization approach] | Y/N | (TX) |
| **Regulatory** | [e.g., "GDPR requires data residency in EU"] | [Limits architecture options] | N | (TX) |
| **Timeline** | [e.g., "Must ship before Q3 board meeting"] | [Constrains scope and quality tradeoff] | Partially | (TX) |
| **Resource** | [e.g., "2 engineers for 6 weeks"] | [Limits implementation complexity] | Y/N | (TX) |
| **Organizational** | [e.g., "Requires sign-off from 3 VPs"] | [Adds approval latency] | Partially | (TX) |
| **User** | [e.g., "Users will not install a desktop agent"] | [Eliminates solution class Y] | N (behavioral) | (TX) |

**Constraint interaction matrix:** [Note any constraints that compound -- e.g., timeline + resource = scope must be cut. These compound constraints are often the real decision drivers.]

**Critical distinction:** Constraints are NOT the same as assumptions. A constraint is a verified limitation. An assumed constraint should be listed in the Assumption Registry with a plan to validate.

---

## 8. Stakeholder Impact Matrix

| Stakeholder | Problem Impact | Power (1-5) | Interest (1-5) | Current Position | Action Needed |
|---|---|---|---|---|---|
| [e.g., "End users -- data analysts"] | [How this problem affects them] | X | X | Champion / Supporter / Neutral / Resistant | [What to do about this stakeholder] |
| [e.g., "IT admins"] | [How this problem affects them] | X | X | | |
| [e.g., "VP Product"] | [How this problem affects them] | X | X | | |
| [e.g., "Engineering lead"] | [How this problem affects them] | X | X | | |

**Scoring rubric:**

| Score | Power | Interest |
|---|---|---|
| **5** | Can unilaterally approve/kill the initiative | Problem directly affects their core metrics/goals |
| **4** | Strong influence on decision; effective veto | Problem is a top-3 concern for them |
| **3** | Moderate influence; voice in the room | Aware and somewhat affected |
| **2** | Minimal direct influence | Tangentially affected |
| **1** | No decision authority | Unaware or unaffected |

**Stakeholder strategy grid:**

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | **Manage closely** -- these stakeholders define your constraints and your approval path. Align on problem definition before proceeding. | **Keep satisfied** -- they can block you but won't unless provoked. Keep informed; do not surprise. |
| **Low Power** | **Keep informed** -- they care but can't block. Valuable for evidence gathering and validation. | **Monitor** -- minimal investment. |

**Key insight:** The stakeholder who PRESENTS the problem and the stakeholder who HAS the problem are often different people. A VP saying "our users need X" is a T5 claim. The users themselves are the T1/T2 source. Always trace the problem to the person experiencing it.

---

## 9. Problem Prioritization

| Problem | Impact (1-5) | Confidence (1-5) | Ease (1-5) | ICE Score | RICE Score | Rank |
|---|---|---|---|---|---|---|
| [Problem 1] | X (TX) | X | X | [I*C*E] | [R*I*C/E] | |
| [Problem 2] | | | | | | |
| [Problem 3] | | | | | | |

*If only one problem is being framed, this section is "Skipped -- single problem, no prioritization needed."*

---

## 10. Recommendations (O->I->R->C->W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see]
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

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---|---|---|---|
| [e.g., "Problem severity vs. opportunity size"] | [Canvas: problem is Critical] | [Opportunity Sizing: breadth is <5%] | [Which matters more and why -- e.g., "Critical pain for a tiny population may not justify investment unless the segment is strategic"] |

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
[Steelmanned argument against the problem definition. What assumption is made? What evidence would disprove it? Scenario where this problem framing leads the team in the wrong direction.]

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
1. **Do not skip sections.** If a section is not applicable, write "Skipped -- [reason]" and move on.
2. **Every table cell with a claim or rating must have an evidence tier tag** -- `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Root Cause Analysis") with insight headers (e.g., "Users Don't Have an Onboarding Problem -- They Have a Trust Problem") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **Progress on the Problem-Solution Fit tests is the single most important output.** If any test is UNVALIDATED, the entire document is a hypothesis -- flag this prominently.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology -- not merely referenced. A PM using this skill produces problem definitions that require these frameworks; without them, the output degrades to opinion and assumption.

### Framework 1: Problem Definition Canvas

The foundational decomposition framework. Forces seven questions that most problem statements skip, producing a structured definition that can be tested and communicated.

**The Seven Dimensions:**

| Dimension | Question | Why It Matters | Common Failure |
|---|---|---|---|
| **Who** | Who *specifically* has this problem? (Segment, not "users") | A problem that "everyone" has is a problem nobody has. Specificity enables research and validation. | "Our users" -- too broad. Which users? New or retained? Power or casual? Enterprise or SMB? |
| **What (goal)** | What are they trying to accomplish? | The goal is the anchor. Solutions that don't serve the goal are features without purpose. | Stating the solution as the goal: "They need a dashboard" vs. "They need to understand their team's performance" |
| **What (current)** | What do they do today to accomplish this goal? | Today's behavior reveals the real competitive set -- including manual processes, workarounds, and "do nothing." | Ignoring workarounds. If users have a workaround, the problem is real but the switching cost is nonzero. |
| **Why painful** | Why is the current approach painful? | Pain is the engine of behavior change. No pain = no switching. | Assumed pain. "Spreadsheets are painful" -- to whom? For what task? At what scale? |
| **Trigger** | What triggers the pain? | Triggers reveal when and where to intervene. A problem that has no trigger has no moment of activation. | Missing the trigger entirely. "Users struggle with reporting" -- when? Monthly close? Ad hoc request? Board prep? |
| **Good state** | What does "good" look like? | The desired end state defines the success criteria for any solution. | Defining "good" as "our feature exists" instead of "the user's outcome is achieved." |
| **Verification** | How would the user know the problem is solved? | Observable success criteria that the user (not the PM) would recognize. | PM-centric success: "We shipped the feature" vs. User-centric success: "I can generate a report in under 2 minutes" |

**Application method:**
1. Fill in each dimension with the best available evidence
2. Tag evidence tier for each cell
3. Identify the weakest cells -- these are research priorities
4. Validate the Canvas with at least one representative user (T2) or behavioral data source (T1) before treating it as complete
5. If >3 cells are T5-T6, the Canvas is a hypothesis, not a problem definition. Flag prominently.

**Decision table -- Canvas completeness:**

| Cells at T1-T2 | Cells at T3-T4 | Cells at T5-T6 | Assessment |
|---|---|---|---|
| 5-7 | 0-2 | 0 | **Validated** -- proceed to solution design |
| 3-4 | 2-3 | 0-1 | **Partially validated** -- targeted research on weak cells |
| 1-2 | 2-3 | 2-3 | **Hypothesis** -- broad research needed before commitment |
| 0 | 0-2 | 5-7 | **Speculation** -- do not proceed to solution design. Run Discovery first. |

---

### Framework 2: 5 Whys / Root Cause Analysis

A systematic peeling technique to find the real problem underneath the presented symptom. Deceptively simple but frequently misapplied. The power is in the discipline, not the counting.

**The 5 Whys Protocol:**

1. **Start with the observable symptom** -- not the stakeholder's interpretation. "Users are churning" (observable) not "Users don't like our product" (interpretation).
2. **Ask "Why?" and answer with evidence, not speculation.** Each layer must cite evidence (even if it's T5-T6). An unevidenced "why" is a guess, not a root cause.
3. **Stop when you reach a cause you can act on** -- not necessarily at "Why 5." Some root causes surface at Why 2. Others require Why 7. The number is a guideline, not a rule.
4. **Branch when "Why?" has multiple valid answers.** Root causes are often multi-factorial. A single-branch 5 Whys misses interaction effects.
5. **Validate the root cause by testing the chain in reverse.** Read the chain backward: "Because [root cause], [cause 4] happens, which causes [cause 3]..." If any link breaks, the chain is wrong.

**Common failure modes in 5 Whys:**

| Failure | Example | Fix |
|---|---|---|
| **Stopping at symptoms** | "Why churn? Bad UX. Let's fix the UX." | Ask why the UX is bad. Is it design? Is it complexity? Is it a mismatch between user expectations and product capability? |
| **Leading the witness** | "Why churn? Because we don't have feature X." | This is a solution disguised as a root cause. Ask: "What goal is the user trying to achieve that they cannot?" |
| **Single-threading** | One linear chain when the real cause is multi-factorial | Branch at layers where multiple causes are plausible. Map the tree, not the line. |
| **Blaming people** | "Why was the release buggy? Because the engineer was careless." | Root causes are systemic, not personal. Ask: "Why did the process allow a careless release?" |
| **Infinite regress** | Going 10+ levels deep into philosophical territory | Stop at the level where you can take a meaningful action. If "Why?" leads to "Because physics," you've gone too far. |

**Output format -- 5 Whys Tree:**
```
Symptom: [Observable problem]
|
+-- Why 1: [First-order cause] (TX: evidence)
    |
    +-- Why 2: [Second-order cause] (TX: evidence)
        |
        +-- Why 3a: [Branch A] (TX: evidence)
        |   |
        |   +-- Why 4a: [Deeper cause] (TX)
        |       |
        |       +-- ROOT CAUSE A: [Actionable root cause] (TX)
        |
        +-- Why 3b: [Branch B] (TX: evidence)
            |
            +-- ROOT CAUSE B: [Actionable root cause] (TX)
```

**Root cause validation checklist:**
- [ ] Reading the chain backward makes logical sense
- [ ] Each link has at least T5-level evidence (not pure speculation)
- [ ] The root cause is something you can act on (not "the market changed")
- [ ] If the root cause were eliminated, the symptom would plausibly disappear
- [ ] You have not disguised a solution as a root cause

---

### Framework 3: Jobs-to-be-Done Problem Framing

Christensen's JTBD framework applied at the problem level -- not the solution level. The core insight: users don't have problems with your product. They have jobs they are trying to accomplish, and your product is one of several things they might "hire" for the job. Understanding the job reveals the real problem; understanding the product reveals only the symptom.

**JTBD Structure for Problem Framing:**

| Dimension | Question | Problem-Level Application |
|---|---|---|
| **Functional job** | What is the user concretely trying to accomplish? | The task itself. "Generate a monthly performance report for my team." |
| **Emotional job** | How does the user want to feel while doing it? | The experience. "Confident that the numbers are accurate. Not anxious about making mistakes." |
| **Social job** | How does the user want to be perceived? | The reputation. "Seen as data-driven and competent by leadership." |

**Why all three dimensions matter for problem framing:**

A PM who sees only the functional job designs a better report builder. A PM who sees the emotional job realizes the real problem is data confidence, not report generation. A PM who sees the social job realizes the user needs their manager to trust the output -- which means the problem might be solved by visible data provenance, not faster report creation.

**Competing "hires" analysis:**

| What they hire today | Job dimensions served | Where it fails | Switching barrier |
|---|---|---|---|
| [e.g., "Manual spreadsheet + email"] | Functional: 3/5, Emotional: 1/5, Social: 2/5 | [Specific failure point] | [Cost of switching away from this] |
| [e.g., "Existing BI tool"] | | | |
| [e.g., "Doing nothing / avoiding the task"] | | | |
| [e.g., "Delegating to someone else"] | | | |

**Critical insight:** "Doing nothing" and "workaround" are the most common competitors in problem framing. If users have a workaround that sort-of works, the problem is real but the switching cost is nonzero. If users are not doing the task at all, either the pain is not severe enough or you have a new-market opportunity.

**Job map -- the consumption chain:**

| Step | What happens | Pain point | Opportunity |
|---|---|---|---|
| 1. Recognize the need | [How do they realize they need to do this?] | | |
| 2. Locate resources | [What inputs, data, people do they need?] | | |
| 3. Prepare | [What setup is required?] | | |
| 4. Execute | [The core task] | | |
| 5. Monitor | [How do they know it's working?] | | |
| 6. Resolve issues | [What goes wrong? How do they fix it?] | | |
| 7. Complete/deliver | [How do they finish and hand off?] | | |

**Decision triggers from JTBD analysis:**

| Finding | Implication | Next action |
|---|---|---|
| Functional job under-served | Feature opportunity -- users cannot accomplish the task adequately | Quantify with Opportunity Sizing (F4) |
| Emotional job under-served | Experience opportunity -- users can accomplish the task but it feels terrible | Deep-dive into trigger and pain (Problem Definition Canvas F1) |
| Social job under-served | Positioning/trust opportunity -- the outcome doesn't carry the right signal | Stakeholder Impact Matrix (F7) to understand perception dynamics |
| All jobs over-served | Over-engineering risk -- users don't need a better solution | Check for disruption from below (simpler, cheaper) |
| "Doing nothing" is the top hire | Pain is not severe enough to drive behavior change, OR user doesn't recognize the problem | Validate severity with T1-T2 evidence. If confirmed low severity, deprioritize. |

---

### Framework 4: Opportunity Sizing Framework

Quantifies the problem space across four dimensions to produce a defensible "is this worth solving?" assessment. Not a TAM calculation -- that comes later. This is problem-level sizing: how big is the pain?

**The Four Dimensions:**

| Dimension | Definition | Measurement approach | Evidence source |
|---|---|---|---|
| **Frequency** | How often does the problem occur per affected user? | Usage logs, support ticket frequency, survey data on task frequency | T1: analytics. T2: user interviews. T4: industry benchmarks. |
| **Severity** | How painful is each occurrence? | Impact on user's goal: blocked, delayed, frustrated, annoyed | T1: abandonment data, churn correlation. T2: user interviews. T5: stakeholder claims. |
| **Breadth** | How many users are affected? | Segment analysis, support ticket volume, feature usage data | T1: analytics. T2: survey with proper sampling. T4: market reports. |
| **Willingness** | Would affected users change behavior to solve this? | Current investment in workarounds, stated willingness to pay/switch, past behavior change | T1: workaround adoption data. T2: willingness-to-pay research. T5: stakeholder assertions. |

**Scoring rubric (1-5 per dimension):**

| Score | Frequency | Severity | Breadth | Willingness |
|---|---|---|---|---|
| **5** | Multiple times daily | Cannot complete goal; abandons/churns | >50% of user base | Actively paying for workarounds or switching to alternatives |
| **4** | Daily | Significant time/effort wasted (>30 min per occurrence) | 25-50% of base | Would switch products to solve this |
| **3** | Weekly | Noticeable friction; uses workaround but unhappy | 10-25% of base | Would try a solution if easy/free |
| **2** | Monthly | Minor annoyance; noticed but tolerated | 5-10% of base | Aware of the pain but not acting on it |
| **1** | Rarely / situational | Barely notices | <5% of base | Does not recognize the problem |

**Composite scoring:**

Opportunity Score = Frequency x Severity x Breadth x Willingness

| Score range | Interpretation | Recommended action |
|---|---|---|
| **300-625** | Critical opportunity. High frequency, severe pain, broad reach, proven willingness. | Prioritize. Proceed to Discovery and Spec Writing. |
| **100-299** | Strong opportunity. Multiple dimensions score well but at least one is moderate. | Investigate the weakest dimension. If it upgrades, proceed. If not, consider scope reduction. |
| **30-99** | Moderate opportunity. Worth further investigation but not a clear priority. | Validate the weakest 2 dimensions with T1-T2 evidence before committing resources. |
| **<30** | Weak opportunity. Multiple dimensions score poorly. | Deprioritize unless strategically important for other reasons (e.g., retention of a key segment). |

**Critical caution:** Opportunity sizing is only as good as the evidence behind each score. A 4x4x4x4 = 256 based on T1 evidence is very different from 4x4x4x4 = 256 based on T5/T6. Always tag evidence tiers per dimension.

**Revenue impact estimation (optional, when data available):**

```
Affected users x Problem frequency x Impact per occurrence (time/money) = Annual problem cost
Annual problem cost x Capture rate (what % of value you can capture) = Addressable opportunity
```

---

### Framework 5: Problem-Solution Fit Assessment

The critical gateway between "interesting problem" and "problem worth solving." Many teams skip this and jump from a plausible-sounding problem directly to building. This framework prevents that.

**The Six Tests:**

| Test | Question | Pass Criteria | Common Ways to Fail |
|---|---|---|---|
| **Existence** | Do real users actually have this problem? | At least 5 independent users report the problem unprompted (T2), or behavioral data shows the pattern (T1) | The problem was reported by sales (T5), not users. Or only 1-2 users mentioned it. |
| **Severity** | Is it painful enough to change behavior? | Users have invested effort in workarounds, complained multiple times, or churned citing this issue | Users acknowledge the problem when asked but have never tried to solve it -- a stated preference, not a revealed one |
| **Frequency** | Does it occur often enough to justify a persistent solution? | Problem occurs at least weekly for the affected segment | Happens once a quarter. Real but not worth a product investment -- consider documentation or support. |
| **Willingness** | Would users adopt a solution? | Evidence of: willingness to pay, willingness to switch, willingness to learn a new tool, or willingness to change workflow | "Yes I'd use that" in an interview (T5, heavily biased) without corroborating behavioral evidence |
| **Solvability** | Can this problem be solved within our constraints? | A plausible solution path exists given technical, business, regulatory, and timeline constraints | The problem is real but the solution requires technology that doesn't exist, regulatory changes, or 10x current resources |
| **Timing** | Why now? What has changed? | A specific trigger: new regulation, market shift, competitor move, technology enablement, or user base reaching critical mass | "We should have done this years ago" -- if the problem existed for years without being solved, ask why. Maybe it was not actually painful enough. |

**Evidence quality requirements per test:**

| Test | Minimum evidence for PASS | What makes it UNVALIDATED |
|---|---|---|
| Existence | T2 (at least 5 user interviews) or T1 (behavioral data showing pattern) | Only T5 (stakeholder says so) or T6 (we assume so) |
| Severity | T1 (churn/abandonment data) or T2 (workaround observation) | Only stated preference ("yes that's annoying") without behavioral corroboration |
| Frequency | T1 (usage logs) or T2 (diary study/survey with methodology) | Estimated without measurement |
| Willingness | T1 (existing workaround adoption) or T2 (structured willingness-to-pay research) | "Would you use this?" in an unblinded interview |
| Solvability | T3 (technical feasibility assessment) + F6 Constraint Map | No technical evaluation; assumed feasible |
| Timing | Any tier with a specific, verifiable trigger | No articulated trigger; "it's always been a problem" |

**Decision matrix:**

| # Tests PASS | # Tests FAIL | # Tests UNVALIDATED | Verdict |
|---|---|---|---|
| 6 | 0 | 0 | **Validated problem.** Proceed to Discovery/Spec Writing. |
| 4-5 | 0-1 | 0-2 | **Promising.** Investigate failing/unvalidated dimensions. Design targeted research. |
| 3 | 1-2 | 1-3 | **Hypothesis.** Do not commit engineering resources. Run Discovery to validate. |
| 0-2 | 3+ | Any | **Not a problem worth solving** in current framing. Reframe or deprioritize. |

---

### Framework 6: Constraint Mapping

Maps the boundaries of the solution space BEFORE any solution work begins. Constraints are not obstacles -- they are design parameters. A problem framed without constraints produces solutions that can't be built, can't be shipped, or can't be adopted.

**Constraint Taxonomy:**

| Type | Definition | Examples | Typical Source | Negotiability |
|---|---|---|---|---|
| **Technical** | Limitations of existing systems, architecture, or technology | Legacy API limits, latency requirements, browser compatibility, data format constraints | Engineering assessment (T3) | Often negotiable with investment |
| **Business** | Commercial limitations imposed by business model, pricing, or strategy | Cannot increase pricing, must support free tier, cannot cannibalize existing product | Business stakeholders (T5) | Negotiable but politically expensive |
| **Regulatory** | Legal or compliance requirements | GDPR, HIPAA, SOC2, accessibility standards, industry-specific regulations | Legal/compliance team (T3) | Non-negotiable (but interpretation may vary) |
| **Timeline** | Time constraints on delivery | Board meeting deadline, competitive response window, contractual commitment | Business stakeholders (T5) | Partially negotiable (scope can flex if timeline can't) |
| **Resource** | People, budget, and tooling available | Team size, skill gaps, budget ceiling, infrastructure limits | Org leadership (T5) | Negotiable with strong business case |
| **Organizational** | Decision-making structure, political dynamics, approval chains | Multi-team dependencies, VP sign-off required, cross-functional alignment needed | Observation (T3) or experience (T6) | Partially negotiable |
| **User behavioral** | What users will and will not do | Won't install an app, won't change workflow, won't pay more than X | User research (T2) or behavioral data (T1) | Non-negotiable (you adapt to users, not vice versa) |

**Constraint severity scoring:**

| Severity | Definition | Impact on solution space |
|---|---|---|
| **Hard** | Cannot be violated under any circumstances | Eliminates entire solution classes |
| **Firm** | Can be violated with significant cost or approval | Constrains but does not eliminate solutions |
| **Soft** | Can be violated if justified | Influences solution preference, does not constrain |

**Constraint interaction analysis** -- constraints rarely operate independently. Identify compound constraints:

| Constraint A | + Constraint B | = Compound effect |
|---|---|---|
| [e.g., "6-week timeline"] | [e.g., "2 engineers"] | [e.g., "Scope must be cut by ~60% vs. ideal solution"] |
| [e.g., "Cannot raise price"] | [e.g., "Must improve margins"] | [e.g., "Solution must reduce cost-to-serve, not increase revenue"] |

**The Assumed Constraint Trap** -- many constraints are assumed, not verified. For each constraint, ask:
1. **Who said this is a constraint?** (Source and evidence tier)
2. **When was it last validated?** (Constraints change -- a technical limitation from 2 years ago may no longer exist)
3. **What would it cost to remove this constraint?** (Some "hard" constraints dissolve with a modest investment)
4. **Is this a constraint or a preference?** ("We don't do mobile" may be a strategy choice, not a constraint)

List every assumed constraint in the Assumption Registry.

---

### Framework 7: Stakeholder Impact Matrix

Maps who cares about this problem, how much power they have, and what this means for problem prioritization and solution design. The most politically dangerous part of problem framing -- and therefore the most important to do rigorously.

**Stakeholder Identification Protocol:**

Start by listing every person or group who is affected by, influences, or has decision authority over this problem.

| Category | Who to include | Why they matter |
|---|---|---|
| **End users** | The people who directly experience the problem | They ARE the problem. Their behavior is the T1 evidence. |
| **Buyers** | The people who approve purchase/adoption decisions | They decide whether a solution gets funded or adopted |
| **Influencers** | People who shape the buyer's or user's opinion | They amplify or suppress problem visibility |
| **Blockers** | People who can prevent progress | They define constraints you may not see |
| **Champions** | Internal advocates who want this problem solved | They provide political capital and escalation paths |
| **Affected bystanders** | People impacted by a solution even if they don't have the problem | A solution for Team A that creates work for Team B has a hidden stakeholder |

**Power-Interest Grid Scoring:**

| Dimension | Score 5 | Score 3 | Score 1 |
|---|---|---|---|
| **Power** | Can unilaterally approve or kill | Voice in the room; influence but not authority | No decision authority |
| **Interest** | Problem directly affects their core metrics | Aware and somewhat affected | Unaware or unaffected |

**The Proxy Stakeholder Problem:**

The most dangerous failure in stakeholder analysis: solving for the wrong person.

| Signal | What it means | What to do |
|---|---|---|
| The person requesting the analysis is not the person with the problem | Problem definition may reflect the requester's framing, not the user's reality | Validate problem definition with actual end users (T2) |
| "My team needs X" from a manager | Manager's interpretation of team needs; may not match what the team actually struggles with | Interview the team directly (T2); compare with manager's framing |
| Sales team reports "customers want Y" | Sales attribution bias: customers said something; sales interpreted it through their lens | Access customer verbatims directly or conduct post-decision interviews (T1-T2) |
| Executive asserts "the problem is Z" | HiPPO (Highest-Paid Person's Opinion). May be correct but is T5 evidence regardless | Validate with T1-T2 evidence. If executive is correct, the data will confirm it. If not, you need the data to make the case. |

---

### Framework 8: Problem Prioritization (ICE/RICE Variant)

A structured scoring methodology for ranking multiple candidate problems. Uses explicit rubrics to prevent the two most common prioritization failures: (1) intuition masquerading as analysis, and (2) squeaky-wheel bias (the loudest stakeholder's problem gets priority).

**ICE Scoring (when reach data is unavailable):**

| Dimension | Definition | Scoring rubric |
|---|---|---|
| **Impact** | How much would solving this problem improve the target outcome? | 5: Transforms the experience / eliminates churn driver. 4: Major improvement. 3: Noticeable improvement. 2: Minor improvement. 1: Marginal. |
| **Confidence** | How confident are we that this is a real, solvable problem? | 5: T1-T2 evidence, all PSF tests pass. 4: T2-T3 evidence, most PSF tests pass. 3: T3-T4 evidence, some PSF tests unvalidated. 2: T5 evidence, most PSF tests unvalidated. 1: T6 / assumption only. |
| **Ease** | How easy is it to solve this problem given constraints? | 5: Can solve in <2 weeks with existing team. 4: 2-6 weeks. 3: 1-3 months. 2: 3-6 months. 1: >6 months or requires new capabilities. |

**ICE Score = Impact x Confidence x Ease** (range: 1-125)

**RICE Scoring (when reach data is available):**

| Dimension | Definition | Scoring rubric |
|---|---|---|
| **Reach** | How many users are affected in a given time period? | Actual number of affected users per quarter (from T1 data) |
| **Impact** | How much would solving this improve their experience? | 3: Massive. 2: High. 1: Medium. 0.5: Low. 0.25: Minimal. |
| **Confidence** | How confident are we in the estimates? | 100%: T1-T2 validated. 80%: T2-T3 evidence. 50%: T4-T5 evidence. 20%: Assumption/inference. |
| **Effort** | Person-weeks to solve | Estimated person-weeks (from engineering assessment) |

**RICE Score = (Reach x Impact x Confidence) / Effort**

**Anti-gaming rules for prioritization scoring:**

| Rule | Why |
|---|---|
| **Score each dimension independently.** Do not reason backward from a desired priority. | Prevents anchoring bias: "This should be #1, so let me score it 5/5/5." |
| **Document the evidence behind each score.** | Prevents phantom precision: a score of 4 must cite specific evidence, not gut feel. |
| **Disclose the scorer.** | Prevents political scoring: knowing who scored what enables accountability. |
| **Re-score if new evidence arrives.** | Prevents stale priorities: a problem scored 3 months ago on T5 evidence may now have T1 data that changes the score. |
| **Do not average across scorers without discussing divergence.** | Prevents false consensus: if one scorer gives Impact=5 and another gives Impact=2, averaging to 3.5 hides a genuine disagreement that needs resolution, not arithmetic. |

**Prioritization output format:**

| Rank | Problem | Impact | Confidence | Ease/Effort | Score | Evidence quality | Recommended action |
|---|---|---|---|---|---|---|---|
| 1 | [Problem name] | X (TX) | X (TX) | X (TX) | [Score] | [% of scores at T1-T2] | [Proceed / Investigate / Deprioritize] |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Decision rules:**
- **Score > 75 (ICE) or top quartile (RICE):** Proceed to Discovery or Spec Writing
- **Score 30-75 (ICE):** Investigate -- targeted research on weakest dimension
- **Score < 30 (ICE):** Deprioritize unless strategic override (document the override and its rationale)
- **Confidence score <= 2 for top-ranked problem:** Do not proceed to solution design. Run Discovery first to upgrade confidence.

---

## Evidence Standards

### Evidence Quality Tiers (adapted for problem evidence)

| Tier | Source Type | Weight | Example |
|---|---|---|---|
| **Tier 1** | Direct user behavioral data (what people DO) | Highest | Usage analytics showing abandonment, support ticket patterns, churn data correlated with problem area, session recordings showing struggle, workaround adoption rates |
| **Tier 2** | Primary user research (structured methodology) | High | User interviews with 5+ participants, contextual inquiry, diary studies, usability testing, properly sampled surveys |
| **Tier 3** | Expert analysis with disclosed methodology | Medium-High | UX research reports, domain expert assessments, published case studies with methodology |
| **Tier 4** | Market/industry reports | Medium | Gartner/Forrester problem-area reports, industry surveys, benchmark studies (useful for breadth estimates, less for specific problem validation) |
| **Tier 5** | Stakeholder assertions | Low-Medium | Internal claims from executives, sales team anecdotes, customer success team reports (useful as signal, not as evidence for problem severity) |
| **Tier 6** | Assumptions/inference | Low | First-principles reasoning, analogies from other products/markets, "seems like" conclusions (starting point for investigation, never for commitment) |

**Triangulation Rule:** No problem framing conclusion rests on a single evidence tier. Minimum 2 tiers, ideally 3.

**Staleness Rule:** For every claim, note the source date. If no source newer than 6 months can be identified, flag as `[POTENTIALLY STALE]`. A user interview from 18 months ago may describe a problem that has since been solved by a competitor or workaround.

**Annotation Convention:** Use inline tags throughout -- not just footnotes. Per-cell annotation in matrices: `Critical (T1: churn data)` or `Major (T2: 8/12 users reported)` or `Assumed (T6: inferred from analogous product)`. An end-of-section source list supplements but does not substitute for inline tagging.

### Behavioral > Stated Preference

The single most important evidence standard in problem framing:

| Evidence type | What it tells you | How to weight it |
|---|---|---|
| **What users DO** (T1) | Revealed preference -- the actual problem and its actual severity | Highest weight. Users who churn, abandon tasks, build workarounds, or pay for alternatives are showing you the problem. |
| **What users SAY** (T2-T5) | Stated preference -- what they believe the problem is | Moderate weight. Valuable for understanding context and emotion, but subject to recall bias, social desirability, and post-hoc rationalization. |
| **What stakeholders CLAIM** (T5) | Third-party interpretation of user problems | Low weight for problem definition. Useful as hypothesis generation. Always validate with T1-T2. |
| **What we INFER** (T6) | Our model of the problem | Lowest weight. Starting point for investigation. Never sufficient for commitment. |

**The Behavioral-Stated Gap:**
When behavioral data (T1) contradicts stated preference (T2-T5), always weight behavioral data more heavily. Users who say "I love this feature" but never use it do not have the problem that feature solves. Users who say "this isn't a big deal" but spend 2 hours a week on workarounds DO have a problem worth solving.

---

## Application Method

### Quick Version (10 steps for experienced practitioners)

0a. **Context Fitness Check** -- Verify a Problem Definition Document is the right artifact. Is the problem genuinely unclear? Do you have evidence access? Does the team expect problem framing or a solution?
0b. **Route to framework subset** -- Identify question type from the routing table. Select 3-4 primary frameworks. Note which to skip.
1. **Write the one-sentence problem statement** -- [Who] experiences [what pain] when [trigger], resulting in [consequence]. Tag confidence and evidence tier.
2. **Complete the Problem Definition Canvas** -- Fill all 7 dimensions. Identify the weakest cells as research priorities.
3. **Run 5 Whys on the presented problem** -- Peel to the root cause. Branch when multiple causes exist. Validate by reading the chain backward.
4. **Frame with JTBD** -- Identify functional, emotional, and social jobs. Map competing "hires." Determine which dimensions are under-served.
5. **Size the opportunity** -- Score Frequency x Severity x Breadth x Willingness with evidence per dimension.
6. **Run Problem-Solution Fit tests** -- All 6 tests with evidence. Flag UNVALIDATED tests prominently.
7. **Map constraints** -- All 7 types. Score severity. Identify compound constraints. Flag assumed constraints.
8. **Build the Stakeholder Impact Matrix** -- Power x Interest for each stakeholder. Identify proxy stakeholders.
9. **Prioritize** (if multiple problems) -- ICE or RICE with explicit scoring rubrics and anti-gaming rules.
10. **Cascade every finding to O->I->R->C->W** -- Every key finding gets the full cascade. Write the Executive Summary last.

### Full Version (detailed steps with decision points)

**Step 1: Write the Problem Statement**

Format: **[Who] experiences [what pain] when [trigger/context], resulting in [measurable consequence].**

| Component | Good example | Bad example | Why |
|---|---|---|---|
| Who | "Enterprise data analysts in teams of 5+" | "Users" | Specificity enables validation |
| What pain | "Cannot generate cross-team reports without manually merging data from 3+ sources" | "Struggle with reporting" | The mechanism is stated, not just the category |
| Trigger | "When preparing for monthly business reviews" | (omitted) | Triggers reveal when to intervene |
| Consequence | "Spending 4-6 hours per report, with 30% containing errors that require rework" | "Wasting time" | Quantified impact enables opportunity sizing |

**Decision point:** If any component relies on T5-T6 evidence, flag for validation.

**Step 2: Problem Definition Canvas** -- Apply F1. Tag evidence per cell. If >3 cells at T5-T6, the Canvas is a hypothesis; recommend Discovery research before proceeding.

**Step 3: Root Cause Analysis** -- Apply F2 (5 Whys). Start from observable symptom, branch at multi-factorial nodes, validate by reading the chain backward. **Key decision:** If root cause differs from presented problem, surface the divergence in Executive Summary and Cross-Framework Contradictions.

**Step 4: JTBD Problem Framing** -- Apply F3. Map functional/emotional/social jobs and competing hires. **Key decision:** If "doing nothing" is the dominant hire, the solution must have near-zero switching cost to succeed.

**Step 5: Opportunity Sizing** -- Apply F4. Score all 4 dimensions with evidence tiers. **Key decision:** If any dimension scores 1, the opportunity has a structural weakness regardless of other scores.

**Step 6: Problem-Solution Fit** -- Apply F5. Run all 6 tests. **This is the gateway.** If problem passes all tests, downstream work is justified. If not, next step is research, not solution design.

**Step 7: Constraint Mapping** -- Apply F6. All 7 types with severity. Flag assumed constraints for the Assumption Registry.

**Step 8: Stakeholder Impact Matrix** -- Apply F7. Score Power x Interest. Identify proxy stakeholders.

**Step 9: Prioritize** (if multiple problems) -- Apply F8 ICE/RICE with anti-gaming rules.

**Step 10: Cascade and Synthesize** -- Write Cross-Framework Contradictions, Assumption Registry, Adversarial Self-Critique, Recommendations (O->I->R->C->W), and Executive Summary (last but placed first).

### Mandatory Output: Assumption Registry

Every Problem Definition Document must include a standalone assumption registry. List every load-bearing assumption the analysis depends on:

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | [e.g., "Users are spending 4-6 hours per report"] | F4 Opportunity Sizing (Frequency, Severity) | M | T2: 3 user interviews. Need larger sample. | Time-and-motion study shows <1 hour per report. |
| 2 | [e.g., "The legacy API cannot support real-time sync"] | F6 Constraint Mapping (Technical) | L | T5: Engineering lead's verbal estimate. No formal assessment. | Formal technical spike shows API can handle it with minor modifications. |
| 3 | [e.g., "Users would switch from their current workaround"] | F5 Problem-Solution Fit (Willingness test) | L | T6: Inferred from interview sentiment. No behavioral data. | Prototype test shows <10% adoption despite expressed interest. |

Minimum 3 assumptions. Any assumption at L confidence must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the analysis, execute this step before delivering output:

> *"Now identify >=3 genuine weaknesses in this problem definition. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this problem framing leads the team in the wrong direction entirely?"*

- If you cannot find real weaknesses, you haven't looked hard enough.
- Bear cases must be steelmanned -- not just listed as possibility but argued as forcefully as possible.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the assumption registry -- it is a distinct, explicitly adversarial voice.

### Mandatory Output: Revision Triggers

When should this Problem Definition Document be revisited? Specific, observable conditions:

| Trigger type | Example | What to re-assess |
|---|---|---|
| **Evidence upgrade** | User research completes that validates or invalidates a T5-T6 assumption | All sections that depended on the upgraded assumption |
| **Market shift** | A competitor launches a solution for this problem | Opportunity Sizing (willingness may change), Problem-Solution Fit (timing test) |
| **Constraint change** | A technical constraint is removed or a new regulation is introduced | Constraint Map, Problem-Solution Fit (solvability test) |
| **Stakeholder change** | A key champion leaves or a new decision-maker arrives | Stakeholder Impact Matrix, political feasibility |
| **Data contradicts hypothesis** | Behavioral data (T1) shows the problem is less severe than assumed | The entire Problem Definition Canvas; may require re-framing |
| **Time elapsed** | 3 months since document creation without action | Full document review -- problem landscapes shift |

---

## Quality Gradients

### Intern Tier
- Accepts the presented problem at face value without decomposition
- Problem statement is a restated feature request ("users need a dashboard")
- No evidence tiers -- stakeholder assertions treated as facts
- No root cause analysis -- symptom is treated as the problem
- No opportunity sizing -- "this is important" without quantification
- No constraint mapping -- solutions are proposed without understanding boundaries
- Missing: JTBD framing, stakeholder analysis, any form of prioritization methodology
- Output: a brief or a feature request, not a problem definition

### Consultant Tier
- Problem decomposed using at least 3 frameworks (Problem Definition Canvas, 5 Whys, Opportunity Sizing minimum)
- Evidence is tiered -- distinguishes T1 behavioral data from T5 stakeholder assertions
- Root cause analysis goes at least 3 layers deep
- Opportunity sized with explicit scoring rubric
- Constraints mapped by type with severity ratings
- Every finding has a "So What" with recommended action
- Problem-Solution Fit assessed with evidence per test
- Missing: JTBD depth, full stakeholder dynamics, assumed constraint identification, adversarial self-critique, evidence-limited flagging

### Elite Tier
- All 8 frameworks applied (or explicitly skipped with rationale) with scoring rubrics and decision tables
- Evidence triangulated -- no problem definition conclusion rests on a single tier
- Root cause analysis branches for multi-factorial causes; validated by reading chain backward
- JTBD analysis covers all three dimensions (functional, emotional, social) with competing hires mapped
- Opportunity sized with per-dimension evidence tiers
- Problem-Solution Fit: all 6 tests completed with specific evidence requirements
- Constraints include assumed constraint identification and interaction analysis
- Stakeholder Impact Matrix identifies proxy stakeholders and traces problems to the person experiencing them
- Cross-framework contradictions surfaced explicitly
- Assumption Registry with 3+ load-bearing assumptions and invalidation criteria
- Adversarial Self-Critique with 3+ genuine weaknesses steelmanned
- Every recommendation uses the O->I->R->C->W cascade
- The document is navigable by non-creators: reading guide, notation key, layered depth
- Produces a Problem Definition Document that any downstream skill (Discovery, Competitive Analysis, Spec Writing) can consume as structured input

---

## Failure Modes

**FM-1: Solution Masquerading as Problem**
*What it looks like:* "The problem is that we don't have a mobile app." This is a solution (mobile app), not a problem. The problem might be "field sales reps cannot access customer data during meetings."
*Why it happens:* Stakeholders naturally think in solutions. The jump from "I'm frustrated" to "I need feature X" is instant and unconscious.
*Detection:* Does the problem statement contain a product, feature, or technology name? If yes, it's a solution, not a problem.
*Correction:* Ask "Why do you need [solution]? What are you trying to accomplish? What happens if you don't have it?" Keep asking until you reach the pain, not the prescription.

**FM-2: Problem Too Broad (Boiling the Ocean)**
*What it looks like:* "Our users have a bad experience." This is everything and nothing. It cannot be researched, sized, or solved because it contains every possible problem.
*Why it happens:* Fear of missing something. Or lack of data to narrow. Or a stakeholder who wants to appear strategic rather than specific.
*Detection:* Can you design a study to validate this problem in 2 weeks? If the answer is "no, because it's too big," the problem is too broad.
*Correction:* Decompose. Use the Problem Definition Canvas to force specificity on "who," "when," and "why painful." A broad problem is actually a collection of specific problems -- name them individually.

**FM-3: Problem Too Narrow (Solving a Symptom)**
*What it looks like:* "The submit button is confusing." This may be true, but is this THE problem? Or is it a symptom of a deeper problem (e.g., the entire form flow is unclear, and users express confusion at the final step because that's where they give up)?
*Why it happens:* Narrow problems are easy to solve. PMs gravitate toward solvability over importance.
*Detection:* Apply 5 Whys. If the first "Why?" reveals a bigger problem, the original framing was too narrow.
*Correction:* Peel at least 3 layers before accepting a problem statement. A narrow problem is a valid finding only if it's confirmed as the root cause, not a symptom.

**FM-4: Proxy Stakeholder (Solving for the Wrong Person)**
*What it looks like:* A VP says "our users need better reporting." The PM builds a problem definition around reporting. But the users actually need faster data access -- the VP interpreted their complaints through a reporting lens because that's what the VP cares about.
*Why it happens:* Authority bias. The person with the most organizational power shapes the problem definition, even when they are not the person experiencing the problem.
*Detection:* Who is the source of the problem statement? If it's not the person experiencing the problem, it's a proxy. Check: has anyone who actually has the problem been consulted?
*Correction:* Always trace the problem to the person experiencing it. Use Framework 7 (Stakeholder Impact Matrix) to distinguish presenters from experiencers. Validate with T1-T2 evidence from actual users.

**FM-5: Assumed Severity (No Evidence the Problem Is Painful Enough)**
*What it looks like:* "Users are frustrated with onboarding." How frustrated? Enough to churn? Enough to complain? Or enough to notice but not enough to change behavior? The problem definition assumes high severity without measuring it.
*Why it happens:* Severity is hard to measure. Existence is easier to establish than severity. So the PM proves the problem exists and assumes it's severe.
*Detection:* Check the Severity dimension in Opportunity Sizing (F4). Is it scored with T1-T2 evidence or T5-T6? Check Problem-Solution Fit (F5) Severity test: PASS or UNVALIDATED?
*Correction:* Require behavioral evidence of severity: churn data, time-on-task data, support ticket volume, workaround adoption. If behavioral evidence is unavailable, flag severity as `[EVIDENCE-LIMITED]` and design research to validate it.

**FM-6: Missing Constraints (Solution Space Wider Than Reality Allows)**
*What it looks like:* A beautifully framed problem with a clear statement, validated severity, and quantified opportunity -- followed by a solution that can't be built because the technical architecture doesn't support it, or can't be shipped because of regulatory requirements nobody checked.
*Why it happens:* Problem framing and constraint mapping are done by different people (PM vs. engineering, PM vs. legal) or at different times. The problem definition is "complete" before constraints are considered.
*Detection:* Is Framework 6 (Constraint Mapping) completed before any solution discussion begins? Are all 7 constraint types addressed?
*Correction:* Make Constraint Mapping a required step in the Problem Definition Document, not a downstream activity. Include it before the Recommendations section.

**FM-7: Consensus Problem (Everyone Agrees Because No One Committed)**
*What it looks like:* The problem statement is unanimously accepted in a meeting. Nobody pushes back. This feels like alignment -- but it may mean the problem is defined so vaguely that everyone can project their own interpretation onto it.
*Why it happens:* Vague problem statements generate false consensus. "We need better analytics" is agreeable to everyone because it means something different to each person.
*Detection:* Ask each stakeholder independently: "In your own words, what specific problem are we solving and for whom?" If the answers diverge, the consensus was performative.
*Correction:* Use the Problem Definition Canvas to force specificity. Disagreement on specific dimensions (who? what trigger? what's "good"?) is healthy -- it reveals the real problem definition work that needs to happen.

**FM-8: Right Problem, Wrong Question (Context Fitness)**
*What it looks like:* A rigorous problem definition for an area where the team doesn't actually need problem framing -- they need competitive analysis, or metric design, or a spec. The problem is real, but the Problem Definition Document is the wrong artifact.
*Why it happens:* A team member heard "start with the problem" and triggered this skill for a situation where the problem is already validated. Or the real need is a different type of analysis.
*Detection:* Run the Context Fitness Check (Step 0). If the problem is already well-defined and validated, a Problem Definition Document is overhead.
*Correction:* Redirect to the appropriate skill. If the problem is validated, proceed to Spec Writing. If the question is "how do we compete," use Competitive Analysis. If the question is "what metrics do we track," use Metric Design.

**FM-9: Expert-Only Document (Output Not Navigable by Non-Creators)**
*What it looks like:* Dense with framework names (JTBD, ICE/RICE, PSF Assessment), notation (T1-T6, H/M/L, O->I->R->C->W), and jargon that assumes the reader built the analysis. The VP cannot find the conclusion. The engineer cannot find the constraints.
*Why it happens:* The skill optimizes for analytical completeness, not reader comprehension. The author knows all the notation; the reader doesn't.
*Detection:* Show the output to someone who didn't request it. If they need more than 60 seconds to find the core problem statement, or if they ask "what does T2 mean?", the document fails the reader test.
*Correction:* The output template mandates a "How to Read This Document" section and a Notation Key before the analysis begins. The Executive Summary uses zero framework jargon -- plain language a non-PM exec can act on. Every framework reference gets a one-line contextual explanation the first time it appears.

---

## What's Next

-> This skill's output feeds into: **Discovery & Research** (problem definition identifies what to research and validate), **Competitive & Market Analysis** (a well-framed problem focuses competitive analysis on the right market), **Spec Writing** (the Problem Definition Document defines WHAT to solve; the spec defines HOW), **Metric Design & Experimentation** (problem framing defines the outcomes that metrics must measure)
<- This skill works best after: Raw context -- a vague problem, a stakeholder request, a feature idea that needs decomposition, an underperforming product area, or a strategic initiative kickoff
* **Start here if:** You are unsure what problem you are solving, who has it, whether it matters, or what to do about it. This is the first skill in the chain.

**For a full product cycle:** **[THIS SKILL]** -> Discovery & Research -> Competitive & Market Analysis -> Spec Writing -> Metric Design & Experimentation -> ongoing measurement loop

**Chain interface:**
- **Receives:** Raw context -- a vague problem, a feature request, a stakeholder concern, a performance issue, or a strategic initiative that needs problem definition. No structured input is required; the skill's purpose is to create structure from ambiguity.
- **Produces:** Problem Definition Document -- a structured artifact with: validated problem statement, root cause analysis, JTBD framing, quantified opportunity size, Problem-Solution Fit assessment, constraint map, stakeholder matrix, and prioritization (if multiple problems). Every claim is evidence-graded.
- **Handoff artifact:** The Problem Definition Document's "Problem Statement" (section 1) maps directly to Discovery & Research input (what to investigate). The "Opportunity Sizing" (section 5) maps to Competitive Analysis input (market/problem size). The "Constraint Map" (section 7) maps to Spec Writing input (what limits the solution). The "Problem-Solution Fit Assessment" (section 6) determines whether downstream work is justified at all.

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

**Context and fitness:**
- [ ] Context Fitness Check passed: problem is genuinely unclear or contested
- [ ] If no T1-T2 data: flagged prominently; confidence capped at M for severity claims
- [ ] How to Read This Document section present with role-based reading guide
- [ ] Notation Key present: H/M/L, T1-T6, O->I->R->C->W, problem severity ratings all explained
- [ ] Executive Summary uses zero framework jargon -- plain language only
- [ ] Framework selection routing done (Step 0b) -- primary frameworks identified, irrelevant frameworks skipped

**Problem definition core:**
- [ ] One-sentence problem statement written with [Who], [What pain], [Trigger], [Consequence]
- [ ] Problem statement tagged with confidence (H/M/L) and evidence tier
- [ ] Problem Definition Canvas completed -- all 7 dimensions with evidence tiers
- [ ] Canvas completeness assessed: how many cells at T1-T2 vs. T5-T6?
- [ ] Root Cause Analysis completed: 3+ layers, branched where applicable, validated in reverse
- [ ] Root cause divergence flagged if root cause differs from presented problem
- [ ] JTBD framing completed: functional, emotional, social job dimensions identified
- [ ] Competing "hires" mapped: including workarounds, doing nothing, and competitor products
- [ ] Consumption chain (job map) completed with pain points per phase

**Sizing and validation:**
- [ ] Opportunity Sizing completed: all 4 dimensions scored with rubric, evidence per dimension
- [ ] Composite Opportunity Score calculated with interpretation
- [ ] Problem-Solution Fit Assessment completed: all 6 tests with evidence
- [ ] Tests marked UNVALIDATED are flagged prominently; document labeled as hypothesis if >2 unvalidated
- [ ] Decision rule from PSF assessment stated clearly

**Constraints and stakeholders:**
- [ ] Constraint Map completed: all 7 constraint types assessed with severity scoring
- [ ] Compound constraints identified
- [ ] Assumed constraints flagged and listed in Assumption Registry
- [ ] Stakeholder Impact Matrix completed with Power/Interest scoring
- [ ] Proxy stakeholders identified: gap between problem presenter and problem experiencer flagged

**Prioritization (if multiple problems):**
- [ ] ICE or RICE scoring applied with explicit rubrics
- [ ] Anti-gaming rules followed: evidence cited per score, scorers disclosed, divergence discussed
- [ ] Prioritized output table with recommended action per problem

**Format Rules compliance:**
- [ ] H/M/L confidence levels explicit on every problem framing conclusion (no weasel words)
- [ ] Per-cell evidence tier annotation in ALL tables (T1-T6 inline, not just section footnotes)
- [ ] O->I->R->C->W cascade applied to ALL recommendations
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source >6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key conclusion resting only on T4-T6 evidence
- [ ] Contradictions between frameworks surfaced explicitly (not resolved artificially)
- [ ] Every framework reference gets a one-line contextual explanation on first appearance

**Mandatory output sections:**
- [ ] Cross-Framework Contradictions section completed
- [ ] Assumption Registry present with >=3 load-bearing assumptions with confidence, evidence, and invalidation conditions
- [ ] L-confidence assumptions flagged `[EVIDENCE-LIMITED]` inline
- [ ] Adversarial Self-Critique completed: >=3 genuine weaknesses steelmanned with watch indicators
- [ ] Revision Triggers defined: specific, observable conditions that would require re-assessment
- [ ] Recommendations use O->I->R->C->W cascade (not bare assertions)
