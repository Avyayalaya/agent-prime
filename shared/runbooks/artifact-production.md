# Runbook: Artifact Production

> **Trigger:** On-demand — PM needs a competitive analysis, spec, metric framework, or other skill-powered artifact.
> **Duration:** 1-2 sessions (automated) or 2-3 sessions (manual with review)
> **Agents:** Context Assembly → Artifact Producer (with PM Skill) → Quality Gates → Self-Fix Loop
> **Infrastructure:** `repos/pm-runtime/pipelines/artifact_draft.py`

---

## Phase 1: Context Assembly

**Activate:** Context Assembly pipeline gathers relevant context from M365, prior artifacts, and team knowledge.

**Input:** Task description + artifact type (competitive/spec/metric/research/narrative/problem)

**Output:** Structured context package with prior artifacts, email context, Teams context, meeting notes, file references.

**Fallback:** If WorkIQ unavailable, uses cached context + manual paste prompt.

---

## Phase 2: Artifact Production

**Activate:** Artifact Producer agent with full context loaded.

**Inputs assembled automatically:**

| Input | Source |
|-------|--------|
| PM Skill prompt | `pm-skills-arsenal/skills/{type}/` |
| Output template | `pm-team-system/templates/` |
| Learnings | `shared/learnings.md` |
| Prior team artifacts | `team-knowledge/` |
| Bar-setting exemplar | `config/exemplars.yaml` |

**Output:** Initial markdown draft.

---

## Phase 3: Quality Gates (Automated)

5 structural gates checked automatically:

| Gate | Requirement |
|------|------------|
| Executive Summary | Heading present, zero jargon |
| Assumption Registry | ≥3 load-bearing assumptions |
| Adversarial Self-Critique | ≥3 genuine weaknesses |
| Evidence Tier Annotations | ≥3 [T1]-[T6] markers |
| Context Sources | Section present with references |

**If all pass:** QA Pass template generated → save draft.
**If any fail:** → Phase 4.

---

## Phase 4: Self-Fix Loop

**Activate:** Artifact Fixer agent with gate failure report.

**Rules:**
- Max 2 fix attempts
- Preserve substance — only add missing sections
- If still failing after attempt 2: Escalation Report → Prime

**Output:** Fixed artifact that passes all gates.

---

## Phase 5: HTML Rendering (Optional)

**Trigger:** `output_format="html"` or `"both"`

**Additional gates for HTML:**

| Gate | Requirement |
|------|------------|
| Valid HTML structure | `<html>`, `<head>`, `<body>` |
| Design system CSS | #FDFAF6 background, font imports |
| Sticky navigation | `position:sticky` |
| Evidence badges | ≥3 `.ev-badge` classes |
| Confidence pills | ≥1 `.conf-pill` class |
| Responsive viewport | `<meta viewport>` tag |

---

## Phase 6: Save & Notify

1. Save to `state/pending_review/draft-{DATE}-{SLUG}.md` (and `.html`)
2. Teams notification: draft ready for review
3. Log run to `state/run_log.json`

---

## Runbook Rules

1. **Context assembly failure is non-fatal** — produce artifact with available context
2. **PM Skill is mandatory** — no artifact production without the relevant skill loaded
3. **Quality gates are non-negotiable** — self-fix loop must run
4. **Escalate after 2 failed fixes** — don't loop forever
5. **Exemplar excerpt is capped at 3000 chars** — reference, not copy

---

*Created: 2026-03-11. Maps to: `repos/pm-runtime/pipelines/artifact_draft.py`*
