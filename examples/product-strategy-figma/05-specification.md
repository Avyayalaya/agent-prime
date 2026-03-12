# Figma AI — Intelligent Design Assistant: Product Specification

---

## How to Read This Document

| Time Available | Read These Sections |
|---|---|
| **5 minutes** | Executive Summary, Success Metrics |
| **15 minutes** | Add Scope Boundary Table, User Stories (skim ACs) |
| **30 minutes** | Full document |

| Your Role | Start Here |
|---|---|
| **Engineer** | User Stories & Acceptance Criteria, then Technical & Design Context |
| **QA** | Acceptance Criteria (edge case + error categories), then Failure Conditions |
| **Designer** | Executive Summary, then User Stories for flow context |
| **Stakeholder / Leadership** | Executive Summary and Success Metrics only |

### Notation Key

- **Must / Should / Nice** — MoSCoW priority for acceptance criteria. Must = launch blocker. Should = expected at launch but shippable without. Nice = future iteration candidate.
- **H / M / L** — Confidence level. H = multiple data points or validated assumption. M = single credible source or strong inference. L = directional estimate, requires validation.
- **[EVIDENCE-LIMITED]** — Claim based on public data or inference; internal telemetry would improve confidence.
- **Given / When / Then** — Structured acceptance criteria format. Given = precondition. When = user action. Then = expected system behavior.

---

## Metadata

- **spec_id:** SPEC-FIGMA-AI-001
- **feature:** Figma AI — Intelligent Design Assistant
- **author:** PM Lead, Figma Design Platform
- **spec_date:** 2026-03-12
- **status:** Draft for Engineering Review
- **upstream_artifacts:** 01-competitive-analysis.md (Figma vs Canva vs Adobe Express), 03-problem-framing.md (Figma growth plateau diagnosis), 04-discovery-research.md (designer workflow friction study)
- **target_release:** H2 2026 (phased: Alpha Q3, Beta Q4, GA Q1 2027)

---

## Context Fitness Check

| Question | Answer |
|---|---|
| Is the problem well-enough understood to specify a solution? | **Yes.** Upstream problem framing (03) identified the core tension: Figma's power-user moat is also its adoption ceiling. Canva's AI tools are converting non-designers into "good enough" producers, pulling budget and headcount from Figma's growth path. Discovery research (04) confirmed that even existing Figma users spend 40-60% of their time on production tasks (resizing, layout adjustment, asset generation) rather than creative decisions. |
| Is this net-new, iteration, or migration? | **Net-new capability** embedded into existing product surfaces. Not a standalone product — AI features integrate into the canvas, component library, and prototyping workflows. |
| Are success metrics defined? | **Yes.** Derived from competitive analysis (01) and problem framing (03). Primary metric: design velocity for non-expert users. Secondary: retention of professional users who face production bottleneck. |

---

## Executive Summary

Figma AI embeds an intelligent design assistant directly into the Figma editor. It does three things: generates design elements from natural language prompts (text-to-design), automates repetitive production tasks (layout adjustment, responsive resizing, asset variant generation), and provides contextual design suggestions based on the user's existing design system and component library.

This is not "AI for AI's sake." The upstream competitive analysis identified a specific strategic threat: Canva's AI-powered tools have reduced the time-to-first-deliverable for non-designers from hours to minutes, pulling marketing teams, product managers, and startup founders away from Figma entirely. Meanwhile, professional designers — Figma's core users — report spending 40-60% of their time on production work that AI could automate [EVIDENCE-LIMITED — based on discovery interviews, n=47].

The business outcome: increase design velocity by 3x for non-expert users (closing the Canva gap) while reducing production time by 50% for professional designers (deepening the moat). If successful, this drives two metrics that matter: (1) expansion revenue from non-designer seats adopting Figma instead of Canva, and (2) reduced churn among professional teams frustrated by production overhead.

The spec covers Phase 1 only: text-to-design generation, auto-layout assistance, and design system-aware suggestions. Image generation (competing with Adobe Firefly), full prototyping automation, and code generation are explicitly deferred.

---

## Success Metrics

### Primary Outcome Metric

| Metric | Baseline (Current) | Target (6 months post-GA) | Confidence |
|---|---|---|---|
| **Design velocity for non-expert users** (time from blank canvas to shippable deliverable) | ~4.2 hours median [EVIDENCE-LIMITED] | ~1.4 hours median (3x improvement) | M — baseline from discovery research (n=47), target benchmarked against Canva's reported 45-min median for comparable deliverables |

### Secondary Metrics

| Metric | Baseline | Target | Confidence |
|---|---|---|---|
| Professional designer production time (resize, variant, layout tasks) | ~2.1 hours/day median | ~1.0 hour/day median (50% reduction) | M |
| Non-designer seat expansion rate (teams adding non-design roles to Figma) | 12% QoQ | 25% QoQ | L — depends on pricing/packaging decisions outside this spec |
| Professional team churn (annual) | 8.2% | 6.0% | M |
| AI feature adoption (MAU using any AI feature / total MAU) | 0% (not shipped) | 40% at 6 months post-GA | M — benchmarked against Canva Magic Design adoption (~35% within 6 months) |

### Leading Indicators (1-2 weeks post-launch)

1. **AI feature trial rate:** % of active users who invoke any AI feature at least once. Target: >20% in first 2 weeks.
2. **Generation acceptance rate:** % of AI-generated outputs that users keep (vs. undo/delete within 30 seconds). Target: >45%.
3. **Repeat usage:** % of first-time AI users who use an AI feature again within 7 days. Target: >55%.
4. **Error/frustration signal:** % of AI invocations followed by Cmd+Z within 5 seconds. Target: <25%.

---

## User Stories & Acceptance Criteria

### US-1: Text-to-Design Generation

**As a** product manager with limited design skills, **I want to** describe a UI component or layout in natural language and have Figma generate it on the canvas, **so that** I can create high-fidelity mockups without waiting for a designer.

#### Functional (Must-Have)

- **AC-1.1:** Given the user types a natural language prompt in the AI command bar (e.g., "Create a pricing page with three tiers: Free, Pro, Enterprise"), When the user submits the prompt, Then Figma generates a design on the canvas within 8 seconds that includes the described elements, using the active file's design system tokens (colors, typography, spacing) if a design system is linked.
- **AC-1.2:** Given the AI generates a design, When the user inspects the generated elements, Then every element is a properly structured Figma layer (not a flattened image) — editable text is text layers, shapes are vector layers, spacing uses auto-layout where appropriate.
- **AC-1.3:** Given the user has a linked design system / component library, When the AI generates a design, Then it uses existing components from the library (e.g., button components, card components) rather than creating new ad-hoc elements. If no matching component exists, it creates new layers following the design system's token values.

#### Functional (Should-Have)

- **AC-1.4:** Given the user submits a prompt, When the AI generates a design, Then the user can see 3 variations and select one (or regenerate). Each variation should represent a meaningfully different layout approach, not minor color/spacing tweaks.
- **AC-1.5:** Given the user selects a generated design, When they want to refine it, Then the user can provide follow-up natural language instructions (e.g., "Make the CTA buttons larger and change the Enterprise tier color to blue") and the AI modifies the existing design rather than generating from scratch.

#### Non-Functional (Must-Have)

- **AC-1.6:** Generation latency must be under 8 seconds (P50) and under 15 seconds (P95) for single-component prompts. Multi-component layouts (e.g., full page) must complete under 20 seconds (P50).
- **AC-1.7:** The feature must be accessible via keyboard navigation. The AI command bar must be invocable via keyboard shortcut (default: Cmd+K, then "AI" prefix or dedicated Cmd+Shift+A).
- **AC-1.8:** Generated designs must meet WCAG 2.1 AA contrast ratios by default. If the linked design system has tokens that violate AA, the AI should flag it with a tooltip warning but respect the design system's values.

#### Edge Cases (Must-Have)

- **AC-1.9:** Given the user submits a prompt in a language other than English, When the AI processes it, Then it should generate the design with UI text in the prompt's language (not translate to English). Supported languages at launch: English, Spanish, French, German, Japanese, Korean, Portuguese, Chinese (Simplified).
- **AC-1.10:** Given the user submits an ambiguous or contradictory prompt (e.g., "Create a minimalist page with lots of decorative elements"), When the AI processes it, Then it should generate its best interpretation and surface a clarification prompt: "I interpreted 'minimalist with decorative elements' as [interpretation]. Would you like to adjust?"
- **AC-1.11:** Given the file has no linked design system, When the AI generates a design, Then it uses Figma's default design tokens (system font, neutral palette) and surfaces a suggestion: "Link a design system for brand-consistent results."

#### Error Handling (Must-Have)

- **AC-1.12:** Given the AI service is unavailable or times out, When the user submits a prompt, Then show an inline error message: "AI generation is temporarily unavailable. Your prompt has been saved — try again in a moment." Do not lose the user's prompt text.
- **AC-1.13:** Given the user submits a prompt that violates content policy (e.g., generates deceptive UI patterns), When the AI detects it, Then refuse generation with a specific explanation: "This request was flagged because [reason]. Figma AI does not generate [category]." Do not generate a partial result.

---

### US-2: Auto-Layout and Responsive Resize Assistant

**As a** professional designer, **I want to** select a group of elements and have Figma automatically apply proper auto-layout and responsive constraints, **so that** I can eliminate the repetitive manual work of setting up responsive behavior.

#### Functional (Must-Have)

- **AC-2.1:** Given the user selects a frame or group of elements, When they invoke "AI Auto-Layout" (via right-click menu or command bar), Then Figma analyzes the spatial relationships and applies auto-layout with appropriate direction (horizontal/vertical), spacing, padding, and alignment. The result should match what an experienced designer would configure manually in >80% of cases.
- **AC-2.2:** Given the user invokes AI Auto-Layout on a frame, When the AI applies layout, Then the user sees a before/after preview with the option to accept, reject, or modify. Rejecting restores the exact previous state (full undo).
- **AC-2.3:** Given a frame with auto-layout applied, When the user invokes "AI Responsive Resize," Then the AI generates responsive variants at standard breakpoints (mobile 375px, tablet 768px, desktop 1440px) as separate frames, preserving content hierarchy and design system tokens.

#### Functional (Should-Have)

- **AC-2.4:** Given the user accepts an AI auto-layout suggestion, When they later manually adjust spacing or alignment, Then the AI learns from the correction and applies that preference to future suggestions in the same file (session-level learning, not persistent across files in Phase 1).

#### Non-Functional (Must-Have)

- **AC-2.5:** Auto-layout analysis and application must complete in under 3 seconds for frames with fewer than 200 layers. For frames with 200-1000 layers, under 10 seconds.
- **AC-2.6:** AI auto-layout must not modify layers outside the selected frame. If the selected frame is nested, parent frame constraints must be preserved.

#### Edge Cases (Must-Have)

- **AC-2.7:** Given the user selects a frame containing absolutely-positioned overlapping elements (e.g., a badge on a card corner), When AI Auto-Layout is invoked, Then the AI should preserve absolute positioning for overlapping elements and apply auto-layout to the non-overlapping structure. If the layout is too ambiguous to auto-resolve, surface a prompt: "These elements overlap — should I treat [element] as absolutely positioned or part of the flow?"
- **AC-2.8:** Given the user selects a frame with mixed content types (text, images, icons, shapes), When AI Auto-Layout is invoked, Then the AI should group semantically related elements (e.g., icon + label as a row, image + text as a card) before applying layout. Grouping should be visible and reversible.

#### Error Handling (Must-Have)

- **AC-2.9:** Given the AI produces a layout that breaks existing constraints or component overrides, When this is detected, Then show a warning: "This layout change would break [N] component overrides. Apply anyway?" with a list of affected components.

---

### US-3: Design System-Aware Suggestions

**As a** designer working within a brand's design system, **I want** Figma to proactively suggest design system components and tokens that match what I am building, **so that** I maintain consistency without memorizing the entire component library.

#### Functional (Must-Have)

- **AC-3.1:** Given the user is placing elements on the canvas that resemble an existing design system component (e.g., manually building something that looks like a card component), When the AI detects a >70% structural match, Then it surfaces a non-intrusive suggestion: "This looks like [Component Name] from your design system. Use it instead?" Clicking "Yes" replaces the manual elements with the component instance.
- **AC-3.2:** Given the user applies a color that is not in the linked design system's token set, When the color is applied, Then the AI suggests the nearest design system color token: "[#HexValue] is not in your design system. Nearest token: [Token Name] (#NearestHex). Use it?" The suggestion appears as a tooltip, not a modal.
- **AC-3.3:** Given the user has a linked design system, When they invoke the AI command bar, Then autocomplete suggestions prioritize design system components and patterns over generic generation.

#### Functional (Should-Have)

- **AC-3.4:** Given a team has design system usage analytics enabled, When the AI makes suggestions, Then it prioritizes components by team usage frequency (most-used components suggested first).

#### Non-Functional (Must-Have)

- **AC-3.5:** Suggestion latency must be under 500ms from the triggering action. Suggestions that arrive after the user has moved on (>2 seconds after trigger) should be suppressed, not queued.
- **AC-3.6:** Users must be able to disable AI suggestions globally or per-file via Settings > AI Preferences. Disabled state must persist across sessions.

#### Edge Cases (Must-Have)

- **AC-3.7:** Given a file links to multiple design system libraries, When the AI suggests components, Then it prioritizes the library that is most used in the current file. If usage is equal, show suggestions from all libraries with library name labels.
- **AC-3.8:** Given a design system component has been recently updated (within the last 24 hours), When the AI suggests it, Then it should flag: "[Component] was updated [time ago]. Review changes before using." This prevents silent adoption of breaking changes.

---

### US-4: AI-Powered Asset Variant Generation

**As a** designer preparing a design for multiple platforms and contexts, **I want to** generate asset variants (dark mode, size variants, platform-specific adaptations) from a single source design, **so that** I can eliminate hours of manual variant production work.

#### Functional (Must-Have)

- **AC-4.1:** Given the user selects a completed design frame, When they invoke "Generate Variants" and select target variants (e.g., dark mode, mobile, tablet), Then the AI produces each variant as a new frame on the canvas, preserving the semantic structure (component instances, auto-layout, text content) while adapting visual properties for the target context.
- **AC-4.2:** Given the user generates a dark mode variant, When the variant is created, Then the AI maps light-mode design tokens to their dark-mode equivalents from the linked design system. If no dark-mode tokens exist, the AI generates a reasonable default mapping (invert luminance, preserve hue) and flags: "No dark mode tokens found in your design system. Using auto-generated mapping — review recommended."

#### Functional (Should-Have)

- **AC-4.3:** Given the user has previously generated variants and made manual corrections, When they generate variants again for a different frame, Then the AI applies learned correction patterns (e.g., "user always adjusts dark-mode card backgrounds to #1E1E1E instead of pure black").

#### Edge Cases (Must-Have)

- **AC-4.4:** Given the source frame contains images or illustrations, When generating a dark mode variant, Then the AI should not invert image content. Images should be preserved as-is, with a flag: "[N] images detected — review for dark mode suitability."

---

### US-5: Natural Language Design Iteration

**As a** stakeholder reviewing a design in Figma, **I want to** describe changes in plain language (e.g., "make the header bigger and move the CTA above the fold"), **so that** I can provide actionable feedback without learning Figma's tools.

#### Functional (Must-Have)

- **AC-5.1:** Given a stakeholder with view/comment access opens a file, When they type a natural language edit suggestion in the AI command bar, Then the AI applies the change to a new branch (not the original file) and presents a side-by-side comparison. The original file is never modified by stakeholder suggestions.
- **AC-5.2:** Given the AI applies a natural language change, When the file owner reviews the branch, Then they see the original stakeholder comment, the AI's interpretation, and a diff view highlighting what changed. The owner can accept, reject, or modify.

#### Functional (Should-Have)

- **AC-5.3:** Given a stakeholder describes a change that is structurally ambiguous (e.g., "make it pop"), When the AI processes it, Then it should generate 2-3 interpretations (e.g., increase contrast, add shadow, increase size) as separate options rather than guessing.

---

## Scope Boundary Table

| Category | Item | Status | Rationale |
|---|---|---|---|
| Text-to-design generation (UI components, layouts) | Single and multi-component generation from natural language | **In Scope** | Core value proposition — directly addresses Canva competitive threat |
| Auto-layout assistant | AI-powered auto-layout and responsive resize | **In Scope** | Highest-impact production time saver per discovery research |
| Design system-aware suggestions | Component and token matching suggestions | **In Scope** | Differentiator vs Canva — Canva has no design system layer |
| Asset variant generation | Dark mode, responsive, platform variants | **In Scope** | Second-highest production time saver per discovery |
| Natural language design iteration | Stakeholder feedback as AI edits | **In Scope** | Expands addressable user base to non-designers |
| AI image generation (illustrations, photos) | Generating original images from prompts | **Out of Scope** | Competing head-to-head with Adobe Firefly and Midjourney is a separate product bet. Phase 1 focuses on design structure, not content creation. **Pull-forward trigger:** If Canva ships native image generation integrated into design workflows (not standalone Magic Media) |
| AI prototyping / interaction design | Generating animations, transitions, prototype flows | **Out of Scope** | Requires interaction model changes beyond Phase 1 scope. Auto-layout is the prerequisite. |
| AI code generation (design-to-code) | Generating production code from designs | **Out of Scope** | Adjacent market (Dev Mode). Requires partnership with code generation models. **Pull-forward trigger:** If competitors ship integrated design-to-code that demonstrably reduces developer handoff friction |
| AI-powered user research integration | Analyzing user test results to suggest design changes | **Deferred to Phase 2** | Valuable but depends on Phase 1 AI infrastructure. Trigger: Phase 1 AI feature adoption >30% MAU |
| Cross-file learning / org-level AI preferences | AI learning design patterns across a team's files | **Deferred to Phase 2** | Privacy and data governance requirements not yet resolved. Trigger: Enterprise customer advisory board approval of data policy |
| Fine-tuning on proprietary design data | Training custom models on a team's design history | **Deferred to Phase 3** | Requires model infrastructure investment and enterprise pricing. Trigger: 3+ Enterprise customers request in sales conversations |

---

## Technical & Design Context

### Architecture Constraints

1. **Model hosting:** AI inference runs on Figma's cloud infrastructure, not client-side. The Figma editor sends structured requests (prompt + canvas context) to an AI service; the service returns structured design specifications (not images) that the editor renders as native Figma layers.
2. **Canvas context window:** The AI service receives a serialized representation of the current frame (layer tree, component references, design tokens, spatial coordinates). Maximum context: 5,000 layers per request. Files exceeding this limit require the user to select a sub-frame.
3. **Design system indexing:** Design system libraries must be indexed by a background service that maintains a semantic embedding of each component (name, description, visual properties, usage frequency). Index refresh: within 5 minutes of a library publish.
4. **Branching for stakeholder edits:** US-5 requires Figma branching. All AI-generated changes from non-editor users must be created on a branch, never on the main file. This uses existing branching infrastructure.
5. **Latency budget:** Total round-trip (editor serialization + network + inference + deserialization + render) must stay within the latency targets in ACs. Network budget: <500ms. Inference budget: remainder. Implication: model must be optimized for structured output speed, not just quality.

### API Dependencies

| Dependency | Owner | Status | Risk |
|---|---|---|---|
| AI inference service (internal, code name "Muse") | Figma AI Platform team | In development — API contract finalized, alpha endpoint available | **Medium** — inference latency on complex prompts is currently 12s P50 (target: 8s). Optimization sprint planned for Q3. |
| Design system indexing service | Design Systems team | Production — existing infrastructure for search/autocomplete | **Low** — requires new embedding endpoint (semantic similarity), estimated 3 weeks engineering |
| Figma branching API | Editor Platform team | Production | **Low** — mature API, used by existing features |
| Content moderation service | Trust & Safety team | Production — existing image/text moderation | **Medium** — needs extension for design pattern moderation (e.g., deceptive UI detection). Estimated 4 weeks. |
| Usage analytics pipeline | Data Engineering | Production | **Low** — standard event logging |

### Data Requirements

- **Training data:** Model trained on anonymized, aggregated design patterns from public Figma Community files (with consent per ToS) and licensed design datasets. No proprietary customer file data used in training.
- **Inference context:** Per-request context includes only the current file's layer tree, linked design system tokens, and component library metadata. No cross-file or cross-team data accessed.
- **User preference storage:** Session-level AI learning (AC-2.4, AC-4.3) stored in browser local storage. No server-side user preference persistence in Phase 1.

### Decision Log

| # | Decision | Rationale | Date | Decided By |
|---|---|---|---|---|
| D1 | AI generates structured Figma layers, not rasterized images | Preserves editability — core Figma value prop. Canva generates flat outputs; this is our differentiator. | 2026-02-15 | PM + Eng Lead |
| D2 | Phase 1 uses a single foundation model (Muse) rather than routing to specialized models | Simplifies infrastructure and reduces latency. Specialized models (layout-specific, color-specific) deferred to Phase 2 based on quality gaps observed. | 2026-02-20 | AI Platform Lead |
| D3 | Design system suggestions are non-intrusive (tooltip, not modal) | Discovery research showed designers abandon tools with aggressive interruptions. Tooltip with keyboard shortcut to accept. | 2026-03-01 | Design Lead |
| D4 | Stakeholder AI edits always create a branch | Non-negotiable — file owners must have approval authority over all AI-generated changes from non-editors. | 2026-03-05 | PM + Legal |
| D5 | No client-side model execution in Phase 1 | WebAssembly model execution is not mature enough for the model size required. Revisit when WebGPU adoption exceeds 60% of Figma's browser user base. | 2026-02-25 | Eng Lead |

### Open Questions

| # | Question | Owner | Deadline | Impact if Unresolved |
|---|---|---|---|---|
| OQ-1 | What is the pricing model for AI features? Per-seat add-on, usage-based, or included in existing tiers? | Head of Product | 2026-04-15 | Blocks GTM planning and non-designer seat expansion metric target. Does not block engineering. |
| OQ-2 | Should AI generation count against file storage quotas? Generated layers add to file size. | PM + Eng Lead | 2026-05-01 | Could create surprise storage overages for free-tier users. Needs decision before GA. |
| OQ-3 | Content moderation policy for generated design patterns — what constitutes a "deceptive UI pattern"? | Trust & Safety + Legal | 2026-04-30 | Blocks AC-1.13 implementation. Interim: conservative blocklist of known dark patterns. |

---

## Failure Conditions & Rollback

### Failure Mode Register

| ID | Failure Mode | Detection Method | Impact | Mitigation |
|---|---|---|---|---|
| FM-1 | AI service latency exceeds targets consistently (>15s P50) | Latency monitoring dashboard, P50/P95 alerts | Users abandon feature, negative perception of "slow AI" | Circuit breaker: if P50 > 15s for 5 minutes, disable AI features and show "AI is experiencing high demand" message. Queue-based retry with user notification. |
| FM-2 | Generated designs are low quality (acceptance rate <30%) | Generation acceptance rate metric (leading indicator #2) | Users try once, never return — adoption dies | Quality gate: if acceptance rate drops below 30% for any 24-hour window, trigger model quality review. Fallback: route to higher-quality (slower) model variant. |
| FM-3 | Design system suggestions are wrong or annoying (suggestion dismissal rate >70%) | Dismissal rate tracking per suggestion type | Users disable suggestions entirely, losing the stickiness benefit | Adaptive throttling: if a user dismisses 3 consecutive suggestions, reduce suggestion frequency by 50% for that session. If dismissal rate >70% globally, pause suggestions and investigate. |
| FM-4 | AI generates content policy violations that slip past moderation | Automated scanning + user reports | Reputational damage, potential legal exposure | Post-generation scan (async) in addition to pre-generation check. User report mechanism with <4 hour response SLA for T&S review. |
| FM-5 | AI modifications corrupt file structure (broken layers, lost data) | File integrity check after every AI operation; automated regression tests | Data loss — worst case scenario | Every AI operation creates a recoverable snapshot (Figma version history entry) before execution. If integrity check fails, auto-revert to snapshot and surface error to user. |
| FM-6 | Model training data copyright claims | Legal monitoring, industry litigation tracking | Feature suspension, legal liability | Training data provenance documentation maintained. Ability to identify and remove specific training data contributions. Model retraining pipeline tested quarterly. |

### Rollback Criteria

Initiate full feature rollback (disable AI features behind feature flag) if ANY of the following occur:

1. **Data integrity:** Any confirmed case of AI operations causing file data loss or corruption in production.
2. **Sustained quality failure:** Generation acceptance rate below 25% for 48+ hours despite mitigation attempts.
3. **Security breach:** Any evidence that AI inference requests expose data from other users' files.
4. **Sustained latency:** P50 latency above 20 seconds for 2+ hours (indicates infrastructure failure, not load).

Rollback mechanism: Feature flag (`ai_features_enabled`) at organization, team, and global levels. Rollback time: <5 minutes from decision to full disable.

---

## Non-Functional Requirements

### Performance

| Requirement | Target | Measurement |
|---|---|---|
| Text-to-design generation (single component) | <8s P50, <15s P95 | Server-side latency + client render time |
| Text-to-design generation (full page) | <20s P50, <35s P95 | Server-side latency + client render time |
| Auto-layout analysis (<200 layers) | <3s P50 | Client-side analysis + server round-trip |
| Design system suggestion | <500ms from trigger | Client-side detection + index lookup |
| AI service availability | 99.5% uptime (separate from core Figma uptime SLA) | Uptime monitoring |

### Accessibility

- All AI UI surfaces (command bar, suggestion tooltips, variant picker) must meet WCAG 2.1 AA.
- AI command bar must be fully operable via keyboard (no mouse-only interactions).
- Screen reader announcements for AI generation progress: "Generating design... Design ready. Press Enter to place on canvas."
- AI-generated designs must produce accessible output by default (contrast ratios, semantic structure). The AI should not generate designs that fail basic accessibility checks unless the user explicitly overrides.

### Localization

- AI command bar UI: localized for all Figma-supported languages at launch (25 languages).
- Natural language prompt input: supported in 8 languages at launch (see AC-1.9). Additional languages based on usage data post-launch.
- AI-generated UI text: matches prompt language. Does not auto-translate.
- Design system token names remain in their original language (not translated).

### Security & Privacy

- No customer file data used for model training without explicit opt-in (enterprise admin-controlled).
- AI inference requests are isolated per-tenant. No cross-tenant data leakage in inference context.
- All AI-related API calls logged in enterprise audit trail (available to admins).
- AI features can be disabled at the organization level by enterprise admins (Settings > Organization > AI Features).

---

## Risk Register

| ID | Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R-1 | Muse model quality insufficient for production use at launch | Medium | High — delays launch or ships below quality bar | Parallel evaluation of third-party model APIs (Anthropic, OpenAI) as fallback. Decision point: 2026-06-01 internal quality benchmark. | AI Platform Lead |
| R-2 | Canva ships deeper AI integration before Figma GA | High | Medium — narrative disadvantage but Figma's design system integration is a structural moat Canva cannot replicate quickly | Accelerate alpha/beta timeline. Ship auto-layout assistant (US-2) as standalone feature in Q3 even if text-to-design is not ready. | PM Lead |
| R-3 | Enterprise customers block AI features due to data governance concerns | Medium | High — enterprise is 60%+ of revenue | Pre-launch enterprise advisory board (6 customers) to co-design data governance controls. Enterprise admin kill switch (already in NFRs). SOC 2 AI addendum. | Enterprise PM |
| R-4 | AI-generated designs create copyright/IP liability | Low | High — existential legal risk | Training data provenance documentation. Legal review of generated output sampling. Indemnification clause in ToS (legal draft in progress). | Legal |
| R-5 | Professional designers perceive AI features as threatening their role and resist adoption | Medium | Medium — vocal backlash could damage brand with core user base | Positioning: "AI handles production, you handle creativity." Beta program with design influencers. Never market as "replacing designers." | Marketing + PM |
| R-6 | Feature flag complexity causes incidents (wrong cohort gets AI, or AI disabled for paying users) | Low | Medium | Feature flag testing in staging with all permutations. Dedicated QA sprint for flag combinations. | Eng Lead |

---

## Assumption Registry

| # | Assumption | Confidence | What Breaks If Wrong |
|---|---|---|---|
| A-1 | Designers will trust AI-generated design elements enough to use them as starting points rather than building from scratch. | **M** — Canva's Magic Design adoption (~35% MAU) suggests willingness, but Figma's professional user base may have higher quality standards and lower tolerance for imperfect output. | If wrong, generation acceptance rate stays below 30% and the feature becomes a novelty rather than a workflow tool. Mitigation: invest in quality over speed; better to generate fewer, higher-quality outputs. |
| A-2 | The "Muse" inference service will achieve target latency (<8s P50) by Q3 2026. Current alpha is at 12s P50. | **M** — AI Platform team's optimization roadmap is credible but unproven at scale. 4-second improvement requires both model optimization and infrastructure scaling. | If wrong, text-to-design (US-1) ships with degraded UX. Auto-layout (US-2) and suggestions (US-3) are less latency-sensitive and can ship on time. Worst case: Phase 1 ships without text-to-design, which undermines the Canva-competitive narrative. |
| A-3 | Figma's design system indexing can be extended to support semantic embeddings without major re-architecture. | **H** — Design Systems team has confirmed technical feasibility and estimated 3 weeks of work. Embedding infrastructure exists for search; extending to component similarity is incremental. | If wrong, design system-aware suggestions (US-3) are delayed or degraded to keyword matching rather than semantic matching. Functional but less impressive. |
| A-4 | Non-designer users (PMs, marketers, founders) will adopt Figma for AI-assisted design rather than staying on Canva. | **L** — This is the highest-risk assumption. Switching costs are real (Canva templates, team familiarity). Figma's AI must be demonstrably better for their use cases, not just "also has AI." | If wrong, the non-designer seat expansion metric misses target. Professional designer productivity gains still justify the investment, but the growth narrative weakens. Mitigation: focus launch marketing on use cases where Figma AI is structurally better (design system consistency, component reuse, team collaboration). |
| A-5 | Content moderation for generated design patterns is solvable with existing approaches (classifier + blocklist) rather than requiring novel research. | **M** — Text and image moderation are mature. "Deceptive UI pattern" detection is less mature but bounded (known dark pattern taxonomies exist). | If wrong, AC-1.13 launches with an overly conservative moderation policy that blocks legitimate designs, frustrating users. Or launches with an overly permissive policy that allows deceptive patterns, creating reputational risk. |

---

## Adversarial Self-Critique

1. **The "3x velocity" target is aspirational, not evidence-based.** The baseline (4.2 hours) comes from 47 discovery interviews, which is a reasonable sample for qualitative patterns but not for a quantitative baseline. The 3x improvement target is benchmarked against Canva's reported metrics, but Canva's use cases are simpler (social media graphics vs. product UI). A more honest target might be 2x for comparable complexity, with 3x as a stretch goal. **Risk:** The team anchors on 3x and perceives 2x as failure.

2. **The spec does not address the cold-start problem for design system indexing.** For new Figma teams or teams without a mature design system, US-3 (design system-aware suggestions) provides no value. This is a significant portion of the non-designer target audience — the people most likely to be using Figma without a design system are the same people the AI features are supposed to attract. The spec should define a "no design system" fallback experience that is still compelling.

3. **Session-level learning (AC-2.4, AC-4.3) is a half-measure that may frustrate users.** Learning resets between sessions means the AI "forgets" preferences regularly. Users who invest in teaching the AI their preferences will feel the reset acutely. But server-side preference persistence was deferred for data governance reasons. This creates a UX gap that is known but unresolved. **Risk:** Users perceive the AI as "dumb" because it does not remember what they taught it yesterday.

4. **The stakeholder editing flow (US-5) introduces a novel collaboration model that is under-specified.** What happens when multiple stakeholders submit conflicting natural language edits? How does the branch merge experience work when AI-generated changes conflict with designer changes made in parallel? The spec defines the happy path but the multi-user concurrency scenarios need deeper design work before implementation.

5. **Latency targets assume stable model serving costs.** If inference costs are higher than projected, the business may pressure the team to degrade model quality (use smaller/faster model) to control costs. The spec does not define a minimum quality floor below which the feature should be disabled rather than degraded. Without this, cost pressure could gradually erode quality until the feature is useless but still "shipped."

---

## Quality Check

| Criterion | Status | Notes |
|---|---|---|
| Outcome-First Framing (measurable outcome, not feature description) | Pass | Primary metric: design velocity 3x. Secondary: production time -50%, seat expansion, churn. |
| Acceptance Criteria Taxonomy (functional, non-functional, edge, error) | Pass | All 5 user stories have categorized ACs with Given/When/Then. |
| Scope Boundary Protocol (in/out/deferred with rationale and triggers) | Pass | 11 items with explicit pull-forward triggers for deferred items. |
| Executor Context Model (architecture, APIs, data, decisions, open questions) | Pass | 5 architecture constraints, 5 API dependencies, decision log, 3 open questions with owners. |
| Failure Condition Design (failure modes, detection, rollback) | Pass | 6 failure modes with detection + mitigation. 4 rollback criteria with mechanism. |
| Assumption Registry (>=3 load-bearing assumptions) | Pass | 5 assumptions with confidence levels and "what breaks" analysis. |
| Adversarial Self-Critique (>=3 genuine weaknesses) | Pass | 5 weaknesses identified, including self-critique of the primary success metric. |
| Zero-question spec (engineer can start building) | Partial | OQ-1 (pricing) and OQ-3 (content moderation policy) remain open but do not block engineering start. Engineering can build all features behind feature flags while these resolve. |
| Reader Guide | Pass | Role-based and time-based reading paths in document header. |
