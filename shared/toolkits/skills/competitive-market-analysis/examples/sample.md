# Worked Example: AI Note-Taking App Market — Competitive & Market Analysis

> **Context:** A PM at a mid-stage startup building an AI-powered note-taking app needs to understand the competitive landscape before deciding their positioning strategy. They have 3 known competitors and want to understand where structural advantages lie.

---

## Input

**Product:** NoteAI — AI-powered note-taking app with meeting transcription, action item extraction, and knowledge graph features  
**Target Market:** Knowledge workers in tech companies (50-5000 employees)  
**Known Competitors:** Notion AI, Mem, Reflect  
**Key Question:** Where do we have a structural right to win, and what's the most defensible positioning?

---

## Output (Elite Tier)

### Executive Summary

NoteAI faces a structurally asymmetric competitive landscape where the dominant threat isn't feature parity from direct competitors — it's Notion AI's aggregation of the user relationship through its existing workflow embedding. The knowledge graph differentiator has a 12-18 month window before commoditization. The defensible position is **enterprise meeting intelligence** (not general note-taking), where switching costs compound through organizational data accumulation and Notion AI's horizontal architecture creates a counter-positioning opportunity.

### 1. Competitive Set

| Tier | Competitor | Rationale |
|------|-----------|-----------|
| **Primary** | Notion AI | Direct substitute, dominant workflow tool, adding AI features aggressively |
| **Primary** | Mem | AI-native note-taking, knowledge graph, same target segment |
| **Primary** | Reflect | AI note-taking focused on networked thought, privacy-first |
| **Secondary** | Microsoft Copilot (OneNote) | Adjacent — expanding from enterprise productivity into meeting intelligence |
| **Secondary** | Otter.ai | Adjacent — expanding from transcription into knowledge management |
| **Secondary** | Obsidian + AI plugins | Adjacent — open-source with growing AI plugin ecosystem |
| **Non-obvious** | LLM-native interfaces | Paradigm — ChatGPT/Claude as the "note-taking" surface (users dump context into chat instead of structured notes) |

### 2. 7 Powers Heat Map

| Power | Notion AI | Mem | Reflect | NoteAI (Ours) |
|-------|:---:|:---:|:---:|:---:|
| Scale Economies | 🟢 Strong ↑ | 🔴 Weak → | 🔴 Weak → | 🔴 Weak → |
| Network Effects | 🟢 Collab NE ↑ | 🟡 Data NE → | 🔴 None | 🟡 Org NE (nascent) |
| Counter-Positioning | 🔴 None | 🟡 AI-native vs. legacy | 🟡 Privacy vs. cloud | 🟢 Meeting intelligence vs. horizontal |
| Switching Costs | 🟢 Workflow ↑ | 🟡 Data → | 🟡 Data → | 🟡 Org data (growing) |
| Branding | 🟢 Premium → | 🟡 Niche → | 🟡 Niche → | 🔴 Unknown |
| Cornered Resource | 🟡 User base | 🟡 AI talent | 🔴 None | 🟡 Meeting corpus |
| Process Power | 🟡 Moderate | 🔴 None | 🔴 None | 🔴 None |

**Moat Durability Index:**

| Competitor | MDI | Rating |
|-----------|:---:|--------|
| Notion AI | 68.2/100 | 🟡 Moderate (accruing toward durable) |
| Mem | 28.5/100 | 🔴 Fragile |
| Reflect | 22.1/100 | 🔴 Fragile |
| NoteAI | 31.7/100 | 🔴 Fragile (but counter-positioning accruing) |

**So What:** Notion AI is the only player with a meaningful moat, and it's strengthening. Mem and Reflect are structurally vulnerable — they could be acquired or out-competed without Notion even trying. Our counter-positioning (meeting intelligence vs. horizontal notes) is our ONLY structural advantage. If we compete on general note-taking, we lose. If we own meeting intelligence for teams, we build switching costs Notion can't match without restructuring their product.

### 3. Switching Cost Decomposition

| Cost Type | Notion AI | Mem | Reflect | NoteAI |
|-----------|:---:|:---:|:---:|:---:|
| Financial/Contractual | █████░░░░░ 5/10 | ██░░░░░░░░ 2/10 | ██░░░░░░░░ 2/10 | ███░░░░░░░ 3/10 |
| Data/Migration | ████████░░ 8/10 | █████░░░░░ 5/10 | ████░░░░░░ 4/10 | ██████░░░░ 6/10 |
| Workflow/Integration | █████████░ 9/10 | ███░░░░░░░ 3/10 | ██░░░░░░░░ 2/10 | ███████░░░ 7/10 |
| Identity | ██████░░░░ 6/10 | ████░░░░░░ 4/10 | █████░░░░░ 5/10 | ██░░░░░░░░ 2/10 |
| Learning/Procedural | ███████░░░ 7/10 | ████░░░░░░ 4/10 | ███░░░░░░░ 3/10 | ████░░░░░░ 4/10 |
| Relational/Trust | ████████░░ 8/10 | ███░░░░░░░ 3/10 | ███░░░░░░░ 3/10 | █████░░░░░ 5/10 |

**Key insight:** Notion's highest switching costs are customer-CREATED (workflow embedding, data accumulation, relational) — these compound with usage and are extremely durable. Our path to comparable switching costs is through ORGANIZATIONAL data accumulation: meeting transcripts, action items, decision logs that become the team's institutional memory. Individual note-taking switching costs are weak. Team-level knowledge switching costs are very high.

### 4. Aggregation Theory Assessment

| Question | Assessment |
|----------|-----------|
| Who owns the user relationship? | **Notion** — daily active habit, workspace is home base |
| Marginal costs near zero? | All players — cloud AI costs declining, but Notion has scale advantage |
| Acquisition costs decreasing? | **Notion** — viral within teams (direct NE). Mem/Reflect/NoteAI pay for every user |
| Supplier multi-homing? | N/A (not a marketplace model) |
| Commoditization risk? | **High** — AI note features becoming table stakes. LLM providers commoditize the AI layer |

**Value Chain COAP Analysis:**
```
[LLM/AI models] → [Note-taking app] → [Workflow integration] → [User relationship]
     ↓                                        ↑                        ↑
  Commoditizing                         Integrating              Where value accrues
```

Profits are shifting FROM the AI model layer (commodity) TOWARD workflow integration and user relationship ownership. Building a better AI note feature is building on the commoditizing layer. Building deeper workflow integration is building on the value-accruing layer.

### 5. Disruption Vector Analysis

| Vector | Applicable? | Assessment |
|--------|:-----------:|-----------|
| Low-end | 🔴 No | Note-taking isn't over-served — users want MORE features, not fewer |
| New-market | 🟢 Yes | Meeting participants who never took structured notes → NoteAI transcribes automatically |
| COAP | 🟢 Yes | AI models commoditizing → value shifts to integration layer → build there |

**NoteAI's disruption opportunity:** New-market disruption. Target meeting participants who DON'T take notes today (non-consumers). Automatic transcription + AI extraction means zero effort → massive expansion of who "takes notes." Notion AI can't match this without breaking their editor-first UX.

### 6. Strategic Recommendations

| # | Recommendation | Confidence | Watch Indicator |
|---|---------------|:----------:|-----------------|
| 1 | **Position as "Meeting Intelligence for Teams" not "AI Note-Taking"** | 85% | If Notion ships dedicated meeting features in next 6 months, confidence drops to 50% |
| 2 | **Build organizational switching costs** — make team meeting history the moat | 90% | Monthly active teams (not users) as north star |
| 3 | **Don't compete on editor quality** — Notion's 5-year head start on editor UX is insurmountable | 95% | If editor complaints appear in churn surveys, minimal investment only |
| 4 | **Integrate INTO Notion, don't compete against it** — be the meeting intelligence layer that Notion users add | 70% | Integration install rate vs. standalone adoption rate |
| 5 | **Ship action item → task sync before knowledge graph** — workflow embedding builds switching costs faster than knowledge features | 80% | Action item completion rate, task sync DAU |

**Counterfactual:** If we're wrong about meeting intelligence positioning and Notion ships native meeting features → our fallback is the knowledge graph as differentiator, but that's a weaker moat (12-18 month commoditization window). The leading indicator is Notion's job postings for meeting/audio engineering roles.

---

## Why This Works

This analysis applies the full Application Method from the skill:

1. **Competitive set defined** across 3 tiers (Step 1) — including the non-obvious LLM threat
2. **7 Powers scored** with evidence and trajectory indicators (Step 2) — reveals Notion is the only durable player
3. **Switching costs decomposed** by type (Step 3) — shows organizational data is the path to moat, not individual notes
4. **Aggregation + COAP applied** (Step 4) — identifies that building on the AI layer is building on sand; workflow integration is where value accrues
5. **Disruption vectors assessed** (Step 5) — identifies new-market disruption as the opportunity
6. **Tactical layer built** with feature matrix context (Step 6)
7. **Every insight cascaded to "So What"** with confidence levels and watch indicators (Step 7)

**Unaided test passed:** Without this skill, a PM would list competitors and compare features. WITH the skill, the analysis reveals that: (a) counter-positioning is the only structural advantage, (b) organizational data accumulation is the moat strategy, (c) integrating into Notion beats competing against it, and (d) the LLM commoditization trend means the AI layer isn't defensible. These insights require the encoded frameworks — they don't emerge from raw prompting.

**Practitioner test passed:** A $500/hr strategy consultant would use 7 Powers, Aggregation Theory, and COAP in exactly this way. The switching cost decomposition and moat durability scoring add rigor that even most consultants skip.

---

*Generated using Competitive & Market Analysis skill v1.0 | PM Skills Arsenal*
