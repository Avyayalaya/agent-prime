---
name: multi-channel-publishing
description: "Use when repurposing long-form content into channel-specific formats — LinkedIn posts, conference abstracts, podcast briefs, newsletter summaries, tweet threads, or spoken scripts. Encodes compression methodology, channel format rules, evidence density calibration, and audience adaptation. Produces channel-ready derivatives, not summaries."
version: "1.0.0"
type: "codex"
tags: ["Content", "Publishing", "Distribution", "Strategy"]
created: "2026-03-12"
valid_until: "2026-09-12"
derived_from: "agents/writer/prompt.md, shared/learnings.md (P2, P8, P10, P16, P17)"
tested_with: []
license: "MIT"
capability_summary: "Produces channel-specific content derivatives from a source document using evidence-calibrated compression, maintaining thesis fidelity across formats including LinkedIn posts, conference abstracts, spoken scripts, podcast briefs, and newsletter summaries."
input_schema:
  source_document: "string — the full source content to derive from (article, thesis, essay)"
  target_channel: "enum[linkedin_post, linkedin_article, conference_abstract, spoken_script, podcast_brief, newsletter, tweet_thread, executive_briefing]"
  audience_context: "string — optional, who will read this derivative and what they care about"
  voice_reference: "string — optional, path to voice/style guide or example of author's writing"
output_schema:
  channel_derivative: "The formatted content for the target channel, ready to publish"
  compression_log: "What was kept, what was cut, and why — traces back to source"
  thesis_fidelity_check: "Verification that the core claim survived compression"
  quality_check: "Pass/fail on each quality dimension"
example_invocation: "examples/USE_CASES.md"
---

## Purpose

Produce a channel-ready content derivative from a source document — not a summary, but a structurally adapted compression that preserves the source's thesis, maintains evidence fidelity, and conforms to the target channel's format constraints, audience expectations, and hook conventions. The output is a publishable artifact with a compression log proving nothing was lost by accident.

## When to Use / When NOT to Use

**Use this skill when:**
- Repurposing a long-form article (Substack, blog, thesis) into a LinkedIn post, conference abstract, podcast brief, newsletter, tweet thread, spoken script, or executive briefing
- Deriving a compressed format from a full argument (compression direction: long → short)
- Adapting content for a new audience or channel while preserving the core claim
- Producing a spoken script from written beats or a conference proposal
- Creating a distribution package (multiple derivatives from one source)

**Do NOT use this skill when:**
- You need to write the original long-form piece (use the source-appropriate writing methodology first — P2: Substack first, derivatives second)
- You need to combine multiple sources into one synthesis (use Narrative Building or Problem Framing)
- You need to translate between languages (this is structural adaptation, not linguistic translation)
- The source document is internal/confidential and the target channel is public (Context Gate will catch this, but flag it early)
- You need a generic summary for no specific audience or channel (summaries without channel constraints produce FM-1: Summary, Not Derivative)

**Anti-inputs (what this skill does NOT handle):**
- Original content creation from scratch (this skill DERIVES, it does not originate)
- Content strategy or editorial calendar planning (this is a single-derivation tool)
- SEO optimization (channel format rules include discoverability principles, but this is not an SEO skill)
- Visual design or layout (this produces text; design is a separate discipline)

---

## Context Gate (Step -1) — Mandatory Pre-Check

Before deriving ANY content, answer these four questions. If any answer is "No" or "Uncertain," STOP and resolve before proceeding.

| # | Gate Question | Pass Condition | If Fail |
|---|---------------|----------------|---------|
| 1 | **Does a source document exist?** | A complete, published or finalized long-form piece is available. Not notes. Not an outline. Not bullet points. | STOP. Write the source document first. P2: "Writing short before writing long produces shallow thinking disguised as brevity." |
| 2 | **Is the target channel appropriate for this content?** | The source's thesis can survive compression to the target format without becoming misleading or trivial. | STOP. Either choose a different channel or acknowledge the derivation will be a pointer ("read the full piece"), not a standalone argument. |
| 3 | **Is the source → channel direction public-safe?** | The source does not contain confidential, internal-only, or NDA-protected material that would be exposed on the target channel. | STOP. Redact or abstract the sensitive content before deriving. Flag specific sections that cannot survive the public/private boundary. |
| 4 | **Do you have the author's voice reference?** | Either a voice/style guide, previous published examples on this channel, or explicit voice constraints are loaded. | PROCEED WITH CAUTION. Flag `[VOICE-UNGROUNDED]` on the output. The derivative will default to generic professional tone. P8/P17: "Format length does not exempt the context verification gate." |

**Context Gate Decision Table:**

| Source Type | Appropriate Channels | Channels to Avoid | Why |
|---|---|---|---|
| Published Substack/blog (2500-4000 words) | LinkedIn post, LinkedIn article, conference abstract, newsletter, tweet thread, podcast brief | Executive briefing (unless the topic is strategy) | Full argument available; any compression direction works |
| Strategic thesis (internal) | Executive briefing, conference abstract (if anonymized), podcast brief (if non-confidential) | LinkedIn post, tweet thread | Confidentiality risk; thesis jargon needs heavy translation for public channels |
| Conference talk proposal | Spoken script, podcast brief, newsletter | LinkedIn post (too structured), tweet thread (too formal) | Proposals are structural; they derive naturally into performance formats, not feed formats |
| Research synthesis | LinkedIn article, newsletter, executive briefing, podcast brief | Tweet thread (evidence density too low), LinkedIn post (too much to compress) | Research needs space for evidence; ultra-short formats lose the substance |
| Essay / personal reflection | LinkedIn post, newsletter, Substack Note | Conference abstract (wrong register), executive briefing (wrong audience) | Personal voice is the asset; channels that strip voice lose the value |

---

## Format Rules (Read First)

These rules govern every output. They are quality enforcement mechanisms, not style preferences.

1. **Compression is not omission.** Every derivative must visibly contain the source's compressed argument — thesis, evidence beats, and framework logic — not a single extracted fact padded to length. A 300-word post with three evidence layers and a structural insight is compression. A 220-word post with one data point and no framework is omission (P16). If you cannot fit the argument, choose a longer channel format.

2. **Source document first, derivative second. Always.** Never write the compressed version before the full argument exists (P2). If the source doesn't exist, this skill does not apply. The production order is inviolable: full argument → compressed derivatives.

3. **Per-channel format constraints are hard limits.** Word counts, structural requirements, and hook conventions per channel are not guidelines — they are constraints derived from how each platform's algorithm and audience behavior reward content. Exceeding LinkedIn's fold (first 2-3 lines) with a philosophical opening is a format violation, not a style choice.

4. **Thesis statement survives verbatim or near-verbatim.** The one-sentence core claim from the source must appear in every derivative. If it cannot fit, the derivative must contain a faithful compression that a reader could reconstruct the original thesis from. Thesis Drift (FM-2) is the highest-severity failure mode.

5. **Evidence density scales with channel length.** Long-form: 5+ evidence layers. LinkedIn post: 2-3 compressed evidence beats. Tweet thread: 1 evidence point per tweet. Conference abstract: promise of evidence, not the evidence itself. The Evidence Density Calibration framework (Framework 4) provides exact targets.

6. **Hook archetype must match channel.** A Substack opening (vivid scenario, slow build) deployed on LinkedIn (where 2 lines decide whether the reader continues) is a channel-blind failure (FM-5). The Hook Adaptation framework (Framework 3) maps archetypes to channels.

7. **Voice consistency across derivatives.** All derivatives from the same source must sound like the same author. If the source is written in first person with short sentences and self-implicating humor, the LinkedIn post cannot read like a consultant's press release. Voice Fracture (FM-7) is detectable by reading the source and derivative side-by-side.

8. **Cite what survives compression.** When an evidence beat from the source survives into a derivative, the citation or attribution must survive too. Uncited claims in a derivative that were cited in the source is evidence laundering.

9. **The Compression Log is mandatory output.** Every derivative ships with a log showing: what was kept (with source location), what was cut (with reason), and what was adapted (with the adaptation rationale). This makes the derivation auditable and prevents FM-3 (Evidence Omission) from going undetected.

---

## Output Template (Mandatory Document Skeleton)

Every channel derivative MUST include these sections. Copy this skeleton and fill it in. The channel-specific content section varies by target channel (see Channel Format Taxonomy below for the exact structure per channel).

```markdown
# Channel Derivative: [Source Title] → [Target Channel]

> **Source:** [Title and location of source document]
> **Target channel:** [linkedin_post | linkedin_article | conference_abstract | spoken_script | podcast_brief | newsletter | tweet_thread | executive_briefing]
> **Date:** [YYYY-MM-DD] | **Author voice:** [Grounded / Ungrounded] | **Compression ratio:** [source words → derivative words, X:1]

---

## Context Gate Results

| Gate | Result | Notes |
|---|---|---|
| Source exists? | ✅/❌ | |
| Channel appropriate? | ✅/❌ | |
| Public-safe? | ✅/❌ | |
| Voice grounded? | ✅/❌ | |

---

## Step 0: Framework Selection

| Source type | Target channel | Primary frameworks | Supporting frameworks | Skipped (why) |
|---|---|---|---|---|
| [e.g., "Published Substack"] | [e.g., "LinkedIn post"] | [e.g., "Compression Protocol, Hook Adaptation, Evidence Density"] | [e.g., "Audience Context Matching"] | [e.g., "Spoken Script Derivation — wrong channel"] |

---

## Thesis Fidelity Check

| Dimension | Source | Derivative | Verdict |
|---|---|---|---|
| Core claim (verbatim or compressed) | [Source thesis sentence] | [Derivative thesis sentence] | ✅ Preserved / ⚠️ Compressed / ❌ Drifted |
| Key evidence beats preserved | [Count in source] | [Count in derivative] | [X of Y preserved] |
| Counterargument preserved | [Strongest counterargument in source] | [Present / Absent in derivative] | ✅/❌ |
| Framework/structural insight | [Framework in source] | [Compressed/present in derivative] | ✅/❌ |

---

## [Channel-Specific Content Section]

[The actual derivative content — structure varies by channel. See Channel Format Taxonomy.]

---

## Compression Log

| Element | Source Location | Action | Rationale |
|---|---|---|---|
| [e.g., "Thesis statement"] | [e.g., "Paragraph 3"] | Kept verbatim | Core claim — non-negotiable |
| [e.g., "Evidence beat 2: Stanford study"] | [e.g., "Section 3, para 2"] | Kept, compressed | Strongest surprise factor for this audience |
| [e.g., "Philosophical layer: judgment erosion"] | [e.g., "Section 4"] | Cut | Channel constraint — LinkedIn post cannot support this depth; compressed to 1 sentence woven into evidence |
| [e.g., "Counterargument 2: privacy tradeoff"] | [e.g., "Section 6, para 3"] | Cut | Kept only the strongest counterargument (Counterargument 1) per Compression Protocol Step 6 |
| [e.g., "Framework table: 3-domain taxonomy"] | [e.g., "Section 5"] | Adapted | Compressed from table to inline list; structure preserved, visual format changed for feed readability |

---

## Audience Context Match

| Dimension | Channel default audience | This derivative's specific audience | Adaptation applied |
|---|---|---|---|
| Expertise level | [e.g., "Mixed: peers + executives + recruiters"] | [e.g., "Senior PMs at enterprise companies"] | [e.g., "Skipped basic definitions; led with strategic implication"] |
| Reading context | [e.g., "Feed scroll, 3-second attention"] | [Specific context if known] | [Adaptation] |
| What they care about | [Channel default] | [Specific if known] | [Adaptation] |

---

## Quality Check

- [ ] Thesis preserved (verbatim or faithful compression)
- [ ] Evidence density meets channel target (see Evidence Density Calibration)
- [ ] Hook archetype matches channel (see Hook Adaptation)
- [ ] Voice consistent with source author
- [ ] Format constraints met (word count, structure, platform rules)
- [ ] Compression Log complete — every cut is justified
- [ ] No uncited claims that were cited in source
- [ ] Counterargument preserved (at least one, the strongest)
- [ ] Framework/structural insight visible in derivative
- [ ] Context Gate passed before derivation began

---

## Assumption Registry

| # | Assumption | Confidence | Evidence | What would invalidate |
|---|---|---|---|---|
| 1 | [e.g., "This audience has not read the source"] | H/M/L | [basis] | [invalidation condition] |
| 2 | [e.g., "LinkedIn algorithm still rewards short paragraphs and line breaks"] | H/M/L | [basis] | [invalidation condition] |
| 3 | [e.g., "The source's evidence beats are still current"] | H/M/L | [basis] | [invalidation condition] |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
[What assumption is being made? What evidence would disprove it? Scenario where this derivative fails its purpose.]

**Weakness 2: [Title]**
[Same depth]

**Weakness 3: [Title]**
[Same depth]

---

## Revision Triggers

| Trigger | What to re-derive | Timeline |
|---|---|---|
| [e.g., "Source document is updated with new evidence"] | [Re-run derivation for all channels] | [Immediate] |
| [e.g., "Channel algorithm changes (e.g., LinkedIn changes fold behavior)"] | [Re-check format constraints] | [Within 1 week of change] |
| [e.g., "Evidence in derivative becomes stale (>6 months)"] | [Update evidence beats or add staleness flag] | [At 6-month mark] |
```

**Rules for using this template:**
1. **Do not skip sections.** If a section isn't applicable, write "Not applicable — [reason]" and move on.
2. **The Compression Log is the audit trail.** Every element from the source must appear in the log as Kept/Cut/Adapted with rationale.
3. **The channel-specific content section uses the exact structure from the Channel Format Taxonomy** for the target channel — not a generic paragraph format.
4. **Thesis Fidelity Check is completed AFTER writing the derivative** — it is a verification step, not a planning step.
5. **The Quality Check is the final gate.** If any checkbox fails, revise before delivering.

---

## Reader Navigation

### How to Read This Skill

**If you have 5 minutes:** Read the Context Gate (Step -1) and the Compression Protocol (Framework 2). These two sections give you the decision logic for whether to derive and the 7-step method for doing it.

**If you have 15 minutes:** Add the Channel Format Taxonomy (Framework 1) for your target channel and the Hook Adaptation table (Framework 3). You now have channel-specific constraints and the right opening strategy.

**If you have 30 minutes:** Read the full skill. The Evidence Density Calibration (Framework 4), Audience Context Matching (Framework 5), and Source Fidelity Verification (Framework 6) add the quality layers that separate consultant-tier from elite-tier derivatives. The Spoken Script Derivation (Framework 7) is only needed for talk/presentation outputs.

### By Role

| Role | Start here | Focus on | Skip |
|---|---|---|---|
| **Content creator / Writer** | Compression Protocol → Channel Format Taxonomy | Hook Adaptation, Evidence Density, Voice consistency rules | Spoken Script Derivation (unless producing talks) |
| **PM / Strategist** | Context Gate → Audience Context Matching | Thesis Fidelity Check, Framework Selection routing | Detailed channel format constraints (delegate to writer) |
| **Speaker / Presenter** | Spoken Script Derivation → Compression Protocol | Performance notation, SCRIPTED vs GUIDED beats, rehearsal guide | Tweet thread and newsletter formats |
| **Editor / Reviewer** | Source Fidelity Verification → Quality Check | Compression Log audit, thesis drift detection, evidence omission | Framework internals (focus on output quality) |

### Notation Key

| Symbol | Meaning |
|---|---|
| **H / M / L** | Confidence level: H (>70%), M (40-70%), L (<40%) |
| **(T1)-(T6)** | Evidence tier: T1 = behavioral data, T2 = primary research, T3 = expert analysis, T4 = industry reports, T5 = executive statements, T6 = punditry/inference |
| **O→I→R→C→W** | Observation → Implication → Response → Confidence → Watch Indicator cascade |
| `[POTENTIALLY STALE]` | Claim based on data older than 6 months |
| `[EVIDENCE-LIMITED]` | Key conclusion resting only on Tier 4-6 evidence |
| `[VOICE-UNGROUNDED]` | Derivative produced without author voice reference loaded |
| `[SCRIPTED]` | Spoken script beat: word-for-word, rehearsed to feel natural |
| `[GUIDED]` | Spoken script beat: structured talking points with key phrases bolded |
| `[PAUSE: Xs]` | Timed silence in spoken script |
| ████░░░░░░ | Progress bar: relative strength or density (visual, not decorative) |

---

## Domain Frameworks

> This section IS the knowledge weapon. Each framework is encoded with scoring rubrics, decision tables, and application rules. A writer using this skill produces derivatives that require these frameworks; without them, the output degrades to generic summarization.

### Framework 1: Channel Format Taxonomy

Structured definitions of each target channel with hard constraints. These are not guidelines — they are derived from platform algorithms, audience behavior research, and publishing failure modes.

#### LinkedIn Post (Feed Format)

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 200-350 words | LinkedIn's feed algorithm rewards engagement-per-word; posts >400 words see declining completion rates (H) |
| **Structure** | Hook (2 lines) → Thesis (1 sentence) → Evidence beats (3 compressed, 1-2 sentences each) → Framework/insight → Implication or question | The fold (first 2-3 lines before "see more") decides whether 80% of viewers read on (H) |
| **Hook placement** | First 2 lines must stop the scroll | LinkedIn shows ~210 characters before truncation on mobile (T1: platform behavior) |
| **Paragraph length** | 1-3 sentences per paragraph; use line breaks aggressively | Feed readability requires visual scannability; dense paragraphs get skipped (M) |
| **Evidence density** | 2-3 compressed beats; each beat = 1-2 sentences mixing data + observation | Enough to show thinking depth; not so much it reads as academic (H) |
| **Framework visibility** | If the source has a framework, compress it inline (list, not table) | The reader must see HOW you think, not just WHAT you read (P16) |
| **Tone** | Authoritative, conversational, short sentences; CXO test applies | Would a CPO say this in a board meeting? If not, rewrite it |
| **CTA** | Invitation, not CTA; end with a question or tension worth sitting with | "What do you think?" is lazy; a genuine question from the argument is powerful |
| **Formatting** | Bold key phrases; no hashtag spam (0-3 relevant tags); no emoji-heavy formatting | Professional register; the content is the hook, not the formatting |

**Scoring Rubric — LinkedIn Post Quality:**

| Rating | Symbol | Criteria |
|---|---|---|
| **Publishable** | 🟢 | Thesis present, 2+ evidence beats, framework visible, hook stops scroll, voice consistent, under 350 words |
| **Needs revision** | 🟡 | Missing one element: weak hook OR missing framework OR only 1 evidence beat OR voice drift |
| **Rewrite** | 🔴 | Summary not derivative (FM-1), thesis drifted (FM-2), single-fact padding (FM-6), or over word limit |

---

#### LinkedIn Article (Long-Form)

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 1000-1500 words | Compressed from Substack (2500-4000 words); must hold its own as standalone (H) |
| **Structure** | Hook → Thesis → Evidence (3 beats, 1 paragraph each) → Framework (1, the most accessible) → Strongest counterargument (2-3 sentences) → Implication → Invitation | Derivation Protocol from Writer agent: steps 1-7 applied (T1: tested methodology) |
| **Companion Sharing Post** | 4-6 short lines, under 200 words, hooks the article | The sharing post is what people see in the feed; the article is the substance |
| **Inline linking** | 2-3 key links (most important claims) | LinkedIn's renderer doesn't reward heavy linking; pick the claims that need sourcing |
| **Tone** | Same as source but tighter; authoritative and curious | The article is a compressed version of the author, not a different author |

---

#### Conference Talk Abstract

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 200-300 words | Selection committees read 50-200 abstracts; yours gets 30-60 seconds (H) |
| **Structure** | Problem (2-3 sentences: what's broken, with a surprising framing) → Insight (1-2 sentences: the pivot that reframes) → What the audience learns (2-3 takeaways, action-oriented) → Why this speaker (1-2 sentences: unique qualification) | Outcome-first for the committee; they're asking "will 500 people sit still for 25 minutes?" |
| **Title** | Provocative, memorable, tweetable; not descriptive | "The Personalization Paradox" beats "A Framework for AI Personalization" every time (H) |
| **Evidence density** | 0-1 evidence points (promise of evidence) | Abstracts sell the talk; they don't deliver it. "I'll show data from X" > the data itself |
| **Hook** | The title IS the hook; abstract opens with the problem the audience feels | Selection committees are pragmatists buying on audience appeal, not intellectual depth |
| **Tone** | Confident, outcome-oriented, slightly provocative | The abstract competes with 100 others; safe titles lose |

**Decision Table — Abstract Quality:**

| Signal | Interpretation | Action |
|---|---|---|
| Title is descriptive ("A Study of X") | Will be passed over by committee | Rewrite as provocative claim or question |
| Abstract summarizes the talk | Committee doesn't know what to expect in the room | Rewrite to show the EXPERIENCE: what happens, what the audience walks away with |
| No "why me" element | Committee can't differentiate from other proposals | Add 1-2 sentences connecting speaker's unique experience to the topic |
| >300 words | Committee stops reading | Cut to 250 words; every sentence must earn its place |

---

#### Spoken Script / Talk

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 5000-9000 words for 45-60 min talk | Speakers deliver ~130-150 words/min; script covers ~60-70% of stage time with exact language (H) |
| **Beat types** | SCRIPTED (word-for-word: openings, closings, key transitions, confessions, killer lines, audience questions) and GUIDED (structured talking points with key phrases bolded) | Scripted moments must land exactly right; guided moments need natural delivery (H) |
| **Sentence cap** | 12 words max for SCRIPTED beats | Written handles 15-20 words; spoken maxes at 12. If you can't say it in one breath, split it (T1: performance methodology) |
| **Performance notation** | `[PAUSE: Xs]`, `[SLOW]`, `[PACE: fast]`, `[VOLUME: drop]`, `[SILENCE: Xs]`, `[SLIDE: description]`, `[MOVE: description]`, `[LOOK: description]` | Inline notation for rehearsal; less is more — if every line has a pause, none matter |
| **Structure** | Header block → Pre-stage notes → Beat-by-beat script → Post-stage notes → Rehearsal guide | Full performance document, not just words |
| **Derivation rule** | NEVER read the article aloud; articles have connective tissue, stage has silence | A spoken script is NOT a transcript; it is a performance document |

---

#### Podcast Brief

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 500-800 words | Provides the conversational skeleton; the host fills in naturally (H) |
| **Structure** | Topic hook (1-2 sentences: why this matters NOW) → 3-5 discussion questions (each with the surprising angle) → Key talking points per question (2-3 bullets each) → The one thing the listener should remember | Question-driven format mirrors how podcast conversations flow (H) |
| **Evidence density** | 1-2 data points per question (enough to ground the conversation) | Podcast listeners are multitasking; memorable hooks > citation chains (M) |
| **Tone** | Conversational framing; written as if briefing a friend before the recording | The brief should sound like what the speaker would say if you asked "what are you going to talk about?" |
| **CTA** | The "one thing" at the end; a single memorable takeaway the host can use as the close | Podcasts end on a note, not a summary |

---

#### Newsletter / Email

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 300-500 words | Inbox competition is fierce; newsletters that respect time get opened next time (H) |
| **Structure** | Hook (1-2 sentences: why this piece matters to the subscriber) → Thesis preview (1 sentence) → 2-3 evidence beats (1 sentence each, the most surprising) → The "read the full piece" bridge → Link to source | Action-oriented: the newsletter is a pointer with enough substance to justify the open (M) |
| **Evidence density** | 2-3 beats (the most surprising ones; leave the rest for the full piece) | Enough to show value; not so much that the subscriber skips the source |
| **Tone** | More personal than the source; subscriber relationship is intimate | "I published something this week that I think you'll care about" > "New article: [title]" |
| **Subject line** | Follows the same hook archetypes as the source, compressed to <60 characters | Subject line is the hook for the hook; it decides open rate |

---

#### Tweet Thread

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 3-7 tweets, each ≤280 characters | Platform constraint is hard; threads >7 tweets lose completion rate exponentially (H) |
| **Structure** | Tweet 1: Killer hook + thesis (this tweet must work standalone) → Tweets 2-5: One evidence beat or insight per tweet → Tweet 6-7: Implication + invitation/CTA → (Optional) Final tweet: link to source | Each tweet must work if someone sees only that one tweet in isolation (H) |
| **Evidence density** | 1 evidence point per tweet (compressed to a single punchy sentence) | 280 characters forces maximal compression; one number or one claim per tweet |
| **Tone** | Punchy, declarative, no qualifiers; every word earns its place | Twitter/X rewards confidence and surprise; hedging is invisible |
| **Numbering** | "1/" style numbering on each tweet | Signals thread; readers can jump to any tweet |

---

#### Executive Briefing

| Dimension | Constraint | Rationale |
|---|---|---|
| **Length** | 400-700 words | Executives read on mobile between meetings; respect the time (H) |
| **Structure** | Bottom line up front (BLUF: 2-3 sentences, the decision this informs) → Key findings (3-5 bullets, each with evidence tier) → Implication for our business (1 paragraph) → Recommended action (1-2 sentences) → Assumptions and risks (3-5 bullets) | Decision-first; pyramid principle — conclusion, then evidence, then caveats (H) |
| **Evidence density** | Every finding has an evidence tier tag inline | Executive audiences need to know confidence level on each claim; they decide what to verify (H) |
| **Tone** | Zero jargon; no framework names unless the executive already uses them | "Hamilton Helmer's 7 Powers analysis shows..." → "Three structural advantages protect us: [plain language]" (P16: zero-jargon executive summary) |
| **Format** | Bullets and bold headers; no flowing prose | Scannability > readability for this format |

---

### Framework 2: Compression Protocol

The 7-step methodology for deriving a compressed format from a full argument. This is the operational core of the skill. Every derivation follows these steps in order.

**Prerequisite:** The source document must be fully read and its structure mapped before starting. Identify: (a) the thesis statement, (b) all evidence beats, (c) all framework applications, (d) all counterarguments, (e) the philosophical/deeper layer (if present), (f) the opening hook, (g) the closing invitation.

**Step 1: Sharpen the Hook (Channel-Appropriate)**

The source's opening rarely transfers directly. Adapt using the Hook Adaptation framework (Framework 3).

| Source hook type | LinkedIn post adaptation | Conference abstract adaptation | Tweet thread adaptation |
|---|---|---|---|
| Vivid scenario (3-4 paragraphs) | Compress to 2 lines: the sharpest image + the tension | Compress to the title: provocative claim | First tweet: the scenario in 1 sentence + "Here's what that means →" |
| Killer stat | Keep the stat; cut the setup | Lead with the stat in the abstract body (title = the implication) | First tweet IS the stat |
| Contrarian claim | Keep verbatim if ≤2 lines; otherwise sharpen | Title = the claim | First tweet = the claim |
| Dialectic tension | Compress to 1 sentence holding both truths | Title = the tension; abstract = the resolution | First 2 tweets: one truth each; tweet 3 = the synthesis |

**Decision Table — Hook Adaptation:**

| If the source hook is... | And the target is short-form (post, tweet) | And the target is long-form (article, script) | And the target is structured (abstract, briefing) |
|---|---|---|---|
| Already punchy (≤2 sentences) | Use as-is or micro-edit | Use as-is; build from it | Adapt to format structure (problem → insight) |
| Setup-heavy (3+ paragraphs) | Extract the punchline; discard setup | Compress setup to 1 paragraph | Extract the core tension; state it directly |
| Data-driven | Lead with the single sharpest number | Lead with the number; add 1 sentence of context | BLUF: state the implication of the number |
| Story-based | Compress to 1-2 sentences preserving the image | Keep the story but cut to 60% of original length | Transform story to problem statement |

**Step 2: Keep the Thesis Statement Intact**

The thesis is the one sentence the reader could repeat back. It survives every derivation.

| Thesis state in source | Action |
|---|---|
| Already 1 clear sentence | Copy verbatim into derivative |
| Spread across 2-3 sentences | Compress to 1 sentence preserving the core claim |
| Implicit (never stated directly) | State it explicitly — if you can't, the source has a thesis problem, not a compression problem |
| Contains jargon | For public channels: translate jargon to plain language while preserving the mechanism |

**Fidelity test:** After writing the derivative, extract the thesis from BOTH source and derivative. If a reader would state the core claim differently after reading each, you have thesis drift (FM-2).

**Step 3: Pick 3 Evidence Beats (From the Source's N Beats)**

Most sources have 4-7 evidence beats. Most derivatives need 2-3. Selection criteria:

| Selection criterion | Weight | Rationale |
|---|---|---|
| **Surprise factor** | Highest | Does this evidence contradict what the reader already believes? If yes, it survives compression. |
| **Thesis support strength** | High | Does this evidence directly prove the thesis? Tangential evidence gets cut first. |
| **Channel-audience match** | High | Will THIS audience find this evidence compelling? Technical data for LinkedIn technical audience; human stories for podcast. |
| **Recency** | Medium | More recent evidence > older evidence for time-sensitive channels (social, newsletter). Flag `[POTENTIALLY STALE]` for evidence >6 months old. |
| **Uniqueness** | Medium | Is this evidence available only from the source, or widely known? Unique evidence survives; googleable facts get cut. |

**Decision Table — Evidence Selection:**

| Number of source evidence beats | Target channel is short-form (≤350 words) | Target channel is medium (350-1500 words) | Target channel is long-form (>1500 words) |
|---|---|---|---|
| 3-4 beats | Keep 2, cut the weakest | Keep all 3, compress each | Keep all, compress lightly |
| 5-7 beats | Keep 3, cut by surprise + uniqueness ranking | Keep 3-4, compress each | Keep 4-5, compress the weakest |
| 8+ beats | Keep 3 max; this is a high-compression derivation | Keep 3-4; compress aggressively | Keep 5-6; the rest go to the Compression Log |

**Step 4: Keep 1 Framework Application (The Most Accessible)**

If the source applies multiple frameworks, the derivative keeps one — the one that is most intuitive to the target audience.

| Audience expertise | Framework selection rule |
|---|---|
| **General professional** (LinkedIn, newsletter) | Pick the framework with the most concrete, visual output (a table, a taxonomy, a 2x2). Drop abstract models. |
| **Domain expert** (executive briefing, conference) | Pick the framework with the sharpest strategic implication. The audience knows the basics; they want the uncommon knowledge. |
| **Mixed** (podcast, tweet thread) | Pick the framework that produces the most memorable single insight. "Three types of X" > "A multi-factor assessment of Y." |

**Compression rule:** The framework goes from a full section (500-1000 words) to an inline reference (1-3 sentences) or a compressed visual (a list instead of a table). The structure is preserved; the explanation is cut.

**Step 5: Drop Philosophy (Keep Mechanism)**

The source's "deeper layer" — philosophical implications, societal commentary, abstract reflection — rarely survives compression. The mechanism behind the philosophy does.

| Source has... | Derivative action |
|---|---|
| A philosophical paragraph with a killer line | Keep the killer line; cut the paragraph. Drop it into an evidence beat as a one-sentence gut-punch. |
| A philosophical section (500+ words) | Compress to 1-2 sentences woven into the implication section. The philosophy becomes texture, not structure. |
| No philosophical layer | Nothing to cut. If the derivative feels shallow, the problem is evidence selection, not missing philosophy. |

**The 10% Rule:** Philosophical/personal passages should be ≤10% of any derivative. If the derivative is 300 words, that's 30 words of philosophical depth — one sentence. Earn it.

**Step 6: Keep 1 Counterargument (The Strongest)**

Intellectual honesty survives compression. Counterarguments are what separate a confident argument from a confident assertion.

| Source counterargument count | Derivative action |
|---|---|
| 2-3 counterarguments | Keep the strongest; defeat it in 2-3 sentences. Cut the rest. |
| 1 counterargument | Keep it. |
| 0 counterarguments | Flag: "Source has no counterarguments — derivative inherits this weakness." |

**Selection criterion:** The strongest counterargument is the one that, if true, would most seriously undermine the thesis. Not the easiest to defeat — the hardest.

**Step 7: Shorten the Invitation/CTA**

The source's closing (often 1-2 paragraphs: forward look + invitation) compresses to 1-2 sentences.

| Target channel | Closing format |
|---|---|
| LinkedIn post | 1 sentence: a question or tension worth sitting with. Not "What do you think?" — a genuine question from the argument. |
| LinkedIn article | 2-3 sentences: the forward look compressed + invitation. |
| Conference abstract | Already handled in the "what the audience learns" section — no separate close. |
| Spoken script | The close is a full SCRIPTED beat — see Spoken Script Derivation (Framework 7). |
| Tweet thread | Final tweet: the implication + link to source. |
| Newsletter | "Read the full piece" bridge + link. |
| Executive briefing | "Recommended action" section — no invitation, just the decision prompt. |
| Podcast brief | "The one thing the listener should remember." |

---

### Framework 3: Hook Adaptation by Channel

Four hook archetypes mapped to channel effectiveness. Every source document opens with one of these (explicitly or implicitly). The derivative must adapt the archetype to the target channel's constraints.

**The Four Hook Archetypes:**

| Archetype | Definition | Source Example | When it works best |
|---|---|---|---|
| **Killer Stat** | A single surprising number that contradicts conventional wisdom | "97% of AI systems fail a basic safety test when you give them memory." | Research data is genuinely surprising; the number IS the hook |
| **Vivid Scenario** | A concrete, visual situation that drops the reader into the problem | "Imagine a child growing up with an AI that resolves every conflict..." | The implication is human and visceral, not just technical |
| **Contrarian Claim** | A direct assertion that the reader's first instinct is to dispute | "The AI industry is building personalization backwards." | The reader's "wait, that can't be right" reaction is the hook |
| **Dialectic Tension** | Two seemingly contradictory truths held together | "Everything about building products has changed. And nothing has changed." | Two observations create a productive tension; resolution requires the reader to keep going |

**Hook × Channel Effectiveness Matrix:**

| Hook Archetype | LinkedIn Post | LinkedIn Article | Conference Abstract | Spoken Script | Podcast Brief | Newsletter | Tweet Thread | Executive Briefing |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Killer Stat | 🟢 (T2) | 🟢 (T2) | 🟡 (T3) | 🟢 (T2) | 🟢 (T3) | 🟢 (T2) | 🟢 (T2) | 🟢 (T1) |
| Vivid Scenario | 🟡 (T3) | 🟢 (T2) | 🟡 (T3) | 🟢 (T1) | 🟢 (T2) | 🟡 (T3) | 🔴 (T3) | 🔴 (T3) |
| Contrarian Claim | 🟢 (T2) | 🟢 (T2) | 🟢 (T2) | 🟢 (T2) | 🟡 (T3) | 🟢 (T2) | 🟢 (T1) | 🟡 (T3) |
| Dialectic Tension | 🟡 (T3) | 🟢 (T2) | 🟢 (T2) | 🟢 (T1) | 🟡 (T3) | 🟡 (T3) | 🔴 (T4) | 🔴 (T4) |

**Key:** 🟢 = Strong fit (use as-is or lightly adapt) | 🟡 = Moderate fit (adapt significantly) | 🔴 = Poor fit (choose different archetype)

**Channel-Specific Hook Constraints:**

| Channel | Hook constraint | Implication |
|---|---|---|
| **LinkedIn post** | First ~210 characters visible before fold on mobile (T1: platform behavior) | Hook must land in 2 lines. Vivid Scenarios that need 4 paragraphs to build are channel-blind on LinkedIn. |
| **Conference abstract** | Title ≤80 characters; abstract opens after title | The title IS the primary hook. Abstract hook is secondary. Provocative title > descriptive title. |
| **Tweet thread** | First tweet ≤280 characters, must work standalone | Hook + thesis must fit in 1 tweet. No build-up possible. |
| **Spoken script** | Cold open: 60-90 seconds, no "Hi I'm..." | Vivid Scenarios and Dialectic Tensions are strongest on stage (audience leans forward). Stats work if genuinely shocking. |
| **Podcast brief** | Opening question or angle that the host can riff on | The hook must be conversational, not written-register. "What if I told you..." framing works here, fails on LinkedIn. |
| **Executive briefing** | BLUF (Bottom Line Up Front); no hook needed — state the conclusion | Hooks are for audiences that haven't opted in. Executives reading a briefing have already opted in. Lead with the decision. |
| **Newsletter** | Subject line ≤60 characters; first line visible in inbox preview | Two hooks needed: subject line (decides open) + first sentence (decides read). They must work together, not repeat. |

---

### Framework 4: Evidence Density Calibration

How much evidence per channel. This framework provides exact targets for the number, depth, and annotation of evidence beats per derivative format.

**Evidence Density Targets:**

| Channel | Evidence beats | Depth per beat | Citation requirement | Evidence-per-word ratio target |
|---|:---:|---|---|---|
| **Source (Substack/blog)** | 5-7 | Full: data + interpretation + source link + implication (50-150 words each) | Inline links to every claim; full Sources section at bottom | 1 evidence beat per 500-700 words |
| **LinkedIn post** | 2-3 | Compressed: 1-2 sentences mixing data + observation | 0-1 inline links; author tagging for attribution | 1 evidence beat per 100-120 words |
| **LinkedIn article** | 3-4 | Moderate: 1 paragraph each with key data point | 2-3 inline links (most important claims) | 1 evidence beat per 300-400 words |
| **Conference abstract** | 0-1 | Promise: "I'll show data from X" or 1 surprising stat | None required — the talk delivers the evidence | 0-1 beats total |
| **Spoken script** | 3-5 | Story/demo format: evidence as narrative, not citation. "Stanford ran a study. Thirty years of data. They found..." | No inline citations; evidence IS the story beat | 1 evidence beat per 1500-2000 words |
| **Podcast brief** | 1-2 per question | Conversational: enough to ground the discussion point | None; the host or guest cites naturally in conversation | 1 data point per discussion question |
| **Newsletter** | 2-3 | Headline: the most surprising number or claim, 1 sentence each | Link to source for detail | 1 evidence beat per 150-200 words |
| **Tweet thread** | 1 per tweet | Atomic: one number, one claim, one finding per tweet | None in-tweet; source link in final tweet | 1 beat per 280 characters |
| **Executive briefing** | 3-5 | Bullet: finding + evidence tier tag inline | Every finding has (TX) annotation | 1 evidence beat per 100-150 words |

**Scoring Rubric — Evidence Density:**

| Rating | Symbol | Criteria |
|---|---|---|
| **On target** | 🟢 | Evidence beat count and depth match the channel target within 20% |
| **Thin** | 🟡 | 1 fewer beat than target, or beats are shallower than channel depth requires |
| **Failed** | 🔴 | Evidence dropped entirely (FM-3), or evidence density from wrong channel applied (FM-4) |

**Decision Table — When Evidence is Insufficient:**

| Situation | If target is short-form | If target is long-form |
|---|---|---|
| Source has fewer evidence beats than the channel target | Use all available evidence; note the deficit in the Compression Log | Flag `[EVIDENCE-LIMITED]`; recommend the reader check the source for full evidence |
| Evidence beats are stale (>6 months) | Flag `[POTENTIALLY STALE]` on each stale beat; use anyway if nothing fresher exists | Flag `[POTENTIALLY STALE]` and recommend verification before acting on the derivative |
| No evidence in source (pure assertion) | Do not derive — the source has a quality problem, not a compression problem | Same. The derivative cannot add evidence the source doesn't have. |

---

### Framework 5: Audience Context Matching

Different channels serve different audiences. The same argument, compressed to the same length, needs different framing depending on who reads it and where.

**Audience × Channel Matrix:**

| Channel | Primary audience | Expertise assumption | Reading context | Framing adjustment |
|---|---|---|---|---|
| **LinkedIn post** | Peers, executives, recruiters; professional network | Mixed: some domain experts, many generalists | Feed scroll, 3-second attention test, mobile-first | Lead with personal experience or credential; jargon-free; show thinking, not just conclusions |
| **LinkedIn article** | Self-selected readers who clicked through | Higher expertise than post viewers (self-selected) | Dedicated reading, still mobile-common | Can go deeper; still needs scannable structure; less hook-dependent since reader opted in |
| **Conference abstract** | Selection committee first, attendees second | Committee: generalists evaluating 200 proposals. Attendees: self-selected by topic. | Batch reading (committee reads 50+ in a session); fast scan | Optimize for committee: outcome-first, "why should 500 people sit still?" framing |
| **Spoken script** | Live audience in a room | Mixed: some came for you, some for the conference | Captive but distracted; phones, fatigue, post-lunch | Stories > data; repeat key phrases; rhetorical questions earn silence; one number per beat |
| **Podcast brief** | Listeners multitasking (commuting, exercising) | Self-selected by topic interest | Audio-only; no re-reading; linear consumption | Memorable hooks > nuanced argument; conversational register; "the one thing" principle |
| **Newsletter** | Subscribers who opted in | High engagement (they subscribed); expertise varies | Inbox competition; scanning subject lines; opens are earned | Personal tone; "I wrote something you'll care about"; respect their time — 300-500 words, then link |
| **Tweet thread** | Public timeline; followers + algorithm-surfaced | Low context; each tweet must work for someone who sees only that tweet | Fastest scroll speed of any channel; attention measured in fractions of seconds | Maximum compression; punchy declaratives; no setup, no qualifiers |
| **Executive briefing** | Senior leadership; decision-makers | High on business context; variable on domain specifics | Between meetings; mobile; needs BLUF | Zero jargon; bottom line first; evidence tiers inline; recommendation with action and owner |

**Audience Adaptation Decision Table:**

| If the source uses... | And the audience is generalist | And the audience is domain expert | And the audience is executive |
|---|---|---|---|
| Technical jargon | Translate to plain language; add 1-sentence explanation on first use | Keep jargon; they expect it | Remove jargon entirely; state the implication, not the mechanism |
| Framework names (e.g., "7 Powers", "JTBD") | Replace with the insight the framework produces ("three structural advantages") | Keep framework names; they add credibility | Use only if the executive already uses this framework; otherwise translate |
| Academic citations | Replace with accessible framing ("Stanford researchers found...") | Keep full citation; they validate on source quality | "Research shows..." + the number. No author names unless famous. |
| First-person narrative | Keep if the author has relevant credential; otherwise shift to third person | Keep if it demonstrates practitioner credibility | Remove personal narrative; keep only if it establishes unique authority to speak |
| Counterarguments | Keep the strongest one; it builds credibility with skeptics | Keep 2+; experts respect rigor | Keep 1 in "risks" section; frame as "what could go wrong" not "counterargument" |

---

### Framework 6: Source Fidelity Verification

The quality assurance framework that prevents derivatives from drifting away from the source argument. Run this AFTER producing the derivative, BEFORE delivering it.

**Five Fidelity Dimensions:**

| # | Dimension | Verification Question | Pass Condition | Common Failure |
|---|---|---|---|---|
| 1 | **Thesis Preservation** | Is the core claim intact? Could a reader state the same thesis after reading only the derivative? | Thesis appears verbatim or as a faithful compression. A reader of only the derivative would agree with a reader of only the source about "what this is about." | FM-2: Thesis Drift — the claim shifts to fit the channel better ("AI is building personalization backwards" becomes "AI personalization has challenges") |
| 2 | **Evidence Fidelity** | Are the compressed claims still accurate? Did compression change the meaning of any evidence? | Every evidence beat in the derivative is traceable to a specific location in the source. No claim was strengthened, weakened, or recontextualized in a way that changes its meaning. | FM-3: Evidence Omission — all evidence dropped. FM-6: Single-Fact Padding — one fact kept, padded to length |
| 3 | **Counterargument Preservation** | Did we keep intellectual honesty? | At least the strongest counterargument from the source appears in the derivative (for channels that support it: article, briefing, spoken script). | FM-2: Thesis Drift via omission — dropping all counterarguments makes the argument look stronger than the source intended |
| 4 | **Voice Consistency** | Does this sound like the same author? | Reading the source and derivative side-by-side, the register, sentence length patterns, and personality markers are consistent. | FM-7: Voice Fracture — the derivative sounds like a press release when the source sounds like a conversation |
| 5 | **Structural Integrity** | Does the derivative's argument structure track the source's logic? | The derivative follows the same logical arc (claim → evidence → implication) even if compressed. It does not rearrange the argument in a way that changes the causal logic. | FM-1: Summary, Not Derivative — the structure is "this article talks about X, Y, Z" instead of making the argument |

**Fidelity Scoring Rubric:**

| Score | Symbol | Definition |
|---|---|---|
| **5/5 dimensions pass** | 🟢 | Derivative is faithful and channel-appropriate. Ship it. |
| **4/5 dimensions pass** | 🟡 | One dimension needs attention. Fix before publishing. Identify which dimension failed and why. |
| **3/5 or fewer pass** | 🔴 | Derivative has drifted from source. Re-derive from scratch using the Compression Protocol. Do not patch. |

**Anti-Drift Scoring Rubric (Detailed):**

| Dimension | 3 — Faithful | 2 — Minor drift | 1 — Significant drift | 0 — Failed |
|---|---|---|---|---|
| **Thesis** | Verbatim or indistinguishable compression | Thesis present but softened (added qualifiers, weakened claim) | Thesis changed (different claim than source) | Thesis absent or contradicts source |
| **Evidence** | All kept beats traceable to source; meaning preserved | 1 beat over-compressed (meaning slightly changed) | Evidence recontextualized (used to support a different point) | Evidence fabricated or entirely omitted |
| **Counterargument** | Strongest preserved and defeated | Present but weakened (straw-manned) | Present but wrong one chosen (easiest, not strongest) | Absent |
| **Voice** | Indistinguishable from author's other work on this channel | Minor tone shift (1-2 sentences off-register) | Significant tone shift (reads like different author) | Completely different voice (consultant-speak, PR, academic) |
| **Structure** | Same logical arc, compressed | Arc preserved but one logic step skipped | Arc rearranged (changes causal flow) | No argument structure (FM-1: summary) |

**Scoring:** Sum all 5 dimensions. Maximum = 15. Minimum for publish = 12 (no dimension below 2).

---

### Framework 7: Spoken Script Derivation

The full methodology for transforming written content into a spoken performance document. This framework applies ONLY when the target channel is `spoken_script`. It supplements the Compression Protocol with performance-specific methodology.

**Prerequisite:** A conference talk proposal, thesis document, or presentation beats document must exist. The spoken script derives from structure, never invented from scratch. This mirrors P2: full argument first, derivatives second.

**Beat Classification Protocol:**

| Beat Type | Marker | When to Use | Writing Rules |
|---|---|---|---|
| **SCRIPTED** | `[SCRIPTED]` | Openings, closings, key transitions, confessions, the single killer philosophical line, questions posed to the audience | Word-for-word. 12-word sentence cap. Read aloud — if it takes 2 breaths, split. Rehearsed until natural, not read. |
| **GUIDED** | `[GUIDED]` | Evidence sections, framework walkthroughs, story details, Q&A responses | Structured talking points with key phrases **bolded**. Speaker knows territory + destination; chooses path. Each guided beat includes: the point, 2-3 must-appear phrases, transition to next beat. |

**SCRIPTED/GUIDED Ratio:**

| Talk type | SCRIPTED % | GUIDED % | Rationale |
|---|---|---|---|
| Keynote (high-stakes, large audience) | 60-70% | 30-40% | Every moment matters; less room for improvisation risk |
| Conference session (medium-stakes) | 40-50% | 50-60% | Balanced; key moments scripted, evidence sections guided |
| Workshop (interactive) | 20-30% | 70-80% | Mostly guided; audience interaction unpredictable |
| Panel / Q&A prep | 10-20% | 80-90% | Almost entirely guided; scripted openings/closings only |

**Performance Notation System:**

| Notation | Effect | Use Sparingly When... | Overuse Signal |
|---|---|---|---|
| `[PAUSE: 2s]` | Timed silence | After a key claim that needs to land | More than 5 per 10-minute segment |
| `[SLOW]` | Reduce pace, next 1-2 sentences | Moment that needs to sink in; often before the thesis restatement | More than 3 per 10-minute segment |
| `[PACE: fast]` | Increase pace for accumulation | Rapid-fire evidence, building momentum before a payoff | More than 2 per 10-minute segment |
| `[VOLUME: drop]` | Lower volume; forces room to lean in | Before a key claim; creates intimacy | More than 2 per talk |
| `[SILENCE: 5s]` | Structural silence; longer than a pause | After a major revelation; before a movement shift | More than 2 per talk |
| `[SLIDE: description]` | What appears on screen | Visual anchor, not content dump — 1-2 words or an image | If you need the slide to carry the argument, the script is too weak |
| `[MOVE: description]` | Physical staging | Walk to center, step toward audience, stop moving | More than 5 per talk; movement must feel motivated |
| `[LOOK: description]` | Eye contact direction | "Scan room slowly." "Pick one person, hold." "Look down, then up." | More than 3 per talk; every look instruction must earn its weight |

**Spoken Voice Rules (Supplements Standard Voice Rules):**

| Rule | Written register | Spoken register | Example |
|---|---|---|---|
| Sentence length | 15-20 words acceptable | 12 words max for SCRIPTED | "The study, which was conducted by Stanford researchers using thirty years of data, found that..." → "Stanford ran a study. Thirty years of data. They found..." |
| Repetition | Redundant | Emphasis | If a phrase matters, say it twice — once to introduce, once to land |
| Subordinate clauses | Tolerated | Banned | "AI, which has been the subject of much debate, is transforming..." → "AI is transforming..." |
| Verb placement | Flexible | End-of-sentence for punch | "AI doesn't just know science. It does science." |
| Contractions | Optional | Always | "It is" → "It's". Without contractions, spoken delivery sounds like a press release. |
| Rhetorical questions | Transition device | Earns silence | Ask the question, then shut up. 3-5 seconds. The question is a moment, not a bridge. |
| Story tense | Past tense | Present tense | "I'm sitting in my apartment. The offer letter is open on my laptop." Present tense puts the audience in the room. |
| Numbers per beat | Multiple acceptable | One per beat | Audience remembers one number, not three. Pick the sharpest; others become texture. |

**7-Step Spoken Script Derivation Process:**

1. **Read the source end-to-end.** Identify which moments are SCRIPTED (must land exactly) vs. GUIDED (territory + destination).
2. **Write SCRIPTED beats.** Exact sentences. Read aloud. If any sentence requires a second breath or re-read to parse → simplify. Apply the 12-word cap.
3. **Write GUIDED beats.** Extract key phrases and transition sentence. Write 3-5 bullet points for the territory. **Bold** phrases that must appear.
4. **Add performance notation.** Less is more — only mark genuine shifts in pace, volume, or staging. If every other line has `[PAUSE]`, none of them matter.
5. **Write transitions.** The last sentence of beat N should make the first sentence of beat N+1 feel inevitable.
6. **Read aloud, full script.** Time yourself. Mark where you stumble. Those are rewrite targets.
7. **Write the rehearsal guide.** Which 5 beats to drill, which transitions to practice, what to time, what to record yourself doing.

---

## Evidence Standards

### Evidence Quality Tiers (Applied to Source Verification)

| Tier | Source Type | Weight in Derivative | Example |
|---|---|---|---|
| **Tier 1** | Direct behavioral data (what people DO) | Survives all compressions; cite in every format | Usage analytics, app store data, revenue data, patent filings |
| **Tier 2** | Primary research, credible methodology | Survives most compressions; name the researcher/study | Well-sampled surveys, structured interviews, experiments |
| **Tier 3** | Expert analysis with disclosed reasoning | Survives medium+ formats; can be compressed to "experts find..." | Analyst reports with methodology, academic papers |
| **Tier 4** | Industry reports from reputable firms | Useful for sizing; compress to the number only | Gartner, IDC, Forrester sizing data |
| **Tier 5** | Executive statements and press releases | Use only as strategic signaling analysis | Company announcements, keynote claims |
| **Tier 6** | Punditry, blog posts, social media | Sentiment only; never for structural claims | Twitter discourse, opinion pieces |

**Compression Rule for Evidence Tiers:** When compressing, higher-tier evidence survives over lower-tier. If you can only keep 2 beats, keep the T1 and T2 beats; cut the T4-T6 beats.

---

## Application Method

### Step 0: Route to Framework Subset (Do This First)

Select the load-bearing frameworks based on source type and target channel. Not every derivation needs every framework.

| Source Type × Target Channel | Primary Frameworks (apply in full) | Supporting Frameworks (reference) | Skip |
|---|---|---|---|
| **Article → LinkedIn post** | Compression Protocol, Hook Adaptation, Evidence Density | Audience Context Matching | Spoken Script Derivation, Source Fidelity (run after) |
| **Article → LinkedIn article** | Compression Protocol, Evidence Density, Audience Context | Hook Adaptation (lighter — reader opted in) | Spoken Script Derivation |
| **Thesis → Conference abstract** | Hook Adaptation (title focus), Audience Context (committee targeting) | Compression Protocol (Step 1 and 2 only) | Evidence Density (abstracts promise, not deliver), Spoken Script |
| **Thesis → Spoken script** | Spoken Script Derivation, Compression Protocol, Hook Adaptation | Evidence Density (spoken format) | Audience Context (audience is live — adapt in the room) |
| **Article → Podcast brief** | Compression Protocol (Steps 1-3), Audience Context | Evidence Density (conversational format) | Hook Adaptation (host provides the hook), Spoken Script |
| **Article → Newsletter** | Compression Protocol (all 7 steps), Hook Adaptation (subject line) | Evidence Density, Audience Context | Spoken Script |
| **Article → Tweet thread** | Compression Protocol (extreme compression), Hook Adaptation | Evidence Density (1 per tweet) | Audience Context (lowest context channel), Spoken Script |
| **Article → Executive briefing** | Audience Context (executive framing), Evidence Density (tiered) | Compression Protocol (Steps 2-3) | Hook Adaptation (BLUF replaces hooks), Spoken Script |
| **Full distribution package** | All frameworks except Spoken Script (unless talk is included) | Source Fidelity Verification on each derivative | None — but prioritize: LinkedIn post first, then article, then remaining |

### Quick Version (7 steps for experienced practitioners)

0. **Route to framework subset** — Identify source type and target channel from the table above. Select primary frameworks.
1. **Pass the Context Gate** — Source exists? Channel appropriate? Public-safe? Voice grounded?
2. **Map the source document** — Identify thesis, evidence beats (count and rank by surprise), frameworks, counterarguments, philosophical layer, hook, closing.
3. **Execute the 7-step Compression Protocol** — Sharpen hook → keep thesis → pick 3 evidence beats → keep 1 framework → drop philosophy → keep 1 counterargument → shorten closing.
4. **Apply channel format constraints** — Word count, structure, tone, formatting rules from the Channel Format Taxonomy.
5. **Run Source Fidelity Verification** — Thesis preserved? Evidence faithful? Counterargument intact? Voice consistent? Structure tracks?
6. **Complete the Compression Log** — Every element from the source: Kept/Cut/Adapted with rationale.
7. **Fill the Output Template** — Context Gate, Step 0, Thesis Fidelity Check, derivative content, Compression Log, Audience Match, Quality Check, Assumptions, Self-Critique, Revision Triggers.

### Full Version (detailed steps with decision points)

**Step 1: Pass the Context Gate**

Answer all four gate questions (Section: Context Gate above). Hard stop if any gate fails.

**Quality checkpoint:** If the source is notes or an outline — not a finished piece — STOP. The derivative will be shallow because the source thinking is incomplete. P2: "Writing short before writing long produces shallow thinking disguised as brevity."

**Step 2: Map the Source Document**

Before cutting anything, map what exists:

| Element | What to identify | Where it usually lives |
|---|---|---|
| Thesis statement | The one sentence a reader could repeat back | Paragraph 2-3 of the source; sometimes the subheadline |
| Evidence beats | Each distinct data point, research finding, or observed pattern | Body sections; count them and rank by surprise factor |
| Framework applications | Named or unnamed analytical structures | Usually a dedicated section; sometimes embedded in evidence |
| Counterarguments | Objections the source addresses | Often Section 6 or near the end; sometimes woven throughout |
| Philosophical layer | Abstract implications, societal commentary, deeper meaning | The "deeper layer" section; sometimes a standalone paragraph |
| Opening hook | First 2-5 sentences; the entry point | Paragraph 1 |
| Closing invitation | The final paragraph(s); the send-off | Last section |

**Decision point:** If the source has ≤2 evidence beats, the derivative will be thin regardless of skill applied. Consider whether the source needs more development before deriving.

**Step 3: Execute the 7-Step Compression Protocol**

Apply Framework 2 in full. Each step has its own decision tables (see Framework 2 above). The most common mistake is skipping Step 3 (evidence selection) and keeping everything, producing a derivative that's an abridgment, not a compression.

**Quality checkpoint after Step 3:** Read the evidence beats you selected. Do they support the thesis independently? If someone read only these 2-3 beats, would they understand WHY the thesis is true? If not, you selected wrong — swap beats.

**Step 4: Apply Channel Format Constraints**

Consult the Channel Format Taxonomy (Framework 1) for the target channel. Check:
- Word count: within range?
- Structure: matches the channel template?
- Hook: uses an archetype effective for this channel (Framework 3)?
- Evidence density: matches the channel target (Framework 4)?
- Tone: matches the channel expectation (Framework 5)?

**Decision point:** If the derivative exceeds the word count by >20%, you haven't compressed enough. Go back to Step 3 and cut another evidence beat. If it's under by >20%, you may have lost too much — check for FM-3 (Evidence Omission).

**Step 5: Run Source Fidelity Verification**

Apply Framework 6 in full. Score all 5 dimensions. Minimum score for publish: 12/15 with no dimension below 2.

**Quality checkpoint:** Read the source thesis, then the derivative thesis. If they feel like different arguments, you have FM-2 (Thesis Drift). Read the source's strongest counterargument. Is it in the derivative? If not, check whether the channel supports it — some channels (tweet thread) may not have room.

**Step 6: Complete the Compression Log**

The Compression Log is the audit trail. Every substantive element from the source appears as a row: what happened to it (Kept/Cut/Adapted) and why.

**Quality checkpoint:** If the log has more "Cut" entries than "Kept" entries for a medium-form derivative (article, newsletter), you may be over-compressing. If it has zero "Cut" entries, you may have produced an abridgment, not a derivative.

**Step 7: Fill the Output Template**

Use the Output Template skeleton (Section: Output Template above). Fill every section. The Quality Check at the end is the final gate — every checkbox must pass.

### Mandatory Output: Assumption Registry

Every derivative must include an Assumption Registry with minimum 3 assumptions:

| # | Assumption | Confidence | Evidence | What would invalidate |
|---|---|---|---|---|
| 1 | The target audience has not read the source document | H/M/L | [basis] | If the audience has read the source, the derivative adds no value and may feel redundant |
| 2 | The channel's current algorithm/format rules still apply | H/M/L | [basis — e.g., last verified date] | Platform algorithm change; format rule change (e.g., LinkedIn expanding fold) |
| 3 | The source's evidence is still current and accurate | H/M/L | [source dates] | Any cited data becomes outdated, retracted, or superseded |

### Mandatory Step: Adversarial Self-Critique

After completing the derivative, answer:

> *"Identify 3+ genuine weaknesses in this derivative. For each: what assumption is being made? What evidence would prove this derivative fails its purpose? Is there a scenario where this derivative actively harms the author's credibility?"*

- Bear cases must be steelmanned — argued forcefully, not probability-weighted disclaimers.
- Each weakness links to a specific Revision Trigger.
- The adversarial critique is not optional and must not be folded into the Quality Check.

---

## Quality Gradients

### Intern Tier
- Produces a generic summary: "This article discusses X. Key points include Y and Z."
- No channel-specific formatting — same text could go on any platform
- Thesis absent or drifted — the derivative makes a different (usually weaker) claim than the source
- Evidence stripped entirely for brevity — assertions without support
- No compression log — impossible to trace what was lost
- Voice fracture — reads like a press release regardless of the source author's voice
- Hook is generic ("In today's fast-paced world...")
- No counterargument preserved
- Missing: audience adaptation, evidence density calibration, format constraints

### Consultant Tier
- Channel format followed (word count, basic structure)
- Thesis present and mostly faithful
- 2+ evidence beats preserved with reasonable compression
- Hook appropriate for channel (not copy-pasted from source)
- Voice roughly consistent with source author
- Some adaptation for target audience
- Compression log present but incomplete (not every element tracked)
- Missing: fidelity scoring, adversarial self-critique, assumption registry, evidence tier annotation, uncommon knowledge prioritization, framework visibility in compressed format

### Elite Tier
- Thesis survives verbatim or as indistinguishable compression — fidelity score 12+ /15
- Evidence beats selected by surprise × uniqueness ranking; highest-tier evidence prioritized
- Hook adapted using the correct archetype for the channel with channel-specific constraints respected
- Voice is indistinguishable from the author's other work on this channel
- Evidence density matches the channel target (per Evidence Density Calibration)
- Audience adaptation is explicit (jargon translated, framing adjusted, expertise assumptions matched)
- Framework/structural insight visible in the derivative — the reader sees HOW the author thinks
- Counterargument preserved (strongest one, defeated concisely)
- Compression Log is complete and auditable — every source element has a disposition
- Assumption Registry with 3+ assumptions, each with confidence and invalidation conditions
- Adversarial Self-Critique with 3+ steelmanned weaknesses
- Every evidence claim in the derivative traces to a specific source location
- The derivative could not have been produced by summarizing — it required structural judgment about what to keep, what to cut, and how to adapt for the channel

---

## Failure Modes

**FM-1: Summary, Not Derivative**
*What it looks like:* The output reads: "This article discusses three topics: A, B, and C. The author argues that..." It is a book-report-style summary that could describe any article on the topic, not a channel-specific compression of THIS argument.
*Why it happens:* The writer summarized instead of compressing. Summarization describes the source from outside; compression re-makes the argument from inside but shorter.
*Detection:* Remove the source attribution. Could this derivative have been written about a different article on the same topic? If yes, it's a summary.
*Correction:* Re-derive using the Compression Protocol. The thesis must appear as a direct claim, not reported speech. The evidence beats must argue, not describe.

**FM-2: Thesis Drift**
*What it looks like:* The source says "AI personalization is building backwards — optimizing for what people want, destroying their capacity to know what they should want." The derivative says "AI personalization has both benefits and challenges." The core claim has been softened, hedged, or shifted to fit the channel's "safe" register.
*Why it happens:* Subconscious risk aversion. The writer weakens the claim because the channel (LinkedIn, executive briefing) feels like it demands diplomatic language. Or: the compression process lost the sharp edge of the claim.
*Detection:* Extract the thesis from source and derivative separately. Ask: would a reader of the derivative state the same core claim as a reader of the source? If the derivative reader would state a weaker, vaguer, or different claim → thesis drift.
*Correction:* Copy the source thesis verbatim into the derivative as a starting point. Compress from there, never from memory.

**FM-3: Evidence Omission**
*What it looks like:* The derivative makes assertions without support. "AI systems have a significant memory problem" with no data, no study, no example. The source had 5 evidence beats; the derivative has zero. P16: "compression is not omission."
*Why it happens:* Brevity pressure. The writer decides evidence "doesn't fit" in a short format and cuts all of it.
*Detection:* Count the evidence beats in the derivative. If the count is zero for any channel except a conference abstract (which promises evidence), this is FM-3.
*Correction:* Re-select evidence using Step 3 of the Compression Protocol. Even a tweet thread (280 characters per tweet) can carry one evidence point per tweet.

**FM-4: Channel-Blind Formatting**
*What it looks like:* A Substack article copy-pasted into a LinkedIn post (1500 words in a feed format). Or a LinkedIn post expanded to article length by adding filler. The content was moved between channels without structural adaptation.
*Why it happens:* Laziness or misunderstanding of channel constraints. The writer treated "derivation" as "copy-paste with minor edits."
*Detection:* Check word count against channel target. Check structure against channel template. If either is off by >30%, the formatting is channel-blind.
*Correction:* Start the derivation from scratch using the Compression Protocol. The Channel Format Taxonomy provides the structural template.

**FM-5: Hook Mismatch**
*What it looks like:* A 4-paragraph vivid scenario opening on a LinkedIn post (where the fold hides everything after line 2). A punchy one-line stat on a Substack piece (where readers expect a slower build). A provocative contrarian claim in an executive briefing (where the audience wants BLUF, not provocation).
*Why it happens:* The hook from the source was copied without channel adaptation. The Hook Adaptation framework (Framework 3) was not consulted.
*Detection:* Match the hook archetype to the channel effectiveness matrix. If the archetype shows 🔴 for this channel, the hook is mismatched.
*Correction:* Consult Framework 3 and select the highest-rated archetype for the target channel. Adapt the source hook accordingly.

**FM-6: Single-Fact Padding**
*What it looks like:* The derivative takes one interesting factoid from the source and builds 300 words around it — adding context, restating the fact, reflecting on the fact, and concluding with the fact. The source's actual argument (thesis, framework, multiple evidence beats) is entirely absent. P16: the THS-004 v0.1 failure — "only one external paper. Doesn't talk about Stratum. Nothing about what I think."
*Why it happens:* The writer found one compelling data point and defaulted to "padding" rather than "compressing." Padding produces word count. Compression produces argument.
*Detection:* Count how many distinct arguments, evidence beats, and structural insights appear in the derivative. If the answer is 1, it's padding. Even a 200-word LinkedIn post should have 2-3 distinct beats.
*Correction:* Go back to Step 3 of the Compression Protocol. Select 2-3 evidence beats by surprise and uniqueness ranking. Ensure the framework/insight from the source is visible.

**FM-7: Voice Fracture**
*What it looks like:* The source author writes in short, punchy, self-implicating sentences. The derivative reads like a consulting report: passive voice, long subordinate clauses, hedging qualifiers, and zero personality. Side-by-side, they read like different authors.
*Why it happens:* Channel conventions (LinkedIn "professional" tone, executive briefing "formal" tone) overrode the source author's voice. Or: no voice reference was loaded (Context Gate question 4 failed).
*Detection:* Read 3 sentences from the source and 3 from the derivative aloud. If they sound like different people, voice has fractured.
*Correction:* Load the author's voice reference. Rewrite the derivative matching the source's sentence length patterns, register, and personality markers. The channel adapts the structure, not the voice.

**FM-8: Context Gate Failure**
*What it looks like:* An internal strategy document with confidential competitive data is derived into a public LinkedIn post. Or: an early-draft thesis with unverified claims is derived into a newsletter sent to 10,000 subscribers.
*Why it happens:* Context Gate (Step -1) was skipped or answered carelessly. The "public-safe?" and "source exists?" gates are the most commonly failed.
*Detection:* Audit the Context Gate results in the output. If any gate shows "skipped" or the answers were not verified, this is FM-8.
*Correction:* Run the Context Gate before any other step. If gate 3 (public-safe) fails, redact before deriving. If gate 1 (source exists) fails, write the source first.

**FM-9: Expert-Only Derivative**
*What it looks like:* The derivative uses framework jargon from the source without translation. "The COAP analysis reveals profit migration toward the distribution layer" in a LinkedIn post targeting general professionals. The source's expert terminology leaked into a channel where the audience doesn't share that vocabulary.
*Why it happens:* The Audience Context Matching framework (Framework 5) was not applied. The writer assumed the derivative's audience is the same as the source's audience.
*Detection:* Identify every technical term, framework name, or domain-specific concept in the derivative. For each: would the target channel's primary audience understand it without context? If >2 terms fail this test, the derivative is expert-only.
*Correction:* Apply the Audience Adaptation Decision Table (Framework 5). Translate jargon to the implication. "Three structural advantages protect this position" instead of "7 Powers analysis shows three strong powers."

---

## What's Next

<- This skill works best after: **Narrative Building** (if the source is a positioning piece) or any skill that produces a long-form written artifact (thesis, analysis, specification)
-> This skill's output feeds well into: **Connector** (distribution planning for derivatives), **Writer** (voice refinement), or direct publishing workflows
+ **Start here if:** You have a completed source document and need to publish it across multiple channels
**For a full content cycle:** Problem Framing -> Discovery & Research -> Competitive Market Analysis / Narrative Building -> **[SOURCE DOCUMENT CREATION]** -> **[THIS SKILL]** -> Distribution & Engagement

**Chain interface:**
- **Receives:** A completed source document (article, thesis, essay, analysis) with the target channel(s) specified
- **Produces:** Channel-ready derivative content with compression log, thesis fidelity verification, and quality check
- **Handoff artifact:** The derivative itself (ready to publish on the target channel) plus the Compression Log (audit trail for the author to review what was kept and cut)

---

## Appendix: Quick-Reference Checklist

Use this to verify output completeness before delivering:

- [ ] Context Gate passed: source exists, channel appropriate, public-safe, voice grounded
- [ ] Step 0 completed: frameworks selected for source type x target channel
- [ ] Thesis preserved: verbatim or faithful compression; fidelity check completed
- [ ] Evidence beats selected: 2-3 for short-form, 3-5 for long-form, by surprise x uniqueness ranking
- [ ] Evidence density matches channel target (per Evidence Density Calibration)
- [ ] Hook adapted: archetype matched to channel (per Hook Adaptation matrix)
- [ ] Framework/structural insight visible in derivative (not omitted for brevity)
- [ ] Counterargument preserved (strongest one, for channels that support it)
- [ ] Philosophy compressed to ≤10% of derivative (mechanism kept, depth cut)
- [ ] Voice consistent with source author (read side-by-side test)
- [ ] Channel format constraints met: word count, structure, tone, formatting
- [ ] Audience adaptation applied: jargon translated, framing adjusted, expertise assumptions matched
- [ ] Compression Log complete: every source element has disposition (Kept/Cut/Adapted) with rationale
- [ ] No uncited claims that were cited in source (evidence laundering check)
- [ ] Assumption Registry present with ≥3 assumptions, each with confidence and invalidation conditions
- [ ] Adversarial Self-Critique present with ≥3 steelmanned weaknesses
- [ ] Revision Triggers defined: when to re-derive, what to watch for
- [ ] Source Fidelity Verification scored: 12+/15, no dimension below 2
- [ ] Evidence tier tags preserved on surviving claims
- [ ] `[POTENTIALLY STALE]` flags on any evidence >6 months old
- [ ] `[EVIDENCE-LIMITED]` flags on any conclusion resting on T4-T6 evidence only
- [ ] O→I→R→C→W cascade applied to strategic recommendations within the derivative (if applicable)
- [ ] H/M/L confidence levels on all claims in the derivative
- [ ] Quality Check section completed with all boxes checked

---

## Worked Example

### Input

> **Source:** A 3,200-word Substack article titled "The Memory Paradox: Why Making AI Remember Everything Makes It Forget What Matters" — argues that AI memory systems optimize for recall volume over relevance quality, creating a personalization trap where the AI knows your history but not your context.
>
> **Target channel:** LinkedIn post
>
> **Audience context:** Senior PMs and engineering leaders at enterprise AI companies
>
> **Voice reference:** Blunt, conversational, self-implicating, short sentences, CXO test

### Output (abbreviated — demonstrates key formats)

**Context Gate:**

| Gate | Result |
|---|---|
| Source exists? | ✅ Published Substack, 3,200 words |
| Channel appropriate? | ✅ Thesis survives LinkedIn compression |
| Public-safe? | ✅ No internal data; all evidence is public research |
| Voice grounded? | ✅ Voice reference loaded |

**Step 0:** Source = Published Substack → Target = LinkedIn post. Primary: Compression Protocol, Hook Adaptation, Evidence Density. Supporting: Audience Context. Skip: Spoken Script.

**Thesis Fidelity Check:**

| Dimension | Source | Derivative | Verdict |
|---|---|---|---|
| Core claim | "AI memory systems optimize for recall volume over relevance quality, creating a personalization trap" | "We are building AI memory backwards. Optimizing for total recall. Ignoring what actually matters: relevance." | ✅ Preserved (adapted to spoken register) |
| Evidence beats | 6 in source | 3 in derivative | 3 of 6 preserved (strongest by surprise ranking) |
| Counterargument | "More memory enables emergent capabilities" | "Yes, more memory enables things. But at what cost to the user's actual experience?" | ✅ Preserved and addressed |
| Framework | "Memory Relevance Taxonomy (3 types)" | "Three types of memory. Only one matters for personalization." | ✅ Compressed inline |

**The Derivative (LinkedIn Post — 287 words):**

I run personalization for a product used by 400 million people. Every week I watch the same pattern.

We ship a memory feature. AI recalls more. Users feel less understood.

That sounds contradictory. It isn't.

PersistBench — the first serious benchmark for LLM memory — found that 97% of models exhibit sycophantic recall. They remember what you said. They don't know why it mattered.

Stanford's longitudinal study tracked 2,400 users over 8 months. Users with the most comprehensive AI memory profiles reported the lowest personalization satisfaction scores. More recall. Less relevance.

There are three types of AI memory. Episodic (what happened). Semantic (what you know). Contextual (what matters right now). We are building systems drowning in the first two and starving for the third.

Yes, comprehensive memory enables things. But optimizing for total recall while ignoring contextual relevance is how you build an AI that knows your coffee order but can't tell when you need caffeine versus sleep.

The memory paradox: the more your AI remembers, the less it understands — unless you architect for relevance over recall.

What would it look like to build memory systems that forget on purpose?

**Compression Log (abbreviated):**

| Element | Action | Rationale |
|---|---|---|
| Thesis statement | Kept, sharpened | Adapted to short-sentence spoken register for feed |
| Evidence: PersistBench study | Kept, compressed | Highest surprise factor — stat contradicts "more memory = better" |
| Evidence: Stanford longitudinal | Kept, compressed | T2 primary research; directly supports thesis |
| Evidence: MIT attention study | Cut | Lower surprise; Stanford covers same ground stronger |
| Framework: Memory Relevance Taxonomy | Kept, compressed to 3 sentences | Most accessible framework; produces memorable insight |
| Philosophical layer (500 words) | Cut (1 sentence woven in: "coffee order" line) | 10% rule; mechanism kept, depth cut |
| Counterarguments 1-3 | Kept 1, cut 2 | Strongest counterargument ("emergent capabilities") preserved |
| Closing: 2-paragraph forward look | Compressed to 1 question | LinkedIn invitation format |

---

### Why This Works

This derivative was produced by executing the full Compression Protocol (7 steps): hook sharpened to a personal-experience opener (archetype: Killer Stat supported by credential), thesis preserved with spoken-register adaptation, 3 evidence beats selected by surprise ranking (PersistBench and Stanford rank highest; MIT cut as redundant), Memory Relevance Taxonomy compressed from a full section to 3 inline sentences, philosophy compressed from 500 words to a single "coffee order" metaphor, strongest counterargument preserved and defeated in 2 sentences, and the closing compressed to one genuine question. The derivative is 287 words (within the 200-350 target), uses aggressive line breaks for feed scannability, and scores 14/15 on the Source Fidelity Verification (minor voice adaptation from written to feed register is intentional, not drift).

---

## References

**Methodology Sources:**
- Writer Agent prompt (Agent Prime) — Compression Protocol, Hook Archetypes, Spoken Script Derivation, Channel Specifications, Tone Harmonization
- Learnings P2: Production order (source first, derivatives second)
- Learnings P8: Context Verification Gate is mandatory for all formats
- Learnings P10: Default to LinkedIn post, not article
- Learnings P16: Compression is not omission
- Learnings P17: Context Gate is non-negotiable regardless of format length

**Framework References:**
- Barbara Minto, *The Pyramid Principle* (1987) — BLUF structure for executive briefings
- Ann Handley, *Everybody Writes* (2014) — channel-specific writing constraints
- Carmine Gallo, *Talk Like TED* (2014) — spoken delivery methodology, 18-minute rule
- Nancy Duarte, *Resonate* (2010) — presentation structure, audience-first framing

**Related Skills in PM Skills Arsenal:**
- Narrative Building — upstream (produces positioning content to derive from)
- Competitive Market Analysis — upstream (produces war maps that may need executive briefing derivatives)
- Discovery & Research — upstream (produces research syntheses that need distribution)
- Problem Framing — upstream (produces problem definitions that may need stakeholder briefings)
- Specification Writing — parallel (specs rarely need derivatives, but the author's content does)

---

*Created: 2026-03-12 | PM Skills Arsenal v1.0 | Multi-Channel Publishing Codex*
*Quality tier: Elite (1300+ lines, 7 encoded frameworks, quality gradients, 9 failure modes)*
*License: MIT*
