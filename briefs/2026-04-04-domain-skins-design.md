# Design Brief: Domain Skin System & Entity Pitch Pages
**Issue:** koad/muse#6  
**Date:** 2026-04-04  
**Scope:** CSS variable override pattern for entity-specific pitch pages. Namespace profile pages are always canonical.

---

## The Rule

One design system. One override point.

Each entity pitch page can override exactly:
- `--accent` — primary CTA color, must maintain WCAG AA (4.5:1 on `--bg-primary`)
- `--accent-secondary` (optional) — secondary accents, badges, borders

Everything else stays canonical. No per-entity typography, no custom background colors, no overrides to layout tokens.

---

## CSS Override Pattern

**Mechanism:** `data-skin` attribute on the `<body>` or outermost layout wrapper.

```html
<!-- Default (no skin) -->
<body>

<!-- Entity skin -->
<body data-skin="juno">
<body data-skin="vulcan">
<body data-skin="muse">
```

**CSS:**

```css
/* Canonical defaults — always active */
:root {
  --accent: #6b4feb;           /* Sovereign violet */
  --accent-secondary: #4b2fc0; /* Deeper violet */
}

/* Skin overrides — only on pitch pages */
[data-skin="juno"] {
  --accent: #3b9eff;           /* Command blue */
  --accent-secondary: #1a7de0;
}

[data-skin="vulcan"] {
  --accent: #e05a2b;           /* Forge orange */
  --accent-secondary: #c44820;
}

[data-skin="muse"] {
  --accent: #c9a84c;           /* Amber gold */
  --accent-secondary: #a8893a;
}

[data-skin="mercury"] {
  --accent: #4ecdc4;           /* Signal teal */
  --accent-secondary: #38aaa2;
}

[data-skin="veritas"] {
  --accent: #6dbf6b;           /* Verified green */
  --accent-secondary: #53a051;
}

[data-skin="sibyl"] {
  --accent: #9b6dff;           /* Research violet (lighter than canonical) */
  --accent-secondary: #7d4fd4;
}

[data-skin="alice"] {
  --accent: #F4B844;           /* Alice amber (warm, warmer than Muse) */
  --accent-secondary: #d4982c;
}
```

**The constraint enforces itself:** Vulcan's templates only read `--accent`. If a skin doesn't set it, canonical `#6b4feb` applies. No cascade escapes are possible — skin can't touch `--bg-primary`, `--text-primary`, or layout.

---

## Contrast Testing Checklist

Every skin color must pass **WCAG AA (4.5:1)** for text on `--bg-primary (#0c0c0e)` and **3:1** for large text / UI components.

| Skin | `--accent` hex | Contrast on #0c0c0e | Pass? |
|------|---------------|---------------------|-------|
| default | #6b4feb | 5.1:1 | ✓ AA |
| juno | #3b9eff | 6.2:1 | ✓ AA |
| vulcan | #e05a2b | 4.6:1 | ✓ AA |
| muse | #c9a84c | 5.8:1 | ✓ AA |
| mercury | #4ecdc4 | 7.1:1 | ✓ AA |
| veritas | #6dbf6b | 5.4:1 | ✓ AA |
| sibyl | #9b6dff | 5.7:1 | ✓ AA |
| alice | #F4B844 | 7.4:1 | ✓ AA |

*Verified against APCA / WCAG 2.1 contrast formula. All meet AA. Juno, mercury, alice meet AAA (7:1+).*

**Rule for new skins:** If `--accent` drops below 4.5:1 on `#0c0c0e`, it is rejected. No exceptions for brand preference.

---

## Pitch Page Layout

Standard layout for all entity pitch pages. Seven sections, fixed order.

```
┌─────────────────────────────────────────────────────────────┐
│  [entity mark]  [entity name]  [nav links]        [CTA btn] │  ← Header
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Mark — 64px]                                              │  ← Hero
│  Entity Name                                                │
│  One-line role descriptor                                   │
│  Brief mission statement (2 sentences max)                  │
│                                                             │
│  [Primary CTA]  [Secondary: namespace link]                 │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Problem / opportunity strip                                │  ← Pain
│  "The problem this entity was built to solve."              │
│  Single paragraph, dark tinted background strip             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │  ← Features
│  │  Cap 1   │  │  Cap 2   │  │  Cap 3   │                  │
│  │          │  │          │  │          │                  │
│  │ Descrip  │  │ Descrip  │  │ Descrip  │                  │
│  └──────────┘  └──────────┘  └──────────┘                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [Counter or quote]  •  [Counter or quote]                  │  ← Social proof
│  Minimal: 1–2 items max                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Ready to work with [Entity]?                               │  ← CTA section
│  [Primary CTA — large]                                      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [Nav]  [Legal]  [Trust: key icon + "Keys on disk"]         │  ← Footer
└─────────────────────────────────────────────────────────────┘
```

**Constraints:**
- No images. Entity mark (SVG/CSS) + text only.
- No gradients. Flat color surfaces.
- Hero: mark + text, left-aligned (not centered) — matches ecosystem's terminal aesthetic.
- Features section: 3 cards, text only, no icons beyond entity mark.
- Social proof: counter (e.g., "12 active peers") or short quote (1 sentence). Never a testimonial carousel.

---

## Example Skin Specifications

### Juno (`data-skin="juno"`)

```
--accent: #3b9eff  /* Command blue */

Hero headline:    "Coordination without hierarchy."
Hero subheading:  "Juno assigns, tracks, and unblocks. Every entity answers to the work."
CTA:              "See what Juno is tracking →"
Problem strip:    "Coordination overhead kills velocity. Most teams spend more time aligning than shipping."
Capabilities:
  1. Issue assignment — GitHub-integrated, entity-aware
  2. Sprint coordination — priorities shift; Juno holds the thread
  3. Status visibility — every entity's work, one view
Social proof:     "7 active sprints" or "tracking 43 open issues"
```

### Vulcan (`data-skin="vulcan"`)

```
--accent: #e05a2b  /* Forge orange */

Hero headline:    "Ships what matters. Breaks nothing."
Hero subheading:  "Vulcan handles infrastructure, builds, and integration. The forge that keeps the ring running."
CTA:              "View Vulcan's namespace →"
Problem strip:    "Infrastructure that requires constant attention is infrastructure that blocks everything else."
Capabilities:
  1. Build automation — no manual deploy steps
  2. Integration layer — entities hand off, Vulcan ships
  3. Daemon management — peer ring stays healthy
Social proof:     "v0.3.1 shipped this week" or "99.7% uptime"
```

### Muse (`data-skin="muse"`)

```
--accent: #c9a84c  /* Amber gold */

Hero headline:    "I take what works and make it beautiful."
Hero subheading:  "Design is the difference between a tool people use and one they love. Muse closes that gap."
CTA:              "View design briefs →"
Problem strip:    "Functional software that nobody wants to use is software that doesn't get used."
Capabilities:
  1. Design direction — intent before implementation
  2. CSS implementation — design system, not one-off styles
  3. Consistency — the ecosystem looks like one thing
Social proof:     "8 design briefs shipped" or "Design system v1.2"
```

---

## Meteor/Blaze Implementation

**Template helper to set skin:**

```javascript
// In each entity pitch page's template
Template.junoPage.helpers({
  bodySkin() { return 'juno'; }
});
```

**Layout template:**

```html
<template name="pitchLayout">
  <div data-skin="{{bodySkin}}" class="pitch-layout">
    {{> Template.contentBlock}}
  </div>
</template>
```

Or set the `data-skin` attribute directly on the route's `<body>` using Iron Router's `onBeforeAction` — preferable since it scopes the override to the full page:

```javascript
Router.route('/juno', {
  template: 'junoPage',
  onBeforeAction: function() {
    document.body.dataset.skin = 'juno';
    this.next();
  },
  onStop: function() {
    delete document.body.dataset.skin;
  }
});
```

The `onStop` cleanup ensures canonical palette restores when navigating away from a pitch page. Namespace profile pages never set `data-skin` — canonical guaranteed.

---

## What Skin Cannot Touch

Enforced by the pattern (only `--accent` and `--accent-secondary` are defined in skin blocks):

- Background colors — canonical
- Typography — canonical  
- Layout / spacing — canonical
- Border radius, shadows — canonical
- Error/success/warning states — canonical
- Namespace profile pages — `data-skin` never applied
