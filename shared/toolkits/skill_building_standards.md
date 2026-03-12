# Skill Building Standards
## PM Skills Arsenal — Design Playbook

> This document encodes every architectural, quality, and design pattern learned from:
> 1. Benchmarking PM Codex against Anthropic's competitive-analysis skill (2026-02-19)
> 2. Reading the Industry Analyst and Investment Analyst agent prompts in Agent Prime
> 3. Comparative analysis of the Claude Code skills ecosystem
>
> Apply these standards before building any new skill.

---

## 1. Skill Archetypes

Two valid archetypes. Choose before writing a single line.

| Archetype | Type value | Best for | Worst for |
|---|---|---|---|
| **Methodology** | `"methodology"` | Process guidance, templates, checklists, "how to do X step by step" | Encoding domain knowledge, framework application |
| **Codex** | `"codex"` | Domain knowledge, frameworks with scoring rubrics, decision tables, "the knowledge needed to do X well" | Process walkthrough for unfamiliar users |

**Avoid mixing.** A codex that also tries to be a tutorial becomes neither. A methodology skill that tries to encode deep frameworks becomes bloated.

**Anthropic's competitive-analysis skill** is a Methodology. Our PM Codex skills are Codex. The Methodology scored 77.1% vs. Codex's 93.3% on the 7-dimension rubric — not because Methodology is worse, but because different archetypes optimize for different dimensions.

---

## 2. Format Rules (Apply to Every Codex Skill)

These are mandatory rules derived from the Industry Analyst and Investment Analyst agent prompts and validated by benchmark scoring:

### 2.1 Position-Taking Rule
**Never hedge with weasel words.** "Likely," "may," "could," "seems" are banned from conclusions.
**Replace with:** Explicit confidence levels: **H (>70%)**, **M (40-70%)**, **L (<40%)**.
*Why:* Baseline Claude scores 0/3 on Calibration (D7) because it states everything with equal confidence. This one rule is worth ~5 points on any scoring rubric.

### 2.2 Per-Cell Evidence Annotation
**Every comparison matrix cell must carry an evidence tier tag inline.**
Format: `Strong (T2)` or `Adequate (T4: G2 reviews)` or `Unknown (T6: inferred)`.
*Why:* The most common gap in benchmark scoring — matrices contain unannotated cells that make the evidence quality opaque. An end-of-section evidence table is a supplement, not a substitute.

### 2.3 O→I→R→C→W Cascade (Mandatory for All Recommendations)
Every strategic recommendation follows:
```
OBSERVATION [evidence tier] → IMPLICATION [mechanism] → RESPONSE [specific action + owner] → CONFIDENCE [H/M/L + key assumption] → WATCH INDICATOR [observable signal]
```
*Why:* This is the single highest-impact structural pattern. Codex P2 and P4 scored 20/21 (maximum) in part because this cascade was applied throughout. P1 scored 18/21 because it was applied only in the final section.

### 2.4 Framework Selection Before Application
**Every codex skill must have a Step 0 routing table** that maps question types to the 3-4 load-bearing frameworks for that scenario.
*Why:* Benchmark outputs applied all 9 frameworks to every question — including entry frameworks (Blue Ocean, Crossing the Chasm) to defensive moat questions. This inflates length 2-3x without improving decision quality.

### 2.5 Contradiction Surfacing
**When frameworks produce contradictory conclusions, surface the contradiction explicitly.**
Do not resolve artificially or hide in footnotes.
*Why:* From the Investment Analyst prompt: *"Contradictions are FEATURES, not bugs. Preserve them as decision-relevant tensions."* A contradiction between 7 Powers (moat is strong) and COAP (profits shifting away) is the most valuable finding.

### 2.6 Staleness Flags
**Any claim based on data older than 6 months** must carry `[POTENTIALLY STALE — verify before presenting]`.
Evidence tier and evidence recency are independent dimensions — flag both.

### 2.7 Evidence-Limited Flags
**If a key strategic conclusion rests only on Tier 4-6 evidence**, prepend: `[EVIDENCE-LIMITED: validate with Tier 1-2 before acting]`.

---

## 3. Mandatory Output Sections (Every Codex Skill)

These sections must appear in every output, regardless of question type. They are quality assurance mechanisms, not optional extras.

### 3.1 Assumption Registry
A standalone table of every load-bearing assumption, modeled on investment analyst practice:

| Assumption | Framework underpinned | Confidence | Evidence | What would invalidate |
|---|---|---|---|---|

Minimum 3 assumptions. Any L-confidence assumption must be `[EVIDENCE-LIMITED]`-flagged inline.
*Why:* Absent from all three benchmark conditions. The scorecards flag this as the most important missing pattern from investment-grade analyst work.

### 3.2 Adversarial Self-Critique
A mandatory final step: *"Identify ≥3 genuine weaknesses in this analysis."*

Format per weakness:
- What assumption is being made?
- What evidence would disprove it?
- What is the watch indicator?
- Is there a scenario where this recommendation is catastrophically wrong?

**Critical:** Not optional. Not the same as scenario analysis. Must be explicitly adversarial — argue against your own conclusions as forcefully as possible.
*Why:* Industry Analyst agent has: *"If you can't find real weaknesses, you haven't looked hard enough."* This is the intellectual standard.

### 3.3 Revision Triggers
When should this analysis be re-run? Specific, observable conditions:
- [Competitor raises new funding]
- [Competitor enters your core segment]
- [A load-bearing assumption changes]
- [Win rate drops below X% vs. specific competitor]

*Why:* Transforms a point-in-time analysis into a living document. Absent from all baseline and Anthropic outputs. Present in Codex outputs as "leading indicators" — formalize into a distinct section.

### 3.4 Output Template (Mandatory Document Skeleton)

Every codex skill MUST include an **Output Template** section between Format Rules and Domain Frameworks. This template is a complete, copy-paste-ready document skeleton that defines:

1. **Exact section order** — the model sees the full structure before generating any content
2. **Table formats per section** — column headers, evidence tier placeholders, scoring columns
3. **Placeholder syntax** — `[bracketed instructions]` that make fill-in-the-blank obvious
4. **Visual formatting rules** — progress bars where applicable, emoji markers, header style

**Why this is mandatory:** Without a skeleton, formatting instructions are scattered across the skill — embedded in individual frameworks, a visualization section near the end, and formatting rules at the top. The model must assemble format cues from 10+ locations, producing inconsistent visual presentation across runs. Content structure fires reliably; visual structure does not. The output template fixes this.

**Design rules for output templates:**
- Place between Format Rules and Domain Frameworks — the model reads the skeleton before it encounters any framework content
- Include every section that could appear in the output, including conditional sections (mark with "if applicable")
- Include the mandatory output sections (Assumption Registry, Adversarial Self-Critique, Revision Triggers) in the skeleton
- Add a **"Rules for using this template"** block at the bottom (5 rules max) that enforces: no skipping sections, evidence tier tags per cell, insight headers over generic headers, which section is written last, and any skill-specific visual requirements
- The Executive Summary / header section is always written last but appears first

**Example from PM Codex competitive-market-analysis (v1.2.0):** 16-section skeleton covering Executive Summary → Step 0 → Competitive Set → 7 Powers Heat Map → ... → Adversarial Self-Critique → Revision Triggers → Sources. Added 241 lines; immediately standardized output format across all runs.

---

## 4. Quality Gradients

Three tiers of output quality for any codex skill:

| Tier | Characteristics |
|---|---|
| **Baseline** (no skill) | No frameworks named, evidence undifferentiated, conclusions stated as facts, no uncertainty acknowledged |
| **Adequate** | One framework applied, some evidence quality distinction, structured output, some specificity |
| **Elite** | Multiple frameworks applied and cross-referenced, per-cell evidence annotation, H/M/L confidence throughout, adversarial self-critique, assumption registry, revision triggers |

**Design goal:** Your skill should make Elite-tier output the default, not an exceptional outcome.

**Benchmark scores for reference (2026-02-19):**
- Baseline (Claude, no skill): 47/105 (44.8%)
- Anthropic PM Skill (methodology): 81/105 (77.1%)
- PM Codex (codex): 98/105 (93.3%)

---

## 5. Framework Encoding Patterns

### 5.1 The Scoring Rubric Pattern
Every framework must have an explicit scoring rubric with symbols and criteria — not just a definition.
*Example from 7 Powers:*
- 🟢 Strong — mature, accruing, 3+ years to replicate
- 🟡 Moderate — exists but nascent, eroding, or limited
- 🔴 Weak/Absent — no meaningful barrier

### 5.2 The Decision Table Pattern
For every framework, include at least one decision table that maps a condition to an action.
*Example:* "If no competitor holds >2 strong powers → market is structurally contestable. If one holds 4+ → likely long-term winner."

### 5.3 The Replication Cost Test
For moat-related frameworks: "What would it cost a well-funded competitor to replicate this position? How long would it take?"
If the answer is <2 years and <$1B → moat score should be ≤4 regardless of current market position.
*Source: Industry Analyst agent.*

### 5.4 The Uncommon Knowledge Test
For every framework output: classify each finding as:
- **Common knowledge** — a smart generalist already knows this (include minimally)
- **Domain knowledge** — a domain expert knows this (include for completeness)
- **Uncommon knowledge** — neither would know this **(lead with this — this is insight)**

Elite-tier outputs have a high ratio of uncommon knowledge. Generic outputs are mostly common knowledge with domain vocabulary.

### 5.5 The Asymmetric Competition Pattern
For every primary competitor, include:
- What do they optimize for?
- What are they willing to sacrifice?
- What does winning look like from their perspective?

This produces insights that feature matrices cannot. The insight that *Visier's free tier is a benchmark data flywheel* — not a price move — comes from this pattern applied to Aggregation Theory.

---

## 6. Architecture Patterns

### 6.1 Codex vs. Process Skills (Don't Conflate)
| Codex skill | Process/Methodology skill |
|---|---|
| Encodes WHAT frameworks to use and HOW to apply them | Tells you WHERE to get data and WHAT process to follow |
| Self-contained reasoning engine | Orchestration guide |
| Framework depth is the value | Source lists, templates, and process steps are the value |

Anthropic's competitive-analysis skill is excellent at its archetype (methodology). Our codex is excellent at a different archetype. They are complementary, not competitive.

**Implication:** Don't add source-crawling logic to a codex skill. Do add evidence requirements (what each framework needs as input) so the user/agent knows what to gather before applying the codex.

### 6.2 Composition Over Inclusion
When you have existing specialized agents (e.g., Industry Analyst, Investment Analyst), do NOT duplicate their functionality in the skill.
Instead: define the **Input Contract** — what the skill needs as input, expressed as evidence types.

| Framework | Minimum evidence needed |
|---|---|
| 7 Powers | Market share signals, pricing data, switching cost estimates, job postings |
| Aggregation Theory | User acquisition data, supplier count, distribution data, marginal cost signals |
| Blue Ocean | Non-customer behavior, substitute usage, demand-side research |
| Crossing the Chasm | Early adopter profiles, mainstream buyer signals, reference customer data |
| Win/Loss | ≥5 customer interviews post-decision, CRM deal notes, churn attribution data |

The skill is the reasoning engine. The analyst agents are the evidence engines. They are different layers.

### 6.3 Output Format by Question Type
Do not produce one-size-fits-all output length. Calibrate to the question:

| Question type | Target output format |
|---|---|
| Quick moat check | 3-4 framework applications, ≤2,000 words |
| Competitive response | 5-6 frameworks + response matrix, ≤3,500 words |
| Market entry | 6-7 frameworks + go/no-go recommendation with conditions, ≤4,000 words |
| Board/investor prep | All frameworks tiered, ≤5,000 words, executive summary first |

A 13,000-word output for a 2,000-word question is a failure mode — even if the content quality is high. The Industry Analyst agent has an explicit: *"Target 3,000-5,000 words total."* The Investment Analyst: *"Target ≤5,000 words total."*

---

## 7. Plugin Structure

For skills to be discoverable and installable as a Claude Code plugin:

```
pm-skills-plugin/               ← plugin root
  .claude-plugin/
    plugin.json                 ← plugin identity (name, version, author)
    marketplace.json            ← self-marketplace manifest (source: "./")
  skills/
    <skill-name>/
      SKILL.md                  ← the skill itself
  README.md
```

**Key YAML fields in SKILL.md:**
- `name` — lowercase identifier (e.g., `competitive-market-analysis`)
- `description` — triggers auto-activation by Claude Code agents; write as "Use when..."
- `type` — `"codex"` or `"methodology"`
- `version` — semver

**Installation:**
```bash
# From the plugin's parent directory:
claude plugin marketplace add ./pm-skills-plugin
claude plugin install pm-skills@pm-skills-dev

# To update after edits:
claude plugin update pm-skills@pm-skills-dev
```

---

## 8. Benchmarking New Skills

Before publishing any skill, run a head-to-head benchmark:

**Setup:**
1. Define 5 prompts at escalating difficulty (P1=entry, P5=expert synthesis)
2. Run 3 conditions: Baseline (no skill), closest competitor skill, your skill
3. Score on 7 dimensions × 0-3 scale (max 21/output, 105/condition)

**Scoring rubric:**
| Dimension | 3 criteria |
|---|---|
| D1 Framework Application | Multiple frameworks applied precisely, cross-referenced |
| D2 Evidence Hierarchy | Inline tier annotations on every substantive claim |
| D3 Strategic Specificity | Precise, sequenced, actionable steps with owners |
| D4 Failure Mode Awareness | Failure modes + adversarial self-critique + countermeasures |
| D5 Synthesis Quality | Cross-framework tensions surfaced and resolved |
| D6 Output Structure | Executive-ready, decision-first |
| D7 Calibration | H/M/L explicit on every conclusion, assumptions surfaced |

**Publication threshold:** Score ≥90/105 (85.7%) across all 5 prompts before publishing publicly.

**PM Codex benchmark baseline (2026-02-19):** 98/105 (93.3%) — above publication threshold.

---

## 9. Lessons from Agent Prime Analyst Agents

Key design patterns from the Industry Analyst and Investment Analyst prompts that apply to skill design:

| Pattern | Source agent | Apply to skills as |
|---|---|---|
| Format Rules at top | Both agents | Mandatory rules section before domain frameworks |
| H/M/L confidence | Both agents | Format Rule 2.1 |
| Three-annotation system (confidence + assumption + verification source) | Investment Analyst | O→I→R→C→W cascade |
| Adversarial self-critique | Both agents | Mandatory output section |
| Assumption registry | Both agents | Mandatory output section |
| Revision triggers | Industry Analyst | Mandatory output section |
| DATA-LIMITED flag | Industry Analyst | EVIDENCE-LIMITED flag |
| Quality Check checklist | Both agents | Appendix Checklist |
| Feedback template | Both agents | Not needed for skills (skills are consumed, not reviewed) |
| Decision-first structure | Investment Analyst | "Executive summary first" in Quality Gradients |
| Tiering (Tier 1/2 = full analysis, Tier 2 = screening note) | Investment Analyst | Framework Selection routing (Step 0) |
| Replication cost test for moat evaluation | Industry Analyst | Section 5.3 of this document |
| Cross-lens tensions as features | Investment Analyst | Contradiction Surfacing rule (2.5) |
| Wright's Law test for bottleneck durability | Industry Analyst | Analog: Replication Cost Test for moat durability |

---

*Created: 2026-02-19 | BLD-003 post-benchmark*
*Source: Benchmark scorecard at `benchmark/scores/scorecard.md`*
*Source: Industry Analyst prompt at `agents/industry_analyst/prompt.md`*
*Source: Investment Analyst prompt at `agents/investment_analyst/prompt.md`*
