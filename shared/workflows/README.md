# Declarative Workflow Specifications

> **Status:** Documentation specs — not runtime engines
> **Origin:** VoltAgent analysis (2026-04-07) — absorbing the workflow-as-spec pattern

---

## What Are These?

Agent Prime's orchestration patterns are implicit — encoded in agent prompts, dispatch successor rules, and CLAUDE.md rules. A new reader (human or AI) must read 5+ files to understand "how does research become a published article?"

These YAML files make implicit patterns explicit. They are **documentation specs**, not executable code — any agent (or future automation) can read them to understand the full pipeline without reading all agent prompts.

## How to Read a Workflow

Each YAML file defines:

| Field | Meaning |
|-------|---------|
| `id` | Unique workflow identifier |
| `name` | Human-readable name |
| `description` | What the workflow accomplishes |
| `trigger` | What kicks off this workflow |
| `steps` | Ordered list of pipeline steps |

Each **step** has:

| Field | Meaning |
|-------|---------|
| `id` | Step identifier (unique within workflow) |
| `agent` | Which Agent Prime agent executes this step |
| `decision_type` | `auto` (no approval), `review` (operator reviews), `approve` (operator must approve), `input` (operator provides) |
| `description` | What happens in this step |
| `input` | What this step consumes |
| `output` | What this step produces |
| `successor` | Next step (if not simply the next in the list) |
| `quality_gate` | Checks that must pass before moving on |
| `suspend_if` / `resume_with` | Conditions for pausing and resuming |
| `permission_tier` | Emissary tier (1=auto, 2=batch-approved, 3=human-only) |

## Workflow Index

| File | Pipeline | Steps |
|------|----------|-------|
| `research-to-publish.yaml` | Thesis to Article to Distribution | 7 steps: brain_dump > signal_scan > synthesize > write_longform > write_compressed > distribute > publish |
| `idea-to-build.yaml` | Idea to Plan to Build to Ship | 9 steps: register > plan (4 stages) > capability_map > preflight > build > review |
| `signal-to-action.yaml` | Sense to Process to Permission to Execute | 4 steps: sense > process > permission > execute |
| `inbound-to-response.yaml` | Log to Assess to Draft to Send | 4 steps: log > assess > draft_response > send |

## Design Notes

- These are **specs, not runtime engines** — agents read them as context, not as executable code
- Each workflow references Agent Prime rules (by number) where relevant
- The `suspend_if` / `resume_with` pattern is borrowed from VoltAgent's workflow engine
- `decision_type` maps directly to existing dispatch types (auto/approve/review/input)
- `quality_gate` references guardrail files (once P1b is complete)
- Workflows can be loaded by Prime during session start to determine what pipeline a task belongs to
