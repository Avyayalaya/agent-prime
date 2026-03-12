---
name: narrative-building
description: "Use when building product positioning, crafting strategy narratives, preparing stakeholder pitches, writing launch narratives, or constructing the 'why now' story for a product or initiative. Encodes Narrative Arc Construction, April Dunford-inspired Positioning, Why Now analysis, Audience Adaptation, Evidence-Narrative Integration, Objection Anticipation, Competitive Narrative Analysis, and Narrative Testing. Produces a Strategic Narrative Document."
version: "1.3.0"
type: "codex"
tags: ["Narrative", "Positioning", "Strategy"]
created: "2026-02-20"
valid_until: "2026-08-20"
derived_from: "original"
tested_with: ["Claude Sonnet 4.5", "Claude Opus 4.6"]
license: "MIT"
---

## Purpose

Produce an elite-tier Strategic Narrative Document that constructs the story making a product, feature, or strategy feel inevitable — not by assertion but by structural argument. The output is not a tagline or a slide deck outline; it is a narrative engineering system: a structural spine, audience-adapted variants, evidence-integrated claims, pre-embedded objection responses, and a testing protocol that validates the narrative before it goes live.

## When to Use / When NOT to Use

**Use this skill when:**
- Positioning a new product or repositioning an existing one in a competitive market
- Preparing a board deck, investor pitch, or executive strategy narrative
- Writing the "why now" story for a product launch or market entry
- Crafting the internal alignment narrative ("here's why we're doing this and not that")
- Building a launch narrative for press, analyst briefings, or customer communications
- Translating competitive analysis findings into a positioning story (downstream of Competitive Analysis)
- A product has strong fundamentals but the story isn't landing with stakeholders or customers

**Do NOT use this skill when:**
- You need competitive analysis (use Competitive & Market Analysis skill first — this skill consumes its output, it does not produce it)
- You need to define what to build (use Specification Writing skill — narrative follows strategy, not the other way around)
- You need customer discovery or research synthesis (use Discovery & Research skill — that's primary research, this is narrative construction from existing inputs)
- You need metric design or success measurement (use Metric Design & Experimentation skill)
- You need a tagline, slogan, or brand identity system (this skill produces strategic narrative, not copy)

**Anti-inputs (what this skill does NOT handle):**
- Customer interview synthesis (-> Discovery & Research skill)
- Competitive landscape mapping (-> Competitive & Market Analysis skill)
- Product specification (-> Specification Writing skill)
- Marketing copy, ad copy, or social media content (-> copywriting, not strategic narrative)
- Visual design for presentations (this produces the narrative structure; design is a separate discipline)

---

## Format Rules (Read First)

These rules govern every output produced by this codex. They are not style preferences — they are quality enforcement mechanisms derived from benchmarking against investment-grade narrative documents and positioning work.

1. **Take positions. Never hedge with weasel words.** "Likely," "may," "could," and "seems" are banned from narrative claims. Flag uncertainty with explicit confidence levels: **H (>70% confident)**, **M (40-70%)**, **L (<40%)**. Example: *"The shift to hybrid work has permanently expanded the market for async collaboration tools (H)"* not *"Hybrid work may be creating opportunities for async tools."*

2. **Per-cell evidence tier annotation is mandatory in all comparison matrices and claim tables.** Every cell in an audience adaptation matrix, competitive narrative comparison, or evidence integration table must carry an inline evidence tier tag: `(T1)`, `(T2)`, `(T3)` etc. Where evidence is absent: `(T6: assertion)`. A matrix with untagged cells is incomplete.

3. **The O->I->R->C->W cascade applies to ALL narrative recommendations**, not just final sections. Format: Observation [evidence tier] -> Implication [mechanism] -> Response [specific narrative action] -> Confidence [H/M/L + assumption] -> Watch Indicator [observable signal that the narrative is or isn't landing].

4. **Begin with Context Fitness Check and Framework Selection (Step 0 / Step 0b)** before applying any framework. Identify the narrative type; select the 3-5 load-bearing frameworks; note which to skip. Applying all 8 frameworks to a simple launch narrative dilutes signal and inflates length.

5. **Contradictions between frameworks are signal, not noise.** When Positioning analysis suggests one category and Competitive Narrative Analysis reveals the category is already owned by a competitor, surface the contradiction explicitly and state which to weight more heavily and why.

6. **Flag time-sensitive claims.** Any claim based on data older than 6 months must carry `[POTENTIALLY STALE -- verify before presenting]`. Market shifts, competitor moves, and regulatory changes erode narrative foundations. Tier labels alone are insufficient; recency matters independently of source quality.

7. **Flag thin-evidence conclusions.** If a key narrative claim rests only on Tier 4-6 evidence, prepend it with `[EVIDENCE-LIMITED: validate with Tier 1-2 before using in external-facing narrative]`.

8. **Every framework reference gets a one-line contextual explanation the first time it appears.** Not "April Dunford's Positioning Framework" but "Dunford's framework for defining what makes your product the best choice for a specific customer in a specific context -- we use it here to identify the positioning that makes competitors irrelevant rather than merely inferior." The framework name is for the author's rigor. The reader needs to know why this lens matters for *their* narrative.

9. **The document must be navigable by someone who didn't create it.** Include a reading guide (by time and by role), a notation key, and layered depth. A VP should be able to read only the Executive Narrative and use it verbatim. A PM should be able to read through the audience-adapted variants and select the right one. A comms lead should be able to dive into the evidence integration and testing protocol. No reader should encounter unexplained notation.

---

## Output Template (Mandatory Document Skeleton)

Every Strategic Narrative Document MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. If a framework was skipped in Step 0, note "Skipped -- not load-bearing for this narrative type" in that section.

```markdown
# Strategic Narrative Document: [Subject -- e.g., "Vanta Analytics Launch Positioning"]

> **Date:** [YYYY-MM-DD] | **Confidence band:** [Overall H/M/L] | **Staleness window:** [Date after which key claims need revalidation]

---

## Executive Narrative

[5-7 sentences max. This IS the narrative -- a VP reads only this and uses it verbatim in their next meeting. No framework names, no jargon, no evidence tier tags. Plain language that makes the product/strategy feel inevitable. Structure: tension -> shift -> opportunity -> your role -> proof -> call to action. Final sentence = the recommended positioning statement in bold.]

---

## How to Read This Document

**What this is:** A narrative engineering system -- not a tagline or a slide deck. It constructs the structural argument for why this product/strategy is inevitable, adapts it for every audience, weaves in evidence, anticipates objections, and provides a testing protocol.

**Reading by time available:**

| Time | Read | You'll get |
|---|---|---|
| **5 min** | Executive Narrative only | The story itself -- ready to use in a meeting |
| **15 min** | Executive Narrative + Narrative Arc (section 1) + Audience Variants (section 4) | The story + its structural logic + which version to use for which audience |
| **30 min** | Full document through Recommendations | Complete narrative system with evidence, objection handling, and competitive positioning |
| **Deep dive** | Everything including Appendix | Full framework applications, testing protocol, assumption stress-testing |

**Reading by role:**

| Role | Start with | Then read | Skip unless curious |
|---|---|---|---|
| VP / Exec | Executive Narrative | Audience Variants (section 4) for their specific context | Everything else -- the narrative is ready to use |
| PM Lead | Executive Narrative | Narrative Arc (section 1), Positioning (section 2), Why Now (section 3), Objection Handling (section 6) | Testing Protocol, Competitive Narrative deep dive |
| Comms / Marketing | Executive Narrative | Audience Variants (section 4), Evidence Integration (section 5), Testing Protocol (section 8) | Framework theory sections |
| Strategy / Analyst | Full document in order | Cross-Framework Contradictions, Adversarial Self-Critique | Nothing -- this is your primary artifact |

---

## Notation Key

**Confidence levels** -- applied to every narrative claim:
- **H (>70% confident)** -- Strong evidence supports this claim. Build the narrative on it.
- **M (40-70%)** -- Direction is probable but evidence is mixed. Use in narrative but flag internally as requiring validation.
- **L (<40%)** -- This is a hypothesis, not a finding. Do not use in external-facing narrative without further evidence.

**Evidence tiers** -- how we know what we claim to know (tagged inline as T1-T6):
- **T1** -- Quantitative proof: revenue data, usage metrics, market share, SEC filings (strongest)
- **T2** -- Customer evidence: testimonials, case studies with measurable outcomes
- **T3** -- Third-party validation: analyst reports, press coverage, awards, expert endorsements
- **T4** -- Logical argument: well-structured reasoning from accepted premises
- **T5** -- Analogies and precedents: "this worked for X, so it should work here"
- **T6** -- Vision/assertion: claims about the future without supporting data (weakest)

**Narrative element ratings:**
- **Strong** -- Element is compelling, evidence-backed, and structurally sound
- **Adequate** -- Element exists but could be strengthened with better evidence or sharper framing
- **Weak/Missing** -- Element is absent or unconvincing; narrative has a structural gap here

**Recommendation format** (O->I->R->C->W):
- **O**bservation -- What we see (with evidence tier)
- **I**mplication -- Why it matters for the narrative (the mechanism)
- **R**esponse -- What to do (specific narrative action + owner + timeline)
- **C**onfidence -- How sure we are (H/M/L + key assumption)
- **W**atch -- How to know if the narrative is landing or failing (observable signal)

**Flags:**
- `[POTENTIALLY STALE]` -- Source data is >6 months old; verify before using in narrative
- `[EVIDENCE-LIMITED]` -- Claim rests on T4-T6 evidence only; validate with stronger data before external use

---

## Step 0: Context Fitness Check

Before selecting frameworks, verify that a Strategic Narrative Document is the right artifact for this question.

| Question | If Yes | If No |
|---|---|---|
| **Do you have a clear product/strategy to narrate, or are you still deciding what to build?** | Proceed to Framework Selection | A narrative is premature. Use Problem Framing or Discovery first. Narrative without substance is spin. |
| **Do you have competitive analysis or market context as input?** | Narrative can incorporate competitive positioning and "why now" with evidence | Flag prominently: "This narrative is constructed without competitive context. Positioning claims are hypotheses -- validate against competitive landscape before external use." |
| **Is the primary goal external (market-facing) or internal (alignment)?** | External: weight Positioning, Audience Adaptation, Evidence Integration heavily. Internal: weight Narrative Arc, Why Now, Objection Anticipation heavily. | Both: produce both variants explicitly; they differ in emphasis, evidence standards, and tone. |
| **Do you have access to customer evidence (testimonials, case studies, usage data)?** | Narrative can use T1-T2 evidence for claims | Flag: "Narrative evidence is limited to T3-T6. Claims will need customer proof points before customer-facing use." |

**If any answer is "No":** State this prominently at the top of the Executive Narrative. Example: *"Note: This narrative is constructed without competitive analysis input. Positioning claims should be treated as hypotheses to be validated against the competitive landscape before external use."*

---

## Step 0b: Framework Selection

| Narrative type | Primary frameworks (apply in full) | Supporting frameworks (scan only) | Skipped (why) |
|---|---|---|---|
| [e.g., "Product launch positioning"] | [e.g., F1 Narrative Arc, F2 Positioning, F3 Why Now, F4 Audience Adaptation] | [e.g., F5 Evidence-Narrative Integration, F6 Objection Anticipation] | [e.g., "F7 Competitive Narrative Analysis -- no direct competitor narrative to reverse-engineer"] |

---

## 1. Narrative Arc

**Status Quo:** [What the world looks like today -- the tension the audience already feels]

**Disruption:** [What has changed -- the structural shift that makes the status quo untenable]

**New Reality:** [What the world looks like after the shift -- the inevitable destination]

**Your Role:** [How this product/strategy is the bridge from status quo to new reality]

**Proof:** [Evidence that this is already happening -- not aspirational, but demonstrated]

**Call to Action:** [What the audience should do next -- specific and immediate]

**Narrative Arc Scorecard:**

| Element | Score | Evidence Tier | Strength Assessment | Gap / Action Needed |
|---|:---:|:---:|---|---|
| Status Quo | 1-5 | TX | [Strong/Adequate/Weak] | [If <4, what's missing] |
| Disruption | 1-5 | TX | | |
| New Reality | 1-5 | TX | | |
| Your Role | 1-5 | TX | | |
| Proof | 1-5 | TX | | |
| Call to Action | 1-5 | TX | | |
| **Total** | X/30 | | | |

---

## 2. Positioning Analysis

**Competitive Alternatives:**

| Alternative | What customers do today instead | Why they switch away from it |
|---|---|---|
| [Alternative 1] | [behavior/product] (TX) | [pain point driving switch] |
| [Alternative 2] | | |
| [Alternative 3] | | |
| "Do nothing" | [current workaround] | [cost of inaction] |

**Unique Attributes:**

| Attribute | Why it matters | Evidence | Defensible? |
|---|---|---|---|
| [Attribute 1] | [value mechanism] | (TX) | H/M/L |
| [Attribute 2] | | | |
| [Attribute 3] | | | |

**Value Delivered:** [Specific, measurable value the customer receives -- not features, but outcomes]

**Target Customer:** [Specific segment with identifying characteristics an outsider could use to find them]

**Market Category Decision:**

| Option | Criteria | Score | Rationale |
|---|---|:---:|---|
| **Create new category** | No existing category captures your value; you'd be compared to wrong alternatives | H/M/L fit | [Why or why not] |
| **Enter existing category** | Category is understood; you win on differentiation within it | H/M/L fit | [Why or why not] |
| **Reframe existing category** | Category exists but the buying criteria are wrong for your strengths | H/M/L fit | [Why or why not] |

**Selected positioning:** [One sentence a new hire could repeat]

---

## 3. Why Now Analysis

**Structural Preconditions:**

| Precondition Type | Specific Shift | Evidence | Independently Verifiable? | Confidence |
|---|---|---|:---:|:---:|
| **Technology shift** | [What technology change enables this now?] | (TX) | Yes/No | H/M/L |
| **Market shift** | [What market dynamic changed?] | (TX) | Yes/No | H/M/L |
| **Regulatory shift** | [What regulatory change opened or closed a door?] | (TX) | Yes/No | H/M/L |
| **Behavioral shift** | [What user/buyer behavior changed?] | (TX) | Yes/No | H/M/L |

**Why Now Scoring Rubric:**

| Score | Criteria |
|:---:|---|
| **5 -- Irrefutable** | Multiple independently verifiable structural shifts converge. Anyone analyzing the market would reach the same "why now" conclusion. Evidence is T1-T2. |
| **4 -- Strong** | 2-3 structural shifts with strong evidence. Reasonable people might disagree on timing but not on direction. Evidence is T1-T3. |
| **3 -- Adequate** | 1-2 structural shifts with moderate evidence. The "why now" is defensible but not self-evident. Evidence is T2-T4. |
| **2 -- Weak** | Structural shift is asserted but not independently verifiable. "Why now" depends on the narrator's framing, not observable market conditions. Evidence is T4-T6. |
| **1 -- Missing** | No structural "why now." The product could have been built 5 years ago or 5 years from now with equal justification. The narrative relies on "we built it, therefore now." |

**Why Now Score:** [X/5] -- [one-sentence assessment]

**The "Not Too Early, Not Too Late" Test:**

| Question | Answer | Implication |
|---|---|---|
| Could this have succeeded 3 years ago? | [Yes/No + why] | If yes: you're late, and must explain what changed. If no: the structural shift is real. |
| Will this opportunity still exist in 3 years? | [Yes/No + why] | If yes: urgency argument is weak -- tighten it. If no: urgency is genuine. |
| Who else sees this timing? | [competitors/entrants] | If many: timing is obvious, differentiation must be on execution. If few: timing insight is a genuine advantage. |

---

## 4. Audience Adaptation Matrix

**Core narrative (invariant across audiences):** [2-3 sentences that never change regardless of audience]

| Dimension | Board / Investors | Engineering | Customers | Press / Analysts |
|---|---|---|---|---|
| **Lead with** | ROI + market size (TX) | Technical vision + feasibility (TX) | Value + trust (TX) | Novelty + significance (TX) |
| **Status Quo framing** | [market inefficiency / missed revenue] | [technical limitation / architecture gap] | [pain point / unmet need] | [industry trend / structural shift] |
| **Disruption framing** | [market shift creating window] | [technology breakthrough enabling solution] | [new possibility for their workflow] | [paradigm change in the category] |
| **Proof type that resonates** | Revenue data, market share, unit economics | Architecture decisions, performance benchmarks, tech stack | Case studies, testimonials, measurable outcomes | First-mover data, analyst validation, adoption velocity |
| **Call to action** | [Approve investment / fund next phase] | [Commit to building this architecture] | [Try the product / expand usage] | [Cover this story / include in report] |
| **Objections to pre-address** | [ROI timeline, competitive risk, market size] | [Technical debt, feasibility, team capacity] | [Switching cost, risk, learning curve] | [Is this real or hype? Who else validates?] |
| **Tone** | Confident, data-driven, opportunity-sized | Honest, technically rigorous, vision-forward | Empathetic, outcome-focused, trustworthy | Authoritative, contextual, non-promotional |
| **Evidence standard** | T1-T2 required; T3 acceptable for market sizing | T1 (benchmarks) + T4 (architecture reasoning) | T2 (testimonials) + T1 (measurable outcomes) | T3 (expert validation) + T1 (data proof) |

**Audience-Specific Narrative Variants:**

### Board / Investor Variant
[Full narrative adapted for this audience -- 1 paragraph max, using their proof types, tone, and lead]

### Engineering Variant
[Full narrative adapted for this audience]

### Customer Variant
[Full narrative adapted for this audience]

### Press / Analyst Variant
[Full narrative adapted for this audience]

---

## 5. Evidence-Narrative Integration

**Claim-Evidence-Implication Chain:**

| # | Narrative Claim | Evidence | Tier | Implication for Audience | Integration Method |
|---|---|---|:---:|---|---|
| 1 | [claim made in the narrative] | [specific data point or proof] | TX | [so what -- why this evidence matters to the reader] | [Embedded in narrative / Footnoted / Callout box] |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Evidence Density Assessment:**

| Narrative Section | Claims Made | Claims with T1-T2 Evidence | Claims with T3-T4 Evidence | Claims with T5-T6 Only | Evidence Gap? |
|---|:---:|:---:|:---:|:---:|:---:|
| Status Quo | X | X | X | X | Yes/No |
| Disruption | | | | | |
| New Reality | | | | | |
| Your Role | | | | | |
| Proof | | | | | |

**Anti-Pattern Check:**

| Anti-Pattern | Present? | Fix |
|---|:---:|---|
| **Data dump without narrative thread** -- evidence is listed but not woven into a story. Reader sees numbers but not meaning. | Yes/No | Each data point must answer "so what?" in the context of the narrative arc. Data serves story; story does not serve data. |
| **Narrative without data support** -- story is compelling but no claims are backed by evidence. Reader is persuaded but cannot defend the argument. | Yes/No | Every claim in the arc that a skeptic would challenge must have at least T3 evidence. External-facing claims require T1-T2. |
| **Evidence-claim mismatch** -- the evidence cited does not actually support the claim being made. Correlation presented as causation, or adjacent data used for a different point. | Yes/No | For each claim-evidence pair, ask: "Does this evidence DIRECTLY support this specific claim, or is it merely related?" |

---

## 6. Objection Anticipation & Pre-Response

**Objection Inventory:**

| # | Objection (steelmanned) | Probability of Being Raised | Severity if Unaddressed | Difficulty of Response | Priority Score |
|---|---|:---:|:---:|:---:|:---:|
| 1 | [strongest version of the objection -- argue it as forcefully as the objector would] | H/M/L | H/M/L | H/M/L | [sum] |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Priority Scoring:**
- H = 3, M = 2, L = 1
- Priority = Probability + Severity + Difficulty
- Score 7-9: Must be pre-embedded in narrative. Score 4-6: Prepare response but embed only if space allows. Score 3: Monitor but do not address preemptively.

**Pre-Embedded Responses:**

**Objection 1: [Title]**
- **Steelmanned objection:** [The strongest version of this argument against you]
- **Pre-embedded response:** [How the narrative addresses this WITHOUT sounding defensive -- the response is woven into the story, not appended as a rebuttal]
- **Where in narrative:** [Which section of the arc naturally addresses this]
- **Evidence supporting response:** (TX) [specific proof]
- **If pressed further:** [The deeper response for follow-up questions]

**Objection 2: [Title]**
[Same structure]

**Objection 3: [Title]**
[Same structure]

---

## 7. Competitive Narrative Analysis

**Competitor Narrative Reverse-Engineering:**

| Dimension | Competitor A | Competitor B | Competitor C | Your Narrative |
|---|---|---|---|---|
| **Their story in one sentence** | [what they claim] (TX) | | | [what you claim] |
| **Status quo they attack** | [the tension they highlight] | | | [the tension you highlight] |
| **Disruption they claim** | [their "why now"] | | | [your "why now"] |
| **Proof they offer** | [their evidence type and quality] | | | [your evidence type and quality] |
| **Category they claim** | [how they frame the market] | | | [how you frame the market] |
| **Audience they optimize for** | [who their narrative targets first] | | | [who your narrative targets first] |

**Narrative Strength Comparison:**

| Element | Competitor A | Competitor B | Your Narrative | Gap / Advantage |
|---|:---:|:---:|:---:|---|
| Status Quo resonance | 1-5 (TX) | 1-5 (TX) | 1-5 (TX) | [where you win/lose] |
| Disruption credibility | 1-5 (TX) | 1-5 (TX) | 1-5 (TX) | |
| Proof strength | 1-5 (TX) | 1-5 (TX) | 1-5 (TX) | |
| Why Now clarity | 1-5 (TX) | 1-5 (TX) | 1-5 (TX) | |
| Audience fit | 1-5 (TX) | 1-5 (TX) | 1-5 (TX) | |

**Narrative Gaps to Exploit:**

| Competitor Gap | Why It Exists | How Your Narrative Exploits It | Risk of Them Closing It |
|---|---|---|---|
| [specific weakness in their story] | [structural reason] (TX) | [your narrative move] | H/M/L |
| | | | |

**Narrative Collision Points:**

Where your narrative and a competitor's narrative make directly contradictory claims -- these are the battlegrounds where the audience must choose which story to believe.

| Collision Point | Their Claim | Your Claim | Evidence Advantage | Resolution for Audience |
|---|---|---|---|---|
| [specific contested territory] | [what they say] (TX) | [what you say] (TX) | [who has stronger evidence?] | [why the audience should believe your version] |

---

## 8. Narrative Testing Protocol

**Pre-Launch Validation Tests:**

| Test | Method | Pass Criteria | Fail Signal | Action on Fail |
|---|---|---|---|---|
| **"Say It Back" Test** | Tell narrative to 5 people. Ask them to repeat it back in their own words within 24 hours. | >=4 of 5 can reproduce the core argument (not word-for-word, but structurally accurate) | <3 of 5 can reproduce it | Narrative is too complex or unmemorable. Simplify the arc. Reduce to fewer, stronger claims. |
| **"So What" Test** | After delivering the narrative, ask: "So what should I do about this?" | Audience names a specific action aligned with your call to action | Audience says "interesting" but names no action, or names the wrong action | Call to action is unclear or disconnected from the narrative arc. Strengthen the bridge from proof to action. |
| **"Why Should I Care" Test** | Deliver the narrative to someone outside the target audience. Ask: "Why would [target audience] care about this?" | Outsider can articulate the audience's motivation correctly | Outsider cannot identify why the target cares | Status Quo section is not resonating -- the tension is not universal enough or is framed in insider language. |
| **"What Would Change Your Mind" Test** | Ask a friendly skeptic: "What evidence would make you disbelieve this narrative?" | Skeptic names specific, falsifiable conditions that are not currently true | Skeptic names conditions that ARE currently true | Narrative contains a claim that is already falsified. Remove or reframe immediately. |
| **"Borrowed Story" Test** | Replace your company name with a competitor's. Does the narrative still work? | Narrative breaks -- it depends on YOUR unique attributes, evidence, and positioning | Narrative works equally well for a competitor | Narrative is generic. Return to Positioning (F2) and strengthen unique attributes. |

**Narrative Testing Scorecard:**

| Test | Result | Score (1-5) | Action |
|---|---|:---:|---|
| Say It Back | [pass/fail + detail] | | [if <4, specific fix] |
| So What | | | |
| Why Should I Care | | | |
| What Would Change Your Mind | | | |
| Borrowed Story | | | |
| **Total** | | X/25 | |

**Scoring Guide:**
- 20-25: Narrative is ready for external use
- 15-19: Narrative needs targeted strengthening before external use
- 10-14: Narrative has structural issues; revisit arc and positioning
- <10: Narrative requires fundamental rework

---

## 9. Strategic Narrative Recommendations (O->I->R->C->W Cascade)

**Recommendation 1: [Title]**
- **Observation** [TX]: [What we see in the narrative analysis]
- **Implication**: [Why it matters for the narrative's effectiveness]
- **Response**: [Specific narrative action + owner + timeline]
- **Confidence**: [H/M/L] -- assumes [key assumption]
- **Watch**: [Observable signal that this narrative move is working or failing]

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
| [e.g., "Category choice vs. competitive narrative"] | [Positioning: create new category] | [Competitive Narrative: competitor already owns that framing] | [Which matters more and why] |

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
[Steelmanned argument against the narrative. What assumption is made? What evidence would disprove it? Scenario where this narrative backfires catastrophically.]

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
1. **Do not skip sections.** If a section isn't applicable, write "Skipped -- [reason]" and move on.
2. **Every table cell with a claim, rating, or comparison must have an evidence tier tag** -- `(T1)` through `(T6)`.
3. **Section headers are conclusions, not labels.** Replace generic headers (e.g., "Positioning Analysis") with insight headers (e.g., "We Own the Workflow Category -- Competitors Own the Dashboard Category") after completing the section.
4. **The Executive Narrative is written last** but appears first. Do not write it until all sections are complete.
5. **Audience variants are not optional.** A narrative without audience adaptation is a one-audience narrative (FM-4). Produce at least 3 variants.

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with its scoring rubrics, decision tables, and application methodology -- not merely referenced. A PM using this skill produces narrative documents that withstand scrutiny, adapt to audiences, and pre-empt objections; without these frameworks, the output degrades to a slide deck outline.

### Framework 1: Narrative Arc Construction (F1)

The structural spine of every strategic narrative. A compelling narrative is not a list of features or a collection of data points -- it is a story with a specific structural shape that creates tension, resolves it, and positions your product as the inevitable resolution.

**The Six-Element Arc:**

| Element | Purpose | What It Must Do | Failure Mode if Missing |
|---------|---------|-----------------|------------------------|
| **Status Quo** | Establish shared reality with the audience | Name a tension the audience already feels -- not a problem they need to be educated about | No shared starting point; audience questions your understanding of their world |
| **Disruption** | Create urgency | Identify a structural change that makes the status quo untenable -- not just uncomfortable, but unsustainable | No urgency; "this is interesting" instead of "we must act" |
| **New Reality** | Paint the destination | Describe the world after the shift -- make it feel inevitable with or without your product | No vision; audience cannot see where this is going |
| **Your Role** | Position your product | Show how your product/strategy is the best bridge from status quo to new reality | No differentiation; "any product could do this" |
| **Proof** | Establish credibility | Provide evidence this is already happening -- working examples, data, or testimonials | No credibility; narrative is aspiration without foundation |
| **Call to Action** | Drive behavior | Tell the audience exactly what to do next -- specific and immediate | No conversion; "great story" but no next step |

**Scoring Rubric -- Per Element:**

| Score | Criteria | Diagnostic |
|:-----:|----------|------------|
| **5** | Element is compelling, evidence-backed (T1-T2), and structurally necessary -- removing it breaks the narrative | "Can I remove this without weakening the story?" If removing it breaks it: 5. |
| **4** | Element is strong and evidence-supported (T1-T3), but could be sharper or more specific | "Would a skeptic challenge this?" If not: 4. If yes: needs strengthening. |
| **3** | Element exists and is defensible, but relies on weaker evidence (T3-T4) or generic framing | "Have I heard this exact argument from another company?" If yes: it's generic. 3. |
| **2** | Element is present but weak -- asserted without evidence, or framed in a way that doesn't resonate with the target audience | "Would the audience nod along but not remember this tomorrow?" If yes: 2. |
| **1** | Element is missing or counterproductive -- either absent or actively undermining the narrative (e.g., a "disruption" that's actually a feature description) | "Does this element earn its place in the story?" If no: 1. |

**Arc Quality Thresholds:**

| Total Score (out of 30) | Assessment | Action |
|:---:|---|---|
| 25-30 | Narrative is structurally sound and ready for audience adaptation | Proceed to Framework 2 |
| 18-24 | Narrative has the right shape but weak elements; strengthen before adapting | Address every element scoring <4 before proceeding |
| 12-17 | Narrative has structural issues; the story doesn't flow from tension to resolution | Rebuild the arc from Status Quo forward; likely missing Disruption or Proof |
| <12 | Narrative is not a story -- it's a feature list or data dump dressed up as narrative | Start over. Begin with "What tension does the audience already feel?" |

**The Inevitability Test:**

The strongest narratives make the product feel *inevitable* -- not because the narrator says so, but because the structural argument leaves no other conclusion. Test your arc:

| Question | Strong Answer | Weak Answer |
|----------|---------------|-------------|
| After hearing Status Quo + Disruption, does the audience say "yes, and..."? | The audience is already leaning forward, expecting the New Reality | The audience says "I'm not sure that's true" or "that doesn't affect me" |
| After hearing New Reality, could the audience predict Your Role? | The positioning is so natural that the audience anticipates it | Your Role feels like a pivot -- "wait, how did we get here?" |
| After hearing Proof, does the audience feel this is happening now? | "This isn't a pitch; this is a report on reality" | "Sounds like a vision, not a fact" |

**Decision Table -- Arc Construction:**

| Condition | Action |
|-----------|--------|
| Status Quo doesn't resonate with the audience | You're narrating YOUR tension, not THEIR tension. Interview the audience. What keeps them up at night? |
| Disruption is a feature description ("we built X") | Reframe as a structural shift. Not "we built AI search" but "the shift from query-based to intent-based information retrieval" |
| New Reality is indistinguishable from a competitor's | Your New Reality must include an element that ONLY your product can deliver. Otherwise, you're narrating their opportunity. |
| Your Role section lists features | Reframe in terms of the bridge: "We are the [mechanism] that makes [New Reality] accessible to [Target Customer]" |
| Proof section has only T5-T6 evidence | Narrative is not ready for external use. Acquire T1-T2 proof before launching. |
| Call to Action is vague ("learn more") | Specify the action, the timeline, and what the audience gets by acting: "Start a pilot by Q3 and see [specific outcome] within 90 days" |

---

### Framework 2: Positioning Framework (F2)

Inspired by April Dunford's positioning methodology -- the systematic process of defining what makes your product the obvious choice for a specific customer in a specific context. Positioning is not messaging; it is the strategic decision about how the product will be perceived. Messaging follows positioning; never the reverse.

**The Five Positioning Components:**

| Component | Question | Common Mistake | How to Get It Right |
|-----------|----------|----------------|---------------------|
| **Competitive Alternatives** | What would the customer do if your product didn't exist? | Listing only direct competitors; missing "do nothing," spreadsheets, manual processes, and status quo | List EVERYTHING the customer considers -- including workarounds, inaction, and internal tools. The real alternative is rarely your closest competitor. |
| **Unique Attributes** | What do you have that alternatives don't? | Listing features instead of capabilities that matter. "AI-powered" is an attribute; "processes 10,000 documents in 2 minutes" is a capability. | Each attribute must pass the "so what" test: if the customer doesn't care about this attribute, it's not a positioning asset. |
| **Value Delivered** | What does the customer GET from those attributes? | Stating value in company terms ("increases revenue") instead of customer terms ("saves your team 15 hours/week on compliance reporting") | Value must be stated in the customer's language, describing their outcome, not your metric. |
| **Target Customer** | Who cares the most about this value? | "Everyone" or demographics-only targeting. "Mid-market SaaS companies" is a demographic; "Compliance teams at mid-market SaaS companies who are manually tracking SOC 2 evidence" is a target. | The target customer has a *specific pain* that your unique attributes address better than any alternative. If your target is too broad, your positioning is too weak. |
| **Market Category** | What frame of reference helps the customer understand you? | Choosing a category because it's trendy rather than because it sets the right expectations. "AI platform" sets different expectations than "compliance automation." | The category must trigger the right set of buying criteria -- criteria where you win. |

**Category Decision Table:**

| Decision | When to Choose | Signals | Risk | Mitigation |
|----------|---------------|---------|------|------------|
| **Create new category** | No existing category captures your value proposition; existing categories trigger the wrong buying criteria and comparisons | Customers say "I've never seen anything like this." Analysts don't know where to put you. | Enormous education burden. Customers may not understand what you are. Long sales cycles. | Anchor to a known pain point. "The first [known concept] for [new context]." Example: "DevOps for compliance" made Vanta intelligible. |
| **Enter existing category** | Category is well-understood and growing; you have genuine differentiation on the buying criteria that matter | Clear competitive set, established buyer expectations, existing budget category | Compared directly to incumbents on THEIR terms. Feature parity becomes table stakes. | Enter only if you can differentiate on 2+ buying criteria that matter to underserved segments. |
| **Reframe existing category** | Category exists but the buying criteria are wrong for your strengths; you need to shift how the category is evaluated | Customers buy on criteria where you lose; your strengths are on criteria they don't yet prioritize | Requires changing buyer behavior, not just buyer choice. Slower than entering on current criteria. | Lead with a trend or structural shift that makes the NEW criteria urgent. "The old way of evaluating [category] doesn't work because [disruption]." |

**Positioning Strength Rubric:**

| Dimension | Score 1 (Weak) | Score 3 (Adequate) | Score 5 (Strong) |
|-----------|---------------|-------------------|-----------------|
| **Alternatives clarity** | Only direct competitors listed | Direct + indirect alternatives | Complete landscape including "do nothing" and workarounds |
| **Attribute uniqueness** | Features shared with competitors | Some unique capabilities | 2+ capabilities no alternative offers |
| **Value specificity** | Generic value ("saves time") | Outcome-oriented ("saves 15 hrs/week") | Quantified + customer-validated outcome ("saves 15 hrs/week; validated by 12 customers") |
| **Target precision** | "Everyone" or broad demographics | Job-role + company-type targeting | Specific pain + specific persona + specific buying moment |
| **Category fit** | Category triggers wrong comparisons | Category is acceptable but not advantageous | Category sets buying criteria where you win |

---

### Framework 3: "Why Now" Framework (F3)

The most common narrative failure is differentiation without timing. "We're better" is not a narrative. "We're better, AND the structural conditions that make this matter just arrived" is a narrative. The "Why Now" framework identifies the structural preconditions that make this moment uniquely right -- not marketing urgency, but genuine structural timing.

**The Four Structural Preconditions:**

| Precondition | Definition | Scoring Criteria | Example |
|-------------|-----------|-----------------|---------|
| **Technology Shift** | A new technology capability that didn't exist (or wasn't mature enough) before | Must be independently verifiable by citing a specific technology milestone, not a general trend | "GPT-4-class models now process 128K token contexts, enabling full-document analysis for the first time" (T1: model specs) -- not "AI is getting better" |
| **Market Shift** | A change in market structure, buyer behavior, or competitive landscape | Must cite a measurable change: market size shift, consolidation event, buyer budget reallocation | "The compliance automation market grew 340% in 3 years as SOC 2 became a sales prerequisite, not a nice-to-have" (T3: analyst report) |
| **Regulatory Shift** | A new regulation, enforcement action, or policy change that creates demand or removes barriers | Must cite the specific regulation, enforcement action, or policy with effective date | "EU AI Act enforcement begins 2026, requiring audit trails for every AI decision -- 85% of companies have no system for this" (T1: regulation text + T3: survey data) |
| **Behavioral Shift** | A change in how people work, buy, or use technology that creates new needs or makes old solutions inadequate | Must cite observable behavior change with data, not assumed behavior change | "Remote work normalized async decision-making: 67% of strategic decisions now happen without a real-time meeting" (T2: survey, large sample) -- not "people work differently now" |

**Precondition Scoring:**

Each precondition is scored independently:

| Score | Criteria |
|:-----:|----------|
| **5** | Verifiable with T1-T2 evidence. Happened within last 12 months. Directly creates demand for your specific product. |
| **4** | Verifiable with T2-T3 evidence. Happened within last 24 months. Creates demand for your product category. |
| **3** | Verifiable with T3-T4 evidence. Trend is real but timing is debatable. Creates general market opportunity. |
| **2** | Claimed but not independently verifiable. Based on T4-T5 evidence. Could be true but could also be confirmation bias. |
| **1** | Asserted without evidence. "Everyone knows..." or "The market is shifting toward..." without data. |

**Composite Why Now Score:**

| Composite | Calculation |
|-----------|-------------|
| Add all applicable precondition scores | Max possible = 20 (all four at 5) |
| **16-20** | "Why Now" is structurally bulletproof. Lead with timing in the narrative. |
| **11-15** | "Why Now" is credible. Include but don't make it the centerpiece. |
| **6-10** | "Why Now" is thin. Either find stronger evidence or de-emphasize timing in favor of differentiation. |
| **<6** | There is no structural "Why Now." The narrative must rely on other elements. Do NOT fabricate timing urgency. |

**The Timing Trap Detector:**

| Trap | What It Sounds Like | Test | Fix |
|------|---------------------|------|-----|
| **Manufactured urgency** | "The window is closing!" with no structural basis | Can you name the specific event that closes the window, with a date? If not: manufactured. | Remove urgency claim or replace with a genuine structural trigger. |
| **Trend extrapolation** | "X is growing Y% so it will be Z by next year" | Is the trend accelerating, linear, or decelerating? Are there structural ceilings? | State the growth with its deceleration risk, not just its current trajectory. |
| **Survivor narrative** | "Company A succeeded by doing this at this moment" | Would Company A have succeeded at a different moment? Did Companies B-E try the same thing and fail? | Survivorship bias invalidates single-example "why now" arguments. Require 3+ examples or structural reasoning. |

---

### Framework 4: Audience Adaptation Matrix (F4)

The same core narrative, adapted for different audiences by changing emphasis, proof type, framing, and call to action -- without changing the underlying truth. A narrative that works for every audience works for none. The Audience Adaptation Matrix is the systematic method for producing variants that share a structural spine but differ in what they lead with.

**The Invariance Principle:**

The core narrative (Status Quo -> Disruption -> New Reality -> Your Role) must be *structurally identical* across all audience variants. What changes:
- **What you lead with** (the first thing the audience hears)
- **What evidence you emphasize** (different audiences trust different proof types)
- **What objections you pre-address** (different audiences have different fears)
- **What call to action you make** (different audiences have different agency)
- **What you omit** (every audience gets less detail in areas they don't control)

What does NOT change:
- The core claim about what is true in the market
- The structural logic of why now
- The factual evidence base (you can emphasize different facts, but you cannot contradict between audiences)

**Audience Decision Table:**

| Audience | They Optimize For | They Fear | Lead With | Prove With | Ask Them To |
|----------|------------------|-----------|-----------|------------|-------------|
| **Board / Investors** | Return on investment; market share; competitive position | Wasted capital; missed market window; competitive blindside | Market size + timing (TX) | Revenue data, market share, unit economics (T1) | Approve investment; fund next phase; remove blockers |
| **Engineering** | Technical excellence; feasibility; maintainability | Technical debt; impossible commitments; scope creep | Technical possibility + architecture vision | Benchmarks, architecture diagrams, proof-of-concept results (T1) | Commit to building; validate technical approach; estimate effort |
| **Customers** | Value for their money/time; risk reduction; trust | Switching cost; implementation failure; vendor lock-in | Their pain point + specific outcome they'll get | Case studies, testimonials, trial results (T2) | Try the product; expand usage; become a reference |
| **Press / Analysts** | Newsworthiness; accuracy; significance | Being wrong; promoting vaporware; missing the real story | What's genuinely new + industry significance | Data, expert quotes, competitive context (T1 + T3) | Cover the story; include in report; brief their audience |
| **Internal Team** | Meaning in their work; clarity of direction; achievability | Wasted effort; shifting priorities; lack of conviction from leadership | Why this matters + why we're uniquely positioned | Customer feedback, competitive gaps, team capability (T1 + T2) | Align behind this direction; prioritize accordingly |

**Adaptation Quality Check:**

For each audience variant, verify:

| Check | Pass | Fail |
|-------|------|------|
| Does the variant lead with what THIS audience cares about? | First sentence addresses their primary concern | First sentence addresses YOUR concern, not theirs |
| Does the variant use proof types THIS audience trusts? | Evidence matches audience trust hierarchy (see table above) | Same evidence for all audiences regardless of trust profile |
| Does the variant pre-address THIS audience's top objection? | The objection is handled before the audience raises it | Objection is absent or addressed with wrong evidence type |
| Is the call to action within THIS audience's agency? | Audience can take the requested action without escalation | Asks them to do something outside their authority |
| Could you replace this with the variant for a DIFFERENT audience? | No -- it would feel wrong for the other audience | Yes -- the variant is generic enough to work for anyone |

---

### Framework 5: Evidence-Narrative Integration (F5)

The systematic method for weaving data into story without losing either. Most narratives fail in one of two ways: they are compelling stories with no proof (narrative without data), or they are data-rich documents with no story (data without narrative). The Claim-Evidence-Implication pattern prevents both failures.

**The C-E-I Pattern (Claim -> Evidence -> Implication):**

Every substantive claim in the narrative follows this three-part structure:

| Part | Purpose | Format | Example |
|------|---------|--------|---------|
| **Claim** | State what you believe to be true | Declarative sentence, no hedging | "The compliance automation market is in a structural transition from manual to automated workflows." |
| **Evidence** | Prove the claim is true, not merely asserted | Specific data point with evidence tier | "SOC 2 audit preparation costs dropped 62% for companies using automated evidence collection vs. manual processes (T2: Vanta customer survey, n=340, Jan 2026)." |
| **Implication** | Explain why this matters to the audience | "This means..." statement connecting claim to audience concern | "This means any compliance team still running manual processes is spending 3x what their automated peers spend -- and the gap widens every quarter as audit requirements increase." |

**Evidence Integration Methods:**

| Method | When to Use | Example | Risk |
|--------|-----------|---------|------|
| **Embedded** | Claim is central to the narrative arc; evidence must be immediate | "Teams using automated compliance save 62% (T2: n=340 survey) -- which means manual processes aren't just slow, they're a competitive liability." | Can slow the narrative pace if overused |
| **Anchored** | Evidence is important but detailed; anchor with a headline, detail in footnote | "Automated compliance cuts costs by 62%.^1" with footnote: "^1 Vanta customer survey, Jan 2026, n=340" | Footnotes may not be read in verbal presentations |
| **Callout box** | Evidence is particularly striking and deserves visual emphasis | Sidebar: "62% cost reduction -- verified across 340 companies" | Overuse dilutes impact; reserve for 2-3 key data points |
| **Narrative flow** | Evidence is woven naturally into the story arc, not presented as a separate "proof" section | "When Acme Corp switched, they cut audit prep from 6 weeks to 3 days. Their compliance lead said..." | Requires strong writing; poorly executed, it feels like an ad |

**Evidence Density Targets:**

| Narrative Section | Minimum Evidence Standard | Rationale |
|-------------------|--------------------------|-----------|
| Status Quo | T3-T4 (the audience already believes the tension; you need context, not proof) | Over-proving the status quo bores the audience. They know. |
| Disruption | T1-T3 (the disruption must be credibly new; this is where skeptics challenge) | Under-proving the disruption kills the narrative. The skeptic asks "is this really happening?" |
| New Reality | T4-T6 acceptable (this is vision; evidence is directional, not definitive) | The new reality hasn't fully arrived -- acknowledge this. |
| Your Role | T1-T2 required for external narratives; T3-T4 acceptable for internal | Your Role is where credibility lives or dies. Weak proof here destroys the arc. |
| Proof | T1-T2 mandatory (this section exists specifically to provide evidence) | If the Proof section relies on T5-T6, the narrative is not ready for external use. |

**Anti-Patterns (encoded as detection + correction):**

| Anti-Pattern | Detection Signal | Correction |
|-------------|-----------------|------------|
| **Data dump** | >3 data points in a single paragraph; audience glazes over; no "so what" after any number | Each data point earns its place by answering one specific "so what." If two data points answer the same "so what," cut the weaker one. |
| **Narrative without data** | Exciting story that a skeptic can dismantle in 60 seconds; no claim has a source | Walk through the arc element by element. For each claim, ask: "What would a skeptic say?" If the answer is "prove it," you need evidence there. |
| **Evidence-claim mismatch** | Evidence cited is "adjacent" to the claim but doesn't directly support it; correlation treated as causation | For each C-E-I triplet, ask: "Does this evidence DIRECTLY prove this specific claim?" If it merely supports a related point, find better evidence or weaken the claim. |
| **Stale evidence** | Data cited is >6 months old in a fast-moving market | Flag `[POTENTIALLY STALE]`. Seek fresh data. If unavailable, acknowledge the gap and state why the directional conclusion still holds. |

---

### Framework 6: Objection Anticipation Framework (F6)

A narrative that doesn't anticipate objections is a narrative waiting to be dismantled. The Objection Anticipation Framework systematizes the process of identifying, prioritizing, and pre-embedding responses to the strongest arguments against your narrative.

**The Steelmanning Requirement:**

Every objection must be stated in its strongest form -- the way the most articulate, most informed critic would state it. Not a straw man. Not a softened version. The real objection, argued as forcefully as possible.

| Steelmanned (required) | Straw man (rejected) |
|------------------------|---------------------|
| "Your compliance automation handles SOC 2 well, but enterprise customers need ISO 27001, HIPAA, and SOX simultaneously. Single-framework tools create more compliance silos, not fewer." | "People might think we only do SOC 2." |
| "The 62% cost reduction figure comes from companies with <500 employees. At enterprise scale, the integration overhead offsets automation gains, and the last 20% of audit evidence still requires manual expert judgment." | "Some companies might not save as much." |

**Objection Scoring Matrix:**

| Dimension | H (3 points) | M (2 points) | L (1 point) |
|-----------|-------------|-------------|-------------|
| **Probability of being raised** | Will be raised in >70% of presentations to this audience | Will be raised in 30-70% of presentations | Unlikely to surface unprompted |
| **Severity if unaddressed** | Narrative fails -- audience walks away unconvinced or actively opposed | Narrative weakened -- audience has doubts but stays engaged | Minor -- audience notes it but it doesn't change their conclusion |
| **Difficulty of response** | No easy answer; requires structural argument and evidence | Answer exists but requires nuance; one-liner won't suffice | Simple, factual answer that resolves the objection immediately |

**Priority Tiers:**

| Priority Score | Tier | Action |
|:--------------:|------|--------|
| 7-9 | **Critical** | Must be pre-embedded in the narrative arc itself -- the story should address this before the audience raises it |
| 4-6 | **Important** | Prepare a response; embed in narrative if space allows; have ready for Q&A |
| 1-3 | **Monitor** | Acknowledge if raised but do not address preemptively; addressing minor objections clutters the narrative |

**Pre-Embedding Techniques:**

The goal is to address objections *within the narrative flow*, not in a defensive appendix. Techniques:

| Technique | How It Works | Example |
|-----------|-------------|---------|
| **Preemptive concession** | Acknowledge the limitation before the audience raises it, then pivot to why it doesn't matter (or matters less than they think) | "We started with SOC 2 -- deliberately. [Concession.] The compliance problem isn't breadth of frameworks; it's the 80% of evidence collection that's identical across all frameworks. [Pivot.] We solve the common denominator first, then extend." |
| **Reframing** | Accept the premise of the objection but change the frame of reference | "Yes, enterprise integration is complex. That's exactly why we built an API-first architecture rather than a monolithic platform -- you integrate what you need, not what we decided to ship." |
| **Evidence preemption** | Provide the data that answers the objection before it's asked | "Our enterprise customers -- including three Fortune 500 companies -- see 48% cost reduction, not the 62% our SMB customers see. Different scale, still transformative." |
| **Narrative inoculation** | Mention the objection in a way that makes raising it feel unnecessary | "You might be thinking: 'but does this scale to enterprise?' We wondered the same thing. Here's what we found..." |

---

### Framework 7: Competitive Narrative Analysis (F7)

Every competitor tells a story. Most companies never analyze those stories structurally -- they react to competitor *features* without understanding competitor *narratives*. Competitive Narrative Analysis reverse-engineers the story each competitor tells, identifies where those stories are strong, and finds the gaps your narrative can exploit.

**Narrative Reverse-Engineering Method:**

For each significant competitor, decode their narrative arc:

| Step | Action | Source |
|------|--------|--------|
| 1. Find their origin story | What founding narrative do they tell? What problem do they claim to have discovered? | About page, founder interviews, early press coverage (T3-T5) |
| 2. Decode their "Why Now" | What timing claim do they make? Is it genuine or manufactured? | Launch messaging, investor pitches, keynote speeches (T5) |
| 3. Identify their positioning | What category do they claim? What buying criteria do they set? | Website positioning, analyst briefings, sales collateral (T5) |
| 4. Map their proof strategy | What evidence do they lead with? What evidence tier dominates? | Case studies, press releases, testimonials, benchmark claims (T2-T5) |
| 5. Find the narrative gaps | Where does their story fail the "so what" or "prove it" test? | Customer reviews, analyst critiques, competitor comparisons (T2-T3) |

**Competitive Narrative Strength Assessment:**

For each competitor's narrative, score these dimensions:

| Dimension | What to Assess | Score 1 (Weak) | Score 3 (Adequate) | Score 5 (Strong) |
|-----------|---------------|----------------|-------------------|-----------------|
| **Origin story resonance** | Does their founding narrative create emotional connection? | Generic: "We saw a problem and decided to fix it" | Specific: "Our founder experienced X at Company Y" | Iconic: The origin story IS the brand -- inseparable from the product |
| **Disruption credibility** | Is their "why now" structurally grounded? | Manufactured urgency with no evidence | Real trend, but not unique to them | Structural shift that only they saw first |
| **Positioning precision** | Do they own a clear category position? | "We do everything for everyone" | Clear category, but shared with competitors | Own the category or set the buying criteria |
| **Proof density** | How much evidence backs their claims? | Assertions only (T5-T6) | Case studies and benchmarks (T2-T3) | Quantified, multi-source, independently verified (T1-T2) |
| **Narrative consistency** | Does the same story appear across all channels? | Different story on website, in sales, and at conferences | Mostly consistent with minor variations | Exact same structural arc everywhere -- well-drilled |

**Gap Exploitation Decision Table:**

| Gap Type | How to Exploit | Risk |
|----------|---------------|------|
| **Weak origin story** | Your origin story becomes the differentiator; lead with "why we exist" | They can acquire a better origin story through acquisition or rebrand |
| **Manufactured "Why Now"** | Lead with your genuine structural "Why Now" with T1-T2 evidence; make their timing claim look hollow | If their timing claim becomes real, your advantage disappears |
| **Vague positioning** | Position precisely where they are vague; claim the specific niche they're leaving undefended | If they sharpen their positioning, the gap closes |
| **Thin proof** | Lead with evidence density; make every claim provable; contrast implicitly | They can acquire proof through customer growth -- this gap is temporary |
| **Inconsistent narrative** | Own a single, repeated story that becomes synonymous with the category; repetition beats variety | Requires discipline -- your team must tell the same story every time |

---

### Framework 8: Narrative Testing Protocol (F8)

A narrative that hasn't been tested is a hypothesis. The Narrative Testing Protocol provides five structured tests that validate whether a narrative is memorable, actionable, resonant, defensible, and differentiated -- before it goes live.

**Test 1: The "Say It Back" Test (Memorability)**

| Parameter | Specification |
|-----------|---------------|
| **Purpose** | Test whether the narrative is simple enough to remember and repeat |
| **Method** | Deliver the narrative to 5 people from the target audience. Wait 24 hours. Ask each to explain the story in their own words. |
| **Pass** | 4+ of 5 can reproduce the *structural argument* (not word-for-word) -- they get the tension, the shift, and your role |
| **Fail** | <3 of 5 can reproduce the core argument; they remember details but not the arc |
| **Diagnosis on fail** | Narrative has too many claims, no clear through-line, or no memorable "hook" at the disruption point |
| **Fix** | Reduce to 3 claims max. Make the disruption the emotional peak. Create a one-sentence version of the entire arc. |

**Test 2: The "So What" Test (Actionability)**

| Parameter | Specification |
|-----------|---------------|
| **Purpose** | Test whether the narrative drives specific action, not just agreement |
| **Method** | After delivering the narrative, ask: "Based on what I just told you, what should you do next?" |
| **Pass** | Audience names a specific action aligned with your intended call to action |
| **Fail** | Audience says "interesting" or "I agree" but cannot name an action, or names the wrong action |
| **Diagnosis on fail** | The bridge from Proof to Call to Action is broken. The narrative convinces but doesn't convert. |
| **Fix** | Strengthen the Call to Action: make it specific, immediate, and low-friction. Connect it explicitly to the proof: "Given that [proof], the next step is [action]." |

**Test 3: The "Why Should I Care" Test (Resonance)**

| Parameter | Specification |
|-----------|---------------|
| **Purpose** | Test whether the Status Quo resonates -- whether the audience feels the tension |
| **Method** | Deliver the narrative to someone *adjacent* to the target audience (knows the domain but isn't the buyer). Ask: "Why would [target audience] care about this?" |
| **Pass** | Adjacent person can articulate the target audience's motivation correctly |
| **Fail** | Adjacent person cannot explain why the target would care, or explains a different motivation |
| **Diagnosis on fail** | The Status Quo is framed in insider language, or addresses a tension the narrator feels but the audience doesn't |
| **Fix** | Rewrite the Status Quo from the audience's perspective. Interview 3 target audience members: "What is the most frustrating thing about [domain]?" Use their language, not yours. |

**Test 4: The "What Would Change Your Mind" Test (Defensibility)**

| Parameter | Specification |
|-----------|---------------|
| **Purpose** | Test whether the narrative is falsifiable and whether it's currently false |
| **Method** | Ask a friendly skeptic: "What evidence would make you disbelieve this story?" |
| **Pass** | Skeptic names specific, falsifiable conditions that are NOT currently true |
| **Fail** | Skeptic names conditions that ARE currently true -- the narrative contains a falsified claim |
| **Diagnosis on fail** | A core claim in the narrative is already disproven or actively contested with strong counter-evidence |
| **Fix** | Remove or reframe the falsified claim immediately. A narrative built on a falsified claim is worse than no narrative -- it destroys credibility when exposed. |

**Test 5: The "Borrowed Story" Test (Differentiation)**

| Parameter | Specification |
|-----------|---------------|
| **Purpose** | Test whether the narrative is uniquely yours or could belong to any competitor |
| **Method** | Replace your company/product name with a competitor's name. Read the narrative aloud. |
| **Pass** | The narrative breaks -- it depends on YOUR specific attributes, evidence, and positioning that competitors don't have |
| **Fail** | The narrative works equally well with a competitor's name substituted |
| **Diagnosis on fail** | The narrative is generic -- it describes a category truth rather than a company truth. Your Role section lacks unique attributes. |
| **Fix** | Return to Positioning (F2). Identify 2+ attributes that are genuinely unique. Rewrite Your Role around those specific attributes. If nothing is unique, the problem is the product, not the narrative. |

**Composite Scoring and Decision Rules:**

| Total Score (5 tests, 1-5 each) | Assessment | Decision |
|:---:|---|---|
| 20-25 | Narrative is field-ready | Deploy across all audiences. Monitor with Watch indicators. |
| 15-19 | Narrative needs targeted fixes | Address failing tests before external deployment. Internal use acceptable. |
| 10-14 | Narrative has structural issues | Do not deploy. Return to Framework 1 (Narrative Arc) and rebuild. |
| <10 | Narrative is not viable | The issue is likely upstream -- product positioning, competitive differentiation, or "why now" is missing. Fix the strategy, then build the narrative. |

---

## Evidence Standards

### Evidence Quality Tiers (Narrative-Adapted)

| Tier | Source Type | Weight in Narrative | When to Use | Example |
|------|-----------|---------------------|-------------|---------|
| **T1** | Quantitative proof: revenue data, usage metrics, market share, SEC filings | Highest -- anchor claims that skeptics will challenge | Proof section, Your Role section, any customer-facing claim | "62% reduction in audit prep time (n=340 customers, Jan 2026)" |
| **T2** | Customer evidence: testimonials, case studies with measurable outcomes | High -- creates emotional resonance + credibility | Proof section, Customer audience variant, objection pre-emption | "Acme Corp reduced compliance prep from 6 weeks to 3 days" |
| **T3** | Third-party validation: analyst reports, press coverage, awards, expert endorsements | Medium-High -- useful for external credibility, especially with press/analyst audiences | Press variant, board variant (market sizing), "Why Now" section | "Gartner recognizes compliance automation as a top-3 priority for CISOs in 2026" |
| **T4** | Logical argument: well-structured reasoning from accepted premises | Medium -- useful for "New Reality" and structural arguments; insufficient alone for claims | New Reality section, internal alignment narrative, "Why Now" structural reasoning | "If audit requirements compound 20% annually and team sizes are flat, automation becomes inevitable" |
| **T5** | Analogies and precedents: "this worked for X, so it should work here" | Low-Medium -- useful for framing but not for proving; audiences vary in how they trust analogies | Status Quo framing, board presentations, internal motivation | "What Salesforce did for CRM, compliance automation does for security" |
| **T6** | Vision/assertion: claims about the future without supporting data | Low -- acceptable in New Reality section; never acceptable for claims about current state | New Reality section only; clearly labeled as vision | "By 2028, manual compliance will be as rare as manual bookkeeping" |

**Narrative Evidence Rules:**

1. **The Proof section requires T1-T2 exclusively.** T3 is acceptable as supplementary. T4-T6 are not proof; they are argument.
2. **External-facing narratives require at least 3 T1-T2 evidence points.** Internal narratives can function with T3-T4 supplemented by structural reasoning.
3. **Every audience variant must include at least one evidence point from the tier THAT audience trusts most** (see Audience Decision Table in F4).
4. **Analogies (T5) are powerful openers but dangerous closers.** Use them to frame, not to prove. A narrative that ends with an analogy instead of data leaves the audience with borrowed conviction, not their own.
5. **Vision (T6) must be labeled.** When the narrative shifts from evidence-backed claims to vision, signal the transition explicitly: "Here's what we see coming..." This prevents the audience from confusing your prediction with your proof.

**Triangulation Rule:** No narrative claim that a skeptic would challenge should rest on a single evidence tier. Minimum 2 tiers, ideally 3. Example: T1 (usage data) + T2 (customer testimonial) + T3 (analyst validation) = triangulated claim.

**Staleness Rule:** Market narratives decay. For every evidence point, note the source date. If no source newer than 6 months supports a claim, flag as `[POTENTIALLY STALE]`.

---

## Application Method

### Step 0b: Route to Framework Subset

After passing the Context Fitness Check, identify the narrative type and select load-bearing frameworks. Applying all 8 frameworks to every narrative inflates length, buries signal, and applies wrong-context frameworks.

| Narrative Type | Prompt Signals | Primary Frameworks | Frameworks to Skip |
|---|---|---|---|
| **Product launch positioning** | "position this product", "launch narrative", "how do we talk about this" | F1 (Narrative Arc), F2 (Positioning), F3 (Why Now), F4 (Audience Adaptation) | F7 (Competitive Narrative): skip if no direct competitor narrative exists |
| **Board / investor pitch** | "board deck", "investor narrative", "fundraising story" | F1 (Narrative Arc), F3 (Why Now), F5 (Evidence-Narrative Integration), F6 (Objection Anticipation) | F4 (Audience Adaptation): only one audience -- board. F7 (Competitive Narrative): include only if board will benchmark against specific competitors |
| **Competitive repositioning** | "we're losing to X", "reposition against", "competitive narrative" | F2 (Positioning), F7 (Competitive Narrative Analysis), F6 (Objection Anticipation), F4 (Audience Adaptation) | F3 (Why Now): skip unless timing has changed |
| **Internal alignment** | "get the team aligned", "internal narrative", "why we're doing this" | F1 (Narrative Arc), F3 (Why Now), F6 (Objection Anticipation) | F2 (Positioning): only relevant if internal team doesn't understand external positioning. F7 (Competitive Narrative): only if internal alignment problem is about competitive response |
| **Full strategic narrative** | "complete narrative", "end-to-end positioning", "narrative system" | All 8 -- tier explicitly: 4 primary, rest supporting | None -- but label tiers |
| **Press / analyst narrative** | "analyst briefing", "press narrative", "launch story for media" | F1 (Narrative Arc), F5 (Evidence-Narrative Integration), F8 (Narrative Testing), F4 (Audience Adaptation) | F6 (Objection Anticipation): journalists don't object the same way stakeholders do; replace with "question anticipation" |

Apply primary frameworks fully. Apply supporting frameworks at reduced depth unless they surface a conflicting signal -- in which case surface the contradiction explicitly.

### Quick Version (8 steps for experienced practitioners)

0a. **Context Fitness Check** -- Verify a Strategic Narrative Document is the right artifact. Check: do you have a product/strategy to narrate? Do you have competitive context? Is this external or internal?
0b. **Route to framework subset** -- Identify narrative type from the table above. Select 3-5 primary frameworks. Note which to skip.
1. **Construct the Narrative Arc** -- Build the six-element spine: Status Quo -> Disruption -> New Reality -> Your Role -> Proof -> Call to Action. Score each element 1-5.
2. **Define Positioning** -- Competitive alternatives, unique attributes, value delivered, target customer, market category decision (create/enter/reframe).
3. **Build the "Why Now"** -- Identify 2-4 structural preconditions. Score each. Compute composite. If <11, de-emphasize timing.
4. **Adapt for audiences** -- Produce variants for each target audience using the Audience Adaptation Matrix. Verify with the Adaptation Quality Check.
5. **Integrate evidence** -- Map C-E-I chains for every substantive claim. Check evidence density by section. Flag anti-patterns.
6. **Anticipate objections** -- Steelman the top 3-5 objections. Score by probability, severity, difficulty. Pre-embed critical-tier responses in the narrative.
7. **Analyze competitive narratives** -- Reverse-engineer competitor stories. Score their narrative strength. Identify gaps to exploit and collision points to win.
8. **Test the narrative** -- Run all 5 tests from the Testing Protocol. Score. If <15, iterate before deployment.

### Full Version (detailed steps with decision points)

**Step 1: Construct the Narrative Arc**

1. Start with the audience. Before writing any narrative element, answer: "What tension does THIS audience already feel?" Write the Status Quo in their language, not yours.
2. The Disruption must be a structural shift -- not your product, not your feature, not your technology. Ask: "What changed in the world that makes the old way untenable?" If the answer is "we built a product," you don't have a disruption.
3. The New Reality must feel inevitable -- with or without your product. Test: "Would this future arrive even if our company didn't exist?" If yes, the New Reality is genuinely structural. If no, it's a product pitch dressed as vision.
4. Your Role positions the product as the *best bridge* from Status Quo to New Reality. Not the only bridge. Not a magical solution. The best path for this specific customer.
5. Proof must be current, specific, and from the evidence tier the audience trusts (see F4 Audience Decision Table).
6. Score every element using the per-element rubric. If any element scores <3, fix it before proceeding.

**Quality checkpoint:** Read the arc aloud. Does it flow as a single story? If you feel the need to say "and another thing" between elements, the arc has broken connections.

**Step 2: Define Positioning**

1. List ALL competitive alternatives -- not just products, but behaviors: manual processes, spreadsheets, "do nothing," hiring consultants. Include at least one non-product alternative.
2. For each alternative, identify why customers switch away. This reveals the *real* buying criteria.
3. List your unique attributes. For each, apply the "so what" test: if the customer doesn't care, it's not a positioning asset.
4. State the value in customer language. Not "increases efficiency" but "saves your compliance team 15 hours per week."
5. Define target customer with enough specificity that a sales team could identify them without asking you.
6. Make the category decision using the Category Decision Table. This is the highest-leverage positioning choice -- get it right.

**Quality checkpoint:** Read the positioning statement to someone who doesn't know your product. Do they understand what you do, for whom, and why you're different? If they say "so it's like [wrong thing]?" your category choice is wrong.

**Step 3: Build the "Why Now"**

1. For each of the four precondition types (technology, market, regulatory, behavioral), identify whether a relevant shift has occurred.
2. Score each applicable precondition using the scoring criteria.
3. Compute the composite score.
4. Run the Timing Trap Detector on every precondition. If any trap is triggered, downgrade the score.
5. Run the "Not Too Early, Not Too Late" test.

**Quality checkpoint:** If your composite "Why Now" score is <11, do NOT force timing into the narrative. A weak "why now" is worse than no "why now" -- it invites the objection "you could have done this 5 years ago."

**Step 4: Adapt for Audiences**

1. State the core narrative (invariant text) -- 2-3 sentences that appear in every variant.
2. For each target audience, complete the Audience Adaptation Matrix row.
3. Write the full variant for each audience.
4. Run the Adaptation Quality Check on each variant.

**Quality checkpoint:** Read the board variant to an engineer. Do they say "this isn't for me"? Good -- it shouldn't be. If every variant sounds the same, you haven't adapted; you've copied.

**Step 5: Integrate Evidence**

1. Map every substantive claim to its evidence using C-E-I chains.
2. Assess evidence density per narrative section.
3. Check for anti-patterns (data dump, narrative without data, evidence-claim mismatch).
4. Flag any section where >50% of claims rest on T5-T6 evidence.

**Quality checkpoint:** Could a skeptic dismantle any section in 60 seconds? If yes, that section needs stronger evidence.

**Step 6: Anticipate Objections**

1. List 3-5 objections, steelmanned.
2. Score each using the Objection Scoring Matrix.
3. For critical-tier objections (score 7-9), select a pre-embedding technique and write the response into the narrative arc.
4. For important-tier objections (score 4-6), prepare standalone responses for Q&A.

**Quality checkpoint:** Read each steelmanned objection to a teammate. Does it make them uncomfortable? Good -- that means it's genuinely strong. If they shrug, you're not steelmanning hard enough.

**Step 7: Analyze Competitive Narratives (if applicable)**

1. For each significant competitor, run the Narrative Reverse-Engineering Method.
2. Score their narrative strength on 5 dimensions.
3. Identify gaps to exploit using the Gap Exploitation Decision Table.
4. Identify collision points -- claims where your narrative directly contradicts theirs.

**Quality checkpoint:** Can you state each competitor's narrative arc as compellingly as your own? If not, you haven't understood their story well enough to beat it.

**Step 8: Test the Narrative**

1. Run all 5 tests from the Narrative Testing Protocol.
2. Score each test 1-5.
3. Compute the total.
4. If <15, address failing tests before external deployment.
5. If <10, return to Step 1 and rebuild.

**Quality checkpoint:** The narrative is ready when it passes all 5 tests AND you can deliver it in 2 minutes without notes. If you need notes, the arc isn't clear enough.

---

## Mandatory Output Sections

These sections must appear in every output from this skill, regardless of narrative type. They are quality assurance mechanisms, not optional extras.

### Assumption Registry

A standalone table of every load-bearing assumption underpinning the narrative:

| Assumption | Framework Underpinned | Confidence | Evidence | What Would Invalidate |
|---|---|---|---|---|

Minimum 3 assumptions. Common load-bearing assumptions for narratives:
- "The target audience feels the tension described in the Status Quo" -- must be validated with audience research; if the audience doesn't feel the tension, the narrative falls flat
- "Our unique attributes are genuinely unique and not replicable within 12 months" -- must be validated against competitor roadmaps; if a competitor ships the same capability, positioning collapses
- "The structural 'why now' preconditions will persist through the narrative's useful life" -- if a technology shift reverses or a regulation changes, the timing argument evaporates
- "The market category choice sets buying criteria where we win" -- if the audience maps us to a different category, we're compared on the wrong dimensions

Any L-confidence assumption must be `[EVIDENCE-LIMITED]`-flagged inline.

### Adversarial Self-Critique

A mandatory final step: *"Identify >=3 genuine weaknesses in this narrative."*

Format per weakness:
- What assumption is being made?
- What evidence would disprove it?
- What is the watch indicator?
- Is there a scenario where this narrative backfires? (e.g., competitor copies your positioning; "why now" precondition reverses; audience doesn't feel the stated tension)

**Critical:** This is not the same as listing failure modes -- failure modes are general patterns. Adversarial self-critique argues against *your specific narrative decisions* as forcefully as possible.

### Revision Triggers

When should this Strategic Narrative Document be revisited? Specific, observable conditions:
- Competitor launches a product that invalidates a unique attribute claim
- Market category shifts -- analyst reclassification, new entrant reframes the category
- "Why Now" precondition reverses or expires (regulation delayed, technology shift commoditized)
- Narrative testing scores drop below 15 in re-test (audiences no longer repeat it back)
- Customer evidence (T2) contradicts a core narrative claim
- Internal team can no longer deliver the narrative without notes (complexity creep)

---

## Quality Gradients

### Intern Tier
- Narrative is a feature list organized chronologically ("first we built X, then we built Y")
- No structural arc -- reads like a product update, not a story
- Positioning is vague ("we're the best solution for everyone")
- No audience adaptation -- same narrative for board, engineers, and customers
- Evidence is assertion-only (T5-T6): "we believe," "the market is shifting"
- No objection anticipation -- narrative collapses under first skeptical question
- No competitive narrative awareness -- narrative could belong to any company in the space
- Missing: "why now," structural tension, audience variants, evidence integration

### Consultant Tier
- Clear narrative arc: Status Quo -> Disruption -> New Reality -> Your Role -> Proof
- Positioning is specific: target customer identified, competitive alternatives listed, category chosen
- 2-3 audience variants with different emphasis
- Evidence is tiered -- T1-T3 for major claims, with evidence density tracked
- Top 3 objections anticipated with prepared responses
- "Why Now" is present and defensible, though may rely on T3-T4 evidence
- Competitive awareness: knows what competitors say, but doesn't systematically analyze their narrative structure
- Missing: narrative testing protocol, per-element scoring, pre-embedding techniques, competitive narrative gap exploitation, systematic evidence-claim mapping

### Elite Tier
- All 8 frameworks applied with scoring rubrics and decision tables
- Narrative arc scored per element with 25+ total; every element earning its structural place
- Positioning tested against Category Decision Table; unique attributes verified as genuinely unique and defensible
- "Why Now" composite score >=16; each precondition independently verifiable with T1-T3 evidence
- Audience variants pass the Adaptation Quality Check -- each leads with what THAT audience cares about, uses proof types THAT audience trusts
- Evidence integrated via C-E-I chains for every claim; evidence density tracked per section; anti-patterns detected and corrected
- Objections steelmanned (not straw-manned), scored by probability/severity/difficulty, critical-tier pre-embedded in the narrative arc using specific techniques
- Competitive narratives reverse-engineered; strength scored on 5 dimensions; gaps exploited; collision points identified with evidence advantage assessment
- Narrative tested with all 5 tests, scoring >=20/25
- Produces a narrative system a PM cannot construct unaided -- this is the codex test

---

## Failure Modes

**FM-1: Feature Narrative**
*What it looks like:* The "narrative" is a chronological list of capabilities. "We built X. We also have Y. And Z is coming in Q3." No tension, no arc, no audience adaptation.
*Why it happens:* The narrator knows the product deeply and defaults to describing it rather than telling a story about the world that the product fits into. Features are concrete; narratives require abstraction.
*Detection:* Remove all product-specific content. Is there still a story? If removing your product removes the entire narrative, it's a feature list.
*Correction:* Start with Status Quo -- what tension exists in the audience's world BEFORE your product enters the picture? The story begins before you.

**FM-2: Missing the Antagonist**
*What it looks like:* The narrative is positive and aspirational but has no tension. "The world is changing! Things are getting better! We're part of it!" There is no disruption, no urgency, no reason to act NOW.
*Why it happens:* Narrators avoid negativity. They want the story to feel good. But stories without antagonists have no urgency. The antagonist is the Status Quo that must be overcome, the structural shift that makes inaction dangerous, or the competitor whose narrative you must displace.
*Detection:* After hearing the narrative, does the audience feel they MUST act, or merely that they COULD act? "Must" = urgency present. "Could" = antagonist missing.
*Correction:* Strengthen the Disruption element. Name the specific cost of inaction. Quantify what the audience loses by not acting. Make the Status Quo feel untenable, not just suboptimal.

**FM-3: "Why Us" Without "Why Now"**
*What it looks like:* Strong differentiation, clear positioning, compelling proof -- but no timing argument. The narrative could have been delivered 3 years ago or 3 years from now with equal validity.
*Why it happens:* The narrator focuses on what makes the product different (easier) rather than what makes this moment different (harder). Differentiation is product work; timing is market work.
*Detection:* Apply the "Not Too Early, Not Too Late" test from Framework 3. If the answer to "Could this have succeeded 3 years ago?" is "yes," the "why now" is missing.
*Correction:* Identify at least 2 structural preconditions (technology, market, regulatory, or behavioral shift) that are independently verifiable and have occurred within the last 24 months.

**FM-4: One-Audience Narrative**
*What it looks like:* The same narrative is delivered to the board, to engineers, to customers, and to press. It works for one audience and fails for the others. Board members hear technical details they don't care about. Engineers hear ROI projections that don't motivate them. Customers hear industry jargon that excludes them.
*Why it happens:* Building audience variants is 4x the work of building one narrative. The narrator optimizes for their most frequent audience and uses that version everywhere.
*Detection:* Read the narrative aloud and imagine each audience separately. Does any audience hear content designed for someone else? Does any audience miss content they need?
*Correction:* Apply Framework 4 (Audience Adaptation Matrix). Produce at least 3 variants. The core arc stays the same; the lead, proof type, objection pre-emption, and call to action change per audience.

**FM-5: Data Without Story**
*What it looks like:* The "narrative" is a well-organized evidence document. Charts, data points, benchmarks, comparisons -- but no story. The audience is informed but not moved. They know the facts but don't know what to feel about them.
*Why it happens:* The narrator has strong analytical skills and defaults to evidence presentation rather than story construction. Data feels more rigorous than narrative. But data without story is a report, not a narrative.
*Detection:* Remove all data. Is there a story left? If yes, the data supports the story (good). If no, the data IS the story (bad -- it's a report).
*Correction:* Build the Narrative Arc (F1) FIRST -- before any data. Then integrate evidence using the C-E-I pattern (F5). Data serves the story; the story does not serve the data.

**FM-6: Story Without Data**
*What it looks like:* Compelling, emotionally resonant narrative that a skeptic can dismantle in 60 seconds. "Prove it" has no answer. The story feels right but cannot be defended.
*Why it happens:* The narrator has strong storytelling instincts but doesn't ground claims in evidence. The narrative is built on charisma, not proof.
*Detection:* For every claim in the arc, ask: "What would a skeptic say?" If the skeptic says "prove it" and you can't, the narrative has an evidence gap.
*Correction:* Map every claim to evidence using C-E-I chains (F5). Any claim without at least T3 evidence must be weakened, removed, or flagged for evidence acquisition.

**FM-7: Borrowed Narrative**
*What it looks like:* Your narrative uses the same framing, the same "why now," the same category claim, and the same structural arc as a competitor. Replace your company name with theirs and nothing breaks. You're telling their story, not yours.
*Why it happens:* The narrator benchmarked against competitors (good) but then adopted their framing instead of creating their own (bad). Or the category leader has defined the narrative so successfully that everyone unconsciously tells their story.
*Detection:* Run the "Borrowed Story" test from Framework 8. If substituting a competitor's name doesn't break the narrative, it's borrowed.
*Correction:* Return to Positioning (F2). Identify the unique attributes that are genuinely yours. Rebuild the narrative around YOUR specific advantages. If nothing is unique, the problem is the product, not the narrative.

**FM-8: Right Narrative, Wrong Question**
*What it looks like:* A structurally excellent, well-evidenced, audience-adapted narrative -- for a product whose real problem isn't narrative. The product doesn't have a positioning problem; it has a product-market fit problem, a distribution problem, or an execution problem. The narrative is polished but irrelevant.
*Why it happens:* The skill is triggered by any narrative-sounding prompt ("help me position this") without checking whether a narrative is the right artifact. A product that customers don't want won't be saved by a better story.
*Detection:* Ask: "If the narrative were perfect and every audience believed it, would the product succeed?" If the answer is "no, because [non-narrative problem]," the narrative is solving the wrong problem.
*Correction:* Run the Context Fitness Check (Step 0) before Framework Selection. If the core problem is product-market fit, redirect to Discovery & Research. If the core problem is execution, redirect to Specification Writing. If the core problem is measurement, redirect to Metric Design & Experimentation.

**FM-9: Expert-Only Document**
*What it looks like:* Output is dense with framework names (Dunford Positioning, C-E-I Integration, Narrative Inoculation), notation (T1-T6, H/M/L, O->I->R->C->W), and jargon that assumes the reader built the analysis. A VP or comms lead cannot extract the narrative without a guided tour from the author.
*Why it happens:* The skill optimizes for analytical completeness, not reader comprehension. The author knows all the notation; the reader doesn't. No reading guide, no notation key, no layered depth.
*Detection:* Show the output to someone who didn't request it. If they need more than 60 seconds to find the actual narrative, or if they ask "what does T2 mean?", the document fails the reader test.
*Correction:* The output template mandates a "How to Read This Document" section and a Notation Key before the analysis begins. The Executive Narrative uses zero framework jargon -- plain language that a VP can use verbatim.

---

## What's Next

<- This skill works best after: **Competitive & Market Analysis** (competitive landscape informs positioning and competitive narrative analysis) and **Discovery & Research** (customer evidence provides T1-T2 proof for the narrative)
-> This skill's output feeds well into: **Specification Writing** (the narrative informs what to build and how to frame requirements), **Metric Design & Experimentation** (narrative claims become hypotheses to measure)
+ **Start here if:** You have a product, a strategy, or a decision -- and the story isn't landing. The fundamentals exist; the narrative doesn't.
For a full product cycle: Problem Framing -> Discovery & Research -> Competitive Analysis -> **[THIS SKILL]** -> Spec Writing -> Outcome Measurement

**Chain interface:**
- **Receives:** Competitive War Map with positioning choices (from Competitive & Market Analysis), customer evidence and voice-of-customer data (from Discovery & Research), or raw context (product description, market context, audience, and purpose)
- **Produces:** Strategic Narrative Document with narrative arc, positioning analysis, "why now" framework, audience-adapted variants, evidence-integrated claims, objection pre-responses, competitive narrative analysis, and testing protocol
- **Handoff artifact:** The Strategic Narrative Document's audience-adapted variants map directly to Spec Writing input (what to build, framed by narrative priorities) and Metric Design input (narrative claims become measurement hypotheses)

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness:

- [ ] Context Fitness Check passed: product/strategy exists to narrate, competitive context available, audience identified
- [ ] If no competitive context: flagged prominently in Executive Narrative; positioning claims marked as hypotheses
- [ ] How to Read This Document section present with role-based reading guide
- [ ] Notation Key present: H/M/L, T1-T6, O->I->R->C->W all explained
- [ ] Executive Narrative uses zero framework jargon -- plain language a VP can use verbatim
- [ ] Narrative Arc constructed with all 6 elements: Status Quo, Disruption, New Reality, Your Role, Proof, Call to Action
- [ ] Each arc element scored 1-5 with evidence tier; total >= 18 before proceeding
- [ ] Positioning analysis complete: competitive alternatives (including "do nothing"), unique attributes, value delivered, target customer, market category decision
- [ ] Category decision made using Category Decision Table (create/enter/reframe) with rationale
- [ ] "Why Now" analysis with 2+ structural preconditions scored; composite score computed
- [ ] If "Why Now" composite < 11: timing de-emphasized, not fabricated
- [ ] "Not Too Early, Not Too Late" test completed
- [ ] Timing Trap Detector run on each precondition
- [ ] Audience Adaptation Matrix completed for >= 3 audiences
- [ ] Each audience variant leads with what THAT audience cares about (not what the narrator cares about)
- [ ] Adaptation Quality Check passed for each variant
- [ ] Evidence integrated via Claim-Evidence-Implication chains for every substantive claim
- [ ] Evidence density assessed per narrative section; Proof section uses T1-T2 exclusively
- [ ] Anti-patterns checked: data dump, narrative without data, evidence-claim mismatch
- [ ] Top 3-5 objections steelmanned (not straw-manned)
- [ ] Objections scored by probability, severity, difficulty; critical-tier pre-embedded in narrative
- [ ] Competitive narratives reverse-engineered (if applicable): arc decoded, strength scored, gaps identified
- [ ] Narrative collision points identified with evidence advantage assessment
- [ ] Narrative Testing Protocol run: all 5 tests scored; total >= 15 before external deployment
- [ ] "Borrowed Story" test passed -- narrative breaks when competitor name is substituted
- [ ] Framework selection routing done (Step 0b) -- primary frameworks identified, irrelevant frameworks skipped
- [ ] Per-cell evidence tier annotation in ALL comparison matrices and claim tables
- [ ] O->I->R->C->W cascade applied to ALL narrative recommendations
- [ ] H/M/L confidence levels explicit on every narrative claim -- no weasel words
- [ ] Time-sensitive claims flagged `[POTENTIALLY STALE]` if source > 6 months old
- [ ] `[EVIDENCE-LIMITED]` flag applied to any key narrative claim resting only on T4-T6 evidence
- [ ] Assumption Registry present with >= 3 load-bearing assumptions
- [ ] Adversarial Self-Critique section present with >= 3 genuine weaknesses in THIS specific narrative
- [ ] Cross-framework contradictions surfaced explicitly (not resolved artificially)
- [ ] Revision Triggers defined with specific, observable conditions
