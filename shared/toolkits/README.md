# Shared Toolkits

> **Purpose:** Accumulated analytical methodologies, frameworks, and quality standards. These are NOT analogies (that's `reference_library.md`). These are HOW-TO playbooks — the thinking infrastructure that makes any agent's output elite-tier.

> **How agents use this:** When any agent needs to produce analysis, research, or structured thinking, check the relevant toolkit first. These encode the quality bar and methodology that separate generic output from world-class output.

> **How to add:** Each toolkit is a standalone `.md` file in this folder. One domain per file. Accumulate — never start from zero.

## Index

| Toolkit | File | Purpose | Created |
|---------|------|---------|---------|
| Competitive Analysis | [competitive_analysis.md](competitive_analysis.md) | Frameworks, lenses, evidence standards, and output quality markers for elite competitive/market analysis | 2026-02-15 |
| Skill File Specification | [skill_file_spec.md](skill_file_spec.md) | Structural contract for what a skill file must contain — YAML front matter schema + 6 body sections. Governs all files in `skills/`. | 2026-07-24 |

## Skills Library

Portable, standalone skill files that any agent or human can load and execute. Each skill conforms to the Skill File Specification above.

**Index:** [`skills/README.md`](skills/README.md) — full skills index with tags, versions, validation status, and freshness protocol.

| Skill | File | Tags | Derived From |
|-------|------|------|-------------|
| Specification Writing | [skills/specification_writing.md](skills/specification_writing.md) | Problem Shaping, Execution | Original |
| Research Synthesis | [skills/research_synthesis.md](skills/research_synthesis.md) | Context Engineering, Evaluation | `agents/synthesizer/prompt.md` |

---

*Created: 2026-02-15*
*Last updated: 2026-07-24*
