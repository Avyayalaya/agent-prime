# Guardrails

Structured validation gates that apply to agent inputs and outputs. Each guardrail is a referenceable artifact with a trigger condition, validation logic, and enforcement action.

## How Guardrails Work

Guardrails are **specs, not code** — they describe what to check, when, and what to do if the check fails. Every agent reads the `registry.yaml` to know which guardrails apply to it. Guardrails are enforced at two points:

1. **Input guardrails** — validate context/inputs BEFORE the agent produces output
2. **Output guardrails** — validate output BEFORE it leaves the agent

## Files

| Guardrail | Type | Applies To | CLAUDE.md Source |
|-----------|------|------------|------------------|
| [nda_filter.md](nda_filter.md) | output | All agents | Rule 4 |
| [voice_check.md](voice_check.md) | output | Writer, Connector, all external-facing | Rule 3, Rule 31 |
| [quality_bar.md](quality_bar.md) | output | All agents | Rule 10, Rule 23 |
| [context_gate.md](context_gate.md) | input | All agents | Rule 1, Rule 25 |
| [permission_tier.md](permission_tier.md) | permission | Emissary | Rules 41-43 |
| [production_order.md](production_order.md) | output | Writer | Rule 5 |
| [publish_parity.md](publish_parity.md) | output | Planner, Builder | Rule 21, Rule 33 |
| [registry.yaml](registry.yaml) | config | — | — |

## Usage

When producing output, agents check:
1. Load `registry.yaml` to find applicable guardrails
2. For each input guardrail: verify before starting work
3. For each output guardrail: verify before delivering output
4. If any guardrail fails: stop and report (block), or flag and continue (warn)
