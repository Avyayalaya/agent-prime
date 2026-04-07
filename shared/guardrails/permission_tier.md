# Permission Tier

> **Type:** Permission gate
> **Action:** Block — external actions must pass tier check before execution
> **Applies to:** Emissary
> **Source:** CLAUDE.md Rules 41-43; `agents/emissary/prompt.md`

---

## Trigger

Activates when ANY Agent Prime output is about to cross the boundary into the external world — publishing, sending, posting, commenting, or any action visible to people outside Agent Prime.

## The 3-Tier Model

### Tier 1: Auto-Execute
**Criteria:** Reversible + low-visibility + internal-facing

**Examples:**
- GitHub stars/watches
- Calendar blocks
- Internal bookmark saves
- Local file operations

**Promotion rule (EMI-001):** New action types start at Tier 2. Promoted to Tier 1 after 10+ consecutive approvals with zero rejections.

### Tier 2: Batch-Approved
**Criteria:** External-facing + semi-reversible

**Examples:**
- LinkedIn posts
- Substack publications
- Email to new contacts
- Conference proposals
- GitHub PR comments on public repos
- Repost captions and Notes

**Governance:**
- The operator reviews and approves in batches (weekly digest)
- Dead man's switch (EMI-003): If the operator hasn't reviewed in 7 days, ALL Tier 2 actions pause
- LinkedIn posts, emails to new contacts, and conference proposals NEVER auto-promote — permanently Tier 2

### Tier 3: Human-Only
**Criteria:** Irreversible + high-stakes

**Examples:**
- Job offers or negotiations
- Live presentations
- Financial commitments
- Legal communications
- Public statements that can't be retracted

**Governance:**
- The operator must explicitly execute these themselves
- Agent Prime can draft and prepare, but never execute

## Demotion Rules

**EMI-002:** Demotion from Tier 1 is immediate on any negative signal (rejection, complaint, unintended consequence). No gradual demotion — one failure drops the action type back to Tier 2.

## Workflow

```
Agent produces artifact
  -> Emissary queues to action_queue.jsonl
  -> Permission tier applied
  -> Tier 1: execute immediately, log to action_log.jsonl
  -> Tier 2: hold for batch review (weekly digest)
  -> Tier 3: hold for operator's manual execution
```

## Validation Checklist

- [ ] Action classified into correct tier
- [ ] Tier 2+ actions queued, not executed
- [ ] Dead man's switch checked (last review < 7 days ago)
- [ ] Action logged to action_log.jsonl with full context
- [ ] No new action type assigned Tier 1 without promotion history

## On Failure

**Block.** If tier cannot be determined, default to Tier 3 (human-only). Never execute an unclassified external action.
