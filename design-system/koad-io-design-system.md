# koad:io Design System

**Version:** 1.1  
**Author:** Muse (UI Beauty Entity)  
**Date:** 2026-04-04  
**Status:** Reference Guide  
**Audience:** All design and frontend implementation

**Changelog:**
- v1.1 (2026-04-04): Alice domain skin formalized; philosophy updated to reflect Faber's Alice-first funnel pivot (STRATEGY.md) and Iris positioning audit; conversational UI component patterns added.

---

## I. Design Philosophy

### Core Positioning: Sovereignty by Hardware

**The Shift (Q1 2026):**
- ~~Cryptographic identity is our differentiator~~ → _Hardware-resident keys are our differentiator_
- **New emphasis:** Decentralized. Hardware-resident. Owner-controlled. No vendor lock-in.
- **Visual metaphor:** Not a SaaS dashboard. A digital passport. Not flashy. Trusted.

**Canonical positioning statement (Iris, 2026-04-04):**
> koad:io is an open-source framework for running AI entities as git repos on your own hardware — where governance, memory, and trust bonds live on your disk and no platform mediates them.

**What this means for visual design:** The interface should communicate ownership and permanence. Not ephemeral SaaS. Not cloud-managed. The user's entity exists on their machine and the UI should feel like it belongs there too.

### Alice-First Entry Point (Faber STRATEGY.md, 2026-04-04)

Alice is the top-of-funnel product. She is not the infrastructure — she is the guide to it. The first thing a stranger experiences on kingofalldata.com is Alice: warm, patient, personal.

**Design implications:**
- Alice's interface is deliberately softer than the broader koad:io system — warmer colors, conversational spacing, no technical intimidation
- The infrastructure story (keys, governance, trust bonds) comes after Alice earns trust, not before
- Alice has her own domain skin (see Section XV) — do not apply the main violet/purple accent palette to Alice's UI
- "Come meet Alice" should feel like meeting a person, not installing software

**What NOT to lead with visually (Iris, 2026-04-04):**
- ❌ "Not your keys, not your agent" in hero copy or hero-adjacent UI — earns confusion before conviction. Save for users who already understand the architecture.
- ❌ "Sovereign AI" as a label — not ownable, sounds abstract
- ❌ Sovereign web / rings / Dark Passenger — not shipped, creates expectation debt
- ✓ Alice's name and warmth first; credentials and proof points second

### Visual Language

**Aesthetic:** Terminal-adjacent minimalism with sovereign elegance.
- **Mood:** Trustworthy, technical, confident — not cold or corporate
- **Tone:** The interface disappears; the user's identity is paramount
- **Inspiration:** Hardware wallets, SSH clients, cryptographic proof systems

**Alice exception:** Alice's specific aesthetic is warm and conversational. Her palette and spacing are intentionally softer. See Section XV.

### Beauty Principle

Beauty in koad:io is not decoration. It is:
- Information hierarchy that respects the user's time
- Spacing that communicates structure without noise
- Typography that treats technical data (keys, hashes) with respect
- Dark theme that is readable for extended use
- Mobile-first layouts that work everywhere without compromise

---

## II. Color System

### Dark Mode (Primary)

All color values use CSS custom properties. Dark mode is the default for koad:io products.

```css
/* Backgrounds */
--color-bg-primary:      #0c0c0e;  /* Near-black, slight blue undertone */
--color-bg-secondary:    #141418;  /* Card, panel backgrounds */
--color-bg-tertiary:     #1c1c22;  /* Elevated surfaces, inputs, modals */
--color-bg-hover:        #242429;  /* Interactive hover states */
--color-bg-active:       #2a2a32;  /* Pressed, active states */

/* Borders & Dividers */
--color-border-subtle:   #1f1f27;  /* Very subtle dividers */
--color-border-default:  #2a2a32;  /* Default borders, dividers */
--color-border-strong:   #3a3a44;  /* Emphasized borders, focus rings */

/* Text */
--color-text-primary:    #e8e8ec;  /* Primary text, headings */
--color-text-secondary:  #8888a0;  /* Secondary text, labels, hints */
--color-text-muted:      #64647c;  /* Tertiary text, very low contrast */
--color-text-inverse:    #0c0c0e;  /* Text on light backgrounds */

/* Semantic Colors */
--color-accent:          #7c6aff;  /* Primary CTA, active states, highlights */
--color-accent-subtle:   #7c6aff20; /* Subtle accent backgrounds */
--color-accent-glow:     #7c6aff40; /* Glow effects, overlays */

--color-success:         #4ade80;  /* Verification, trust confirmed */
--color-success-subtle:  #4ade8020;

--color-warning:         #fbbf24;  /* Caution, attention required */
--color-warning-subtle:  #fbbf2420;

--color-error:           #f87171;  /* Errors, critical states */
--color-error-subtle:    #f8717120;

--color-info:            #60a5fa;  /* Informational, status updates */
--color-info-subtle:     #60a5fa20;
```

### Light Mode (Secondary)

Light mode is available but dark mode is canonical. Light mode uses the same variable names, overridden in `[data-theme="light"]`.

```css
[data-theme="light"] {
  --color-bg-primary:      #fafafa;
  --color-bg-secondary:    #ffffff;
  --color-bg-tertiary:     #f0f0f2;
  --color-bg-hover:        #efefef;
  --color-bg-active:       #e8e8ec;
  
  --color-border-subtle:   #f0f0f2;
  --color-border-default:  #e0e0e4;
  --color-border-strong:   #c8c8d0;
  
  --color-text-primary:    #18181c;
  --color-text-secondary:  #6b6b80;
  --color-text-muted:      #a0a0b0;
  --color-text-inverse:    #ffffff;
  
  --color-accent:          #6b4feb;  /* Darker for contrast */
  --color-accent-subtle:   #6b4feb15;
  --color-accent-glow:     #6b4feb25;
  
  --color-success:         #3a9d4d;
  --color-success-subtle:  #3a9d4d15;
  
  --color-warning:         #d97706;
  --color-warning-subtle:  #d9770615;
  
  --color-error:           #dc2626;
  --color-error-subtle:    #dc262615;
  
  --color-info:            #0284c7;
  --color-info-subtle:     #0284c715;
}
```

### Domain Skin Overrides

Domain skins (entity pitch pages) may override `--color-accent` and optionally `--color-accent-secondary`. This allows visual differentiation on root pages while keeping namespace profile pages consistent.

**Constraint:** Accent colors must maintain WCAG AA contrast with both `--color-bg-primary` and `--color-text-primary`.

### Contrast Checklist

- ✓ `--color-text-primary` on `--color-bg-primary`: 15:1 (AAA)
- ✓ `--color-text-secondary` on `--color-bg-primary`: 4.8:1 (AA)
- ✓ `--color-accent` on `--color-bg-primary`: 4.5:1 (AA)
- ✓ All accent colors tested on both primary and tertiary backgrounds

---

## III. Typography System

### Typeface Selection

| Role | Typeface | Rationale |
|------|----------|-----------|
| **Keys, hashes, technical data** | JetBrains Mono or IBM Plex Mono | Monospace respects cryptographic identity; each character distinct |
| **Headings, labels, UI chrome** | Inter 600–700 | Humanist sans-serif, excellent legibility, accessible |
| **Body copy, descriptions** | Inter 400 | Clean, readable, web-optimized |

**Font loading:** System fonts first (fallback to `-apple-system, BlinkMacSystemFont`), then Inter + JetBrains Mono via self-hosted CDN (not Google Fonts — no external dependency).

### Scale & Rhythm

Base font size: **14px**  
Line height: **1.5** (21px) for body copy, **1.3** (18px) for headings  
Letter spacing: Standard, except monospace data (+0.02em)

```css
/* Heading hierarchy */
--font-h1: 2rem (32px);     /* Page titles, hero headlines */
--font-h2: 1.5rem (24px);   /* Section titles */
--font-h3: 1.25rem (20px);  /* Subsection titles */
--font-h4: 1.125rem (18px); /* Component titles */
--font-body: 0.875rem (14px); /* Default body, UI text */
--font-sm: 0.75rem (12px);  /* Labels, captions, small UI */

/* Weight system */
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Monospace variants */
--font-mono-body: 0.85rem (12px) JetBrains Mono; /* Keys, fingerprints */
--font-mono-label: 0.75rem (11px) JetBrains Mono; /* Hash previews */
```

### Typography Patterns

**Namespace identifiers** (usernames, keys)  
- Font: `--font-mono-body`
- Color: `--color-text-secondary`
- Example: `alice.kingofalldata.com`

**Sensitive data** (public key fingerprints, signatures)  
- Font: `--font-mono-body`
- Color: `--color-text-primary`
- Announce to screen readers as "monospace" to ensure proper pronunciation
- Example: `AAAA-1234-5678-9ABC-DEFG`

**Call-to-action copy**  
- Font: Inter 600
- Color: `--color-text-primary` on `--color-accent` background
- No all-caps (except abbreviations: GitHub, PWA, etc.)

---

## IV. Spacing System

Spacing uses an 8px base unit for consistency across all dimensions.

```css
/* Spacing scale */
--space-0: 0;
--space-1: 0.25rem (4px);
--space-2: 0.5rem (8px);    /* Base unit */
--space-3: 0.75rem (12px);
--space-4: 1rem (16px);
--space-5: 1.25rem (20px);
--space-6: 1.5rem (24px);
--space-8: 2rem (32px);
--space-10: 2.5rem (40px);
--space-12: 3rem (48px);
--space-16: 4rem (64px);
```

### Padding

**Buttons & form inputs:** `--space-4` vertical, `--space-6` horizontal  
**Cards & panels:** `--space-6` all sides  
**List items:** `--space-4` vertical, `--space-6` horizontal  
**Page sections:** `--space-16` top/bottom (mobile: `--space-12`)  

### Margins

**Between sections:** `--space-16` (mobile: `--space-12`)  
**Between subsections:** `--space-8`  
**Between list items:** `--space-4`  
**Text hierarchy gap:** `--space-2` to `--space-4`  

### Grid & Columns

**Maximum content width:** 1200px (comfortable reading, not stretched)  
**Sidebar width:** 240px (desktop)  
**Gutter:** `--space-6` between columns  

**Responsive breakpoints:**
- `xs: 0px` — Mobile baseline
- `sm: 640px` — Small tablet
- `md: 768px` — Tablet, sidebar appears
- `lg: 1024px` — Desktop
- `xl: 1280px` — Large desktop

---

## V. Component System

### Button

**Variants:**
- **Primary:** Background `--color-accent`, text white, full-width on mobile
- **Secondary:** Border `--color-border-default`, text `--color-text-primary`
- **Tertiary/Text:** No background, text `--color-accent`, underline on hover
- **Danger:** Background `--color-error`, text white

**Sizing:**
- **Large:** `--space-4` vertical, `--space-8` horizontal (primary CTAs)
- **Default:** `--space-3` vertical, `--space-6` horizontal (most buttons)
- **Small:** `--space-2` vertical, `--space-4` horizontal (inline actions)

**Touch target minimum:** 44x44px (all buttons on mobile)

**Interactive states:**
- **Hover:** Brightness +10%, subtle shadow
- **Active/Pressed:** Brightness -10%, no shadow
- **Disabled:** Opacity 50%, cursor `not-allowed`
- **Focus:** `--color-border-strong` outline, 2px, offset 2px

### Input Fields

**Container:** Background `--color-bg-tertiary`, border `--color-border-default`, 8px radius

**Padding:** `--space-3` vertical, `--space-4` horizontal

**Focus state:** Border `--color-border-strong` (2px), outline `--color-accent` (1px, offset 2px)

**Error state:** Border `--color-error` (2px), helper text in `--color-error`

**Label:** `--font-sm`, `--color-text-secondary`, above input, margin-bottom `--space-2`

**Placeholder:** `--color-text-muted`, no opacity change (keep at 1.0 for readability)

### Cards

**Background:** `--color-bg-secondary`  
**Border:** 1px `--color-border-default`  
**Padding:** `--space-6`  
**Border-radius:** 8px  
**Shadow:** Subtle elevation (0 4px 12px rgba(0,0,0,0.3)) for interactive cards only

**Hover state (interactive):** Border `--color-border-strong`, transform: translateY(-2px), shadow increase

### Badges & Status Indicators

**Verified/Success:**
- Background: `--color-success-subtle`
- Border: 1px `--color-success`
- Text: `--color-success` (bold)
- Icon: Checkmark (16px)
- Example: "Key verified" on trust bonds

**Pending/Unverified:**
- Background: `--color-warning-subtle`
- Border: 1px `--color-warning`
- Text: `--color-warning`
- Icon: Clock (16px)

**Online/Presence:**
- Indicator: 8px circle, `--color-success`, positioned absolute
- With timestamp: "2m ago", `--color-text-secondary`

### Conversational UI (Alice PWA)

Message bubbles, typing indicators, and progress tracks for the Alice conversation interface.

**Message bubbles:**
- Max width: 82% mobile, 72% desktop (sm+)
- Alice messages: Background `--alice-surface`, border `--alice-border`, `border-bottom-left-radius: 2px` (tail)
- Human messages: Warm dark background (derive from `--alice-accent` hue at very low lightness), `border-bottom-right-radius: 2px`
- Font: 0.95rem, line-height 1.6
- Sender label: 0.75rem, uppercase, letter-spacing 0.04em; Alice in `--alice-accent`, human in muted

**Typing indicator:**
- Three dots, `typingPulse` animation (opacity + scale), 1.2s cycle, staggered 0.2s delays
- Same bubble style as Alice messages
- Always appears inline in the conversation flow, not floating

**Progress bar (Journey screen):**
- Height: 2px (minimal, not intrusive)
- Track: `--alice-border`
- Fill: `--alice-accent`, animated width transition 0.4s ease
- Placed above the level list, below the heading — visual anchor, not decoration

**Level list items:**
- Three states: `complete` (opacity 0.65, restores on hover), `active` (surface background, border visible), `locked` (opacity 0.35, cursor default)
- Gap between items: 2px — almost flush, feels like a tight list not a card grid
- Padding: 0.875rem vertical, 1rem horizontal
- Touch target: Ensure full row is interactive, not just text

**Certificate block:**
- Border-top accent stripe (3px `--alice-accent`) signals authority/signature
- GPG signature: `--alice-mono`, very small (0.65rem) — acceptable for cryptographic data but offer "copy" affordance
- Background slightly elevated from card background

**IMPORTANT — `prefers-reduced-motion`:**
All conversational animations (`messageIn`, `typingPulse`, `starPulse`, `fadeIn`) must be suppressed when `prefers-reduced-motion: reduce` is set. Use the global reset pattern from Section VIII:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Navigation

**Tabs (horizontal):**
- Inactive: Text `--color-text-secondary`, underline none
- Active: Text `--color-text-primary`, underline `--color-accent` (2px, offset -2px)
- Interaction: Click to activate, instant (no fade)

**Sidebar (desktop):**
- Background: `--color-bg-secondary`
- Item padding: `--space-3` vertical, `--space-4` horizontal
- Inactive: Text `--color-text-secondary`
- Active: Background `--color-bg-active`, text `--color-accent`
- Icon + text, 24px icons

---

## VI. Animation & Motion

### Principles

- **Purposeful:** Every animation conveys state change or guides attention
- **Respects preference:** `prefers-reduced-motion` → no animations (instant transitions only)
- **Fast:** 150–300ms for most interactions, never > 500ms
- **Easing:** `ease-out` for enters, `ease-in-out` for continuous

### Standard Animations

**Fade in/out**
- Duration: 200ms
- Easing: `ease-out`
- Example: Loading skeletons → content

**Slide up** (drawer/modal enter)
- Duration: 250ms
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (spring-like)

**Scale** (button press feedback)
- Duration: 150ms
- Range: 100% → 98% → 100%
- Easing: `ease-in-out`

**Color transition** (hover/focus state changes)
- Duration: 150ms
- Easing: `ease-out`
- Example: Button border color change on focus

### Avoid

- ❌ Carousel auto-play animations
- ❌ Parallax scrolling
- ❌ Decorative animations without purpose
- ❌ Animations that loop infinitely (except loading spinners, use sparingly)

---

## VII. Accessibility

### Standards

All koad:io products meet **WCAG 2.1 AA** minimum. AAA compliance preferred where feasible.

### Color & Contrast

- Foreground-to-background contrast: 4.5:1 minimum for small text, 3:1 for large (18px+)
- Do not communicate state via color alone (always include icon, text, or pattern)
- Color palette tested against deuteranopia (green-blind) and protanopia (red-blind) simulators

### Focus Management

- Visible focus indicator on all interactive elements: `outline: 2px solid --color-border-strong`
- Focus order follows DOM order (no tabindex jumps unless necessary)
- Skip link to main content (visible on focus)
- Modal dialogs trap focus within, restore on dismiss

### Motion

- Respect `prefers-reduced-motion: reduce` — replace animations with instant transitions
- No auto-playing videos
- No flashing content (> 3 flashes per second)

### Semantics

- Use semantic HTML: `<button>`, `<nav>`, `<main>`, `<article>`, `<section>`
- Form labels explicitly associated: `<label for="input-id">`
- Headings in logical order (h1 → h2 → h3, no skips)
- Image alt text: "Alice's avatar" (descriptive), not "pic1.jpg"
- Key fingerprints announced as monospace to screen readers

### Testing

Automated tools (axe, Lighthouse) + manual testing on:
- macOS + Safari + VoiceOver
- Windows + Firefox + NVDA
- Android + Chrome + TalkBack

---

## VIII. Implementation Guidelines

### CSS Architecture

**Structure:** Custom CSS with CSS custom properties (no Tailwind unless Vulcan has introduced it into the product).

**File organization:**
```
styles/
  ├── tokens.css          /* Color, typography, spacing variables */
  ├── global.css          /* Reset, base element styles */
  ├── components/
  │   ├── button.css
  │   ├── input.css
  │   ├── card.css
  │   └── ...
  ├── layout/
  │   ├── sidebar.css
  │   ├── grid.css
  │   └── responsive.css
  └── theme/
      ├── dark.css
      └── light.css
```

**Root variables:**
```css
:root {
  /* All color, spacing, typography variables from this design system */
  --color-bg-primary: #0c0c0e;
  --space-2: 0.5rem;
  /* ... */
}

[data-theme="light"] {
  /* Light mode overrides only */
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Blaze Template Patterns

**Component composition:**
```handlebars
{{> button 
  label="Provision Namespace" 
  variant="primary" 
  size="large"
  onClick=handleProvision
}}
```

**Class naming:** BEM convention at component level
```html
<div class="card card--interactive">
  <h3 class="card__title">Namespace</h3>
  <p class="card__description">alice.kingofalldata.com</p>
</div>
```

**Data attributes for state:**
```html
<button data-state="active" class="button">
  Sign in
</button>
```

### Dark Mode Setup

Dark mode is the default. Light mode is opt-in.

```html
<!-- HTML root attribute -->
<html data-theme="dark">

<!-- User preference toggle (stores in localStorage) -->
<script>
const userTheme = localStorage.getItem('theme') || 'dark';
document.documentElement.setAttribute('data-theme', userTheme);
</script>
```

---

## IX. Responsive Strategy

### Mobile-First Approach

All layouts start at mobile (320px). Breakpoints add complexity only as needed.

**Example:**
```css
.grid {
  display: grid;
  grid-template-columns: 1fr; /* Mobile: single column */
  gap: var(--space-6);
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: 1fr 1fr; /* sm: two columns */
  }
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: 1fr 1fr 1fr; /* md: three columns */
  }
}
```

### Touch Targets

Minimum 44×44px for all tappable elements. Spacing between adjacent targets: `--space-2` minimum.

### Overflow Handling

- Text truncation: Use `text-overflow: ellipsis` + `overflow: hidden` for single lines only
- Code/keys: Scrollable container with monospace font, `white-space: pre-wrap` for readability
- Tables: Horizontal scroll on mobile (`overflow-x: auto`)

### Images & Media

- WebP primary format, PNG fallback
- Lazy-load below-fold images: `loading="lazy"`
- SVG icons: Inline for single-use, sprite sheets for repeated icons
- Responsive images: `srcset` for 1x and 2x pixel densities

---

## X. Performance Targets

### Core Web Vitals

- **Largest Contentful Paint (LCP):** < 2.5s
- **First Input Delay (FID):** < 100ms
- **Cumulative Layout Shift (CLS):** < 0.1

### Bundle & Load Time

- **Initial CSS:** < 40kb (gzipped)
- **Initial JS:** < 150kb (gzipped)
- **Total page load:** < 3s (on 4G)

### Optimization Practices

- No blocking stylesheets in `<head>` (critical CSS inline, rest async)
- Font loading: `font-display: swap` (show fallback immediately)
- JavaScript: Code-split by route, lazy-load non-critical modules
- Images: Compress before upload, use WebP with fallbacks
- Icons: SVG sprite sheet or inline for < 1kb icons

---

## XI. Sovereignty Design Principles

### Hardware-Resident Keys: Visual Integrity

When displaying or referencing keys, hashes, or cryptographic identifiers:

1. **Always use monospace** — each character distinct
2. **Never abbreviate** without explicit user action (e.g., click to show full fingerprint)
3. **Copy action:** Clicking a key/hash displays "Copied!" toast adjacent, fades after 1.5s
4. **No masking** — show full public keys by default. Private keys never transmitted or stored in browser.

### Trust & Verification Visual Language

Trust bonds and key verification are core to koad:io. Visual patterns:

- **Unverified:** Border `--color-border-default`, text `--color-text-secondary`, no icon
- **Pending verification:** Badge with `--color-warning`, clock icon
- **Verified:** Border `--color-success`, badge with checkmark, `--color-success` text
- **Revoked/Expired:** Border `--color-error`, strike-through text, red X icon

### Decentralized Architecture: Navigation

The interface should never imply centralized authority:

- ❌ "Managed by us" language
- ❌ Vendor lock-in UI patterns (e.g., "You can't export your data")
- ✓ "Your namespace," "Your keys," "Self-hosted option"
- ✓ Clear export/portability paths in UI
- ✓ Open standards prominently featured

### Owner-Controlled Presentation

Users control their namespace presentation. Design reflects that:

- Namespace pages: User's avatar, user's bio, user's custom domain (if available)
- No platform branding on user-facing pages — only on root pitch pages
- Settings always visible and accessible
- Clear data ownership: "Only you can access your private keys"

---

## XII. Anti-Patterns

❌ Do not use these patterns on koad:io products:

- Decorative gradients (except as background texture, very subtle)
- Heavy drop shadows (max shadow: 0 4px 12px with low opacity)
- Carousels or hero sliders
- Stock photography
- Lightbox modals (use full-screen overlays or drawers instead)
- Sans-serif monospace (only use true monospace fonts for code)
- Rotating loading spinners (use pulse animations instead)
- Obfuscated or masked sensitive data by default
- "Free trial" / countdown timers (contrary to sovereignty message)
- Vendor lock-in copy ("only on our platform")

---

## XIII. Future Extensions

### Domain Skins

Each entity namespace can have a custom "skin" for their pitch page (root domain). Skins override:
- `--color-accent` (primary CTA color)
- Optional: `--color-accent-secondary`

Namespace profile pages remain on canonical palette.

**Canonical example:** Alice's skin at `kingofalldata.com` — see Section XV for full specification. Alice uses amber (`#F4B844`) instead of violet (`#7c6aff`), establishing that skin overrides extend beyond accent alone when the product's personality warrants it.

### Accessible Color Schemes

Future: Provide high-contrast and monochrome variants via `data-color-scheme` attribute (AAA compliance for vision-impaired users).

### Internationalization (i18n)

Typography scale may adjust for languages with complex scripts. RTL support planned.

---

## XV. Alice Domain Skin

Alice is the canonical example of a domain skin. She overrides the main koad:io violet palette with a warm amber — communicating warmth, patience, and personality. This is intentional: Alice is not infrastructure, she is a guide.

### Alice Palette

```css
/* Alice skin — warm amber, not violet */
--alice-accent:       #F4B844;  /* Warm amber — Alice's voice, CTA, active states */
--alice-accent-dark:  #E8A738;  /* Hover/pressed state of accent */

/* Backgrounds — warmer near-black, slight brown undertone */
--alice-bg:           #0a0a0a;  /* True near-black */
--alice-surface:      #111111;  /* Card/message backgrounds */
--alice-surface-2:    #161616;  /* Elevated surfaces */

/* Text */
--alice-text:         #f0ede5;  /* Slightly warm white — not pure #ffffff */
--alice-subtle:       #555555;  /* Secondary text, hints */

/* Borders */
--alice-border:       #2a2a2a;  /* Dividers, input borders */

/* Status */
--alice-success:      #8ac926;  /* Level complete, positive states */

/* Spacing */
--alice-spacing:      1.5rem;
--alice-spacing-sm:   0.75rem;
--alice-spacing-lg:   2.5rem;
--alice-line-height:  1.6;      /* Slightly more open than body — conversational rhythm */

/* Border radius */
--alice-radius:       6px;      /* Softer than 0px, less clinical than 12px */

/* Typography — system fonts acceptable for PWA (performance priority) */
--alice-font:         -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
--alice-mono:         "Space Mono", "JetBrains Mono", "Courier New", monospace;
```

### Human Message Bubble — Derived Colors

Do not hardcode `#1e1a10` or `#3a3020`. Derive from the accent hue:

```css
/* Human message bubble (warm-tinted dark) */
.message.human .message-bubble {
  background: color-mix(in srgb, var(--alice-accent) 8%, var(--alice-bg));
  border: 1px solid color-mix(in srgb, var(--alice-accent) 20%, var(--alice-border));
}
```

If `color-mix()` is not available (Safari < 16.2), use the fallback values `#1e1a10` / `#3a3020`, but document them as derived from amber at 8%/20% opacity over `#0a0a0a`.

Similarly for the exercise prompt, graduation-next panel, and completion card — all warm-tinted surfaces should derive from the accent, not be arbitrary hex values.

### Typography Decision — System Fonts vs. Inter

Alice uses system fonts intentionally:
- **Why:** Alice is a PWA. First-load performance is critical. System fonts eliminate a font request and any layout shift on load.
- **Acceptable trade-off:** Slight inconsistency with the broader koad:io Inter stack — Alice's conversational context does not require the precision of a dashboard.
- **Rule:** If Inter is already cached on the page (e.g., user came from a koad:io namespace page), Alice may inherit it. But Alice's CSS must not require it.

### What Alice Shares vs. What She Overrides

| Token | koad:io system | Alice skin |
|-------|---------------|------------|
| Primary accent | `#7c6aff` (violet) | `#F4B844` (amber) |
| BG primary | `#0c0c0e` | `#0a0a0a` |
| Text primary | `#e8e8ec` (cool white) | `#f0ede5` (warm white) |
| Border radius | 8px | 6px (slightly tighter) |
| Body font | Inter | System fonts |
| Monospace | JetBrains Mono | Space Mono (fallback acceptable) |
| Spacing scale | `--space-*` (8px base) | `--alice-spacing` (1.5rem base) |
| Line height | 1.5 | 1.6 (more open, conversational) |

### Scope of Alice Skin

Alice's amber skin applies to:
- `kingofalldata.com` — root domain and all Alice PWA screens
- Any future "Come meet Alice" landing pages

The amber skin does **not** apply to:
- Namespace profile pages (`*.kingofalldata.com`)
- The sponsor dashboard
- The Stream PWA operational dashboard
- Any page where the infrastructure (not Alice) is the subject

---

## XIV. Checklist for Designers & Developers

Before shipping any feature:

- [ ] Colors tested against contrast checklist (4.5:1 minimum)
- [ ] Spacing uses `--space-*` variables (no magic numbers)
- [ ] Interactive elements are ≥ 44×44px
- [ ] Focus states visible and keyboard-navigable
- [ ] Monospace used for keys/hashes, sans-serif for UI chrome
- [ ] Mobile layout tested on real device (not just DevTools)
- [ ] `prefers-reduced-motion` respected
- [ ] Images WebP with PNG fallback
- [ ] Alt text on all images, descriptive not generic
- [ ] Semantic HTML used throughout
- [ ] Performance budget checked: CSS < 40kb, JS < 150kb initial
- [ ] Dark mode default, light mode tested
- [ ] No platform branding on user-facing pages (unless pitch page)
- [ ] Copy reflects ownership language ("your namespace," not "managed by us")

---

## Appendix: Quick Reference

**Color Variables:**
```
--color-bg-primary, --color-bg-secondary, --color-bg-tertiary
--color-border-subtle, --color-border-default, --color-border-strong
--color-text-primary, --color-text-secondary, --color-text-muted
--color-accent, --color-success, --color-warning, --color-error, --color-info
```

**Spacing:**
```
--space-2: 8px (base)
--space-4: 16px
--space-6: 24px
--space-8: 32px
--space-12: 48px
--space-16: 64px
```

**Typography:**
```
--font-h1 (32px), --font-h2 (24px), --font-h3 (20px), --font-body (14px), --font-sm (12px)
--font-mono-body: JetBrains Mono 12px
```

**Breakpoints:**
```
sm: 640px | md: 768px | lg: 1024px | xl: 1280px
```

---

*Design System by Muse — the sovereignty-focused visual language for all koad:io products.*
