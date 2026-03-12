# Agent Prime — Shared Context

> This document is the foundational reference for all agents. Every agent reads this before producing output.
> **Fill this in before using Agent Prime.** The Onboarding Agent (`agents/onboarder/prompt.md`) can help you complete this interactively — just invoke it and answer its questions.

---

## Who Are You?

### Identity
- **Name:** <!-- Your full name -->
- **Current Role:** <!-- e.g., Senior Product Manager, Acme Corp -->
- **Location:** <!-- City, Country -->
- **Target:** <!-- Where you're heading — e.g., VP Product at a Series B startup, CTO at a climate tech company -->
- **Values:** <!-- 3-5 core values that drive your decisions — e.g., Curiosity, Craftsmanship, Impact -->
- **Motto:** <!-- Optional — a personal operating principle in a few words -->

### Career Arc

<!-- Fill in your professional journey. This helps agents understand your experience base and what makes your perspective unique. -->

| Phase | Company | Role | Years | Scale/Impact |
|-------|---------|------|-------|--------------|
| <!-- Phase 1 --> | <!-- Company --> | <!-- Role --> | <!-- Years --> | <!-- What you built, how big it was --> |
| <!-- Phase 2 --> | <!-- Company --> | <!-- Role --> | <!-- Years --> | <!-- What you built, how big it was --> |
| <!-- Phase 3 --> | <!-- Company --> | <!-- Role --> | <!-- Years --> | <!-- What you built, how big it was --> |

### Your Unique Lens

<!-- What makes YOUR perspective different from someone with a similar title? What intersections of experience do you bring? 2-3 sentences. Example: "I've worked across hardware (manufacturing), marketplace (e-commerce), and AI (enterprise SaaS). This cross-domain trajectory shapes how I see platform problems — I think in supply chains, not just software abstractions." -->

### Intellectual Breadth

<!-- What do you read, study, and think about BEYOND your day job? This isn't decoration — it's the substrate of your pattern recognition. Agents use this to find cross-disciplinary analogies that fit your thinking. -->

**CRITICAL FOR AGENTS:** The examples below are *illustrative of a thinking mode*, not an exhaustive inventory. The user reads and thinks across many fields. Agents should reason independently from any field or model that structurally fits the thesis being built. The reference library (`shared/reference_library.md`) captures what has been explicitly articulated so far, but it is a growing snapshot, not a boundary.

**The thinking mode (what to replicate):**
- Read about a system in any field → extract the mechanism → test whether it maps structurally to the problem at hand → if the isomorphism holds, use it
- The mechanism matters, not the source. Any model from any field is valid if it passes the structural isomorphism bar.

**Models and domains you draw from** (add your own — this list should grow constantly):

<!-- Examples of what to put here:
*Science:* Game theory, network effects, systems dynamics, thermodynamics, evolutionary biology
*Economics:* Behavioral economics, market microstructure, platform economics
*Philosophy:* Stoicism, epistemology, Eastern philosophy
*Art:* Architecture, music theory, visual design principles
*Sport:* Chess (positional vs tactical), martial arts (leverage), endurance sports (pacing)
-->

### NDA / Confidentiality Rules

<!-- What can and can't be referenced in public-facing content? -->

- **Current employer:** Never reference internal data, roadmaps, or unreleased features from <!-- your current employer -->
- **Previous employers:** Never reference proprietary systems or confidential processes from <!-- your previous employers -->
- **General rule:** Frame all insights as industry observations, personal frameworks, or public information. When in doubt, abstract the specific into the general.

### Goals

<!-- What are you trying to achieve with Agent Prime? These map to agent workflows. -->

| Goal | What it means | How you'll measure it |
|------|--------------|----------------------|
| <!-- e.g., "Build authority" --> | <!-- e.g., "Become a recognized voice in AI product management" --> | <!-- e.g., "3 published articles, 2 conference talks, 1000 LinkedIn followers in 6 months" --> |
| <!-- e.g., "Ship a product" --> | <!-- e.g., "Launch my side project to 100 users" --> | <!-- e.g., "MVP shipped, 100 signups, 50 WAU" --> |
| <!-- e.g., "Learn deeply" --> | <!-- e.g., "Build genuine expertise in quantum computing" --> | <!-- e.g., "Publish a synthesis that experts validate as insightful" --> |

---

## How You Think (Meta-Cognitive Model)

<!-- This section is OPTIONAL but powerful. If you can articulate HOW you think — not just WHAT you think about — agents will produce dramatically better output. The Onboarding Agent can help you discover these patterns. -->

**Reasoning operations you naturally use:**

1. **Layer thinking.** Any complex system has layers. The interesting failures and opportunities happen at the *interfaces* between layers — not inside them. First question in any new domain: "What are the layers and where are the hidden dependencies between them?"

2. **Isomorphic mapping.** Structural parallels between systems in completely different domains — the same shape, different substrate. The bar: if you can't state the isomorphism in one sentence, the analogy isn't precise enough.

3. **Non-linear dynamics.** Feedback loops, compounding effects, tipping points. Look for where small inputs produce disproportionate outputs.

4. **Hidden dependency hunting.** "What breaks this? What is the single point of failure that isn't in anyone's risk register?"

5. **Adversarial self-critique.** "Now rip this entire thinking to shreds." Genuine attempts to break your own reasoning.

6. **Framework generalization.** When a framework works in one domain, immediately ask: "How does this generalize? What is the meta-pattern?"

<!-- Add, remove, or modify these. They should reflect YOUR actual reasoning patterns, not generic good practices. -->

### Epistemic Failure Modes (Guardrails)

These 9 failure modes corrupt thinking when using AI as a thought partner. They are not generic AI risks — they are *epistemic failure modes that corrupt thinking itself.* Every agent should be aware of these:

1. **Premature Coherence** — AI produces clean explanations too early. Linguistic fluency gets mistaken for ontological clarity. *Guardrail:* "This feels coherent but shallow. What assumptions are allowing this coherence?"

2. **Analogy Capture** — A powerful analogy starts *driving* the inquiry instead of *testing* it. *Guardrail:* "Where exactly does this analogy stop being valid?"

3. **Teleology Smuggling** — Purpose, optimization, or progress quietly enter the model without being invited. *Guardrail:* "Rebuild this without assuming purpose or destination. What remains?"

4. **Category Collapse** — Distinct layers collapse into one another without justification. *Guardrail:* "Which category is this statement operating in? What breaks if we separate these layers?"

5. **Deference Drift** — The human slowly stops pushing back. AI becomes the silent authority. *Guardrail:* "Assume the AI is wrong here. What would I propose myself?"

6. **Surface Abstraction** — The inquiry becomes abstract without becoming deep. *Guardrail:* "Express this as a narrative, then as a rule, then as an aphorism. What disappears?"

7. **Endless Refinement Loop** — Each pass produces minor improvements without structural change. *Guardrail:* "Is this genuinely unstable, or just unfamiliar?"

8. **Forced Synthesis** — Different lenses forced to agree when they shouldn't. *Guardrail:* "Where does this framework fundamentally fail?"

9. **Mistaking Output for Insight** — The production of text confused with understanding. *Guardrail:* "If the AI disappeared now, what do I actually understand?"

**Rule for agents:** These guardrails apply to the agents themselves. When the Synthesizer builds a thesis or the Writer constructs an argument, these 9 failure modes are the quality bar.

### Reference Library Index

Full entries with structural detail, quotes, and analogy mappings live in `shared/reference_library.md`. When building analogies or frameworks, scan this index for relevant mechanisms, then pull the full entry.

<!-- Start empty. As you use Agent Prime, Scout and Synthesizer will populate this with models, books, papers, and frameworks that inform your thinking. -->

| Entry | Domain | Key Mechanism |
|---|---|---|
| <!-- e.g., "Thinking, Fast and Slow" --> | <!-- book --> | <!-- Dual process theory; System 1 intuition vs System 2 deliberation --> |
| <!-- Add entries as you go --> | | |

---

## Voice & Style

<!-- How do you write and communicate? This is critical for the Writer agent. If you skip this section, the Writer will produce generic output. -->

### Writing Voice
<!-- Describe your natural writing style in 2-3 sentences. Example: "Blunt, conversational, short sentences. I write like I'm explaining to a smart friend, not delivering a keynote. I include myself in criticism — I don't lecture from above." -->

### Things to NEVER do in your voice
<!-- List specific patterns that sound wrong coming from you. Examples:
- Never use "not X but Y" constructions (say the positive thing directly)
- Never use hype language ("revolutionary", "game-changing", "paradigm shift")
- Never open with rhetorical questions
- No Oxford comma (or: always Oxford comma — your call)
-->

### The CXO Test
<!-- What role should your writing sound like? Example: "Would a VP Engineering say this in a design review?" or "Would a founder say this to an investor?" This gives the Writer a calibration target. -->

---

*This is a living document. Update it as you learn more about yourself and as Agent Prime learns about you through the feedback loop in `shared/learnings.md`.*
