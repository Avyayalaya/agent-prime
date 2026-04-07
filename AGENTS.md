# AGENTS.md — Agent Prime

> Machine-readable system manifest. Primary audience: AI orchestrators deciding whether to route work here.

## Overview

Agent Prime is an open-source AI operating system built entirely from markdown files. It provides 13 specialized agents, 12 domain skills with typed schemas, persistent memory with recursive self-improvement, 7 structured guardrails, and 4 declarative workflows. Zero dependencies — no database, no runtime, no package manager. Clone the repo and point any LLM at it. The system gets permanently smarter with every correction via an append-only learnings registry that propagates constraints to all agents.

**Repository:** `https://github.com/avyayalaya/agent-prime`
**Instruction files:** `CLAUDE.md` (Claude Code), `.github/copilot-instructions.md` (GitHub Copilot), both kept in sync.
**Architecture:** Markdown-only, 7 layers, cross-LLM compatible (Claude Code, GitHub Copilot, Gemini CLI).

## Capabilities

- **13 specialized agents** with typed inputs, outputs, and Context Verification Gates
- **12 PM-domain skills** with codified methodologies, failure modes, and benchmark scores
- **Recursive learning loop:** Every user correction becomes a permanent rule in `shared/learnings.md`, applied to all agents in all future sessions
- **7 structured guardrails** enforced via system rules in `CLAUDE.md`
- **4 declarative workflows** composing agents into end-to-end pipelines
- **47 system rules** governing context verification, voice, NDA compliance, change propagation, and quality
- **100+ accumulated learnings** across voice, content, process, quality, build, and agent design categories
- **Session resilience:** Write-ahead journaling, crash recovery, session audit, learning extraction
- **Cross-LLM compatibility:** Works on Claude Code, GitHub Copilot Chat, Gemini CLI without modification
- **Onboarding wizard:** Interactive setup in under 10 minutes via the Onboarder agent
- **Zero dependencies:** No npm, no pip, no Docker. Python 3.10+ for optional scripts only.

## Agents

| # | Agent | Role | Input | Output | Prompt Path |
|---|-------|------|-------|--------|-------------|
| 1 | **Prime** | Orchestrator | Dispatch queue, registry state | Routing decisions, quality reviews, kill signals | `agents/prime/prompt.md` |
| 2 | **Scout** | Signal detection | Topic or thesis area | Ranked signals with source, relevance, freshness scores | `agents/scout/prompt.md` |
| 3 | **Synthesizer** | Thesis building | Signals, evidence fragments | Structured thesis with evidence map and confidence levels | `agents/synthesizer/prompt.md` |
| 4 | **Writer** | Publication | Mature thesis | Publishable artifact (Substack, LinkedIn, conference talk) | `agents/writer/prompt.md` |
| 5 | **Connector** | Relationship building | Published artifacts, strategic goals | Distribution plans, outreach sequences, relationship pipeline | `agents/connector/prompt.md` |
| 6 | **Planner** | 4-stage planning | Rough idea or scratchpad | Build Handoff Spec (Excavation, Research, Architecture, Critique) | `agents/planner/prompt.md` |
| 7 | **Builder** | Execution | Build Handoff Spec from Planner | Built deliverables, integration reports, validation results | `agents/builder/prompt.md` |
| 8 | **Industry Analyst** | Deep structural mapping | Industry name or sector | ~80-90KB structural analysis: 9 steps, 13 frameworks, 91+ citations | `agents/industry_analyst/prompt.md` |
| 9 | **Investment Analyst** | Investment-grade analysis | Industry structural map | 4-lens valuation, stress-tested scenarios, investment watchlist | `agents/investment_analyst/prompt.md` |
| 10 | **Experimenter** | Empirical validation | Thesis claim to test | Runnable experiments, prototypes, validation results | `agents/experimenter/prompt.md` |
| 11 | **Clerk** | Task tracking | Registry state, deadlines | Staleness reports, commitment audits, deadline alerts | `agents/clerk/prompt.md` |
| 12 | **Judge** | Decision proxy | Pending decisions with context | Auto-acts on low-risk decisions; holds high-risk with structured reasoning | `agents/judge/prompt.md` |
| 13 | **Emissary** | External boundary agent | Inbound signals, outbound actions | 5-layer pipeline: Sensing, Creation, Action, Permission, Learning. 3-tier permission governance. | `agents/emissary/prompt.md` |

**Supporting agent (not counted in 13):**

| Agent | Role | Prompt Path |
|-------|------|-------------|
| **Onboarder** | Interactive setup wizard — configures identity, goals, registry in under 10 minutes | `agents/onboarder/prompt.md` |

### Agent Composition Rules

Agents trigger each other via successor rules in the dispatch queue:

| Completing Agent | Successor Agent | Condition |
|-----------------|-----------------|-----------|
| Scout | Synthesizer | Signal is thesis-worthy |
| Synthesizer | Writer | Thesis reaches maturity |
| Writer | Connector | Artifact is publishable |
| Planner | Builder | Spec passes critique stage |
| Builder | Writer or Connector | Build is complete |

## Workflows

| # | Workflow | Agent Sequence | Output | Trigger |
|---|----------|---------------|--------|---------|
| 1 | **Research to Publish** | Scout → Synthesizer → Writer → Connector | Published article with distribution plan | New topic or signal detected |
| 2 | **Idea to Build** | Planner (4 stages) → Builder | Built deliverable with validation | Rough idea added to registry |
| 3 | **Signal to Action** | Scout → Industry Analyst → Investment Analyst | Investment-grade analysis with watchlist | Market signal in tracked sector |
| 4 | **Inbound to Response** | Emissary (5-layer pipeline) | Assessed inbound with drafted response | External inbound received |

### Guided Projects (for new users)

| Project | Path | What You Build |
|---------|------|---------------|
| Research & Publish | `getting-started/project-1-research-publish/` | A real draft article via Scout → Synthesizer → Writer |
| Plan & Build | `getting-started/project-2-plan-build/` | A real plan via the 4-stage Planner methodology |

## Skills (PM Domain)

12 codified skills with typed schemas, 1.1-1.3K lines each, 9-12 failure modes per skill.

| # | Skill | Domain | Frameworks | Input | Output | Path |
|---|-------|--------|------------|-------|--------|------|
| 1 | `competitive-market-analysis` | Analysis | 9 (7 Powers, Aggregation Theory, Christensen, JTBD, Wardley) | Industry or competitor name | Structural competitive map with moat scoring | `shared/toolkits/skills/competitive-market-analysis/` |
| 2 | `discovery-research` | Research | 8 | Interview data, research sources | Evidence-backed feature hypotheses | `shared/toolkits/skills/discovery-research/` |
| 3 | `problem-framing` | Research | 8 | Vague problem description | Structured problem statement with sizing | `shared/toolkits/skills/problem-framing/` |
| 4 | `specification-writing` | Definition | 6 | Feature or product requirement | Zero-question spec with acceptance criteria | `shared/toolkits/skills/specification-writing/` |
| 5 | `metric-design-experimentation` | Measurement | 9 | Business objective | Metric framework, NSM, experiment designs | `shared/toolkits/skills/metric-design-experimentation/` |
| 6 | `product-strategy` | Strategy | 7 (Vision Cascade, Bet-Sizing, Option-Value Sequencing) | Strategic context | Roadmap with bet sizing and resource allocation | `shared/toolkits/skills/product-strategy/` |
| 7 | `go-to-market-strategy` | Strategy | 7 (Market Entry Thesis, Channel Unit Economics, Dunford Positioning) | Product and market context | GTM plan with launch gating and growth mechanics | `shared/toolkits/skills/go-to-market-strategy/` |
| 8 | `pricing-packaging` | Strategy | 7 (WTP/Van Westendorp, Good/Better/Best, Sensitivity Analysis) | Product and competitive context | Pricing model with packaging tiers and revenue impact | `shared/toolkits/skills/pricing-packaging/` |
| 9 | `executive-writing` | Communication | 8 (Minto/SCR, Audience Calibration, Decision Architecture) | Decision or strategy context | Board memo, strategy one-pager, or exec brief | `shared/toolkits/skills/executive-writing/` |
| 10 | `narrative-building` | Communication | 8 | Product or strategy context | Positioning narrative with stakeholder pitch | `shared/toolkits/skills/narrative-building/` |
| 11 | `multi-channel-publishing` | Communication | 7 (Channel Taxonomy, Hook Adaptation, Spoken Script Derivation) | Long-form content | Channel-specific formats (LinkedIn, conference, newsletter, podcast) | `shared/toolkits/skills/multi-channel-publishing/` |
| 12 | `stakeholder-alignment` | Influence | 7 (Power-Interest-Position, Coalition Analysis, Decision Archaeology) | Stakeholder context | Alignment plan with objection pre-emption and sequencing | `shared/toolkits/skills/stakeholder-alignment/` |

### Skill Design Standards

Every skill follows codified standards (see `shared/toolkits/skill_file_spec.md`):
- **Context Gate:** Required context declared upfront; skill refuses to proceed without it
- **Reader Navigation:** Table of contents with section anchors
- **Notation Key:** Standardized symbols for confidence, evidence quality, risk
- **Failure Modes:** 9-12 explicitly named failure patterns with detection and mitigation
- **Discoverability YAML:** Identity metadata for agent-to-agent discovery (SYS-015)

## Guardrails

| # | Guardrail | Type | Action | Applies To |
|---|-----------|------|--------|------------|
| 1 | **Context Gate** | Blocking | Agent stops and asks if required files are missing — never proceeds with degraded context | All agents |
| 2 | **NDA Filter** | Blocking | Never references internal employer data, roadmaps, or unreleased features | All outputs |
| 3 | **Voice Check** | Corrective | Applies voice rules from `shared/context.md`; bans hype language, "not X but Y" constructions | All artifacts |
| 4 | **Quality Bar** | Validating | Every substantial artifact includes a visible `## Quality Check` section | All agents |
| 5 | **Permission Tier** | Gating | 3-tier governance for external actions (auto/confirm/escalate) | Emissary, Connector |
| 6 | **Production Order** | Sequential | Long-form first, short-form second — never compress before the full argument exists | Writer, Multi-Channel Publishing |
| 7 | **Publish Parity** | Parallel | Build specs must include distribution plans with equal rigor to the build itself | Planner, Builder, Writer |

## Getting Started

### For AI agents (programmatic)

```
1. Read CLAUDE.md (system rules and file map)
2. Read shared/context.md (user identity, goals, constraints)
3. Read shared/registry.json (current state of all work items)
4. Read shared/learnings.md (accumulated hard constraints)
5. Invoke agents via their prompt files at agents/{name}/prompt.md
```

### For humans (interactive)

```bash
git clone https://github.com/avyayalaya/agent-prime.git
cd agent-prime
python meta/scripts/first_run.py
```

Three modes available: `preview` (see it in browser), `quick-trial` (pre-built example), `onboard` (guided setup).

### For LLM environments

| Environment | Instruction File | How It Loads |
|-------------|-----------------|--------------|
| Claude Code | `CLAUDE.md` | Auto-loaded at session start |
| GitHub Copilot Chat | `.github/copilot-instructions.md` | Auto-injected into every conversation |
| Gemini CLI | `CLAUDE.md` | Read manually or via config |
| Any LLM | `CLAUDE.md` | Point the model at this file as system context |

## Benchmarks

| Metric | Score | Methodology |
|--------|-------|-------------|
| **PM Skills Arsenal (v1.3.0)** | 93.3/105 (88.9%) | 7-dimension rubric on competitive-market-analysis skill output |
| Anthropic PM Skill (baseline) | 81/105 (77.1%) | Same rubric, Anthropic's built-in PM skill |
| No skill (control) | 47/105 (44.8%) | Same rubric, raw LLM with no skill guidance |
| **Improvement over no-skill** | +108% | 47 → 98 points on identical input |
| **Publication threshold** | 90/105 | Minimum score for public release (exceeded) |

Benchmark based on the competitive-market-analysis skill. Same one-sentence input across all three conditions.

## Architecture

```
Layer 7: Workflows          4 declarative pipelines composing agents
Layer 6: Agents             13 specialized agents with typed I/O
Layer 5: Skills             12 PM-domain skills with codified methodologies
Layer 4: Guardrails         7 rules enforcing quality, voice, NDA, permissions
Layer 3: State              Registry (JSON) + dispatch queue + session state
Layer 2: Memory             Learnings (append-only) + context + reference library
Layer 1: Identity           User context, voice, goals, constraints
```

**Design principles:**
1. Composable agents, not a hierarchy — each agent is self-contained
2. State lives in files, not memory — all state is human-readable markdown and JSON
3. Learning is permanent — corrections become hard constraints
4. Agents trigger agents — dispatch queue creates push-based pipelines
5. Quality is visible — every output includes verification

**Key state files:**

| File | Role | Format |
|------|------|--------|
| `shared/registry.json` | Single source of truth for all work items | JSON |
| `shared/learnings.md` | Append-only correction log — hard constraints | Markdown |
| `shared/context.md` | User identity, goals, voice, constraints | Markdown |
| `prime/dispatch.md` | Agent task queue with priorities | Markdown |
| `prime/dashboard.md` | Auto-generated pipeline view | Markdown (generated) |
| `shared/dependency_map.md` | Change propagation registry | Markdown |
| `shared/theses.json` | Thesis data for Synthesizer and Writer | JSON |

**Schemas:** `shared/schemas/` contains JSON schemas for pipeline, signals, and tasks.

## File Structure

```
agent-prime/
├── AGENTS.md                    # This file — system manifest
├── CLAUDE.md                    # System rules (Claude Code)
├── ARCHITECTURE.md              # Detailed architecture documentation
├── QUICKSTART.md                # 4-path getting started guide
├── agents/
│   ├── prime/prompt.md          # Orchestrator
│   ├── scout/prompt.md          # Signal detection
│   ├── synthesizer/prompt.md    # Thesis building
│   ├── writer/prompt.md         # Publication
│   ├── connector/prompt.md      # Relationship building
│   ├── planner/prompt.md        # 4-stage planning
│   ├── builder/prompt.md        # Execution
│   ├── industry_analyst/prompt.md   # Structural mapping
│   ├── investment_analyst/prompt.md # Investment analysis
│   ├── experimenter/prompt.md   # Empirical validation
│   ├── clerk/prompt.md          # Task tracking
│   ├── judge/prompt.md          # Decision proxy
│   ├── emissary/prompt.md       # External boundary
│   └── onboarder/prompt.md      # Setup wizard
├── shared/
│   ├── context.md               # User identity and goals
│   ├── learnings.md             # Accumulated corrections
│   ├── registry.json            # Work item state
│   ├── dependency_map.md        # Change propagation
│   ├── theses.json              # Thesis data
│   ├── schemas/                 # JSON schemas
│   ├── runbooks/                # Operational runbooks
│   └── toolkits/skills/         # 12 PM-domain skills
├── prime/
│   ├── dashboard.md             # Auto-generated pipeline view
│   ├── dispatch.md              # Agent task queue
│   ├── briefing.md              # Session briefing
│   ├── session_state.md         # Session bootstrap
│   └── config.json              # Agent cadences
├── meta/scripts/                # Python automation scripts
├── getting-started/             # Guided first projects
└── examples/                    # Pre-built configurations
```

## Contact

**Author:** Parth Sangani
**License:** See `LICENSE`
**Issues:** `https://github.com/avyayalaya/agent-prime/issues`
