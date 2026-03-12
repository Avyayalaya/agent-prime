# Skills Library — Index

> **Purpose:** Standalone, portable skill files that any agent, human, or external system can load and execute. Each skill is a self-contained markdown document with a YAML front matter block and standardized body sections.
>
> **How to use:** Find the skill relevant to your task. Load it into your context. Follow the Method section. Evaluate your output against the Evaluation Criteria section.
>
> **Spec:** All skill files conform to the [Skill File Specification](../skill_file_spec.md). The spec defines the structural contract — YAML schema, required sections, quality bar.
>
> **Governing decisions:** [ADR document](../../../projects/SYS-003_learning_capture/plan/adr.md) — extraction approach, composability model, taxonomy, feedback mechanism, format.

---

## Skills Index

| Skill | File | Format | Tags | Version | Valid Until | Derived From |
|-------|------|--------|------|---------|-------------|-------------|
| Specification Writing | [specification_writing.md](specification_writing.md) | Methodology | Problem Shaping, Execution | 1.0.0 | 2027-01-23 | Original |
| Research Synthesis | [research_synthesis.md](research_synthesis.md) | Methodology | Context Engineering, Evaluation | 1.0.0 | 2027-01-23 | `agents/synthesizer/prompt.md` |
| Competitive & Market Analysis | [competitive-market-analysis/SKILL.md](competitive-market-analysis/SKILL.md) | Codex | Analyze, Strategy, Market Intelligence | 1.0.0 | 2026-08-18 | `shared/toolkits/competitive_analysis.md` |
| Metric Design & Experimentation | [metric-design-experimentation/SKILL.md](metric-design-experimentation/SKILL.md) | Codex | Evaluate, Metrics, Experimentation | 1.0.0 | 2026-08-18 | Original |
| Deep Domain Learning | [deep-domain-learning/SKILL.md](deep-domain-learning/SKILL.md) | Codex | Context Engineering, Evaluation, Meta | 1.0.0 | 2026-08-25 | `Projects/AI_Learning and Mastery/World_Model_Builder_v2.1_FINAL.md` |

---

## Tags Taxonomy

Skills carry multiple tags for discoverability (ADR-3). Tags draw from the established taxonomy:

| Tag | Description | Skills |
|-----|-------------|--------|
| Context Engineering | Building, managing, and optimizing context for AI agents and humans | Research Synthesis, Deep Domain Learning |
| Problem Shaping | Defining problems, writing specs, scoping work | Specification Writing |
| Architecture | System design, decomposition, interface contracts | *(none yet)* |
| Evaluation | Assessing quality, grading evidence, running validations | Research Synthesis, Deep Domain Learning |
| Execution | Building, shipping, completing defined work | Specification Writing |
| Meta | Skills about skills — meta-cognitive, process-level | Deep Domain Learning |
| Analyze | Structural analysis of markets, competitors, systems | Competitive & Market Analysis |
| Strategy | Strategic framework application and decision-making | Competitive & Market Analysis |
| Market Intelligence | Competitive landscape, moat assessment, disruption analysis | Competitive & Market Analysis |
| Metrics | Metric design, North Star frameworks, Goodhart countermeasures | Metric Design & Experimentation |
| Experimentation | A/B test design, statistical validity, experiment planning | Metric Design & Experimentation |

Custom tags are permitted. Governance deferred until >10 skills exist (ADR-3).

---

## Freshness Protocol

Every skill has a `valid_until` date in its YAML front matter (ADR-4). When this date passes:

1. The skill is flagged for review in the weekly Prime audit.
2. Any agent loading an expired skill must note the expiry to the user.
3. Review means: re-read the skill, verify the Method and Evaluation Criteria still reflect current best practice, update `valid_until` to a new date (max 6 months out), bump the `version` patch number.

**Current freshness status:**

| Skill | Valid Until | Status |
|-------|------------|--------|
| Specification Writing | 2027-01-23 | 🟢 Fresh |
| Research Synthesis | 2027-01-23 | 🟢 Fresh |
| Competitive & Market Analysis | 2026-08-18 | 🟢 Fresh |
| Metric Design & Experimentation | 2026-08-18 | 🟢 Fresh |
| Deep Domain Learning | 2026-08-25 | 🟢 Fresh |

---

## Validation Status

| Skill | Tested With | Validation Result | Date |
|-------|-------------|-------------------|------|
| Specification Writing | Builder agent (generic, no Agent Prime context) | PASS — 8/8 evaluation criteria | 2026-07-24 |
| Research Synthesis | Builder agent (generic, no Agent Prime context) | PASS — 8/8 evaluation criteria | 2026-07-24 |
| Competitive & Market Analysis | Claude Sonnet 4, Claude Opus 4 | Not formally validated yet | — |
| Metric Design & Experimentation | Claude Sonnet 4, GPT-5.1 | Not formally validated yet | — |
| Deep Domain Learning | Claude Opus 4, Claude Sonnet 4.5 | Not formally validated yet | — |

See `projects/SYS-003_learning_capture/plan/validation_results.md` for full validation details.

---

## V2 Gate

V2 development (additional skills, composition model, usage tracking) is **gated on demonstrated usage:**
- **Threshold:** Skills loaded in ≥3 distinct sessions within 8 weeks of v1 ship.
- **Tracking:** Manual — note in session logs when a skill is loaded.
- **If threshold not met:** Park the project (K3). The portability thesis is validated technically but not practically.

## v1.1 Planned Upgrades

From MAI Copilot design skill comparison (learnings Q8, Q9, Q10):
- [ ] Add 2-3 inline do/don't examples per Method step in existing skills
- [ ] Add `references_path` optional field to YAML schema in skill_file_spec.md
- [ ] Add optional "Context Detection" section to skill_file_spec.md
- [ ] Add "Code-Producing Skills Addendum" to skill_file_spec.md for future code-heavy skills

---

*Created: 2026-07-24 | Builder Agent, Session 3*
*Governing spec: `shared/toolkits/skill_file_spec.md`*
*Governing ADRs: `projects/SYS-003_learning_capture/plan/adr.md`*
