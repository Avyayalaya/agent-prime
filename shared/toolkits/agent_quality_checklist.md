# Agent Quality Self-Check Protocol

> **Purpose:** Before any agent returns "task complete," it runs this checklist against its own output and returns a compliance report WITH the output. This prevents structural gaps from reaching human review.

---

## When to Use

This checklist applies to agents building:
- Skills (SKILL.md files)
- Use cases (USE_CASES.md files)
- Case studies (cross-skill workflow demonstrations)
- Any structured artifact with required sections

---

## Skill File Checklist (for SKILL.md builders)

Run this before saying "skill complete":

### Structural Requirements
- [ ] YAML front matter present with all required fields (name, description, version, type, tags, created, valid_until, derived_from, tested_with, license)
- [ ] Purpose section (2-3 sentences, names the output artifact)
- [ ] When to Use / When NOT to Use (with Anti-inputs subsection)
- [ ] Format Rules section (9 rules minimum)
- [ ] Output Template (mandatory document skeleton)
- [ ] Executive Summary template (zero-jargon requirement)
- [ ] How to Read This Document (time-based + role-based navigation)
- [ ] Notation Key (explains all symbols, tiers, confidence levels)
- [ ] Step 0: Context Fitness Check
- [ ] Step 0b: Framework Selection (routing table)
- [ ] Domain Frameworks section (minimum 6 frameworks)
- [ ] Evidence Standards (T1-T6 tier system)
- [ ] Application Method (Quick + Full versions)
- [ ] Mandatory Output Sections (Assumption Registry, Adversarial Self-Critique, Revision Triggers)
- [ ] Quality Gradients (Intern / Consultant / Elite tiers)
- [ ] Failure Modes (minimum 7, with What/Why/Detection/Correction)
- [ ] What's Next (chain interface with upstream/downstream skills)
- [ ] Appendix: Quick-Reference Checklist

### Framework Quality
- [ ] Each framework has a scoring rubric OR decision table (not just description)
- [ ] Each framework has at least one worked example or application pattern
- [ ] Frameworks are domain-specific (not generic strategy advice)

### Format Rules Compliance
- [ ] H/M/L confidence levels specified (not "likely" or "may")
- [ ] Per-cell evidence tier annotation shown in at least one comparison matrix
- [ ] O→I→R→C→W cascade format demonstrated (Observation → Implication → Response → Confidence → Watch Indicator)
- [ ] Step 0 routing table present (question type → framework selection)
- [ ] Cross-framework contradictions handling described
- [ ] `[POTENTIALLY STALE]` flag usage documented
- [ ] `[EVIDENCE-LIMITED]` flag usage documented

### Completeness
- [ ] File length 800-1300 lines (if significantly shorter or longer, justify why)
- [ ] Footnote/attribution style consistent
- [ ] No placeholder text (no "TBD", "[example]", "[framework name]")

### Self-Assessment Output Format

```markdown
## Skill Quality Self-Check: [skill-name]

**Line count:** [actual] / 800-1300 target
**Structural sections:** [X]/20 required sections present
**Frameworks:** [X]/6 minimum (each with rubric/decision table)
**Failure modes:** [X]/7 minimum
**Format rules compliance:** [X]/9 rules demonstrated

### Missing/Incomplete Items
- [List any checklist items that are ❌ or only partially complete]

### Warnings
- [Any items that are technically present but lower quality than expected]

### Ready to Ship?
[YES/NO + brief reasoning]
```

---

## Use Case File Checklist (for USE_CASES.md builders)

Run this before saying "use cases complete":

- [ ] 3 use cases present
- [ ] Each use case has: Scenario, Prompt, Without the Skill, With the Skill, What Changed
- [ ] "Without" section is 200-300 words (competent but shallow)
- [ ] "With" section is 400-600 words (demonstrates specific frameworks)
- [ ] "What Changed" has 4-5 specific, named improvements
- [ ] Use cases demonstrate DIFFERENT frameworks/capabilities (not repetitive)
- [ ] Real company scenarios (can be anonymized, but problems must be realistic)
- [ ] Evidence tiers shown in "With" section
- [ ] Confidence levels (H/M/L) shown in "With" section
- [ ] At least one use case shows O→I→R→C→W cascade
- [ ] "Without" section is not strawmanned (represents good AI without skill)

---

## Case Study Checklist (for cross-skill workflow demonstrations)

Run this before saying "case study complete":

- [ ] Realistic scenario (specific numbers, real business problem)
- [ ] 4-5 skills chained in sequence
- [ ] Each skill's output section shows abbreviated artifact (not just summary)
- [ ] Handoffs between skills are EXPLICIT (not implied)
- [ ] Time estimate provided (and realistic)
- [ ] "What This Demonstrates" section present
- [ ] Target audience will recognize their work in the scenario
- [ ] No framework jargon without explanation
- [ ] Demonstrates value delta (with skills vs. without)

---

## How to Use This Checklist

**Before returning output:**
1. Read this checklist
2. Check your output against it
3. Generate the self-assessment report
4. Return BOTH: (a) your output file, (b) the self-assessment report

**Example return message:**
```
Skill file written to: [path]
Line count: 1,099 / 800-1300 ✅
Structural compliance: 20/20 sections ✅
Frameworks: 8/6 (with rubrics) ✅
Failure modes: 9/7 ✅
Format rules: 9/9 demonstrated ✅

Ready to ship: YES
```

This way the human reviewer knows WHERE to focus effort (or can skip detailed review if everything passes).
