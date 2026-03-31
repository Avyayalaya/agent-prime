# Quickstart Guide

> Four ways to get started. The easiest path is now one guided first-run command.

| Path | Time | Best for |
|------|------|----------|
| **0: Product shell** | 5 min | People who want to see the app-shaped direction first |
| **A: Automated** | 15 min | First-time users who want a guided setup |
| **B: Manual** | 30 min | Users who want full control over configuration |
| **C: Quick trial** | 5 min | Skeptics who want to see it work before investing time |

---

## Start Here First

Clone the repo and run the first-run guide:

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py
```

Platform wrappers:
- macOS/Linux: `./install.sh`
- PowerShell: `.\install.ps1`

The guide offers three modes:
- `preview` — opens the workspace MVP and points you to the hosted preview
- `quick-trial` — loads the startup-founder example, generates the dashboard, and verifies the repo
- `onboard` — tells you when to run `@onboarder`, then finishes generation + verification

If you already know the path you want, use the direct options below.

---

## Path 0: Product-Shell Preview (5 minutes)

Want to see the app-shaped version of Agent Prime before you work directly with prompts and files?

Open the hosted preview in your browser:

`https://avyayalaya.github.io/agent-prime/workspace-mvp/`

If you're working from a local clone, `workspace-mvp/index.html` is the same experience offline.

What this preview includes:
- guided onboarding instead of editing `shared/context.md`
- 3 starter workflows instead of raw agent syntax
- a run studio with visible step states
- artifact review with `Approve`, `Request Revision`, and `Save as Rule`
- browser-local persistence plus export/reset

Important: this is a static prototype that demonstrates the plug-and-play product direction. It does **not** replace the main markdown-based system documented below.

---

## Path C: Quick Trial (5 minutes)

Want to see Agent Prime work before configuring it for yourself? Use the pre-built startup-founder example.

### Step 1: Clone the repo

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
```

### Step 2: Load the example

```bash
python meta/scripts/first_run.py --mode quick-trial --yes
```

### Step 3: Run the system

Open your AI coding environment (Claude Code or VS Code Copilot Chat) and try:

```
Show me the system pulse from prime/dashboard.md
```

You now have a working system with 6 real work items, 4 queued tasks, and 3 goals. Poke around. Run `@scout` on a topic. When you're ready to configure it for yourself, switch to Path A or B.

### Step 4: Verify setup (optional)

```bash
python meta/scripts/verify_setup.py
```

---

## Path A: Automated Setup (Recommended)

### Step 1: Clone and Open (2 min)

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py --mode onboard
```

### Step 2: Open the repo in your AI coding environment (10 min)

```bash
code .
```

Then run the Onboarding Agent:

`@onboarder`

The agent will:
1. Ask you 10-12 questions about your identity, goals, and working style
2. Generate your personalized `shared/context.md`
3. Seed `shared/registry.json` with 3-5 starter work items
4. Set up your dispatch queue in `prime/dispatch.md`
5. Map your goals to agents in `prime/config.json`

### Step 3: Return to the first-run flow and finish verification (2 min)

After onboarding finishes, go back to the terminal where `first_run.py` is running and press Enter. It will generate the dashboard and run verification for you.

Open `prime/dashboard.md` — you should see your work items and a system pulse.

### Step 4: Run a Guided Project (20 min)

Pick one:
- **Research & Publish** (`getting-started/project-1-research-publish/`): Walk through Scout → Synthesizer → Writer on a topic you care about. Output: a real draft article.
- **Plan & Build** (`getting-started/project-2-plan-build/`): Walk through the 4-stage Planner methodology on a project you want to execute. Output: a real plan.

---

## Path B: Manual Setup

### Step 1: Configure Your Identity

Open `shared/context.md` and fill in each section. The file now explains what gets built on first run and what you should add manually if you skip onboarding. See `examples/startup-founder/context.md` for a fully worked example.

**Required sections:**
- Identity (name, role, organization)
- Goals (2-3 strategic goals with success metrics)
- Voice & Style (how you write, hard rules)
- NDA Constraints (what's off-limits)
- Unique Lens / Fields You Draw From
- Decision Patterns or Guardrails if they matter for your work

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

Work item types: `THS` (thesis), `BLD` (build), `STR` (strategy), `EVT` (event), `TSK` (task), `TLK` (toolkit), `EXP` (experiment), `PRG` (program), `SYS` (system).

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
