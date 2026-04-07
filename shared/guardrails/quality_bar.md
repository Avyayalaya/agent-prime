# Quality Bar

> **Type:** Output guardrail
> **Action:** Warn — flag missing quality checks but don't block delivery
> **Applies to:** All agents
> **Source:** CLAUDE.md Rule 10, Rule 23, Rule 9

---

## Trigger

Activates on every substantial artifact — theses, analyses, specs, articles, reports, build outputs. Does NOT activate on internal state updates (registry changes, dispatch entries, session journal entries).

## Validation Logic

### 1. Quality Check Visibility (Rule 10)
Every substantial artifact must include a `## Quality Check` section showing which checks were applied. Quality verification must be visible, not invisible.

### 2. Methodology Completeness (Rule 23)
When executing an agent's methodology (Industry Analyst 9-step, Investment Analyst multi-lens valuation), EVERY step must be executed with its output before moving to the next. Never compress a multi-step methodology into a single-pass output.

**Reference benchmarks:**
- Industry Analyst: ~80-90KB output
- Investment Analyst: ~80-90KB output
- If output is significantly smaller, steps were skipped

### 3. Epistemic Failure Mode Self-Check (Rule 9)
Nine failure modes are documented in `shared/context.md`. Every thesis and draft must pass:

- [ ] Not pattern-matching without evidence
- [ ] Not overfitting to a single framework
- [ ] Not confusing correlation with causation
- [ ] Not anchoring to the first data point
- [ ] Not ignoring base rates
- [ ] Not survivorship bias in examples
- [ ] Not authority fallacy
- [ ] Not sunk cost reasoning
- [ ] Not narrative fallacy (story feels true but isn't)

### 4. Evidence Grading
Claims must have confidence levels (high/medium/low) where applicable. Ungraded claims in strategic theses are a quality failure.

## Validation Checklist

- [ ] `## Quality Check` section present in output
- [ ] If multi-step methodology: all steps executed with output
- [ ] Epistemic failure modes self-checked
- [ ] Claims have confidence levels where relevant
- [ ] Counter-evidence acknowledged (not just supporting evidence)

## On Failure

**Warn.** Flag the missing quality elements to the user. The output can still be delivered but the user should know what's missing.
