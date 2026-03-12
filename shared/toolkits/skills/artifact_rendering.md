---
name: "Artifact Rendering"
version: "1.0.0"
tags: ["Execution", "Architecture"]
created: "2026-03-02"
valid_until: "2026-09-02"
derived_from: "shared/toolkits/showcase-building-standard.md, agents/builder/templates/"
tested_with: ["Builder agent"]
references_path: "../../showcase-building-standard.md"
description: "Use when converting markdown documents, analyses, or structured data into interactive HTML showcases or slide decks."
---

## Purpose

Convert structured markdown content (analyses, case studies, experiment reports, investment research) into self-contained, interactive HTML artifacts using the Agent Prime design system and template library.

## Input Contract

### Required

- **Source content** (markdown file or structured data): The document to render. Can be a thesis, analysis, experiment report, case study, or any structured markdown with sections, tables, and data.
- **Template selection** (string): Which template to use:
  - `"case-study"` → `agents/builder/templates/showcase-case-study.html` — 3-tab editorial layout (Article · Process · System). Best for: project write-ups, experiment reports, research showcases, investment analyses.
  - `"slide-deck"` → `agents/builder/templates/slide-deck.html` — Presenter-mode slide deck with keyboard navigation. Best for: meeting decks, reviews, proposals, status updates.
  - `"custom"` → Build from scratch following the design standard. Only when neither template fits.

### Optional

- **Tab structure override** (list of strings, default: auto-derived from content headings): Custom tab names if the content doesn't map cleanly to the template's default tabs.
- **Output path** (string, default: caller decides): Where to save the rendered HTML file.
- **Hero stats** (list of {value, label} pairs, default: derived from content): Numbers to display in the header stats row.

### Anti-Inputs

- **Raw prose without structure.** This skill renders structured content. If the input is unstructured prose, route to the Writer first to structure it, then render.
- **Content creation.** This skill transforms existing content into HTML. It does not write new content, analyze data, or form theses.

## Method

### Quick Version

1. Read the source content and identify its structure (sections, tables, data points, key metrics).
2. Select template (case-study or slide-deck) based on content type.
3. Map content sections to template tabs/slides using the Tab Grouping Algorithm from the design standard.
4. Replace all `{{PLACEHOLDERS}}` in the template with real content.
5. Apply the component library — match content patterns to HTML components.
6. Validate against the quality checklist.

### Full Version

**Step 1: Content Audit**

Read the source markdown. Classify each section:

| Classification | Detection | Template mapping |
|---|---|---|
| Summary / overview | Executive summary, abstract, intro | Hero header + first tab |
| Structured data | Tables, matrices, registries | Data tables, metrics rows, stat cards |
| Process / timeline | Chronological steps, phases, iterations | Process tab with timeline dots |
| Architecture / system | Components, layers, flows, dependencies | System tab with architecture grid |
| Analysis / narrative | Paragraphs with claims, evidence, insights | Article tab with aside callouts + highlight items |
| Metrics / results | Numbers, percentages, scores, comparisons | Stats row, metrics grid, progress bars |

**Step 2: Template Selection**

| Content type | Template | Reasoning |
|---|---|---|
| Project write-up, experiment report, case study | `case-study` | Natural 3-tab split: what happened (Article), how (Process), what enabled it (System) |
| Investment / industry analysis | `case-study` | Article = thesis + findings, Process = methodology, System = data sources + portfolio context |
| Meeting deck, review, proposal | `slide-deck` | Discrete slides with presenter navigation |
| Multi-section framework or spec | `custom` | When content has >3 natural sections that don't fit Article/Process/System |

**Step 3: Tab/Slide Mapping**

For **case-study** template:
- **Article tab** ← Findings, thesis, highlights, metrics, conclusions
- **Process tab** ← Methodology, timeline, iteration history, failures/pivots
- **System tab** ← Architecture, tools used, design principles, dependencies

For **slide-deck** template:
- Map each major section to a slide
- Title slide = overview + key stats
- Choose component blocks per slide (pillar grid, before/after, data table, timeline, architecture flow, two-column cards)
- Update nav buttons to match slide count

Apply the **Tab Budget** rule: maximum 9 tabs. If content has more sections, merge adjacent sections per the Tab Grouping Algorithm (see `shared/toolkits/showcase-building-standard.md` § 1.3).

**Step 4: Placeholder Replacement**

Copy the template. Find every `{{PLACEHOLDER}}` and replace with real content:
- `{{HEADLINE}}` → Document title
- `{{SUBTITLE}}` → One-sentence summary
- `{{N1}}`...`{{N4}}` → Key metrics from content
- `{{AUTHOR_NAME}}`, `{{DATE}}` → Attribution
- Content blocks → Narrative paragraphs, highlight items, timeline phases, architecture layers

**Step 5: Component Application**

Match content patterns to the design system's component library:

| Content pattern | Component | Reference |
|---|---|---|
| Key insight or callout | `.aside-block` with icon | Building standard § 3.6 |
| Numbered list of findings | `.highlight-item` with markers (01, 02...) | Building standard § 3.7 |
| Metric comparisons | `.metrics-row` 3-column grid | Building standard § 3.10 |
| Chronological phases | `.tl-phase` with dot states (done/fail/pivot) | Template Process tab |
| System components | `.layer-item` chips (active/built) in `.arch-grid` | Template System tab |
| Evidence tiers | `.ev-badge` with tier colors | Building standard § 3.2 |
| Confidence levels | `.conf-pill` (H/M/L) | Building standard § 3.3 |
| Status indicators | `.chip` (done/prog/pending) | Slide deck template |

**Step 6: Quality Validation**

Run the quality checklist from the building standard:

- [ ] Self-contained — opens in any browser, no external dependencies except Google Fonts
- [ ] Tabbed navigation works — each tab shows/hides correctly
- [ ] Design tokens applied — terracotta accent, sage green, warm gold palette
- [ ] Typography — Source Serif 4 headings, Inter body, JetBrains Mono for data
- [ ] Max-width 960px (case study) or 1400px (slide deck)
- [ ] Responsive — readable at 768px
- [ ] Keyboard navigation works (slide deck: arrows + F for fullscreen)
- [ ] No placeholder text remaining — all `{{...}}` replaced
- [ ] Print stylesheet present
- [ ] File named per Rule 20: `{subject}_{type}_{date}.html`

## Evaluation Criteria

A rendered artifact is successful when:

1. **Navigability** — Reader can reach any section in ≤2 clicks. No scrolling through irrelevant content.
2. **Visual consistency** — Matches the design system. Same colors, fonts, and component patterns as other Agent Prime showcases.
3. **Content fidelity** — All source content is present. Nothing dropped, nothing invented.
4. **Self-contained** — Opens in any browser with no server, no build step, no dependencies beyond Google Fonts CDN.
5. **Component-appropriate** — Content patterns are rendered as the right components (tables as tables, timelines as timelines, not everything as paragraphs).

## Key References

- **Design standard:** `shared/toolkits/showcase-building-standard.md` — color tokens, typography, all 10 component types, processing pipeline, quality checklist
- **Case study template:** `agents/builder/templates/showcase-case-study.html` — 3-tab (Article · Process · System), `{{PLACEHOLDER}}` parameterized
- **Slide deck template:** `agents/builder/templates/slide-deck.html` — presenter-mode, 11 component block types, keyboard navigation
- **Template index:** `agents/builder/templates/README.md` — quick reference for available templates and color tokens
