# Agent Prime

**A persistent AI operating system that gets better every time you use it.**

You ask AI to analyze an industry. It produces 800 words of generic overview. Agent Prime produces 1,328 lines of structural analysis with 13 frameworks, 91 citations, and a stress-tested investment watchlist — from the same one-sentence input.

The difference isn't the model. It's the system.

---

## Start Here

If you're new, don't start by reading the whole architecture.

| Path | What you get | How to start |
|------|---------------|--------------|
| **Try the live preview** | See the app-shaped direction in your browser | [Open the hosted workspace preview](https://avyayalaya.github.io/agent-prime/workspace-mvp/) |
| **Run first-time setup** | Choose preview, quick trial, or guided onboarding from one entry point | Clone the repo, then run `./install.sh`, `.\install.ps1`, or `python meta/scripts/first_run.py` |
| **Load a prebuilt example** | Start with a fully configured founder system and inspect how the pieces fit | Run the first-time setup flow and choose `quick-trial` |

**Recommended first move:**

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py
```

Use the Python command everywhere, or the platform wrappers if you prefer:
- macOS/Linux: `./install.sh`
- PowerShell: `.\install.ps1`

---

## What Agent Prime Does

Agent Prime is seven layers of persistent infrastructure — markdown files that give AI your thinking model, your memory, your standards, and a recursive loop that gets smarter every session. It leverages AI's strengths (tireless execution, cross-domain synthesis, parallel processing) while mitigating its biggest weaknesses (no memory, no judgment without structure, generic voice). Every correction you make becomes a permanent rule, applied automatically across all agents, in every future session.

The architecture is goal-agnostic. The agents are composable. The system works for any domain.

**Three ceilings it breaks:**

| Ceiling | Without Agent Prime | With Agent Prime |
|---------|-------------------|-----------------|
| **Context** | Every session starts from zero | 42+ decisions, 14+ voice rules, 11+ design patterns — all persistent |
| **Consistency** | Same mistakes, different sessions | Every correction becomes a permanent rule across all agents |
| **Throughput** | One task, one thread | Parallel workstreams: research, analysis, writing, building |

---

## See What It Produces

Real pipeline outputs. One sentence in, pages of structured analysis out.

### "Map the AI robotics industry for investment"

**Pipeline:** Scout → Industry Analyst → Investment Analyst
**Output:** 1,328 lines | 13 frameworks | 91 citations

8-layer value chain decomposition, bottleneck analysis with severity scores, 6 deployment scenarios with probability weights, 4-lens investment valuation, stress-tested watchlist with exit rules.

Raw AI on the same question: ~800 words of generic overview.

> [View the full pipeline](examples/ai-robotics-industry/) | [See the raw AI comparison](examples/ai-robotics-industry/comparison.md)

### "Build me a complete product strategy"

**Pipeline:** Problem Framing → Discovery Research → Competitive Analysis → Metric Design → Spec Writing → Narrative Building
**Output:** 2,399 lines across 6 artifacts | 30+ frameworks | 70+ citations

Six PM skills chained together. Each artifact feeds the next — problem framing shapes research, research informs competitive analysis, analysis drives metrics, metrics anchor the spec, spec feeds positioning. One sentence of input produced a complete product strategy across 6 interconnected documents.

> [View the full pipeline](examples/product-strategy-figma/) | [See the raw AI comparison](examples/product-strategy-figma/comparison.md)

### "Level up my PM team for the AI era"

**Pipeline:** Scout → Synthesizer → Planner → Builder
**Output:** 1,342 lines across 4 artifacts | 10 sourced signals | 4-phase implementation

Scout gathered 10 signals (MIT, Stanford, HBS studies + Stripe, Figma, Linear examples). Synthesizer produced a thesis: "The PM Skill Stack is Inverting." Planner designed a 4-layer team OS. Builder produced a phased implementation plan with day-by-day scheduling.

> [View the full pipeline](examples/pm-team-performance/) | [See the raw AI comparison](examples/pm-team-performance/comparison.md)

### The Pattern

| | Raw AI | Agent Prime |
|---|---|---|
| **Input** | Same question | Same question |
| **Output** | 500-800 words | 1,300-2,400 lines (30-50 pages) |
| **Frameworks applied** | 0 | 13-30+ |
| **Evidence citations** | 0 | 70-91 |
| **Actionable deliverables** | "Do more research" | Watchlists, specs, implementation plans |

---

## The Seven Layers

Each layer is independently useful. Together, they compound.

| Layer | What It Does | Files |
|-------|-------------|-------|
| **01 Identity** | Encodes who you are — thinking patterns, judgment heuristics, epistemic guardrails | `shared/context.md` |
| **02 Memory** | Every correction compounds. Fix something once, it propagates everywhere. | `shared/learnings.md`, `shared/dependency_map.md` |
| **03 Agents** | 11 specialized agents — scout, synthesizer, writer, planner, builder, and more | `agents/*/prompt.md` |
| **04 Orchestration** | Registry tracks work items, dispatch queue sequences tasks, briefings surface priorities | `shared/registry.json`, `prime/dispatch.md`, `prime/dashboard.md` |
| **05 Skills** | 12 PM methodologies — competitive analysis, metric design, problem framing, and more | `shared/toolkits/skills/` |
| **06 Craft** | Design system + templates that turn markdown into publication-quality HTML | `agents/builder/templates/`, `assets/style.css` |
| **07 The Loop** | The recursive mechanism — learnings propagate, agents chain, the system audits itself | Emerges from layers 1-6 |

---

## The 11 Agents

Composable capabilities, not a hierarchy. Your goals determine which agents activate.

| Track | Agent | What It Does |
|-------|-------|-------------|
| **Research** | **Scout** | Scans sources for signals, evidence, market data with provenance |
| | **Synthesizer** | Combines raw signals into structured theses with evidence tiers |
| | **Writer** | Converts theses into publishable content in your voice |
| | **Connector** | Maps audiences, builds relationships, distributes work |
| **Analysis** | **Industry Analyst** | 9-step structural mapping of industries (~80-90KB output) |
| | **Investment Analyst** | Multi-lens valuation — SIG/EV, adoption curves, comparables, stress tests |
| **Build** | **Planner** | 4-stage methodology: Excavation → Research → Architecture → Critique |
| | **Builder** | Executes Build Handoff Specs with mechanical reliability |
| **System** | **Prime** | Orchestrates everything — routes work, enforces quality, kills noise |
| | **Experimenter** | Validates claims empirically before they become theses |
| | **Clerk** | Tracks commitments, deadlines, and staleness across all workstreams |

Plus an **Onboarder** agent that interviews you and configures the system in ≤10 minutes.

---

## The 12 Skills

Each skill encodes how an expert thinks about a problem — frameworks, failure modes, quality gates, adversarial self-critique. Any agent can load any skill. Agent Prime scored 93% on structured benchmarks vs. 45% baseline (same model, no skill).

### Analysis & Intelligence
| Skill | Frameworks | What It Produces |
|-------|-----------|-----------------|
| **Competitive Market Analysis** | 7 Powers, Aggregation Theory, Wardley, JTBD, Blue Ocean, Crossing the Chasm | Competitive War Map with evidence tiers |
| **Discovery Research** | Evidence Triangulation, Interview Analysis, Signal vs Noise, Research Gap Mapping | Research Synthesis with confidence ratings |
| **Problem Framing** | Problem Definition Canvas, 5 Whys, JTBD, Opportunity Sizing, ICE/RICE | Structured Problem Statement with constraints |

### Strategy & Planning
| Skill | Frameworks | What It Produces |
|-------|-----------|-----------------|
| **Product Strategy** | Vision-to-Roadmap, Portfolio Prioritization, Strategic Bets, Platform vs Product | Strategy Document with evidence-backed bets |
| **Go-to-Market Strategy** | Launch Sequencing, Channel Strategy, Adoption Flywheel, Market Timing | GTM Plan with channel-specific tactics |
| **Pricing & Packaging** | Value Metric ID, Tier Design, WTP Analysis, Competitive Pricing | Pricing Model with expansion paths |

### Measurement & Specification
| Skill | Frameworks | What It Produces |
|-------|-----------|-----------------|
| **Metric Design & Experimentation** | NSM Rubrics, Goodhart Countermeasures, A/B Design, Retention Cohorts | Measurement System with experiment designs |
| **Specification Writing** | Outcome-First, AC Taxonomy, Scope Boundary, Executor Context | Zero-Question Spec engineers can build from |
| **Stakeholder Alignment** | Stakeholder Mapping, Influence Strategy, Decision Rights, Escalation Frameworks | Alignment Plan with stakeholder profiles |

### Communication & Distribution
| Skill | Frameworks | What It Produces |
|-------|-----------|-----------------|
| **Narrative Building** | Narrative Arc, Dunford Positioning, Why Now, Audience Adaptation | Strategic Narrative with objection responses |
| **Executive Writing** | Board Memo Structure, Decision Documents, Brevity-with-Depth | Executive Documents for 5-minute decisions |
| **Multi-Channel Publishing** | Long-to-Short Compression, Platform Adaptation, Content Atomization | 8 format-native pieces from one thesis |

---

## What Makes This a System (Not a Prompt Collection)

### Knowledge Engineering
Agents carry four layers of encoded expertise:

| Layer | What It Does | Why It Matters |
|-------|-------------|----------------|
| **Decision Architecture** | Scoring rubrics, decision tables, multi-lens analysis | AI knows *how* to think, not just *what* to do |
| **Evidence Standards** | 6-tier hierarchy, source verification, inline provenance | No hallucinated citations, no unsourced claims |
| **Calibration System** | Confidence levels, adversarial self-critique, 9 epistemic failure modes | AI flags uncertainty instead of faking confidence |
| **Output Architecture** | Document skeletons, formatting rules, voice constraints | Consistent, publication-ready output every time |

Most people build Layer 4 (templates) and stop. The gap between generic AI and Agent Prime lives in Layers 1-3.

### Self-Correction Loop
1. You give feedback ("these sentences are too long")
2. The system captures the **pattern** ("short sentences, subject-verb-object")
3. The rule propagates to every agent that needs it
4. A Propagation Tracker ensures no learning is captured but never applied
5. The mistake cannot recur in any agent, in any future session

Month 3 is unrecognizable from month 1.

### Push Architecture
Agents trigger each other. Scout findings feed the Synthesizer. Synthesizer theses feed the Writer. Each agent writes successor tasks to the dispatch queue. You review and decide. The system proposes and executes.

---

## Getting Started

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (recommended) **or** [VS Code](https://code.visualstudio.com/) with [GitHub Copilot](https://github.com/features/copilot)
- Python 3.10+ (for automation scripts)

### Fastest Path (Recommended)

Clone the repo and run the guided first-run command:

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py
```

Platform wrappers:
- macOS/Linux: `./install.sh`
- PowerShell: `.\install.ps1`

The first-run flow lets you choose:
- **preview** — open the workspace MVP locally and use the hosted preview link
- **quick-trial** — load the startup-founder example, generate the dashboard, and verify setup
- **onboard** — run `@onboarder`, then finish setup and verification

### Product-Shell Preview (5 min)

If you want to see the plug-and-play direction before working directly with prompts and files:

- Hosted preview: `https://avyayalaya.github.io/agent-prime/workspace-mvp/`
- Local clone: `workspace-mvp/index.html`

This static preview shows what Agent Prime could feel like as an app shell:
- guided onboarding
- 3 starter workflows
- visible run state
- artifact review with approvals and revisions
- saved rules
- browser-local persistence, export, and reset

It is a product-shell demo, not a replacement for the markdown-first system in the rest of the repo.

### Path A: Automated Setup (15 min)

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py --mode onboard
```

Then run the Onboarding Agent:
```
@onboarder
```

It interviews you and generates your identity, goals, starter registry, and task queue. Then run your first workflow:
- [Guided Project 1: Research & Publish](getting-started/project-1-research-publish/) — 20 minutes
- [Guided Project 2: Plan & Build](getting-started/project-2-plan-build/) — 25 minutes

### Path B: Manual Setup (30 min)

1. Fill in `shared/context.md` — your identity, goals, voice, constraints
2. Set your goals in `prime/config.json`
3. Add your first work item to `shared/registry.json`
4. Add your first task to `prime/dispatch.md`
5. Run `python meta/scripts/generate_dashboard.py`

See [QUICKSTART.md](QUICKSTART.md) for the detailed guide.

### Path C: Quick Trial (5 min)

Load the startup-founder example and let the first-run flow wire the system:
```bash
python meta/scripts/first_run.py --mode quick-trial --yes
```

### Verify Setup

```bash
python meta/scripts/verify_setup.py
```

### Every Session

```
1. Generate briefing     →  python meta/scripts/generate_briefing.py
2. Read your priorities  →  prime/briefing.md
3. Invoke an agent       →  @writer, @scout, @planner, etc.
4. Agent does work       →  reads full context, applies all learnings, produces output
5. System learns         →  your corrections become permanent rules, dispatch updated
```

---

## Repository Structure

```
agent-prime/
├── CLAUDE.md                             ← Claude Code system instructions (auto-loaded)
├── .github/copilot-instructions.md       ← VS Code Copilot instructions (auto-injected)
├── agents/                               ← 11 agent prompts + onboarder
│   ├── prime/prompt.md                   ← Orchestrator
│   ├── scout/prompt.md                   ← Signal scanning
│   ├── synthesizer/prompt.md             ← Thesis building
│   ├── writer/prompt.md                  ← Content production
│   ├── planner/prompt.md                 ← 4-stage planning
│   ├── builder/prompt.md                 ← Build execution
│   ├── industry_analyst/prompt.md        ← Structural mapping
│   ├── investment_analyst/prompt.md      ← Investment analysis
│   ├── connector/prompt.md               ← Distribution
│   ├── experimenter/prompt.md            ← Validation
│   ├── clerk/prompt.md                   ← Tracking
│   └── onboarder/prompt.md              ← Setup wizard
├── shared/
│   ├── context.md                        ← Your identity & goals
│   ├── registry.json                     ← All work items (single source of truth)
│   ├── learnings.md                      ← Accumulated corrections (append-only)
│   ├── dependency_map.md                 ← Change propagation registry
│   └── toolkits/skills/                  ← 12 PM methodologies (~1,200 lines each)
├── prime/
│   ├── dashboard.md                      ← Auto-generated status view
│   ├── briefing.md                       ← Session-start priorities
│   ├── dispatch.md                       ← Task queue with successor rules
│   └── config.json                       ← Agent cadences & goal mappings
├── workspace-mvp/                        ← Plug-and-play product-shell prototype
│   ├── index.html                        ← Guided workspace experience
│   └── assets/                           ← Local JS + styling for the prototype
├── meta/scripts/                         ← Python automation (6 scripts)
│   └── first_run.py                      ← Guided entry point for preview / trial / onboarding
├── install.sh                            ← macOS/Linux first-run wrapper
├── install.ps1                           ← PowerShell first-run wrapper
├── examples/
│   ├── startup-founder/                  ← Fully configured example system
│   ├── ai-robotics-industry/             ← Pipeline: investment analysis (1,328 lines)
│   ├── product-strategy-figma/           ← Pipeline: 6-skill product strategy (2,399 lines)
│   └── pm-team-performance/              ← Pipeline: team transformation (1,342 lines)
└── getting-started/                      ← Guided projects (20-25 min each)
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design.

---

## Examples

### Pipeline Examples (Real Output)

Three complete pipeline traces showing input → agent chain → output, with raw AI comparisons:

| Example | Input | Agents | Output | Lines |
|---------|-------|--------|--------|-------|
| [AI Robotics Industry](examples/ai-robotics-industry/) | 1 sentence | Scout → Industry → Investment | Value chain + valuation + watchlist | 1,328 |
| [Product Strategy](examples/product-strategy-figma/) | 1 sentence | 6 PM skills chained | 6 interconnected artifacts | 2,399 |
| [PM Team Performance](examples/pm-team-performance/) | 2 sentences | Scout → Synth → Plan → Build | Thesis + team OS + implementation | 1,342 |

### Worked Example: Startup Founder

The `examples/startup-founder/` directory shows a fully configured system for Maya Chen, a Series A startup CEO:
- Complete `context.md` with identity, goals, and voice rules
- Seeded registry with 6 work items across 3 goals
- Active dispatch queue with 4 agent tasks
- Goal → agent mappings

Clone this to skip manual setup and explore the system immediately.

---

## Requirements

| Component | Required | Notes |
|-----------|----------|-------|
| Claude Code **or** VS Code + GitHub Copilot | Yes | Claude Code recommended — auto-loads CLAUDE.md |
| Python 3.10+ | Yes | For automation scripts |
| LM Studio | Optional | For local model dispatch |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills, agent improvements, and documentation fixes welcome. Keep PRs focused.

## License

MIT. See [LICENSE](LICENSE).
