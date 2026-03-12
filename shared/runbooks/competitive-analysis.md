# Runbook: Competitive Analysis

> **Trigger:** New competitive analysis needed — competitor move, market entry assessment, or scheduled refresh.
> **Duration:** 1-2 sessions
> **Agents:** Scout → Intel Agent / Industry Analyst → Synthesizer → Writer
> **Quality Gate:** Prime reviews final artifact against PM Skills quality standards

---

## Phase 1: Signal Gathering (Scout)

**Activate:** Scout with targeted scope on the competitive landscape.

**Input:**
- Competitor names or product area
- Specific trigger (what prompted this analysis?)
- Any existing team-knowledge/competitive/ artifacts to build on

**Output:** Signal digest with competitive signals tagged, sources verified.

**Handoff:** Standard Handoff → Phase 2

---

## Phase 2: Structural Analysis (Intel Agent or Industry Analyst)

**Choose agent:**
- **Intel Agent** — for weekly competitive scans, surface-level moves
- **Industry Analyst** — for deep structural mapping, value chain analysis

**Input:**
- Scout's signal digest
- Existing team-knowledge/competitive/ artifacts (mandatory read)
- Specific analysis questions from the trigger

**Output:** Competitive intelligence report or structural industry map.

**Quality Check:** Does the analysis go beyond description to reveal mechanisms?

**Handoff:** Standard Handoff → Phase 3

---

## Phase 3: Thesis Integration (Synthesizer)

**Activate:** Synthesizer to integrate competitive findings into strategic theses.

**Input:**
- Intel/Industry Analyst output
- Active theses that touch this competitive landscape
- PM Skills `competitive-market-analysis` skill (if producing a full war map)

**Output:** Updated thesis section OR standalone competitive thesis.

**Handoff:** Standard Handoff → Phase 4

---

## Phase 4: Publication (Writer)

**Activate:** Writer to transform into publishable artifact.

**Input:**
- Synthesizer's strategic framing
- Target format (Substack article, internal memo, war map)
- Voice rules from learnings.md

**Output:** Publication-ready artifact.

**Quality Gate:** QA Pass template required. Gates: Executive Summary, Evidence Tiers, Assumption Registry, Self-Critique, Sources.

---

## Runbook Rules

1. **Always check team-knowledge/competitive/ first** — don't re-analyze what's current
2. **PM Skills Arsenal activates in Phase 3** if producing a formal competitive artifact
3. **Escalate to Prime** if Phase 2 reveals the real question isn't competitive (Context Gate failure)
4. **Time cap:** If Phase 2 exceeds 1 session, split into structural map (session 1) + strategic implications (session 2)

---

*Created: 2026-03-11.*
