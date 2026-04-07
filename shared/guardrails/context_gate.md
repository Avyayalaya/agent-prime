# Context Verification Gate

> **Type:** Input guardrail
> **Action:** Block — no output produced until gate passes
> **Applies to:** All agents
> **Source:** CLAUDE.md Rule 1, Rule 25

---

## Trigger

Activates BEFORE any agent produces ANY output. This is the first check, every time.

## Validation Logic

### The Gate (Rule 1)
Every agent prompt has a Context Verification Gate at the top listing required files. Before producing ANY output, verify every required file has been actually read into the conversation.

### No Exceptions for Format Length (Rule 25)
A 200-word LinkedIn post requires the same gate as a 4,000-word Substack article. The gate does not scale with output length.

**Two confirmed failures (P8, P17):** Skipping the gate because "this is short" always produces generic output lacking the user's thinking, voice, and framework.

### Required Files (minimum for any agent)
These files must be loaded regardless of which agent is invoked:

| File | Why |
|------|-----|
| Agent's own `prompt.md` | Identity and methodology |
| `shared/learnings.md` | Accumulated corrections (hard constraints) |
| `shared/instincts/*.yaml` | Machine-readable learnings matching agent's `applies_to` |

### Additional per-agent requirements
Each agent's prompt.md specifies additional required files. Common patterns:
- Writer: `shared/voice_corpus/voice_recipe.md`, `shared/context.md`
- Scout: `shared/resource_registry.md`, `shared/platform_configs/`
- Synthesizer: `shared/context.md`, `prime/proof_stack.json`
- Builder: `shared/learnings.md` (Agent Design category), Build Handoff Spec

### Instinct Loading (Rule 38)
Also load relevant instinct YAML files from `shared/instincts/`. Match by agent role to `applies_to` field:
- Writer: `voice.yaml`, `framing.yaml`, `quality.yaml`, `surface_craft.yaml`
- Builder: `agent_design.yaml`, `build.yaml`
- All agents: `process.yaml`, `quality.yaml` (applies_to: ["*"])

## Validation Checklist

- [ ] Agent's prompt.md has been read (not just referenced)
- [ ] `shared/learnings.md` has been read
- [ ] Relevant instinct YAML files loaded
- [ ] All files in agent's Context Verification Gate read via tool call
- [ ] No file marked as "needed" without being actually read

## On Failure

**Block.** Stop and ask the user to provide the missing file. Do not proceed with degraded context. Silent quality degradation is the #1 system risk.
