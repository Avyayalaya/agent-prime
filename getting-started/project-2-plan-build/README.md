# Guided Project 2: Plan & Build

> **Time:** ~25 minutes  
> **Prerequisites:** Completed onboarding (you have a filled `shared/context.md` and `shared/registry.json`)  
> **What you'll build:** A real project plan with Build Handoff Spec  
> **Agent used:** Planner (4-stage methodology)

This project walks you through Agent Prime's planning discipline. You'll pick a project you actually want to execute, and the Planner will take you through four stages that surface questions you'd normally skip.

By the end, you'll have a plan with phases, dependencies, risks, and kill conditions — structured enough to hand off to the Builder agent (or to yourself).

---

## Before You Start

Make sure you have:
- [x] Completed onboarding (your `shared/context.md` exists and is filled in)
- [x] VS Code with GitHub Copilot Chat open

Pick a real project. Something you've been meaning to do but haven't structured yet.

**Example projects:**
- Build a personal website or portfolio
- Create a course or workshop on your expertise
- Launch a side project or tool
- Write a book or content series
- Design a new process for your team

Write your project here (just keep it in mind): _____________________

---

## Step 1: Add Your Project to the Registry (~2 min)

Open `shared/registry.json` and add:

```json
{
  "id": "BLD-001",
  "type": "BLD",
  "title": "Your project title here",
  "status": "planning",
  "priority": "P1",
  "owner": "user",
  "created": "2026-01-01",
  "updated": "2026-01-01",
  "next_action": "Planner Stage 1: Excavation",
  "goal": "Build"
}
```

Replace the title and set today's date. Use the next available ID if BLD-001 is taken.

---

## Step 2: Stage 1 — Excavation (~5 min)

The Planner's first job is to restate your project as the *real* question. Most projects fail because they solve the wrong problem.

**Open Copilot Chat and type:**

```
@planner Stage 1: Excavation for my project: [your project title]

Here's what I want to build: [2-3 sentences describing it]
Here's why it matters to me: [1-2 sentences]

Restate the real question. What am I actually trying to accomplish? 
What assumptions am I making that might be wrong?
```

**What to expect:**
- Planner will reframe your project as a precise question
- It may challenge your assumptions or scope
- You'll get a clear problem statement that's more specific than what you started with

**What to check:**
- Does the reframed question feel more precise than your original description?
- Did it surface assumptions you hadn't noticed?
- Do you agree with the reframe (push back if not)?

---

## Step 3: Stage 2 — Research (~5 min)

Now the Planner looks at how others have solved similar problems — prior art, analogies, and approaches worth borrowing.

**Open Copilot Chat and type:**

```
@planner Stage 2: Research for [your project title]

Using the excavation from Stage 1, research:
- How have others approached similar problems?
- What analogies from other fields apply?
- What's the conventional approach, and what's wrong with it?
- What constraints should I know about?
```

**What to expect:**
- Prior art and comparable projects
- Structural analogies (patterns from other domains that apply)
- Constraints and gotchas you hadn't considered

**What to check:**
- Does the research actually inform the plan (not just pad it)?
- Did you learn something you didn't already know?

---

## Step 4: Stage 3 — Architecture (~8 min)

This is the core planning stage — phases, deliverables, dependencies, and risks.

**Open Copilot Chat and type:**

```
@planner Stage 3: Architecture for [your project title]

Using Stages 1-2, design the execution plan:
- Break it into phases (what is done in what order)
- Define deliverables for each phase (concrete outputs, not activities)
- Map dependencies (what blocks what)
- Identify the top 3-5 risks and mitigations
- Set kill conditions (when should I abandon this?)
- What's the minimum viable version that delivers value?
```

**What to expect:**
- A structured plan with 2-4 phases
- Specific deliverables with acceptance criteria
- A dependency graph showing what blocks what
- Risk register with mitigations
- Kill conditions that prevent zombie projects

**What to check:**
- Are the phases ordered correctly (dependencies respected)?
- Are deliverables concrete enough to verify ("write docs" is too vague; "README with setup instructions" is right)?
- Do the kill conditions make sense (would you actually kill the project if they triggered)?
- Is the minimum viable version something you'd actually ship?

---

## Step 5: Stage 4 — Critique (~5 min)

The final stage stress-tests the plan before you commit to building.

**Open Copilot Chat and type:**

```
@planner Stage 4: Critique for [your project title]

Run a pre-mortem on the plan from Stage 3:
- It's 3 months from now and this project failed. What went wrong?
- Devil's advocate: argue against doing this project at all
- What's the biggest blind spot in this plan?
- If I could only do ONE phase, which delivers the most value?
```

**What to expect:**
- A pre-mortem identifying likely failure modes
- A devil's advocate argument (honest, not token)
- Prioritization guidance for if time runs out

**What to check:**
- Does the pre-mortem identify real risks (not generic ones)?
- Did the critique change anything about your plan?
- Do you feel more confident about the plan after this step, not less?

---

## What You Just Did

You ran the Planner's 4-stage methodology:

```
Excavation (real question) → Research (prior art) → Architecture (plan) → Critique (stress test)
```

Each stage exists because it catches something specific:
- **Excavation** prevents solving the wrong problem
- **Research** prevents reinventing the wheel
- **Architecture** prevents scope creep and missing dependencies
- **Critique** prevents the planning fallacy

The output is a Build Handoff Spec — enough structure that you (or the Builder agent) can execute without going back to ask "wait, what are we building again?"

### What's Next

You can now hand the plan to the Builder agent:

```
@builder Execute the Build Handoff Spec for [your project title].
Start with Phase 1, Deliverable 1.
```

Or execute it yourself using the plan as your guide. Either way, the plan lives in the registry — update it as you go.

---

## Next Steps

- **Start building** — hand the plan to `@builder` or begin yourself
- **Review [Guided Project 1: Research & Publish](../project-1-research-publish/)** if you haven't already
- **Explore other agents** — see the [agent invocation reference](../../prime/invocations.md)
