# Runbook: Incident — Metric Drop

> **Trigger:** Signal Monitor or Data Scout detects a significant metric drop (>10% WoW on a key metric, or P0 bug spike).
> **Duration:** 1-3 hours (rapid response)
> **Agents:** Signal Monitor (alert) → Data Scout (deep dive) → Intel Agent (competitive check) → Prime (decision)
> **Severity Levels:** P0 (>25% drop or revenue impact), P1 (>10% drop), P2 (sustained negative trend)

---

## Phase 1: Alert & Triage (Signal Monitor)

**Trigger conditions:**
- Key metric drops >10% WoW
- P0 bug count spikes >3x baseline
- Customer feedback volume spikes >50%

**Output:** Alert signal with:
- Metric name + magnitude of change
- Time window (when did it start?)
- Affected product area
- Initial severity assessment (P0/P1/P2)

**Handoff:** Escalation Report → Prime for severity confirmation, then → Phase 2

---

## Phase 2: Deep Dive (Data Scout)

**Activate:** Data Scout with targeted scope on the affected metric.

**Investigation protocol:**
1. Pull the metric time series (daily grain, past 30 days)
2. Check for correlated metrics (did anything else move?)
3. Check ADO for recent deployments or config changes
4. Check OCV for customer reports matching the timeframe
5. Check for external factors (outage, holiday, competitor launch)

**Output:** Root cause assessment with evidence, formatted as pending signals.

**Time cap:** 30 minutes. If inconclusive, state what's known and what needs manual investigation.

---

## Phase 3: Competitive Check (Intel Agent)

**Activate:** Intel Agent with focus on whether the drop correlates with a competitive move.

**Quick scan:**
- Did a competitor launch something in the past 7 days?
- Did a competitor change pricing or packaging?
- Any analyst coverage suggesting market shift?

**Output:** Competitive context (if relevant) or "No competitive correlation found."

**Time cap:** 15 minutes.

---

## Phase 4: Decision (Prime)

**Prime receives:**
- Signal Monitor's alert
- Data Scout's root cause assessment
- Intel Agent's competitive context

**Decision matrix:**

| Severity | Action |
|----------|--------|
| P0 | Immediate escalation to system owner. Draft incident summary for stakeholders. |
| P1 | Flag in next briefing. Recommend investigation tasks for registry. |
| P2 | Monitor for 1 more week. Add to Data Scout's watch list. |

**Output:** Decision logged in dispatch.md with follow-up actions.

---

## Post-Incident

1. **If root cause found:** Update team-knowledge/ with learnings
2. **If competitive:** Trigger Competitive Analysis runbook
3. **If recurring:** Create SYS project to build automated monitoring

---

## Runbook Rules

1. **Time-boxed** — total response under 1 hour for P0, under 3 hours for P1
2. **Evidence over speculation** — state what you know vs. what you're guessing
3. **Don't fix, diagnose** — this runbook identifies the problem; fixing is a separate workstream
4. **Always check deployment correlation** — most metric drops are deployment-caused
5. **Competitive check is fast** — 15 minutes max, not a full analysis

---

*Created: 2026-03-11.*
