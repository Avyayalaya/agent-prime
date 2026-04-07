# NDA Filter

> **Type:** Output guardrail
> **Action:** Block — output must not be delivered if this fails
> **Applies to:** All agents
> **Source:** CLAUDE.md Rule 4

---

## Trigger

Activates on ALL output that could reach external channels — articles, posts, emails, conference materials, public repos, outreach, and any artifact that passes through Emissary.

Also activates on internal artifacts that reference specific companies where the operator has NDA obligations.

## Validation Logic

The output MUST NOT contain:

### Hard blocks (immediate rejection)
- Internal employer product roadmaps, unreleased features, or internal metrics
- Any data from internal dashboards, internal wikis, or internal communications
- Code snippets from proprietary codebases
- Customer names, deal sizes, or revenue figures from internal sources
- Internal project codenames or internal team names
- Specific performance metrics or telemetry data from internal systems

### Reframing required (transform, don't block)
- Industry observations derived from internal experience — frame as "industry observation" or "personal framework"
- Patterns observed across multiple employers — frame as "pattern across [N] companies" without naming
- Technical architecture insights from internal work — frame as general best practices

## Validation Checklist

- [ ] No company-internal data, metrics, or roadmaps referenced
- [ ] No unreleased features or internal project names mentioned
- [ ] Insights framed as industry observations or personal frameworks
- [ ] No specific customer or partner names from internal context
- [ ] Code examples are generic or from public sources only

## On Failure

**Block.** Do not deliver the output. Report the specific violation to the user and suggest a reframing.
