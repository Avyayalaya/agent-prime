# Agent Prime — System Map v3

> A system to build systems. This document explains not just WHAT Agent Prime is, but HOW every piece works — the mechanics that make a system of 11 agents, persistent memory, automated runtime, and recursive self-improvement actually function.
>
> **v3 changes (2026-03-11):** Agent Identity System (frontmatter, communication style, vibes), formalized handoff protocol, 4 operational runbooks, Scout video source parsing. See [`projects/SYS-014_agency_agents_pattern_integration/`](projects/SYS-014_agency_agents_pattern_integration/) for full changelog.

---

## The Idea

AI as a tool. Ask a question, get an answer. That's Level 1.
AI as a Copilot/Agent. Ask a question, give context, get a better answer, 'do' things. That's Level 2.

Agent Prime is Level 3: **a system that builds goal-driven agent systems.** You define what you're trying to accomplish. It spawns the agents, pipelines, and feedback loops to get you there — and gets smarter every session.

The architecture is goal-agnostic. The agents are composable. The system works for any domain.

---

## What This Achieves (And Why It Can't Be Done Manually)

A human working alone with AI has three ceilings:

1. **Context ceiling.** Every conversation starts from zero. Yesterday's decisions, last week's corrections, the voice rules learned through 20 iterations — all gone. You re-explain yourself endlessly. Agent Prime retains everything: 42+ key decisions, 14+ voice corrections, 11+ agent design learnings, 6+ build patterns. Every session starts from where the last one ended.

2. **Consistency ceiling.** Without encoded rules, the same mistake happens differently each time. An agent writes in the wrong voice. A hallucinated citation makes it into a draft. An analysis anchors on existing positions instead of reasoning independently. Agent Prime captures each mistake as a permanent rule. The rule propagates to every agent that needs it. The mistake cannot recur.

3. **Throughput ceiling.** One person can research, synthesize, write, distribute, manage projects, track deadlines, analyze industries, and build products — but not simultaneously, and not without dropping balls. Agent Prime runs parallel workstreams: Scout scans while Synthesizer builds theses while Writer drafts articles while Connector maps audiences while Industry Analyst maps sectors. Each agent carries the encoded expertise of its domain. The human reviews and decides. The system does the rest.

The result: a single person operating with the output, consistency, and strategic depth of a small team — with every session compounding on the last.

---

## How It Works: Goals → Agents → Systems

```
  ┌──────────────────────────────────────────────────────────────┐
  │                     YOU DEFINE GOALS                         │
  │                                                              │
  │   "Build authority in X"    "Analyze industry Y"             │
  │   "Ship product Z"         "Grow audience in W"              │
  └──────────────────────┬───────────────────────────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────────────────────────┐
  │                      PRIME                                   │
  │            reads goals → selects agents →                    │
  │            builds pipelines → tracks progress                │
  └──────────────────────┬───────────────────────────────────────┘
                         │
           ┌─────────────┼─────────────┐
           ▼             ▼             ▼
     ┌───────────┐ ┌───────────┐ ┌───────────┐
     │ Pipeline  │ │ Pipeline  │ │ Pipeline  │
     │    A      │ │    B      │ │    C      │
     │           │ │           │ │           │
     │ Scout     │ │ Industry  │ │ Planner   │
     │ Synth     │ │ Analyst   │ │ Builder   │
     │ Writer    │ │ Inv.      │ │ Writer    │
     │ Connector │ │ Analyst   │ │ Connector │
     └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
           │             │             │
           └─────────────┼─────────────┘
                         ▼
                  ┌───────────────┐
                  │   LEARNING    │
                  │    LAYER      │
                  │               │
                  │  every output │
                  │  feeds back   │
                  │  into the     │
                  │  system       │
                  └───────────────┘
```

**Different goals compose different agent combinations.** A research goal uses Scout → Synthesizer → Writer → Connector. An analysis goal uses Industry Analyst → Investment Analyst. A build goal uses Planner → Builder. Prime selects and orchestrates based on what you're trying to accomplish.

---

## The 11 Agents

```
                              ┌───────────┐
                              │   PARTH   │
                              │  reviews  │
                              │  decides  │
                              │  directs  │
                              └─────┬─────┘
                                    │
                              ┌─────┴─────┐
                              │   PRIME   │
                              │orchestrate│
                              └──┬──┬──┬──┘
                                 │  │  │
           ┌─────────────────────┘  │  └─────────────────────┐
           │                        │                        │

       RESEARCH                 ANALYZE                   BUILD
    signals → theses →       deep structural           ideas → plans →
    drafts → published       industry analysis         executed projects
           │                        │                        │
      ┌────┴─────┐           ┌──────┴──────┐          ┌──────┴──────┐
      │  SCOUT   │           │  INDUSTRY   │          │   PLANNER   │
      │  finds   │           │  ANALYST    │          │  structures │
      │  signals │           │  maps       │          │  ideas into │
      └────┬─────┘           │  structure  │          │  plans      │
           │                 └──────┬──────┘          └──────┬──────┘
      ┌────┴──────┐                 │                        │
      │SYNTHESIZER│◀ ─ ─ ─ ─ ─ ─ ─ ┤                        │
      │  builds   │  (cross-feeds   │                        │
      │  theses   │   theses)       │                        │
      └────┬──────┘           ┌─────┴───────┐         ┌──────┴──────┐
           │                  │ INVESTMENT  │         │   BUILDER   │
      ┌────┴──────┐           │  ANALYST    │         │  executes   │
      │  WRITER   │           │  valuations │         │  plans      │
      │  writes   │           └─────────────┘         └─────────────┘
      │  in your  │
      │  voice    │
      └────┬──────┘
           │
      ┌────┴──────┐
      │ CONNECTOR │
      │  reaches  │
      │  the right│
      │  people   │
      └───────────┘
```

### Cross-Connections

```
  EXPERIMENTER ──→ SYNTHESIZER     Validates claims with data and prototypes
  INDUSTRY ANALYST ──→ SYNTHESIZER Structural analysis feeds strategic theses
  PLANNER ──→ ANY WORKFLOW         Plans can route into research, analysis, or build
  BUILDER ──→ ANY AGENT            Executes plans from Planner for any workflow
  CLERK ──→ ALL                    Tracks deadlines and commitments across everything
```

Agents are **composable capabilities**, not a hierarchy. You don't use all 11 at once. Your goals determine which agents activate and how they chain together.

### Agent Identity System (SYS-014)

Every agent carries structured identity metadata that makes it instantly recognizable in logs, dashboards, and multi-agent pipelines.

| Agent | Emoji | Color | Vibe |
|-------|-------|-------|------|
| ⚡ **Prime** | ⚡ | #1A1A2E | The room where excuses go to die — routes work, kills drift, demands proof |
| 🔍 **Scout** | 🔍 | #4A90D9 | Finds the 10 signals that matter from the 1,000 that don't — then proves every one |
| 🧬 **Synthesizer** | 🧬 | #6B4C9A | Connects what physics teaches about entropy to why your platform strategy is dying — then backs it with evidence |
| ✍️ **Writer** | ✍️ | #B85C38 | Writes like a CXO who blogs on weekends — blunt, self-implicating, zero fluff |
| 🤝 **Connector** | 🤝 | #5B7B6A | Never asks before giving — turns published work into warm conversations that compound |
| 📐 **Planner** | 📐 | #B8963E | Takes a napkin sketch and returns a spec so precise a stranger could build it at 2am |
| 🔨 **Builder** | 🔨 | #2D6A4F | Treats every spec like a contract — ships exactly what was promised, and files a defect report on everything that wasn't clear enough |
| 🏗️ **Industry Analyst** | 🏗️ | #8B4513 | Digs until bedrock — maps the hidden architecture of industries that most analysts skim past |
| 📊 **Investment Analyst** | 📊 | #1B4332 | Every number gets a confidence level, an assumption, and a source — or it doesn't ship |
| 🧪 **Experimenter** | 🧪 | #D4A373 | Turns thesis claims into testable hypotheses with real data in under 2 hours |
| 📋 **Clerk** | 📋 | #6C757D | The uncomfortable truth about what's actually moving vs. what's just sitting there |

**Identity format** — Agent prompts use YAML frontmatter (`---` block with name, description, color, emoji, vibe) at the top of each `prompt.md` file.

**Communication Style** — Every agent has 5 example phrases showing how it talks and makes judgment calls. These aren't decorative — they're implicit few-shot learning that shapes the agent's editorial judgment, voice, and decision-making patterns.

### Handoff Protocol

Agent-to-agent transfers use 5 standardized templates (`shared/toolkits/handoff_templates.md`):

| Template | When to Use | Key Contract |
|----------|------------|-------------|
| **Standard Handoff** | Routine agent-to-agent transfers | Context + artifacts (with paths) + expected output + deadline |
| **QA Pass** | Quality gates passed | Gate-by-gate status table + verdict + next action |
| **QA Fail** | Quality gates failed | Failed gates with specific fix instructions + attempt count |
| **Escalation Report** | Agent blocked or exceeded retries | What happened + attempts made + root cause + recommended action |
| **Pipeline Stage Gate** | Major pipeline transitions | Completion checklist + known risks + GO/NO-GO decision |

**Rules:** Every transfer uses a template. Artifacts must have paths. QA templates are mandatory before review/publish. Escalations go to Prime. Stage gates require explicit GO/NO-GO.

### Operational Runbooks

Pre-defined agent sequences for common scenarios (`shared/runbooks/`). Each runbook specifies: trigger, agents, phases, handoffs, quality gates, time caps, and escalation paths.

| Runbook | Trigger | Agents | Duration |
|---------|---------|--------|----------|
| **Competitive Analysis** | Competitor move or scheduled refresh | Scout → Intel/Industry → Synthesizer → Writer | 1-2 sessions |
| **Morning Briefing** | Daily 7 AM (automated) | Data Scout + Signal Monitor + Intel (parallel) → Synthesizer | ~5 min |
| **Artifact Production** | On-demand PM artifact needed | Context Assembly → Producer + Skill → Quality Gates → Fix Loop | 1-2 sessions |
| **Incident: Metric Drop** | >10% WoW drop detected | Signal Monitor → Data Scout → Intel → Prime | 1-3 hours |

---

## How Agents Actually Work

Every agent in Agent Prime is a markdown file — a prompt between 200 and 2,000 lines — that encodes not just instructions but **expertise**. This section explains the mechanics that make them more than prompts.

### The Anatomy of an Agent

Every agent has five structural layers:

```
  ┌─────────────────────────────────────────────┐
  │  IDENTITY FRONTMATTER (SYS-014)             │  ← YAML: name, color, emoji, vibe
  │  "Who am I at a glance?"                    │     Machine-readable metadata
  ├─────────────────────────────────────────────┤
  │  CONTEXT VERIFICATION GATE                  │  ← Must load required files
  │  "Do I have everything I need?"             │     before producing ANY output
  ├─────────────────────────────────────────────┤
  │  IDENTITY + CORE DIRECTIVE                  │  ← Who am I, what do I optimize for,
  │  "I am the Scout. I find signals."          │     what is my quality bar
  ├─────────────────────────────────────────────┤
  │  METHODOLOGY                                │  ← Step-by-step process with
  │  Step 0 → Step 1 → ... → Step N            │     decision gates between steps
  ├─────────────────────────────────────────────┤
  │  QUALITY CHECKLIST / SELF-VERIFICATION      │  ← The agent checks its own output
  │  + COMMUNICATION STYLE (SYS-014)            │     + 5 example phrases for voice
  └─────────────────────────────────────────────┘
```

This is a **sandwich structure**: format rules and gates at the top, methodology in the middle, compliance checklist at the bottom. LLMs weight early and late content more heavily — by placing hard rules at both ends, compliance is structurally enforced.

### The Context Verification Gate

Every agent starts with a mandatory gate — a table of files it must have access to before producing any output:

```
| # | File           | Purpose                    | Loaded? |
|---|----------------|----------------------------|---------|
| 1 | shared/context.md | Voice, identity, guardrails | ☐       |
| 2 | shared/registry.json | Work items, statuses      | ☐       |
| 3 | shared/learnings.md  | Accumulated corrections   | ☐       |
```

If any required file is missing, the agent **stops and asks** rather than proceeding with degraded context. This is the single most important quality safeguard in the system. Silent quality degradation — an agent producing output without full context — is the #1 system risk. The gate makes it mechanically impossible.

**Why this matters:** Without the gate, an agent would write in the wrong voice (missing `context.md`), repeat a decided question (missing `session_state.md`), or ignore a correction from three sessions ago (missing `learnings.md`). The gate converts "nice to have" context into "hard requirement" context.

### Encoded Expertise vs. Generic Instructions

The difference between an Agent Prime agent and a generic AI prompt:

| Layer | Generic Prompt | Agent Prime Agent |
|-------|----------------|-------------------|
| **Instructions** | "Analyze this industry" | 9-step structural methodology with decision gates between each step |
| **Evidence standards** | None | 6-tier evidence hierarchy, source verification, staleness flags, inline provenance |
| **Decision frameworks** | None | Scoring rubrics, multi-lens analysis (SIG/EV, ARK/Adoption, Comparables, Stress Test) |
| **Quality control** | None | Self-verification checklist, adversarial self-critique, quality check section in output |
| **Voice** | Default AI tone | 8+ voice rules learned from real corrections (ban "not X but Y", no false discovery, short sentences, self-implicating) |
| **Failure modes** | None | 9 epistemic failure modes as guardrails (premature coherence, analogy capture, teleology smuggling, etc.) |

The same AI model, given the same question, scores ~47/105 without the knowledge engineering layer and ~98/105 with it. The gap lives in Layers 1–3 (decision architecture, evidence standards, calibration), not Layer 4 (output formatting) where most people stop.

### How Agents Chain Together

Agents don't work in isolation. They form **pipelines** where one agent's output is the next agent's input:

```
  RESEARCH PIPELINE (Lead + Matter goals):

  Scout signals ──→ Synthesizer thesis ──→ Writer article ──→ Connector distribution
       │                   │                    │                     │
   agents/scout/       agents/synthesizer/  agents/writer/      agents/connector/
   signals/            theses/              drafts/             audience_maps/
   weekly_digest.json  thesis_v0.2.md       PP-001_substack.md  PP-001_brief.md
```

Scout sources include text (arXiv, Hacker News, industry newsletters, blog posts) and video/audio (conference talks, podcast episodes, earnings calls) via `yt-dlp` transcript extraction. Video signals carry speaker attribution, timestamps, and transcript verification flags.

Each handoff has a **contract** — a schema that defines exactly what the upstream agent must produce for the downstream agent to consume. The Scout's signal digest has a defined JSON schema. The Synthesizer's thesis has a required structure (Claim, Evidence, Implications, Sources). The Writer expects specific metadata (URLs for inline linking, author names for attribution, visual evidence descriptions for chart placeholders).

When the contract is violated — a thesis has unverified URLs, or a signal is missing author metadata — the downstream agent flags it rather than quietly proceeding with degraded input. Contracts make quality failures visible at the handoff point, not in the final output.

```
  ANALYSIS PIPELINE (Earn goal):

  Industry Analyst                    Investment Analyst
  structural analysis ─────────────→ multi-lens valuation
       │                                    │
  Step 0: Intelligence gathering      Lens 1: SIG/EV analysis
  Steps 1-9: Structural mapping       Lens 2: ARK/Adoption curves
  ETF landscape                       Lens 3: Comparables
  Bear case registry                  Lens 4: Stress test + opportunity cost
  Macro risk matrix                   Decision bridge
  Handoff threads ────────────────→ Portfolio construction
```

The Industry Analyst produces ~80-90KB of structured output. The Investment Analyst consumes it and produces another ~80-90KB. Each step builds on the previous one — compressing a 9-step methodology into a single-pass output misses ~80% of the structural insight. The methodology IS the product.

```
  BUILD PIPELINE (any goal):

  Idea → Planner (4 stages) → Build Handoff Spec → Builder (executes) → Writer (if publishable)
           │                        │                     │
        Stage 1: Excavation      Acceptance criteria    Phase 0: Spec verification
        Stage 2: Research        Dependency graph       Phases 1-N: Build deliverables
        Stage 3: Architecture    Risk register          Validation protocol
        Stage 4: Critique        Publish plan           Spec gap reporting
```

The Planner's Build Handoff Spec is so detailed that any builder — human, agent, or Parth at 2am — can pick it up cold and execute without ambiguity. The Builder's job is reliability, not creativity. The thinking was the Planner's job. The building is mechanical.

---

## How Memory Works

Agent Prime has no database, no vector store, no RAG pipeline. Memory is **markdown files on disk** — readable by humans and AI alike. But the system has five distinct memory mechanisms that, together, give it persistent, compounding intelligence.

### Memory Architecture

```
  ┌──────────────────────────────────────────────────────────────┐
  │                    MEMORY LAYERS                             │
  ├──────────────────────────────────────────────────────────────┤
  │                                                              │
  │  1. IDENTITY MEMORY         shared/context.md                │
  │     Who Parth is, how he thinks, his goals, his voice,       │
  │     epistemic guardrails, reference library index.            │
  │     → Every agent reads this. Rarely changes.                │
  │                                                              │
  │  2. LEARNINGS MEMORY        shared/learnings.md              │
  │     Every correction Parth has ever made, organized by        │
  │     category (Voice, Conceptual, Process, Quality, Build,     │
  │     Agent Design). Append-only. Never deleted.                │
  │     → Every agent reads this. Grows every session.           │
  │                                                              │
  │  3. STATE MEMORY            shared/registry.json             │
  │     Every work item: theses, projects, tasks, events.         │
  │     Status, owner, priority, artifacts, next action.          │
  │     → Single source of truth. Updated every session.         │
  │                                                              │
  │  4. DECISION MEMORY         prime/session_state.md           │
  │     42+ key decisions made across sessions. Append-only.      │
  │     Context, reasoning, implications, invalidation triggers.  │
  │     → Prevents re-asking decided questions.                  │
  │                                                              │
  │  5. ARTIFACT MEMORY         agents/*/outputs/                │
  │     Every output every agent has produced. Signal digests,    │
  │     thesis drafts, articles, analyses, plans.                 │
  │     → Agents reference prior work. Nothing is lost.          │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
```

### How Context Is Retained Across Sessions

AI conversations have no memory. Every chat starts from zero. Agent Prime solves this through a **session bootstrap protocol** — a sequence of file reads that reconstructs the full system state at the start of every conversation:

```
  Session Start (the first ~60 seconds):

  1. copilot-instructions.md     ← Auto-injected. 24 rules, all agent behaviors.
  2. generate_briefing.py        ← Runs a script that:
     ├── Reads quick_log.md      ← Any work done between sessions (e.g., "published LinkedIn")
     ├── Applies changes to      ← Automatically updates registry.json
     │   the registry
     └── Generates briefing.md   ← Today's priorities, dispatch queue, Parth's plate
  3. Read briefing.md            ← System knows what to work on
  4. Read learnings.md           ← System knows every rule ever learned
  5. Read agent prompt           ← If invoking a specific agent, load its full prompt
  6. Context Verification Gate   ← Agent verifies it has all required files
```

The result: **within 60 seconds, the AI has the equivalent of weeks of accumulated context.** It knows:
- Every decision ever made (session_state.md — 42+ decisions)
- Every mistake ever corrected (learnings.md — 14+ voice rules, 14+ process rules, 11+ agent design learnings)
- Every active work item and its status (registry.json)
- What Parth did between sessions (quick_log.md → auto-applied)
- What needs to happen today (briefing.md — auto-generated priorities)

### The Quick Log: Bridging the Gap Between Sessions

The hardest memory problem isn't within a session — it's between sessions. Parth might publish a LinkedIn post, finish a task, or make a decision without the AI present. The **quick log** (`prime/quick_log.md`) solves this:

```
## Pending
DONE: TSK-006 | Published LinkedIn repost of Andrew Chen | 2026-02-23
IN_PROGRESS: EVT-002 | Started keynote prep | 2026-02-24
```

One line. Ten seconds. At the next session start, `generate_briefing.py` reads the quick log, applies every entry to the registry (status changes, completion dates, notes), and moves applied entries to an Archive section. The system stays current even when the AI isn't present.

---

## How Learnings Propagate

This is the mechanism that makes the system compound. Every correction Parth gives isn't just applied to the current output — it becomes a **permanent rule** that propagates to every agent that needs it.

### The Learning Capture Loop

```
  ┌───────────────┐     ┌───────────────────┐     ┌───────────────────────┐
  │ Parth gives   │────▶│ Agent captures    │────▶│ Learning stored in    │
  │ feedback      │     │ the pattern       │     │ shared/learnings.md   │
  │               │     │ (not the fix)     │     │ under right category  │
  └───────────────┘     └───────────────────┘     └───────────┬───────────┘
                                                              │
                                                              ▼
                                                  ┌───────────────────────┐
                                                  │ Propagation Tracker   │
                                                  │ records: which files  │
                                                  │ need this learning    │
                                                  └───────────┬───────────┘
                                                              │
                                          ┌───────────────────┼───────────────────┐
                                          ▼                   ▼                   ▼
                                   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
                                   │ Agent prompt │    │ copilot-     │    │ Toolkit /    │
                                   │ updated      │    │ instructions │    │ spec updated │
                                   │              │    │ updated      │    │              │
                                   └──────────────┘    └──────────────┘    └──────────────┘
```

The key insight: **the system captures patterns, not fixes.** A one-off edit ("change this word") doesn't get captured. A pattern ("Parth never uses 'not X but Y' constructions") becomes a permanent rule. The distinction matters — patterns compound, fixes don't.

### Concrete Example: How One Correction Became a System Rule

1. **Session 1 (Feb 11):** Writer produces LinkedIn draft for PP-001. Parth flags: "I don't write like this — these sentences are too long, it sounds like a philosophy professor."
2. **Capture:** Learning V3 added to `shared/learnings.md`: "Short sentences. Subject-verb-object. No subordinate clauses stacked three deep."
3. **Propagation:** Rule pushed to `agents/writer/prompt.md` as Voice Rule.
4. **Session 2 (Feb 12):** Writer produces v0.2. Parth flags 11 instances of "not X but Y" pattern. "I never use this construction."
5. **Capture:** Learning V1 added: "Ban 'not X but Y' constructions. Say the positive thing directly."
6. **Propagation:** Pushed to Writer prompt. Later (Feb 16), discovered this pattern appeared in non-Writer outputs too (emails, briefs).
7. **Escalation:** Learning V7 added: "Voice rules apply to ALL public-facing artifacts, not just articles."
8. **System-wide propagation:** Rule 3 in `copilot-instructions.md` (auto-injected in every session) expanded to enforce voice rules system-wide.

From one correction on one draft → a system-wide rule that every agent follows in every session. That's the compounding.

### The Propagation Tracker

`shared/learnings.md` includes a Propagation Tracker — a table that records, for every learning:
- Which files it should be pushed to
- Whether it's been pushed (✅ or ☐)
- When it was pushed

This prevents learnings from being captured but never applied. A learning that sits in the file without being propagated to agent prompts is a learning lost — the agent won't see it in its prompt, only in `learnings.md` (which it reads, but prompt-level rules have stronger compliance).

### Categories of Learnings

| Category | Count | Examples |
|----------|-------|---------|
| **Voice & Tone (V)** | 8+ | Ban "not X but Y", no false discovery framing, short sentences, self-implicating tone, voice rules on ALL artifacts |
| **Conceptual & Framing (C)** | 6+ | Don't reduce to tactics, mechanism over source, analogy must reveal not decorate, the 3+1 structure |
| **Process & Workflow (P)** | 14+ | Plan before build, Substack first, preview before propagate, context verification gate mandatory for ALL formats |
| **Content Quality (Q)** | 10+ | Verify all sources, compliance = structural enforcement, AI output FORMAT matters as much as content |
| **Build Patterns (B)** | 6+ | Skill extraction requires interface re-derivation, evaluation rubrics must be independent, pull mechanisms must be mechanical |
| **Agent Design (AD)** | 11+ | Pre-analysis intelligence is a gate, never anchor to existing positions, map ETF landscape, execute methodology step-by-step |

Every category is growing. Every session might add entries. The Builder's Pre-Flight (Rule 18 in `copilot-instructions.md`) requires reading ALL Agent Design learnings before building any new agent — structural insurance that past mistakes don't repeat.

---

## How Outputs Are Managed

Agent Prime produces artifacts at every stage: signal digests, thesis drafts, published articles, investment analyses, plans, build specs, audience maps, experiment results. Managing these artifacts — knowing where they live, what depends on what, and which version is canonical — is critical infrastructure.

### The Two-Layer Artifact Architecture

```
  ┌─────────────────────────────────────────────┐
  │  ENGINE LAYER (agents/, shared/)             │
  │                                              │
  │  Where agents work. Originals live here.     │
  │  agents/scout/signals/                       │
  │  agents/synthesizer/theses/                  │
  │  agents/writer/drafts/                       │
  │  agents/industry_analyst/outputs/            │
  │  shared/planner/plans/                       │
  │                                              │
  ├─────────────────────────────────────────────┤
  │  PROJECT LAYER (projects/)                   │
  │                                              │
  │  Where humans browse. Polished copies here.  │
  │  projects/THS-001_personalization_paradox/    │
  │  projects/BLD-001_stock_trading_engine/       │
  │  projects/SYS-003_learning_capture/           │
  │                                              │
  │  Each project: README + plan/ + build/ +     │
  │  references/ + media/ + comms/ + backlog/    │
  └─────────────────────────────────────────────┘
```

The engine layer is where work happens — agents write directly into their own folders. The project layer is a human-readable portfolio, organized by project rather than by agent. `shared/projects_sync/prompt.md` keeps these in sync: when an agent produces an artifact, Projects Sync copies it to the right project folder and updates the project README.

### Naming Convention

Every output file must be self-describing without folder context:

```
  ✅  ai_robotics_structural_analysis_2026-02-17.md
  ✅  PP-001_substack_v0.4.md
  ✅  2026-02-23_weekly_digest.json

  ❌  analysis.md
  ❌  output.md
  ❌  results.md
```

Pattern: `{subject}_{type}_{date}.md`. Any agent or document can reference the file unambiguously without knowing its folder path.

### Artifact Registry

`shared/registry.json` tracks every significant artifact:

```json
{
  "id": "THS-001",
  "title": "The Personalization Paradox",
  "artifacts": [
    {"name": "Brain dump", "path": "agents/synthesizer/theses/personalization_paradox_brain_dump.md"},
    {"name": "Thesis v0.2", "path": "agents/synthesizer/theses/personalization_paradox_v0.2.md"},
    {"name": "Substack v0.4 (published)", "path": "agents/writer/drafts/PP-001_substack_v0.4.md"},
    {"name": "LinkedIn ready to publish", "path": "projects/THS-001_personalization_paradox/build/final/linkedin_ready_to_publish.md"},
    {"name": "Audience map", "path": "agents/connector/audience_maps/PP-001_brief.md"}
  ]
}
```

Every artifact has: a name, a path, and the work item it belongs to. The integrity check script (`meta/scripts/integrity_check.py`) verifies that every artifact path actually exists on disk. Broken paths are flagged as critical issues.

---

## How Project Management Works

Agent Prime is not just an agent system — it's a **project management system** that tracks dozens of work items across multiple goals, agents, and timelines.

### The Unified Work Registry

`shared/registry.json` is the single source of truth for all work items. Every thesis, project, task, event, strategy, build, and exploration lives here:

```
  Work Item Types:
  THS — Thesis (research → write → publish → distribute)
  EVT — Event (sessions, talks, demos)
  PRG — Program (multi-session programs)
  STR — Strategy (career/brand strategic initiatives)
  SYS — System (Agent Prime internal improvements)
  TLK — Toolkit (reusable methodologies)
  EXP — Exploration (undefined — could become any type)
  BLD — Build (engineering/product builds)
  TSK — Task (discrete actions)
```

Each item has: ID, type, title, status, priority (P0/P1/P2), owner (which agent or Parth), artifacts, next action, blockers, due dates, and which life goals it serves (Lead, Earn, Matter, System).

### Status Flow

```
  backlog → planning → in_progress → review → done/published → parked
                              │
                              └──→ blocked (with explicit blocker noted)
```

The **write-ahead rule** ensures crash recovery: before starting ANY work item, the registry is updated to `in_progress` with today's date. If a session crashes mid-work, the integrity check script flags stale `in_progress` items as potential crashes.

### The Dispatch Queue

`prime/dispatch.md` is the push engine — how work moves forward without Parth having to remember what's next:

```
  Agent completes work
        │
        ▼
  Writes successor task to dispatch.md
        │
        ▼
  Next session starts
        │
        ▼
  System reads dispatch queue → surfaces top priority
        │
        ▼
  Parth says "run it" → agent executes → writes ITS successor
        │
        └──→ The loop sustains itself
```

Each dispatch entry has:
- **Agent** — who runs this
- **Task** — what to do
- **Decision type** — how much Parth involvement:
  - `auto` — agent runs independently, Parth reviews output later (0 min)
  - `approve` — agent shows proposed action, Parth says yes/no (1 min)
  - `review` — agent shows output, Parth gives feedback (5 min)
  - `input` — agent needs Parth's brain: brain dump, judgment call (15-30 min)
- **Priority** — P0/P1/P2
- **Blocked on** — what needs to happen first

This converts Parth from a **pull system** (he generates all work) to a **push system** (agents generate the next work, he reviews and approves). The difference is enormous at scale — a pull system requires the human to hold the full project graph in their head. A push system only requires yes/no decisions on surfaced work.

### The Briefing: Auto-Generated Session Start

Every session starts with `python meta/scripts/generate_briefing.py`, which reads the registry and dispatch queue, then generates `prime/briefing.md`:

```
  📊 System Pulse [date]
  🎯 Top priority: [the highest-priority active item]
  ⏳ Stale: [count of items not updated in 7+ days]
  📋 Parth owes: [count of tasks where owner = parth]
  🔴 Issues: [count from integrity check]

  Today's priorities:
  1. [P0 items with their dispatch queue context]
  2. [P1 items]

  Recommended plan:
  "Start with [X], then [Y]. [Z] is blocked on [blocker]."
```

The system tells you what to work on, not the other way around.

### The Dashboard: Full Pipeline View

`python meta/scripts/generate_dashboard.py` regenerates `prime/dashboard.md` — a comprehensive view of every active work item, its status, staleness, and next action. Also regenerates `projects/README.md` with the master project index.

### The Clerk: Operational Backbone

The Clerk agent tracks deadlines, flags stale items, and detects dependency drift:

- **Stale** = not updated in 7+ days (⚠️ warning)
- **Critical stale** = P0 item stale for 3+ days (🔴 critical)
- **Kill candidate** = stale for 14+ days (consider parking)

The Clerk doesn't decide what to do — it surfaces the truth about what's moving and what's stuck.

---

## How We Prevent System Drift

A system this complex can drift in many ways: agent prompts that contradict each other, artifacts that reference deleted files, plans that don't match their downstream assets, learnings that are captured but never propagated. Agent Prime has five anti-drift mechanisms.

### 1. The Dependency Map

`shared/dependency_map.md` is a change propagation registry — a table that says: **when this file changes, these other files must also be checked and updated.**

```
  Example chain:

  Source: agents/synthesizer/theses/personalization_paradox_v0.2.md
    └── Depends: agents/writer/drafts/PP-001_substack_v0.4.md
         └── Depends: agents/writer/drafts/PP-001_linkedin_v0.2.md
              └── Depends: agents/connector/audience_maps/PP-001_brief.md
```

If the thesis changes, the Substack draft must be checked. If the Substack changes, the LinkedIn draft must be checked. If the LinkedIn draft changes, the distribution brief must be checked. The dependency map makes this mechanical — you look up the file you changed, you see what depends on it, you update those files. No memory required.

Rule 12 in `copilot-instructions.md` enforces this: "A build session isn't done when the asset is done — it's done when every dependent file is consistent."

### 2. The Integrity Check Script

`python meta/scripts/integrity_check.py` runs automated health checks:

- **Broken artifact paths** — does every path in the registry actually exist on disk?
- **Staleness** — any active item not updated in 7+ days? 14+ days?
- **Orphaned items** — items with no `next_action` that aren't done
- **Crash detection** — items stuck in `in_progress` (might be crashed sessions)
- **Dependency freshness** — are dependency chains current?

Output is categorized by severity: 🔴 critical, 🟡 warning, ℹ️ info. The session-start protocol runs this automatically and surfaces issues before any work begins.

### 3. Preview Before Propagate

Rule 17: Before making any change that affects 3+ files or restructures existing content, produce a complete change log showing:
1. What will change
2. In which files
3. The impact
4. The risk level

Parth reviews the log before any files are touched. Small additive changes proceed directly. This prevents well-intentioned propagation from introducing new drift.

### 4. Session-End Refresh

At the end of any session where state changed:
1. Update `shared/registry.json` with all status changes
2. Run `generate_dashboard.py` — regenerate dashboard and projects index
3. Run `integrity_check.py` — verify no broken paths or drift
4. Run Learning Loop Protocol:
   - Did this session produce a reusable pattern? → Capture it.
   - Check Propagation Tracker — any unpushed items? → Push them.
   - Did we build something with a reusable methodology? → Flag it as a potential toolkit.

### 5. Copilot-Instructions as the Constitution

`.github/copilot-instructions.md` is auto-injected into every VS Code Copilot Chat session. It contains 24 rules that every agent reads on startup:

- Rule 1: Context Verification Gate
- Rule 3: Voice rules on ALL artifacts
- Rule 5: Production order (Substack first)
- Rule 11: Learning capture
- Rule 12: Change propagation
- Rule 15: Skills check before acting
- Rule 16: Plan before build
- Rule 17: Preview before propagate
- Rule 22: Evaluation independence
- Rule 23: Execute methodology step-by-step
- ...and 14 more

These rules are the **constitutional layer** of the system. Individual agent prompts can add rules but can't override these. When a new learning is important enough to be system-wide, it graduates from `learnings.md` to a numbered rule in `copilot-instructions.md`.

---

## How the System Recursively Improves Itself

This is the mechanism that separates Agent Prime from a collection of prompts. Every session makes the next one better — not metaphorically, but through concrete, traceable mechanisms.

### The Recursive Loop

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │  GOALS   │────▶│  AGENTS  │────▶│ OUTPUTS  │────▶│ LEARNING │
  │          │     │  execute  │     │ artifacts│     │ captured │
  └──────────┘     └──────────┘     └──────────┘     └────┬─────┘
       ▲                                                   │
       │               THE RECURSIVE LOOP                  │
       │                                                   │
       │           ┌──────────────────┐                    │
       └───────────│  System evolves  │◀───────────────────┘
                   │  agents improve  │
                   │  quality rises   │
                   │  new agents spawn│
                   └──────────────────┘
```

### Five Concrete Ways the System Improves Itself

**1. Feedback → Rules → Better Output**
Every correction generates a learning. Every learning propagates to agent prompts. Every agent prompt now contains its accumulated corrections. Output quality ratchets up — the same mistake can't recur because the rule preventing it is structurally embedded.

Real trajectory: Writer v0.1 (14% philosophy, long sentences, false discovery framing, 11 "not X but Y" instances) → Writer v0.4 (≤10% philosophy, short sentences, banned constructions, self-implicating tone). Same AI model. Different encoded knowledge.

**2. Missing Capabilities → New Agents**
When a goal needs a capability the system doesn't have, a new agent gets built:

| Gap Detected | Agent Spawned | When |
|--------------|---------------|------|
| "We need to validate thesis claims empirically" | Experimenter | Week 1 |
| "We need rigorous planning before building" | Planner | Week 2 |
| "We need investment-grade industry analysis" | Industry Analyst | Week 3 |
| "We need multi-lens stock valuation" | Investment Analyst | Week 3 |
| "We need someone to execute plans reliably" | Builder | Week 3 |

Each new agent is built using patterns learned from building the previous agents — the Agent Design learnings (AD1–AD11) are the accumulated knowledge of what works and what doesn't. Rule 18 requires reading ALL of these before building any new agent.

**3. Methodology Refinement Through Use**
Agent methodologies improve through actual use:
- Industry Analyst v1 ran on AI Robotics → exposed 6 gaps (no ETF mapping, no contrarian signals, no macro risks, position anchoring, weak handoff threads, generic filenames) → all 6 became permanent methodology improvements
- Investment Analyst v1 → Kill Gate 2 feedback revealed missing Stress Test lens → became the 4th analytical lens
- Writer methodology → Andrew Chen repost exposed that context verification gate was being skipped for short-form content → gate made mandatory for ALL formats

**4. Process Learnings Become System Rules**
When a process failure repeats, it graduates from a learning to a constitutional rule:

```
  Process failure → Learning captured → Pattern confirmed → Rule added

  Example:
  "PLN-003 gap demo redesigned but plan had 9 stale sections"
    → P5: "Change propagation is not optional"
    → dependency_map.md created
    → Rule 12 in copilot-instructions.md: "A build session isn't done
       when the asset is done — it's done when every dependent file is consistent."
```

**5. Skills Extraction: Making Knowledge Portable**
When an agent's methodology proves valuable, it gets extracted into a portable **skill file** (`shared/toolkits/skills/`) — a standalone methodology that any AI (not just Agent Prime agents) can use. The agent retains its full prompt with identity and context; the skill carries just the methodology, with a clean input/output contract.

This is how the system's knowledge compounds beyond its own boundaries: Agent Prime develops the methodology internally, validates it through real use, then packages it for external distribution.

### Meta-Thinking: The System Monitors Itself

Agent Prime doesn't just work on Parth's goals — it monitors its own health and proposes its own improvements. Several mechanisms drive this:

**The Session-End Learning Sweep (Rule 19):**
Before closing any session, explicitly check: "Did we learn anything this session that should be captured in `shared/learnings.md`?" If yes, capture immediately. If no, state "No new learnings this session." This prevents the most common failure mode in learning systems — capturing knowledge sometimes but not consistently.

**The Integrity Check as Self-Diagnosis:**
The integrity script isn't just a health check — it's a **system reflection tool**. When it finds 5 stale items, that's not just a task management problem — it's a signal about workflow friction. When it finds broken artifact paths, that's a signal about naming or organization problems. The patterns in integrity failures become system improvement candidates.

**The Ideas Backlog as System Evolution Queue:**
`shared/ideas_backlog.md` is a cross-agent parking lot for future ideas. Some of these ideas are about the system itself:
- "Recursive Agent" — an agent that monitors and improves the overall system
- "Agent Architect" — codifying the agent design process itself
- "Autonomous Agents" — reducing Parth's involvement for low-risk operations

When promoted, these become SYS-type projects in the registry — system improvements that make Agent Prime better at making Agent Prime better.

**Change Propagation as Coherence Enforcement:**
The dependency map doesn't just prevent drift — it reveals the system's actual structure. Where dependencies are dense (many files depending on `shared/context.md`), the system is tightly coupled. Where dependencies are sparse, components are independent. This structural visibility enables informed decisions about where to invest in decoupling vs. where tight coupling is appropriate.

---

## The Knowledge Engineering Layer

The agents aren't just prompt templates. They carry **encoded expertise** — the thinking models, evidence hierarchies, and quality standards that separate expert output from generic AI responses.

```
  Layer 1: Decision Architecture    ← Scoring rubrics, decision tables, multi-lens frameworks
  Layer 2: Evidence Standards       ← 6-tier evidence hierarchy, source verification, staleness flags
  Layer 3: Calibration System       ← Confidence levels, adversarial critique, epistemic failure modes
  Layer 4: Output Architecture      ← Document skeletons, formatting rules, naming conventions
```

Most people build Layer 4 (templates) and stop. The largest quality gap lives in Layers 1–3. This is the difference between telling AI *what to do* and giving it *what it needs to think well*.

### The Evidence Hierarchy

Agent Prime doesn't treat all evidence equally:

```
  Tier 1: Empirical data, verified metrics, published benchmarks
  Tier 2: Peer-reviewed research, institutional reports (ARK, McKinsey)
  Tier 3: Industry analysis, expert commentary, earnings data
  Tier 4: Logical reasoning, structural analysis, framework application
  Tier 5: Personal experience, practitioner observation
  Tier 6: AI-generated synthesis (requires verification)
```

Every claim carries provenance — where it came from, whether the source was verified, how stale it might be. Hallucinated citations (like the fabricated arxiv link in v0.4 of PP-001) are caught by the source verification protocol: every URL must carry a `url_verified: true/false` flag. Unverified links are marked `[LINK UNVERIFIED]` inline, preventing them from reaching published output.

### The Epistemic Guardrails

Nine failure modes, documented in `shared/context.md`, apply to every agent:

1. **Premature Coherence** — AI produces clean explanations too early
2. **Analogy Capture** — an analogy starts driving the inquiry instead of testing it
3. **Teleology Smuggling** — purpose or progress quietly enters the model uninvited
4. **Category Collapse** — distinct layers collapse into one another
5. **Deference Drift** — the human stops pushing back
6. **Surface Abstraction** — elegant language with low explanatory power
7. **Endless Refinement Loop** — minor improvements without structural change
8. **Forced Synthesis** — different lenses forced to agree when they shouldn't
9. **Mistaking Output for Insight** — text production confused with understanding

Each failure mode has a guardrail — a specific question the agent asks itself to detect and correct the failure. These aren't generic AI safety measures — they're epistemic guardrails for the *quality of thinking itself.*

---

## The Three Levels

**Level 1** — Give AI your thinking model. Not data. Your frameworks, your evidence standards, your quality bar. 5x better output tomorrow.

**Level 2** — Make AI your thinking partner. It challenges you, not agrees with you. Each conversation sharpens your mental model.

**Level 3** — Build AI as infrastructure. A system of agents pursuing your goals. Every session makes the next one smarter. Recursive loops. **A system to build systems.**

> Most people are at Level 0.1. We need to do Level 1 and 2 very well.

---

## Why This Pattern Matters

Agent Prime is an instance, not a product. The pattern is portable:

1. **Define goals** — what you're trying to accomplish (any domain, any scale)
2. **Compose agents** — each encodes a capability with real expertise
3. **Build pipelines** — chain agents into workflows that serve those goals
4. **Close the loop** — every output feeds back, every mistake becomes a rule
5. **The system compounds** — month 3 is unrecognizable from month 1

The tools are markdown files, VS Code, and whichever AI is in the conversation. No special infrastructure. No vendor lock-in. Portable across every AI platform.

### What You Need to Build Your Own

```
  INFRASTRUCTURE:

  Text editor (VS Code)         ← Where agents live
  AI model (any)                ← The reasoning engine
  Markdown files                ← Memory, prompts, state, learnings
  A few Python scripts          ← Briefing generator, dashboard, integrity check

  INTELLECTUAL WORK:

  Your thinking model           ← How YOU reason (not generic frameworks)
  Your quality bar              ← What good output looks like in YOUR domain
  Your evidence standards       ← What counts as proof in YOUR work
  Your failure modes            ← How YOUR thinking goes wrong
  Willingness to correct        ← Every correction compounds. Skip one, lose forever.
```

No databases. No vector stores. No APIs. No cloud services. Markdown and discipline.

**Gradatim, Ferociter!**

---

*Built with VS Code, Claude, markdown files, and whichever AI is in the conversation. v3 — 2026-03-11.*
