# DESIGN.md — Warm Editorial

> The design system for Agent Prime's landing site.
> Every token below is extracted from the shipped CSS. When in doubt, the CSS is canonical.

---

## 1. Visual Theme & Atmosphere

Warm Editorial is a design language built on the premise that intelligence should feel human-made. Where most technical sites lean on cold blues and clinical whites, Warm Editorial grounds itself in the palette of a well-kept leather journal: cream paper, terracotta ink, sage bookmarks, warm shadows that fall like afternoon light through a study window.

The atmosphere is **quiet confidence**. Nothing flashes. Nothing pulses. Information reveals itself through scroll-driven fade-ins that feel like turning a page. Headlines are set in a variable-optical-size serif (Source Serif 4) that carries the weight of considered thought. Body text is Inter — clean, readable, invisible — because the ideas should be louder than the typeface.

Dark mode is not an afterthought. It shifts to a warm olive-tinted near-black (`#0F0D0B`) that avoids the dead-screen look of pure `#000`. Surfaces become translucent glass. Stat cards gain a subtle glassmorphism blur. The code block background inverts to match the reading context, not fight it.

Color is semantic, not decorative. Each of Agent Prime's seven architectural layers owns a color — terracotta for Identity, sage for Memory, warm gold for Agents, stone for Orchestration, purple for Skills, error red for Craft, dark text for The Loop. These colors appear on card borders, layer numbers, and navigation links, building a subconscious map that persists across pages.

The overall effect: a site that feels like it was designed by someone who reads books, not someone who ships SaaS dashboards. Editorial warmth, engineering precision, zero dependencies.

---

## 2. Color Palette & Roles

### Light Mode (default)

| Token | Hex / Value | Role |
|-------|-------------|------|
| `--bg` | `#FDFAF6` | Page background — warm cream, not clinical white |
| `--surface` | `#FFFFFF` | Card and panel backgrounds |
| `--surface-warm` | `#F7F3ED` | Tinted surface for table headers, callout backgrounds, alternating rows |
| `--border` | `#E8E0D4` | Standard borders — warm, not gray |
| `--border-light` | `#F0EBE3` | Subtle separators, code inline borders |
| `--text` | `#2C2520` | Primary text — warm dark brown, never pure black |
| `--text-secondary` | `#6B5E52` | Secondary text, table cell values, subtitles |
| `--text-muted` | `#9B8E82` | Tertiary text, list markers, meta information |
| `--accent` | `#B85C38` | Terracotta — brand accent, links, primary buttons, active states |
| `--accent-light` | `rgba(184, 92, 56, 0.08)` | Accent tint for hover rows, light backgrounds |
| `--accent-medium` | `rgba(184, 92, 56, 0.15)` | Text selection highlight, medium emphasis |
| `--sage` | `#5B7B6A` | Sage green — Memory layer color |
| `--sage-light` | `rgba(91, 123, 106, 0.08)` | Sage tint for badges and backgrounds |
| `--warm-gold` | `#B8963E` | Warm gold — Agents layer color |
| `--warm-gold-light` | `rgba(184, 150, 62, 0.08)` | Gold tint for badges and backgrounds |
| `--stone` | `#8B7D6B` | Stone — Orchestration layer color |
| `--human` | `#6B4C8A` | Purple — Skills layer color |
| `--human-light` | `rgba(107, 76, 138, 0.08)` | Purple tint for badges and backgrounds |
| `--error` | `#A04030` | Error red — also Craft layer color |
| `--error-light` | `rgba(160, 64, 48, 0.08)` | Error tint for backgrounds |

### Dark Mode

Applied via `[data-theme="dark"]` on the `<html>` element. Every token is remapped:

| Token | Value | Notes |
|-------|-------|-------|
| `--bg` | `#0F0D0B` | Near-black with warm olive undertone |
| `--surface` | `rgba(255, 255, 255, 0.04)` | Translucent glass |
| `--surface-warm` | `rgba(255, 255, 255, 0.06)` | Slightly more opaque glass |
| `--border` | `rgba(255, 255, 255, 0.08)` | Faint white borders |
| `--border-light` | `rgba(255, 255, 255, 0.04)` | Near-invisible separators |
| `--text` | `#F0EDE8` | Warm off-white, not pure `#FFF` |
| `--text-secondary` | `#B0A89E` | Muted warm light |
| `--text-muted` | `#7A7068` | Subtle tertiary |
| `--accent` | `#D4714A` | Lighter terracotta — boosted for dark contrast |
| `--sage` | `#7BA08A` | Lightened sage |
| `--warm-gold` | `#D4B44A` | Lightened gold |
| `--stone` | `#A89888` | Lightened stone |
| `--human` | `#9A7CB8` | Lightened purple |
| `--error` | `#D05040` | Lightened error red |

### Layer Color System (semantic mapping)

Each of Agent Prime's seven architectural layers has a dedicated color. Use these consistently for top borders on layer cards, layer number text, badge variants, and navigation link accents:

| Layer | Color Token | Light Hex | Dark Hex |
|-------|-------------|-----------|----------|
| Identity | `--accent` | `#B85C38` | `#D4714A` |
| Memory | `--sage` | `#5B7B6A` | `#7BA08A` |
| Agents | `--warm-gold` | `#B8963E` | `#D4B44A` |
| Orchestration | `--stone` | `#8B7D6B` | `#A89888` |
| Skills | `--human` | `#6B4C8A` | `#9A7CB8` |
| Craft | `--error` | `#A04030` | `#D05040` |
| The Loop | `--text` | `#2C2520` | `#F0EDE8` |

### Shadows

Shadows use warm brown tint in light mode and pure black in dark mode. Never gray.

| Token | Light Mode | Dark Mode |
|-------|------------|-----------|
| `--shadow-sm` | `0 1px 3px rgba(44, 37, 32, 0.06)` | `0 1px 3px rgba(0, 0, 0, 0.2)` |
| `--shadow-md` | `0 4px 12px rgba(44, 37, 32, 0.08)` | `0 4px 12px rgba(0, 0, 0, 0.25)` |
| `--shadow-lg` | `0 8px 24px rgba(44, 37, 32, 0.12)` | `0 8px 24px rgba(0, 0, 0, 0.35)` |

### Gradient

The hero headline "Prime" uses a three-stop gradient applied via `background-clip: text`:

```css
background: linear-gradient(135deg, var(--accent), var(--warm-gold), var(--sage));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

---

## 3. Typography Rules

### Font Stacks

| Role | Stack | CSS Variable |
|------|-------|-------------|
| Headlines | `'Source Serif 4', Georgia, 'Times New Roman', serif` | `--font-serif` |
| Body / UI | `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` | `--font-sans` |
| Code | `'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace` | `--font-mono` |

### Weights Loaded

- **Source Serif 4:** 400 (regular), 600 (semibold), 700 (bold) — each in normal + italic
- **Inter:** 400 (regular), 500 (medium), 600 (semibold)
- **JetBrains Mono:** 400 (regular)

### Type Scale

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Source Serif 4 | 3.5rem (56px) | 700 | 1.15 | -0.03em | Landing page headline only |
| Section Title | Source Serif 4 | 2rem (32px) | 700 | 1.25 | -0.02em | `.section__title` |
| H1 | Source Serif 4 | 2.25rem (36px) | 700 | 1.25 | -0.02em | Page-level headings |
| H2 | Source Serif 4 | 1.625rem (26px) | 600 | 1.25 | -0.015em | Section sub-headings |
| H3 / Card Title | Source Serif 4 | 1.25rem (20px) | 600 | 1.25 | normal | Card headings, feature titles |
| H4 | Source Serif 4 | 1.0625rem (17px) | 600 | 1.25 | normal | Subsection headings |
| H5 | Source Serif 4 | 0.9375rem (15px) | 600 | 1.25 | normal | Minor headings |
| H6 / Overline | Source Serif 4 | 0.8125rem (13px) | 600 | 1.25 | 0.05em | Uppercase overlines, labels |
| Body | Inter | 1rem (16px) | 400 | 1.65–1.7 | normal | Default paragraph text |
| Subtitle | Inter | 1.0625rem (17px) | 400 | 1.7 | normal | `.subtitle`, section descriptions |
| Manifesto | Source Serif 4 | 1.1875rem (19px) | 400 | 1.8 | normal | Hero body copy — serif for gravitas |
| Nav Link | Inter | 0.875rem (14px) | 500 | 1.4 | normal | Navigation items |
| Button | Inter | 0.9375rem (15px) | 600 | 1.4 | normal | Primary / secondary buttons |
| Small Button / CTA | Inter | 0.8125rem (13px) | 600 | 1.4 | normal | Nav CTA, compact buttons |
| Badge | Inter | 0.75rem (12px) | 600 | 1.4 | normal | Pill badges |
| Table | Inter | 0.875rem (14px) | 400 (td) / 600 (th) | 1.4 | normal | Data tables |
| Layer Number | Source Serif 4 | 0.75rem (12px) | 600 | 1.0 | 0.1em | Uppercase, layer card labels |
| Stat Value | Source Serif 4 | 2rem (32px) | 700 | 1.2 | normal | Hero stat counters |
| Stat Label | JetBrains Mono | 0.6875rem (11px) | 500 | 1.0 | 0.05em | Uppercase, stat descriptions |
| Inline Code | JetBrains Mono | 0.8125em | 400 | inherit | normal | Relative to parent size |
| Code Block | JetBrains Mono | 0.8125rem (13px) | 400 | 1.65 | normal | Preformatted code |
| Footer | Inter | 0.8125rem (13px) | 400 | 1.4 | normal | Footer links and text |
| Footer Motto | Source Serif 4 | 0.875rem (14px) | 400 italic | 1.4 | normal | Italic closing line |

### Key Typographic Principles

- **Headings are serif, body is sans.** This contrast is the core of the editorial feel. Never set headings in Inter or body text in Source Serif (except for the hero manifesto, which deliberately uses serif for gravitas).
- **Tight tracking on large text.** Anything above 1.25rem gets negative letter-spacing (-0.015em to -0.03em). This prevents display text from looking loose.
- **Generous line height on body.** 1.65 to 1.8 for running text. Comfortable reading rhythm.
- **Uppercase is intentional, never default.** Only H6/overlines, layer numbers, stat labels, and badges use uppercase — always paired with widened letter-spacing (0.05em–0.1em).
- **`text-wrap: balance`** is applied to all headings to prevent orphans.
- **Font smoothing:** antialiased rendering on macOS (`-webkit-font-smoothing: antialiased`), grayscale on Firefox (`-moz-osx-font-smoothing: grayscale`), plus `text-rendering: optimizeLegibility`.

---

## 4. Component Stylings

### Buttons

**Primary Button (`.btn--primary`)**
```
Background:     var(--accent)          /* #B85C38 */
Text:           #FFFFFF
Padding:        0.75rem 1.75rem
Border-radius:  var(--radius)          /* 8px */
Font:           Inter, 0.9375rem (15px), weight 600
Hover:          background #A04E2E, box-shadow var(--shadow-md), transform translateY(-1px)
Transition:     all 0.2s ease
```

**Secondary Button (`.btn--secondary`)**
```
Background:     transparent
Text:           var(--text)
Border:         1.5px solid var(--border)
Padding:        0.75rem 1.75rem
Border-radius:  var(--radius)          /* 8px */
Font:           Inter, 0.9375rem (15px), weight 600
Hover:          border-color var(--accent), color var(--accent)
```

**Nav CTA (`.site-nav__cta`)**
```
Background:     var(--accent)
Text:           #FFFFFF
Padding:        0.5rem 1.25rem
Font:           Inter, 0.8125rem (13px), weight 600
Border-radius:  var(--radius)          /* 8px */
```

### Cards

**Standard Card**
```
Background:     var(--surface)
Border:         1px solid var(--border)
Border-radius:  var(--radius-lg)       /* 12px */
Padding:        1.5rem
Box-shadow:     var(--shadow-sm)
Hover:          box-shadow var(--shadow-md), transform translateY(-2px)
Transition:     box-shadow 0.25s ease, transform 0.25s ease
```

**Layer Card (`.layer-card`)**
```
Same as standard card, plus:
Border-top:     3px solid [layer-color]
```
Layer colors: `--accent` (Identity), `--sage` (Memory), `--warm-gold` (Agents), `--stone` (Orchestration), `--human` (Skills), `--error` (Craft), `--text` (The Loop).

**Artifact Card**
```
Border-radius:  var(--radius-lg)       /* 12px */
Image:          height 240px, object-fit: cover
Body padding:   1.25rem
```

**Decision Card**
```
Background:     var(--surface)
Border:         1px solid var(--border)
Border-left:    3px solid [layer-color]
Border-radius:  var(--radius)          /* 8px */
Padding:        1.25rem 1.5rem
Hover:          border-color var(--accent)
```

### Badges

```
Padding:        0.25rem 0.625rem
Font:           Inter, 0.75rem (12px), weight 600
Border-radius:  100px                  /* pill shape */
Line-height:    1.4
```

**Variants** (background uses `-light` token, text uses main token):
- `accent` — terracotta
- `sage` — sage green
- `gold` — warm gold
- `stone` — stone
- `human` — purple
- `error` — error red

### Callouts & Blockquotes

```
Border-left:    3px solid var(--accent)
Background:     var(--surface-warm)
Padding:        1.25rem 1.5rem
Border-radius:  0 8px 8px 0
```

**Variants** (change the `border-left` color):
- Default: `--accent` (terracotta)
- Info: `--sage`
- Warning: `--warm-gold`
- Tip: `--human`
- Error: `--error`

### Tables

```
Header row:     background var(--surface-warm)
TH padding:     0.75rem 1rem
TH font:        Inter, 0.875rem (14px), weight 600
TD padding:     0.75rem 1rem
TD color:       var(--text-secondary)
Even rows:      background var(--surface-warm)
Row hover:      background var(--accent-light)
```

### Code

**Inline Code**
```
Background:     var(--surface-warm)
Padding:        0.15rem 0.4rem
Border-radius:  4px
Border:         1px solid var(--border-light)
Color:          var(--accent)
Font:           JetBrains Mono, 0.8125em
```

**Code Block**
```
Background:     #1E1B18              /* warm near-black */
Text:           #E8E0D4
Padding:        1.25rem 1.5rem
Border-radius:  var(--radius)        /* 8px */
Border:         1px solid rgba(255, 255, 255, 0.06)
Font:           JetBrains Mono, 0.8125rem, line-height 1.65
Dark mode bg:   rgba(255, 255, 255, 0.04)
Dark mode border: var(--border)
```

### Navigation Bar

```
Background:     rgba(--bg with opacity) + backdrop-filter: blur
Position:       fixed, top: 0, full width
Logo:           Source Serif 4, weight 700, color var(--text)
Links:          Inter, 0.875rem, weight 500
CTA:            See Nav CTA button above
Theme toggle:   2.25rem square, var(--surface) bg, var(--border) border, var(--radius) corners
```

### Progress Bar

```
Position:       fixed, top: 0, left: 0
Height:         3px
Background:     linear-gradient(90deg, var(--accent), var(--warm-gold))
Z-index:        200
Width:          0%→100% (scroll-driven via JS)
```

### Hero Stat Cards (dark mode)

```
Glassmorphism:  backdrop-filter: blur(12px)
Background:     rgba(255, 255, 255, 0.06)
Border:         1px solid rgba(255, 255, 255, 0.1)
```

### Clone Command (dark mode)

```
Inverted:       background #F0EDE8, text #0F0D0B
```

---

## 5. Layout Principles

### Base Grid

- **Unit:** 8px — all spacing is derived from 0.5rem (8px) increments
- **Max content width:** 1200px (`.section` max-width, centered with auto margins)
- **Hero content width:** 800px max (narrower for reading focus)

### Spacing Scale

| Token | Value | Use |
|-------|-------|-----|
| `0.375rem` | 6px | Tight margins (list items, badge groups) |
| `0.5rem` | 8px | Compact padding (buttons, tags) |
| `0.75rem` | 12px | Standard button padding, table cells |
| `1rem` | 16px | Paragraph margins, standard gaps |
| `1.25rem` | 20px | Card inner padding (compact), callout padding |
| `1.5rem` | 24px | Card padding (standard), grid gaps |
| `2rem` | 32px | Section horizontal padding, horizontal rules |
| `4rem` | 64px | Hero bottom padding |
| `6rem` | 96px | Section vertical padding |
| `8rem` | 128px | Hero top padding |

### Section Structure

Every section follows the same rhythm:
```
padding: 6rem 2rem        /* 96px top/bottom, 32px sides */
max-width: 1200px
margin: 0 auto
```

The hero section uses expanded padding:
```
padding: 8rem 2rem 4rem   /* 128px top, 32px sides, 64px bottom */
```

### Grid Patterns

| Pattern | CSS | Use |
|---------|-----|-----|
| 3-column | `grid-template-columns: repeat(3, 1fr)` | Ceilings, paths, levels |
| 2-column | `grid-template-columns: repeat(2, 1fr)` | Layers, decisions |
| Auto-fit gallery | `grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))` | Artifact gallery, flexible grids |
| Card gap | `gap: 1.5rem` (24px) | Consistent spacing between all grid children |

### Section Numbering

Each major section includes a large, decorative section number positioned above the header:
```
Font:           Source Serif 4, weight 700
Size:           Large (display-scale)
Color:          var(--border)          /* subtle, not competing with content */
```

---

## 6. Depth & Elevation

### Elevation Tiers

| Level | Shadow | Transform | Use |
|-------|--------|-----------|-----|
| Resting | `--shadow-sm` | none | Cards at rest, nav bar |
| Raised | `--shadow-md` | `translateY(-1px)` | Primary button hover |
| Lifted | `--shadow-md` | `translateY(-2px)` | Card hover state |
| Floating | `--shadow-lg` | none | Modals, overlays (reserved) |

### Transition Standards

All elevation changes use consistent easing:
```
transition: box-shadow 0.25s ease, transform 0.25s ease
```

Buttons use a faster transition:
```
transition: all 0.2s ease
```

### Border Depth

Borders provide structural depth in addition to shadows:
- **Standard:** `1px solid var(--border)` — most containers
- **Light:** `1px solid var(--border-light)` — inline code, subtle separators
- **Accent highlight:** `3px solid [color]` — layer card tops, callout left edges, decision card left edges

### Dark Mode Depth

In dark mode, shadows shift to pure black with heavier opacity (0.2 / 0.25 / 0.35). Surface depth is primarily communicated through **opacity layers** rather than shadows:
- Background (`--bg`): solid `#0F0D0B`
- Surface: `rgba(255, 255, 255, 0.04)` — barely visible lift
- Surface-warm: `rgba(255, 255, 255, 0.06)` — slightly more present
- Borders: `rgba(255, 255, 255, 0.08)` — faint structural lines

This creates depth through luminosity stacking, not drop shadows.

### Special Effects

**Glassmorphism** (dark mode hero stats only):
```css
backdrop-filter: blur(12px);
background: rgba(255, 255, 255, 0.06);
border: 1px solid rgba(255, 255, 255, 0.1);
```

**Gradient text** (hero "Prime" word):
```css
background: linear-gradient(135deg, var(--accent), var(--warm-gold), var(--sage));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

---

## 7. Do's and Don'ts

### Do

- **Use warm tones for shadows.** Light mode shadows are `rgba(44, 37, 32, ...)` — brown-tinted, matching the warm palette. Gray shadows (`rgba(0,0,0,...)`) are only for dark mode.
- **Pair serif headlines with sans body.** This typographic contrast is the signature. Source Serif 4 for anything that should feel considered; Inter for anything that should feel clear.
- **Use the layer color system consistently.** If a card represents the Memory layer, its top border is sage. If a badge says "Agents," it uses the gold variant. This mapping is not decorative — it builds spatial memory.
- **Apply `-light` tints for backgrounds.** When a layer color needs to appear as a background (not a border or text), use the `-light` variant (8% opacity). Full-strength colors as backgrounds overwhelm the warm cream.
- **Keep text warm, never black.** Primary text is `#2C2520`, not `#000000`. Dark mode text is `#F0EDE8`, not `#FFFFFF`. Pure black and white create harsh contrast that breaks the editorial warmth.
- **Use the scroll animation pattern.** Elements should fade in from `translateY(20px)` with `opacity: 0→1` over `0.6s ease`. Stagger children by `0.1s` each. This creates a reading rhythm, not a performance.
- **Use `text-wrap: balance` on all headings.** Prevents typographic orphans.
- **Set inline code in the accent color.** `color: var(--accent)` on inline code makes it visually distinct without being garish.

### Don't

- **Don't use pure black (`#000`) or pure white (`#FFF`) for text.** The system uses warm near-black and warm off-white. The only exception is button text on accent backgrounds (`#FFFFFF` is acceptable there for contrast).
- **Don't use gray shadows in light mode.** Every shadow in light mode uses `rgba(44, 37, 32, ...)`. Gray shadows (`rgba(0,0,0,...)`) look cold and alien.
- **Don't use border-radius above 12px on containers.** Cards and large containers use `--radius-lg` (12px). Only badges use the pill radius (100px). Rounded rectangles above 12px look like mobile OS buttons, not editorial design.
- **Don't set body text in Source Serif 4.** The sole exception is the hero manifesto (19px, serif, high line-height). All other running text uses Inter.
- **Don't add new colors outside the layer system.** If something needs a color, it maps to an existing layer or uses the accent. If you catch yourself reaching for a blue, an orange, or a teal — stop. The palette is intentionally constrained.
- **Don't apply uppercase without widened letter-spacing.** Uppercase text with normal tracking looks cramped. Every uppercase element in the system pairs with 0.05em–0.1em letter-spacing.
- **Don't animate with durations above 0.6s** (except the background floating shapes at 7–8s). UI transitions stay at 0.15s–0.3s. Scroll reveals at 0.6s. Anything slower feels sluggish.
- **Don't use background colors for emphasis in dark mode.** Dark mode depth comes from opacity layers, not distinct background colors. Adding a solid `#1A1A1A` card onto a `#0F0D0B` page breaks the translucency system.

---

## 8. Responsive Behavior

### Breakpoints

The system uses a mobile-first approach with two primary breakpoints:

| Breakpoint | Width | Grid Change |
|------------|-------|-------------|
| Small | < 768px | Single column, stacked layout |
| Medium | 768px–1024px | 2-column where applicable |
| Large | > 1024px | Full 3-column grid, side-by-side layouts |

### Responsive Adjustments

**Typography:**
- Hero display scales from `3.5rem` (56px) on desktop to approximately `2rem` (32px) on mobile
- Section titles scale from `2rem` (32px) to approximately `1.5rem` (24px)
- Body text remains `1rem` (16px) — it does not scale down
- Line heights remain constant across breakpoints

**Layout:**
- 3-column grids collapse to 2 columns at medium, then 1 column at small
- 2-column grids collapse to 1 column at small
- `auto-fit minmax(260px, 1fr)` grids self-adjust naturally
- Section padding reduces from `6rem 2rem` to approximately `3rem 1rem` on mobile
- Hero padding reduces from `8rem 2rem 4rem` to approximately `4rem 1rem 2rem`

**Navigation:**
- At small breakpoints, the nav links collapse into a hamburger menu
- The nav CTA button and theme toggle remain visible
- The hamburger icon (`&#9776;`) toggles an `aria-expanded` menu panel

**Cards:**
- Card padding may reduce from `1.5rem` to `1.25rem` on mobile
- Hover transforms (`translateY(-2px)`) are preserved — they work on touch via tap feedback
- Artifact card image height may reduce from `240px` to `180px`

**General principles:**
- The `max-width: 1200px` container naturally centers and constrains on large screens
- Horizontal padding (`2rem` on sections) prevents edge-to-edge content on tablets
- The progress bar and floating shapes remain full-width on all screen sizes
- Font loading strategy does not change — all weights are loaded regardless of viewport

---

## 9. Agent Prompt Guide

Use these prompts when asking an AI to generate new pages or components for the Agent Prime site. Each prompt encodes the Warm Editorial system so that output is visually consistent without the AI needing to read the full CSS.

### Prompt: New Layer Page

```
You are building a page for the Agent Prime landing site using the "Warm Editorial" design system.

Design tokens (use these as CSS custom properties):
- Backgrounds: --bg (#FDFAF6), --surface (#FFF), --surface-warm (#F7F3ED)
- Text: --text (#2C2520, warm dark brown — never pure black), --text-secondary (#6B5E52), --text-muted (#9B8E82)
- Accent: --accent (#B85C38, terracotta), hover darken to #A04E2E
- Borders: --border (#E8E0D4), --border-light (#F0EBE3)
- Shadows: warm brown tint — --shadow-sm (0 1px 3px rgba(44,37,32,0.06)), --shadow-md (0 4px 12px rgba(44,37,32,0.08))
- Radii: --radius (8px), --radius-lg (12px)

Typography:
- Headlines: 'Source Serif 4', Georgia, serif — weights 600/700, tight letter-spacing (-0.02em)
- Body: 'Inter', system-ui, sans-serif — weight 400, line-height 1.65–1.7
- Code: 'JetBrains Mono', monospace — weight 400
- Headings are serif, body is sans. Never mix.

Layer color for this page: [INSERT LAYER TOKEN, e.g., --sage for Memory].
Use the layer color for: top border on cards (3px), layer number text, badge backgrounds (use the -light variant at 8% opacity), and navigation link accents.

Components:
- Cards: --surface bg, 1px --border, 12px radius, 1.5rem padding, --shadow-sm resting, hover lifts -2px with --shadow-md
- Buttons: Primary is --accent bg with #FFF text, 8px radius, 0.75rem 1.75rem padding. Secondary is transparent with 1.5px --border.
- Badges: 0.75rem (12px) font, 600 weight, 100px radius pill, 0.25rem 0.625rem padding
- Callouts: 3px left border in layer color, --surface-warm bg, 0 8px 8px 0 radius
- Code inline: --surface-warm bg, --accent text color, 4px radius, 1px --border-light border

Animations: Scroll fade-in (translateY(20px) to 0, opacity 0 to 1, 0.6s ease, stagger 0.1s per child). Card hover: translateY(-2px), 0.25s ease.

Dark mode: Applied via [data-theme="dark"]. --bg becomes #0F0D0B, --surface becomes rgba(255,255,255,0.04), --text becomes #F0EDE8, shadows switch to rgba(0,0,0,...). All layer colors lighten. Depth comes from opacity layers, not distinct background colors.

Layout: Max-width 1200px centered. Section padding 6rem 2rem. Card grid gap 1.5rem.

Build a [DESCRIBE PAGE] that follows this system exactly. Use semantic HTML5, BEM-style class names, and include dark mode support.
```

### Prompt: New Component

```
You are adding a component to the Agent Prime landing site ("Warm Editorial" design system).

Core rules:
1. Text is NEVER pure black or pure white. Use --text (#2C2520) and --text (#F0EDE8) in dark mode.
2. Shadows are warm brown in light mode: rgba(44, 37, 32, ...). Pure black in dark mode.
3. Headlines use Source Serif 4 (serif). Body uses Inter (sans-serif). Code uses JetBrains Mono.
4. Border-radius: 8px (standard), 12px (cards/large containers), 100px (badges only).
5. The accent color is terracotta (#B85C38). Hover darkens to #A04E2E.
6. Every interactive element needs hover lift (translateY(-1px or -2px)) and shadow escalation.
7. The layer color system maps: Identity=terracotta, Memory=sage (#5B7B6A), Agents=gold (#B8963E), Orchestration=stone (#8B7D6B), Skills=purple (#6B4C8A), Craft=error-red (#A04030), The Loop=text-color.
8. Dark mode uses translucent surfaces (rgba(255,255,255,0.04-0.06)), not distinct solid colors.
9. Inline code: terracotta text, warm surface bg, light border, 4px radius.
10. Uppercase text always pairs with letter-spacing (0.05em–0.1em).

Build a [DESCRIBE COMPONENT] following these rules. Output clean HTML + CSS using the custom property names above.
```

### Prompt: Matching Content Section

```
I need a new content section for the Agent Prime landing site. The existing sections follow this pattern:

Structure:
- Section wrapper: class="section fade-in", padding 6rem 2rem, max-width 1200px centered
- Section number: decorative "04" style number in --border color
- Section header: .section__title (Source Serif 4, 2rem, 700, -0.02em tracking) + .section__subtitle (Inter, 1.0625rem, --text-secondary)
- Content grid: cards or content blocks in a grid (gap 1.5rem), with stagger class for animation
- Each child card: class="reveal" for scroll-triggered fade-in

Visual feel: "A well-kept leather journal." Warm cream backgrounds, terracotta accents, editorial serif headlines with clean sans-serif body. Quiet confidence — nothing flashes, information reveals itself through gentle scroll animations.

Section number for this one: [NUMBER, e.g., "04"].
Topic: [DESCRIBE SECTION CONTENT].

Match the existing rhythm exactly. Use the CSS custom properties (--bg, --surface, --border, --accent, --text, --text-secondary, --radius-lg, --shadow-sm, etc.). Include the fade-in and stagger animation classes.
```

### Prompt: Dark Mode Audit

```
Review the following HTML/CSS for Warm Editorial dark mode compliance:

Checklist:
- [ ] No hardcoded #FDFAF6, #FFFFFF, #2C2520, or other light-mode colors — all must use CSS custom properties
- [ ] Shadows use --shadow-sm/md/lg tokens (which remap to rgba(0,0,0,...) in dark mode)
- [ ] No solid dark backgrounds — surfaces should be rgba(255,255,255,0.04) or 0.06
- [ ] Accent color lightens in dark mode (#B85C38 → #D4714A) via the token remap
- [ ] Text never becomes pure #FFFFFF — should be #F0EDE8 via --text
- [ ] Code blocks switch from #1E1B18 bg to rgba(255,255,255,0.04) bg in dark mode
- [ ] Inline code border switches from --border-light to dark mode's rgba(255,255,255,0.04)
- [ ] Hero stat cards use glassmorphism (backdrop-filter: blur(12px), rgba surface, rgba border)
- [ ] Layer colors all remap to their lightened variants
- [ ] No gray shadows (rgba(128,128,128,...)) anywhere

[PASTE CODE HERE]
```

---

*Warm Editorial v1.0.0 — extracted from `assets/style.css`, canonical as of 2026-04-07.*
