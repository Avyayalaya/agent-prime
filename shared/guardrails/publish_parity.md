# Publish Parity

> **Type:** Output guardrail
> **Action:** Block — build specs without distribution plans are incomplete
> **Applies to:** Planner, Builder
> **Source:** CLAUDE.md Rule 21, Rule 33

---

## Trigger

Activates when Planner produces a Build Handoff Spec for any shippable artifact: repo, tool, article, framework, teaching material. Also activates when Builder reviews a spec before starting work.

## Validation Logic

### Publish Parity (Rule 21)
Every Build Handoff Spec for a shippable artifact must include a **Publish & Distribution** section with equal rigor to the build spec:
- Channels (where it ships)
- Launch sequence (what order)
- Content derivatives (what other formats get produced)
- Target audience (who it's for)
- Success metrics (how we know it worked)

**Test:** If a plan has 8 pages on architecture and 3 bullet points on GTM, it's incomplete — send it back to the Planner.

### Discoverability (Rule 33)
Every shippable artifact must be discoverable, evaluable, and composable by other AI systems:

**(a) Identity** — structured capability manifest (AGENTS.md, metadata block, or equivalent)
**(b) Evaluability** — reproducible benchmarks and at least one complete example invocation
**(c) Composability** — typed input/output schemas

**Test:** If a Build Handoff Spec doesn't include a Discoverability section, it's incomplete.

### Capability Deployment Map (Rule 44)
Before P0/P1 builds: Prime must produce a map of every agent, skill, and script mapped to specific tasks for this project. Without it, Builder cannot start.

## Validation Checklist

- [ ] Build Handoff Spec has Publish & Distribution section
- [ ] Distribution section has equal page-count rigor to build section
- [ ] Channels, launch sequence, content derivatives, audience, success metrics defined
- [ ] Discoverability section present (identity + evaluability + composability)
- [ ] For P0/P1 builds: Capability Deployment Map exists

## On Failure

**Block.** Return the spec to Planner with a note specifying which sections are missing. Builder does not start until parity is achieved.
