---
name: "Research Synthesis"
version: "1.0.0"
tags: ["Context Engineering", "Evaluation"]
created: "2026-07-24"
valid_until: "2027-01-23"
derived_from: "agents/synthesizer/prompt.md"
tested_with: ["Builder agent (generic, zero Agent Prime context)"]
---

## Purpose

Turn multiple primary and secondary sources into a structured, evidence-graded synthesis with explicit confidence levels, counter-evidence, and actionable implications.

## Input Contract

### Required

- **Research question or thesis claim** (string): A specific question to answer or claim to evaluate. Must be falsifiable or scoped enough that the synthesis can conclude with a position. Example: "Does long-context window size improve RAG accuracy, or does retrieval quality matter more?"
- **Source materials** (list of strings or documents): Minimum 3 sources. Each source should be a document, article, paper, dataset, or structured observation. Sources can be full text, URLs, or summaries — but the synthesis quality scales with source depth.

### Optional

- **Target audience** (string, default: "senior product/technical leader"): Who will read the synthesis. Determines the depth of technical detail and the framing of implications.
- **Evidence standard** (string, default: "mixed"): One of: `"academic"` (peer-reviewed sources prioritized, statistical rigor required), `"practitioner"` (production experience and case studies weighted equally to research), `"mixed"` (both accepted, graded transparently).
- **Counter-evidence requirement** (boolean, default: true): Whether the synthesis must actively seek and present evidence against its primary conclusion.
- **Source verification status** (list of objects, default: unverified): For each source, whether the URL/citation has been independently verified. Format: `{source_id, url_verified: true|false}`. Unverified sources can be used but must be flagged in the output.

### Anti-Inputs (what this skill does NOT handle)

- **Original research.** This skill synthesizes existing sources — it does not design experiments, collect primary data, or run analyses. If the question requires new data to answer, the output should say so.
- **Summarization.** A synthesis takes a position and grades evidence for and against it. A summary restates what each source says. If the caller wants a summary, this is the wrong skill.
- **Recommendations for a specific product or business.** The synthesis produces a structured argument with implications. Translating implications into "what to build" or "what to ship" requires domain-specific judgment that belongs to the caller, not the skill.

## Method

### Quick Version

1. Decompose the research question into 2–5 sub-questions that together answer the main question.
2. Map each source to the sub-questions it addresses — identify coverage gaps.
3. Extract claims from each source with evidence type (empirical data, case study, expert opinion, logical argument) and strength (strong/moderate/weak).
4. For each sub-question, synthesize across sources: where do they agree, where do they conflict, where is evidence absent?
5. Grade confidence for each sub-question: High (multiple strong, convergent sources), Medium (mixed or limited evidence), Low (single source, conflicting evidence, or extrapolation).
6. Construct the counter-argument: what is the strongest case against your primary conclusion? Present it fairly, then address it.
7. State the overall conclusion with confidence level, key implications, and what evidence would change the conclusion.

### Full Version

**Step 1: Decompose the research question**

Break the main question into 2–5 sub-questions. Each sub-question should be independently answerable and collectively they should cover the main question without gaps or significant overlap.

Decision point: If you cannot decompose into at least 2 sub-questions, the research question may be too narrow for synthesis (a single source might answer it). If you generate more than 5, the research question is too broad — narrow it or split into multiple synthesis tasks.

Test: Would answering all sub-questions fully answer the main question? If no, you have a gap. If answering a sub-question requires answering another sub-question first, reorder or merge them.

**Step 2: Map sources to sub-questions**

Create a source-coverage matrix: rows are sub-questions, columns are sources. Mark each cell as: directly addresses / tangentially relevant / silent.

This reveals:
- **Coverage gaps:** Sub-questions with zero "directly addresses" sources need flagging. The synthesis must note the gap rather than speculating.
- **Source clustering:** If all sources address the same sub-question and ignore others, the synthesis will be lopsided. Note this.
- **Conflicts:** If two sources directly address the same sub-question with opposing conclusions, flag for Step 4.

**Step 3: Extract claims with evidence grading**

For each source, extract the specific claims relevant to each sub-question. For each claim, record:

- **The claim itself** — stated in one sentence.
- **Evidence type:**
  - *Empirical data:* Quantitative results from experiments, surveys, production metrics. Strongest evidence type.
  - *Case study:* Detailed account of one implementation or deployment. Moderate — shows feasibility but not generalizability.
  - *Expert opinion:* Stated by a credible practitioner or researcher without supporting data. Weakest standalone, but valuable when convergent with other evidence types.
  - *Logical argument:* Derived from first principles or structural analysis. Strength depends on the soundness of premises.
- **Evidence strength:** Strong (replicable, large-scale, peer-reviewed), Moderate (credible but limited scope or unverified), Weak (anecdotal, single-instance, or unverified).
- **Source verification:** Is the source URL/citation verified? If not, flag: `[SOURCE UNVERIFIED]`.

Decision point: If a claim has no evidence beyond assertion, classify it as "expert opinion — weak" and note the gap. Do not discard it — weak evidence is still evidence, but it must not be presented as strong.

**Step 4: Synthesize across sources per sub-question**

For each sub-question, compare the extracted claims across sources. Produce one of three assessments:

- **Convergent:** Multiple sources agree, with at least one providing strong evidence. State the converged position.
- **Divergent:** Sources disagree. State each position, the evidence behind it, and why the disagreement exists (different definitions, different contexts, different data, genuine uncertainty).
- **Insufficient:** Fewer than 2 sources address this sub-question, or all evidence is weak. State what is known, what is not, and what evidence would resolve the gap.

Edge case: If sources appear to agree but are all drawing from the same original data or the same author, note the dependency. Three sources citing one study is one data point, not three.

**Step 5: Grade confidence per sub-question**

Assign a confidence level to the synthesis position on each sub-question:

| Level | Criteria |
|-------|----------|
| **High** | ≥2 sources with strong evidence converge. No strong counter-evidence exists. The conclusion would survive a hostile review. |
| **Medium** | Evidence supports the position but with caveats: limited sources, moderate evidence strength, or context-dependent findings. A reasonable expert could disagree. |
| **Low** | Based on single source, weak evidence, or significant extrapolation. The position is defensible but fragile. |

Decision point: If all sub-questions are Low confidence, the synthesis should explicitly state that the research question cannot be answered with the available sources. This is a valid output — "we don't know yet" is better than a poorly supported conclusion.

**Step 6: Construct the counter-argument**

Identify the strongest case against your primary conclusion. This is not a token objection — it is the argument a smart, informed critic would make.

Rules:
- Present the counter-argument in its strongest form before addressing it. Do not straw-man.
- If the counter-argument has strong evidence, acknowledge the tension. "The counter-evidence is strong, but our conclusion holds because..." is more credible than pretending the counter-evidence doesn't exist.
- If the counter-argument is stronger than your conclusion, revise your conclusion. The synthesis follows the evidence, not the hypothesis.

**Step 7: State the overall conclusion**

Produce a structured conclusion:

- **Position:** One sentence stating the answer to the research question.
- **Confidence:** Overall confidence level (derived from sub-question confidence levels — the overall is at most as strong as the weakest critical sub-question).
- **Key evidence:** The 2–3 most important pieces of evidence supporting the position.
- **Key counter-evidence:** The strongest opposing evidence and how you addressed it.
- **Implications:** What follows if this conclusion is correct? What should the reader do differently?
- **Revision triggers:** What new evidence would change this conclusion? Be specific — "a large-scale study showing X" or "production data from Y" — not "more research."

## Evaluation Criteria

- [ ] The synthesis states a clear position on the research question — not a summary of "some say X, others say Y" without resolution.
- [ ] Every claim in the synthesis has an explicit evidence type (empirical data, case study, expert opinion, logical argument) and strength grade (strong, moderate, weak).
- [ ] Each sub-question carries a confidence level (high, medium, low) with criteria-based justification for the assigned level.
- [ ] Counter-evidence is presented in its strongest form and explicitly addressed — not omitted or straw-manned.
- [ ] Source coverage gaps are identified: any sub-question with insufficient evidence is flagged as such, not silently filled with speculation.
- [ ] No unverified source is presented as verified. All sources with unverified URLs/citations carry a visible flag.
- [ ] The conclusion includes specific revision triggers — concrete evidence that would change the position.
- [ ] The synthesis is usable without access to the original sources — a reader can understand the argument, evidence, and confidence from the synthesis alone.

## Failure Modes

**FM-1: The Literature Review**
*What it looks like:* The output summarizes each source sequentially ("Source A says X, Source B says Y, Source C says Z") without synthesizing across them. There is no convergent/divergent assessment, no confidence grading, and no position taken. The reader finishes knowing what each source says but not what to believe.
*Why it happens:* The author skipped Step 4 (synthesize across sources) and treated extraction as the endpoint. Summarization is easier than synthesis — it requires no judgment. The cure is Step 4's explicit convergent/divergent/insufficient framework, which forces a cross-source position.

**FM-2: The Confirmation Funnel**
*What it looks like:* The synthesis arrives at a confident conclusion, but all evidence points in one direction. Counter-evidence is absent or dismissed in one sentence. The output feels like advocacy, not analysis.
*Why it happens:* The author entered with a hypothesis and selected/weighted sources that confirmed it. Step 6 (counter-argument) was perfunctory or skipped. The fix is to write the counter-argument before writing the conclusion — if you can't steelman the opposition, you don't understand the question well enough.

**FM-3: Confidence Inflation**
*What it looks like:* Sub-questions are graded "high confidence" despite being supported by a single source, or by multiple sources citing the same original data. The synthesis sounds authoritative but collapses under scrutiny.
*Why it happens:* The author conflated number of sources with independence of evidence. Three blog posts citing the same arXiv paper are one data point, not three. The Step 4 edge-case check (are sources drawing from the same original?) exists to catch this, but it requires discipline to apply.

**FM-4: The Speculation Bridge**
*What it looks like:* The synthesis has strong evidence for sub-questions A and C but fills sub-question B with extrapolation presented at the same confidence level. The gap is invisible to the reader.
*Why it happens:* The author identified a coverage gap in Step 2 but didn't flag it in the output. Instead, they inferred an answer to the gap sub-question from adjacent evidence. This is legitimate at Low confidence with explicit flagging — but illegitimate when presented as Medium or High.

**FM-5: Missing Revision Triggers**
*What it looks like:* The conclusion states a position and confidence level but doesn't say what evidence would change it. The synthesis is a closed argument rather than an updatable position.
*Why it happens:* The author treated the synthesis as final rather than as a snapshot. Step 7 requires explicit revision triggers — "what would make me wrong?" — because a synthesis without update conditions decays silently as new evidence emerges.
