---
name: specification-writing
description: "Use when writing a product spec, feature spec, API contract, agent task spec, or any other specification where a zero-question document is required. Encodes outcome-first methodology, acceptance criteria taxonomy, scope boundary protocol, executor context model, and ambiguity resolution framework."
version: "1.3.0"
type: "codex"
tags: ["Problem Shaping", "Execution"]
created: "2026-02-19"
valid_until: "2026-08-19"
derived_from: "shared/toolkits/skills/specification_writing.md"
tested_with: ["Claude Sonnet 4.6", "Claude Opus 4.6"]
license: "MIT"
---

## Purpose

Produce a **Zero-Question Specification** — a spec so complete that any competent executor (AI agent, engineer, contractor, cross-functional team) can begin work immediately without asking a single clarifying question.

A Zero-Question Spec is not the same as a long spec. Length is a symptom, not a goal. The goal is that every assumption is surfaced, every ambiguity is resolved or explicitly marked TBD with an owner and deadline, every acceptance criterion is binary-testable, and every scope boundary names the adjacent capability it excludes.

This codex encodes six interlocking frameworks that systematize the transition from "rough feature intent" to "executable specification." Each framework targets a specific class of spec failure. Together, they eliminate the five most common causes of execution failure: unclear outcomes, untestable criteria, invisible scope creep, missing executor context, and silent assumptions.

---

## When to Use / When NOT to Use

### When to Use

- Writing a **product or feature spec** for a new user-facing capability
- Writing an **API contract spec** that multiple teams or services will implement against
- Writing an **agent task spec** for an AI agent that will execute autonomously
- Writing a **process or workflow spec** that crosses team boundaries
- Writing an **infrastructure or migration spec** where failure conditions are critical
- Writing a **research or discovery spec** where "done" is ambiguous without explicit criteria
- Upgrading a draft spec that has already generated clarifying questions from executors
- Reviewing an existing spec for completeness before handing off to execution

### When NOT to Use

- **Brainstorming or ideation** — this skill assumes you already know WHAT to build; if you don't, use Problem Framing or Discovery first
- **One-line tickets for well-understood changes** — if the executor already has full context and the change is trivial (e.g., "change button color from blue to green"), a zero-question spec is overhead
- **Exploratory prototypes with no success criteria** — if the goal is "try things and see what works," a spec constrains prematurely. Use a time-boxed spike instead.
- **Post-hoc documentation** — this skill is for BEFORE execution, not for documenting what was already built
- **Specs where the audience is exclusively yourself** — the frameworks are calibrated for context transfer to another executor. If you are the sole executor and have full context, a lighter checklist may suffice.

---

## Format Rules

These rules apply to EVERY output produced using this skill. They are not optional stylistic preferences — they are structural requirements that prevent the most common spec failure modes.

### Rule 1: Take Positions with Calibrated Confidence

Never write acceptance criteria or scope boundaries in hedged language ("should probably," "ideally," "as appropriate"). Use explicit confidence levels on every assumption:

- **H (>70%)** — this assumption is almost certainly correct; proceed without blocking on validation
- **M (40-70%)** — this assumption needs validation before execution begins; name the validator and deadline
- **L (<40%)** — this assumption is a guess; it MUST be resolved before the spec is actionable. An L-confidence assumption that remains unresolved makes the spec a draft, not a spec.

**Why this matters:** Hedged language transfers decision-making from the spec author (who has context) to the executor (who does not). Every hedge is a hidden question the executor must answer alone.

### Rule 2: Per-Cell Evidence Tier Annotation

Every decision or constraint in the spec that rests on an assumption carries an inline annotation:

- `[Validated]` — confirmed by stakeholder, data, or documented decision. Source named.
- `[Assumed: verify]` — reasonable assumption that aligns with precedent or logic, but needs explicit sign-off before execution begins. Validator named.
- `[Unknown: TBD by {date}/{person}]` — explicitly unknown; the spec is incomplete until this is resolved. The spec author acknowledges the gap rather than papering over it.

**Why this matters:** Unannotated decisions look equally certain. An executor cannot distinguish "we confirmed this with the VP" from "I guessed this in the shower." Annotations make certainty gradients visible.

### Rule 3: Scope Intervention Cascade for Ambiguous Boundaries

When scope is contested or unclear, apply this structured cascade rather than making a silent judgment call:

```
OBSERVATION   → [what's ambiguous — name the specific boundary in question]
IMPLICATION   → [what would happen if an executor misinterpreted this boundary]
RESPONSE      → [specific scope decision: IN or OUT, with rationale]
CONFIDENCE    → [H/M/L + the key assumption underlying this decision]
WATCH         → [how to detect scope creep during execution — the observable signal]
```

**Why this matters:** Silent scope decisions are the #1 source of "that's not what I meant" during execution. The cascade forces the spec author to reason about consequences before committing.

### Rule 4: Spec Type Routing Before Writing (Step 0)

Different spec types require different framework emphasis. An API contract spec needs heavy failure condition design but lighter outcome methodology. An agent task spec needs maximum context depth but can skip stakeholder mapping. Always apply the Step 0 routing table (see Application Method) before writing.

**Why this matters:** Applying all six frameworks at maximum depth to every spec is wasteful. Step 0 prevents over-engineering simple specs and under-engineering complex ones.

### Rule 5: Surface Specification Tensions Explicitly

When acceptance criteria conflict, when scope boundaries create dependencies, or when failure conditions reveal unresolved design questions — surface these explicitly as **Open Tensions** rather than silently resolving them.

Format:
```
**OPEN TENSION:** [Criterion A] requires [X], but [Criterion B] requires [Y].
These cannot both be satisfied simultaneously.
PROPOSED RESOLUTION: [your recommendation]
DECISION OWNER: [who resolves this]
DEADLINE: [when this must be resolved for the spec to be actionable]
```

**Why this matters:** Silently resolving tensions means the spec author is making design decisions that should be made by the decision owner. Surfacing tensions preserves decision authority and prevents downstream surprises.

### Rule 6: Staleness Flags

Any decision, constraint, or dependency reference older than 30 days in a rapidly-moving codebase must carry:

`[POTENTIALLY STALE — last verified {date}; verify before execution]`

**Why this matters:** Specs reference a world that changes. A dependency that was "ready" 6 weeks ago may now be deprecated. Staleness flags remind the executor to re-verify rather than trust outdated context.

### Rule 7: Evidence-Limited Flags

If a spec section rests on multiple assumptions rather than validated decisions, prepend:

`[ASSUMPTION-HEAVY: {N} unvalidated assumptions in this section; requires stakeholder sign-off before execution]`

**Why this matters:** Sections built on assumptions look identical to sections built on validated decisions. The flag alerts reviewers and executors to concentrate their verification effort where uncertainty is highest.

### Rule 8: The Spec Must Be Navigable by Every Role That Reads It

An engineer needs Acceptance Criteria and Dependencies. A QA engineer needs AC and Failure Conditions. A designer needs Outcome Statement and Scope. A stakeholder needs Outcome Statement and Open Tensions. Include a role-based reading guide so each reader finds their sections immediately. A spec that requires reading end-to-end before any team member can start work is a lecture, not a reference document.

### Rule 9: Notation Must Be Self-Explanatory

Every spec uses annotation conventions: `[Validated]`, `[Assumed: verify]`, `[Unknown: TBD]`, H/M/L confidence, quality scores (0-3). Include a notation key at the top. An executor encountering `[Assumed: verify]` for the first time should know exactly what it means and what action they should take.

---

## Output Template (Mandatory Document Skeleton)

Every Zero-Question Specification MUST follow this exact structure. Copy this skeleton and fill it in. Do not reorder sections, skip sections, or invent new top-level sections. Depth per section varies by spec type (see Step 0 routing table) — lighter sections should still appear with a brief note, not be omitted.

```markdown
# Specification: [Title — name the capability, not the project]

> **Spec type:** [Product/feature | API contract | Agent task | Process/workflow | Infrastructure/migration | Research/discovery]
> **Load-bearing frameworks:** [F-numbers] | **Supporting:** [F-numbers]
> **Date:** [YYYY-MM-DD] | **Author:** [name] | **Decision owner:** [name]
> **Zero-Question Score:** [X — computed after Step 6]

---

## How to Read This Spec

**Reading by role — start with your sections, reference others as needed:**

| Role | Must read | Reference as needed | Skip unless relevant |
|---|---|---|---|
| **Engineer / Executor** | Outcome (§1), Scope (§2), Acceptance Criteria (§3), Dependencies (§4) | Failure Conditions (§5), Implementation Guidance (§7) | Ambiguity Audit, Assumption Registry |
| **QA / Test** | Acceptance Criteria (§3), Failure Conditions (§5) | Edge cases in Scope (§2), Dependencies (§4) | Outcome rationale, Stakeholders |
| **Designer** | Outcome (§1), Scope (§2), Edge Cases in AC (§3) | Constraints (§4), Open Tensions | Dependencies, Failure Conditions |
| **PM / Stakeholder** | Outcome (§1), Scope (§2), Open Tensions, Assumption Registry | AC (§3) for completeness check | Implementation Guidance, Dependencies |
| **Decision Owner** | Outcome (§1), Open Tensions, Assumption Registry, Adversarial Self-Critique | Scope (§2) for boundary validation | Everything else — this spec should not require your deep read to be actionable |

---

## Notation Key

**Decision annotations** — every decision and constraint carries one:
- `[Validated]` — Confirmed by stakeholder, data, or documented decision. Source named. Act on it.
- `[Assumed: verify]` — Reasonable assumption; needs explicit sign-off before execution begins. Validator named.
- `[Unknown: TBD by {date}/{person}]` — Explicitly unknown. The spec is incomplete until resolved.

**Confidence levels** — applied to assumptions and scope decisions:
- **H (>70%)** — Almost certainly correct; proceed without blocking
- **M (40-70%)** — Needs validation before execution; validator and deadline named
- **L (<40%)** — This is a guess. Must be resolved before the spec is actionable.

**Acceptance Criteria quality scores:**
- **0** — Not testable (subjective, aspirational). Must rewrite.
- **1** — Testable with prior knowledge the executor may not have. Needs more context.
- **2** — Testable by an outsider using only the spec. Acceptable.
- **3** — Binary-testable with a specific threshold or automated test. Target for all "definition of done" criteria.

**Flags:**
- `[POTENTIALLY STALE]` — Referenced decision/dependency last verified >30 days ago; re-verify
- `[ASSUMPTION-HEAVY]` — Section contains multiple unvalidated assumptions; needs stakeholder review

---

## 1. Outcome Statement

**After this spec is executed:**
[One sentence. What is true that wasn't true before? Binary-testable. Score ≥ 3 on the Outcome Rubric.]

**Verification method:** [How an outsider confirms this outcome is achieved.]

**Outcome rubric score:** [0-3 + brief rationale]

---

## 2. Scope

### IN Scope

| # | Capability | Description | Acceptance Criteria Reference |
|---|---|---|---|
| S-1 | [specific capability] | [what it does] | AC-1, AC-2 |
| S-2 | | | |

### OUT of Scope

| # | Excluded Capability | Rationale | Where/When Addressed |
|---|---|---|---|
| X-1 | [named adjacent capability] | [why excluded now] | [e.g., "Phase 2 — tracked in backlog item #123"] |
| X-2 | | | |

### Scope Dependencies

[Any OUT-of-scope item that is a prerequisite for an IN-scope item. Flag these — they are execution blockers.]

### Open Scope Tensions (if any)

```
OPEN TENSION: [Capability A] requires [X], but [Capability B] requires [Y].
PROPOSED RESOLUTION: [recommendation]
DECISION OWNER: [who resolves]
DEADLINE: [when]
```

---

## 3. Acceptance Criteria

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-1 | Behavioral | [Given... When... Then... — binary pass/fail] | 0-3 | [Validated] / [Assumed: verify] / [Unknown: TBD by date/person] |
| AC-2 | Non-behavioral | [Performance/security/accessibility threshold] | 0-3 | |
| AC-3 | Negative | [What the system explicitly does NOT do] | 0-3 | |
| AC-4 | Edge case | [Empty state / error state / boundary value] | 0-3 | |
| AC-5 | Dependency | [What must be true for other criteria to be testable] | 0-3 | |

**Complexity check:** [Simple ≤5 | Medium 5-10 | Complex 10-15 | If >15, split the spec.]

**Definition of done:** [All AC criteria pass + all non-behavioral thresholds met + all dependency criteria verified.]

---

## 4. Context and Decisions

### Executor Profile

| Field | Value |
|---|---|
| Executor type | [Senior engineer / Junior engineer / AI agent / Contractor / Cross-functional team] |
| Domain familiarity | [High / Medium / Low / None] |
| Codebase familiarity | [High / Medium / Low / None] |
| Available for questions? | [Yes — sync / Yes — async / No — spec must be fully self-contained] |

### Glossary

| Term | Definition | Why non-obvious |
|---|---|---|
| [term] | [precise definition] | [what an executor might wrongly assume it means] |

### Decisions Already Made

| # | Decision | Rationale | Date | Decided by |
|---|---|---|---|---|
| D-1 | [specific design choice] | [why this over alternatives] | [date] | [name] |

### Dependencies

| # | Dependency | Type | Status | Owner | Blocker? |
|---|---|---|---|---|---|
| DEP-1 | [system/API/asset/team] | [Technical / Data / Team / External] | [Ready / In progress / Blocked] | [name] | [Yes/No] |

### Constraints

| # | Constraint | Type | Source |
|---|---|---|---|
| C-1 | [limitation] | [Technical / Resource / Timeline / Legal / Policy] | [who/what imposed this] |

### Stakeholders

| Role | Name | Involvement |
|---|---|---|
| Decision owner | [name] | Approves scope changes, resolves tensions |
| Technical lead | [name] | Reviews AC feasibility, owns architecture decisions |
| [Other] | [name] | [involvement] |

---

## 5. Failure Conditions

| # | Type | Assumption at Risk | Deviation Signal | Escalation Action | Severity |
|---|---|---|---|---|---|
| FC-1 | [Technical / Data / Process / External] | [what the spec assumes] | [observable signal that assumption is wrong] | STOP / ADJUST [how] / ESCALATE to [whom] | [Critical / Major / Minor] |
| FC-2 | | | | | |

**Worst Misinterpretation Test:**
[For each critical AC, what is the worst thing an executor could build that technically passes the criterion as written? Add failure conditions for dangerous misinterpretations.]

---

## 6. Ambiguity Audit

| # | Ambiguity Type | Question an Executor Would Ask | Resolution | Confidence |
|---|---|---|---|---|
| AMB-1 | [Definitional / Behavioral / Precedence / Temporal / Ownership] | [the question] | [answer added to spec OR TBD by {date}/{person}] | H/M/L |

**Zero-Question Score:** [Count of unresolved questions not marked TBD with owner + deadline]

---

## 7. Implementation Guidance (optional — include for complex specs)

### Suggested Approach

[High-level technical direction. Not prescriptive architecture — enough to prevent an executor from going down a dead end.]

### Known Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [risk] | H/M/L | H/M/L | [mitigation] |

### Milestones / Checkpoints

| # | Milestone | Checkpoint Criteria | Estimated Effort |
|---|---|---|---|
| M-1 | [deliverable] | [what to verify before proceeding] | [T-shirt size] |

---

## Open Tensions

[Surface any unresolved tensions between criteria, scope, constraints, or stakeholder needs. Each tension names the conflict, proposes a resolution, identifies the decision owner, and has a deadline.]

---

## Assumption Registry

| # | Assumption | Section Underpinned | Confidence | Evidence | What Would Invalidate |
|---|---|---|:---:|---|---|
| A-1 | [specific assumption] | [which section] | H/M/L | [source or reasoning] | [observable invalidation condition] |
| A-2 | | | | | |
| A-3 | | | | | |

---

## Adversarial Self-Critique

**Weakness 1: [Title]**
- **Assumption being made:** [the specific assumption]
- **What happens if wrong:** [what the executor would build incorrectly]
- **Watch indicator:** [observable signal during execution]

**Weakness 2: [Title]**
- **Assumption being made:** ...
- **What happens if wrong:** ...
- **Watch indicator:** ...

**Weakness 3: [Title]**
- **Assumption being made:** ...
- **What happens if wrong:** ...
- **Watch indicator:** ...

---

## Revision Triggers

| # | Trigger | Affected Section | Why |
|---|---|---|---|
| 1 | [specific observable condition] | [section] | [which assumption it invalidates] |
| 2 | | | |
| 3 | | | |

---

## Appendix (optional)

[Wireframes, data schemas, API signatures, reference materials — anything that supports the spec but isn't the spec itself.]
```

**Rules for using this template:**
1. **Do not skip sections.** If a section is light for this spec type (per Step 0), include it with a brief note rather than omitting it.
2. **Every AC must be scored** using the AC Quality Rubric (0-3). Criteria scoring 0-1 must be rewritten before the spec is considered complete.
3. **Every decision and constraint must carry an annotation** — `[Validated]`, `[Assumed: verify]`, or `[Unknown: TBD by {date}/{person}]`.
4. **Section headers are conclusions where possible.** Replace generic headers (e.g., "Scope") with insight headers (e.g., "Scope: Dashboard Editing Only — No Export, No Sharing, No Mobile") after completing the section.
5. **The Zero-Question Score is computed last** but appears in the header. A score > 0 means the spec is a draft, not a spec.

---

## Domain Frameworks

These six frameworks are the encoded knowledge core of this codex. Each framework targets a specific class of spec failure and provides a systematic method for eliminating it. Frameworks are numbered F1-F6 for cross-referencing in the Application Method and Step 0 routing table.

---

### Framework 1: Outcome-First Methodology (F1)

#### Definition and Context

A specification defines a **change in the world**, not a list of features. Most spec failures begin here — the author describes what will be built (a feature list) instead of what will be different after it's built (an outcome).

The distinction matters because features can be "complete" while the outcome remains unachieved. A login page can be built exactly to spec and still fail to reduce unauthorized access if the spec described the page instead of the security outcome.

**The "Change in the World" Test:** After this spec is executed, what is true that wasn't true before? If you can't answer this in one sentence, the spec is either too large (split it) or too vague (sharpen the outcome).

**Uncommon insight:** The most dangerous outcome statements are the ones that sound specific but aren't. "Users can manage their settings" sounds concrete but is actually unbounded — "manage" could mean view, edit, delete, export, import, or audit. The test is not whether the statement sounds clear to the author, but whether two different executors would build the same thing from it.

#### Outcome Statement Scoring Rubric

| Score | Criteria | Example |
|-------|----------|---------|
| **0 — Feature description** | Describes what will be built, not what changes. No observable outcome. Uses verbs like "build," "create," "add." | "Build a notification system for training compliance." |
| **1 — Aspirational outcome** | States a desired end-state but in unmeasurable or subjective terms. Uses words like "improve," "enhance," "better." | "Improve visibility into which employees have completed security training." |
| **2 — Concrete outcome, ambiguous scope** | States a measurable end-state but the boundary is unclear. A reasonable executor might build too much or too little. | "Managers can see which direct reports have completed security training." |
| **3 — Binary-testable outcome** | One sentence. States the specific change. Could be verified as true/false by an outsider. Implies a clear boundary. | "Any people-manager can, from their existing team dashboard, see each direct report's security-training completion status (complete, in-progress, not-started) and the date of last completion, without navigating to a separate system." |

**Target:** Every spec's outcome statement scores 3. A score of 2 is acceptable only if the Scope Boundary Protocol (F3) explicitly resolves the ambiguity.

#### Decision Table

| Condition | Action |
|-----------|--------|
| Outcome statement is >2 sentences | Split the spec into multiple specs, each with a single-sentence outcome |
| Outcome statement uses "improve," "enhance," "better," or "optimize" | Replace with a specific, observable change. Ask: "improve FROM what TO what?" |
| Outcome statement describes a deliverable ("build X") not an outcome ("X is possible") | Rewrite in terms of what becomes TRUE, not what gets BUILT |
| Two executors would build different things from this statement | The statement is ambiguous — add constraints or split |
| Outcome cannot be verified without asking the spec author | The statement fails the outsider test — add measurement criteria |

#### Output Format Template

```markdown
## Outcome Statement

**After this spec is executed:**
[One sentence: what is true that wasn't true before]

**Outcome Score:** [0-3] — [rationale for score]

**Verification method:** [How an outsider would confirm this outcome is achieved]
```

#### Common Traps

- **The Output/Outcome Confusion:** "Deliver a dashboard" (output) vs. "Managers can see training status without leaving their workflow" (outcome). The dashboard is a means, not an end.
- **The Aspirational Outcome:** "Improve user engagement" — improve from what baseline? To what target? By when? Aspirational outcomes are wishes, not specs.
- **The Compound Outcome:** "Users can manage settings AND receive notifications AND export data" — three outcomes pretending to be one. Each needs its own spec or its own acceptance criteria section.

---

### Framework 2: Acceptance Criteria Taxonomy (F2)

#### Definition and Context

Not all acceptance criteria serve the same function. A behavioral criterion ("user can click X and see Y") tests a different thing than a non-behavioral criterion ("page loads in <2s"). Most specs include only behavioral criteria and miss the other four types, leaving non-functional requirements, edge cases, and dependency assumptions untested.

The taxonomy classifies every acceptance criterion into one of five types, each with a specific quality test. The goal is not to generate criteria mechanically but to ensure no critical type is missing.

**Uncommon insight:** The single most impactful type to add to any spec is the **negative criterion** — what the system explicitly does NOT do. Negative criteria prevent the most common form of scope creep: the executor who adds "helpful" features that weren't requested. Every spec without negative criteria is an implicit invitation to build more than intended.

#### The Five Criterion Types

**1. Behavioral Criteria** — what the system DOES in response to user or system action.

- Format: "When [trigger], [actor] can [action] and [observable result]."
- Quality test: Can an outsider verify this by performing the trigger and observing the result? If they need to ask "what counts as [result]?" the criterion is incomplete.
- Example: "When a manager opens their team dashboard, they see a 'Training Status' column showing each direct report's completion status (complete / in-progress / not-started)."

**2. Non-Behavioral Criteria** — performance, reliability, security, accessibility thresholds.

- Format: "[Measurement] must be [operator] [threshold] under [conditions]."
- Quality test: Is the threshold a number? Is the measurement method defined? Are the conditions specified?
- Example: "The Training Status column loads in <500ms for teams of up to 50 direct reports, measured from dashboard render-complete event." `[Assumed: verify — 500ms threshold based on general UX guidelines, not user research for this feature]`

**3. Negative Criteria** — what the system explicitly does NOT do.

- Format: "The system does NOT [action] [in context]."
- Quality test: Would an executor who built this capability be wrong? If yes, the negative criterion is valid.
- Example: "The Training Status column does NOT show completion data for employees outside the manager's direct reporting line (no skip-level visibility)."

**4. Edge Case Criteria** — empty states, error states, boundary values, concurrent operations.

- Format: "When [edge condition], the system [specific behavior]."
- Quality test: Is the edge condition specific enough to reproduce? Is the expected behavior defined?
- Example: "When a manager has zero direct reports (new manager, all reports recently transferred), the Training Status column displays 'No direct reports found' instead of an empty table."

**5. Dependency Criteria** — what must be TRUE in the environment for other criteria to be testable.

- Format: "[System/service/data] must be [state] for [which criteria] to be testable."
- Quality test: If this dependency is not met, which criteria become untestable? Is the dependency's current status known?
- Example: "The HR system API (v2.3+) must be accessible and returning training completion data in the documented format for criteria 1-3 to be testable." `[Validated — API v2.3 confirmed available in staging as of 2026-02-15]`

#### AC Quality Rubric

Score each criterion individually:

| Score | Criteria | Diagnostic Question |
|-------|----------|---------------------|
| **0 — Not testable** | Subjective, aspirational, or dependent on undefined context. Uses words like "intuitive," "user-friendly," "appropriate," "reasonable." | "Could two reasonable people disagree about whether this is met?" If yes: score 0. |
| **1 — Testable with context** | Could be verified, but requires prior knowledge the executor may not have (domain terms, system behavior, user expectations). | "Would a new team member need to ask a question before testing this?" If yes: score 1. |
| **2 — Testable by outsider** | Someone with no prior context could evaluate pass/fail given the spec alone. All terms defined, all thresholds stated. | "Could a contractor who has never seen this product test this criterion using only the spec?" If yes: score 2. |
| **3 — Binary-testable with measurement** | Pass/fail determined by a specific threshold, observable state, or automated test. No human judgment required for evaluation. | "Could an automated test verify this?" If yes: score 3. |

**Targets:**
- Every criterion scores >= 2
- All "definition of done" criteria (criteria that determine whether the spec is complete) must score 3
- Criteria scoring 0 must be rewritten or removed — they create false confidence

#### Count and Composition Rules

| Spec Complexity | Minimum Criteria | Composition Requirements |
|-----------------|------------------|--------------------------|
| **Small** (single feature, one executor, no integrations) | 3-5 | >= 1 behavioral, >= 1 negative, >= 0 edge case |
| **Medium** (multi-component feature, team execution, 1-2 integrations) | 5-8 | >= 2 behavioral, >= 1 non-behavioral, >= 1 negative, >= 1 edge case |
| **Large** (cross-team feature, multiple integrations, regulatory constraints) | 8-12 | >= 3 behavioral, >= 1 non-behavioral, >= 2 negative, >= 2 edge case, >= 1 dependency |

**The 10 Criteria Rule:** If a single spec section has more than 10 acceptance criteria, the spec is likely trying to cover too much scope. Consider splitting into sub-specs, each with its own outcome statement. Exception: infrastructure/migration specs where comprehensive rollback criteria are necessary.

**The Negative Criterion Rule:** Every spec MUST have at least one negative criterion. A spec with zero negative criteria is implicitly saying "build whatever you think is appropriate beyond the stated requirements" — which is an invitation to scope creep.

#### Output Format Template

```markdown
## Acceptance Criteria

| # | Type | Criterion | Quality Score | Annotation |
|---|------|-----------|---------------|------------|
| AC-1 | Behavioral | When [trigger], [actor] can [action] and [result]. | 3 | [Validated] |
| AC-2 | Non-behavioral | [Measurement] must be [op] [threshold] under [conditions]. | 2 | [Assumed: verify] |
| AC-3 | Negative | The system does NOT [action] [context]. | 3 | [Validated] |
| AC-4 | Edge case | When [edge condition], the system [behavior]. | 2 | [Assumed: verify] |
| AC-5 | Dependency | [System] must be [state] for AC-1 through AC-3. | 3 | [Validated] |

**Criteria count:** [N] ([breakdown by type])
**Average quality score:** [X.X]
**Negative criteria present:** Yes/No
**Lowest-scoring criterion:** AC-[N] — [reason and plan to improve]
```

---

### Framework 3: Scope Boundary Protocol (F3)

#### Definition and Context

Every spec exerts a **scope gravity field** — adjacent features, related improvements, and "while we're in there" enhancements are pulled toward the spec by proximity. Without explicit boundary declaration, scope creep is inevitable because the executor cannot distinguish "intended scope" from "adjacent and tempting."

The Scope Boundary Protocol requires two things: (1) naming what is IN scope with enough specificity that the executor knows when they're done, and (2) naming what is OUT of scope by referencing specific, adjacent capabilities — not vague categories.

**Uncommon insight:** The most dangerous scope creep comes not from adding new features but from extending existing criteria. "Show training status" creeps into "show training status with filtering" which creeps into "show training status with filtering and export." Each extension feels small. The defense is naming the boundary BETWEEN "show status" and "show status with filtering" explicitly in the OUT section.

#### The Adjacent Feature Mapping Method

For every feature or capability that is IN scope, identify 2-3 features that are "in the orbit" — related enough that an executor might reasonably assume they're included — and declare them explicitly OUT.

| IN Scope | Adjacent (OUT of Scope) | Why It's Adjacent |
|----------|------------------------|-------------------|
| [Feature A] | [Feature A'] — extended version | Natural extension of A that feels like "finishing the job" |
| [Feature A] | [Feature B] — related capability | Often built alongside A but serves a different outcome |
| [Feature A] | [Feature C] — prerequisite improvement | Would make A better but is a separate initiative |

#### The Named Exclusion Rule

OUT of scope must NAME specific capabilities, not vague categories. Named exclusions are testable — an executor can check "am I building [named thing]?" Vague exclusions are not.

| Exclusion Type | Example | Testable? |
|----------------|---------|-----------|
| **Vague (unacceptable)** | "Future enhancements are out of scope" | No — "future enhancements" could mean anything |
| **Categorical (weak)** | "Reporting features are out of scope" | Partially — but what counts as "reporting"? |
| **Named (required)** | "CSV export of training data is out of scope" | Yes — the executor knows not to build CSV export |
| **Named + rationale (ideal)** | "CSV export of training data is out of scope — it will be addressed in Q3 as part of the Reporting initiative (PROJ-456)" | Yes — and the executor understands WHY, preventing re-litigation |

#### Scope Dependency Marker

When an OUT-of-scope item must be completed before this spec can be fully implemented, mark it:

`OUT [depends-on: {item} — {status: ready/in-progress/blocked/unknown}]`

This prevents the common failure mode where a spec declares something OUT of scope but then implicitly depends on it.

#### Decision Table

| Condition | Action |
|-----------|--------|
| OUT of scope section is empty | The spec is incomplete — every spec has adjacent capabilities to exclude |
| OUT of scope uses vague categories ("future work," "phase 2") | Replace with named exclusions referencing specific capabilities |
| An OUT-of-scope item is a prerequisite for an IN-scope item | Mark with Scope Dependency Marker; escalate if status is blocked or unknown |
| Executor asks "should I also build X?" during execution | X should have been in the OUT section — add it retroactively and update the spec |
| Scope section has not been reviewed by the executor | The scope section only works if the executor reads it BEFORE starting work |

#### Common Scope Boundary Traps

- **The Adjacent UI Trap:** "Build the training status column" creeps into "also update the column header styling" and "also add a tooltip" and "also make the column sortable." Each feels like a small addition. Defense: name the UI boundary explicitly ("column displays data only; sorting, filtering, and tooltips are OUT").
- **The API Extension Trap:** "Integrate with the HR API" creeps into "also handle the three edge cases the HR API doesn't document" and "also build a fallback for when the HR API is down." Defense: name the integration boundary ("spec covers happy-path integration only; error handling and fallback are separate specs").
- **The "While We're In There" Trap:** "Since we're already touching the dashboard, let's also fix the alignment bug and update the color scheme." Defense: if it's not in the outcome statement, it's not in scope. Period.

#### Output Format Template

```markdown
## Scope

### IN Scope
- [Capability 1]: [one-sentence description of what's included]
- [Capability 2]: [one-sentence description]
- [Capability 3]: [one-sentence description]

### OUT of Scope
- [Named exclusion 1]: [why it's excluded + where/when it will be addressed]
- [Named exclusion 2]: [why it's excluded]
- [Named exclusion 3]: [why it's excluded]
  OUT [depends-on: {prerequisite} — status: {ready/in-progress/blocked/unknown}]

### Adjacent Feature Map
| IN Scope | Adjacent (OUT) | Rationale for Exclusion |
|----------|---------------|------------------------|
| [Feature] | [Adjacent feature 1] | [Why excluded now] |
| [Feature] | [Adjacent feature 2] | [Why excluded now] |

### Open Scope Tensions
[Any unresolved scope boundaries — see Format Rule 5]
```

---

### Framework 4: Executor Context Model (F4)

#### Definition and Context

A spec is not a standalone document — it is a communication to a specific executor. Different executors have radically different context gaps. A spec written for a senior engineer who built the previous version of the system will fail catastrophically if handed to an AI agent or a new contractor.

The Executor Context Model forces the spec author to identify WHO will execute the spec, map their known/unknown context, and fill the gaps explicitly.

**Uncommon insight:** Most spec authors unconsciously write for a "mind-reader executor" — someone who shares the author's full context. This imaginary executor has attended every meeting, read every Slack thread, and understands every prior decision. Real executors have none of this. The antidote is to specify the executor type BEFORE writing and then systematically fill each gap category.

#### Executor Type Decision Table

| Executor Type | What They Typically Know | What They Typically Don't Know | Context Depth Required | Special Requirements |
|---|---|---|---|---|
| **AI Agent** (no system context) | General coding patterns, common frameworks, language semantics | Your codebase structure, your naming conventions, your domain model, every prior decision, every stakeholder preference | **Maximum** — define every term, every decision, every file path, every dependency. Assume zero institutional knowledge. | Acceptance criteria MUST be binary-testable (score 3). Ambiguous language will be interpreted literally. |
| **Junior Engineer** (new to team, <6 months) | Programming fundamentals, general design patterns, the technology stack | Domain model, prior architectural decisions, why things are built the way they are, team conventions | **High** — explain the "why" for all non-obvious decisions. Define domain terms. State dependencies with status. Provide file paths and entry points. | Include "Decisions Already Made" section explaining prior choices they might question. |
| **Senior Engineer** (knows codebase, >1 year) | Architecture, prior decisions, domain model, team conventions, codebase structure | Specific requirements for THIS feature, stakeholder preferences for THIS spec, constraints introduced since their last involvement | **Medium** — skip fundamentals. Focus on requirements, constraints, and deviations from established patterns. Highlight anything that CONTRADICTS existing patterns. | Flag deviations from convention explicitly: "Note: this deviates from our standard [pattern] because [reason]." |
| **Cross-functional team** (eng + design + data + QA) | Each member knows their domain deeply | What falls under their scope vs. others, handoff points, who makes which decisions, shared terminology that means different things to different roles | **High** — explicitly state responsibilities per role, handoff points between roles, and shared terminology with domain-specific definitions. | Include a RACI or responsibility matrix. Define terms that have different meanings in different disciplines. |
| **External contractor** (agency, freelancer) | General technical skills, industry patterns | Everything about your product, your users, your domain, your conventions, your history, your stakeholders | **Maximum** — assume zero institutional knowledge. Provide architectural context, domain glossary, and decision history. | Provide access instructions, environment setup, and contact points for questions. Specify communication cadence. |

#### Context Gap Identification Protocol

For the identified executor type, systematically check each of the five gap categories:

**1. Terminology Gaps** — domain-specific terms that could be misinterpreted.
- Method: List every noun in the spec that is not a common English word or a universally understood technical term. For each, ask: "Would the executor understand this exactly as I intend?" If no, define it.
- Output: Glossary of terms with precise, narrow definitions.
- Trap: "Training" could mean employee training, ML model training, or physical training. "Status" could mean HTTP status, workflow status, or enrollment status.

**2. Decision Gaps** — choices already made that the executor might re-open.
- Method: List every design or implementation choice in the spec. For each, ask: "Would the executor consider an alternative approach?" If yes, state the decision AND one sentence of rationale.
- Output: "Decisions Already Made" table with Decision, Rationale, and Date columns.
- Trap: Not stating rationale invites re-litigation. Stating rationale prevents it.

**3. Dependency Gaps** — what must exist, be ready, or be accessible before the executor can begin.
- Method: List every external system, API, dataset, design asset, or approval the spec references. For each, state its current status: ready / in-progress / blocked / unknown.
- Output: Dependency table with Name, Type, Status, and Owner columns.
- Trap: "See Confluence" is NOT filling a dependency gap. The executor may not have Confluence access, the page may be stale, or the relevant information may be buried. Inline the critical information and provide a stable, specific link as a supplement.

**4. Constraint Gaps** — limitations not obvious from the requirements.
- Method: List every constraint that affects HOW the executor builds (not WHAT they build). Technology stack requirements, performance budgets, regulatory requirements, accessibility standards, backward compatibility requirements.
- Output: Constraints table with Constraint, Type (technical/regulatory/business), and Source columns.
- Trap: Unstated constraints lead to rework. An executor who builds a React component when the team uses Vue must rebuild. State stack constraints explicitly.

**5. Stakeholder Gaps** — who must approve, who must be informed, who is the decision owner for unresolved questions.
- Method: For every open question or future decision in the spec, name the decision owner. For every deliverable, name the approver.
- Output: Stakeholder table with Role, Name, Scope of Authority, and Contact columns.
- Trap: "The team will decide" is not a stakeholder assignment. Name the person.

#### Context Filling Rules

| Condition | Action |
|-----------|--------|
| A term could mean two things | Define it inline, in the spec, with a narrow definition |
| A decision was made | State the decision AND one sentence of rationale AND the date |
| A dependency exists | State its name, type, current status (ready/in-progress/blocked/unknown), and owner |
| Context exists in another document | Inline the critical answer. Optionally link to the source as supplement, not substitute. |
| Executor type is AI Agent | All five gap categories are mandatory at maximum depth. No exceptions. |
| Executor type is Senior Engineer (known codebase) | Terminology and Decision gaps can be lighter. Dependency and Constraint gaps remain full depth. |

#### Output Format Template

```markdown
## Context and Decisions

**Target executor:** [Executor type from decision table]
**Context depth:** [Maximum / High / Medium]

### Glossary
| Term | Definition (as used in this spec) |
|------|-----------------------------------|
| [Term 1] | [Narrow, specific definition] |
| [Term 2] | [Narrow, specific definition] |

### Decisions Already Made
| # | Decision | Rationale | Date | Annotation |
|---|----------|-----------|------|------------|
| D-1 | [What was decided] | [Why — one sentence] | [Date] | [Validated] |
| D-2 | [What was decided] | [Why] | [Date] | [Assumed: verify] |

### Dependencies
| # | Name | Type | Status | Owner | Annotation |
|---|------|------|--------|-------|------------|
| DEP-1 | [System/API/asset] | [Integration/Data/Design/Approval] | [Ready/In-progress/Blocked/Unknown] | [Name] | [Validated/Stale] |

### Constraints
| # | Constraint | Type | Source |
|---|-----------|------|--------|
| C-1 | [Limitation] | [Technical/Regulatory/Business] | [Where this constraint comes from] |

### Stakeholders
| Role | Name | Scope of Authority | Contact |
|------|------|--------------------|---------|
| Decision owner | [Name] | [What they decide] | [How to reach] |
| Approver | [Name] | [What they approve] | [How to reach] |
```

---

### Framework 5: Failure Condition Design (F5)

#### Definition and Context

Failure conditions are the most valuable and most skipped section of any specification. They convert implicit assumptions — the things the spec author believes to be true but has not verified — into explicit escalation triggers that tell the executor what to do when reality diverges from the plan.

A spec without failure conditions is a spec that assumes perfect execution in a perfect world. Failure conditions make the spec robust to the real world.

**Uncommon insight:** Failure conditions are not error handling requirements. Error handling says "when the API returns a 500, show an error message." Failure conditions say "IF the API returns a 500 more than 3 times in testing, STOP execution and escalate — because the integration assumption is invalid and the spec may need revision." Failure conditions protect the spec itself, not the product.

#### The Four Types of Failure Conditions

**Type 1: Data Model Assumptions**
- Pattern: "This spec assumes [data source] returns [field] in [format]."
- Detection signal: Data structure, field names, data types, or response format differ from what the spec describes.
- Example: "If the HR API returns `training_status` as a free-text field instead of the enum (complete/in-progress/not-started), STOP — the display logic assumes a closed set of values."
- Escalation: Re-examine acceptance criteria that depend on the data model; adjust or request API contract update.

**Type 2: Integration Assumptions**
- Pattern: "This spec assumes [external service] is available, performant, and returns expected responses."
- Detection signal: Service is unavailable, returns unexpected status codes, latency exceeds threshold, or authentication fails.
- Example: "If the HR API returns non-200 responses for >5% of requests during integration testing, STOP — the spec does not include error handling or retry logic (those are OUT of scope)."
- Escalation: Determine if error handling should be added to THIS spec or a separate spec.

**Type 3: Process/Workflow Assumptions**
- Pattern: "This spec assumes the workflow has [N] stages with [specific transitions]."
- Detection signal: The actual workflow has more stages, different transitions, or conditional paths not modeled in the spec.
- Example: "If the training completion workflow includes a 'manager approval' stage (not just employee completion), STOP — the status model needs a fourth state."
- Escalation: Update the acceptance criteria to reflect the actual workflow; may require stakeholder input.

**Type 4: Authorization Assumptions**
- Pattern: "This spec assumes [role] has [permission] to [action]."
- Detection signal: The executor or the system encounters permission errors when attempting actions the spec assumes are allowed.
- Example: "If the 'manager' role does not have read access to the training completions endpoint in production, STOP — the spec assumes this permission exists. Do not request elevated permissions without PM approval."
- Escalation: Verify permission model with the platform team; may require access request process.

#### Failure Condition Quality Rubric

| Score | Criteria | Example |
|-------|----------|---------|
| **0 — Absent** | No failure conditions in the spec. Implicit assumption that everything works as expected. | [No failure conditions section] |
| **1 — Generic** | Failure conditions exist but are vague catch-alls without specific triggers or escalation paths. | "If something unexpected happens, stop and ask." |
| **2 — Typed and actionable** | Each failure condition names the specific assumption, describes the observable deviation, specifies the exact escalation action, and is tagged with a type (1-4). | "Type 2 (Integration): If HR API v2.3 returns non-200 for >5% of requests during integration testing, STOP execution. Escalate to [name] to determine if error handling should be added to this spec or addressed separately. Do not implement retry logic without spec revision." |

**Target:** >= 2 failure conditions per spec, all scoring 2.

#### The Worst Misinterpretation Test

For every acceptance criterion, ask: **"What would the executor build if they interpreted this criterion in the worst possible way?"**

- If the worst interpretation produces the wrong result: add a failure condition or clarify the criterion.
- If the worst interpretation produces an acceptable result: the criterion is robust.

This test is especially critical for AI Agent executors, who interpret literally and will follow the worst reasonable interpretation if it is not excluded.

#### Output Format Template

```markdown
## Failure Conditions

| # | Type | Assumption | Deviation Signal | Escalation Action | Annotation |
|---|------|-----------|------------------|-------------------|------------|
| FC-1 | Data Model | [What's assumed about data] | [Observable deviation] | [Specific action: STOP/ADJUST/ESCALATE to whom] | [H/M/L confidence] |
| FC-2 | Integration | [What's assumed about service] | [Observable deviation] | [Specific action] | [H/M/L] |
| FC-3 | Process | [What's assumed about workflow] | [Observable deviation] | [Specific action] | [H/M/L] |

**Failure condition count:** [N]
**All scored 2 (typed and actionable):** Yes/No
**Worst Misinterpretation Test run:** Yes/No — [number of criteria tested]
```

---

### Framework 6: Ambiguity Resolution Framework (F6)

#### Definition and Context

Ambiguity is the silent killer of specifications. The most dangerous ambiguities are the ones that feel clear to the author — because the author has context that disambiguates them. The executor does not have that context.

This framework systematizes the detection and resolution of five types of ambiguity. It culminates in the Zero-Question Protocol — a self-review method that simulates the executor's reading experience.

**Uncommon insight:** Ambiguity is not the same as incompleteness. A spec can be complete (covers every feature) and still ambiguous (multiple valid interpretations of how those features work). Ambiguity resolution requires the spec author to think adversarially: "How could a competent but uninformed executor misread this?"

#### The Five Ambiguity Types

**Type 1: Definitional Ambiguity**
- What it is: A term could mean two different things in context.
- Detection question: "What does [term] mean in this spec, and could it be read differently?"
- Resolution: Define the term inline with a specific, narrow definition. Add to Glossary.
- Example: "Status" in this spec means training completion status (complete/in-progress/not-started), NOT HTTP response status or workflow stage status.

**Type 2: Behavioral Ambiguity**
- What it is: It's unclear what should happen in a specific situation.
- Detection question: "What happens when [edge case / unusual input / concurrent operation]?"
- Resolution: Add an acceptance criterion (edge case type) for that situation.
- Example: "What happens when a manager views training status but the HR API is temporarily unavailable?" If unanswered, the executor must guess or ask.

**Type 3: Precedence Ambiguity**
- What it is: Two rules, criteria, or constraints conflict, and it's unclear which takes priority.
- Detection question: "Rule A says X but Rule B says Y — which wins when they conflict?"
- Resolution: State the priority ordering explicitly. Surface as an Open Tension if the conflict requires a design decision.
- Example: AC-2 says "load in <500ms" but AC-4 says "show all direct reports regardless of team size." For a team of 500, these may conflict. Which takes precedence?

**Type 4: Temporal Ambiguity**
- What it is: It's unclear when something starts, stops, recurs, or changes state.
- Detection question: "When does [this behavior] apply? When does it stop? What triggers the transition?"
- Resolution: Specify time bounds, triggers, and termination conditions.
- Example: "Training status updates in real time" — does this mean polling every 5 seconds, WebSocket push, or refresh on page load? "Real time" is temporally ambiguous.

**Type 5: Ownership Ambiguity**
- What it is: It's unclear who is responsible for a decision, deliverable, or action.
- Detection question: "Who decides [this open question]? Who builds [this component]? Who approves [this deliverable]?"
- Resolution: Name the decision owner and the decision process.
- Example: "The design team will provide the mockups" — which designer? By when? What if mockups aren't ready when development starts?

#### The Zero-Question Protocol

A systematic self-review method that simulates the executor's reading experience:

1. **Set the executor persona.** Choose the specific executor type from the F4 decision table. Read the spec AS that person — with their knowledge and their gaps.
2. **Read the spec linearly.** For every sentence, ask: "Would this executor understand this without asking me a question?" If no, the sentence contains a gap.
3. **List every question.** Write down every question the simulated executor would ask. Be adversarial — assume the executor is competent but has exactly the context gaps mapped in F4.
4. **Classify each question.** Map each question to one of the five ambiguity types.
5. **Resolve or mark TBD.** For each question: either fill the gap in the spec, or mark it explicitly as `[Unknown: TBD by {date}/{person}]`.
6. **Repeat.** Read the updated spec again. If new questions emerge, repeat. Continue until the question list is empty or all remaining questions are marked TBD with owners and deadlines.

#### Zero-Question Score

| Score | Meaning | Spec Status |
|-------|---------|-------------|
| **0 questions remaining** | Zero-Question Spec | Ready to execute. Hand off with confidence. |
| **1-3 questions remaining** | Near-complete | Fill the remaining gaps before sending. If gaps are TBD with owners, the spec is conditionally ready. |
| **4-7 questions remaining** | Incomplete | Significant context gaps remain. Do not hand off — the executor will stall or build the wrong thing. |
| **8+ questions remaining** | Draft only | Not ready for execution. Major revision needed. Return to Framework selection and rebuild. |

#### Ambiguity Audit Output Format

```markdown
## Ambiguity Audit

**Executor persona used:** [Executor type]
**Audit date:** [Date]

| # | Ambiguity Type | The Question | Resolution | Status |
|---|---------------|-------------|------------|--------|
| AMB-1 | Definitional | What does "status" mean here? | Defined in Glossary: training completion status (complete/in-progress/not-started) | Resolved |
| AMB-2 | Behavioral | What happens when HR API is down? | Added AC-6 (edge case): display cached data with staleness warning | Resolved |
| AMB-3 | Temporal | How often does status refresh? | [Unknown: TBD by 2026-03-01 / Sarah Chen] | Open |

**Zero-Question Score:** [N] questions remaining
**Spec status:** [Ready / Near-complete / Incomplete / Draft]
```

---

## Application Method

### Step 0: Framework Selection

Before writing any spec content, identify the spec type and select the load-bearing frameworks. Not every spec needs all six frameworks at full depth. Step 0 prevents over-engineering simple specs and under-engineering complex ones.

#### Spec Type Routing Table

| Spec Type | Load-Bearing Frameworks (apply at full depth) | Supporting Frameworks (apply at lighter depth) |
|---|---|---|
| **Product/feature spec** (new user-facing capability) | F1 (Outcome-First), F2 (AC Taxonomy), F3 (Scope Boundary), F4 (Executor Context) | F5 (Failure Conditions): add if external integrations exist. F6 (Ambiguity): use Zero-Question Protocol as final review. |
| **API contract spec** (interface definition for multiple consumers) | F2 (AC Taxonomy — behavioral + non-behavioral criteria), F5 (Failure Conditions — data model + integration types), F4 (Executor Context for API consumers) | F1: brief — outcome is "contract is implementable without questions." F3: focus on what the API does NOT handle. F6: focus on definitional ambiguity in field names and types. |
| **Agent task spec** (spec for an AI agent executor) | F4 (Executor Context — maximum depth, zero assumed knowledge), F6 (Ambiguity Resolution — AI agents interpret literally), F2 (AC Taxonomy — binary-testable criteria only, all must score 3), F5 (Failure Conditions — all 4 types) | F1: critical — AI agents need the outcome stated precisely or they will optimize for the wrong thing. F3: explicit OUT of scope prevents hallucinated scope expansion. |
| **Process/workflow spec** (cross-team workflow definition) | F3 (Scope Boundary — who does what and where handoffs occur), F4 (Executor Context — responsibility mapping per role), F6 (Temporal + ownership ambiguity resolution) | F2: focus on edge case criteria for workflow exceptions. F5: focus on process/workflow failure conditions (Type 3). F1: outcome is the workflow state change. |
| **Infrastructure/migration spec** (system change with rollback requirements) | F5 (Failure Conditions — all 4 types at maximum depth), F4 (Dependency gaps are critical — what must be in place before migration), F2 (AC with rollback criteria: "system can return to previous state within [time]") | F3: focus on what is NOT being migrated. F6: precedence ambiguity — old system rules vs. new system rules during transition. F1: outcome is the post-migration state. |
| **Research/discovery spec** (investigation with decision output) | F1 (Outcome: what insight or decision results from this research — not "do research"), F6 (Definitional ambiguity for research questions — what exactly are we trying to learn?), F2 (AC: what would "complete" look like? What artifact is produced?) | F3: scope boundary for research is "what is OUT of scope for this investigation." F4: lighter depth — researcher typically has domain knowledge. F5: lighter unless research depends on data access. |

#### How to Use Step 0

1. Identify the spec type from the routing table. If your spec spans multiple types (e.g., a product feature that includes an API contract), use the type that represents the PRIMARY deliverable and add supporting frameworks from the secondary type.
2. Apply load-bearing frameworks at full depth — every section, every rubric, every quality check.
3. Apply supporting frameworks at the depth noted — some sections may be brief or omitted if the framework note says so.
4. Document your Step 0 decision at the top of the spec: "Spec type: [type]. Load-bearing frameworks: [list]. Supporting: [list]."

---

### Quick Version (7 Steps)

For experienced practitioners who have internalized the frameworks. Use the full version for your first 5-10 specs.

| Step | Action | Framework | Quality Check |
|------|--------|-----------|---------------|
| **0** | **Select frameworks** — use the Step 0 routing table to identify load-bearing and supporting frameworks for this spec type | Routing Table | Selected 2-4 load-bearing frameworks? Documented the selection? |
| **1** | **State the outcome** — one sentence: what is true after this is done that wasn't true before? | F1 | Scores 3 on the Outcome rubric? Passes the "two executors" test? |
| **2** | **Define the boundary** — IN scope (specific capabilities) and OUT of scope (named adjacent capabilities) | F3 | OUT section has named exclusions? Adjacent Feature Map completed? |
| **3** | **Write acceptance criteria** — use the AC Taxonomy: behavioral, non-behavioral, negative, edge case, dependency | F2 | >= minimum count for complexity? All score >= 2? >= 1 negative criterion? |
| **4** | **Identify and fill context gaps** — run the Executor Context Model for your executor type across all 5 gap categories | F4 | Executor type identified? All 5 gap categories checked? No "see Confluence" references without inline answers? |
| **5** | **Add failure conditions** — >= 2 typed failure conditions using the 4-type taxonomy | F5 | >= 2 conditions? All score 2 (typed + actionable)? Worst Misinterpretation Test run? |
| **6** | **Resolve ambiguities** — run the Zero-Question Protocol. Each remaining question is a gap to fill or mark TBD | F6 | Zero-Question Score = 0? All TBDs have owner + deadline? |
| **7** | **Self-review** — score the spec against the Zero-Question Scale and all applicable rubrics | All | Elite tier on Quality Gradients? All mandatory output sections present? |

---

### Full Version

#### Step 0: Select Frameworks

**Produces:** Framework selection decision documented at the top of the spec.

1. Read the spec request / feature intent / ticket.
2. Classify the spec type using the Step 0 routing table.
3. If the spec spans multiple types, identify the primary type (the main deliverable) and note secondary types.
4. Select load-bearing frameworks (2-4) and supporting frameworks.
5. Document: "Spec type: [type]. Load-bearing: [F-numbers]. Supporting: [F-numbers with depth notes]."

**Quality checkpoint:** If you selected fewer than 2 load-bearing frameworks, the spec type may be miscategorized. If you selected all 6 at full depth, you may be over-engineering — revisit Step 0.

**Decision point:** If the spec type is "research/discovery," consider whether a spec is the right artifact at all. Research sometimes needs a brief rather than a full spec.

#### Step 1: State the Outcome

**Produces:** Outcome Statement section with rubric score.

1. Write one sentence answering: "After this spec is executed, what is true that wasn't true before?"
2. Apply the "Change in the World" test — does the sentence describe a state change, not a deliverable?
3. Score the statement using the F1 Outcome Statement Scoring Rubric (target: 3).
4. If score < 3, rewrite. Common fixes: replace "build X" with "X is possible," replace "improve" with "FROM [baseline] TO [target]," split compound outcomes.
5. Add the verification method: how would an outsider confirm this outcome is achieved?

**Quality checkpoint:** Read the outcome statement to someone with no context. Ask them: "What would you build?" If their answer doesn't match your intent, the statement is ambiguous.

**Failure looks like:** The outcome describes a deliverable ("build a dashboard") instead of a change ("managers can see training status from their existing workflow"). Or the outcome is compound (3 outcomes in one sentence).

#### Step 2: Define the Boundary

**Produces:** Scope section with IN/OUT lists, Adjacent Feature Map.

1. List everything IN scope — specific capabilities, not vague categories.
2. For each IN-scope item, identify 2-3 adjacent capabilities that are OUT.
3. Write the OUT section with named exclusions (not "future work").
4. For each OUT item, add rationale (why excluded now, where/when addressed).
5. Check for Scope Dependencies — any OUT item that's a prerequisite for an IN item? Mark it.
6. Apply the Scope Intervention Cascade (Format Rule 3) for any contested boundaries.

**Quality checkpoint:** Ask a colleague to read the OUT section. If they say "obviously that's out of scope," the exclusion is too broad. Good exclusions make the reader think "oh, I might have included that — good thing it's explicitly excluded."

**Failure looks like:** Empty OUT section. Vague exclusions ("phase 2 items"). Missing Scope Dependencies that surface during execution.

#### Step 3: Write Acceptance Criteria

**Produces:** Acceptance Criteria table with types, scores, and annotations.

1. Write behavioral criteria first — what does the system DO?
2. Add non-behavioral criteria — performance, security, accessibility thresholds.
3. Write at least one negative criterion — what does the system NOT do?
4. Add edge case criteria — empty states, error states, boundary values.
5. Add dependency criteria — what must be true for other criteria to be testable?
6. Score each criterion using the AC Quality Rubric (target: all >= 2, definition-of-done criteria = 3).
7. Check count against complexity guidelines. If > 10, consider splitting the spec.
8. Rewrite any criterion scoring 0 or 1.

**Quality checkpoint:** Hand the criteria to someone unfamiliar with the project. Ask them to evaluate each criterion as pass/fail. If they need to ask a question before they can evaluate, the criterion scores < 2.

**Failure looks like:** All criteria are behavioral (missing non-behavioral and edge cases). No negative criteria. Criteria use subjective language ("user-friendly," "intuitive," "fast").

#### Step 4: Identify and Fill Context Gaps

**Produces:** Context and Decisions section with Glossary, Decisions, Dependencies, Constraints, and Stakeholders.

1. Identify the target executor type from the F4 decision table.
2. Check Terminology gaps: list every non-obvious term. Define each.
3. Check Decision gaps: list every design choice. State decision + rationale + date.
4. Check Dependency gaps: list every external system, API, asset. State status.
5. Check Constraint gaps: list every limitation. State type and source.
6. Check Stakeholder gaps: name every decision owner and approver.
7. Apply Context Filling Rules — inline answers, not document references.

**Quality checkpoint:** Read the spec as the identified executor type. For every sentence, ask: "Would this executor understand this without asking me?" If no, the context is incomplete.

**Failure looks like:** Executor type not identified. "See Confluence" references without inline answers. Missing dependency status. Unnamed decision owners.

#### Step 5: Add Failure Conditions

**Produces:** Failure Conditions table with types, assumptions, deviation signals, and escalation actions.

1. List every assumption the spec makes about external systems, data, workflows, and permissions.
2. For each assumption, identify what deviation looks like (the signal).
3. For each deviation, define the escalation action (STOP / ADJUST / ESCALATE to whom).
4. Classify each condition using the 4-type taxonomy.
5. Score each condition using the Failure Condition Quality Rubric (target: all = 2).
6. Run the Worst Misinterpretation Test on acceptance criteria — add failure conditions for dangerous misinterpretations.

**Quality checkpoint:** >= 2 failure conditions, all scoring 2. If you have 0, you are assuming perfect execution — revisit.

**Failure looks like:** Zero failure conditions. Generic "if something goes wrong, stop" conditions. Failure conditions that don't name specific assumptions.

#### Step 6: Resolve Ambiguities

**Produces:** Ambiguity Audit table and Zero-Question Score.

1. Set the executor persona (from Step 4).
2. Read the entire spec linearly as that persona.
3. For every point of confusion, write the question the executor would ask.
4. Classify each question by ambiguity type (definitional, behavioral, precedence, temporal, ownership).
5. Resolve each question: fill the gap in the spec OR mark as `[Unknown: TBD by {date}/{person}]`.
6. Re-read. Repeat until question list is empty or all remaining questions are TBD with owners.
7. Calculate Zero-Question Score.

**Quality checkpoint:** Zero-Question Score = 0 (all gaps filled or explicitly TBD with owners). If score is 4+, the spec needs significant work — return to the relevant framework.

**Failure looks like:** Zero-Question Protocol skipped. Score not calculated. TBD items without owners or deadlines.

#### Step 7: Self-Review and Mandatory Output Sections

**Produces:** Assumption Registry, Adversarial Self-Critique, Revision Triggers. Final quality assessment.

1. Build the Assumption Registry: list every assumption, the section it underpins, confidence level (H/M/L), evidence, and what would invalidate it. Minimum 3 assumptions.
2. Write the Adversarial Self-Critique: >= 3 genuine weaknesses specific to THIS spec. For each: the assumption being made, what happens if it's wrong, and the watch indicator.
3. Write Revision Triggers: specific, observable conditions that should trigger a spec revision.
4. Score the spec against the Quality Gradients (target: Elite Tier).
5. Verify all Format Rules are applied: confidence levels, annotations, staleness flags, tension surfacing.

**Quality checkpoint:** All three mandatory output sections present and substantive (not boilerplate). Quality Gradients score is Elite Tier.

**Failure looks like:** Assumption Registry has < 3 entries. Self-Critique lists generic failure modes instead of spec-specific weaknesses. Revision Triggers are vague ("when things change").

---

## Mandatory Output Sections

These three sections MUST appear in every spec produced using this skill. They are not optional appendices — they are structural components that make the spec's uncertainty visible and manageable.

### Assumption Registry

Every spec rests on assumptions. The Assumption Registry makes them explicit, traceable, and actionable.

```markdown
## Assumption Registry

| # | Assumption | Section Underpinned | Confidence | Evidence | What Would Invalidate |
|---|-----------|--------------------:|:----------:|----------|----------------------|
| A-1 | [Specific assumption] | [Which spec section depends on this] | H/M/L | [Source or reasoning] | [Observable condition that proves this wrong] |
| A-2 | ... | ... | ... | ... | ... |
| A-3 | ... | ... | ... | ... | ... |
```

**Rules:**
- Minimum 3 assumptions per spec.
- L-confidence assumptions must carry `[ASSUMPTION-HEAVY]` annotation on the sections they underpin.
- If > 3 assumptions are M or L confidence, the spec is fragile — flag for stakeholder review (see FM-5: Assumption Avalanche).
- Assumptions invalidated during execution trigger spec revision (see Revision Triggers).

### Adversarial Self-Critique

The spec author's honest assessment of where this spec is weakest. Not generic failure modes — specific weaknesses in THIS spec.

```markdown
## Adversarial Self-Critique

### Weakness 1: [Name]
- **Assumption being made:** [The specific assumption this weakness rests on]
- **What happens if wrong:** [What the executor would build/do incorrectly]
- **Watch indicator:** [Observable signal during execution that this assumption is failing]

### Weakness 2: [Name]
- **Assumption being made:** [...]
- **What happens if wrong:** [...]
- **Watch indicator:** [...]

### Weakness 3: [Name]
- **Assumption being made:** [...]
- **What happens if wrong:** [...]
- **Watch indicator:** [...]
```

**Rules:**
- Minimum 3 weaknesses per spec.
- Each weakness must be specific to THIS spec — "specs can be misinterpreted" is not a valid weakness.
- Watch indicators must be observable during execution, not after.

### Revision Triggers

Specific, observable conditions under which this spec should be re-opened and revised.

```markdown
## Revision Triggers

This spec should be revised if any of the following occur:

1. [Specific observable condition] — because [which assumption it invalidates]
2. [Specific observable condition] — because [which section becomes inaccurate]
3. [Specific observable condition] — because [which dependency has changed]
```

**Rules:**
- Minimum 3 triggers per spec.
- Each trigger must be observable (not "if requirements change" — instead, "if the HR API deprecates the v2.3 training endpoint").
- Each trigger must name which part of the spec is affected.

---

## Quality Gradients

### Intern Tier

A spec at this tier is recognizable as a specification but fails to transfer context to the executor. It generates 8+ clarifying questions.

**What's present:**
- A description of what needs to be built (feature list, not outcome)
- Some acceptance criteria, but subjective ("the UI should be intuitive") or incomplete
- General sense of scope, but no explicit boundaries

**What's missing:**
- Outcome statement (replaced by feature description)
- Binary-testable acceptance criteria (criteria are aspirational or vague)
- OUT of scope section (absent or says "future work")
- Executor context (assumes the reader shares the author's knowledge)
- Failure conditions (absent — assumes everything works)
- Ambiguity resolution (not attempted)
- Mandatory output sections (absent)

**Observable symptoms:** Executor asks 8+ questions before starting. Multiple rounds of clarification. Executor builds something different from intent. Scope creep occurs because boundaries were never stated.

### Consultant Tier

A spec at this tier is competent and covers the major requirements. It generates 2-5 clarifying questions, primarily around edge cases and assumed context.

**What's present:**
- Clear outcome statement (scores 2 on F1 rubric — concrete but ambiguous scope)
- Testable acceptance criteria (mostly behavioral, scoring 1-2 on AC rubric)
- Basic IN/OUT scope (but OUT uses vague categories, not named exclusions)
- Fills obvious context gaps (domain terms defined, major decisions stated)
- 1-2 failure conditions (but generic, scoring 1 on FC rubric)

**What's missing:**
- AC Taxonomy applied systematically (missing non-behavioral, edge case, and dependency criteria)
- Negative criteria (the spec says what to build but not what NOT to build)
- Executor Context Model run for specific executor type (context is generic, not calibrated)
- Ambiguity audit (not conducted — ambiguities remain undetected)
- Assumption Registry (assumptions are implicit, not surfaced)
- Adversarial Self-Critique (weaknesses not examined)
- Staleness flags and evidence annotations (decisions look equally certain)

**Observable symptoms:** Executor starts work but hits 2-5 questions within the first day. Edge cases discovered during implementation require spec clarification. Minor scope creep occurs around unnamed boundaries.

### Elite Tier

A Zero-Question Spec. The executor begins work immediately. Questions that arise during execution are about implementation choices, not spec ambiguities.

**What's present — every item is required:**
- **Outcome statement scores 3** on the F1 rubric: one sentence, binary-testable, passes the "two executors" test
- **AC Taxonomy fully applied:** all 5 criterion types present where relevant; all criteria score >= 2 on the AC Quality Rubric; definition-of-done criteria score 3; >= 1 negative criterion; count within complexity guidelines
- **Scope boundary names specific adjacent capabilities:** OUT section uses named exclusions with rationale; Adjacent Feature Map completed; no vague "future work" exclusions; Scope Dependencies marked where applicable
- **Executor Context Model run for the specific executor type:** all 5 gap categories checked and filled; Glossary, Decisions, Dependencies, Constraints, and Stakeholders sections populated; no "see Confluence" without inline answers
- **Failure conditions typed using the 4-type taxonomy:** >= 2 conditions, all scoring 2 (typed + actionable); Worst Misinterpretation Test run on acceptance criteria
- **Zero-Question Protocol run and score = 0:** Ambiguity Audit table completed; all questions resolved or marked TBD with owner and deadline; executor persona documented
- **Assumption Registry completed:** >= 3 assumptions; L-confidence assumptions flagged; fragility assessment if > 3 are M/L
- **Adversarial Self-Critique completed:** >= 3 spec-specific weaknesses with watch indicators
- **Revision Triggers defined:** >= 3 observable conditions with affected sections named
- **Format Rules applied:** H/M/L confidence levels, per-cell evidence annotations, staleness flags where applicable, tensions surfaced explicitly

**Observable symptoms:** Executor begins work within hours of receiving the spec. Questions during execution are about implementation approach, not requirements. No scope creep. Failure conditions trigger spec revision before wasted effort accumulates.

---

## Failure Modes

### FM-1: The Wish Spec

- **What it looks like:** The spec reads like a product vision or marketing brief. Outcome is aspirational ("delight users," "world-class experience"). Acceptance criteria are subjective ("intuitive," "fast," "beautiful"). No measurable thresholds.
- **Why it happens:** The spec author conflates inspiration with specification. They write what they WANT, not what they need to BE TRUE. Often occurs when the author is a senior stakeholder dictating requirements verbally.
- **Detection signal:** Count the adjectives. If > 30% of acceptance criteria contain subjective adjectives (intuitive, seamless, elegant, robust, scalable — without thresholds), the spec is a wish.
- **Correction:** For every subjective criterion, ask "what would I measure to verify this?" Replace the adjective with the measurement. "Fast" becomes "loads in < 500ms under [conditions]." "Intuitive" becomes "new user completes [task] without help in < 2 minutes."

### FM-2: The Assumed-Context Spec

- **What it looks like:** The spec makes sense to the author and to anyone who attended the same meetings, but is incomprehensible or misleading to anyone else. Uses undefined acronyms, references undocumented decisions, assumes knowledge of prior conversations.
- **Why it happens:** The author writes for the "mind-reader executor" — someone who shares their full institutional context. This is the default writing mode for anyone embedded in a team.
- **Detection signal:** Hand the spec to someone who was NOT in the planning meetings. Count their questions. If they ask > 3 questions about terms, decisions, or context (not about the feature itself), the spec assumes too much context.
- **Correction:** Run the Executor Context Model (F4) for the actual executor type. Fill all 5 gap categories. Apply the Zero-Question Protocol (F6) with the correct executor persona.

### FM-3: The Unbounded Spec

- **What it looks like:** The spec describes what to build but never says what NOT to build. OUT of scope is empty or says "future enhancements." No adjacent capabilities are named. The executor doesn't know when they're done.
- **Why it happens:** Naming exclusions feels negative ("we're not building that?") and requires knowing what's adjacent — which requires deeper analysis than listing what's included. The author avoids the work of boundary-setting.
- **Detection signal:** Read the spec and ask "would a motivated executor add [adjacent feature]?" If yes, and the spec doesn't say NOT to, the spec is unbounded. Alternatively: OUT of scope is empty or contains only vague categories.
- **Correction:** Apply the Scope Boundary Protocol (F3). For every IN-scope item, name 2-3 adjacent OUT-of-scope items with named exclusions and rationale. Complete the Adjacent Feature Map.

### FM-4: The Premature Solution Spec

- **What it looks like:** The spec describes HOW to build something (specific technology, architecture, UI layout) before defining WHAT needs to be true. Implementation details crowd out requirements. The executor has no room to find a better solution.
- **Why it happens:** The author (often a senior engineer or tech lead) has already mentally designed the solution and writes the design as the spec. Requirements and constraints are implicit in the solution description rather than stated independently.
- **Detection signal:** Count the sentences about WHAT (outcomes, criteria, constraints) vs. HOW (technology, architecture, implementation). If HOW > WHAT, the spec is premature. Also: if the acceptance criteria can only be met by ONE specific implementation, the spec may be over-constrained.
- **Correction:** Separate requirements from implementation. Rewrite the outcome statement using F1 (what changes, not how). Rewrite acceptance criteria to describe WHAT must be true, not HOW to achieve it. Move implementation guidance to a non-normative "Suggested Approach" section that the executor can deviate from.

### FM-5: The Assumption Avalanche

- **What it looks like:** The spec is technically complete — all sections are present, criteria are testable, scope is bounded. But it rests on 5+ unvalidated assumptions, each of which would require a significant spec rewrite if invalidated. The spec LOOKS solid but is structurally fragile.
- **Why it happens:** The spec author filled every section but skipped validation. Each assumption was individually reasonable, but collectively they create a house of cards. No one looked at the assumption portfolio as a whole.
- **Detection signal:** Build the Assumption Registry. Count assumptions tagged `[Assumed: verify]` or with M/L confidence. If > 3 assumptions are unvalidated, the spec is fragile. If > 5, the spec is an avalanche waiting to happen.
- **Correction:** Triage assumptions by impact. For each unvalidated assumption, ask: "If this is wrong, how much of the spec must be rewritten?" Validate high-impact assumptions before the spec is finalized. Accept that the spec is a draft until critical assumptions are confirmed.

### FM-6: The Binary Criteria Gap

- **What it looks like:** The spec has acceptance criteria that appear testable but cannot actually be verified as pass/fail without asking the spec author a question. The criteria are grammatically specific but semantically dependent on unstated context.
- **Why it happens:** The author tests their own criteria against their own mental model — and they always pass, because the author knows what they meant. The criteria are evaluated by the wrong person.
- **Detection signal:** Hand each criterion to someone unfamiliar with the project. Ask: "Can you test this — yes or no — without asking me anything?" If they need to ask a question before they can test, the criterion is not binary. This is the F2 AC Quality Rubric in action — criteria scoring < 2 fail this test.
- **Correction:** For each non-binary criterion, identify the missing context that would make it testable. Add the context inline (define terms, add thresholds, specify conditions). Re-score using the AC Quality Rubric. Target: all >= 2, definition-of-done >= 3.

### FM-7: The Silent Conflict

- **What it looks like:** Two acceptance criteria, two scope decisions, or a criterion and a constraint contradict each other. Neither is wrong individually, but they cannot both be satisfied simultaneously. The executor discovers the conflict during implementation and must make a design decision that the spec should have made.
- **Why it happens:** Criteria and constraints are written independently, often by different people or at different times. No cross-check is performed. Each item is reviewed in isolation.
- **Detection signal:** For each pair of criteria, ask: "Is it possible to satisfy BOTH of these simultaneously?" If no, the spec has a silent conflict. Common examples: performance threshold vs. feature completeness, security restriction vs. user convenience, backward compatibility vs. new behavior.
- **Correction:** Surface the conflict as an Open Tension (Format Rule 5). State the conflict, propose a resolution, name the decision owner, and set a deadline. The spec is incomplete until the tension is resolved.

### FM-8: The Stale Reference

- **What it looks like:** The spec references a decision, dependency, API version, or system state that was accurate when written but has since changed. The spec is internally consistent but externally outdated.
- **Why it happens:** Specs are written at a point in time but executed later. Dependencies change, APIs are updated, decisions are revised. Without staleness management, the spec becomes silently outdated.
- **Detection signal:** Check every dependency status and every decision reference date. If any are older than 30 days in an active codebase, they may be stale. Apply Format Rule 6: staleness flags.
- **Correction:** Add `[POTENTIALLY STALE — last verified {date}; verify before execution]` to any reference older than 30 days. In the Revision Triggers, add a trigger for each stale-flagged item. Before handoff, re-verify flagged items or accept the risk explicitly.

### FM-9: The Expert-Only Spec

- **What it looks like:** The spec uses notation (`[Assumed: verify]`, H/M/L, quality scores 0-3) and framework concepts (negative criteria, edge case criteria, scope boundary protocol) without explaining them. A new team member or external contractor encounters the spec and cannot distinguish a score-2 criterion from a score-3, or understand what `[Assumed: verify]` means they should do.
- **Why it happens:** The spec author is fluent in the notation system. They assume readers are too. This is rarely true for cross-functional teams, new hires, or external executors.
- **Detection signal:** Show the spec to someone who has never used this skill. If they ask "what does this annotation mean?" for any notation, the spec fails the reader test.
- **Correction:** The output template mandates a "How to Read This Spec" section with role-based navigation and a Notation Key that explains every annotation, score, and flag. The spec should be self-contained — the reader should never need to reference the skill file to understand the spec.

---

## What's Next

### Upstream Skills (use BEFORE specification writing)

- **Problem Framing** — defines WHAT problem to solve. Specification writing defines HOW to specify the solution. If the problem is not yet framed, a spec is premature.
- **Discovery & Research** — evidence from research defines what acceptance criteria need to cover. Research outputs (user insights, data patterns, technical feasibility) feed directly into spec constraints and criteria.
- **Competitive & Market Analysis** — competitive context defines constraints and positioning that belong in the spec's Constraints section. Market requirements may define non-negotiable acceptance criteria.

### Downstream Skills (use AFTER specification writing)

- **Metric Design & Experimentation** — specs define what to measure; metrics validate whether the spec outcome was achieved. The outcome statement from F1 directly informs success metric selection.
- **Any executor** (AI agent, engineer, team, contractor) who builds from the spec. The spec IS the handoff artifact.

### Chain Interface

**Receives from upstream:**
- Problem definition or feature intent (rough description of what needs to be built)
- Target executor type (who will implement this)
- Known constraints (technical, regulatory, business, timeline)
- Prior decisions (what has already been decided and should not be re-opened)

**Produces for downstream:**
- Zero-Question Specification containing: outcome statement, IN/OUT scope with named exclusions, acceptance criteria (AC Taxonomy applied, all scored), context/decisions (Executor Context Model applied for specific executor type), failure conditions (typed using 4-type taxonomy), Assumption Registry, Adversarial Self-Critique, Revision Triggers

**Handoff artifact:** The spec IS the handoff. No separate handoff document is needed. The Assumption Registry section travels with the spec through execution — assumptions that are invalidated during execution trigger spec revision per the Revision Triggers.

---

## Appendix: Quick-Reference Checklist

Use this checklist as a final review before handing off any spec. Every item should be checkable.

### Meta
- [ ] Step 0 completed: spec type identified, load-bearing frameworks selected, decision documented
- [ ] Target executor type identified and documented
- [ ] All Format Rules applied (confidence levels, annotations, cascade, tensions, staleness flags, assumption-heavy flags)
- [ ] How to Read This Spec section present with role-based navigation
- [ ] Notation Key present: [Validated]/[Assumed]/[Unknown], H/M/L, quality scores 0-3 all explained

### Outcome (F1)
- [ ] Outcome statement is one sentence
- [ ] Outcome describes a change in the world, not a deliverable
- [ ] Outcome scores >= 3 on the Outcome Statement Scoring Rubric
- [ ] Verification method stated (how an outsider confirms the outcome)
- [ ] No compound outcomes (one outcome per spec)

### Scope (F3)
- [ ] IN scope lists specific capabilities (not vague categories)
- [ ] OUT scope lists named exclusions (not "future work" or "phase 2")
- [ ] For each IN-scope item, 2-3 adjacent OUT-of-scope items identified
- [ ] Adjacent Feature Map completed
- [ ] Scope Dependencies marked where OUT items are prerequisites for IN items
- [ ] Scope Intervention Cascade applied for any contested boundaries

### Acceptance Criteria (F2)
- [ ] AC Taxonomy applied: behavioral, non-behavioral, negative, edge case, dependency types present where relevant
- [ ] All criteria scored using AC Quality Rubric
- [ ] All criteria score >= 2; definition-of-done criteria score 3
- [ ] >= 1 negative criterion present
- [ ] Criteria count within complexity guidelines (small: 3-5, medium: 5-8, large: 8-12)
- [ ] No criterion exceeds 10 per section (or split justified)
- [ ] No subjective language without thresholds ("intuitive," "fast," "user-friendly")

### Context (F4)
- [ ] Executor type identified from decision table
- [ ] Terminology gaps: all non-obvious terms defined in Glossary
- [ ] Decision gaps: all design choices stated with rationale and date
- [ ] Dependency gaps: all external systems/APIs/assets listed with status (ready/in-progress/blocked/unknown)
- [ ] Constraint gaps: all limitations stated with type and source
- [ ] Stakeholder gaps: all decision owners and approvers named
- [ ] No "see Confluence" or "see Slack" without inline answers

### Failure Conditions (F5)
- [ ] >= 2 failure conditions present
- [ ] Each condition typed (data model / integration / process / authorization)
- [ ] Each condition scores 2 on FC Quality Rubric (typed + actionable)
- [ ] Each condition names: assumption, deviation signal, escalation action
- [ ] Worst Misinterpretation Test run on acceptance criteria

### Ambiguity (F6)
- [ ] Zero-Question Protocol run with correct executor persona
- [ ] Ambiguity Audit table completed
- [ ] Each question classified by ambiguity type
- [ ] Each question resolved or marked TBD with owner and deadline
- [ ] Zero-Question Score calculated and documented
- [ ] Score = 0 (or all remaining questions are TBD with owners)

### Mandatory Output Sections
- [ ] Assumption Registry present with >= 3 assumptions
- [ ] L-confidence assumptions flagged as [ASSUMPTION-HEAVY] on underpinned sections
- [ ] If > 3 assumptions are M/L, spec flagged as fragile (FM-5 check)
- [ ] Adversarial Self-Critique present with >= 3 spec-specific weaknesses
- [ ] Each weakness has: assumption, consequence if wrong, watch indicator
- [ ] Revision Triggers present with >= 3 observable conditions
- [ ] Each trigger names the affected spec section

### Quality Gradients Final Check
- [ ] Spec meets ALL Elite Tier criteria
- [ ] No Intern Tier symptoms present (subjective criteria, missing OUT scope, no failure conditions)
- [ ] No Consultant Tier gaps remain (missing AC types, generic failure conditions, no ambiguity audit)

---

## Worked Example

### Context

A PM needs to specify a feature that adds security training completion visibility to an existing team management dashboard. The executor is a junior engineer who joined the team 3 months ago.

### Step 0: Framework Selection

**Spec type:** Product/feature spec (new user-facing capability)
**Load-bearing frameworks:** F1 (Outcome-First), F2 (AC Taxonomy), F3 (Scope Boundary), F4 (Executor Context)
**Supporting frameworks:** F5 (Failure Conditions — external HR API integration exists), F6 (Ambiguity — Zero-Question Protocol as final review)

---

### Outcome Statement

**After this spec is executed:**
Any people-manager can, from their existing team dashboard, see each direct report's security-training completion status (complete, in-progress, not-started) and the date of last completion, without navigating to a separate system.

**Outcome Score:** 3 — Binary-testable. States the specific change (visibility from the dashboard). Implies a clear boundary (direct reports only, existing dashboard, no separate system). An outsider could verify this by checking: does the dashboard show the status? Is it limited to direct reports? Does it avoid requiring navigation to another system?

**Verification method:** Open the team dashboard as a people-manager with >= 1 direct report. Confirm the Training Status column is visible, shows status and date for each direct report, and does not require navigating away from the dashboard.

*Framework used: F1 (Outcome-First Methodology). The outcome passes the "change in the world" test — what is true after (managers can see training status on their dashboard) was not true before (they had to check a separate HR system).*

---

### Scope

#### IN Scope
- **Training status column** on the existing team dashboard page, showing completion status (complete / in-progress / not-started) and date of last completion for each direct report
- **Data integration** with the HR system API (v2.3) to retrieve training completion data
- **Empty state handling** when a manager has zero direct reports or when training data is unavailable

#### OUT of Scope
- **CSV/PDF export of training data** — will be addressed in Q3 Reporting initiative (PROJ-456) `[Validated — confirmed with VP Product 2026-02-10]`
- **Filtering or sorting the Training Status column** — the column displays data only; interactive features are a separate initiative `[Assumed: verify — this boundary should be confirmed with the design lead]`
- **Skip-level visibility** (seeing training status for reports-of-reports) — intentionally excluded to match existing dashboard's direct-report-only model `[Validated — consistent with current dashboard architecture]`
- **Training completion reminders or nudges** — notification features are owned by the L&D team and are out of scope for this dashboard feature `[Validated — L&D team confirmed ownership 2026-02-12]`
- **Historical training data** (past completions beyond the most recent) — the column shows current status only `[Assumed: verify — confirm with stakeholder whether historical view is needed]`
- **Mobile/responsive layout for the Training Status column** — the team dashboard is desktop-only; mobile support is a separate initiative
  OUT [depends-on: responsive dashboard framework — status: in-progress, ETA Q3]

#### Adjacent Feature Map

| IN Scope | Adjacent (OUT) | Rationale for Exclusion |
|----------|---------------|------------------------|
| Training status column (display) | Column sorting/filtering | Interactive column features are a separate UX initiative |
| Training status column (display) | Training completion export (CSV/PDF) | Part of Q3 Reporting initiative (PROJ-456) |
| Direct report training status | Skip-level training status | Matches existing dashboard scope (direct reports only) |
| HR API integration (read) | HR API write-back (mark complete) | Write access introduces authorization complexity; separate spec |
| Empty state handling | Error retry/fallback UX | Error handling beyond empty state is a separate resilience spec |

*Framework used: F3 (Scope Boundary Protocol). Note named exclusions with rationale — not "future work." The Adjacent Feature Map makes the scope gravity field explicit.*

---

### Acceptance Criteria

| # | Type | Criterion | Score | Annotation |
|---|------|-----------|:-----:|------------|
| AC-1 | Behavioral | When a people-manager opens the team dashboard, they see a "Training Status" column after the existing "Role" column, showing one row per direct report with fields: employee name, completion status (complete / in-progress / not-started), and date of last completion (YYYY-MM-DD format). | 3 | [Validated — column position confirmed with design lead 2026-02-14] |
| AC-2 | Non-behavioral | The Training Status column renders within 500ms of the dashboard's DOMContentLoaded event for teams of up to 50 direct reports, measured in Chrome DevTools Performance tab. | 3 | [Assumed: verify — 500ms threshold based on existing dashboard performance SLA, not user research for this specific column] |
| AC-3 | Negative | The Training Status column does NOT display completion data for employees outside the manager's direct reporting line (no skip-level, no dotted-line reports, no former direct reports). | 3 | [Validated — matches existing dashboard data model] |
| AC-4 | Negative | The Training Status column does NOT support sorting, filtering, searching, or any interactive manipulation. It is a read-only display column. | 3 | [Assumed: verify — confirm with design lead that interactive features are intentionally excluded for v1] |
| AC-5 | Edge case | When a people-manager has zero direct reports (new manager, all reports recently transferred), the Training Status column displays the message "No direct reports found" in the column area instead of an empty table or missing column. | 2 | [Assumed: verify — empty state copy not yet confirmed with content team] |
| AC-6 | Edge case | When the HR API returns a non-200 response or times out (>3s), the Training Status column displays "Training data temporarily unavailable" with a "Retry" link that re-fetches from the API. No other dashboard columns are affected. | 2 | [Assumed: verify — error UX pattern not yet reviewed by design] |
| AC-7 | Dependency | The HR system API (v2.3+) must be accessible from the dashboard's backend service and returning training completion data in the documented JSON format (see DEP-1) for AC-1, AC-2, and AC-3 to be testable. | 3 | [Validated — API v2.3 confirmed available in staging as of 2026-02-15] |

**Criteria count:** 7 (2 behavioral, 1 non-behavioral, 2 negative, 2 edge case, 1 dependency) — within medium complexity range (5-8).
**Average quality score:** 2.7
**Negative criteria present:** Yes (AC-3, AC-4)
**Lowest-scoring criterion:** AC-5, AC-6 (score 2) — edge case UX copy and error pattern need design confirmation to reach score 3.

*Framework used: F2 (Acceptance Criteria Taxonomy). All 5 types represented. All criteria score >= 2. Two negative criteria prevent scope creep (no skip-level visibility, no interactive features). Dependency criterion ensures testability.*

---

### Context and Decisions

**Target executor:** Junior Engineer (3 months on team)
**Context depth:** High — explain the "why" for all non-obvious decisions. Define domain terms. State dependencies with status.

#### Glossary

| Term | Definition (as used in this spec) |
|------|-----------------------------------|
| People-manager | An employee with >= 1 direct report in the HR system. Distinguished from "team lead" (who may not have direct reports) and "skip-level manager" (who manages managers). |
| Training status | Security training completion status as reported by the HR API: one of three enum values: `complete`, `in-progress`, `not-started`. NOT HTTP status. NOT workflow stage. |
| Direct report | An employee whose `manager_id` in the HR system matches the current user's `employee_id`. Does not include dotted-line reports, temporary assignments, or former direct reports. |
| Team dashboard | The existing `/dashboard/team` page in the management portal. This is the page that currently shows direct report name, role, and start date. |
| HR API v2.3 | The REST API exposed by the HR system at `https://hr-api.internal/v2.3/`. Training completion data is available at the `/training/completions` endpoint. API documentation: `https://docs.internal/hr-api/v2.3` `[Validated — docs current as of 2026-02-15]` |

#### Decisions Already Made

| # | Decision | Rationale | Date | Annotation |
|---|----------|-----------|------|------------|
| D-1 | Column placement: after "Role" column, before "Start Date" column | Design review determined this position aligns with information hierarchy — identity first, then role, then compliance status | 2026-02-14 | [Validated] |
| D-2 | Date format: YYYY-MM-DD | Consistent with existing dashboard date formats; avoids MM/DD vs DD/MM ambiguity for international teams | 2026-02-10 | [Validated] |
| D-3 | Status displayed as text labels, not icons or color codes | Accessibility requirement — text labels are screen-reader compatible without additional ARIA markup | 2026-02-12 | [Validated] |
| D-4 | Single API call per dashboard load, not real-time polling | Training status changes infrequently (daily at most); real-time updates add complexity without user value | 2026-02-10 | [Assumed: verify — confirm this is acceptable to stakeholders who may expect instant updates] |

#### Dependencies

| # | Name | Type | Status | Owner | Annotation |
|---|------|------|--------|-------|------------|
| DEP-1 | HR API v2.3 `/training/completions` endpoint | Integration | Ready — available in staging | Platform team (J. Martinez) | [Validated — tested 2026-02-15] |
| DEP-2 | Design mockup for Training Status column | Design | In-progress — draft available, final pending | Design team (A. Patel) | [Assumed: verify — ETA 2026-02-22] |
| DEP-3 | Dashboard backend has permission to call HR API | Authorization | Unknown — not yet verified in production | Platform team (J. Martinez) | [Unknown: TBD by 2026-02-21 / J. Martinez] |

#### Constraints

| # | Constraint | Type | Source |
|---|-----------|------|--------|
| C-1 | Dashboard frontend uses React 18 + TypeScript | Technical | Existing codebase — deviating would require migration |
| C-2 | Backend calls must go through the API gateway, not directly to HR API | Technical | Platform architecture requirement (security) |
| C-3 | No PII beyond employee name may be displayed on the dashboard | Regulatory | Data privacy policy v3.1 — training status is not PII but training dates may be in some jurisdictions `[Assumed: verify — confirm with legal]` |

#### Stakeholders

| Role | Name | Scope of Authority | Contact |
|------|------|--------------------|---------|
| Decision owner (feature) | M. Thompson (PM) | Final say on feature scope and priority | Slack: @mthompson |
| Decision owner (design) | A. Patel (Design Lead) | Final say on UX pattern and visual design | Slack: @apatel |
| Approver (code review) | S. Kim (Senior Eng) | Technical review and merge approval | Slack: @skim |
| Informed | L&D team | No decision authority on this feature; informed because it affects training visibility | Email: ld-team@company.com |

*Framework used: F4 (Executor Context Model). All 5 gap categories addressed. Context depth is High for a junior engineer — glossary defines potentially ambiguous terms, decisions include rationale, dependencies include status and owner.*

---

### Failure Conditions

| # | Type | Assumption | Deviation Signal | Escalation Action | Confidence |
|---|------|-----------|------------------|-------------------|:----------:|
| FC-1 | Data Model (Type 1) | HR API returns `training_status` as one of three enum values: `complete`, `in-progress`, `not-started` | API returns different values (e.g., `completed`, `pending`, `null`) or returns the field as free-text instead of enum | **STOP.** Do not map unknown values to the expected enum. Escalate to J. Martinez (Platform) and M. Thompson (PM). The display logic assumes a closed set. | M |
| FC-2 | Integration (Type 2) | HR API responds within 3 seconds and returns 200 for valid requests | API returns non-200 for >5% of requests during integration testing, or latency exceeds 3s consistently | **STOP integration work.** Escalate to J. Martinez (Platform). Do not build custom retry/fallback logic — that is OUT of scope (separate resilience spec). Implement AC-6 (error state UX) only. | H |
| FC-3 | Authorization (Type 4) | The dashboard backend service account has read permission on the `/training/completions` endpoint in production | Permission error (403) when calling the endpoint from the backend in staging or production | **STOP.** Do not request elevated permissions independently. Escalate to J. Martinez (Platform) and M. Thompson (PM) for access request process. | M |

**Failure condition count:** 3
**All scored 2 (typed and actionable):** Yes
**Worst Misinterpretation Test run:** Yes — tested AC-1 ("what if the executor interprets 'after the Role column' as 'replacing the Role column'?" — unlikely but added D-1 with explicit position description), AC-3 ("what if the executor interprets 'direct reporting line' to include dotted-line reports?" — clarified in Glossary definition of "direct report").

*Framework used: F5 (Failure Condition Design). Three conditions covering three of the four types (Data Model, Integration, Authorization). Process/Workflow type not applicable — this feature has no multi-stage workflow. Each condition names the specific assumption, deviation signal, and escalation action.*

---

### Ambiguity Audit

**Executor persona used:** Junior Engineer (3 months on team)
**Audit date:** 2026-02-19

| # | Ambiguity Type | The Question | Resolution | Status |
|---|---------------|-------------|------------|--------|
| AMB-1 | Definitional | Does "training" mean security training specifically, or all company training? | Clarified in Glossary: "training status" in this spec refers exclusively to security training completion. Added "security-training" to the outcome statement. | Resolved |
| AMB-2 | Behavioral | What happens if a direct report has never been enrolled in security training (vs. enrolled but not started)? | Both display as "not-started" — the HR API does not distinguish between "never enrolled" and "enrolled but not started." Added note to Glossary under "training status." | Resolved |
| AMB-3 | Temporal | How often does the training status refresh on the dashboard? | D-4 clarifies: single API call per dashboard load. Status refreshes when the manager reloads the page. No polling, no WebSocket. | Resolved |
| AMB-4 | Precedence | AC-2 (500ms load time) vs. AC-6 (3s timeout for HR API) — if the API takes 2.5s, does the 500ms criterion fail? | Clarified: AC-2's 500ms measures column render time AFTER data is received. The 3s timeout in AC-6 is the maximum wait for data. Total user-visible wait can be up to 3.5s. These do not conflict. | Resolved |
| AMB-5 | Ownership | Who decides the error message copy in AC-5 and AC-6? | Added to Stakeholder table: A. Patel (Design Lead) owns UX copy decisions. | Resolved |

**Zero-Question Score:** 0 questions remaining (all 5 resolved).
**Spec status:** Ready to execute.

*Framework used: F6 (Ambiguity Resolution Framework). Five ambiguities detected and resolved. AMB-4 (precedence) was the most dangerous — without resolution, an engineer might have tried to make the ENTIRE load experience fit in 500ms, which is impossible when the API can take up to 3s.*

---

### Assumption Registry

| # | Assumption | Section Underpinned | Confidence | Evidence | What Would Invalidate |
|---|-----------|--------------------:|:----------:|----------|----------------------|
| A-1 | HR API v2.3 returns training status as a three-value enum (complete/in-progress/not-started) | AC-1 (display values), FC-1 (data model assumption) | M | API documentation states enum values; not yet tested with live data | API returns different values, additional states, or free-text field |
| A-2 | Managers will find training status useful on the team dashboard (vs. a separate training-specific page) | Outcome statement, overall feature value | H | User research from Q4 2025 showed 73% of managers check training status weekly and currently navigate to a separate HR portal | User research was conducted 4+ months ago; preferences may have shifted `[POTENTIALLY STALE — last verified Q4 2025; verify before execution]` |
| A-3 | The dashboard backend service account has (or can get) read access to the HR training completions endpoint | AC-7 (dependency), FC-3 (authorization assumption) | M | Platform team stated "should be possible" but has not verified in production | Production permission model differs from staging; access request process takes longer than feature timeline |
| A-4 | Training status data is not classified as PII under applicable privacy regulations | C-3 (constraint) | M | Training completion status (complete/not-started) is generally not PII; however, dates of completion combined with employee identity could be considered personal data in some jurisdictions | Legal review determines that training dates constitute personal data requiring additional privacy controls |

`[ASSUMPTION-HEAVY: 3 of 4 assumptions are M-confidence; requires stakeholder sign-off before execution begins]`

---

### Adversarial Self-Critique

#### Weakness 1: HR API Data Model Unverified

- **Assumption being made:** The HR API returns training status as a clean three-value enum. The spec's display logic, acceptance criteria, and failure conditions all depend on this being true.
- **What happens if wrong:** If the API returns additional states (e.g., "expired," "exempted," "pending-approval"), the column display logic breaks or silently hides valid states. The executor might map unknown states to "not-started" — which is incorrect.
- **Watch indicator:** During integration testing, log all unique values returned by the `training_status` field. If any value is not in {complete, in-progress, not-started}, STOP and invoke FC-1.

#### Weakness 2: Performance Criterion May Be Unrealistic for Large Teams

- **Assumption being made:** 500ms render time is achievable for teams up to 50 direct reports with a single API call.
- **What happens if wrong:** If the HR API response time scales linearly with team size, large teams (30-50 reports) may push total render time past the threshold. The executor might optimize prematurely (caching, pagination) which is out of scope.
- **Watch indicator:** During development, benchmark API response time for teams of 10, 25, and 50 direct reports. If response time for 50 reports exceeds 400ms, the 500ms render budget is likely insufficient.

#### Weakness 3: Production Authorization Not Verified

- **Assumption being made:** The dashboard backend can access the HR training completions endpoint in production.
- **What happens if wrong:** The entire feature is blocked at the deployment stage. The executor builds and tests everything in staging, then discovers a permission blocker in production. All work is wasted until the access request is resolved.
- **Watch indicator:** DEP-3 status. If DEP-3 is still "Unknown" by 2026-02-21, escalate immediately — do not wait until deployment to discover the blocker.

---

### Revision Triggers

This spec should be revised if any of the following occur:

1. **HR API v2.3 is deprecated or its `/training/completions` endpoint schema changes** — because AC-1 (display format), AC-7 (dependency), and FC-1 (data model assumption) all depend on the current API contract. Source: monitor Platform team release notes.

2. **The team dashboard is migrated to a new frontend framework or receives a responsive/mobile layout** — because C-1 (React 18 constraint) and the OUT-of-scope mobile exclusion would both be affected. Source: monitor Frontend Architecture team roadmap.

3. **Legal determines that training completion dates constitute PII under applicable regulations** — because C-3 (no PII constraint) would require removing or anonymizing the date field in AC-1. Source: monitor Legal team's data classification review (expected Q2 2026).

4. **More than 3 Assumption Registry items are invalidated during execution** — because the spec is built on an assumption portfolio. Three or more invalidations indicate the spec's foundation is unsound and a holistic rewrite is needed, not patchwork fixes.

---

### Why This Works

This example demonstrates the six frameworks in concert:

| Framework | What It Contributed | Without It |
|-----------|--------------------|-----------|
| **F1: Outcome-First** | The outcome statement (score 3) makes the target state binary-testable: either managers can see training status on the dashboard or they can't. | The spec would describe "add a training column" (feature description) without clarifying the user-facing change or how to verify it. |
| **F2: AC Taxonomy** | Seven criteria across all 5 types ensure coverage of behavior, performance, exclusions, edge cases, and dependencies. Two negative criteria (AC-3, AC-4) prevent the most likely scope creep. | Criteria would cover the happy path only. Edge cases (empty state, API failure) would be discovered during implementation. Negative criteria would be absent, inviting scope creep. |
| **F3: Scope Boundary** | Six named exclusions with rationale prevent the scope gravity field from pulling in adjacent features (export, filtering, skip-level, reminders, historical data, mobile). | The executor would reasonably ask "should I also add filtering?" and "what about mobile?" — or worse, build them without asking. |
| **F4: Executor Context** | Calibrated for a junior engineer: glossary defines 5 potentially ambiguous terms, 4 decisions include rationale, 3 dependencies include status and owner, constraints are explicit. | The junior engineer would misinterpret "training status" (which training?), not know where the column goes (D-1), and discover the API permission issue (DEP-3) at deployment. |
| **F5: Failure Conditions** | Three typed conditions covering data model, integration, and authorization assumptions. Each names the specific deviation and escalation action. | The executor would encounter the API enum mismatch and guess at a mapping, or hit a 403 in production and not know who to escalate to. |
| **F6: Ambiguity Resolution** | Five ambiguities detected and resolved. AMB-4 (precedence between load time and API timeout) was particularly dangerous — silent resolution would have created an impossible requirement. | The executor would try to achieve 500ms total (including API wait), fail, and either miss the deadline or ask a clarifying question that delays work. |

**Zero-Question Score: 0.** A junior engineer can begin implementation from this spec without asking a single clarifying question. Questions that arise during implementation will be about implementation approach (how to structure the React component, how to call the API gateway), not about requirements.

---

## References

- Outcome-first methodology adapted from "Shape Up" (Basecamp) and Jobs-to-Be-Done framework
- Acceptance criteria taxonomy informed by ISTQB testing standards and Behavior-Driven Development (BDD) specification patterns
- Scope boundary protocol adapted from agile scope management and feature-mapping practices
- Executor context model derived from knowledge transfer and cognitive load research in software engineering
- Zero-Question Protocol is an original synthesis of "assumption-based planning" from military decision-making and "pre-mortem" analysis from behavioral economics
- Failure condition design informed by FMEA (Failure Modes and Effects Analysis) adapted for product specification