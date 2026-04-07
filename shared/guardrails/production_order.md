# Production Order

> **Type:** Output guardrail
> **Action:** Block — compressed versions cannot be produced before the full argument
> **Applies to:** Writer
> **Source:** CLAUDE.md Rule 5

---

## Trigger

Activates when Writer is producing multi-channel content from a thesis or analysis. Specifically when more than one format is requested (Substack + LinkedIn, or Article + Conference, etc.).

## Validation Logic

### The Order (non-negotiable)

```
1. Substack (long-form, full argument)     -> FIRST
2. LinkedIn (compressed, derivative)        -> SECOND
3. Conference (distilled, presentation)     -> THIRD
```

### Why This Order

The full argument must exist before compression. Writing the compressed version first produces omission, not compression (Rule 31). The Substack version is the canonical source; all other formats derive from it.

### Enforcement

- Before producing a LinkedIn post for a thesis: verify Substack draft exists
- Before producing a conference proposal: verify LinkedIn post exists (or Substack at minimum)
- If only one format is requested and it's not Substack: proceed (single-format requests bypass ordering)

## Validation Checklist

- [ ] If multi-channel: Substack version exists before LinkedIn version
- [ ] If multi-channel: LinkedIn version exists before Conference version
- [ ] Compressed versions visibly derive from the full argument (not independent drafts)

## On Failure

**Block.** Tell the user the production order requires the long-form version first. Offer to produce the Substack version.
