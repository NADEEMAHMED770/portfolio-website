# Design System

**Document:** 09-design-system.md
**Version:** 1.0
**Status:** Awaiting palette decision — Phase 1, Session 5
**Last Updated:** 2026-10-13

---

## 1. Design Principles

| Principle | What It Means |
|---|---|
| **Content first** | Design serves the content. No decoration that distracts. |
| **Quiet confidence** | No flashy gradients, no animations for their own sake. |
| **Consistent over clever** | Every button looks the same. Every card uses the same radius. |
| **Accessible by default** | WCAG 2.1 AA minimum. Contrast checked before shipping. |
| **Fast by design** | No heavy frameworks. CSS variables, minimal JS. |

**Target audience:** Recruiters, hiring managers, technical peers.
**Feel:** Engineer-built, not designer-decorated.

---

## 2. Color Palettes — Three Options

**Each option includes:**
- Full color scale (50 → 900) for primary
- Text/neutral colors
- Semantic colors (success, warning, error)
- Dark mode equivalents

### 🅰️ Palette A — Technical Indigo

**Vibe:** Modern SaaS, calm, professional. Inspired by Vercel, Linear, Stripe.

**Primary (Indigo):**
```
50   #EEF2FF    Lightest (backgrounds)
100  #E0E7FF
200  #C7D2FE
300  #A5B4FC
400  #818CF8
500  #6366F1    ← Base
600  #4F46E5    ← Main brand color
700  #4338CA
800  #3730A3
900  #312E81    Darkest
```

**Accent:** Cyan `#06B6D4`

**Neutrals (Slate):**
```
50   #F8FAFC    Page background (light)
100  #F1F5F9    Card background (light)
200  #E2E8F0    Borders
300  #CBD5E1
400  #94A3B8
500  #64748B    Muted text
600  #475569
700  #334155
800  #1E293B    Card background (dark)
900  #0F172A    Page background (dark)
```

**Semantic:**
```
Success  #10B981   (Emerald 500)
Warning  #F59E0B   (Amber 500)
Error    #EF4444   (Red 500)
Info     #3B82F6   (Blue 500)
```

**Photo treatment:** Remove green background → replace with neutral gray or dark slate.

---

### 🅱️ Palette B — Data Emerald ⭐ RECOMMENDED

**Vibe:** Data-focused, distinctive, matches existing photo. Signal: "I work with data."

**Primary (Emerald):**
```
50   #ECFDF5    Lightest
100  #D1FAE5
200  #A7F3D0
300  #6EE7B7
400  #34D399
500  #10B981    ← Base
600  #059669    ← Main brand color
700  #047857
800  #065F46
900  #064E3B    Darkest
```

**Accent:** Slate 900 `#0F172A` (near-black for emphasis)

**Neutrals (Slate):** *(same as Palette A — keeping neutrals consistent across options)*
```
50   #F8FAFC    Page background (light)
100  #F1F5F9    Card background (light)
200  #E2E8F0    Borders
300  #CBD5E1
400  #94A3B8
500  #64748B    Muted text
600  #475569
700  #334155
800  #1E293B    Card background (dark)
900  #0F172A    Page background (dark)
```

**Semantic:** *(same as Palette A)*

**Photo treatment:** **Keep the green background.** It becomes part of the brand identity — no replacement needed.

**Why this is my recommendation:**
- Your photo already has bright green — palette B makes it *intentional*
- Green signals data/analytics (used by Datadog, Grafana, Sentry)
- Distinctive — most dev portfolios are blue/purple
- Works with WCAG AA on Slate 900 text
- Feels modern without being trendy

---

### 🅲 Palette C — AI Violet

**Vibe:** Bold, AI-startup energy. Inspired by modern LLM tools.

**Primary (Violet):**
```
50   #F5F3FF    Lightest
100  #EDE9FE
200  #DDD6FE
300  #C4B5FD
400  #A78BFA
500  #8B5CF6    ← Base
600  #7C3AED    ← Main brand color
700  #6D28D9
800  #5B21B6
900  #4C1D95    Darkest
```

**Accent:** Pink `#EC4899`

**Neutrals (Slate):** *(same as A/B)*

**Semantic:** *(same as A/B)*

**Photo treatment:** Remove green background → replace with dark charcoal.

**Risk:** Violet + pink can read as "hackathon project" if not executed precisely. Requires discipline.

---

## 3. Palette Comparison

| Aspect | A — Indigo | B — Emerald ⭐ | C — Violet |
|---|---|---|---|
| Uniqueness | Low (very common) | High | Medium |
| AI/Data signaling | Generic tech | Strong | Strong |
| Matches photo | ❌ Requires new photo | ✅ Works as-is | ❌ Requires new photo |
| Risk | Low | Low | Medium |
| Feels | Corporate | Distinctive | Bold |
| Dark mode | Excellent | Excellent | Good |

**My recommendation: B (Data Emerald).** Reasons above.

---

## 4. Typography

### Fonts

| Use | Font | Fallback |
|---|---|---|
| UI / body | **Inter** | system-ui, -apple-system, sans-serif |
| Code / mono | **JetBrains Mono** | Fira Code, Menlo, monospace |

**Both are free, open-source, and industry standard.** Load via Google Fonts.

### Type Scale (Fluid)

Use `clamp()` for responsive sizing without media queries.

| Token | Mobile | Desktop | Use |
|---|---|---|---|
| `text-xs` | 12px | 12px | Labels, badges |
| `text-sm` | 14px | 14px | Secondary text, meta |
| `text-base` | 16px | 16px | Body |
| `text-lg` | 17px | 18px | Lead paragraphs |
| `text-xl` | 19px | 20px | Subheadings |
| `text-2xl` | 22px | 24px | Section titles |
| `text-3xl` | 26px | 30px | Page titles |
| `text-4xl` | 30px | 36px | Hero subheading |
| `text-5xl` | 34px | 48px | Hero heading |

### Weights

| Weight | Value | Use |
|---|---|---|
| Regular | 400 | Body |
| Medium | 500 | Emphasis, nav |
| Semibold | 600 | Headings |
| Bold | 700 | Hero heading |

### Line Heights

| Context | Line-height |
|---|---|
| Headings | 1.2 |
| Body | 1.6 |
| Compact UI | 1.4 |

### Letter Spacing

- Body: 0 (default)
- Headings: -0.02em (tightens large text)
- Uppercase labels: 0.05em

---

## 5. Spacing System

**8px base grid.** All spacing values are multiples.

| Token | Value | Use |
|---|---|---|
| `space-1` | 4px | Icon padding |
| `space-2` | 8px | Small gaps |
| `space-3` | 12px | Compact padding |
| `space-4` | 16px | Default padding |
| `space-6` | 24px | Section gaps |
| `space-8` | 32px | Section padding |
| `space-12` | 48px | Large gaps |
| `space-16` | 64px | Section separators |
| `space-24` | 96px | Hero padding |

**Why 8px?** Divides cleanly, matches device pixel ratios, industry standard (Tailwind, Material, Bootstrap).

---

## 6. Border Radius

| Token | Value | Use |
|---|---|---|
| `radius-sm` | 4px | Tags, chips |
| `radius` | 8px | Buttons, inputs, cards |
| `radius-lg` | 12px | Large cards, modals |
| `radius-xl` | 16px | Hero image container |
| `radius-full` | 9999px | Avatars, pills |

**Consistency rule:** Button radius = input radius = card radius (8px). Creates visual coherence.

---

## 7. Shadows

Subtle, layered. Never harsh.

| Token | Value | Use |
|---|---|---|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elevation |
| `shadow` | `0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)` | Cards (default) |
| `shadow-md` | `0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)` | Hover states |
| `shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | Modals, dropdowns |

**Dark mode:** Reduce opacity; rely on subtle borders instead.

---

## 8. Component Inventory

Components needed for v1.0, grouped by priority:

### Core (Must-Have)
| Component | Variants | Used In |
|---|---|---|
| Button | primary, secondary, ghost, icon | Everywhere |
| Card | default, project, stat | Home, Projects, Dashboard |
| Input | text, email, password, textarea, select | Forms |
| Navbar | public, mobile, admin | All public pages |
| Footer | 3-column | All public pages |
| Chip / Tag | skill, tech, filter | Skills, Projects |
| Badge | info, success, warning | Status indicators |
| Alert / Flash | success, error, info | Form feedback |
| Modal | confirm, form | Admin delete confirmations |
| Avatar | circle, square | Hero, profile |

### Composite (Must-Have)
| Component | Built From | Used In |
|---|---|---|
| Project Card | Card + Image + Chip + Button | Home, Projects |
| Skill Chip | Chip + Icon | Skills section |
| Education Card | Card + Stat | Home, Education |
| Stat Card | Card + Big Number | Admin Dashboard |
| Gallery | Image + Thumbnails | Project Detail |
| Admin Form | Input + Label + Button + Alert | Admin CRUD |

### Deferred (V0.7+)
- Toast notifications
- Markdown renderer
- Pagination
- Filter bar (client-side)
- Skeleton loaders (V0.9)
- Tabs

---

## 9. Component States

Every interactive element must define these states:

| State | Visual Change |
|---|---|
| Default | Base styling |
| Hover | Background darkens 5%, cursor pointer |
| Focus | 2px outline in primary color, offset 2px |
| Active | Background darkens 10%, slight scale |
| Disabled | Opacity 50%, cursor not-allowed |
| Loading | Spinner or skeleton, opacity 70% |

**Accessibility rule:** Focus states are **mandatory**. Never remove outlines.

---

## 10. Dark Mode Specification

**Strategy:** `prefers-color-scheme` + manual override stored in `localStorage`.

**Implementation:** CSS variables swap via `[data-theme="dark"]` attribute on `<html>`.

| Token | Light | Dark |
|---|---|---|
| `--bg-page` | `#F8FAFC` (Slate 50) | `#0F172A` (Slate 900) |
| `--bg-card` | `#FFFFFF` | `#1E293B` (Slate 800) |
| `--bg-elevated` | `#FFFFFF` | `#334155` (Slate 700) |
| `--text-primary` | `#0F172A` | `#F8FAFC` |
| `--text-secondary` | `#475569` | `#CBD5E1` |
| `--text-muted` | `#64748B` | `#94A3B8` |
| `--border` | `#E2E8F0` | `#334155` |
| `--primary` | *(from palette)* | *(brighter variant)* |

**Primary shift in dark mode:** Lighten the primary color by 1 step (e.g., Emerald 600 → Emerald 500) for better contrast on dark backgrounds.

**Shadows:** Reduce opacity by ~50% in dark mode. Prefer borders.

**Images:** Reduce brightness by 5% in dark mode for eye comfort.

---

## 11. Accessibility Targets

| Requirement | Target | How |
|---|---|---|
| Text contrast (body) | ≥ 4.5:1 | Check with WebAIM contrast checker |
| Text contrast (large) | ≥ 3:1 | Same |
| Interactive target size | ≥ 44×44px | Padding enforces |
| Focus visible | Always | Never `outline: none` |
| Color alone | Never conveys info | Pair with icon/text |
| Motion | Respects `prefers-reduced-motion` | Wrap animations in media query |
| Alt text | Every image | Required field in admin |

**WCAG 2.1 Level AA is the minimum.** Verify before shipping each component.

---

## 12. Layout Grid

| Breakpoint | Container Max | Columns |
|---|---|---|
| Mobile (≤ 640px) | 100% - 32px padding | 1 |
| Tablet (641–1024px) | 720px | 2 |
| Desktop (1025–1440px) | 1080px | 3 |
| Wide (≥ 1441px) | 1200px | 4 (project cards) |

**Container:** Auto-centered with `margin: 0 auto`.

---

## 13. Iconography

**Library:** Lucide Icons (SVG, tree-shakeable, MIT license).

**Sizes:** 16px (inline), 20px (buttons), 24px (headers), 32px (hero).

**Style:** Stroke-based, 2px weight, rounded caps. Consistent with minimal aesthetic.

**Colors:** Inherit from text. Never standalone colors (except brand logos in social links).

---

## 14. Motion & Animation

**Principle:** Motion should **help understanding**, not decorate.

| Element | Animation | Duration |
|---|---|---|
| Button hover | Background + translateY(-1px) | 150ms |
| Card hover | Shadow + translateY(-2px) | 200ms |
| Nav link hover | Underline slide-in | 200ms |
| Page fade-in | Opacity 0 → 1 | 300ms |
| Modal open | Scale 0.95 → 1 + opacity | 200ms |
| Scroll-triggered fade-in | IntersectionObserver | V0.9 |

**Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` (Material-style).

**Reduced motion:** All animations disabled when `prefers-reduced-motion: reduce`.

---

## 15. File Structure (CSS)

```
static/css/
├── main.css          → imports all below
├── tokens.css        → CSS variables (colors, spacing, fonts)
├── base.css          → reset, typography, elements
├── layout.css        → containers, grids, sections
├── components/
│   ├── buttons.css
│   ├── cards.css
│   ├── forms.css
│   ├── navbar.css
│   ├── footer.css
│   └── ...
└── themes/
    └── dark.css      → dark mode overrides
```

**Import order matters** — tokens first, then base, then components.

---

## 16. Design Tokens (CSS Variables Example)

Once palette is chosen, these become the source of truth:

```css
:root {
  /* Colors — example uses Palette B (Emerald) */
  --color-primary-50:  #ECFDF5;
  --color-primary-500: #10B981;
  --color-primary-600: #059669;
  --color-primary-700: #047857;

  --color-text-primary:   #0F172A;
  --color-text-secondary: #475569;
  --color-text-muted:     #64748B;

  --color-bg-page: #F8FAFC;
  --color-bg-card: #FFFFFF;
  --color-border:  #E2E8F0;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing */
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;

  /* Radius */
  --radius: 8px;
  --radius-lg: 12px;

  /* Shadow */
  --shadow: 0 1px 3px rgba(0,0,0,0.1);
}
```

**Every component references these tokens.** Changing `--color-primary-600` updates every button, link, and accent in the site.

---

## 17. DECISION REQUIRED

**Before Session 6, choose the palette:**

- [ ] **A. Technical Indigo** — safe, corporate, requires new photo
- [ ] **B. Data Emerald** ⭐ — distinctive, matches photo, recommended
- [ ] **C. AI Violet** — bold, requires new photo

**Also decide:**

- [ ] **Photo treatment** — depends on palette (see Section 2)
- [ ] **Font choices** — accept Inter + JetBrains Mono, or propose alternatives?
- [ ] **Icon library** — accept Lucide, or propose alternatives?

---

## 18. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — awaiting palette decision |