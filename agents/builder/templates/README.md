# Builder Templates

Reusable HTML templates for producing showcase-quality artifacts. Imported from `pm-agent-systems` design system.

## Design Standard

**[shared/toolkits/showcase-building-standard.md](../../../shared/toolkits/showcase-building-standard.md)** — Master design spec. Covers layout rules, color tokens, typography, component library (10 types), tabbed navigation (max 9 tabs), processing pipeline, and quality checklist. Read this before using any template.

## Templates

### showcase-case-study.html
Three-tab editorial layout: **Article · Process · System**

Best for: project write-ups, experiment reports, case studies, analysis showcases.

Features:
- Hero header with stats row
- Article tab with numbered highlights, aside callouts, metrics grid, vision block
- Process tab with timeline (done/fail/pivot dot states)
- System tab with layered architecture grid and principle cards
- `{{PLACEHOLDER}}` parameterization — find-replace to populate

### slide-deck.html
Presenter-mode slide deck with keyboard navigation.

Best for: meeting decks, reviews, status updates, proposals.

Features:
- Sticky nav with pill buttons per slide
- `F` for fullscreen, arrows/space to navigate, Esc to exit
- Component blocks: title, pillar grid, before/after comparison, data table, status chips, timeline, architecture flow, feature row, two-column cards
- Presenter bar with slide counter
- Most component blocks are commented out — uncomment what you need

## How to Use

1. Copy the template to the target project folder
2. Replace all `{{PLACEHOLDERS}}` with real content
3. Add/remove component blocks as needed
4. Open in browser — fully self-contained, no server required

## Color Tokens (quick reference)

| Token | Hex | Use |
|-------|-----|-----|
| `--accent` | `#B85C38` | Terracotta — primary accent, active states |
| `--sage` | `#5B7B6A` | Sage green — success, done states |
| `--warm-gold` | `#B8963E` | Gold — in-progress, secondary accent |
| `--stone` | `#8B7D6B` | Stone — neutral, muted elements |
| `--bg` | `#FDFAF6` | Cream background |

## Typography

- **Headings:** Source Serif 4 (serif)
- **Body:** Inter (sans-serif)
- **Data/Code:** JetBrains Mono (monospace)
