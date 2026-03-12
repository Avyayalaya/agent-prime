---
name: stakeholder-alignment
description: "Use when navigating organizational alignment — stakeholder mapping, influence analysis, coalition building, decision archaeology, cross-functional alignment, executive buy-in, or any situation where the path to a decision runs through multiple people with different interests. Produces a stakeholder alignment strategy, not a RACI matrix."
version: "1.0.0"
type: "codex"
tags: ["Leadership", "Communication", "Influence", "Organizational"]
created: "2026-03-12"
valid_until: "2026-09-12"
derived_from: "agents/connector/prompt.md"
tested_with: []
license: "MIT"
capability_summary: "Produces a stakeholder alignment strategy with power-interest-position mapping, coalition analysis, decision archaeology, sequenced alignment plan, per-stakeholder communication strategies, and objection pre-emption playbooks."
input_schema:
  decision_or_initiative: "string — what needs alignment"
  stakeholders: "array[{name: string, role: string, known_position: string}] — optional, known stakeholders"
  context: "string — organizational context, political dynamics, history"
  desired_outcome: "string — what 'aligned' looks like for this decision"
  timeline: "string — optional, when the decision must be made"
output_schema:
  executive_summary: "Zero-jargon alignment situation assessment, ≤300 words"
  stakeholder_map: "Power-Interest-Position matrix with scoring"
  coalition_analysis: "Allies, opponents, swing voters, power brokers"
  decision_archaeology: "Why stakeholders hold current positions"
  alignment_sequence: "Ordered approach plan with timing"
  communication_strategies: "Per-stakeholder framing, format, messenger"
  objection_playbook: "Anticipated objections with steel-manned responses"
  assumption_registry: "Load-bearing assumptions about stakeholder positions"
  self_critique: "≥3 genuine weaknesses in this alignment strategy"
example_invocation: "examples/USE_CASES.md"
---

## Purpose

Produce an elite-tier stakeholder alignment strategy that maps power, interest, and position for every relevant stakeholder, uncovers the historical and incentive structures behind their positions, sequences the alignment approach for maximum coalition momentum, and delivers per-stakeholder communication playbooks a PM cannot produce unaided. The output is a Stakeholder Alignment Strategy — not a RACI matrix, but a political map of who needs to move, why they haven't, and exactly how to move them.

## When to Use / When NOT to Use

**Use this skill when:**
- A decision requires buy-in from 3+ stakeholders with different interests
- You're navigating cross-functional alignment (PM, Eng, Design, Legal, Finance, Exec)
- You need executive sponsorship for an initiative that changes priorities, budgets, or org structure
- A previous alignment attempt failed and you need to understand why
- You sense hidden resistance (silence, delegation, "let's revisit") and need to diagnose it
- You're sequencing a multi-week alignment campaign before a major decision point
- You inherited a project and need to understand the political landscape

**Do NOT use this skill when:**
- You need a RACI matrix (just build one directly — RACI assigns roles, it does not build agreement)
- The decision is purely technical with one decision-maker (no alignment needed)
- You need team process design (use Spec Writing for how the team works)
- You need competitive intelligence to make the decision itself (use Competitive & Market Analysis first, then align stakeholders on the recommendation)
- The decision has already been made and you need execution planning (use Spec Writing)

**Anti-inputs (what this skill does NOT handle):**
- Product specification or feature prioritization (-> Spec Writing skill)
- Customer research or user needs (-> Discovery & Research skill)
- Market or competitive analysis (-> Competitive & Market Analysis skill)
- Meeting facilitation or agenda design (direct request, no skill needed)
- Performance management or personnel decisions (HR domain, not PM tooling)

---

## Context Gate (Step -1)

Before building a Stakeholder Alignment Strategy, verify this is the right artifact.

| Question | If Yes | If No |
|---|---|---|
| **Does this decision genuinely require alignment across multiple stakeholders?** | Proceed. This is exactly when you need it. | If one person decides, skip this skill. Write a 1-page brief for that decision-maker instead. A Stakeholder Alignment Strategy for a single-approver decision is overhead. |
| **Do you have access to stakeholder positions (stated or inferred)?** | Strategy can produce H-confidence conclusions about alignment paths. | Flag prominently: "This alignment strategy is built from inference and secondhand input (T5-T6). All position assessments are hypotheses — validate with direct conversations before executing the alignment sequence." Cap confidence at M for all position claims. |
| **Is the requester asking for alignment or already asking for a communication plan?** | Proceed with full analysis — alignment strategy precedes communication. | If stakeholder positions are already understood and the request is "how do I present this," the alignment mapping may be unnecessary. Produce a lighter Communication Strategy section without full Decision Archaeology. |
| **Has a previous alignment attempt failed on this decision?** | Decision Archaeology (F3) is load-bearing. Apply it fully. Past failures shape current positions — you cannot align without understanding history. | If this is a fresh initiative with no prior attempts, Decision Archaeology focuses on adjacent decisions and incentive structures, not failure recovery. |
| **Is there a hard deadline for the decision?** | Time-box the alignment sequence. Flag stakeholders who cannot be fully aligned before the deadline — they need a different engagement strategy (pre-commit, escalation, or accommodation). | Full alignment sequence with no artificial compression. |

**If the core answer is "this is a single-approver decision":** State this prominently. Recommend a direct brief or the Narrative Building skill instead. A Stakeholder Alignment Strategy for a unilateral decision is waste.

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are quality enforcement mechanisms, not style preferences.

1. **Take positions on stakeholder assessments. Never hedge with weasel words.** "Likely supportive," "may resist," "could be convinced" are banned. Replace with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"VP Engineering is a blocker because this initiative threatens the Q3 roadmap she already committed to the CEO (H)"* not *"VP Engineering may have concerns about timeline."*

2. **Per-cell evidence tier annotation is mandatory in all stakeholder matrices.** Every cell in a Power-Interest-Position map, coalition analysis, or objection playbook must carry an inline evidence tier tag. Where evidence is absent: `(T6: inferred)`. A stakeholder map with untagged cells is incomplete.

3. **The O→I→R→C→W cascade applies to ALL alignment recommendations**, not just final sections. Format: Observation [evidence tier] → Implication [mechanism] → Response [specific action] → Confidence [H/M/L + assumption] → Watch Indicator [observable signal].

4. **Begin with Context Gate and Framework Selection (Step -1 / Step 0)** before applying any framework. A stakeholder alignment strategy for a decision that doesn't need alignment is the most common failure mode.

5. **Contradictions between stakeholders' stated positions and revealed behavior are signal.** When a stakeholder says they're supportive but acts as a blocker (delays meetings, delegates to reports, raises new requirements), surface the contradiction explicitly. Stated position ≠ revealed position.

6. **Flag time-sensitive assessments.** Stakeholder positions change. Any position assessment based on information older than 30 days must carry `[POSITION MAY HAVE SHIFTED — revalidate before acting]`. Alignment decays faster than competitive intelligence.

7. **Flag thin-evidence position assessments.** If a key stakeholder position assessment rests only on Tier 4-6 evidence (secondhand reports, inference), prepend it with `[EVIDENCE-LIMITED: validate with direct conversation before executing alignment strategy]`.

8. **Framework references get one-line contextual explanations.** First reference to any framework includes why it matters for this stakeholder situation. Not everyone reading the document knows what "Decision Archaeology" means.

9. **The document must be navigable by non-creators.** A VP reading this document should find the recommended action in the Executive Summary. A PM should find the alignment sequence. A chief of staff should find the per-stakeholder communication strategies. Include "How to Read This Document" before the analysis.

---

## How to Read This Document

**What this is:** A stakeholder alignment strategy — a political map and action plan for navigating a multi-stakeholder decision. It maps who has power, what they care about, why they hold their current positions, and exactly how to sequence the alignment campaign.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Summary only | The alignment situation, biggest risk, and recommended first move |
| **15 min** | Executive Summary + Stakeholder Map + Alignment Sequence | Who matters, where they stand, and the order to approach them |
| **30 min** | Full document | Complete political map, historical context, per-stakeholder playbooks, and objection pre-emption |

**Reading by role:**

| Role | Start here | Focus on |
|---|---|---|
| **Executive sponsor** | Executive Summary → Alignment Sequence → Assumption Registry | Whether the coalition path is viable and what risks exist |
| **PM (alignment owner)** | Full document, sequentially | Every section — this is your operational playbook |
| **Chief of staff / program manager** | Alignment Sequence → Communication Strategies → Alignment Monitoring | Logistics of executing the alignment campaign |
| **Stakeholder (reviewing their own assessment)** | Redact before sharing — this document is for the alignment owner, not the stakeholders being aligned. Produce a separate brief per stakeholder from the Communication Strategies section. |

---

## Notation Key

**Confidence levels** — applied to every stakeholder position assessment and alignment recommendation:
- **H (>70% confident)** — Direct evidence supports this assessment. Act on it.
- **M (40-70%)** — Direction is probable but evidence is mixed or secondhand. Validate before critical alignment moves.
- **L (<40%)** — This is a hypothesis. Do not execute alignment actions based solely on L-confidence assessments without direct validation.

**Evidence tiers** — how we know what we claim to know (tagged inline as T1-T6):
- **T1** — Direct observation: you witnessed the stakeholder's behavior, read their written position, or heard them state it firsthand
- **T2** — Credible secondhand: a trusted colleague who interacts directly with the stakeholder reports their position
- **T3** — Structural inference: position inferred from the stakeholder's role, incentives, past decisions, or organizational context
- **T4** — Pattern matching: position inferred from how similar stakeholders behave in similar situations
- **T5** — Speculation from peripheral signals: tone of voice, email response time, meeting attendance patterns
- **T6** — Pure assumption: no evidence; position assumed based on general expectations

**Stakeholder position ratings:**
- **Champion** 🟢 — Actively advocates for this initiative. Will spend political capital.
- **Supporter** 🟡+ — Favorable but passive. Will vote yes, will not fight for it.
- **Neutral** ⚪ — No current position. Movable in either direction.
- **Skeptic** 🟡- — Has concerns but is persuadable. Wants specific conditions met.
- **Blocker** 🔴 — Actively opposes. Will spend political capital to stop this.

**Power ratings:**
- **High** — Can approve, veto, or reallocate resources unilaterally
- **Medium** — Can influence decision-makers or delay through process
- **Low** — Affected by the decision but cannot materially change the outcome

**Alignment state:**
- ✅ **Aligned** — Position matches desired state; written or verbal commitment obtained
- 🔄 **In progress** — Engagement started; position moving but not yet committed
- ⏳ **Not started** — No engagement yet
- ⚠️ **At risk** — Previously aligned but showing drift signals
- ❌ **Blocked** — Active opposition; escalation or accommodation needed

---

## Output Template (Mandatory Document Skeleton)

Every Stakeholder Alignment Strategy MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections.

```markdown
# Stakeholder Alignment Strategy: [Decision/Initiative Name]

> **Date:** [YYYY-MM-DD] | **Decision deadline:** [date or "no hard deadline"] | **Alignment confidence:** [Overall H/M/L] | **Staleness window:** [Date after which position assessments need revalidation]

---

## How to Read This Document

[Copy from the "How to Read This Document" section in the skill. Customize reading paths to this specific document.]

## Notation Key

[Copy from the Notation Key section in the skill.]

---

## Executive Summary

[5 sentences max. Zero framework jargon. A VP reads only this and knows: (1) what decision needs alignment, (2) what the current alignment landscape looks like, (3) the biggest risk, (4) the recommended first move. Final sentence = the recommended next action in bold.]

---

## Step 0: Context Gate & Framework Selection

**Context Gate results:**

| Question | Answer | Implication |
|---|---|---|
| Multiple stakeholders required? | [Yes/No] | [Proceed / redirect to brief] |
| Stakeholder positions known? | [Direct / Inferred / Unknown] | [Confidence cap] |
| Previous alignment attempt? | [Yes/No] | [Decision Archaeology depth] |
| Hard deadline? | [Date or No] | [Sequence compression] |

**Framework Selection:**

| Question type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Cross-functional alignment for new initiative"] | [e.g., F1 Power-Interest-Position, F3 Decision Archaeology, F4 Alignment Sequencing] | [e.g., F2 Coalition Analysis, F6 Communication Strategy] | [e.g., "F7 Alignment Monitoring — alignment campaign hasn't started yet"] |

---

## 1. Stakeholder Map (Power-Interest-Position Matrix)

### 1a. Stakeholder Identification

| # | Stakeholder | Role | Relevance to Decision | Source |
|---|---|---|---|---|
| 1 | [Name] | [Title] | [Why they matter] | (TX) |
| 2 | [Name] | [Title] | [Why they matter] | (TX) |

### 1b. Power-Interest-Position Scoring

| Stakeholder | Power | Interest | Current Position | Desired Position | Gap | Confidence |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| [Name] | H/M/L (TX) | H/M/L (TX) | 🟢/🟡+/⚪/🟡-/🔴 (TX) | [Target] | [Size of shift needed] | H/M/L |

### 1c. Power Source Decomposition

| Stakeholder | Formal Authority | Informal Influence | Resource Control | Veto Capability | Net Power |
|---|:---:|:---:|:---:|:---:|:---:|
| [Name] | H/M/L (TX) | H/M/L (TX) | H/M/L (TX) | Yes/No (TX) | H/M/L |

**Engagement strategy matrix:**

| Power \ Interest | High Interest | Low Interest |
|---|---|---|
| **High Power** | **Manage closely** — regular updates, involve in shaping, address concerns immediately | **Keep satisfied** — periodic briefings, no surprises, low-burden engagement |
| **Low Power** | **Keep informed** — share context, listen to input, acknowledge concerns | **Monitor** — light touch, escalate only if position changes |

**Decision point:** [e.g., "3 of 5 high-power stakeholders are currently skeptic or blocker. Coalition building must precede direct engagement with blockers."]

---

## 2. Coalition Analysis

### 2a. Coalition Map

| Coalition Type | Members | Basis of Alliance | Durability | Defection Risk |
|---|---|---|---|---|
| **Natural allies** | [Names] | [Shared interest] (TX) | H/M/L | [What breaks it] |
| **Marriages of convenience** | [Names] | [Issue-specific alignment] (TX) | H/M/L | [What breaks it] |
| **Stable opponents** | [Names] | [Shared opposition interest] (TX) | H/M/L | [What would convert them] |
| **Swing voters** | [Names] | [Undecided — waiting for signal] (TX) | N/A | [What tips them] |

### 2b. Critical Mass Analysis

| Metric | Value |
|---|---|
| **Total stakeholders** | [N] |
| **Needed for approval** | [N — formal or informal threshold] |
| **Current champions + supporters** | [N] |
| **Gap to critical mass** | [N more needed] |
| **Most convertible targets** | [Names — swing voters or soft skeptics] |

### 2c. Power Broker Identification

| Power Broker | Who They Influence | Mechanism | Current Position | Conversion Priority |
|---|---|---|---|---|
| [Name] | [Names of influenced stakeholders] | [How they influence — authority, trust, information] (TX) | [Position] | H/M/L |

**Decision point:** [e.g., "Converting the VP of Platform Engineering (power broker) shifts 2 additional stakeholders from skeptic to supporter, crossing the critical mass threshold."]

---

## 3. Decision Archaeology

### 3a. Relevant Past Decisions

| Past Decision | Date | Outcome | Who Was Involved | How It Shapes Current Positions |
|---|---|---|---|---|
| [Decision] | [Date] | [Result] | [Names] (TX) | [Impact on current alignment] (TX) |

### 3b. Incentive Alignment Analysis

| Stakeholder | Their Goals/Metrics | How This Initiative Affects Them | Alignment/Conflict | Hidden Agenda Risk |
|---|---|---|---|---|
| [Name] | [What they're measured on] (TX) | [Positive/Negative/Neutral + mechanism] | Aligned / Conflicting / Mixed | [What unstated interest may be at play] (TX) |

### 3c. Trust Network

| Stakeholder A | Stakeholder B | Trust Level | History | Implication for Alignment |
|---|---|---|:---:|---|
| [Name] | [Name] | High/Medium/Low/Adversarial (TX) | [Key events] | [Who can influence whom] |

### 3d. Interview Protocol (5 Questions for Excavation)

Before executing the alignment sequence, ask these questions of trusted insiders who know the stakeholder landscape:

1. "What happened the last time someone proposed something similar?" (Reveals institutional memory)
2. "Who fought hardest for/against, and why?" (Reveals position drivers beyond stated rationale)
3. "What's changed since then?" (Reveals whether past positions are still load-bearing)
4. "Who do the key decision-makers listen to most on this kind of decision?" (Reveals power brokers)
5. "What would make this initiative feel safe to the skeptics?" (Reveals conversion conditions)

---

## 4. Alignment Sequence

### 4a. Sequencing Rules Applied

| Rule | Application |
|---|---|
| Start with strongest champion | [Name] — build momentum and get endorsement for use with others |
| Then swing voters (before blockers frame) | [Names, in order] — each conversation changes the next stakeholder's calculus |
| Then neutral high-power stakeholders | [Names] — approach with champion endorsements |
| Approach blockers LAST | [Names] — with maximum coalition backing |

### 4b. Ordered Alignment Plan

| Sequence | Stakeholder | Current → Desired | Action | Timing | Dependency | Deadline |
|:---:|---|---|---|---|---|---|
| 1 | [Name] | 🟢 → 🟢 (maintain) | [Specific action] | [Date/Week] | None | [Date] |
| 2 | [Name] | ⚪ → 🟡+ | [Specific action] | [Date/Week] | After #1 | [Date] |
| 3 | [Name] | 🟡- → ⚪ | [Specific action] | [Date/Week] | After #2 | [Date] |
| 4 | [Name] | 🔴 → 🟡- | [Specific action] | [Date/Week] | After #1, #2, #3 | [Date] |

### 4c. Anti-Patterns Avoided

| Anti-Pattern | Why It Fails | What We're Doing Instead |
|---|---|---|
| Approaching the blocker first | Gives the blocker time to frame the conversation for swing voters before you do | Approaching swing voters first, then blocker |
| Group meeting alignment | Stakeholders perform for each other; real concerns go underground | 1:1 conversations first; group meeting only after individual alignment |
| Waiting for perfect timing | Alignment decays; delay favors the status quo | Time-boxed sequence with specific deadlines per step |

**Decision point:** [e.g., "If Step 2 fails to convert the swing voter, escalate directly to Step 4 (executive sponsor intervention) rather than proceeding to Step 3 — the remaining sequence depends on the swing voter's conversion."]

---

## 5. Objection Pre-emption Playbook

### Per-Objection Template

**Objection 1: [Title — stated in their words]**
- **Stakeholder(s):** [Who will raise this]
- **Objection type:** Rational / Political / Emotional / Structural
- **Underlying concern:** [What they're actually worried about — may differ from stated objection] (TX)
- **Steel-manned version:** [State the objection stronger than the stakeholder would]
- **Response:** [Your prepared response]
- **Evidence required:** [What data or proof supports your response] (TX)
- **Escalation path:** [If response doesn't resolve: who do you involve?]

**Objection 2: [Title]**
[Same structure]

**Objection 3: [Title]**
[Same structure]

### Common Objection Patterns by Role

| Role | Typical Objection Pattern | Underlying Concern | Response Strategy |
|---|---|---|---|
| **Engineering** | "Too risky / too complex / timeline is unrealistic" | Protecting team capacity and credibility; fear of overcommitment | Show you've scoped the technical complexity honestly; offer phased delivery; demonstrate you've already consulted with their tech leads |
| **Finance** | "ROI is unclear / budget isn't approved / competing priorities" | Protecting budget allocation; accountability for spend | Quantify cost of inaction, not just cost of action; tie to metrics they already track; offer a smaller pilot with go/no-go gate |
| **Legal / Compliance** | "Compliance risk / regulatory exposure / liability" | Professional obligation to flag risk; fear of blame if something goes wrong | Provide pre-vetted compliance assessment; propose risk mitigation measures they can sign off on; make them a co-author of the risk framework |
| **Design** | "User experience concern / we haven't validated this" | Protecting user experience standards; ensuring research rigor | Show existing research (T1-T2) that supports the direction; propose a validation milestone before full commitment |
| **Executive** | "Strategic fit unclear / this isn't a priority right now / what are we not doing?" | Protecting strategic coherence; limited attention bandwidth; fear of dilution | Connect to an existing strategic priority they've publicly stated; show the cost of not doing this; keep the ask crisp — 60 seconds max |

---

## 6. Communication Strategies (Per-Stakeholder)

| Stakeholder | Format Preference | Framing | Channel | Timing | Messenger | Follow-up |
|---|---|---|---|---|---|---|
| [Name] | [Doc / Conversation / Data / Demo] (TX) | [How to frame "why this matters" for THEM specifically] | [1:1 / Group / Async / Slack] | [When — before/after which event] | [You / Their trusted peer / Your exec sponsor] | [How to maintain alignment over time] |

### Messenger Selection Decision Table

| Situation | Best Messenger | Why |
|---|---|---|
| Peer-to-peer alignment | You (the PM) | Direct relationship; you own the context |
| Executive buy-in | Your executive sponsor | Authority parity; exec-to-exec carries more weight |
| Technical credibility concern | Your engineering lead | Technical peer credibility; PM alone may not be trusted on feasibility |
| Cross-org alignment | Shared senior stakeholder | Neutral party with relationships on both sides |
| Blocker neutralization | Power broker who influences the blocker | Indirect influence; direct approach from you may trigger defensiveness |

### Framing Adjustment Rules

The same initiative requires different "why it matters" per stakeholder:

| Stakeholder type | Lead with | Avoid |
|---|---|---|
| Revenue-accountable exec | Revenue impact, competitive risk, customer retention | Technical architecture, implementation details |
| Engineering leader | Technical feasibility, team impact, architecture fit | Revenue projections, executive politics |
| Design leader | User experience evidence, research findings | Revenue metrics, competitive intelligence |
| Finance leader | Cost-benefit analysis, budget impact, ROI timeline | Vision statements, user stories |
| Legal/compliance | Risk mitigation, regulatory alignment, precedent | Opportunity cost, speed-to-market pressure |

---

## 7. Alignment Monitoring & Recovery

### 7a. Alignment Dashboard

| Stakeholder | Needed Position | Current Position | Alignment State | Last Contact | Drift Signals |
|---|:---:|:---:|:---:|---|---|
| [Name] | 🟡+ | ⚪ | 🔄 In progress | [Date] | [Any warning signs] |

### 7b. Drift Detection Signals

| Signal | What It Means | Severity | Response |
|---|---|---|---|
| **Silence** — stakeholder stops responding or engaging | Position may be shifting to opposition; they're avoiding confrontation | High | Direct, private check-in: "I want to make sure I haven't missed something. Are there concerns I should address?" |
| **Delegation** — "talk to my report" / sends a proxy | Deprioritizing or distancing; may be signaling opposition without saying it | Medium | Engage the proxy respectfully, but also request 15 min with the principal: "I value [proxy's] input. I'd also like to make sure I'm hearing your perspective directly." |
| **"Let's revisit"** — postponement language | Not ready to commit; may be waiting for more information or for the political landscape to clarify | Medium | Ask directly: "What would need to be true for you to feel comfortable deciding on [date]?" |
| **New requirements** — adds scope, conditions, or process gates | May be genuine due diligence or may be a delaying tactic to kill through bureaucracy | Medium-High | Engage with the requirements seriously. If they're reasonable, accommodate. If they're blockers disguised as process, name it privately. |
| **Public support, private resistance** — says yes in meetings but doesn't follow through | Political savvy; doesn't want to be seen opposing but isn't actually aligned | High | 1:1 conversation. Acknowledge the gap diplomatically: "I want to make sure we're truly aligned — are there concerns you'd like to address before we move forward?" |

### 7c. Recovery Playbook

| Scenario | Response |
|---|---|
| **Lost a champion** (moved roles, changed priorities) | Find the next strongest supporter; rebuild momentum from that anchor. Do not proceed without a champion — alignment without an advocate collapses. |
| **New stakeholder enters** | Run a rapid Power-Interest-Position assessment. Slot them into the alignment sequence. Brief them separately before the next group touchpoint. |
| **Blocker escalates** | Decide: accommodate (modify the proposal to address their concern), go around (find an alternate decision path that doesn't require their approval), or go above (escalation to a shared superior). See Escalation Framework below. |
| **Alignment decays over time** | Re-engage with a progress update that reminds stakeholders of their commitment and shows momentum. People re-commit when they see others are committed. |

### 7d. Escalation Framework

| Option | When to Use | Risk | Decision Criteria |
|---|---|---|---|
| **Accommodate** | Blocker's concern is legitimate and addressable | Scope creep; perceived weakness | The accommodation doesn't compromise the initiative's core value |
| **Work around** | Blocker's approval is not technically required; alternative decision path exists | Political cost; may create an enemy | Alternative path is legitimate, not manipulative; blocker's org is not needed for execution |
| **Go above** | Blocker is unreasonable and a shared superior exists | Relationship damage; perception of political maneuvering | Only after good-faith engagement has failed; the superior agrees the matter warrants escalation; you have coalition backing |

### 7e. Success Criteria

| Level | What "Aligned" Looks Like | Durability |
|---|---|---|
| **Verbal agreement** | "I'm supportive" in a 1:1 | Low — deniable and forgettable. Alignment decays fastest here. |
| **Written approval** | Email, Slack message, or document sign-off | Medium — creates a record but can be walked back. |
| **Resource commitment** | Budget allocated, headcount assigned, team briefed | High — money and people are hard to un-commit. |
| **Public advocacy** | Stakeholder champions the initiative in forums, reviews, all-hands | Very high — reputational commitment makes reversal costly. |

---

## Cross-Framework Contradictions

| Contradiction | Framework A says | Framework B says | Resolution / Which to weight |
|---|---|---|---|
| [e.g., "Stakeholder's stated support vs. revealed behavior"] | [F1: Position is Supporter based on verbal statement] | [F3: Incentive analysis shows initiative conflicts with their OKRs] | [Which matters more and why] |

---

## Strategic Recommendations (O→I→R→C→W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see in the stakeholder landscape]
- **Implication**: [Why it matters — the mechanism]
- **Response**: [Specific alignment action + owner + timeline]
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

## Assumption Registry

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|---|
| 1 | | | H/M/L | (TX) | |
| 2 | | | H/M/L | (TX) | |
| 3 | | | H/M/L | (TX) | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[Steelmanned argument against this alignment strategy. What assumption is being made? What evidence would disprove it? Scenario where this approach backfires catastrophically.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-assess | Timeline |
|---|---|---|
| [Observable event — e.g., "Key champion changes roles"] | [Which sections break — e.g., "Coalition analysis, alignment sequence"] | [When to check] |
| [e.g., "New executive joins the decision group"] | [Power-Interest-Position Matrix, coalition analysis] | [Immediately] |
| [e.g., "Decision deadline moves"] | [Alignment sequence timing, compression analysis] | [Within 48 hours] |

---

## Sources

[All sources cited in the analysis, with evidence tier and date. Include direct conversations, secondhand reports, organizational documents, and meeting notes.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Skipped — [reason]" and move on.
2. **Every table cell with a position, power, or interest rating must have an evidence tier tag** — `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Coalition Analysis") with insight headers (e.g., "Engineering and Legal Are Natural Allies Against This — Finance Is the Swing Vote") after completing the section.
4. **The Executive Summary is written last** but appears first. Do not write it until all sections are complete.
5. **Stakeholder names must be real or clearly labeled as role-based placeholders.** Never use "Stakeholder A" when you know their name.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology — not merely referenced. A PM using this skill produces analysis that requires these frameworks; without them, the output degrades to a RACI matrix or generic stakeholder list.

### Framework 1: Stakeholder Power-Interest-Position Matrix

The foundational mapping. Every alignment strategy starts here — who has power, who cares, and where they currently stand.

**Three dimensions, scored independently:**

| Dimension | Definition | What It Captures |
|---|---|---|
| **Power** | Ability to affect the outcome — through formal authority, informal influence, resource control, or veto | Who CAN stop or accelerate this |
| **Interest** | How much this decision affects the stakeholder's work, metrics, team, or career | Who CARES about the outcome |
| **Position** | Current stance toward the initiative — from active champion to active blocker | Where they STAND right now |

**Power Scoring Rubric (score each source independently, then synthesize):**

| Power Source | High | Medium | Low |
|---|---|---|---|
| **Formal authority** | Can approve or veto this decision unilaterally | Can delay or add requirements through formal process | Affected but no formal decision rights |
| **Informal influence** | Widely trusted; their opinion shifts rooms | Respected within their function; influences their team | Limited influence beyond direct reports |
| **Resource control** | Controls budget, headcount, or infrastructure needed for execution | Controls resources that support but don't block execution | No control over resources this initiative requires |
| **Veto capability** | Explicit or de facto veto — initiative cannot proceed if they say no | Can block indirectly through process, escalation, or delay | No ability to prevent the initiative |

**Net Power = Highest of the four sources.** A stakeholder with High informal influence and Low formal authority still has High net power — they can kill the initiative through influence even without signing authority.

**Interest Scoring Rubric:**

| Level | Criteria | Behavioral Signal |
|---|---|---|
| **High** | This decision directly changes their team's work, metrics, budget, or headcount | They ask about this proactively; they attend meetings about it; they have opinions |
| **Medium** | This decision affects them tangentially — adjacent team, shared resources, or downstream dependency | They engage when asked but don't seek updates; they'll review but not initiate |
| **Low** | This decision has minimal impact on their day-to-day work or metrics | They skip meetings about it; they delegate to a report; they say "whatever the team decides" |

**Position Taxonomy:**

| Position | Symbol | Definition | Behavioral Signals |
|---|---|---|---|
| **Champion** | 🟢 | Actively advocates. Will spend political capital to make this happen. | Volunteers resources; brings it up in meetings unprompted; defends it when challenged |
| **Supporter** | 🟡+ | Favorable but passive. Will vote yes if asked. Won't fight for it. | Agrees when asked; doesn't block; but doesn't champion in your absence |
| **Neutral** | ⚪ | No position formed. Movable in either direction. | Hasn't engaged; asks questions but doesn't lean; "I need to learn more" |
| **Skeptic** | 🟡- | Has specific concerns but is persuadable. Wants conditions met. | Raises questions, asks for data, names specific risks. Different from a blocker: a skeptic tells you what would change their mind |
| **Blocker** | 🔴 | Actively opposes. Will spend political capital to stop this. | Raises objections in meetings; lobbies others against; adds requirements designed to delay; escalates to leadership |

**Critical insight — position is dynamic:** A stakeholder's position is NOT fixed. It changes based on (a) new information, (b) who they've talked to since your last interaction, (c) how the initiative is framed, and (d) what other stakeholders are doing. Map both **current position** and **desired position** — the gap between them is the alignment work.

**Engagement Strategy Decision Table:**

| Power × Interest | Engagement Strategy | Cadence | Risk if Neglected |
|---|---|---|---|
| **High Power + High Interest** | **Manage closely.** Regular updates, involve in shaping, address concerns immediately. These stakeholders will actively help or actively hinder. | Weekly or more | They become blockers you didn't see coming |
| **High Power + Low Interest** | **Keep satisfied.** Periodic briefings, no surprises. Keep engagement low-burden so they don't become annoyed. | Biweekly summary | A surprise triggers a veto from someone who never cared before |
| **Low Power + High Interest** | **Keep informed.** Share context generously. Their support builds momentum even without decision authority. | Weekly update | They feel ignored and become vocal skeptics who influence others |
| **Low Power + Low Interest** | **Monitor.** Light touch. Engage only if their position changes or their power increases. | Monthly or as needed | Minimal risk unless their role changes |

---

### Framework 2: Coalition Analysis

Understanding group dynamics — who needs whom, which alliances are durable, and where the tipping point is.

**Coalition Taxonomy:**

| Type | Definition | Durability | Strategic Implication |
|---|---|---|---|
| **Natural allies** | Shared long-term interests align them on this initiative AND on most related topics | High — survives setbacks | Core of your coalition. Invest here first. These are the stakeholders who will still be with you after a delay, a scope change, or a leadership shuffle. |
| **Marriages of convenience** | Aligned on THIS issue but not others. Different long-term interests. | Low-Medium — fragile | Useful for critical mass but don't over-rely. These alliances break if the initiative's scope shifts to threaten their other interests. |
| **Stable opponents** | Shared interests that oppose the initiative — structural opposition, not personal | High — hard to convert | Don't waste alignment cycles trying to convert stable opponents. Neutralize (accommodate or work around) rather than persuade. Their opposition is rational given their interests. |
| **Swing voters** | No strong interest pull in either direction. Waiting for a signal to decide. | N/A — they'll move once | Highest-priority alignment targets. Their conversion often depends on which side approaches them first. If the opposition frames the conversation first, you've lost the swing voter. |

**Critical Mass Analysis:**

| Question | Method |
|---|---|
| How many votes/approvals are formally needed? | Review decision governance — is this a single-approver, committee, or consensus decision? |
| How many stakeholders need to be supportive for the initiative to have de facto momentum? | Count the stakeholders whose active opposition would stall execution, regardless of formal approval. |
| Where is the tipping point? | The point at which enough high-power stakeholders are publicly committed that opposing becomes costly. Usually 60-70% of high-power stakeholders. |

**Defection Risk Assessment:**

| Coalition Member | What Holds Them | What Could Break Them | Defection Probability | Mitigation |
|---|---|---|---|---|
| [Name] | [Their interest alignment] | [Scenario that shifts their interest] | H/M/L | [Action to prevent defection] |

**Power Broker Identification — the leverage points:**

A power broker is a stakeholder who can shift MULTIPLE other stakeholders' positions. They are the highest-leverage targets in any alignment campaign.

| Signal | Power Broker Indicator |
|---|---|
| Other stakeholders say "I'd want to hear what [Name] thinks" | Trusted advisor — their endorsement carries weight |
| Their team members mirror their positions on related topics | Organizational influence — they shape their team's views |
| They sit in multiple forums where this decision is discussed | Information broker — they control the narrative across groups |
| They have a track record of shaping past decisions on similar topics | Institutional authority — proven influence, not just positional |

**Decision Table — Coalition Strategy:**

| Coalition State | Strategy |
|---|---|
| You have critical mass among high-power stakeholders | Proceed with formal decision process. The coalition is sufficient. Blocker mitigation is secondary. |
| You're 1-2 stakeholders short of critical mass | Focus ALL alignment energy on swing voters and power brokers. Do not engage blockers yet — that energy is wasted until you have mass. |
| Opposition has critical mass | Re-scope the initiative to address the dominant objection, or escalate to a higher authority who can override the coalition. Continuing the current approach is futile. |
| No coalition exists yet — fragmented positions | Start with the single strongest potential champion. Build a nucleus before reaching out broadly. |

---

### Framework 3: Decision Archaeology

Understanding WHY stakeholders hold their current positions. Without this, alignment attempts are solutions in search of agreement.

**Premise:** Every stakeholder position has a history. A VP who championed a failed initiative similar to yours will be defensive. A finance leader who approved a project that went over budget will apply extra scrutiny. A design leader whose team was sidelined on a previous cross-functional effort will insist on early involvement. These histories are rarely stated. They must be excavated.

**Five Layers of Position Archaeology:**

| Layer | Question | What It Reveals | Evidence Source |
|---|---|---|---|
| **Past decisions** | What previous decisions shaped this stakeholder's current position? | Burned-before patterns, sunk cost attachment, reputation risk | T2-T3: ask trusted colleagues who were present for those decisions |
| **Institutional memory** | What unwritten history exists around this topic? | "We tried this before and it failed" stories that live in organizational culture, not documents | T2-T3: long-tenured employees, skip-level conversations |
| **Incentive alignment** | How does this decision affect this stakeholder's goals, metrics, bonus, and career? | Rational self-interest — the most reliable predictor of position | T1-T3: review their OKRs, team goals, compensation structure if known |
| **Hidden agendas** | What unstated interests are at play? | Budget protection, territorial expansion, succession positioning, face-saving | T4-T6: inferred from behavior patterns, organizational dynamics |
| **Trust history** | Which stakeholders trust each other? Which have adversarial history? | Who can influence whom; which partnerships are available; which paths are blocked | T2-T3: observe meeting dynamics, ask who they collaborate with willingly |

**Incentive Alignment Scoring:**

| Alignment Level | Criteria | Implication for Alignment |
|---|---|---|
| **Strongly aligned** | This initiative directly advances their stated goals and metrics | Champion candidate. Alignment effort = frame it correctly and ask for support. |
| **Neutral** | Initiative doesn't meaningfully affect their goals in either direction | Low natural interest. Will defer to others. Can be won with low-effort framing. |
| **Conflicting** | Initiative competes with their goals — for budget, headcount, leadership attention, or priority ranking | Skeptic or blocker candidate. Alignment requires addressing the conflict directly (accommodation, trade, or reframing). |
| **Threatening** | Initiative could make them look bad, reduce their authority, or undermine their prior decisions | Blocker. Alignment requires making the initiative safe for them — protecting their reputation, preserving their authority, or offering a meaningful role. |

**The "Burned Before" Pattern:**

The most common hidden driver of stakeholder resistance. Detection:

| Signal | Interpretation | Response |
|---|---|---|
| "We tried something like this before" | They have a failed precedent in mind. Your initiative activates that memory. | Acknowledge the precedent directly: "I know the [previous initiative] didn't go as planned. Here's what's different this time: [specific, concrete differences]." |
| Disproportionate focus on risk | They're not assessing your initiative objectively — they're projecting past failure | Address the specific past failure: "I understand [specific past concern] is top of mind. Here's how we're mitigating that exact risk: [specific mitigation]." |
| "I need to see proof before committing" | Higher evidence bar than the decision warrants — driven by past regret | Provide disproportionate evidence for the specific dimension where the past initiative failed. Over-index on their burned area. |

**Interview Protocol — 5 Questions for Excavation:**

Run these before executing any alignment sequence. Ask of trusted insiders who know the stakeholder landscape. NOT of the stakeholders themselves — that reveals your strategy.

1. **"What happened the last time someone proposed something similar?"** — Reveals institutional memory that may not be documented
2. **"Who fought hardest for or against, and why?"** — Reveals position drivers beyond stated rationale
3. **"What's changed since then?"** — Reveals whether past positions are still load-bearing or outdated
4. **"Who do the key decision-makers listen to most on this kind of decision?"** — Reveals power brokers and influence networks
5. **"What would make this initiative feel safe to the skeptics?"** — Reveals conversion conditions — the specific concerns that, if addressed, would remove opposition

---

### Framework 4: Alignment Sequencing

The ORDER in which you approach stakeholders matters as much as what you say to them. Alignment is an information cascade — each conversation changes the next stakeholder's calculus.

**Core Principle:** Aligning Stakeholder A before Stakeholder B changes B's information set. If B knows A supports the initiative, B's risk calculus shifts. If B hears the blocker's framing first, your conversation with B starts from a defensive position.

**Sequencing Rules:**

| Step | Target | Rationale | Dependency |
|---|---|---|---|
| **1** | Strongest champion | Build momentum. Get explicit endorsement you can reference in subsequent conversations. | None — this is the anchor. If your champion isn't solid, the entire sequence is on shaky ground. |
| **2** | Swing voters | Before they hear the blocker's frame. The first framing they encounter anchors their position. | After champion — you need at least one high-power endorsement to cite. |
| **3** | Neutral high-power stakeholders | With champion endorsements and swing voter momentum. Social proof shifts their cost-benefit analysis. | After champion + swing voters. The more names you can cite, the lower the perceived risk of supporting. |
| **4** | Skeptics (convertible) | With maximum coalition backing. Address their specific concerns with data and accommodations. | After steps 1-3. Approaching a skeptic alone is a debate. Approaching a skeptic with 5 supporters is a coalition invitation. |
| **5** | Blockers | Last. With full coalition. The goal is not to convince — it's to make opposition costly by demonstrating the initiative has critical mass. | After steps 1-4. If you can't convert the blocker, you should have enough mass to proceed without them (or escalate). |

**Time-Boxing Rule:**

| Principle | Application |
|---|---|
| Alignment has a shelf life | Verbal alignment obtained 4+ weeks ago without reinforcement should be treated as STALE. Re-validate before depending on it. |
| The sequence has a clock | Each step should take no more than 1 week. A 5-step sequence should complete in 5 weeks or less. Longer timelines invite entropy — new priorities, reorgs, people leaving. |
| Parallel where safe | Steps 2 and 3 can sometimes run in parallel if the swing voters and neutral stakeholders don't interact frequently. But never parallelize step 4 or 5 with earlier steps — blocker engagement before coalition is built is the #1 anti-pattern. |

**Anti-Patterns:**

| Anti-Pattern | Why It Fails | What to Do Instead |
|---|---|---|
| **Approaching the blocker first** ("let me convince the hardest person first") | Gives the blocker your playbook. They now prepare counter-arguments for every subsequent conversation. You've armed the opposition. | Approach the blocker LAST, with maximum coalition backing. |
| **The all-hands reveal** (presenting to everyone at once) | Stakeholders perform for each other. Real concerns go underground. You get polite nodding in the room and hallway opposition after. | 1:1 conversations first. Group alignment meetings only AFTER individual positions are understood and addressed. |
| **The email blast** (sending a document and hoping for alignment) | Documents don't align stakeholders. Conversations do. A document creates awareness, not commitment. | Documents are follow-ups to conversations, not substitutes for them. |
| **Waiting for the "right moment"** (delaying because conditions aren't perfect) | Alignment decays while you wait. The status quo gets stronger every day you don't act. Perfect conditions never arrive. | Time-box. If conditions are 70% right, start the sequence. The sequence itself creates momentum. |

**Decision Table — Sequencing Adjustments:**

| Situation | Sequencing Modification |
|---|---|
| Champion is the most senior person in the room | Standard sequence applies — this is the ideal scenario |
| Champion is junior to the blocker | Need a power broker or executive sponsor to validate the champion's position before approaching senior skeptics |
| No clear champion exists | Find one. Run the Incentive Alignment analysis to identify the stakeholder whose goals this initiative most advances. Help them see it. |
| Blocker has already framed the conversation for swing voters | Skip directly to swing voters with a reframe. You're now playing defense — lead with "I heard [blocker's concern] and here's what's actually true..." |
| Decision deadline is compressed (< 2 weeks) | Compress to 3 steps: champion → swing voters + neutral (parallel) → blocker. Accept lower alignment quality for speed. |

---

### Framework 5: Objection Pre-emption Playbook

Predicting resistance before it happens and preparing specific, steel-manned responses.

**Objection Taxonomy — four types require different response strategies:**

| Type | Definition | Response Lever | Example |
|---|---|---|---|
| **Rational** | Data-based concern. Addressable with evidence. | Provide better data, run an analysis, offer a pilot. | "I don't see how this will move the metric." → Show the causal model with evidence. |
| **Political** | Territory, resource, or authority-based concern. | Incentive alignment, trade, or accommodation. | "This overlaps with my team's charter." → Offer joint ownership or clear boundary definition. |
| **Emotional** | Trust, history, or relationship-based concern. | Relationship building, acknowledgment, face-saving. | "The last time we did something like this, it failed." → Acknowledge the history directly and show what's different. |
| **Structural** | Process, governance, or compliance-based concern. | Procedural compliance, documentation, approvals. | "This hasn't been through the architecture review board." → Schedule the review and demonstrate compliance willingness. |

**The Steel Man Rule:**

> State each objection STRONGER than the stakeholder would. If your prepared response only works against a weak version of the objection, you are not prepared.

| Bad (straw man) | Good (steel man) |
|---|---|
| "They might worry about timeline" | "They will argue that this initiative, given its cross-functional dependencies, cannot realistically ship in the timeline we've proposed — and that promising a date we can't hit will damage the team's credibility with leadership, which is worse than not starting at all" |
| "They could have budget concerns" | "They will point out that this requires $X from a budget already committed to [their existing priority], and that reallocating means either under-delivering on a commitment they've already made to [exec name], or requesting new budget in a cycle where finance is cutting, not adding" |

**Per-Objection Template:**

For each anticipated objection, prepare:

| Component | Purpose |
|---|---|
| **The objection, stated in their words** | Shows you understand their perspective, not a caricature of it |
| **The underlying concern** | The real worry beneath the stated objection — often different from the surface argument |
| **Steel-manned version** | The strongest possible version of the objection |
| **Your response** | Specific, evidence-backed, not dismissive |
| **Evidence required** | What data or proof makes your response credible (with evidence tier) |
| **Escalation path** | If the response doesn't resolve the objection: who gets involved, and what happens |

**Objection Response Principles:**

| Principle | Application |
|---|---|
| **Acknowledge before responding** | "I understand your concern about X, and it's legitimate" — then respond. Skipping acknowledgment makes the response feel dismissive. |
| **Address the underlying concern, not the stated objection** | If the stated objection is "timeline is too aggressive" but the underlying concern is "my team will be blamed if it slips," the response must address blame protection, not just timeline feasibility. |
| **Offer to co-solve, not defend** | "How could we structure this so your concern is addressed?" is stronger than "Here's why your concern is wrong." |
| **Know when to accommodate** | Not every objection needs to be overcome. Some should be accommodated. If a scope adjustment converts a blocker to a supporter and doesn't compromise the core value, accommodate. |

---

### Framework 6: Communication Strategy by Stakeholder

Tailored engagement approach per person. Same initiative, different "why it matters," different format, different messenger.

**Format Preference Assessment:**

| Preference | Signals | Approach |
|---|---|---|
| **Document reader** | Asks "send me something I can read"; reviews docs thoroughly; marks up written materials | Lead with a concise document (max 2 pages). Follow up with a conversation to discuss their questions. |
| **Conversation-first** | Prefers meetings over async; talks through problems verbally; asks for "the quick version" | Lead with a 1:1 conversation. Send a follow-up doc to confirm what was discussed. |
| **Data-driven** | Asks for metrics, models, or quantitative analysis; distrusts qualitative arguments | Lead with data: cost-benefit analysis, impact modeling, comparable examples with numbers. Frame qualitative arguments in quantitative terms. |
| **Demo-driven** | Wants to see the thing working; abstractions don't land; responds to tangible artifacts | Build a prototype, mockup, or scenario walkthrough. Tangibility converts this stakeholder faster than any argument. |

**Channel Selection Decision Table:**

| Situation | Best Channel | Why |
|---|---|---|
| Initial alignment conversation | 1:1 meeting (in-person or video) | Sensitive; you need to read reactions; allows for candid exchange |
| Follow-up after initial alignment | Async document (email or doc) | Confirms what was agreed; gives them time to process and respond |
| Maintaining alignment over time | Slack/Teams message or brief update | Low-burden; keeps them informed without requiring a meeting |
| Resolving a specific objection | 1:1 meeting | Objections need real-time dialogue, not written arguments |
| Group alignment checkpoint | Group meeting — but only after individual alignment | Formalizes individual agreements; creates public commitment |

**Timing Rules:**

| Principle | Application |
|---|---|
| **Before their planning cycle** | If you need budget or headcount, align before their planning process closes — not after |
| **After a win, not after a setback** | Stakeholders are more receptive when things are going well. Don't pitch a new initiative the week after a P0 incident |
| **Monday morning, not Friday afternoon** | Cognitive bandwidth matters. Alignment conversations deserve fresh attention, not end-of-week fatigue |
| **Before the blocker talks to them** | The first framing they encounter anchors their position. Timing relative to the blocker's activities matters as much as absolute timing |

**Follow-up Protocol — Alignment Decays:**

| Timeframe | Action |
|---|---|
| Within 24 hours of alignment conversation | Send a brief confirmation: "Here's what I heard from our conversation: [summary]. Please let me know if I captured it correctly." |
| Weekly during active alignment campaign | Brief progress update to champions and supporters: "Here's where we are. [Names] are on board. Next step: [action]." |
| At decision point | Final check-in with every aligned stakeholder: "We're approaching the decision. I want to confirm your support is still solid." |
| Post-decision | Thank champions and supporters explicitly. Acknowledge accommodations made for former skeptics. This builds relationship capital for next time. |

---

### Framework 7: Alignment Monitoring & Recovery

Tracking alignment state over time and responding to drift before it becomes opposition.

**Alignment State Tracking:**

For each stakeholder, maintain a running record:

| Field | Purpose |
|---|---|
| **Needed position** | What position do you need this stakeholder to hold? |
| **Current position** | Where do they actually stand right now? |
| **Alignment state** | ✅ Aligned / 🔄 In progress / ⏳ Not started / ⚠️ At risk / ❌ Blocked |
| **Last contact** | When was the last meaningful interaction about this initiative? |
| **Next action** | What's the next step with this stakeholder? |
| **Drift signals** | Any warning signs that their position is shifting? |

**Staleness Rule for Alignment:**

| Time Since Last Contact | Risk Level | Action |
|---|---|---|
| < 1 week | Green — fresh | Continue as planned |
| 1-2 weeks | Yellow — aging | Schedule a brief touchpoint this week |
| 2-4 weeks | Orange — stale | Re-validate position before depending on it; alignment may have decayed |
| > 4 weeks | Red — expired | Do NOT assume this stakeholder is still aligned. Re-engage from a neutral assumption. |

**Recovery Patterns:**

| Scenario | Root Cause Analysis | Recovery Action |
|---|---|---|
| **Champion departed** | Single point of failure in the coalition | Identify the next strongest supporter. Brief them on the full strategy. Rebuild momentum from that anchor. Consider: was the coalition dependent on one person, or distributed? |
| **New blocker appeared** | Stakeholder landscape changed; new entrant wasn't in original analysis | Run rapid Power-Interest-Position assessment. Add them to the alignment sequence. They get the same 1:1 treatment — understanding their position before attempting conversion. |
| **Scope change reactivated opposition** | The accommodation that converted a skeptic was undermined by a scope change | Re-engage the former skeptic immediately. Explain the scope change and whether the accommodation still holds. If it doesn't, negotiate a new accommodation. |
| **Decision deadline moved up** | Time compression means the alignment sequence can't complete | Compress: identify the minimum viable coalition (who do you MUST have?) and focus all energy there. Accept that some stakeholders will be informed, not aligned. |
| **General alignment decay** | No active engagement; stakeholders moved on to other priorities | Run a momentum event: a progress update, a demo, or a quick win that reminds people the initiative is alive and moving. People re-commit when they see progress. |

---

### Analytical Lenses (Applied Across All Frameworks)

#### The Asymmetric Interest Lens

Different stakeholders don't just have different positions — they experience the same initiative as fundamentally different things.

| Stakeholder type | What they see | What they fear | What they need to hear |
|---|---|---|---|
| **The exec sponsor** | Strategic opportunity; portfolio allocation decision | Wasting leadership capital on a failure; distraction from priorities | This advances your stated strategy and strengthens your team's position |
| **The resource owner** | Resource competition; capacity impact; team strain | Overcommitment; team burnout; blame for slips | This is properly scoped; your team won't be stretched; we've planned for contingencies |
| **The peer PM** | Territory overlap; charter confusion; collaboration demand | Credit dilution; scope creep into their area; being subordinated | Clear swim lanes; joint ownership model; credit sharing protocol |
| **The engineer** | Technical feasibility; architecture impact; maintenance burden | Unrealistic timeline; tech debt; being set up to fail | We've done the technical diligence; the architecture is sound; we're building with their input |
| **The compliance stakeholder** | Risk exposure; regulatory alignment; audit readiness | Accountability for something they didn't review; surprise exposure | We've done the pre-work; here's the compliance assessment; we want you involved early |

#### The Formal vs. Informal Power Lens

Organizations have two power structures operating simultaneously. Alignment strategies that only address one fail.

| Power Type | Where It Lives | How to Map It | How to Leverage It |
|---|---|---|---|
| **Formal** | Org chart, decision rights, budget authority, approval workflows | Review governance docs, RACI, escalation policies | Follow the process. Formal power is necessary but often not sufficient. |
| **Informal** | Relationships, trust, institutional knowledge, cultural influence | Observe meeting dynamics — who do people defer to? Whose emails get immediate responses? Who gets consulted before decisions? | Identify informal leaders and treat them as power brokers. Their endorsement often matters more than formal approval. |

#### The Stakeholder-as-Audience Lens (from Connector Agent)

Adapted from the Connector agent's Audience Discovery methodology: approach each stakeholder as an audience to be understood before being persuaded.

| Principle | Connector Origin | Alignment Application |
|---|---|---|
| **Topic-first, network-second** | Identify who matters for THIS thesis before checking connections | Identify what matters to THIS stakeholder before checking your relationship |
| **Value-first engagement** | Never ask before you give | Lead every alignment conversation with something useful to them — information, a solution to their concern, recognition of their expertise |
| **Pitch angle per person** | Generic "check out my article" never works | Generic "please support my initiative" never works. Frame why this initiative specifically matters for their specific priorities |
| **50% outside-network rule** | At least half of targets should be new connections | At least some of your alignment effort should go to stakeholders you don't already have strong relationships with — they represent the highest risk |

---

## Evidence Standards for Stakeholder Analysis

### Evidence Quality Tiers (Adapted for Organizational Context)

| Tier | Source Type | Weight | Example |
|---|---|---|---|
| **Tier 1** | Direct observation of the stakeholder's behavior or explicit written/verbal statement to you | Highest | They said "I support this" in a 1:1; you saw them raise objections in a meeting; their email explicitly states a position |
| **Tier 2** | Credible secondhand report from someone who interacts directly with the stakeholder | High | Your manager says "I spoke with [Name] and they're concerned about X"; a trusted peer reports "they're on board" |
| **Tier 3** | Structural inference from role, incentives, past decisions, or organizational context | Medium-High | Their OKRs conflict with this initiative; they championed a similar initiative before; their team would lose headcount |
| **Tier 4** | Pattern matching from similar stakeholders in similar situations | Medium | "VPs of engineering typically resist scope additions in H2"; "Finance always pushes back on unbudgeted initiatives" |
| **Tier 5** | Peripheral signals — tone, response time, body language, meeting attendance | Low-Medium | They stopped attending the project review; their emails are shorter; they delegated to a report |
| **Tier 6** | Pure assumption — no evidence | Low | "I think they'll be supportive because they're generally agreeable" |

**Triangulation Rule:** No stakeholder position assessment should rest on a single evidence tier. Minimum 2 tiers, ideally 3. A T1 verbal statement of support + a T3 incentive analysis showing conflict = surface the contradiction.

**Decay Rule:** Stakeholder evidence decays faster than market evidence. Evidence older than 30 days should carry `[POSITION MAY HAVE SHIFTED]`. Evidence older than 90 days should be treated as T6 (assumption) regardless of original tier.

---

## Application Method

### Step 0: Route to Framework Subset (Do This First)

Identify the alignment challenge type and select load-bearing frameworks before applying any. Applying all 7 frameworks to a straightforward executive briefing inflates the strategy and buries the actionable insight.

| Question Type | Prompt Signals | Primary Frameworks | Frameworks to Skip |
|---|---|---|---|
| **New initiative alignment** | "How do I get buy-in for X", "who needs to approve", "cross-functional alignment needed" | F1 Power-Interest-Position, F4 Alignment Sequencing, F6 Communication Strategy | F7 Monitoring (campaign hasn't started); F3 Decision Archaeology (lighter if no prior history) |
| **Failed alignment recovery** | "We tried before and it didn't work", "the proposal stalled", "lost executive support" | F3 Decision Archaeology (load-bearing), F1 Power-Interest-Position, F5 Objection Pre-emption | F2 Coalition Analysis (rebuild after understanding failure first) |
| **Blocker neutralization** | "VP of X is blocking this", "how do I get past [Name]", "active opposition" | F3 Decision Archaeology, F5 Objection Pre-emption, F2 Coalition Analysis | F6 Communication Strategy (secondary — focus on the blocker specifically) |
| **Coalition building** | "How many supporters do I need", "who should I align first", "building consensus" | F2 Coalition Analysis, F4 Alignment Sequencing, F1 Power-Interest-Position | F5 Objection Pre-emption (secondary until opposition surfaces) |
| **Executive buy-in** | "Need CEO/VP approval", "board-level decision", "executive sponsorship" | F1 Power-Interest-Position, F6 Communication Strategy, F3 Decision Archaeology | F2 Coalition Analysis (lighter — executive decisions are often smaller groups) |
| **Full alignment strategy** | "Complete stakeholder strategy", "high-stakes decision with many stakeholders" | All — tier explicitly: 3 primary, rest supporting | None — but label tiers |

Apply primary frameworks fully. Apply supporting frameworks at reduced depth unless they surface a contradictory signal — in which case surface the contradiction explicitly.

### Quick Version (10 steps for experienced practitioners)

0a. **Context Gate** — Verify a Stakeholder Alignment Strategy is the right artifact. Is alignment genuinely needed? Do you have access to stakeholder positions? Has a previous attempt failed?
0b. **Route to framework subset** — Identify alignment type from the table above. Select 3-4 primary frameworks. Note which to skip.
1. **Map all stakeholders** — List every person who can affect, approve, block, or be affected by this decision. Include non-obvious stakeholders (legal, finance, downstream teams).
2. **Score Power-Interest-Position for each** — Produce the matrix with per-cell evidence tiers. Score power sources independently (formal authority, informal influence, resource control, veto).
3. **Run Coalition Analysis** — Classify: natural allies, marriages of convenience, stable opponents, swing voters. Identify power brokers. Calculate critical mass gap.
4. **Excavate Decision Archaeology** — Past decisions, incentive alignment, trust history, hidden agendas. Run the 5-question interview protocol with trusted insiders.
5. **Design the Alignment Sequence** — Order stakeholder approaches. Start with champion, then swing voters, then neutrals, then skeptics, then blockers. Time-box each step.
6. **Build the Objection Pre-emption Playbook** — Anticipate every significant objection. Steel-man each. Prepare evidence-backed responses. Identify escalation paths.
7. **Design Per-Stakeholder Communication Strategies** — Format, framing, channel, timing, messenger selection. Different "why it matters" for each stakeholder.
8. **Set up Alignment Monitoring** — Dashboard with needed vs. current position, alignment state, drift signals, staleness dates.
9. **Cascade every finding to O→I→R→C→W** — Every key alignment recommendation gets the full cascade. Write the Executive Summary last.
10. **Adversarial Self-Critique** — Identify ≥3 genuine weaknesses in the alignment strategy. What assumptions are you making? What could go catastrophically wrong?

### Full Version (detailed steps with decision points)

**Step 1: Map All Stakeholders**

Don't let the requester's initial list be the final list. Use this expansion protocol:

| Expansion Method | What It Catches |
|---|---|
| **Decision governance review** — who formally approves this decision? | Formal approvers you might not have considered |
| **Resource dependency review** — whose budget, headcount, or infrastructure is needed? | Resource owners who become blockers if surprised |
| **Downstream impact review** — whose work changes if this initiative proceeds? | Affected parties who deserve input even without approval rights |
| **Champion/blocker review** — who has strong opinions about this topic even if they're not formally involved? | Informal influencers who can accelerate or derail through hallway conversations |
| **Historical review** — who was involved in similar past decisions? | Veterans with institutional memory and political context |

**Decision point:** If the stakeholder list exceeds 12 people, tier them. Tier 1 (full analysis): stakeholders with High power or High interest. Tier 2 (scan): everyone else. Full alignment strategy for every stakeholder is not feasible beyond 12.

**Step 2: Score Power-Interest-Position**

For each stakeholder:
1. Score Power using the 4-source decomposition (formal authority, informal influence, resource control, veto). Tag each score with evidence tier.
2. Score Interest using the behavioral signal rubric. Tag with evidence tier.
3. Assess Position using the 5-position taxonomy. Tag with evidence tier.
4. Note the gap between current position and desired position — this is the alignment work.
5. Assign engagement strategy from the Power × Interest decision table.

**Decision point:** If any High-Power stakeholder is at Blocker (🔴) AND has veto capability, the alignment strategy MUST address them. You cannot work around a vetoing blocker.

**Step 3: Run Coalition Analysis**

1. Classify each stakeholder into coalition types (natural ally, marriage of convenience, stable opponent, swing voter).
2. Identify power brokers — who can shift multiple stakeholders' positions?
3. Calculate critical mass: how many high-power supporters do you need? How many do you have? What's the gap?
4. Assess defection risk for each coalition member.

**Decision point:** If the critical mass gap is >3 high-power stakeholders, the initiative may need re-scoping or executive escalation before alignment is feasible.

**Step 4: Excavate Decision Archaeology**

1. Review past decisions related to this initiative. What happened? Who was involved? What went wrong or right?
2. Score incentive alignment for each stakeholder — does this initiative advance or threaten their goals?
3. Map the trust network — which stakeholders trust each other? Which have adversarial history?
4. Run the 5-question interview protocol with 2-3 trusted insiders.

**Decision point:** If Decision Archaeology reveals that a key stakeholder was burned by a similar initiative, the Objection Pre-emption Playbook must address that specific history. Generic responses will fail.

**Step 5: Design the Alignment Sequence**

1. Apply the sequencing rules: champion first → swing voters → neutrals → skeptics → blockers last.
2. Time-box each step (default: 1 week per step).
3. Identify dependencies: which steps must complete before others can start?
4. Check for anti-patterns: are you approaching the blocker first? Planning an all-hands reveal? Relying on email for alignment?

**Decision point:** If the timeline is compressed (< 2 weeks to decision), merge steps. Accept lower alignment quality for speed. Identify the minimum viable coalition.

**Step 6: Build the Objection Pre-emption Playbook**

For each stakeholder likely to raise objections:
1. Predict their objection using Decision Archaeology findings.
2. Classify the objection type (rational, political, emotional, structural).
3. Steel-man the objection — state it stronger than they would.
4. Prepare a response with evidence (tagged by tier).
5. Identify the escalation path if the response doesn't resolve the objection.

**Step 7: Cascade to "So What"**

For EVERY major alignment finding, structure as:

```
OBSERVATION [evidence tier] → IMPLICATION [mechanism] → ALIGNMENT RESPONSE [specific action + owner] → CONFIDENCE [H/M/L + key assumption] → WATCH INDICATOR [observable signal]

"VP of Engineering is a skeptic because this initiative requires 2 engineers from her team during Q3 crunch [T2: her skip-level told us],
which means she will block until resource impact is addressed because her performance review depends on Q3 delivery,
our response is to offer a phased approach where engineering contribution starts Q4, with a Q3 design phase that requires no engineering headcount,
confidence: M — assumes Q4 engineering capacity exists (verify with her team lead),
watch: if she starts raising process objections beyond the resource concern, the underlying driver may be territorial, not resource-based — escalate to Decision Archaeology."
```

### Mandatory Output: Assumption Registry

Every stakeholder alignment strategy must include a standalone assumption registry. List every load-bearing assumption the strategy depends on:

| Assumption | Framework it underpins | Confidence | Evidence | What would invalidate this |
|---|---|---|---|---|
| [e.g., "VP of Design is persuadable — her concerns are about process, not substance"] | F1 (Position), F4 (Sequencing — she's step 3 in the sequence) | M | T2: her skip-level reports she's "open but cautious" | She raises substance objections after seeing the proposal — current assessment was wrong |
| [e.g., "CEO will not override the blocker without coalition backing"] | F2 (Coalition — critical mass calculation), F4 (Sequencing — blocker is last) | H | T3: CEO's pattern is to seek consensus; past escalations without coalition failed | CEO makes an exception for this initiative because of external pressure |

Any assumption at L confidence must be flagged `[EVIDENCE-LIMITED]` in the section where it appears.

### Mandatory Step: Adversarial Self-Critique

After completing the alignment strategy, execute this step before delivering output:

> *"Now identify ≥3 genuine weaknesses in this alignment strategy. For each: what assumption is being made? What evidence would disprove it? Is there a scenario where this alignment approach backfires catastrophically?"*

- If you cannot find real weaknesses, you haven't looked hard enough.
- Bear cases must be steelmanned — not just listed as probability-weighted scenarios but argued as forcefully as possible.
- Each weakness should link to a specific Watch Indicator that would trigger re-assessment.
- The adversarial critique is **not optional** and should not be folded into the risk section — it is a distinct, explicitly adversarial voice.

---

## Quality Gradients

### Intern Tier
- Lists stakeholders and their roles
- Uses RACI as the primary tool
- No distinction between stated and revealed positions
- No evidence tiers — treats secondhand gossip the same as direct observation
- No sequencing — approaches everyone simultaneously or in random order
- Conclusions are descriptive ("VP might resist") without causal analysis or response plan
- Missing: coalition analysis, decision archaeology, objection pre-emption, communication tailoring

### Consultant Tier
- Applies Power-Interest mapping with scoring rubrics
- Evidence is tiered — distinguishes direct observation from inference
- Coalition analysis identifies allies and opponents
- Objections anticipated with prepared responses
- Alignment sequence is ordered with rationale
- Every finding has a "So What" with recommended action
- Covers the primary stakeholders and their most likely positions
- Missing: decision archaeology depth, steel-manned objections, alignment monitoring, per-stakeholder communication tailoring, contradiction surfacing

### Elite Tier
- All 7 frameworks applied with scoring rubrics and decision tables
- Power decomposed by source (formal, informal, resource, veto) — not a single rating
- Position assessed with evidence tiers on every cell; stated vs. revealed position contradictions surfaced
- Decision archaeology excavates institutional memory, incentive structures, trust networks, and hidden agendas
- Coalition analysis includes power broker identification, critical mass calculation, and defection risk assessment
- Alignment sequence is ordered, time-boxed, dependency-mapped, and anti-pattern-checked
- Every objection is steel-manned — stated stronger than the stakeholder would
- Communication strategy is per-stakeholder: different format, framing, channel, timing, and messenger
- Alignment monitoring dashboard with drift detection and recovery playbooks
- Assumption registry with ≥3 load-bearing assumptions
- Adversarial self-critique with ≥3 genuine weaknesses
- Produces artifacts a PM cannot produce unaided — this is the codex test

---

## Failure Modes

**FM-1: Stakeholder Theater**
*What it looks like:* Alignment meetings happen. Calendar is full. But stakeholder positions don't move. Busy-work disguised as alignment.
*Why it happens:* The PM equates activity (meetings held, updates sent) with progress (positions changed, commitments obtained). Alignment without movement is theater.
*Detection:* Compare stakeholder positions before and after each alignment interaction. If no position changed in 2+ weeks of active engagement, the strategy is failing.
*Correction:* Review the alignment sequence. Are you talking to the right people in the right order? Are conversations addressing the actual drivers of their positions (F3: Decision Archaeology) or just repeating the pitch?

**FM-2: Executive Echo Chamber**
*What it looks like:* The stakeholder map only includes supporters and neutral parties. Blockers and skeptics are absent or underestimated. The alignment strategy feels easy because it ignores the hard parts.
*Why it happens:* Confirmation bias. The PM maps people who agree and avoids mapping people who don't. Or the PM correctly identifies blockers but rates them as "skeptics" to make the alignment gap look smaller.
*Detection:* If the stakeholder map has no 🔴 Blockers and no 🟡- Skeptics, it's almost certainly incomplete. Every real organizational decision has opposition.
*Correction:* Add the stakeholder expansion protocol (Step 1 of Full Method). Explicitly ask: "Who would NOT want this to happen, and why?" If you can't name anyone, you haven't mapped the landscape — you've mapped your comfort zone.

**FM-3: Influence Without Understanding**
*What it looks like:* The PM lobbies stakeholders without knowing what actually drives their positions. Pitches the initiative's benefits without addressing the stakeholder's specific concerns. Solution in search of agreement.
*Why it happens:* Skipping Decision Archaeology (F3). The PM assumes stakeholder positions are based on the merits of the initiative, when they're actually based on past experiences, incentive structures, and political dynamics.
*Detection:* If the Objection Pre-emption Playbook contains only rational objections (data-based) and zero political or emotional objections, the PM hasn't excavated what's really driving resistance.
*Correction:* Run the 5-question interview protocol. Map incentive alignment for every blocker and skeptic. Understand BEFORE persuading.

**FM-4: One-Size-Fits-All Framing**
*What it looks like:* Same pitch deck presented to every stakeholder. Same email sent to the entire decision group. Same "why this matters" regardless of audience.
*Why it happens:* Per-stakeholder communication is effortful. The PM takes the path of least resistance — one deck, one framing, one ask.
*Detection:* If the Communication Strategies section has identical framing for stakeholders with different roles and interests, the strategy is one-size-fits-all.
*Correction:* Apply F6 Communication Strategy. Different stakeholders care about different things. The engineering leader cares about feasibility. The finance leader cares about cost. The exec cares about strategic fit. Same initiative, different "why it matters."

**FM-5: Sequencing Failure**
*What it looks like:* The PM approaches the blocker first ("let me convince the hardest person first") or presents to everyone at once in a group meeting. The blocker frames the conversation before the PM can.
*Why it happens:* Intuitive but wrong logic: "If I can convince the skeptic, everyone else will follow." In reality, approaching the blocker first arms them with your playbook and gives them time to organize opposition.
*Detection:* If the alignment sequence starts with a blocker or a group meeting, sequencing has failed before it started.
*Correction:* Apply F4 Alignment Sequencing rules. Champion first → swing voters → neutrals → skeptics → blockers LAST. 1:1 conversations before any group meeting.

**FM-6: Alignment Decay**
*What it looks like:* The PM won alignment 6 weeks ago. By decision time, the champion has moved on to other priorities, the swing voter has been reframed by the opposition, and verbal commitments have evaporated.
*Why it happens:* Treating alignment as a point-in-time event rather than an ongoing campaign. Verbal alignment decays within 2-4 weeks without reinforcement.
*Detection:* If the alignment monitoring dashboard has "last contact" dates older than 2 weeks for key stakeholders, alignment has likely decayed.
*Correction:* Apply F7 Alignment Monitoring. Set staleness alerts. Re-validate positions before depending on them. Send progress updates to maintain commitment.

**FM-7: The RACI Substitute**
*What it looks like:* A RACI matrix presented as stakeholder alignment. "VP is Accountable, Director is Responsible, PM is Consulted." No position assessment, no coalition analysis, no sequencing.
*Why it happens:* RACI is familiar, taught in every PM training. Stakeholder alignment requires political analysis, which is uncomfortable and unfamiliar.
*Detection:* If the output assigns roles (who does what) but not positions (who supports/opposes/is neutral), it's a RACI, not alignment.
*Correction:* RACI answers "who does what." Stakeholder alignment answers "who needs to agree, why don't they yet, and how do I move them." They're different tools for different problems. Use this skill for alignment, build a RACI separately for execution.

**FM-8: Missing Decision Archaeology**
*What it looks like:* The PM proceeds with alignment without understanding why stakeholders hold their current positions. The alignment strategy addresses surface objections while the real drivers — past failures, political history, incentive conflicts — remain unaddressed.
*Why it happens:* Decision Archaeology is uncomfortable. It requires asking about failures, politics, and hidden agendas. The PM prefers to engage on the merits, assuming rational actors.
*Detection:* If the Decision Archaeology section is empty or contains only T4-T6 evidence (pattern matching and assumptions), the excavation hasn't happened.
*Correction:* Run the 5-question interview protocol with 2-3 trusted insiders. You don't need to know everything — you need to know what the stakeholders won't tell you directly.

**FM-9: Conflict Avoidance Disguised as Consensus**
*What it looks like:* The PM declares alignment when stakeholders have simply stopped objecting. Silence is interpreted as support. Acquiescence is reported as buy-in.
*Why it happens:* The PM conflates absence of opposition with presence of support. In organizations, many stakeholders will not actively oppose — they'll simply disengage, delay, or undermine passively. The PM, uncomfortable with conflict, accepts the silence as victory.
*Detection:* If "aligned" stakeholders haven't taken any action that costs them something (allocated resources, publicly endorsed, changed their own plans), they may be acquiescing, not aligned. Apply the Success Criteria from F7: verbal agreement is the lowest-durability form of alignment.
*Correction:* Push for commitment signals beyond verbal agreement: written approval, resource commitment, or public advocacy. If a stakeholder won't commit beyond "sounds good," they are not aligned — they are politely declining to object.

---

## What's Next

← This skill works best after: **Problem Framing** (if the initiative's strategic rationale needs sharpening) or **Competitive & Market Analysis** (if the decision being aligned on is a competitive response or market entry)
→ This skill's output feeds into: **Narrative Building** (the per-stakeholder framing becomes the basis for positioning), **Spec Writing** (aligned requirements and constraints from the alignment process inform the spec), **Metric Design & Experimentation** (success criteria from the alignment process define what to measure)
⊕ **Start here if:** You have a decision that requires buy-in from multiple people with different interests, and you need a strategy for navigating the organizational landscape
💡 **For a full product cycle:** Problem Framing → **[THIS SKILL]** → Spec Writing → Metric Design & Experimentation → ongoing execution

**Chain interface:**
- **Receives:** A decision or initiative that needs alignment, with optional known stakeholder positions, organizational context, and timeline. From Problem Framing: the validated problem statement and its strategic rationale. From Competitive Analysis: the recommendation that needs organizational buy-in.
- **Produces:** A Stakeholder Alignment Strategy with power-interest-position mapping, coalition analysis, decision archaeology, sequenced alignment plan, per-stakeholder communication playbooks, and objection pre-emption.
- **Handoff artifact:** The alignment strategy's "Communication Strategies" section maps directly to Narrative Building's input (per-audience framing). The "Aligned requirements and accommodations" map to Spec Writing's input (constraints from stakeholder negotiation). The "Success Criteria" map to Metric Design's input (what does success look like?).

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

**Context and fitness:**
- [ ] Context Gate passed: alignment is genuinely needed across multiple stakeholders
- [ ] If no T1-T2 evidence on stakeholder positions: flagged prominently; confidence capped at M
- [ ] How to Read This Document section present with role-based reading guide
- [ ] Notation Key present: H/M/L, T1-T6, O→I→R→C→W, position symbols all explained
- [ ] Executive Summary uses zero framework jargon — plain language only
- [ ] Framework selection routing done (Step 0) — primary frameworks identified, irrelevant frameworks skipped

**Stakeholder mapping:**
- [ ] All relevant stakeholders identified — including non-obvious ones from expansion protocol
- [ ] Power scored by 4 sources (formal authority, informal influence, resource control, veto) with evidence tiers
- [ ] Interest scored with behavioral signals and evidence tiers
- [ ] Position assessed using 5-position taxonomy with evidence tiers
- [ ] Current vs. desired position gap identified for each stakeholder
- [ ] Engagement strategy assigned per Power × Interest quadrant

**Coalition and archaeology:**
- [ ] Coalition types classified: natural allies, marriages of convenience, stable opponents, swing voters
- [ ] Power brokers identified with influence mechanisms
- [ ] Critical mass gap calculated: needed vs. current supporter count
- [ ] Defection risk assessed for coalition members
- [ ] Past decisions researched for institutional memory
- [ ] Incentive alignment scored for each key stakeholder
- [ ] Trust network mapped between stakeholders
- [ ] 5-question interview protocol results incorporated (or flagged as not yet executed)

**Sequencing and objections:**
- [ ] Alignment sequence ordered: champion → swing voters → neutrals → skeptics → blockers
- [ ] Each step time-boxed with dependency mapping
- [ ] Anti-patterns avoided: no blocker-first approach, no all-hands reveal, no email-only alignment
- [ ] Objections anticipated per stakeholder with evidence-based predictions
- [ ] Every objection steel-manned — stated stronger than the stakeholder would
- [ ] Objection type classified (rational, political, emotional, structural) with type-appropriate response
- [ ] Escalation paths defined for unresolved objections

**Communication and monitoring:**
- [ ] Per-stakeholder communication strategies: format, framing, channel, timing, messenger
- [ ] Framing adjusted per stakeholder type — not one-size-fits-all
- [ ] Messenger selection justified — sometimes you, sometimes a peer, sometimes an exec
- [ ] Alignment monitoring dashboard set up with needed vs. current position
- [ ] Drift detection signals listed with response protocols
- [ ] Recovery playbooks defined for common scenarios (lost champion, new stakeholder, scope change)
- [ ] Success criteria defined: what "aligned" looks like at each commitment level

**Quality assurance:**
- [ ] Per-cell evidence tier annotation in ALL stakeholder matrices (not just headline claims)
- [ ] O→I→R→C→W cascade applied to ALL alignment recommendations (not just final section)
- [ ] H/M/L confidence levels explicit on every position assessment and recommendation — no weasel words
- [ ] Position assessments older than 30 days flagged `[POSITION MAY HAVE SHIFTED]`
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key assessment resting only on Tier 4-6 evidence
- [ ] Cross-Framework Contradictions section present — stated vs. revealed positions surfaced
- [ ] Assumption Registry present with ≥3 load-bearing assumptions
- [ ] Adversarial Self-Critique section present with ≥3 genuine weaknesses
- [ ] Revision Triggers defined with observable events and re-assessment scope
