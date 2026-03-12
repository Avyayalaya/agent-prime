# Architecture

> How Agent Prime works under the hood. Read this if you want to understand why the system is designed the way it is, extend it, or build your own agents.

---

## Design Principles

1. **Composable agents, not a hierarchy.** Each agent is a self-contained capability. They compose into workflows but don't depend on each other to function. You can use the Writer without the Scout.

2. **State lives in files, not memory.** LLM conversations are ephemeral. Agent Prime stores all state in human-readable files (JSON, Markdown) so nothing is lost between sessions. The registry is the single source of truth.

3. **Learning is permanent.** Every correction the user makes is captured in `shared/learnings.md`. These corrections become hard constraints that apply to all future agent outputs. The system gets smarter with use.

4. **Agents trigger agents.** The dispatch queue (`prime/dispatch.md`) creates a push system where completing one agent's task automatically queues the next. Scout findings trigger the Synthesizer. Mature theses trigger the Writer.

5. **Quality is visible.** Every substantial output includes a Quality Check section. Every session starts with a health check. Epistemic failure modes are explicitly checked. Quality verification is never invisible.

---

## Core Architecture

```
┌─────────────────────────────────────────────────┐
│                  VS Code + Copilot               │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  @scout   │  │ @writer  │  │ @planner │ ...  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
│       │              │              │             │
│       ▼              ▼              ▼             │
│  ┌────────────────────────────────────────┐      │
│  │     .github/copilot-instructions.md    │      │
│  │     (25 system rules, auto-injected)   │      │
│  └────────────────┬───────────────────────┘      │
│                   │                               │
│  ┌────────────────▼───────────────────────┐      │
│  │          Agent Prompt (prompt.md)       │      │
│  │  + shared/context.md (identity)        │      │
│  │  + shared/learnings.md (constraints)   │      │
│  │  + shared/registry.json (state)        │      │
│  └────────────────┬───────────────────────┘      │
│                   │                               │
│                   ▼                               │
│            Agent produces output                  │
│            → Updates state files                  │
│            → Queues next agent task               │
│            → Captures learnings                   │
└─────────────────────────────────────────────────┘
```

### Information Flow

```
User invokes agent
    → Copilot reads copilot-instructions.md (auto-injected)
    → Agent reads its prompt.md (methodology + constraints)
    → Agent reads context.md (identity + goals)
    → Agent reads learnings.md (accumulated corrections)
    → Agent reads relevant state files (registry, theses, dispatch)
    → Agent produces output
    → Output stored in appropriate directory
    → Registry updated (write-ahead rule)
    → Dispatch queue updated (successor task queued)
    → If feedback given → captured in learnings.md
```

---

## State System

### Registry (`shared/registry.json`)

The single source of truth for all work items. Everything tracked by Agent Prime has an entry here.

```json
{
  "items": [
    {
      "id": "THS-001",          // Unique ID (type prefix + number)
      "type": "THS",            // THS, BLD, STR, EVT, TSK, TLK, EXP, PRG, SYS
      "title": "...",           // Human-readable title
      "status": "developing",   // backlog, planning, in_progress, developing, done, killed, parked
      "priority": "P0",         // P0 (critical), P1 (important), P2 (nice-to-have)
      "owner": "user",          // user, or an agent name
      "created": "2026-03-01",
      "updated": "2026-03-01",
      "next_action": "...",     // What happens next (feeds dispatch queue)
      "goal": "Build"           // Which user goal this serves
    }
  ]
}
```

### Dispatch Queue (`prime/dispatch.md`)

Tasks queued for agent execution. Each entry has a priority, assigned agent, inputs/outputs.

Agents trigger each other via successor rules:

| Completing Agent | Successor |
|-----------------|-----------|
| Scout | Synthesizer (if signal is thesis-worthy) |
| Synthesizer | Writer (if thesis is mature) |
| Writer | Connector (if artifact is publishable) |
| Planner | Builder (when spec is complete) |
| Builder | Writer or Connector (when build is done) |

### Learnings (`shared/learnings.md`)

Append-only log of user corrections. Categories:
- **Voice (V):** Writing style corrections
- **Content (C):** Framing or substance corrections
- **Process (P):** Workflow corrections
- **Quality (Q):** Output quality corrections
- **Build (B):** Build execution patterns
- **Agent Design (AD):** Agent architecture patterns

Each learning becomes a permanent constraint. Agents read this at every session start.

### Dashboard (`prime/dashboard.md`)

Auto-generated from the registry by `python meta/scripts/generate_dashboard.py`. Shows:
- System pulse (priority, staleness, tasks)
- Pipeline view (all active items by status)
- User's plate (tasks assigned to user)

---

## Agent Architecture

### Anatomy of an Agent Prompt

Every agent prompt follows the same structure:

```markdown
# Agent Name — Purpose

## Context Verification Gate
| File | Required | Check |
...

## Methodology
Step 1: ...
Step 2: ...

## Output Format
[Explicit output structure]

## Quality Checks
[What to verify]

## Constraints
[Hard rules from learnings.md]
```

### Context Verification Gate

Before producing ANY output, every agent verifies it has access to required files. This prevents "garbage in, garbage out" — the #1 failure mode in LLM-based systems.

If a required file is missing, the agent stops and asks. It never proceeds with degraded context.

### Agent Composition

Agents are designed to compose. The output of one agent becomes the input of the next:

| Workflow | Agents | Each step's output |
|----------|--------|-------------------|
| Research → Publish | Scout → Synthesizer → Writer → Connector | Signals → Thesis → Article → Distribution |
| Investment Research | Scout → Industry Analyst → Investment Analyst | Signals → Structural Map → Investment Analysis |
| Plan → Build | Planner (4 stages) → Builder | Excavation → Research → Architecture → Critique → Build |

---

## Python Scripts

| Script | Purpose | When to run |
|--------|---------|-------------|
| `generate_briefing.py` | Generates session briefing with priorities | Session start |
| `generate_dashboard.py` | Regenerates dashboard + projects index | Session start + after registry changes |
| `integrity_check.py` | Health check: staleness, broken paths, crashes | Session start or when suspicious |
| `dispatcher.py` | Automated agent dispatch via LLM API | Advanced: batch processing tasks |
| `check_skill_compliance.py` | Validates skill files against spec | When creating/modifying skills |

---

## Skills System

Skills are domain-specific methodologies stored in `shared/toolkits/skills/`. Each skill follows a standard format:

```markdown
# Skill Name
metadata:
  domain: competitive-analysis
  valid_until: 2027-01-01
  
## Method
Step-by-step methodology

## Output Format
Expected output structure

## Quality Markers
What good output looks like
```

Agents check `shared/toolkits/skills/README.md` before starting substantive tasks. If a relevant skill exists, the agent follows its methodology.

---

## System Rules

The 25 rules in `.github/copilot-instructions.md` enforce:
- Context verification before output
- Voice consistency
- NDA compliance
- Change propagation (updating dependent files)
- Agent completion protocol (queuing successor tasks)
- Learning capture (corrections become constraints)
- Plan-before-build discipline
- Epistemic rigor (failure mode checks)

See `.github/copilot-instructions.md` for the full list.

---

## Extending Agent Prime

### Adding a New Agent

1. Create `agents/your_agent/prompt.md`
2. Follow the prompt structure: Gate → Methodology → Output Format → Quality Checks
3. Add the agent to the capability table in `copilot-instructions.md`
4. Map it to relevant goals in `prime/config.json`

### Adding a New Skill

1. Follow the spec in `shared/toolkits/skill_file_spec.md`
2. Create the skill file in `shared/toolkits/skills/`
3. Add it to `shared/toolkits/skills/README.md`
4. Run `python meta/scripts/check_skill_compliance.py` to validate

### Adding a New Project Type

1. Add the type prefix to `shared/projects_sync/prompt.md`
2. Create a project folder using the template
3. Add to `projects/README.md`
