# Learnings Registry

> Accumulated corrections and patterns. Every feedback that reveals a reusable pattern is captured here. These are hard constraints, not suggestions.
>
> **How it works:** When you correct an agent's output and the correction is a *pattern* (not a one-off edit), append it here under the relevant category. Every agent reads this file at session start. Learnings compound — they're never session-scoped.
>
> The examples below are real patterns from the system's development. They demonstrate what good learnings look like. Replace or extend them with your own as you use the system.

---

## Voice Patterns

<!-- Add your voice/writing corrections here. Examples:
- Sentence structure preferences
- Tone corrections (too formal, too casual, too academic)
- Phrasing bans (words or constructions that don't sound like you)
-->

---

## Content Patterns

<!-- Add your content/framing corrections here. Examples:
- How deep to go on philosophy vs. practical advice
- Analogy placement rules
- What level of abstraction to frame arguments at
-->

---

## Process Patterns

**P1** (source: system development, 2026-03)
Learning: Started building before the plan was complete. Had to correct errors post-build that a plan review would have caught.
Rule: **Plan before build.** Always complete the planning pipeline before starting execution. Fine-tuning a plan is cheaper than correcting errors post-build.

**P2** (source: system development, 2026-03)
Learning: Changed a downstream asset but forgot to update 4 upstream files that referenced the old version. The next session started with stale references everywhere.
Rule: **Change propagation is not optional.** When any asset changes, check `shared/dependency_map.md` and update ALL dependent files in the same session. Never leave propagation for "next time" — the next session has no memory of what drifted.

**P3** (source: system development, 2026-03)
Learning: Build specs had 8 pages on architecture and 3 bullet points on distribution. The artifact was built perfectly and reached nobody.
Rule: **Publish parity.** Every plan for a shippable artifact must include a distribution section with equal rigor to the build spec — channels, launch sequence, content derivatives, success metrics. Building without a distribution plan is inventory, not leverage.

---

## Quality Patterns

**Q1** (source: system development, 2026-03)
Learning: A hallucinated research paper URL made it into a published article. The source was fabricated by the LLM.
Rule: **Verify all sources.** Every URL, citation, and data point must be verified before inclusion. Scout signals must have `url_verified` status. Never trust LLM-generated citations at face value.

**Q2** (source: system development, 2026-03)
Learning: Agent instructions said "this matters" and "ideally do X." The model treated them as suggestions and skipped half of them.
Rule: **AI compliance requires structural enforcement.** Three levers: (1) put format rules at the TOP of files — models weight early content more. (2) Use directive language ("REQUIRED," "MUST," "FOLLOW EXACTLY"), not suggestion language. (3) Add a self-verification checklist at the BOTTOM — the model checks its own output. Sandwich: rules → content → compliance check.

---

## Build Patterns

**B1** (source: system development, 2026-03)
Learning: Added a "check the skills library" guideline to documentation. Nobody read it. Added the same check as Rule 15 in `copilot-instructions.md` (auto-injected into every session). Now every agent checks it.
Rule: **Pull mechanisms must be mechanical, not aspirational.** Place forcing functions in files that are already in every agent's context window. A rule in documentation is a suggestion; a rule in `copilot-instructions.md` is structural.

**B2** (source: system development, 2026-03)
Learning: Added rendering instructions to each agent's prompt — "after producing output, offer to render to HTML." Agents ignored it. The rendering step competed with 200-2000 lines of core methodology for attention, required loading 4 additional files (skill + standard + template + source), and asked one agent to do two fundamentally different jobs.
Rule: **Content production and artifact rendering are separate invocations.** Never ask a producing agent to also render its output. The Writer writes. The Builder renders. Rendering requires dedicated context: design system, HTML templates, component library. A bolt-on step in the wrong prompt will be ignored or produce broken output. Instead, place the rendering reminder in `copilot-instructions.md` (Rule 26) where it's structurally enforced.

---

## Agent Design Patterns

**AD1** (source: system development, 2026-03)
Learning: Output files named `analysis.md` were ambiguous — any reference required the full folder path for context.
Rule: **Every output file must be self-describing.** Name files so they're referenceable without folder context: `{subject}_{type}_{date}.md`. Never `analysis.md`, `output.md`, or `results.md`.

**AD2** (source: system development, 2026-03)
Learning: Read the agent methodology, then produced a compressed summary of what it would produce. The output was 20% of the expected length and missed 80% of the insights.
Rule: **Execute the methodology step-by-step — never summarize.** Each step builds on the previous one. If the output is significantly shorter than expected, steps were skipped. Sequential execution, not summarization.

---

## Propagation Tracker

| ID | Learning | Target Files | Status |
|----|----------|-------------|--------|
| P1 | Plan before build | `.github/copilot-instructions.md` (Rule 16) | ✅ Built in |
| P2 | Change propagation | `shared/dependency_map.md`, `.github/copilot-instructions.md` (Rule 12) | ✅ Built in |
| B1 | Mechanical pull mechanisms | `.github/copilot-instructions.md` (Rule 15) | ✅ Built in |
| B2 | Rendering is separate invocation | `.github/copilot-instructions.md` (Rule 26), all 9 agent prompts (one-line reminder), README example | ✅ Built in |
| AD1 | Referenceable naming | `.github/copilot-instructions.md` (Rule 20) | ✅ Built in |

