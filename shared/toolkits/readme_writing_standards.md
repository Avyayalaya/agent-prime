# README Writing Standards

Learnings from 4 iterations on pm-skills-arsenal README + analysis of 7 high-star repos (htmx, FastAPI, shadcn/ui, Zod, Pydantic, fabric, promptfoo).

## Core Principles

1. **Don't justify your existence.** If the product is good, a long README looks defensive. shadcn/ui has 107k stars with a README that fits on one screen.

2. **Describe outcomes, not ingredients.** "Scores competitive advantages by durability" tells you more than "uses Hamilton Helmer's 7 Powers framework." Framework names belong inside the product, not on the box.

3. **Never name-drop frameworks as if they're well known.** Most readers don't know them. Listing 10 framework names signals insecurity, not depth. Describe what the frameworks DO.

4. **Radical brevity is a confidence signal.** Every sentence that explains why the product matters is a sentence that implies it might not. Cut until it hurts, then cut more.

5. **Show the transformation, not the tool.** Pydantic shows messy input becoming clean output. The delta IS the pitch. But do it naturally — a labeled "Before / After" section reads like a LinkedIn carousel.

6. **Every claim gets immediate proof.** Screenshot after assertion. Number after value prop. Command after "easy to use." Never assert and move on.

7. **No comparison tables against competitors.** htmx, shadcn/ui, Zod — none compare themselves to alternatives. The product either speaks for itself or it doesn't.

8. **Don't over-explain to smart readers.** PMs reading a PM skills repo are intelligent. Don't define what a North Star metric is. Don't explain why evidence tiers matter. Trust the reader.

## Anti-Patterns (from our iterations)

- **"Not a template, it's a codex"** — defensive framing. Saying what you're NOT is weaker than showing what you ARE.
- **Before/After sections** — feels like marketing, not confidence. If you must show the delta, do it through a sample output, not a labeled comparison.
- **"10-year veteran" / "senior PM"** — caps your ceiling. "Output a PM cannot create unaided" or "the world's best analyst" frames upward.
- **Design Principles sections** — the principles should be visible in the output, not stated in the README.
- **"What Makes These Different"** — if you have to explain why you're different, the product isn't showing it clearly enough.
- **Long contributing sections** — one line. High bar. Link to details elsewhere.

## Structural Pattern (from best repos)

```
1. One-line hook (what it IS, not what problem it solves)
2. One paragraph: what you get (outcomes, not features)
3. Skills/features listed tersely (output-focused, no ingredient lists)
4. Install (2-3 lines max)
5. Proof (benchmark table, no preamble)
6. License line
```

Total: fits on one screen. Everything else lives in docs.

## Reference READMEs

| Repo | Stars | Key Pattern |
|---|---|---|
| shadcn/ui | 107k | Radical brevity. One sentence. Links to docs. |
| FastAPI | 95k | Quantified outcomes first, code example second |
| htmx | 47k | Rhetorical questions that make status quo absurd |
| Zod | 42k | Tagline, example, properties — three things done |
| fabric | 39k | Philosophical reframe as opener |
| Pydantic | 27k | Show the transformation through code |
| promptfoo | 10k | Every claim gets immediate proof |

---

*Created: 2026-02-20. From pm-skills-arsenal README iterations.*
