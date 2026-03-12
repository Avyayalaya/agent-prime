# Guided Project 1: Research & Publish

> **Time:** ~20 minutes  
> **Prerequisites:** Completed onboarding (you have a filled `shared/context.md` and `shared/registry.json`)  
> **What you'll build:** A real draft article on a topic you care about  
> **Agents used:** Scout → Synthesizer → Writer

This project walks you through Agent Prime's core intelligence pipeline. You'll pick a topic, scan for signals, build a thesis, and draft an article — using three agents that compose into a single workflow.

By the end, you'll understand how Scout, Synthesizer, and Writer work individually and how they connect.

---

## Before You Start

Make sure you have:
- [x] Completed onboarding (your `shared/context.md` exists and is filled in)
- [x] VS Code with GitHub Copilot Chat open

Pick a topic you genuinely care about. This works best when you're writing about something you have a real perspective on — not a test topic.

**Example topics:**
- A trend you've noticed in your industry
- A problem you think most people are solving wrong
- A technology shift that will change how your field works

Write your topic here (just keep it in mind): _____________________

---

## Step 1: Add Your Research Project to the Registry (~2 min)

Before any work starts, Agent Prime tracks it in the registry. Open `shared/registry.json` and add an item:

```json
{
  "id": "THS-001",
  "type": "THS",
  "title": "Your topic title here",
  "status": "in_progress",
  "priority": "P1",
  "owner": "user",
  "created": "2026-01-01",
  "updated": "2026-01-01",
  "next_action": "Scout scan for signals",
  "goal": "Matter"
}
```

Replace `"Your topic title here"` with your actual topic and set today's date.

> **Why this matters:** The registry is Agent Prime's memory. Without this entry, agents won't know this work exists. After every step, you'll update the `status` and `next_action` fields.

---

## Step 2: Scout — Scan for Signals (~5 min)

The Scout agent finds evidence, data points, and market signals related to your topic.

**Open Copilot Chat and type:**

```
@scout Scan for signals on: [your topic]

I'm looking for:
- Recent developments or announcements
- Data points or research findings
- Contrarian viewpoints or emerging debates
- Trends that most people haven't connected yet

Save signals to agents/scout/signals/
```

**What to expect:**
- Scout will search for relevant information
- It produces structured signal entries with source, date, and relevance assessment
- Signals are saved as markdown files in `agents/scout/signals/`

**What to check:**
- Are the signals real and specific (not vague platitudes)?
- Do at least 2-3 signals surprise you or add to your existing knowledge?
- Is there enough material here to form an argument?

If the signals are too generic, give Scout more specific direction:
```
@scout These signals are too broad. Focus specifically on [narrower aspect of your topic]. 
I'm especially interested in [specific angle or question].
```

**After this step, update your registry entry:**
```json
"status": "developing",
"next_action": "Synthesizer builds thesis from signals",
"updated": "2026-01-01"
```

---

## Step 3: Synthesizer — Build a Thesis (~5 min)

The Synthesizer takes raw signals and builds a structured argument — your thesis.

**Open Copilot Chat and type:**

```
@synthesizer Build a thesis from the Scout signals in agents/scout/signals/ 
about [your topic].

I want a thesis that:
- Makes a specific, falsifiable claim
- Is supported by the evidence the Scout found
- Has a clear "so what" for practitioners
- Identifies what most people are getting wrong about this topic

Save the thesis to agents/synthesizer/theses/
```

**What to expect:**
- Synthesizer reads the Scout signals
- It produces a structured thesis with: claim, supporting evidence, counterarguments, implications
- The thesis is saved as a markdown file

**What to check:**
- Is the core claim specific enough to disagree with?
- Does the evidence actually support the claim (not just loosely relate to it)?
- Would a smart person in your field find this interesting or provocative?
- Are counterarguments addressed honestly?

If the thesis feels generic:
```
@synthesizer The thesis is too safe. What's the version of this argument that would 
make [type of expert] uncomfortable? What are we actually saying that's different?
```

**After this step, update your registry entry:**
```json
"status": "developing",
"next_action": "Writer drafts article from thesis",
"updated": "2026-01-01"
```

---

## Step 4: Writer — Draft the Article (~8 min)

The Writer converts your thesis into a publishable article.

**Open Copilot Chat and type:**

```
@writer Draft an article from the thesis in agents/synthesizer/theses/[your-thesis-file].

Target: [Substack / LinkedIn / Blog — pick one]
Length: ~1500 words
Audience: [who you're writing for]

Use my voice and style from shared/context.md.
Save the draft to agents/writer/drafts/
```

**What to expect:**
- Writer reads your thesis and your voice/style from context.md
- It produces a structured draft with headline, opening hook, argument, evidence, conclusion
- The draft is saved as a markdown file

**What to check:**
- Does it sound like you (not like a generic AI article)?
- Is the opening hook compelling enough that you'd keep reading?
- Does the argument build logically from the thesis?
- Would you actually publish this (with edits)?

If the voice is wrong:
```
@writer The tone is too [formal/academic/casual]. My actual voice is more like: 
[paste a paragraph you've written before]. Rewrite the opening 3 paragraphs 
in that voice.
```

**After this step, update your registry entry:**
```json
"status": "done",
"next_action": "Edit and publish",
"updated": "2026-01-01"
```

---

## What You Just Did

You ran Agent Prime's core intelligence pipeline:

```
Scout (evidence) → Synthesizer (argument) → Writer (artifact)
```

Each agent did one thing well:
- **Scout** found raw material you might have missed
- **Synthesizer** turned scattered signals into a structured claim
- **Writer** converted the claim into something publishable in your voice

This is the same pipeline that produces any research-driven output in Agent Prime — articles, talks, strategic briefs.

### Running It Again

Next time, you don't need this guide. The pattern is:

1. Add a thesis item to the registry
2. Tell Scout what to scan for
3. Tell Synthesizer to build a thesis from the signals
4. Tell Writer to draft from the thesis
5. Update the registry as you go

You can also queue the whole pipeline in `prime/dispatch.md` and let each agent trigger the next automatically.

---

## Next Steps

- **Edit and publish** your draft — it's a real article, not a demo
- **Try [Guided Project 2: Plan & Build](../project-2-plan-build/)** to learn the Planner workflow
- **Explore other agents** — see the [agent invocation reference](../../prime/invocations.md)
