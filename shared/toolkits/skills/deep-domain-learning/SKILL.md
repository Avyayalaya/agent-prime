---
name: deep-domain-learning
description: "Use when building deep understanding of a new domain, producing a world model document, preparing for expert-level conversations, or needing to reason from first principles in an unfamiliar field. Encodes the Why-Chain Mandate, Quantification Mandate, Evidence Discipline, Grounding Requirement, and Narrative Flow frameworks. Produces a World Model document."
version: "1.0.0"
type: "codex"
tags: ["Context Engineering", "Evaluation", "Meta"]
created: "2026-02-25"
valid_until: "2026-08-25"
derived_from: "Projects/AI_Learning and Mastery/World_Model_Builder_v2.1_FINAL.md"
tested_with: ["Claude Opus 4", "Claude Sonnet 4.5"]
license: "MIT"
---

## Purpose

Produce a deep, mechanistic **World Model** of any domain — a structured narrative document that enables the reader to predict, explain, diagnose, design, and feel the inevitability of outcomes in that domain. The output is not a summary or survey; it is a first-principles construction that traces every mechanism to bedrock.

## When to Use / When NOT to Use

**Use this skill when:**
- Learning a new domain deeply enough to reason from first principles (not just recall facts)
- Preparing for expert-level conversations, keynotes, or advisory work in an unfamiliar field
- Building the conceptual foundation for a thesis, investment analysis, or product strategy
- An agent needs domain context before producing high-quality synthesis or analysis
- You need to identify where your intuitions about a domain are wrong

**Do NOT use this skill when:**
- You need a quick overview or executive summary (ask directly — this produces 10K-30K words)
- The domain is already well-understood by the reader (use Research Synthesis skill instead)
- You need tactical how-to instructions, not conceptual understanding (use a tutorial)
- The topic is narrow enough for a single Q&A exchange
- You need current news or market data (this produces timeless mechanistic understanding, not current events)

**Anti-inputs (what this skill does NOT handle):**
- Competitive analysis or market sizing (→ Competitive & Market Analysis skill)
- Specification of what to build (→ Specification Writing skill)
- Synthesis of multiple existing research papers (→ Research Synthesis skill)
- Opinion formation or thesis construction (→ Synthesizer agent)

---

## Format Rules (Read First)

These rules govern every World Model document. They are not style preferences — they are quality enforcement mechanisms derived from iterative testing of domain learning outputs.

1. **Dense explanatory prose, not bullet lists.** Bullet lists are permitted ONLY for enumeration after narrative explanation. The primary content is flowing paragraphs that build understanding incrementally. A World Model that reads like a slide deck has failed.

2. **Every non-trivial claim carries an inline citation.** Format: `(Author, Year)` or `[Description, Date]`. Uncited claims must be explicitly marked as the author's reasoning or common knowledge. A World Model with naked claims is opinion, not knowledge.

3. **Every abstraction is grounded in concrete reality.** No concept is introduced without at least one observable, measurable, or experimentally demonstrated example. If you can't point to something in the physical world, the abstraction is floating.

4. **Every quantitative claim includes actual numbers with units and context.** Never say "large," "significant," "fast," or "expensive" without numbers. Contextualize numbers with comparisons, scaling relationships, and practical implications.

5. **Epistemic status is marked explicitly on every substantive claim.** Use the five-tier system: PROVEN, CONFIRMED, CONSENSUS, DEBATED, SPECULATIVE. When uncertain: UNCERTAIN with reason. A reader must know how much weight to put on each claim.

6. **Write in flowing paragraphs that build understanding.** Each paragraph makes the reader want to read the next. Structure each concept as: Hook → Build from familiar → Reveal mechanism → Make precise → Show it's real → Connect → Test intuition.

7. **Mathematics is embedded naturally with full intuitive explanation.** Every equation or formal relationship gets: (a) the formula, (b) what each variable means in plain language, (c) why the relationship has this shape, (d) what changes when you change each variable. Math without intuition is decoration.

8. **The Opening is written LAST but placed FIRST.** Only after the full document is written can you distill the essence accurately.

---

## Output Template (Mandatory Document Skeleton)

Every World Model MUST follow this structure. Do not reorder sections, skip sections, or invent new top-level sections. Adjust page lengths based on the LENGTH parameter.

```markdown
# Understanding [DOMAIN]: A World Model

> **Date:** [YYYY-MM-DD] | **Depth:** [Conversational / Practitioner / Expert / Frontier] | **Length:** [Focused / Comprehensive / Exhaustive]

---

## The Opening (2-4 pages)
- The core insight that changes everything
- Why this matters to your world model
- The conceptual landscape and journey ahead
- Where your intuition misleads you
- The best analogy (and where it breaks)

## Part I: Bedrock — What Cannot Be Otherwise
[3-5 fundamental constraints, 5-8 essential concepts]

For each constraint:
- State it and why it's inescapable — trace to deeper principle
- Quantify it with real numbers and context
- Show what would break if it weren't true — thought experiment
- Historical attempts to circumvent it and what happened
- How it shapes everything built above — trace consequences upward
- Observable manifestations in real systems

For each concept:
- Why this concept exists — historical problem it solved
- Build it from primitives — construction or measurement
- Precise definition with math, fully explained
- Why this definition and not plausible alternatives
- The mechanism behind it at micro-level
- How to develop intuition — analogies with limitations stated
- Where intuition fails — common misconceptions with corrections
- Observable signatures — how to recognize it in practice
- Deep connections to other concepts

## Part II: The Machinery — How It Actually Works
[2-3 central processes, 3-5 major interactions]

For each process — complete walkthrough:
- Initial state with specific numbers
- Triggering event
- Each step of transformation — mechanism at micro-level, timescale, energy flows
- Parallel or dependent processes — timing and ordering constraints
- The bottleneck — rate-limiting step, why it's slowest
- Feedback loops — what feeds back where, dynamics, equilibrium
- Completion and efficiency — total time, input/output, losses quantified
- Observable in real systems — examples with data and citations

For each interaction:
- Which processes/components interact and why
- Mechanism of interaction — step-by-step with numbers
- Nonlinearities or threshold effects
- Real examples demonstrating the interaction

## Part III: What Emerges — Seeing the Whole
[2-4 emergent phenomena]

For each phenomenon:
- What you observe at system level
- Why it emerges — trace from micro-interactions to macro-behavior
- Mathematical form and what the structure tells us
- Necessary conditions for emergence
- Inevitability — why it's forced by constraints, not accidental
- Observable signatures and measurements
- Robustness — how it responds to perturbations
- Cross-domain connections — where this pattern appears elsewhere

## Part IV: The Human Reality — Context and Consequences
[3-5 major misconceptions, incentive landscapes, decision-making under uncertainty]

For each misconception:
- Why people believe this — superficial logic
- Why it's wrong — show the mechanism they're missing
- Concrete evidence or thought experiment proving it wrong
- The correct intuition — revised mental model
- Historical example of this mistake and consequences

Then:
- Incentive landscapes (stakeholder motivations, misalignments)
- Decision-making under uncertainty (epistemic status of key claims)
- Real-world implications and tradeoffs

## Part V: The Synthesis — Your Updated World Model
- Core framework unified
- Before/after mental models
- Mental simulation test: can you predict, explain, diagnose, design, and feel inevitability?
- Cross-domain transferable insights

## Part VI: Going Deeper — Your Path Forward
- Next topics to explore with specific resources
- Progressive exercises (week 1, month 2-3)
- Signposts to watch for model updates
- Meta-lessons about learning this domain

## References
[All sources cited inline throughout, compiled here]
```

---

## Domain Frameworks

> These five frameworks are the intellectual core of this codex. Each encodes a specific discipline that separates deep understanding from surface knowledge. A World Model produced without these frameworks reads like a Wikipedia article; with them, it reads like a masterful textbook chapter.

### Framework 1: The Why-Chain Mandate

**Definition:** For every key mechanism or concept, recursively ask "why?" until hitting one of three bedrock types: (a) fundamental physical law (e.g., conservation of energy), (b) mathematical axiom (e.g., chain rule), (c) empirical brute fact (e.g., measured physical constant).

**Scoring Rubric — Depth of Explanation:**

| Depth | Name | Test | Rating |
|-------|------|------|--------|
| D0 | Label | Names the concept without explaining it | 🔴 Unacceptable |
| D1 | Description | Says what the concept does, not why | 🔴 Unacceptable |
| D2 | Mechanism | Explains how it works at one level | 🟡 Insufficient |
| D3 | Causal chain | Traces 2-3 "why" levels with connections | 🟡 Minimum bar |
| D4 | Bedrock trace | Hits fundamental law, axiom, or brute fact | 🟢 Target |
| D5 | Bedrock + alternatives | D4 plus explains why alternatives don't work | 🟢 Elite |

**Decision Rule:** Every core concept in Parts I-III must reach D4. Supporting concepts may be D3. No concept below D2 appears in the final document.

**Application Example:**

- ❌ D1: "Transformers use attention mechanisms to process sequences efficiently."
- ✅ D4: "Attention computes all position-to-position interactions in parallel via matrix multiplication. An RNN must pass information through n-1 intermediate hidden states — a serial dependency chain of O(n·t). Transformers compute QK^T (n×n) in a single matrix multiply, yielding O(n²d) FLOPs but O(1) depth. The dot product q·k = Σ q_i·k_i serves as a differentiable content-based addressing mechanism — maximal when vectors align, minimal when orthogonal. This is identical to the retrieval mechanism in Hopfield networks (1982). The tradeoff: O(n²) memory for O(1) depth. For GPT-3 with context length 2048, that's 4M scores per layer — costly but parallelizable. An LSTM would need 2048 sequential steps. This is why transformers scaled to 100B+ parameters while RNNs topped out at ~200M. (Vaswani et al., 2017; Kaplan et al., 2020)"

---

### Framework 2: The Quantification Mandate

**Definition:** Every quantitative claim must include actual numbers with units, contextual comparisons, scaling relationships, error bars or ranges, and practical interpretation.

**Scoring Rubric — Quantitative Rigor:**

| Level | Name | Test | Rating |
|-------|------|------|--------|
| Q0 | Adjective | "Large," "significant," "fast" — no numbers | 🔴 Unacceptable |
| Q1 | Bare number | A number without context or units | 🔴 Unacceptable |
| Q2 | Number + units | Number with proper units | 🟡 Minimum |
| Q3 | Contextualized | Number + comparison to familiar reference | 🟢 Adequate |
| Q4 | Full quantification | Number + units + comparison + scaling relationship + practical meaning | 🟢 Target |

**Decision Rule:** Core claims must reach Q3. Key mechanisms must reach Q4. No Q0 or Q1 survives in the final document.

**Application Example:**

- ❌ Q0: "Training large models requires significant compute."
- ✅ Q4: "Training GPT-3 (175B parameters) required ~3640 petaflop-days on V100 GPUs, costing ~$4.6M at 2020 cloud pricing (~$3/hr/GPU, ~3000 GPUs, ~1 month). This is 100,000× more compute than GPT-2 (1.5B, ~40 petaflop-days). The scaling follows C ∝ N^1.0 for data-rich training (Kaplan et al., 2020)."

---

### Framework 3: The Evidence Discipline

**Definition:** Every substantive claim is tagged with its epistemic status — how we know what we claim to know.

**Evidence Tier Classification:**

| Status | Definition | Signature | Example |
|--------|-----------|-----------|---------|
| **PROVEN** | Mathematically derived from axioms | Cannot be otherwise | "The gradient of f(g(x)) is f'(g(x))·g'(x) by the chain rule" |
| **CONFIRMED** | Experimentally measured and replicated | Independent replication exists | "Electron charge is 1.602176634×10⁻¹⁹ C (CODATA 2018, uncertainty <1ppb)" |
| **CONSENSUS** | Widely accepted by domain experts, not formally proven | Practitioner experience + limited theory | "Adam typically converges faster than SGD for deep learning (Kingma & Ba, 2014)" |
| **DEBATED** | Experts disagree; show both sides | Active research conflict | "Whether scaling laws continue beyond 10¹² parameters — optimists cite smooth trends, skeptics note phase transitions" |
| **SPECULATIVE** | Plausible but unconfirmed | Structural similarity without direct evidence | "Attention might implement biological working memory — structural similarity to hippocampal indexing, but direct evidence lacking" |
| **UNCERTAIN** | Conflicting evidence or insufficient data | State the reason | "Conflicting measurements — see Smith 2020 vs Jones 2021" |

**Decision Rule:** Every claim in Parts I-III carries an explicit epistemic tag. Part IV discusses epistemic status as a theme. Claims without tags are treated as SPECULATIVE by default.

---

### Framework 4: The Grounding Requirement

**Definition:** Every abstract concept must be anchored to concrete, observable, measurable reality. No floating abstractions.

**Grounding Checklist (apply to every core concept):**

| Element | Question | Required? |
|---------|----------|-----------|
| Concrete example | Can I point to this in the physical world? | Yes — for every concept |
| Numbers | Can I measure it? What are the values? | Yes — at least one measurement |
| Observable phenomenon | What would I see if I watched this happen? | Yes — real or thought experiment |
| Historical grounding | When was this first observed/discovered? By whom? | Recommended |
| Modern confirmation | How do we measure/verify this today? | Recommended |

**Application Example — "Entropy":**

- ❌ Ungrounded: "Entropy is a measure of disorder."
- ✅ Grounded: "Take 100 coins. The macrostate 'all heads' has 1 microstate. The macrostate '50 heads, 50 tails' has ~10²⁹ microstates. S = k ln(Ω), so S_all-heads = 0 while S_50-50 ≈ 67k. Systems evolve toward 50-50 because 10²⁹:1 odds. Observable: food coloring spreads in water — never spontaneously un-mixes. Confirmed: Boltzmann 1898, Einstein 1905, modern measurements Bustamante et al., 2005."

---

### Framework 5: Narrative Flow Architecture

**Definition:** A prescribed structure for introducing each concept or mechanism that builds understanding incrementally. Not a template to fill — a cognitive sequence to follow.

**The Seven-Step Concept Introduction:**

| Step | Name | Purpose | Example (for "attention mechanism") |
|------|------|---------|--------------------------------------|
| 1 | **Hook** | Why this matters or what puzzle it solves | "How do you let a model look at any part of a sequence at any time?" |
| 2 | **Build from familiar** | Start with intuition | "When you read a sentence, your eyes don't process each word in strict order..." |
| 3 | **Reveal the mechanism** | Step-by-step causal chain | "Query, key, and value vectors computed from the input..." |
| 4 | **Make it precise** | Math or formal definition, fully explained | "QK^T/√d_k followed by softmax..." |
| 5 | **Show it's real** | Observable examples, experiments, measurements | "Attention weight visualizations show heads specializing..." |
| 6 | **Connect it** | How it relates to other concepts | "This is differentiable Hopfield retrieval..." |
| 7 | **Test intuition** | What would happen if it were different? | "Without the √d_k normalization, dot products grow with dimension..." |

**Decision Rule:** Core concepts in Part I must follow all 7 steps. Supporting concepts may abbreviate to steps 1, 3, 4, 5. No concept skips steps 1 and 3.

---

## Application Method

### Quick Version

1. Collect the caller's domain, current state, depth target, key questions, bridge domains, and length preference.
2. Research deeply — prioritize Tier 1 (papers, textbooks, primary data) over Tier 2 (documentation, case studies) over Tier 3 (secondary sources).
3. Identify 3-5 bedrock constraints and 5-8 essential concepts for Part I.
4. Map 2-3 central processes and 3-5 interactions for Part II.
5. Write Parts I-V applying all five frameworks: Why-Chain to D4+, Quantification to Q3+, Evidence tags on every claim, Grounding for every abstraction, Narrative Flow for every concept.
6. Write Part VI (Going Deeper) and the Opening (written last, placed first).
7. Run the Final Verification checklist.

### Full Version

**Step 1: Intake and Calibration**

Collect from the caller:
- **DOMAIN** — specific enough to scope (e.g., "transformer attention mechanisms" not "AI")
- **CURRENT STATE** — what they know, what confuses them, intuitions that might be wrong
- **DEPTH TARGET** — one of four levels:

| Level | Output Calibration | Reader Outcome |
|-------|-------------------|----------------|
| Conversational fluency | Explain to others, recognize in practice | Can hold their own in a discussion |
| Working practitioner | Implement, modify, debug intelligently | Can build with this knowledge |
| Deep expert | Design novel variations, see deep implications | Can innovate in this domain |
| Research frontier | Contribute new insights, push boundaries | Can advance the field |

- **KEY QUESTIONS** — specific questions the document must answer
- **BRIDGE DOMAINS** — domains the caller already understands deeply (for cross-domain analogies)
- **LENGTH** — Focused (10-15K words), Comprehensive (20-30K, default), Exhaustive (30K+)

**Quality checkpoint:** If the domain is too broad (e.g., "biology"), push back and ask for scoping. If depth target is mismatched with length (e.g., "research frontier" + "focused"), flag the tension.

**Step 2: Research Phase**

Before writing, build a source inventory:
- **Tier 1 (strongest):** Peer-reviewed papers, textbooks, primary experimental data, fundamental equations
- **Tier 2:** Technical documentation, expert practitioner accounts, well-documented case studies
- **Tier 3:** Reputable secondary sources with clear methodology

Decision point: If Tier 1 sources are unavailable for a key mechanism, flag it with DEBATED or SPECULATIVE status in the output. Never fill gaps with Tier 3 and present as CONFIRMED.

**Step 3: Structural Planning**

Before prose, outline:
- The 3-5 bedrock constraints (what cannot be otherwise in this domain)
- The 5-8 essential concepts (what you must understand to reason in this domain)
- The 2-3 central processes (how the domain's machinery actually works)
- The 3-5 interactions between processes
- The 2-4 emergent phenomena (what arises that isn't obvious from components)
- The 3-5 major misconceptions (where intuition fails)

Decision point: If you can't identify at least 3 bedrock constraints, the domain scoping is too narrow or too abstract. Adjust.

**Step 4: Writing — Parts I through III**

Apply all five frameworks simultaneously:
- **Why-Chain:** Every core concept traced to D4 (bedrock)
- **Quantification:** Every quantitative claim at Q3+ (contextualized numbers)
- **Evidence:** Every substantive claim tagged with epistemic status
- **Grounding:** Every abstraction anchored to observable reality
- **Narrative Flow:** Every core concept follows the 7-step sequence

Quality checkpoint per section: Read back each Part. For every paragraph, ask: "Could a smart person who read only this paragraph and nothing else learn something precise and grounded?" If the answer is no, the paragraph is filler — cut or rewrite.

**Step 5: Writing — Parts IV through VI**

Part IV shifts from mechanism to human context — where intuitions fail, how incentives distort understanding, what decisions the reader faces. Evidence tags become the theme, not just annotations.

Part VI must be genuinely useful — specific resources (not "read more about X"), concrete exercises with timelines, and meta-lessons the reader can apply to learning other domains.

**Step 6: The Opening**

Written LAST. Distill the 3-5 most important insights from the completed document. Set up the conceptual journey. Include the single best analogy for the domain and explicitly state where that analogy breaks.

**Step 7: Final Verification**

Run through every item in the Appendix Checklist below. Fix any gaps before delivering.

---

## Quality Gradients

### Intern Tier
- Accurate factual content but reads like a rearranged Wikipedia article
- Bullet-list heavy; concepts named but not derived
- Numbers present but not contextualized ("175 billion parameters")
- No epistemic status marking — all claims presented with equal confidence
- Analogies are surface-level ("attention is like a spotlight")
- Missing the Why-Chain — concepts explained at D1-D2 only
- Reader can recall facts but cannot reason from first principles

### Consultant Tier
- Well-structured narrative with clear sections
- Some mechanisms traced through 2-3 levels (D3)
- Numbers contextualized with some comparisons
- Citations present but inconsistent
- Some epistemic marking but not systematic
- Analogies are functional but limitations not stated
- Reader can explain the domain to others but cannot predict novel outcomes

### Elite Tier
- Dense narrative prose that builds understanding paragraph by paragraph
- Every core mechanism traced to bedrock (D4-D5)
- Full quantification: numbers + units + comparisons + scaling + practical meaning (Q4)
- Systematic epistemic tagging on every substantive claim
- Every abstraction grounded in observable, measurable reality
- Cross-domain analogies with explicit structural isomorphism and stated limitations
- Reader can predict, explain, diagnose, design, and feel the inevitability of outcomes
- The document itself teaches *how to think* about the domain, not just *what to know*

---

## Failure Modes

**FM-1: The Wikipedia Trap**
*What it looks like:* Document reads like a well-organized encyclopedia entry — accurate but flat. Concepts are defined, not derived. Reader finishes with facts but no working mental model.
*Why it happens:* Writer prioritized breadth (covering all subtopics) over depth (tracing mechanisms to bedrock). Skipped the Why-Chain.
*Detection:* Count the "why" depth of the first 5 core concepts. If average depth is D1-D2, this failure mode is active.
*Correction:* For each concept, ask "why?" three more times and write the answers as connected paragraphs. Cut breadth to make room for depth.

**FM-2: The Number Desert**
*What it looks like:* Prose is conceptually rich but devoid of actual measurements, values, or quantities. Adjectives ("significant," "rapid," "enormous") replace numbers.
*Why it happens:* Writer treated quantification as optional decoration rather than a core discipline. Often caused by choosing a depth target that doesn't match the domain's quantitative nature.
*Detection:* Scan Part II (Machinery) for paragraphs with zero numbers. If >30% of paragraphs lack numbers, this failure mode is active.
*Correction:* For every adjective describing magnitude, find the actual number and substitute. Add scaling relationships and comparisons.

**FM-3: Floating Abstractions**
*What it looks like:* Elegant conceptual explanations that never touch ground. The reader understands the abstract idea but can't point to it in the real world. Common in philosophy-adjacent domains.
*Why it happens:* Writer stayed in the "Build from familiar" and "Make it precise" steps of Narrative Flow but skipped "Show it's real."
*Detection:* For each core concept, check: is there at least one observable, measurable, or experimentally demonstrated example? If not, the concept is floating.
*Correction:* Add a concrete grounding paragraph for each floating concept — a measurement, an experiment, a visible phenomenon.

**FM-4: Epistemic Flatness**
*What it looks like:* All claims presented with identical confidence. Mathematical theorems and speculative hypotheses are grammatically indistinguishable. Reader cannot calibrate what to trust.
*Why it happens:* Writer defaulted to assertive prose throughout without applying the Evidence Discipline. Often a result of using confident language as a stylistic choice.
*Detection:* Search for epistemic tags (PROVEN, CONFIRMED, CONSENSUS, DEBATED, SPECULATIVE). If fewer than 10 tags in a 20K-word document, this failure mode is active.
*Correction:* Re-read every substantive claim and tag it. Rewrite DEBATED and SPECULATIVE claims to present both sides or flag uncertainty.

**FM-5: The Slide Deck**
*What it looks like:* Document is 80%+ bullet lists with minimal connecting prose. Reads like presentation notes, not narrative explanation. Understanding doesn't build — it's scattered.
*Why it happens:* Writer defaulted to list format for efficiency. The Narrative Flow framework was not applied.
*Detection:* Count lines that start with `-`, `*`, or numbered markers vs. prose paragraphs. If bullet content exceeds narrative content by volume, this failure mode is active.
*Correction:* Convert core content from bullets to flowing paragraphs that build on each other. Keep bullets only for genuine enumeration (lists of items after narrative explanation).

**FM-6: Bridge Domain Misuse**
*What it looks like:* Cross-domain analogies are used decoratively ("this is like X") rather than structurally ("the mechanism here is identical to X in Y, and that identity reveals Z"). Analogies don't earn their weight.
*Why it happens:* Writer used the caller's bridge domains as metaphors rather than as structural isomorphisms. The analogy adds color but not insight.
*Detection:* For each cross-domain analogy, ask: "Does this analogy reveal a mechanism the reader couldn't see from inside the domain alone?" If not, it's decorative.
*Correction:* Either sharpen the analogy to a structural isomorphism (state the mapping precisely, then show what it reveals) or cut it.

**FM-7: Premature Coherence**
*What it looks like:* Everything fits together too neatly. No tensions, no open questions, no acknowledged gaps. The document feels like a closed system.
*Why it happens:* Writer smoothed over genuine debates, unresolved questions, and competing explanations to produce a "clean" narrative.
*Detection:* Check Part IV for misconceptions and Part V for open questions. If the document has zero DEBATED or SPECULATIVE tags, this failure mode is likely active.
*Correction:* Actively search for: competing theories, unresolved experimental results, claims that experts disagree on. Add them explicitly.

---

## What's Next

**Upstream skills that feed this one:**
- None required — this skill takes a raw domain name and produces a World Model from scratch
- Optional: if the caller provides research papers, the Research Synthesis skill can pre-process them into structured evidence

**Downstream skills this feeds:**
- **Research Synthesis** — the World Model provides the conceptual framework; Research Synthesis adds current evidence
- **Competitive & Market Analysis** — deep domain understanding enables structural (not surface) competitive assessment
- **Specification Writing** — understanding the domain deeply prevents specs that solve the wrong problem
- **Synthesizer agent** — World Models provide the substrate for thesis construction

**Chain interface:**
- **Receives:** Domain name + caller's current state + depth target + key questions + bridge domains + length preference
- **Produces:** A World Model document (10K-30K+ words) following the mandatory skeleton
- **Handoff artifact:** The World Model document itself, stored as `{domain_slug}_world_model_{date}.md`

---

## Appendix Checklist

Run this checklist before delivering the final document:

- [ ] **Structure:** All six Parts present (Opening, Bedrock, Machinery, Emergence, Human Reality, Synthesis, Going Deeper)
- [ ] **Opening:** Written after the rest of the document; distills the core insight; includes the best analogy with stated limitations
- [ ] **Why-Chain:** Every core concept in Parts I-III traced to bedrock (D4+); no concept below D2
- [ ] **Quantification:** Every quantitative claim has actual numbers with units (Q2+); core claims have full contextualization (Q3-Q4); zero bare adjectives describing magnitude
- [ ] **Evidence tags:** Every substantive claim in Parts I-III carries an epistemic status tag (PROVEN / CONFIRMED / CONSENSUS / DEBATED / SPECULATIVE / UNCERTAIN)
- [ ] **Grounding:** Every abstract concept has at least one concrete, observable, measurable example
- [ ] **Narrative Flow:** Core concepts follow the 7-step introduction sequence; no core concept skips Hook and Reveal
- [ ] **Prose over bullets:** Primary content is flowing narrative paragraphs; bullets used only for genuine enumeration
- [ ] **Citations:** All non-trivial claims have inline citations; References section compiles all sources
- [ ] **Mathematics:** Every equation or formula has full intuitive explanation (what each variable means, why this shape, what changes when you change inputs)
- [ ] **Misconceptions:** Part IV identifies at least 3 places where common intuition is wrong and explains why
- [ ] **Going Deeper:** Part VI includes specific resources (not vague recommendations), progressive exercises with timelines, and meta-lessons
- [ ] **Mental simulation test:** After reading the document, can the reader predict, explain, diagnose, design, and feel inevitability? If any of these five fail, the relevant section is incomplete
- [ ] **Length:** Document matches the requested length parameter (Focused: 10-15K, Comprehensive: 20-30K, Exhaustive: 30K+)
- [ ] **Filename:** Output saved as `{domain_slug}_world_model_{YYYY-MM-DD}.md`
