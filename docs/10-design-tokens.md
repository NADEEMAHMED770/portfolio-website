# Design Tokens

**Document:** 10-design-tokens.md
**Version:** 1.0
**Status:** Locked — Phase 1, Session 5
**Last Updated:** 2026-10-13
**Purpose:** Source of truth for all CSS variables

---

## 1. What Are Design Tokens?

Design tokens are **named variables** that store design decisions. Instead of hardcoding `#059669` in 20 files, we define `--color-primary-600` once. Change it in one place → updates everywhere.

**This document is the reference.** In V0.3 (design system implementation), these become `static/css/tokens.css`.

---

## 2. Color Tokens — Primary (Emerald)

```css
--color-primary-50:  #ECFDF5;
--color-primary-100: #D1FAE5;
--color-primary-200: #A7F3D0;
--color-primary-300: #6EE7B7;
--color-primary-400: #34D399;
--color-primary-500: #10B981;
--color-primary-600: #059669;   /* ← Brand anchor */
--color-primary-700: #047857;
--color-primary-800: #065F46;
--color-primary-900: #064E3B;
```

**Usage:**
| Token | Where |
|---|---|
| `--color-primary-50` | Light backgrounds, hover states |
| `--color-primary-500` | Dark mode brand color |
| `--color-primary-600` | Light mode brand, buttons, links |
| `--color-primary-700` | Button hover, active links |

---

## 3. Color Tokens — Neutrals (Slate)

```css
--color-slate-50:  #F8FAFC;
--color-slate-100: #F1F5F9;
--color-slate-200: #E2E8F0;
--color-slate-300: #CBD5E1;
--color-slate-400: #94A3B8;
--color-slate-500: #64748B;
--color-slate-600: #475569;
--color-slate-700: #334155;
--color-slate-800: #1E293B;
--color-slate-900: #0F172A;
--color-slate-950: #020617;
```

---

## 4. Color Tokens — Semantic

```css
--color-success: #10B981;   /* Emerald 500 */
--color-warning: #F59E0B;   /* Amber 500 */
--color-error:   #EF4444;   /* Red 500 */
--color-info:    #3B82F6;   /* Blue 500 */
```

---

## 5. Semantic Aliases (Theme-Aware)

These flip between light and dark mode. **Components reference these, not raw colors.**

```css
/* Light Mode (default) */
:root {
  /* Backgrounds */
  --bg-page:     var(--color-slate-50);
  --bg-card:     #FFFFFF;
  --bg-elevated: #FFFFFF;
  --bg-subtle:   var(--color-slate-100);

  /* Text */
  --text-primary:   var(--color-slate-900);
  --text-secondary: var(--color-slate-600);
  --text-muted:     var(--color-slate-500);
  --text-inverse:   #FFFFFF;

  /* Brand */
  --color-brand:        var(--color-primary-600);
  --color-brand-hover:  var(--color-primary-700);
  --color-brand-subtle: var(--color-primary-50);

  /* Borders */
  --border-default: var(--color-slate-200);
  --border-subtle:  var(--color-slate-100);
  --border-strong:  var(--color-slate-300);

  /* Interactive */
  --focus-ring: var(--color-primary-500);
}
```

```css
/* Dark Mode */
[data-theme="dark"] {
  /* Backgrounds */
  --bg-page:     var(--color-slate-900);
  --bg-card:     var(--color-slate-800);
  --bg-elevated: var(--color-slate-700);
  --bg-subtle:   var(--color-slate-800);

  /* Text */
  --text-primary:   var(--color-slate-50);
  --text-secondary: var(--color-slate-300);
  --text-muted:     var(--color-slate-400);
  --text-inverse:   var(--color-slate-900);

  /* Brand — brighter in dark mode for contrast */
  --color-brand:        var(--color-primary-500);
  --color-brand-hover:  var(--color-primary-400);
  --color-brand-subtle: rgba(16, 185, 129, 0.1);

  /* Borders */
  --border-default: var(--color-slate-700);
  --border-subtle:  var(--color-slate-800);
  --border-strong:  var(--color-slate-600);

  /* Interactive */
  --focus-ring: var(--color-primary-400);
}
```

---

## 6. Typography Tokens

```css
:root {
  /* Font families */
  --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Menlo, monospace;

  /* Font sizes — fluid via clamp() */
  --text-xs:   0.75rem;                                    /* 12px */
  --text-sm:   0.875rem;                                   /* 14px */
  --text-base: 1rem;                                       /* 16px */
  --text-lg:   clamp(1.0625rem, 1.05rem + 0.1vw, 1.125rem); /* 17–18px */
  --text-xl:   clamp(1.1875rem, 1.15rem + 0.2vw, 1.25rem);  /* 19–20px */
  --text-2xl:  clamp(1.375rem, 1.3rem + 0.4vw, 1.5rem);     /* 22–24px */
  --text-3xl:  clamp(1.625rem, 1.5rem + 0.6vw, 1.875rem);   /* 26–30px */
  --text-4xl:  clamp(1.875rem, 1.7rem + 0.9vw, 2.25rem);    /* 30–36px */
  --text-5xl:  clamp(2.125rem, 1.9rem + 1.1vw, 3rem);       /* 34–48px */

  /* Weights */
  --font-regular:  400;
  --font-medium:   500;
  --font-semibold: 600;
  --font-bold:     700;

  /* Line heights */
  --leading-tight:   1.2;   /* Headings */
  --leading-snug:    1.4;   /* Compact UI */
  --leading-normal:  1.6;   /* Body */
  --leading-relaxed: 1.75;  /* Long-form prose */

  /* Letter spacing */
  --tracking-tight:  -0.02em;   /* Headings */
  --tracking-normal: 0;         /* Body */
  --tracking-wide:   0.05em;    /* Uppercase labels */
}
```

---

## 7. Spacing Tokens

8px base grid.

```css
:root {
  --space-0:  0;
  --space-1:  0.25rem;  /* 4px */
  --space-2:  0.5rem;   /* 8px */
  --space-3:  0.75rem;  /* 12px */
  --space-4:  1rem;     /* 16px */
  --space-5:  1.25rem;  /* 20px */
  --space-6:  1.5rem;   /* 24px */
  --space-8:  2rem;     /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
}
```

---

## 8. Radius Tokens

```css
:root {
  --radius-sm:   4px;
  --radius-md:   8px;    /* Default — buttons, inputs, cards */
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;
}
```

---

## 9. Shadow Tokens

```css
:root {
  --shadow-sm:  0 1px 2px rgba(15, 23, 42, 0.05);
  --shadow-md:  0 4px 6px rgba(15, 23, 42, 0.07), 0 2px 4px rgba(15, 23, 42, 0.06);
  --shadow-lg:  0 10px 15px rgba(15, 23, 42, 0.1), 0 4px 6px rgba(15, 23, 42, 0.05);
  --shadow-xl:  0 20px 25px rgba(15, 23, 42, 0.1), 0 8px 10px rgba(15, 23, 42, 0.04);
}

[data-theme="dark"] {
  --shadow-sm:  0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md:  0 4px 6px rgba(0, 0, 0, 0.35);
  --shadow-lg:  0 10px 15px rgba(0, 0, 0, 0.4);
  --shadow-xl:  0 20px 25px rgba(0, 0, 0, 0.5);
}
```

---

## 10. Motion Tokens

```css
:root {
  /* Durations */
  --duration-fast:   150ms;
  --duration-normal: 200ms;
  --duration-slow:   300ms;

  /* Easing */
  --ease-in-out:   cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out:      cubic-bezier(0, 0, 0.2, 1);
  --ease-in:       cubic-bezier(0.4, 0, 1, 1);
  --ease-bounce:   cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast:   0ms;
    --duration-normal: 0ms;
    --duration-slow:   0ms;
  }
}
```

---

## 11. Layout Tokens

```css
:root {
  /* Container widths */
  --container-sm:  640px;
  --container-md:  768px;
  --container-lg:  1024px;
  --container-xl:  1280px;
  --container-2xl: 1440px;

  /* Content widths */
  --content-narrow:  720px;    /* Long-form reading */
  --content-default: 1080px;   /* Page content */
  --content-wide:    1280px;   /* Dashboards */

  /* Z-index scale */
  --z-base:     1;
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-overlay:  300;
  --z-modal:    400;
  --z-toast:    500;
  --z-tooltip:  600;
}
```

---

## 12. Font Loading (HTML)

Add to `<head>` in `base.html` (V0.2):

```html
<!-- Preconnect for performance -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**`display=swap`** → text renders immediately with fallback, then swaps to custom font when loaded. Prevents invisible text flash.

---

## 13. Complete `tokens.css` (Ready to Use)

When V0.3 ships, this is the full file:

```css
/* ============================================
   Design Tokens — Portfolio Website
   Auto-generated from docs/10-design-tokens.md
   ============================================ */

:root {
  /* --- Colors: Primary (Emerald) --- */
  --color-primary-50:  #ECFDF5;
  --color-primary-100: #D1FAE5;
  --color-primary-200: #A7F3D0;
  --color-primary-300: #6EE7B7;
  --color-primary-400: #34D399;
  --color-primary-500: #10B981;
  --color-primary-600: #059669;
  --color-primary-700: #047857;
  --color-primary-800: #065F46;
  --color-primary-900: #064E3B;

  /* --- Colors: Neutrals (Slate) --- */
  --color-slate-50:  #F8FAFC;
  --color-slate-100: #F1F5F9;
  --color-slate-200: #E2E8F0;
  --color-slate-300: #CBD5E1;
  --color-slate-400: #94A3B8;
  --color-slate-500: #64748B;
  --color-slate-600: #475569;
  --color-slate-700: #334155;
  --color-slate-800: #1E293B;
  --color-slate-900: #0F172A;
  --color-slate-950: #020617;

  /* --- Colors: Semantic --- */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error:   #EF4444;
  --color-info:    #3B82F6;

  /* --- Semantic Aliases (Light) --- */
  --bg-page:     var(--color-slate-50);
  --bg-card:     #FFFFFF;
  --bg-elevated: #FFFFFF;
  --bg-subtle:   var(--color-slate-100);
  --text-primary:   var(--color-slate-900);
  --text-secondary: var(--color-slate-600);
  --text-muted:     var(--color-slate-500);
  --text-inverse:   #FFFFFF;
  --color-brand:        var(--color-primary-600);
  --color-brand-hover:  var(--color-primary-700);
  --color-brand-subtle: var(--color-primary-50);
  --border-default: var(--color-slate-200);
  --border-subtle:  var(--color-slate-100);
  --border-strong:  var(--color-slate-300);
  --focus-ring: var(--color-primary-500);

  /* --- Typography --- */
  --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Menlo, monospace;

  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   clamp(1.0625rem, 1.05rem + 0.1vw, 1.125rem);
  --text-xl:   clamp(1.1875rem, 1.15rem + 0.2vw, 1.25rem);
  --text-2xl:  clamp(1.375rem, 1.3rem + 0.4vw, 1.5rem);
  --text-3xl:  clamp(1.625rem, 1.5rem + 0.6vw, 1.875rem);
  --text-4xl:  clamp(1.875rem, 1.7rem + 0.9vw, 2.25rem);
  --text-5xl:  clamp(2.125rem, 1.9rem + 1.1vw, 3rem);

  --font-regular:  400;
  --font-medium:   500;
  --font-semibold: 600;
  --font-bold:     700;

  --leading-tight:   1.2;
  --leading-snug:    1.4;
  --leading-normal:  1.6;
  --leading-relaxed: 1.75;

  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.05em;

  /* --- Spacing --- */
  --space-0:  0;
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;

  /* --- Radius --- */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
  --shadow-md: 0 4px 6px rgba(15, 23, 42, 0.07), 0 2px 4px rgba(15, 23, 42, 0.06);
  --shadow-lg: 0 10px 15px rgba(15, 23, 42, 0.1), 0 4px 6px rgba(15, 23, 42, 0.05);
  --shadow-xl: 0 20px 25px rgba(15, 23, 42, 0.1), 0 8px 10px rgba(15, 23, 42, 0.04);

  /* --- Motion --- */
  --duration-fast:   150ms;
  --duration-normal: 200ms;
  --duration-slow:   300ms;
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out:    cubic-bezier(0, 0, 0.2, 1);
  --ease-in:     cubic-bezier(0.4, 0, 1, 1);
  --ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  /* --- Layout --- */
  --container-sm:  640px;
  --container-md:  768px;
  --container-lg:  1024px;
  --container-xl:  1280px;
  --content-narrow:  720px;
  --content-default: 1080px;
  --content-wide:    1280px;

  --z-base:     1;
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-overlay:  300;
  --z-modal:    400;
  --z-toast:    500;
  --z-tooltip:  600;
}

/* ============================================
   Dark Mode Overrides
   ============================================ */

[data-theme="dark"] {
  --bg-page:     var(--color-slate-900);
  --bg-card:     var(--color-slate-800);
  --bg-elevated: var(--color-slate-700);
  --bg-subtle:   var(--color-slate-800);

  --text-primary:   var(--color-slate-50);
  --text-secondary: var(--color-slate-300);
  --text-muted:     var(--color-slate-400);
  --text-inverse:   var(--color-slate-900);

  --color-brand:        var(--color-primary-500);
  --color-brand-hover:  var(--color-primary-400);
  --color-brand-subtle: rgba(16, 185, 129, 0.1);

  --border-default: var(--color-slate-700);
  --border-subtle:  var(--color-slate-800);
  --border-strong:  var(--color-slate-600);

  --focus-ring: var(--color-primary-400);

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.35);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.4);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.5);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast:   0ms;
    --duration-normal: 0ms;
    --duration-slow:   0ms;
  }
}
```

---

## 14. Usage Examples

**Button:**

```css
.btn-primary {
  background: var(--color-brand);
  color: var(--text-inverse);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-family: var(--font-sans);
  font-weight: var(--font-semibold);
  font-size: var(--text-base);
  transition: background var(--duration-fast) var(--ease-in-out);
}
.btn-primary:hover { background: var(--color-brand-hover); }
```

**Card:**

```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
}
```

**Section:**

```css
.section {
  padding: var(--space-16) 0;
  background: var(--bg-page);
}
```

Notice: **no hardcoded colors, sizes, or spacing.** Everything references a token.

---

## 15. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — locked with Emerald palette, Inter + JetBrains Mono, Lucide icons |