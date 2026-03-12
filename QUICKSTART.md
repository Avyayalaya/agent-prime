# Quickstart Guide

> Get Agent Prime running in 30 minutes. Two paths: automated (recommended) or manual.

---

## Path A: Automated Setup (Recommended)

### Step 1: Clone and Open (2 min)

```bash
git clone https://github.com/YOUR_USERNAME/agent-prime.git
cd agent-prime
code .
```

### Step 2: Run the Onboarding Agent (10 min)

Open VS Code Copilot Chat and type:

```
@onboarder
```

The agent will:
1. Ask you 10-12 questions about your identity, goals, and working style
2. Generate your personalized `shared/context.md`
3. Seed `shared/registry.json` with 3-5 starter work items
4. Set up your dispatch queue in `prime/dispatch.md`
5. Map your goals to agents in `prime/config.json`

### Step 3: Verify Setup (2 min)

```bash
python meta/scripts/generate_dashboard.py
python meta/scripts/integrity_check.py
```

Open `prime/dashboard.md` — you should see your work items and a system pulse.

### Step 4: Run a Guided Project (20 min)

Pick one:
- **Research & Publish** (`getting-started/project-1-research-publish/`): Walk through Scout → Synthesizer → Writer on a topic you care about. Output: a real draft article.
- **Plan & Build** (`getting-started/project-2-plan-build/`): Walk through the 4-stage Planner methodology on a project you want to execute. Output: a real plan.

---

## Path B: Manual Setup

### Step 1: Configure Your Identity

Open `shared/context.md` and fill in each section. See `examples/startup-founder/context.md` for a fully worked example.

**Required sections:**
- Identity (name, role, organization)
- Career Arc (2-3 sentences on your path)
- Unique Lens (what you see that others miss)
- Voice & Style (how you write, hard rules)
- NDA Constraints (what's off-limits)
- Goals (2-3 strategic goals with success metrics)

**Keep universal sections as-is:**
- Reasoning Operations (6 types)
- Epistemic Failure Modes (9 guardrails)

### Step 2: Set Your Goals

Edit `prime/config.json`:

```json
{
  "goals": {
    "your_goal_1": {
      "name": "Goal Name",
      "agents": ["scout", "synthesizer", "writer"],
      "description": "What success looks like"
    }
  }
}
```

Map each goal to the agents that serve it:

| Goal type | Agents to assign |
|-----------|-----------------|
| Career/positioning | scout, synthesizer, writer, connector |
| Investment/wealth | scout, industry_analyst, investment_analyst |
| Thought leadership | writer, connector, planner, builder |
| Product building | planner, builder, experimenter |

### Step 3: Add Your First Work Item

Edit `shared/registry.json`:

```json
{
  "items": [
    {
      "id": "THS-001",
      "type": "THS",
      "title": "Your first thesis or project",
      "status": "backlog",
      "priority": "P0",
      "owner": "user",
      "created": "2026-03-01",
      "updated": "2026-03-01",
      "next_action": "Scout: scan for signals on [your topic]"
    }
  ]
}
```

Work item types: `THS` (thesis), `BLD` (build), `STR` (strategy), `EVT` (event), `TSK` (task), `TLK` (toolkit), `EXP` (exploration), `PRG` (program), `SYS` (system).

### Step 4: Queue Your First Task

Edit `prime/dispatch.md`:

```markdown
## Q-001: [Your first task]
- **Agent:** scout
- **Priority:** P0
- **Status:** queued
- **Input:** [What the agent needs to know]
- **Output:** [What you expect back]
```

### Step 5: Generate Dashboard

```bash
python meta/scripts/generate_dashboard.py
```

### Step 6: Start Working

In VS Code Copilot Chat:

```
@prime Show me the system pulse. What should I work on?
```

---

## Daily Usage Pattern

```
Morning:
  1. python meta/scripts/generate_briefing.py    # What's on your plate
  2. Read prime/briefing.md                       # Priorities + dispatch queue
  3. Invoke the agent you need                    # @writer, @scout, @planner, etc.

Working:
  4. Agent reads context + learnings automatically
  5. Agent produces output
  6. You review, correct, approve
  7. Corrections captured in shared/learnings.md   # System gets smarter

End of session:
  8. python meta/scripts/generate_dashboard.py    # Update views
  9. python meta/scripts/integrity_check.py       # Health check
```

---

## Agent Invocations

Quick reference for invoking each agent:

| Agent | Invocation | Example |
|-------|-----------|---------|
| Prime | `@prime` | "Show me the system pulse." |
| Scout | `@scout` | "Scan for signals on AI code review tools." |
| Synthesizer | `@synthesizer` | "Build a thesis from these signals." |
| Writer | `@writer` | "Convert THS-001 into a Substack article." |
| Planner | `@planner` | "Plan my Series B narrative." |
| Builder | `@builder` | "Execute PLN-001." |
| Connector | `@connector` | "Build outreach to [person]." |

See `prime/invocations.md` for full invocation templates.

---

## Troubleshooting

**"The agent doesn't know who I am."**
→ `shared/context.md` is empty or not filled in. Run `@onboarder` or fill it manually.

**"Dashboard shows no items."**
→ `shared/registry.json` has no items. Add work items or run `@onboarder`.

**"Scripts fail with import errors."**
→ Ensure Python 3.10+ is installed and in your PATH.

**"Agent output is generic / doesn't match my voice."**
→ Check `shared/context.md` Voice section. Add specific hard rules. Over time, corrections in `shared/learnings.md` will tune the output.
