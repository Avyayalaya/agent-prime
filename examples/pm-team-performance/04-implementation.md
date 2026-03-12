# Implementation Plan: AI-Native PM Team

---

## Metadata

| Field | Value |
|-------|-------|
| **Objective** | Execute the Team Operating System design from 03-team-design.md |
| **Timeline** | 8 weeks (core), 3 months (full maturity) |
| **Team size** | 20 PMs, 1 VP sponsor, 1 PM lead as implementation owner |
| **Dependencies** | AI tool access approved, VP sponsorship confirmed |
| **Confidence** | HIGH on Phase 1-2, MED on Phase 3-4 (dependent on adoption velocity) |
| **Date** | 2026-03-12 |

---

## Phase 1: Set Up Shared Skills Library (Week 1)

**Owner:** PM Lead + 1 technical PM
**Objective:** Infrastructure operational. Skills installed. Knowledge base scaffolded.

### Deliverables

| # | Deliverable | Format | Path/Location | Done when |
|---|------------|--------|---------------|-----------|
| 1.1 | Skills Engine installed (6 plugins) | Claude plugins | `team-system/skills/` | All 12 skills callable from any PM workspace |
| 1.2 | Team Knowledge Base scaffolded | Directory structure + INDEX files | `team-knowledge/competitive/INDEX.md` | 4 empty indices with schemas |
| | | | `team-knowledge/research/INDEX.md` | |
| | | | `team-knowledge/decisions/INDEX.md` | |
| | | | `team-knowledge/metrics/INDEX.md` | |
| 1.3 | Seed artifacts (3-5 existing team analyses reformatted) | Markdown with evidence tiers | `team-knowledge/competitive/CA-001-*.md` | 3+ artifacts indexed and retrievable |
| 1.4 | PUBLISH gate checklist documented | Markdown | `team-system/gates/publish-checklist.md` | 5 gates defined with examples |
| 1.5 | Agent configurations (Scout, Synthesizer, Planner, Builder) | YAML/JSON config | `team-system/agents/` | 4 agents configured and tested |
| 1.6 | Tier assessment survey sent to all 20 PMs | Google Form or equivalent | Distributed via email | 20 responses collected, PMs assigned to tiers |

### Day-by-Day Schedule

| Day | Morning | Afternoon |
|-----|---------|-----------|
| Mon | Install Skills Engine, verify 6 plugins | Scaffold knowledge base directories |
| Tue | Reformat 3 existing artifacts to standard | Configure Scout and Synthesizer agents |
| Wed | Configure Planner and Builder agents | Write PUBLISH gate checklist |
| Thu | Send tier assessment, begin Tier 1 PM identification | Test full pipeline end-to-end (PM Lead runs it) |
| Fri | Fix issues from test run, document gotchas | Phase 1 complete. Knowledge base live with seed artifacts. |

### Exit Criteria
- [ ] All 12 skills installed and callable
- [ ] Knowledge base has 3+ seed artifacts correctly indexed
- [ ] PUBLISH gate checklist reviewed by VP
- [ ] Full pipeline tested end-to-end by PM Lead
- [ ] All 20 PMs tier-assigned

---

## Phase 2: Configure AI Agents for 5 Core PMs (Week 2-3)

**Owner:** PM Lead + Tier 1 PMs
**Objective:** First 5 PMs (Tier 1) fully operational. Producing real artifacts.

### Deliverables

| # | Deliverable | Format | Done when |
|---|------------|--------|-----------|
| 2.1 | 5 Tier 1 PM workspaces configured | Personal workspace directories | Each PM has context file, agent access, knowledge base connection |
| 2.2 | Onboarding walkthrough (90-min session per PM) | Live session + recording | Each PM completes 1 guided pipeline run |
| 2.3 | 5 "real" artifacts produced and PUBLISH-gated | Markdown in knowledge base | 5+ artifacts pass all 5 gates |
| 2.4 | Tier 2 prompt library created | Markdown files | `team-system/prompts/tier-2/` with 6 skill prompts |
| 2.5 | Tier 3 copy-paste prompt library created | Markdown files | `team-system/prompts/tier-3/` with 6 simplified prompts |
| 2.6 | Onboarding script for Tier 2/3 (automated workspace setup) | Shell script | `team-system/scripts/onboard.sh <username>` |

### Onboarding Protocol for Tier 1 PMs

Each Tier 1 PM gets a 90-minute onboarding session:

| Time | Activity |
|------|----------|
| 0-15 min | Context: why we're doing this, the skill stack inversion thesis, what success looks like |
| 15-30 min | Workspace tour: their personal config, how agents work, how the knowledge base connects |
| 30-60 min | Guided pipeline run: PM brings a real problem, we run Scout → Synthesizer together |
| 60-80 min | Independent run: PM completes Planner → Builder on their own |
| 80-90 min | PUBLISH walkthrough: how to submit artifacts, what the gates check, how to handle feedback |

### Week 2-3 Schedule

| Week | Focus | Milestone |
|------|-------|-----------|
| Week 2 | Onboard 5 Tier 1 PMs (1 per day) | All 5 operational, each produces 1 artifact |
| Week 3 | Tier 1 PMs produce real artifacts; prepare Tier 2/3 materials | Knowledge base reaches 10+ artifacts, prompt libraries ready |

### Exit Criteria
- [ ] 5 Tier 1 PMs have each produced ≥1 PUBLISH-gated artifact
- [ ] Knowledge base has 10+ artifacts
- [ ] Tier 2 and Tier 3 prompt libraries tested by 1 PM each
- [ ] Onboarding script tested and working
- [ ] First cross-reference observed (one artifact references another)

---

## Phase 3: First Team Knowledge Artifacts (Week 4-5)

**Owner:** All PMs + PM Lead oversight
**Objective:** Full team onboarded. Knowledge base compounding visible.

### Deliverables

| # | Deliverable | Format | Done when |
|---|------------|--------|-----------|
| 3.1 | 8-10 Tier 2 PMs onboarded | Copilot workspace | Each produces 1 artifact using skill prompts |
| 3.2 | 3-5 Tier 3 PMs onboarded | Web AI + prompt library | Each produces 1 framework-structured draft |
| 3.3 | Knowledge base reaches 25+ artifacts | Indexed in team-knowledge/ | Cross-reference rate ≥15% |
| 3.4 | First team retrospective conducted | Meeting + retro doc | 3+ action items identified and assigned |
| 3.5 | Quality gate calibration complete | Updated checklist | Gates adjusted based on first 25 artifacts |
| 3.6 | Leading indicators dashboard live | Spreadsheet or dashboard | Weekly tracking of 5 leading indicators |

### Tier 2 Onboarding (Pair Model)

Each Tier 2 PM is paired with a Tier 1 PM for 3 sessions:

| Session | Duration | Activity |
|---------|----------|----------|
| 1 | 60 min | Tier 1 PM demonstrates a full pipeline run. Tier 2 PM observes and asks questions. |
| 2 | 60 min | Tier 2 PM runs a skill prompt in Copilot. Tier 1 PM coaches in real-time. |
| 3 | 30 min | Tier 2 PM produces an artifact independently. Tier 1 PM reviews and provides PUBLISH feedback. |

### Tier 3 Onboarding (Workshop Model)

Single 90-minute workshop for all Tier 3 PMs together:

| Time | Activity |
|------|----------|
| 0-20 min | Context + demo: show a before/after (raw AI vs skill-structured output) |
| 20-50 min | Hands-on: each PM picks a prompt, pastes into web AI, produces a draft |
| 50-70 min | Review: PM Lead reviews 2-3 drafts live, shows what good looks like |
| 70-90 min | Q&A + assign Tier 1 reviewers for ongoing PUBLISH support |

### Exit Criteria
- [ ] All 20 PMs have produced ≥1 artifact
- [ ] Knowledge base has 25+ artifacts with ≥15% cross-reference rate
- [ ] Retrospective completed with documented action items
- [ ] Leading indicators dashboard shows positive trends on 4/5 metrics
- [ ] At least 1 Tier 3 PM has expressed interest in moving to Tier 2

---

## Phase 4: Measure and Iterate (Week 5-8)

**Owner:** VP + PM Lead
**Objective:** Demonstrate ROI. Optimize the system. Begin compounding at scale.

### Deliverables

| # | Deliverable | Format | Done when |
|---|------------|--------|-----------|
| 4.1 | Knowledge base reaches 60+ artifacts | Indexed in team-knowledge/ | Cross-reference rate ≥30% |
| 4.2 | Tier migration: ≥3 PMs moved up one tier | Tracked in adoption dashboard | 50% of Tier 3 PMs at Tier 2+  |
| 4.3 | Cycle time measurement: problem → spec | Before/after comparison | 25%+ reduction documented |
| 4.4 | PM satisfaction pulse survey | Survey results | ≥4.0/5 on "high-value work" question |
| 4.5 | ROI summary for VP | 2-page brief | Quantified: time saved, quality improved, coverage expanded |
| 4.6 | System optimization based on retrospective findings | Updated configs/gates/prompts | ≥3 specific improvements implemented |
| 4.7 | Second retrospective | Meeting + retro doc | Comparison to first retro, trend assessment |

### Week-by-Week Focus

| Week | Focus | Key question |
|------|-------|-------------|
| 5 | Measure cycle time reduction | Are we actually faster, or just busier? |
| 6 | Assess knowledge base quality | Are artifacts compounding, or just accumulating? |
| 7 | Evaluate tier migration velocity | Are PMs leveling up, or stuck at their starting tier? |
| 8 | Synthesize ROI case | Can we prove this is working with data? |

### The ROI Brief (Deliverable 4.5)

The VP needs a 2-page document to justify continued investment. Structure:

```
Page 1: Results
- Cycle time: X% reduction (before: Y days, after: Z days)
- Quality: Gate pass rate trend, retrospective quality scores
- Coverage: N artifacts in knowledge base, M cross-references
- Satisfaction: PM pulse survey results

Page 2: What's Next
- Month 3 targets (knowledge base at 100+, tier migration complete)
- Adjacent team expansion plan
- Resource ask (if any)
- Risk update
```

### Exit Criteria
- [ ] 60+ artifacts in knowledge base
- [ ] Cycle time reduction documented with before/after data
- [ ] ROI brief delivered to VP
- [ ] Second retrospective shows improvement over first
- [ ] At least 1 artifact cited by a team outside of Product

---

## Risk Register

| # | Risk | Likelihood | Impact | Mitigation | Contingency |
|---|------|-----------|--------|------------|-------------|
| R1 | **AI tool access blocked by IT** | MED | HIGH | Pre-approve Claude + Copilot in week 1. Get legal sign-off on data handling. | Fall back to Tier 3 (web AI) for all PMs. Slower but functional. |
| R2 | **Tier 1 PMs too busy to mentor** | HIGH | MED | Explicitly allocate 2 hrs/week for mentoring in their calendars. VP communicates this is priority. | Hire external consultant for 2-week onboarding sprint. |
| R3 | **Quality gates create bottleneck** | MED | MED | Distribute reviewing across 5 Tier 1 PMs (4 reviews each per week). Target 30-min review cycle. | Reduce to 3 gates (drop G1 and G5) temporarily. Add back when team is at scale. |
| R4 | **Knowledge base quality degrades** | MED | HIGH | Weekly index review by PM Lead. Quarterly prune of stale artifacts. Cross-reference rate as leading indicator. | Pause new entries. Spend 1 week cleaning and re-indexing existing artifacts. |
| R5 | **VP loses patience before lagging indicators appear** | LOW | HIGH | Show leading indicators weekly from week 2. Spec velocity and artifact count are visible immediately. | Produce 1 high-impact artifact (e.g., competitive war map VP has been wanting) as a quick win by week 2. |
| R6 | **PMs game the metrics (produce volume, not quality)** | LOW | MED | Anti-metrics tracked: artifacts without edits, volume without cross-references. Gates catch low-quality submissions. | Retrospective discussion. Adjust incentives from volume to quality (gate pass rate, cross-reference rate). |
| R7 | **Skill methodologies don't fit team's domain** | LOW | MED | Test with 2-3 real problems in Phase 1 before full rollout. | Customize 1-2 skills for team-specific frameworks. Budget 1 week of skill development. |

---

## Week 1 Checklist

The VP can hand this to the PM Lead tomorrow morning.

- [ ] Confirm AI tool access (Claude, Copilot) with IT — get written approval
- [ ] Identify 5 Tier 1 PMs (most technical, most senior, most enthusiastic — pick 2 of 3)
- [ ] Block 2 hours on PM Lead's calendar every day this week for setup
- [ ] Install Skills Engine (6 plugins) — follow `team-system/setup.md`
- [ ] Create `team-knowledge/` directory with 4 index subdirectories
- [ ] Reformat 3 existing team artifacts to skill standard (evidence tiers, assumption registry)
- [ ] Write PUBLISH gate checklist (use template from `team-system/gates/`)
- [ ] Configure 4 agents (Scout, Synthesizer, Planner, Builder) — test each one
- [ ] Run 1 complete pipeline end-to-end (PM Lead as guinea pig)
- [ ] Send tier assessment survey to all 20 PMs (due by Friday)
- [ ] Schedule Tier 1 onboarding sessions for week 2 (90 min each, 1 per day)
- [ ] Send team-wide email: "Here's what we're doing and why" (use the thesis from 02-synthesis.md as the narrative)

**Time investment for PM Lead in week 1:** ~20 hours
**Time investment for VP in week 1:** ~3 hours (review gate checklist, approve tool access, send team email)

---

## Success Criteria Summary

| Timeframe | Metric | Target |
|-----------|--------|--------|
| Week 1 | Infrastructure live, 5 Tier 1 PMs identified | All setup deliverables complete |
| Week 3 | First 10 artifacts in knowledge base | Cross-reference rate >0% |
| Week 5 | All 20 PMs onboarded, 25+ artifacts | Cross-reference rate ≥15% |
| Week 8 | 60+ artifacts, cycle time measured | 25%+ reduction documented |
| Month 3 | 100+ artifacts, tier migration ≥80% at Tier 2+ | ROI brief with quantified results |
| Month 6 | 200+ artifacts, adjacent teams onboarded | PM team recognized as best analytical team in the company |
