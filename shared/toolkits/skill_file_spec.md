# Skill File Specification

> **Purpose:** The structural contract for what a skill file must contain. Any skill file in `shared/toolkits/skills/` must conform to this spec. A builder reading only this document can produce a conforming skill file without asking clarifying questions.
>
> **Governing decisions:** All structural choices in this spec trace to the ADRs in `projects/SYS-003_learning_capture/plan/adr.md`. See ADR-1 (hybrid extraction), ADR-3 (multi-tag taxonomy), ADR-4 (valid_until feedback mechanism), ADR-5 (markdown + YAML front matter format).
>
> **Quality bar:** `shared/toolkits/competitive_analysis.md` is the reference artifact. It demonstrates the target quality: framework-driven, evidence-tiered, actionable at both strategic and tactical layers (learnings.md Q5). A skill file should match this standard in its domain.

---

## 1. File Format

Every skill file is a markdown document (`.md`) with a YAML front matter block.

**Location:** `shared/toolkits/skills/{skill_name}.md` (flat directory, no subdirectories — ADR-3).

---

## 2. YAML Front Matter (REQUIRED)

The file begins with a YAML front matter block between `---` delimiters. All fields below are required unless marked optional.

```yaml
---
name: "{Skill Name}"
version: "1.0.0"
tags: ["{Tag1}", "{Tag2}"]
created: "YYYY-MM-DD"
valid_until: "YYYY-MM-DD"
derived_from: "{source}"
tested_with: ["{agent or context 1}"]
---
```

### Field Definitions

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `name` | string | Yes | Human-readable skill name. | Sentence case. Matches the `## Purpose` heading's capability description. |
| `version` | string | Yes | Semantic version. | Format: `MAJOR.MINOR.PATCH`. Start at `1.0.0` for new skills. |
| `tags` | list of strings | Yes | Categorization tags for discoverability. | Draw from the established taxonomy: `Context Engineering`, `Problem Shaping`, `Architecture`, `Evaluation`, `Execution`, `Meta`. Custom tags are permitted. Minimum 1 tag, no maximum. |
| `created` | string (date) | Yes | Date the skill was first created. | ISO 8601 date: `YYYY-MM-DD`. |
| `valid_until` | string (date) | Yes | Expiry date for freshness review. | ISO 8601 date. Maximum 6 months from `created` or from last review date. When this date passes, the skill is flagged for review in the weekly Prime audit. Any agent loading an expired skill must note the expiry to the user. |
| `derived_from` | string | Yes | Source of the skill's content. | If extracted from an agent prompt: the file path (e.g., `agents/synthesizer/prompt.md`). If created from scratch: `"original"`. If derived from multiple sources: comma-separated paths. |
| `tested_with` | list of strings | Yes | Agents or contexts that have validated this skill. | List of agent names or descriptions (e.g., `["Builder agent", "Generic Claude instance"]`). Empty list `[]` is valid for untested skills but should be populated after validation. |
| `references_path` | string | No | Path to a companion `references/` folder with deep-dive material (token mappings, extended examples, data tables, codebase-specific guidance). | Relative path from the skill file's location (e.g., `./references/`). The main skill file stays lean (≤500 lines) for context window efficiency; the references folder holds material that supports but doesn't need to be loaded by default. Skills without supplementary material omit this field. |
| `type` | string | No | Archetype classification. | Allowed values: `"methodology"` (default), `"codex"`. Determines which conformance checklist applies (see Section 6). A codex is a self-contained, machine-executable body of knowledge with embedded frameworks and decision rules — it produces output that would be extremely difficult for a single human to generate unaided. |
| `license` | string | No | License under which the skill is distributed. | SPDX identifier (e.g., `"MIT"`, `"Apache-2.0"`). Required if the skill is published publicly; optional for internal skills. |
| `description` | string | No | One-sentence trigger description for Claude Code's model-activated skill system. | Required if the skill is installed as a Claude Code plugin. Should specify when Claude should automatically load this skill (e.g., `"Use when performing competitive analysis, market entry assessment, or moat evaluation."`). Omit for skills used only via explicit loading. |

---

## 3. Body Sections

The markdown body follows the YAML front matter. Five sections are required. One section is optional.

### Section 1: Purpose (REQUIRED)

**What it is:** One sentence stating the capability this skill provides.

**Rules:**
- Maximum two sentences. One is preferred.
- State the capability, not the process. "Produce a structured research synthesis from multiple sources" — not "This skill helps you do research."
- A reader should know after this section whether this skill is relevant to their task.

**Example:**
```markdown
## Purpose
Produce a structured, evidence-graded research synthesis from multiple primary and secondary sources, with explicit confidence levels and counter-evidence.
```

---

### Section 2: Input Contract (REQUIRED)

**What it is:** What the caller MUST provide to use this skill. Explicit — no assumed context.

**Rules:**
- List required inputs with types and formats.
- List optional inputs with their defaults.
- List anti-inputs: what this skill does NOT handle. This prevents misuse.
- A caller with zero domain context and zero Agent Prime context should know exactly what to provide after reading this section.

**Structure:**
```markdown
## Input Contract

### Required
- **{Input name}** ({type}): {description}. {format or example if not obvious}.

### Optional
- **{Input name}** ({type}, default: {value}): {description}.

### Anti-Inputs (what this skill does NOT handle)
- {Description of out-of-scope input or task}.
```

**Quality test:** Read the Input Contract imagining you are a new hire on day one. If you'd need to ask "what do you mean by X?" for any input, the contract is underspecified.

---

### Section 3: Method (REQUIRED)

**What it is:** The operational steps to execute the skill. Graduated complexity with two tiers.

**Rules:**
- **Quick version:** 3–7 numbered steps. For a competent practitioner who needs a reminder, not a tutorial. Each step is one action.
- **Full version:** Detailed steps with decision points, edge cases, and reasoning. For a first-time user encountering this skill. Include "if X, then Y" decision logic where applicable.
- Both versions must produce the same output quality. The quick version is a compression of the full version, not a different method.

**Structure:**
```markdown
## Method

### Quick Version
1. {Step 1}
2. {Step 2}
3. {Step 3}
...

### Full Version
**Step 1: {Step name}**
{Detailed instructions. Include decision points, edge cases, and reasoning.}

**Step 2: {Step name}**
{Detailed instructions.}
...
```

**Quality test:** Give the Quick Version to a senior PM. Give the Full Version to a junior PM. Both should produce output that passes the Evaluation Criteria.

---

### Section 4: Evaluation Criteria (REQUIRED)

**What it is:** How to know the output is good. Specific, testable conditions — not subjective judgments.

**Rules:**
- Each criterion must be answerable as yes/no or with a measurable threshold.
- Avoid: "The output should be high quality." Use: "The output includes a confidence level (high/medium/low) for every claim."
- Include both structural criteria (format, completeness) and substantive criteria (accuracy, depth).
- Minimum 3 criteria. No maximum, but each must be independently testable.

**Structure:**
```markdown
## Evaluation Criteria

- [ ] {Criterion 1 — testable condition}
- [ ] {Criterion 2 — testable condition}
- [ ] {Criterion 3 — testable condition}
...
```

**Quality test:** Hand the criteria to someone who has never seen the skill's output. Can they evaluate a piece of work against the criteria without asking "what counts as X?"

---

### Section 5: Failure Modes (REQUIRED)

**What it is:** What goes wrong when this skill is applied badly. Named patterns with descriptions, not vague warnings.

**Rules:**
- Each failure mode has a name, a description of what it looks like, and why it happens.
- These are patterns, not edge cases. They should be the most common ways the skill fails.
- Minimum 2 failure modes. Aim for 3–5.

**Structure:**
```markdown
## Failure Modes

**{FM-1: Failure Mode Name}**
*What it looks like:* {Observable symptom in the output.}
*Why it happens:* {Root cause — what the user did wrong or what context was missing.}

**{FM-2: Failure Mode Name}**
*What it looks like:* {Observable symptom.}
*Why it happens:* {Root cause.}
```

**Quality test:** A user who reads the Failure Modes before starting should be able to avoid at least the most common failure. If the failure modes are too vague to be actionable ("the output might be wrong"), they fail this test.

---

### Section 6: Context Detection (OPTIONAL — for domain-specific execution skills)

**What it is:** A detection step that routes to different guidance based on the caller's environment or project context.

**When to include:** Domain-specific skills that target particular codebases, environments, or project types. Methodology skills (spec writing, research synthesis) do NOT need this. Execution skills targeting specific environments DO.

**Rules:**
- The detection step runs BEFORE the Method.
- It asks: "Which codebase/project/context are you in?" and routes to the appropriate guidance or reference material.
- Detection should be lightweight — a few questions or checks, not a full analysis.
- Each detected context can point to a different reference file via `references_path`.

**Structure:**
```markdown
## Context Detection

Before applying this skill, identify your context:

1. **{Context A}** (detected by: {signal — e.g., presence of a specific config file, project type, codebase name})
   → Load: `references/{context_a}_guidance.md`
   → Key differences: {what changes in this context}

2. **{Context B}** (detected by: {signal})
   → Load: `references/{context_b}_guidance.md`
   → Key differences: {what changes}

3. **Generic / Unknown context**
   → Use the default Method below without context-specific modifications.
```

---

### Section 7: Worked Example (OPTIONAL but recommended)

**What it is:** One concrete input → output demonstrating correct application of the skill.

**Rules:**
- Show a realistic input, then the output that a correct application of the Method would produce.
- The example should be small enough to fit in the file but realistic enough to demonstrate the skill's value.
- If the skill is domain-specific, use a PM-domain example.
- This section is optional because some skills are too broad for a single example to be representative. Include it when it would help a first-time user understand the expected output format and quality.

**Structure:**
```markdown
## Worked Example

### Input
{Concrete input matching the Input Contract.}

### Output
{The output produced by correctly applying the Method to the input above.}

### Why This Works
{1–2 sentences explaining which Method steps produced this output and which Evaluation Criteria it satisfies.}
```

---

## 4. Archetypes

Two archetypes are defined. The `type` YAML field determines which conformance checklist applies. If `type` is absent, default to `methodology`.

---

### Archetype 1: Methodology (`type: "methodology"` or absent)

**When to use:** Process-oriented skills where the value is in a repeatable procedure — spec writing, research synthesis, code review, etc. The skill encodes *how to do* a task.

**Required body sections:** Purpose · Input Contract · Method (Quick + Full) · Evaluation Criteria · Failure Modes

**Optional body sections:** Context Detection · Worked Example

**Conformance checklist:**

- [ ] YAML front matter is present and parses without errors
- [ ] Required YAML fields populated: `name`, `version`, `tags`, `created`, `valid_until`, `derived_from`, `tested_with`
- [ ] Optional YAML fields correct if present: `type` = `"methodology"`, `license` is SPDX, `description` is ≤2 sentences, `references_path` is a valid relative path
- [ ] `valid_until` is ≤6 months from `created` (or from last review date)
- [ ] `tags` includes at least 1 tag from the established taxonomy
- [ ] **Purpose** section exists: ≤2 sentences, states the capability
- [ ] **Input Contract** section exists: Required inputs, Optional inputs, and Anti-Inputs are all present
- [ ] **Method** section exists: Quick Version (3–7 steps) and Full Version (detailed steps with decision points) are both present
- [ ] **Evaluation Criteria** section exists: ≥3 testable criteria, each answerable yes/no
- [ ] **Failure Modes** section exists: ≥2 named failure patterns with observable symptoms and root causes
- [ ] **Context Detection** (if present): detection signals, context-specific routing, and generic fallback are defined
- [ ] **Worked Example** (if present): includes Input, Output, and Why This Works
- [ ] If skill targets code output: every Method rule has ✅/❌ inline code examples (Design Principle 6)

---

### Archetype 2: Codex (`type: "codex"`)

**When to use:** Domain-expertise skills where the value is in the encoded frameworks, scoring rubrics, and decision tables — competitive analysis, metric design, financial modeling, etc. The skill encodes *what to know* to do a task at elite tier. The output artifact would be extremely difficult to produce at this quality without the skill loaded.

**Signal:** If removing the skill would cause the output to degrade from elite-tier to consultant-tier (because the frameworks would be missing), it is a codex.

**Required body sections:** Purpose · When to Use / When NOT to Use · Domain Frameworks · Application Method · Quality Gradients · Failure Modes · What's Next

**Optional body sections:** Appendix Checklist · Worked Example · Computation Requirements

**Section definitions:**

| Section | Rules |
|---------|-------|
| **Purpose** | ≤2 sentences. States the output artifact, not the process. Name the artifact: "Produce a Competitive War Map" not "help with competitive analysis." |
| **When to Use / When NOT to Use** | Two subsections. "When NOT to Use" is as important as "When to Use" — prevents misuse. Include Anti-inputs: what this skill explicitly does NOT handle. |
| **Domain Frameworks** | Numbered framework sections. Each framework MUST include: (a) a definition, (b) scoring rubric or decision table, (c) output format template. Frameworks referenced but not encoded are worthless — the rubric IS the codex. Minimum 3 frameworks. |
| **Application Method** | Two tiers: Quick Version (numbered steps for experts) and Full Version (decision points, quality checkpoints per step). Both tiers must produce the same output quality. |
| **Quality Gradients** | Three-tier taxonomy: Intern Tier / Consultant Tier / Elite Tier. Each tier names what's present and what's missing. A user reading the Elite tier description should be able to self-evaluate their output. |
| **Failure Modes** | Named failure modes with: what it looks like (observable symptom), why it happens (root cause), detection signal, correction. Minimum 5 failure modes for a codex — these encode the most common ways expertise fails to transfer. |
| **What's Next** | Three components: (a) upstream skills that feed this one, (b) downstream skills this feeds, (c) chain interface — what the skill receives and what handoff artifact it produces. |
| **Appendix Checklist** | A checkbox list covering every output element. Should be usable as a final QA pass before delivering the artifact. |
| **Worked Example** | See Methodology archetype definition. Strongly recommended for codex skills because the output format complexity makes the "right" output non-obvious. |
| **Computation Requirements** | If the skill references scripts: state the command with all required arguments. State what to do if scripts are unavailable. Never require manual calculation when a script can provide precision. |

**Conformance checklist:**

- [ ] YAML front matter is present and parses without errors
- [ ] Required YAML fields populated: `name`, `version`, `tags`, `created`, `valid_until`, `derived_from`, `tested_with`
- [ ] `type: "codex"` present in YAML
- [ ] Optional YAML fields correct if present: `license` is SPDX, `description` is ≤2 sentences trigger for Claude Code, `references_path` is valid
- [ ] `valid_until` is ≤6 months from `created` (or from last review date)
- [ ] **Purpose** section exists: ≤2 sentences, names the output artifact
- [ ] **When to Use / When NOT to Use** section exists: both subsections present, Anti-inputs listed
- [ ] **Domain Frameworks** section exists: ≥3 frameworks, each with scoring rubric or decision table AND output format template
- [ ] **Application Method** section exists: Quick Version (numbered steps) and Full Version (with decision points and quality checkpoints) both present
- [ ] **Quality Gradients** section exists: Intern / Consultant / Elite tiers, each with named characteristics
- [ ] **Failure Modes** section exists: ≥5 named failure modes, each with observable symptom, root cause, detection, and correction
- [ ] **What's Next** section exists: upstream skills, downstream skills, chain interface (receives + produces + handoff artifact)
- [ ] **Appendix Checklist** (if present): covers all output elements as checkboxes
- [ ] **Worked Example** (if present): includes Input, Output, and Why This Works
- [ ] **Computation Requirements** (if present): every script command is complete with required arguments; unavailability fallback is stated

---

## 5. Conformance Checklist (Legacy — use Archetype checklists above)

Use this checklist to verify a skill file conforms to the spec before committing:

---

## 5. Design Principles

These principles govern decisions not covered by specific section rules:

1. **Portability over power.** A skill file that works for any competent agent is more valuable than one optimized for a single agent. Accept some quality loss in exchange for broader usability (ADR-1 consequence).

2. **Explicit over implicit.** If a caller needs to know it, put it in the Input Contract. If an evaluator needs to check it, put it in Evaluation Criteria. No assumed context.

3. **Graduated complexity.** Serve both the expert who needs a reminder and the novice who needs a tutorial. The Quick Version and Full Version in Method accomplish this without forking the skill into two files.

4. **Testable over aspirational.** Every Evaluation Criterion must be checkable. "Produces insight" is not a criterion. "Identifies at least one non-obvious implication that the user did not explicitly request" is a criterion.

5. **Format-translatable.** If a platform standard emerges (ADR-5 rationale, R6), the skill content should port to the new format with mechanical conversion. Don't build dependencies on the specific YAML field names or markdown structure beyond what the spec requires.

6. **Do/Don't examples for code-producing skills.** When a skill targets code output (React components, API calls, scripts, prompts with specific syntax), every rule in the Method must have a concrete "✅ Good — use this" / "❌ Avoid — not this" code snippet. Prose-only rules get ignored by coding agents. Methodology skills (spec writing, research synthesis) can stay prose-based, but code-producing skills MUST have inline examples. This is the single biggest quality lever for execution skills.

---

*Created: 2026-07-24 | Builder Agent, Phase 1*
*Governing ADRs: ADR-1 through ADR-5 in `projects/SYS-003_learning_capture/plan/adr.md`*
*Quality bar reference: `shared/toolkits/competitive_analysis.md`*
