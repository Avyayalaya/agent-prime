# Agent Prime

**A persistent AI operating system for solving complex problems.**

AI forgets everything between sessions. Your corrections vanish. Output quality is inconsistent. None of it compounds.

Agent Prime fixes this. Seven layers of persistent infrastructure — markdown files that give AI your thinking, your memory, your standards, and a recursive loop that improves every session. It leverages AI's strengths (tireless execution, cross-domain synthesis, parallel processing) while mitigating its biggest weaknesses (no memory, no judgment without structure, generic voice). It also encodes your own corrections as permanent constraints, covering blindspots that would otherwise recur.

The architecture is goal-agnostic. The agents are composable. The system works for any domain.

---

## The Problem

A human working alone with AI hits three ceilings:

1. **Context ceiling.** Every conversation starts from zero. Yesterday's decisions, last week's corrections, the voice rules you refined over 20 iterations — all gone. You re-explain yourself endlessly.

2. **Consistency ceiling.** Without encoded rules, the same mistake happens differently each time. The wrong voice. A hallucinated citation. An analysis that anchors on existing positions instead of reasoning independently. No mechanism to prevent recurrence.

3. **Throughput ceiling.** One person can research, synthesize, write, distribute, manage projects, track deadlines, analyze industries, and build products — but not simultaneously, and not without dropping balls.

Agent Prime solves all three. Context persists across sessions. Every correction becomes a permanent rule. Parallel workstreams run simultaneously with the human reviewing and deciding.

The result: one person operating with the output, consistency, and strategic depth of a small team — with every session compounding on the last.

---

## How It Works

You define goals. The system selects agents. Agents chain into pipelines.

```
       ┌────────────────────────────────────────────────┐
       │              YOU DEFINE GOALS                  │
       │                                                │
       │  "Build authority in X"  "Analyze industry Y"  │
       │  "Ship product Z"       "Grow audience in W"   │
       └────────────────────┬───────────────────────────┘
                            │
                            ▼
       ┌────────────────────────────────────────────────┐
       │                   PRIME                        │
       │       reads goals → selects agents →           │
       │       builds pipelines → tracks progress       │
       └──────┬─────────────┬───────────────┬───────────┘
              │             │               │
              ▼             ▼               ▼
        ┌──────────┐  ┌──────────┐   ┌──────────┐
        │ Research │  │ Analysis │   │  Build   │
        │ Pipeline │  │ Pipeline │   │ Pipeline │
        │          │  │          │   │          │
        │ Scout    │  │ Industry │   │ Planner  │
        │ Synth    │  │ Analyst  │   │ Builder  │
        │ Writer   │  │ Inv.     │   │ Writer   │
        │ Connector│  │ Analyst  │   │ Connector│
        └────┬─────┘  └────┬─────┘   └────┬─────┘
             │             │              │
             └─────────────┼──────────────┘
                           ▼
                    ┌────────────┐
                    │  LEARNING  │
                    │   LAYER    │
                    │            │
                    │ every      │
                    │ output     │
                    │ feeds back │
                    └────────────┘
```

Different goals compose different agent combinations. Change your goals, change which agents activate. The system adapts to what you're pursuing.

---

## Example: From Hunch to Published Authority

You have a contrarian take about your industry. Here's what happens:

**You** → Brain dump. 15 raw thoughts in 10 minutes. Messy, unstructured, half-formed.

**Scout** → Scans 50+ sources. Returns 8 signals with hard data — 3 confirming your hunch, 2 counter-evidence (you need to address these), 3 adjacent insights you hadn't considered. Captures author names, affiliations, URLs, visual evidence opportunities.

**Synthesizer** → Finds the *structural* insight buried in your provocations + Scout's data. Not "AI trends are accelerating" but a specific mechanism with a portable name. Tests it against 9 epistemic failure modes (premature coherence, analogy capture, teleology smuggling). Produces a thesis with tiered evidence — not "AI said so" but T1-T6 sourced claims.

**Writer** → 3,000-word Substack article. In YOUR voice — learned from your corrections over dozens of sessions, not default AI prose. Compresses to LinkedIn post. Then to conference abstract. Long → short, never reversed. Every claim hyperlinked. Every chart specced with real data.

**Connector** → Maps 12 practitioners and researchers who'd care based on the thesis topic. Profiles each one — what they've published, what they care about, where they're reachable. Drafts personalized outreach. Sequences distribution: warm engagement first, then share, then pitch.

**Render** *(optional)* → Builder + Artifact Rendering skill converts the article into a self-contained interactive HTML — tabbed navigation, design system, publication-ready formatting. One invocation, no manual CSS. Opens in any browser.

**End state:** Published article with sourced claims. LinkedIn post. Conference pitch. Interactive HTML showcase. 12-person targeted distribution list with personalized outreach. Every voice rule applied. Every past correction already baked in. The system that produced this is smarter than the one that produced your last piece.

**Time:** ~2-3 sessions. The same work without the system: 2-3 weeks, and you'd skip the evidence grading, the counter-arguments, the distribution.

---

## The 11 Agents

Agents are **composable capabilities**, not a hierarchy. You don't use all 11 at once. Your goals determine which agents activate and how they chain together.

### Research Track
| Agent | What It Does |
|-------|-------------|
| **Scout** | Scans sources for signals, evidence, and market data. Captures authors, URLs, visual evidence. |
| **Synthesizer** | Combines raw signals + your experience into structured theses with evidence tiers. |
| **Writer** | Converts theses into publishable content — articles, briefs, talks — in your voice, with your rules. |
| **Connector** | Maps audiences, builds strategic relationships, distributes published work to the right people. |

### Analysis Track
| Agent | What It Does |
|-------|-------------|
| **Industry Analyst** | Deep structural mapping of industries — 9-step methodology producing ~80-90KB of structural analysis. |
| **Investment Analyst** | Multi-lens investment-grade valuation from structural maps — SIG/EV, adoption curves, comparables, stress tests. |

### Build Track
| Agent | What It Does |
|-------|-------------|
| **Planner** | 4-stage planning methodology: Excavation → Research → Architecture → Critique → Build Handoff Spec. |
| **Builder** | Executes Build Handoff Specs with mechanical reliability. The thinking was the Planner's job. |

### System Track
| Agent | What It Does |
|-------|-------------|
| **Prime** | Orchestrates everything — routes work, enforces quality gates, kills noise, manages priorities. |
| **Experimenter** | Validates claims empirically with data and prototypes before they become theses. |
| **Clerk** | Tracks commitments, deadlines, and staleness across all workstreams. |

### Cross-Connections
```
Experimenter ──→ Synthesizer      Validates claims with data
Industry Analyst ──→ Synthesizer  Structural analysis feeds theses
Planner ──→ ANY workflow          Plans route into research, analysis, or build
Clerk ──→ ALL                     Tracks deadlines across everything
```

---

## What Makes This a System (Not a Prompt Collection)

Most "agent frameworks" are prompt collections — files that tell AI what to do. Agent Prime is a **system** with persistent state, compounding intelligence, and self-correction.

### Knowledge Engineering
Agents carry four layers of encoded expertise:

| Layer | What It Does | Why It Matters |
|-------|-------------|----------------|
| **Decision Architecture** | Scoring rubrics, decision tables, multi-lens analysis | AI knows *how* to think, not just *what* to do |
| **Evidence Standards** | 6-tier evidence hierarchy, source verification, inline provenance | No hallucinated citations, no unsourced claims |
| **Calibration System** | Confidence levels, adversarial self-critique, epistemic failure modes | AI flags uncertainty instead of faking confidence |
| **Output Architecture** | Document skeletons, formatting rules, voice constraints | Consistent, publication-ready output every time |

Most people build Layer 4 (templates) and stop. The gap between generic AI and Agent Prime lives in Layers 1–3.

### Persistent Memory
Five memory mechanisms give the system continuity across sessions:

- **Identity memory** (`shared/context.md`) — who you are, how you think, your goals, your voice
- **Learnings memory** (`shared/learnings.md`) — every correction becomes a permanent rule. Append-only. Never deleted.
- **State memory** (`shared/registry.json`) — every work item, its status, its artifacts, its next action
- **Decision memory** (`prime/session_state.md`) — past decisions with context and reasoning. Prevents re-asking decided questions.
- **Artifact memory** (`agents/*/outputs/`) — every output every agent produced. Nothing is lost.

### Self-Correction Loop
Every mistake becomes a permanent rule:

1. You give feedback ("these sentences are too long")
2. The system captures the **pattern**, not just the fix ("short sentences, subject-verb-object")
3. The rule propagates to every agent that needs it
4. A Propagation Tracker ensures no learning is captured but never applied
5. The mistake cannot recur in any agent, in any future session

This is the compounding. Month 3 is unrecognizable from month 1.

### Push Architecture
Agents trigger each other. Scout findings feed the Synthesizer. Synthesizer theses feed the Writer. Writer drafts feed the Connector. Each agent writes its successor task to the dispatch queue. The loop is self-sustaining — you review and decide, the system proposes and executes.

### Skills Library
10 portable analytical methodologies — competitive analysis, metric design, narrative building, research synthesis, problem framing, and more. Any agent or human can load a skill and execute from it. No Agent Prime context required.

### Python Automation
5 scripts handle the plumbing: dashboard generation, briefing assembly, health checks, integrity validation. The system monitors itself.

## Getting Started

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (recommended) **or** [VS Code](https://code.visualstudio.com/) with [GitHub Copilot](https://github.com/features/copilot)
- Python 3.10+ (for scripts)

### Setup (5 minutes)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/avyayalaya/agent-prime.git
   cd agent-prime
   code .
   ```

2. **Run the Onboarding Agent** in VS Code Copilot Chat:
   ```
   @onboarder
   ```
   
   The Onboarding Agent interviews you (≤10 minutes) and generates:
   - Your identity and goals (`shared/context.md`)
   - Starter work items (`shared/registry.json`)
   - Your first task queue (`prime/dispatch.md`)
   - Goal → agent mappings (`prime/config.json`)

3. **Run your first workflow:**
   - [Guided Project 1: Research & Publish](getting-started/project-1-research-publish/) — 20 minutes
   - [Guided Project 2: Plan & Build](getting-started/project-2-plan-build/) — 25 minutes

4. **Or jump in directly:**
   ```
   @prime Show me the system pulse.
   ```

### Manual Setup (Alternative)

If you prefer to configure manually instead of using the Onboarding Agent:

1. Fill in `shared/context.md` — your identity, goals, voice, NDA constraints
2. Set your goals in `prime/config.json`
3. Add your first work item to `shared/registry.json`
4. Add your first task to `prime/dispatch.md`
5. Run `python meta/scripts/generate_dashboard.py`

See [QUICKSTART.md](QUICKSTART.md) for the detailed manual setup guide.

## Every Session

```
1. Generate briefing     →  python meta/scripts/generate_briefing.py
2. Read your priorities  →  prime/briefing.md
3. Invoke an agent       →  @writer, @scout, @planner, etc.
4. Agent does work       →  reads full context, applies all learnings, produces output
5. System learns         →  your corrections become permanent rules, dispatch updated
```

## Repository Structure

```
agent-prime/
├── .github/copilot-instructions.md    ← System rules (auto-injected)
├── agents/                            ← 11 agent prompts
│   ├── prime/prompt.md                ← Orchestrator
│   ├── scout/prompt.md                ← Signal scanning
│   ├── synthesizer/prompt.md          ← Thesis building
│   ├── writer/prompt.md               ← Content production
│   ├── planner/prompt.md              ← 4-stage planning
│   ├── builder/prompt.md              ← Build execution
│   ├── onboarder/prompt.md            ← Setup wizard
│   └── ...                            ← + 5 more agents
├── shared/
│   ├── context.md                     ← Your identity & goals (fill this in)
│   ├── registry.json                  ← All work items
│   ├── learnings.md                   ← Accumulated corrections
│   ├── toolkits/skills/               ← 10 analytical methodologies
│   └── ...
├── prime/
│   ├── dashboard.md                   ← Auto-generated status view
│   ├── dispatch.md                    ← Task queue
│   └── config.json                    ← Agent cadences & goals
├── meta/scripts/                      ← Python automation
├── examples/startup-founder/          ← Fully worked example
└── getting-started/                   ← Guided projects
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design.

## Example: Startup Founder

The `examples/startup-founder/` directory shows a fully configured system for Maya Chen, a Series A startup CEO. It includes:
- Complete `context.md` with identity, goals, and voice rules
- Seeded registry with 6 real work items across 3 goals
- Active dispatch queue with 4 agent tasks
- Goal → agent mappings

## Requirements

| Component | Required | Optional |
|-----------|----------|----------|
| Claude Code **or** VS Code + GitHub Copilot | ✅ | |
| Python 3.10+ | ✅ (for scripts) | |
| LM Studio | | For local model dispatch |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: new skills, agent improvements, and documentation fixes welcome. Keep PRs focused.

## License

MIT. See [LICENSE](LICENSE).
