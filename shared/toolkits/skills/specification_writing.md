---
name: "Specification Writing"
version: "1.0.0"
tags: ["Problem Shaping", "Execution"]
created: "2026-07-24"
valid_until: "2027-01-23"
derived_from: "original"
tested_with: ["Builder agent (generic, zero Agent Prime context)"]
---

## Purpose

Write problem statements and specifications tight enough that an AI agent or human executor can build from them without asking clarifying questions.

## Input Contract

### Required

- **Problem or feature description** (string): A plain-language statement of what needs to be built, solved, or delivered. Can be a rough brain dump — the skill transforms it into a structured spec. Minimum: one sentence describing the desired outcome.
- **Target executor** (string): Who will build from this spec — e.g., "AI agent (Claude)", "junior engineer", "cross-functional team", "contractor with no domain context." This determines the level of explicitness required.

### Optional

- **Constraints** (list of strings, default: none): Known boundaries — budget, timeline, technology stack, regulatory requirements, dependencies on other work.
- **Existing context** (string or file reference, default: none): Background documents, prior decisions, or domain knowledge the executor should have. If provided, the spec can reference it rather than inlining everything.
- **Output format preference** (string, default: "markdown document"): The desired format for the specification — markdown, JIRA ticket, PRD template, one-pager, etc.

### Anti-Inputs (what this skill does NOT handle)

- **Solution design.** This skill produces a problem specification, not an architecture document or technical design. It defines WHAT must be true when done, not HOW to build it.
- **Prioritization.** This skill does not determine whether the spec should be built. It assumes the decision to build has been made.
- **Ongoing project management.** The spec is a point-in-time artifact. Tracking progress, managing scope changes, and handling blockers are separate concerns.

## Method

### Quick Version

1. State the outcome in one sentence — what is true when this is done that isn't true now.
2. Define the boundary — what is IN scope and what is explicitly OUT of scope.
3. List acceptance criteria — testable conditions (yes/no) that together prove the outcome was achieved.
4. Identify the executor's context gap — what does the executor NOT know that they need to know to build this?
5. Fill the context gap with explicit inputs — decisions already made, constraints, dependencies, definitions of ambiguous terms.
6. Add failure conditions — what does "wrong" look like? What should the executor stop and escalate on?
7. Review: read the spec as if you have zero prior context. Every question you'd ask is a gap in the spec.

### Full Version

**Step 1: State the outcome**

Write one sentence that describes the desired end-state. This is not a feature description — it is a change in the world. Ask: "What is true after this is done that isn't true now?"

- Bad: "Build a user profile page."
- Good: "Users can view and edit their display name, email, and avatar from a single settings page accessible from the main navigation."

Decision point: If you cannot state the outcome in one sentence, the spec may be too broad. Split into multiple specs, each with its own outcome.

**Step 2: Define the boundary**

Write two lists: IN scope and OUT of scope. Be specific in both directions. OUT of scope is where most spec failures happen — the executor builds something you didn't want because you didn't say not to.

- IN scope: the specific capabilities, screens, behaviors, or deliverables included.
- OUT of scope: adjacent capabilities that a reasonable executor might assume are included but are not. Name them explicitly.

Decision point: If OUT of scope is empty, you haven't thought hard enough. Every feature borders adjacent features. Name the borders.

**Step 3: List acceptance criteria**

Write 3–10 testable conditions. Each criterion must be answerable as yes/no by someone who was not involved in writing the spec. Together, the criteria constitute a complete definition of "done."

Rules for good acceptance criteria:
- Each starts with a verb: "Users can...", "The system returns...", "The page loads in under..."
- Each is independently testable — failing one does not invalidate others.
- Include at least one negative criterion: what the system should NOT do.
- Include edge cases that are likely: empty states, error states, boundary values.

Decision point: If you have >10 acceptance criteria, the spec is likely covering multiple deliverables. Split.

**Step 4: Identify the executor's context gap**

Put yourself in the executor's position. List everything they would need to ask you before starting. Common gaps:

- Terminology: Are there domain-specific terms the executor might misinterpret?
- Decisions already made: What options were considered and rejected? (Prevents the executor from re-opening decided questions.)
- Dependencies: What must exist before this can be built? What will break if this is built wrong?
- Stakeholders: Who must review or approve the output?

**Step 5: Fill the context gap**

For each gap identified in Step 4, write the answer directly into the spec. Do not say "ask the PM" or "see Confluence" — either inline the answer or provide a specific, stable reference (file path, document URL, section heading).

Rules:
- If a term could be interpreted two ways, define it.
- If a decision was made, state the decision and one sentence of rationale (so the executor doesn't reverse it unknowingly).
- If a dependency exists, state its current status (ready / in progress / blocked).

**Step 6: Add failure conditions**

List 2–5 conditions under which the executor should stop work and escalate rather than making assumptions. These are the "if you hit this, come back to me" signals.

Examples:
- "If the API returns data in a format different from the schema below, stop and flag — do not transform it."
- "If implementing this requires changes to the authentication flow, stop — that's a separate workstream."

Decision point: If you can't name a failure condition, imagine the worst misinterpretation of this spec and write a guardrail against it.

**Step 7: Self-review**

Read the complete spec from the perspective of someone who:
- Has never spoken to you about this project.
- Has competence in execution but zero domain knowledge about your product.
- Will interpret the spec literally — no "obviously they meant X."

Every question this reader would ask is a gap. Fill it or explicitly mark it as "TBD — will be resolved by [date/person]."

## Evaluation Criteria

- [ ] The spec states the desired outcome in ≤2 sentences, describing a change in state (not a feature list).
- [ ] IN scope and OUT of scope are both explicitly listed, with OUT of scope naming at least one adjacent capability that is excluded.
- [ ] Acceptance criteria are present (minimum 3), each answerable as yes/no by someone who did not write the spec.
- [ ] No acceptance criterion uses subjective language ("high quality", "user-friendly", "fast") without a measurable threshold.
- [ ] The spec contains no ambiguous terms — every domain-specific or potentially misinterpreted term is defined.
- [ ] An executor with zero prior context about the project can begin work after reading only this spec (plus any explicitly referenced documents), without asking clarifying questions.
- [ ] At least one failure condition / escalation trigger is stated.
- [ ] All decisions already made are stated as decisions (not open questions), with enough rationale to prevent an executor from unknowingly reversing them.

## Failure Modes

**FM-1: The Wish Spec**
*What it looks like:* The spec describes a desired experience ("users should feel empowered to manage their profile") but contains no testable conditions. An executor reading it knows the *mood* but not the *deliverable*.
*Why it happens:* The author skipped Step 3 (acceptance criteria) or wrote criteria in subjective language. The outcome statement was aspirational rather than concrete.

**FM-2: The Assumed-Context Spec**
*What it looks like:* The spec makes sense to the author and their immediate team, but an outside executor asks 5+ clarifying questions before starting. Key terms are undefined, prior decisions are referenced but not stated, and dependencies are implicit.
*Why it happens:* The author skipped Step 4 (context gap identification) or filled it from their own perspective rather than the executor's. Curse of knowledge — you can't see what you already know.

**FM-3: The Unbounded Spec**
*What it looks like:* The spec has a clear outcome and good acceptance criteria, but no OUT of scope section. The executor builds adjacent features that weren't requested, or the scope grows invisibly during execution because "it seemed related."
*Why it happens:* The author treated OUT of scope as optional. Every spec borders other work. Unnamed borders become scope creep.

**FM-4: The Premature Solution Spec**
*What it looks like:* The spec prescribes implementation details (use React, call this API, put the button here) when the executor's job is to determine the best implementation. The spec conflates WHAT (problem) with HOW (solution).
*Why it happens:* The author has a solution in mind and writes the spec backward from it. The spec becomes implementation instructions disguised as a problem statement. This constrains the executor and prevents better solutions from emerging.

## Worked Example

### Input

**Problem description:** "We need a way for team leads to see which of their direct reports have completed the quarterly security training, so they can follow up with people who haven't."

**Target executor:** AI agent (Claude) with no access to our internal systems — producing a product spec document, not code.

**Constraints:** Must integrate with existing LMS (TalentHub). No new user-facing dashboards — must surface in existing manager tools.

### Output

---

**Specification: Security Training Completion Visibility for Team Leads**

**Outcome:** Team leads can see, from within their existing manager dashboard, which of their direct reports have and have not completed the current quarter's mandatory security training, without leaving the dashboard or querying another system.

**In Scope:**
- Completion status per direct report (completed / not started / in progress) for the current quarter's security training only.
- Display within the existing manager dashboard (Team Overview tab).
- Data sourced from TalentHub API (existing LMS).

**Out of Scope:**
- Historical completion data (prior quarters) — future enhancement, not this spec.
- Training content management or assignment — managed in TalentHub, not in the dashboard.
- Notifications or automated reminders to incomplete reports — separate workstream (see NOTIFY-2025-Q3).

**Acceptance Criteria:**
1. A team lead viewing their Team Overview tab sees a "Training Status" section listing each direct report with their completion status.
2. Completion status values are one of: Completed (with date), In Progress, Not Started.
3. The data reflects TalentHub state with ≤4 hour latency.
4. If a team lead has no direct reports, the section displays "No direct reports found" (not an error state).
5. If TalentHub API is unavailable, the section displays "Training data temporarily unavailable" with a timestamp of the last successful sync.
6. The section does NOT display training data for anyone outside the lead's direct reporting line.

**Context / Decisions Made:**
- *Why not a standalone dashboard?* Decision made in PM review (2025-06-12): manager tools are the primary surface. Adding new dashboards increases tool fragmentation. This is a display-in-existing-surface solution.
- *TalentHub API:* Uses the `/completions` endpoint (v2). Auth via service account — credentials managed by IT. API docs: `internal-docs/talenthub-api-v2.md`.
- *"Current quarter" definition:* Calendar quarter (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec). Determined by the `training_period` field in TalentHub.

**Failure Conditions / Escalation Triggers:**
- If TalentHub API v2 `/completions` endpoint does not return a `training_period` field, stop — the data model assumption is wrong.
- If direct-report relationships are not available from the existing org-data service, stop — this requires a new integration not scoped here.

---

### Why This Works

Steps 1–2 produced a concrete outcome and named the borders (no historical data, no notifications). Step 3 generated testable criteria including an edge case (no reports) and an error state (API down). Steps 4–5 filled the executor's context gap: why not a dashboard, which API endpoint, what "current quarter" means. Step 6 added two escalation triggers tied to assumptions the spec depends on. The output passes all 8 Evaluation Criteria — the outcome is concrete, scope is bounded, criteria are yes/no testable, no ambiguous terms remain, and an outside executor can start without asking questions.
