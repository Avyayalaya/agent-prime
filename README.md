# Agent Prime

**A persistent AI operating system built entirely from markdown files.**

Seven architectural layers. Thirteen specialized agents. A recursive improvement loop that compounds every session. Zero dependencies.

| Agents | Skills | Guardrails | Workflows | Learnings | Dependencies |
|--------|--------|------------|-----------|-----------|--------------|
| 13     | 12     | 7          | 4         | 100+      | 0            |

---

## The Problem

AI has three ceilings that no amount of model intelligence fixes.

| Ceiling | Without Agent Prime | With Agent Prime |
|---------|---------------------|------------------|
| **Context** | Every session starts from zero | 42+ decisions, 14+ voice rules, 11+ design patterns -- all persistent |
| **Consistency** | Same mistakes, different sessions | Every correction becomes a permanent rule across all agents |
| **Throughput** | One task, one thread | Parallel workstreams: research, analysis, writing, building |

Agent Prime is seven layers of persistent infrastructure -- markdown files that encode your thinking model, your memory, your standards, and a recursive loop that gets smarter every session. Every correction you make becomes a permanent rule, applied automatically across all agents, in every future session.

---

## See What It Produces

Real pipeline outputs. One sentence in, structured analysis out.

### "Map the AI robotics industry for investment"

**Pipeline:** Scout --> Industry Analyst --> Investment Analyst
**Output:** 1,328 lines | 13 frameworks | 91 citations

8-layer value chain decomposition, bottleneck analysis with severity scores, 6 deployment scenarios with probability weights, 4-lens investment valuation, stress-tested watchlist with exit rules.

Raw AI on the same question: ~800 words of generic overview.

> [View the full pipeline](examples/ai-robotics-industry/) | [See the raw AI comparison](examples/ai-robotics-industry/comparison.md)

### "Build me a complete product strategy"

**Pipeline:** Problem Framing --> Discovery Research --> Competitive Analysis --> Metric Design --> Spec Writing --> Narrative Building
**Output:** 2,399 lines across 6 artifacts | 30+ frameworks | 70+ citations

Six PM skills chained together. Each artifact feeds the next -- problem framing shapes research, research informs competitive analysis, analysis drives metrics, metrics anchor the spec, spec feeds positioning. One sentence of input produced a complete product strategy across 6 interconnected documents.

> [View the full pipeline](examples/product-strategy-figma/) | [See the raw AI comparison](examples/product-strategy-figma/comparison.md)

### "Level up my PM team for the AI era"

**Pipeline:** Scout --> Synthesizer --> Planner --> Builder
**Output:** 1,342 lines across 4 artifacts | 10 sourced signals | 4-phase implementation

Scout gathered 10 signals (MIT, Stanford, HBS studies + Stripe, Figma, Linear examples). Synthesizer produced a thesis: "The PM Skill Stack is Inverting." Planner designed a 4-layer team OS. Builder produced a phased implementation plan with day-by-day scheduling.

> [View the full pipeline](examples/pm-team-performance/) | [See the raw AI comparison](examples/pm-team-performance/comparison.md)

### The Pattern

| | Raw AI | Agent Prime |
|---|--------|-------------|
| **Input** | Same question | Same question |
| **Output** | 500-800 words | 1,300-2,400 lines (30-50 pages) |
| **Frameworks applied** | 0 | 13-30+ |
| **Evidence citations** | 0 | 70-91 |
| **Actionable deliverables** | "Do more research" | Watchlists, specs, implementation plans |

---

## The System (Seven Layers)

Each layer is independently useful. Together, they compound.

| Layer | What It Does | Key Files |
|-------|-------------|-----------|
| **01 Identity** | Encodes who you are -- thinking patterns, judgment heuristics, epistemic guardrails | `shared/context.md` |
| **02 Memory** | Every correction compounds. Fix something once, it propagates everywhere. | `shared/learnings.md`, `shared/dependency_map.md` |
| **03 Agents** | 13 specialized agents -- scout, synthesizer, writer, planner, builder, and more | `agents/*/prompt.md` |
| **04 Orchestration** | Registry tracks work, dispatch sequences tasks, briefings surface priorities | `shared/registry.json`, `prime/dispatch.md` |
| **05 Skills** | 12 PM methodologies -- competitive analysis, metric design, pricing, GTM, and more | `shared/toolkits/skills/` |
| **06 Craft** | Design system + templates that produce publication-quality HTML from markdown | `agents/builder/templates/` |
| **07 The Loop** | The recursive mechanism -- learnings propagate, agents chain, the system audits itself | Emerges from layers 1-6 |

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design.

---

## Get Started (60 Seconds)

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime

# Point your AI assistant at it:
# Claude Code  — auto-loads CLAUDE.md
# Copilot      — auto-loads .github/copilot-instructions.md
# Any other LLM — load CLAUDE.md as your system prompt
```

**Want the guided setup?** Run `python meta/scripts/first_run.py` for interactive onboarding (preview, quick trial, or full setup).

**Verify everything works:**

```bash
python meta/scripts/verify_setup.py
```

See [QUICKSTART.md](QUICKSTART.md) for the detailed walkthrough.

---

## Benchmarks

| Test | Score | What It Measures |
|------|-------|------------------|
| PM Skills (competitive analysis) | 93.3/105 (88.9%) | Output quality vs. skill-agnostic rubric |
| Baseline (no system) | 47/105 (44.8%) | Same task, vanilla Claude |
| Anthropic PM Skill | 81/105 (77.1%) | Same task, Anthropic's built-in PM skill |

Agent Prime's skill-powered output scores 2x baseline and 21% above Anthropic's own PM skill on the same structured rubric.

More benchmarks in development: session continuity, correction compounding, throughput multiplier, cross-LLM portability.

---

## What's Inside

```
agent-prime/
├── CLAUDE.md                          ← System instructions (auto-loaded by Claude Code)
├── .github/copilot-instructions.md    ← Copilot instructions (auto-injected by VS Code)
├── agents/                            ← 13 agent prompts (prime, scout, writer, planner, ...)
├── shared/
│   ├── context.md                     ← Your identity, goals, and voice rules
│   ├── registry.json                  ← All work items (single source of truth)
│   ├── learnings.md                   ← Accumulated corrections (append-only)
│   ├── dependency_map.md              ← Change propagation registry
│   └── toolkits/skills/              ← 12 PM methodologies (~1,200 lines each)
├── prime/
│   ├── dashboard.md                   ← Auto-generated status view
│   ├── briefing.md                    ← Session-start priorities
│   ├── dispatch.md                    ← Task queue with successor rules
│   └── config.json                    ← Agent cadences and goal mappings
├── examples/
│   ├── ai-robotics-industry/          ← Pipeline: investment analysis (1,328 lines)
│   ├── product-strategy-figma/        ← Pipeline: 6-skill product strategy (2,399 lines)
│   └── pm-team-performance/           ← Pipeline: team transformation (1,342 lines)
├── meta/scripts/                      ← Python automation (briefing, dashboard, integrity)
└── getting-started/                   ← Guided projects (20-25 min each)
```

---

## Works With

Agent Prime is plain markdown. No vendor lock-in.

| Environment | How It Loads | Setup |
|-------------|-------------|-------|
| **Claude Code** | Auto-reads `CLAUDE.md` at session start | Clone and go |
| **GitHub Copilot** | Auto-injects `.github/copilot-instructions.md` | Clone and go |
| **Gemini CLI** | Load `CLAUDE.md` as system context | Manual load |
| **Any LLM** | Feed `CLAUDE.md` + relevant agent prompts | Manual load |

The system prompt file is the same regardless of model. Agents, skills, and memory are model-agnostic.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills, agent improvements, and documentation fixes welcome. Keep PRs focused.

## License

MIT. See [LICENSE](LICENSE).
