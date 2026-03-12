# Excavation: Metric Design & Experimentation (Skill #2)

> **Date:** 2026-02-18
> **Purpose:** Framework research pass before building SKILL.md
> **Method:** PLN-007 spec review + web research + competitive gap analysis + unaided/practitioner test filtering

---

## 1. Competitive Gap Analysis

### What Dean Peters Has (Metrics Space)

| Skill | Type | What It Does |
|-------|------|-------------|
| `finance-metrics-quickref` | Component | Lookup table for 32+ SaaS finance metrics |
| `saas-revenue-growth-metrics` | Component | Revenue, ARPU, MRR/ARR, churn, NRR formulas and definitions |
| `saas-economics-efficiency-metrics` | Component | CAC, LTV, margins, burn rate formulas |
| `business-health-diagnostic` | Interactive | SaaS health scorecard — asks for metrics, produces diagnostic |

### What Dean Does NOT Have

| Domain | Gap |
|--------|-----|
| Metric hierarchy design | No North Star → L1 → L2 → input metric architecture |
| Experiment design | No A/B testing methodology, switchback, quasi-experimental |
| Statistical validity | No significance thresholds, sample size estimation, power analysis |
| Counter-metric design | No Goodhart's Law detection, guardrail metric methodology |
| Metric decomposition trees | No systematic approach to decomposing outcomes into levers |
| Leading vs. lagging design | No taxonomy, no methodology for identifying leading indicators |
| Metric failure modes | No vanity metric detection, proxy divergence, Simpson's paradox, peeking |
| Retention cohort methodology | Basic cohort tables but no analysis methodology |

**Verdict:** Dean's metrics skills are **SaaS accounting references** — what to measure and how to calculate it. Our skill is **metric engineering** — how to design metric systems that resist gaming, detect problems early, and validate causally. Non-overlapping. Greenfield advantage confirmed.

---

## 2. Framework Inventory (Unaided + Practitioner Tests)

### A. Metric Hierarchy Design

| Framework | Source | Unaided Test | Practitioner Test |
|-----------|--------|--------------|-------------------|
| **North Star Framework** | Amplitude / Sean Ellis | ✅ Most PMs can't articulate NSM with proper input metrics | ✅ Every growth consultant uses this |
| **Metric Decomposition Tree** | Mixpanel / Reforge | ✅ PMs rarely decompose beyond one level | ✅ Standard at Amplitude, Stripe, Airbnb |
| **GSM (Goals-Signals-Metrics)** | Google | ✅ Signal-to-metric mapping is the hard part most skip | ✅ Used at Google, Spotify |
| **AARRR (Pirate Metrics)** | Dave McClure | ⚠️ Most PMs know this already | ✅ Standard for startups |
| **HEART Framework** | Google (Kerry Rodden) | ⚠️ Known but poorly applied | ✅ Google standard for UX metrics |

**Decision:** Encode NSM + Decomposition Tree + GSM as primary frameworks with scoring rubrics and design worksheets. AARRR and HEART as secondary reference — show correct application, not just listing.

**Original synthesis to build:**
- **NSM Selection Rubric** — Scoring: reflects value delivery (not vanity), is leading (not lagging), is influenceable, is simple to understand
- **Metric-to-Team Ownership Mapping** — Exec owns NSM, PM owns L1, feature team owns L2/input
- **Metric Hierarchy Design Worksheet** — Define value moment → identify NSM → decompose L1 → decompose L2 → assign ownership → set cadence

### B. Leading vs. Lagging Indicator Design

| Framework | Unaided Test | Practitioner Test |
|-----------|--------------|-------------------|
| **Leading/Lagging Taxonomy** with temporal classification | ✅ PMs confuse these constantly | ✅ Standard in growth teams |
| **Activation Metric Design** ("aha moment" identification) | ✅ Facebook's "7 friends in 10 days" — methodology is opaque to most | ✅ Core growth practice |
| **Temporal Lag Classification** — Immediate / Short / Medium / Long / Structural | ✅ PMs don't think about lag timing | ✅ Determines monitoring cadence |

**Original synthesis to build:**
- **Leading Indicator Discovery Protocol** — Define lagging outcome → list early behaviors → correlate → identify top 3 predictive → set thresholds → build activation metric
- **Lag-to-Cadence Matrix** — Immediate metrics = real-time alerts, Short = daily, Medium = weekly, Long = monthly, Structural = quarterly

### C. Counter-Metric Design / Goodhart's Law

| Framework | Unaided Test | Practitioner Test |
|-----------|--------------|-------------------|
| **Goodhart's Law Taxonomy** — 4 variants: Regressional, Extremal, Causal, Adversarial (Manheim & Garrabrant) | ✅ Most PMs know the quote, not the mechanism types | ✅ Serious metric designers use this |
| **Counter-Metric Pairing** | ✅ PMs rarely design counter-metrics proactively | ✅ Standard at Netflix, Amazon |
| **Guardrail Metric Protocol** | ✅ PMs celebrate primary wins that damage guardrails | ✅ Every serious experimentation platform |
| **Metric Gaming Detection Patterns** | ✅ Sudden spikes, reporting-cycle behavior, incongruent movements | ✅ Used in incentive design |

**Original synthesis to build:**
- **Goodhart Vulnerability Assessment** — For each metric type (engagement, revenue, conversion, retention), list top 3 gaming behaviors and counter-metric
- **Counter-Metric Pairing Template** — Primary → What could go wrong → Counter-metric → Threshold
- **Quarterly Metric Health Review Protocol** — Is metric still measuring what we think? Has proxy diverged? Decision: keep / recalibrate / replace

### D. Experiment Design

| Framework | Unaided Test | Practitioner Test |
|-----------|--------------|-------------------|
| **A/B Test Design Protocol** | ✅ Most PMs run underpowered tests or peek at results | ✅ Standard |
| **Switchback Experiments** | ✅ Most PMs don't know this exists | ✅ Uber, Lyft, DoorDash for marketplace |
| **Quasi-Experimental Methods** (diff-in-diff, propensity matching) | ✅ PMs can't do causal inference without randomization | ✅ Used when RCTs impossible |
| **Sequential Testing** | ✅ Peeking problem is endemic | ✅ Optimizely, Eppo standard |
| **Multi-Armed Bandit** | ⚠️ Engineers know this | ✅ Dynamic allocation |

**Original synthesis to build:**
- **Experiment Type Decision Table** — Can randomize users? → A/B. Marketplace effects? → Switchback. Can't randomize? → Quasi-experimental. Need early stopping? → Sequential. Not enough traffic? → Alternatives section.
- **When NOT to Experiment Checklist** — Ethical, insufficient traffic, irreversible, legal, spillover
- **Experiment Quality Rubric** — Pre-registration, primary metric declared, secondary declared, guardrails set, duration committed, sample size committed

### E. Statistical Validity for PMs

| Concept | Unaided Test | What to Encode |
|---------|--------------|----------------|
| **Significance (α)** | ✅ PMs use p<0.05 without understanding it | Plain-English: "probability your result is a fluke" |
| **Power (1-β)** | ✅ PMs ignore power entirely | "Probability you'd catch a real effect if it exists" |
| **MDE** | ✅ PMs don't know to decide this BEFORE the test | "Smallest effect worth detecting — a business decision" |
| **Confidence Intervals** | ✅ PMs report p-values, not CIs | "The range where the true effect probably lives" |
| **Multiple Testing Correction** | ✅ PMs test 10 metrics, call the significant one a win | Bonferroni correction, confirmatory vs. exploratory |
| **Sample Size Estimation** | ✅ PMs guess duration | Formula in plain English + computation script |

**Critical design note:** This section must be plain-English analogies, not formulas. If it reads like a stats textbook, it failed. The scripts handle the math.

### F. Retention Cohort Methodology

| Framework | Unaided Test |
|-----------|--------------|
| **Cohort Construction Types** — Time-based, behavior-based, acquisition-channel | ✅ Most PMs only do time-based |
| **Retention Curve Analysis** — Flattening point, smile vs. frown patterns | ✅ PMs see tables, not curves |
| **Cohort Degradation Detection** — Newer cohorts worse = PMF erosion | ✅ Hidden in blended metrics |
| **Revenue vs. Logo Retention** | ✅ Most PMs miss this split |

---

## 3. Named Failure Modes (10)

| # | Name | Pattern | Detection |
|---|------|---------|-----------|
| FM-1 | **The Vanity Trap** | Metric looks impressive but doesn't drive decisions | "If this moved 20%, what would we DO?" No answer → vanity |
| FM-2 | **The Proxy Divergence** | Proxy decouples from the outcome it represents | Quarterly: correlate proxy with true outcome. r < 0.5 → diverged |
| FM-3 | **Simpson's Paradox** | Aggregate hides segment-level reversals | Always segment results by key dimensions before declaring winner |
| FM-4 | **The Peeking Problem** | Checking results before sufficient sample → inflated false positives | Pre-commit to N and duration. Use sequential testing for early stopping |
| FM-5 | **Survivorship Bias** | Analyzing only retained users inflates engagement | Include churned users. Study exit points |
| FM-6 | **The Goodhart Spiral** | Metric → target → optimize → meaning lost → new metric → repeat | Counter-metrics. Quarterly health review. Rotate metrics |
| FM-7 | **The Lagging Indicator Trap** | Only measuring outcomes → problems detected too late | For every lagging metric, identify 2-3 leading indicators |
| FM-8 | **The Denominator Shift** | Rate improves because denominator changed, not numerator | Track absolutes alongside rates. Decompose rate changes |
| FM-9 | **The Multiple Testing Trap** | Test 10 metrics, report significant one → 50% false positive chance | Pre-declare primary. Bonferroni for secondaries |
| FM-10 | **The Instrumentation Gap** | Design metrics you can't actually measure | Before committing: verify data exists, is clean, is timely, has history |

---

## 4. Output Artifact: Measurement Framework Document

The skill produces a complete Measurement Framework containing:

1. **Metric Hierarchy** — North Star → L1 → L2 → input metrics → team ownership
2. **Leading Indicator Set** — 3-5 leading indicators per lagging outcome with temporal classification
3. **Counter-Metric Pairs** — Every primary metric paired with counter-metric and threshold
4. **Experiment Plan** — Top 2-3 hypotheses: type, sample size, duration, primary metric, guardrails
5. **Retention Cohort Template** — Construction, cadence, degradation thresholds
6. **Metric Health Review Schedule** — Quarterly protocol with proxy validation

---

## 5. Scripts (HIGH computation value)

| Script | Input | Output |
|--------|-------|--------|
| `sample_size_calculator.py` | Baseline rate, MDE, α, β | Required N, estimated duration given daily traffic |
| `significance_test.py` | Control/treatment counts + conversions | p-value, CI, effect size, achieved power |
| `retention_cohort.py` | CSV (user_id, signup_date, activity_dates) | Cohort table, retention curves, degradation flag |
| `metric_decomposition.py` | Before/after numerator and denominator | Rate change attribution (how much from numerator vs. denominator) |

---

## 6. Quality Gradients

| Tier | Output |
|------|--------|
| **Intern** | Single NSM identified. Basic A/B test plan with primary metric. No counter-metrics. No leading indicators. |
| **Consultant** | Full hierarchy (NSM + L1 + L2). Leading/lagging pairs. Counter-metrics for top 3. Experiment plan with sample size. Basic cohort analysis. |
| **Elite** | Complete measurement framework: hierarchy + ownership map, temporal lag classification, Goodhart vulnerability assessment, experiment decision table, statistical validity justification, retention cohort methodology, quarterly review protocol. Every metric has a counter-metric. Every experiment has guardrails. |

---

## 7. Epistemic Check

1. **Statistical validity risks being too academic.** PMs need plain-English, not formulas. Scripts handle math. Section must explain in analogies.

2. **Are all 10 failure modes genuinely distinct?** FM-2 (Proxy Divergence) and FM-6 (Goodhart Spiral) are related. Test: can a PM read each and recognize a time they made that mistake? If not, merge or cut.

3. **Experiment design may be too ambitious.** Switchback and quasi-experimental are real but rare for most PMs. Make A/B primary, advanced methods as "when A/B won't work" alternatives.

4. **Retention cohort section must go deeper than Dean's.** His has basic tables. Ours needs behavior-based cohorts, degradation detection, revenue vs. logo split — or it's not a knowledge weapon.

---

## 8. Build Readiness Assessment

| Criterion | Status |
|-----------|--------|
| Frameworks identified | ✅ 10+ pass unaided/practitioner tests |
| Competitive gap confirmed | ✅ Zero overlap with Dean Peters |
| Failure modes named | ✅ 10 distinct patterns |
| Output artifact defined | ✅ Measurement Framework (6 components) |
| Scripts scoped | ✅ 4 computation helpers |
| Quality gradients defined | ✅ 3 tiers |
| Epistemic risks identified | ✅ 4 tensions named |

**Ready for SKILL.md build.**

---

*Excavated: 2026-02-18 | Planner research pass for Skill #2*
