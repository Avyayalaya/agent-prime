# Runbook: Morning Briefing

> **Trigger:** Daily, automated via PM Runtime (Nerve) schedule.
> **Duration:** ~5 minutes (automated pipeline)
> **Agents:** Data Scout + Signal Monitor + Intel Agent (parallel) → Context Assembly → Briefing Synthesizer
> **Infrastructure:** `repos/pm-runtime/pipelines/morning_briefing.py`

---

## Phase 1: Parallel Data Gathering

Three agents run simultaneously via `asyncio.gather()`:

| Agent | Scope | Budget | Output |
|-------|-------|--------|--------|
| **Data Scout** | `scope="session"` | 6 WorkIQ calls | Pending signals (max 8) |
| **Signal Monitor** | `scan_type="session"` | 4 WorkIQ calls | Signal digest + Team Knowledge Health |
| **Intel Agent** | Weekly (Monday only) | 0 WorkIQ (web only) | Competitive pulse |

**Context Assembly** runs in parallel with above: 12 WorkIQ calls for email/Teams/meeting context.

**Budget:** 25 total WorkIQ calls (3 reserve). Circuit breaker at 3 consecutive failures.

**Failure handling:** If any agent fails, pipeline continues. Failed agent output replaced with `[Agent X failed: reason]`.

---

## Phase 2: Synthesis

**Briefing Synthesizer** receives all agent outputs and produces a single briefing.

**Rules:**
- Lead with action, not events
- Combine + deduplicate across agents
- Flag conflicts between agents
- Under 500 words
- Max 5 Today's Priorities

**Output format:**
```
# Morning Briefing — {Date}
## What Changed Overnight
## Signals Requiring Action
## Competitive Pulse (if meaningful)
## Team Knowledge Health (if issues)
## Today's Priorities (max 5)
```

---

## Phase 3: Distribution

1. Save to `state/briefings/briefing-{DATE}-{USERNAME}.md`
2. Push Teams notification (non-blocking) via Adaptive Card
3. Log run to `state/run_log.json`

---

## Runbook Rules

1. **Never block on a single agent failure** — degrade gracefully
2. **WorkIQ budget is shared** — Data Scout doesn't get to burn all 25 calls
3. **Intel only runs on Mondays** unless `include_intel=True` is forced
4. **Briefing must be under 500 words** — curation, not aggregation

---

*Created: 2026-03-11. Maps to: `repos/pm-runtime/pipelines/morning_briefing.py`*
