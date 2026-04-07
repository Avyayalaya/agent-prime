# Voice Check

> **Type:** Output guardrail
> **Action:** Block — external-facing output must match voice DNA
> **Applies to:** Writer, Connector, Emissary, Synthesizer (external theses)
> **Source:** CLAUDE.md Rule 3, Rule 31; `shared/voice_corpus/voice_recipe.md`

---

## Trigger

Activates on ALL external-facing content: articles, LinkedIn posts, email outreach, conference proposals, survey text, session descriptions, repost captions, Notes. Also applies to internal documents that will be shown to stakeholders.

Rule 3: "These rules apply to ALL artifacts — articles, emails, briefs, decks, survey text, session descriptions, any public-facing text. Not just Writer-produced content."

## Validation Logic

### Voice DNA (9 ingredients — from voice_recipe.md)
Output must match the operator's voice: blunt, conversational, self-implicating, short sentences.

### CXO Test
Would a CPO say this in a board meeting? If not, it fails.

### Hard Bans (immediate rejection)
- "not X but Y" constructions — say the positive thing directly
- Defining things by what they aren't — say what it IS
- Hype language: "question reality", "visceral", "recontextualize"
- Essayistic, literary, or philosophical-professor tone
- Generic AI platitudes ("in today's rapidly evolving landscape...")

### Compression vs. Omission (Rule 31)
For short-form content (LinkedIn posts, repost captions, Notes):
- **Compression** = fitting the full argument into fewer words (PASS)
- **Omission** = picking one fact and padding around it (FAIL)
- A 220-word post with one citation and no framework is omission
- A 300-word post with three evidence layers + structural insight + product implication is compression
- The source thesis must be visibly compressed, not abandoned

### Channel-Specific Register
Each channel has a voice register defined in voice_recipe.md. The output must match the register for its target channel.

## Validation Checklist

- [ ] Blunt and conversational, not essayistic or literary
- [ ] Short sentences (avg <20 words)
- [ ] Self-implicating where relevant (includes the operator in the problem)
- [ ] No banned constructions ("not X but Y", hype language)
- [ ] CXO test passes — a CPO would say this
- [ ] Channel register matches target platform
- [ ] For short-form: compression, not omission — source thesis visibly compressed

## On Failure

**Block.** Rewrite the failing passages before delivering. Report which specific voice rules were violated.
