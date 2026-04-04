# UI Review: kingofalldata.com Alice PWA
**Date:** 2026-04-04  
**Author:** Muse  
**Source files:** `~/kingofalldata-dot-com/sites/kingofalldata.com/public/`  
**Issue:** koad/muse#3  
**Status:** Complete — pending Veritas review integration (koad/veritas#9)

---

## Context

This review covers the Alice PWA as delivered: a 6-screen single-page application (`index.html` + `alice.css`, ~1100 lines CSS). The product is Alice's 12-level sovereignty curriculum with conversation interface, journey tracker, graduation certificate, and blog. Reviewed against the koad:io design system v1.1 and Faber's Alice-first content strategy.

Note: koad requested holding this until Veritas's review (koad/veritas#9) returns. These refinements are written to be integrated after Veritas completes their findings. Anything Veritas flags about copy should be addressed before Muse's CSS refinements are applied.

---

## What's Working

Before refinements: the foundation is good. Document what to keep.

- **Conversational layout is correct.** The screen-based SPA pattern with full-height panels and a sticky header is the right architecture for Alice. Do not change it.
- **Dark aesthetic lands.** `#0a0a0a` background, warm text `#f0ede5`, amber `#F4B844` accent — the palette has coherence and warmth. Alice feels distinct from technical infrastructure.
- **Amber accent is right for Alice.** This should be formalized as Alice's domain skin (done in design system v1.1), not changed to the system violet.
- **Top accent bar (`alice-bar`, 3px amber stripe).** A good, subtle signal of identity. Keep it.
- **Safe area handling is correct.** `env(safe-area-inset-bottom)` on `.conversation-input` is done properly. Covers iPhone notch/home indicator.
- **Semantic HTML and ARIA roles.** Each screen has `role="main"` and `aria-label`. The conversation log has `aria-live="polite"`. The input has proper `aria-label`. This is solid.
- **PWA setup.** Manifest, service worker, apple-mobile-web-app metadata — complete.
- **Level states (complete/active/locked).** The three visual states are clear and communicate progression without explanation.
- **`messageIn` animation.** 200ms fade + 6px slide-up is the right speed and distance. Feels responsive, not theatrical.

---

## Refinements Required

Ordered by impact. P1 = ship-blocking. P2 = before launch. P3 = polish pass.

---

### P1 — Accessibility: Focus indicator removed on back button

**Location:** `alice.css:96-100`
```css
.screen-header .back-btn:hover,
.screen-header .back-btn:focus-visible {
  color: var(--alice-accent);
  outline: none;  ← problem
}
```

**Problem:** `outline: none` on `:focus-visible` removes the visible focus indicator for keyboard users. A sighted keyboard user pressing Tab to the back button gets no visual feedback.

**Fix:**
```css
.screen-header .back-btn:focus-visible {
  color: var(--alice-accent);
  outline: 2px solid var(--alice-accent);
  outline-offset: 2px;
  border-radius: 2px;
}
```

---

### P1 — Accessibility: Missing `prefers-reduced-motion` block

**Location:** `alice.css` — no `prefers-reduced-motion` media query anywhere

**Problem:** Four animations run unconditionally: `messageIn` (conversation bubbles), `typingPulse` (typing dots), `starPulse` (graduation star), `fadeIn`. Users with vestibular disorders or motion sensitivity get these animations regardless of system preference.

**Fix:** Add at end of `alice.css`:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

### P2 — Touch target: Send button below 44px minimum

**Location:** `alice.css:595-609`
```css
.btn-send {
  width: 42px;
  height: 42px;
  ...
}
```

**Problem:** 42px is below the 44px minimum touch target required by WCAG 2.5.5 (Level AA) and Apple HIG. Two pixels under spec.

**Fix:** `width: 44px; height: 44px;`

---

### P2 — Touch target: Back button has no minimum size

**Location:** `alice.css:83-100`

The `.back-btn` has `padding: 0.25rem 0` (4px vertical) and no minimum height. On mobile this creates a very small touch target — estimated ~30px height.

**Fix:**
```css
.screen-header .back-btn {
  min-height: 44px;
  padding: 0 0.5rem;
  display: flex;
  align-items: center;
}
```

---

### P2 — Magic color values: unmaintainable hardcoded hex

**Locations:**
- `alice.css:443-447` — Human message bubble: `background: #1e1a10; border: 1px solid #3a3020`
- `alice.css:503-511` — Exercise prompt: `background: #12100a; border: 1px solid #2a2510; color: #d4c89a`
- `alice.css:515-523` — Completion card: `background: #0e140a; border: 1px solid #1a2a10`
- `alice.css:740-748` — Graduation next panel: `background: #12100a; border: 1px solid #2a2510`

**Problem:** These are all warm-tinted dark surfaces derived from the amber accent, but they're hardcoded. If Alice's accent color changes, these won't update.

**Fix:** Replace with derived variables. Where `color-mix()` is available:
```css
.message.human .message-bubble {
  background: color-mix(in srgb, var(--alice-accent) 8%, var(--alice-bg));
  border: 1px solid color-mix(in srgb, var(--alice-accent) 18%, var(--alice-border));
}

.exercise-prompt {
  background: color-mix(in srgb, var(--alice-accent) 5%, var(--alice-bg));
  border: 1px solid color-mix(in srgb, var(--alice-accent) 12%, var(--alice-border));
  border-left: 3px solid var(--alice-accent);
}
```

Vulcan should check `color-mix()` browser support table before shipping. If Safari 16.1 support is needed, keep the hex fallbacks as comments with their derived values documented.

---

### P2 — Intro screen: CTA buttons not full-width on mobile

**Location:** `alice.css:170-184`
```css
.btn-primary {
  ...
  align-self: flex-start;  ← makes button shrink-to-content
}
```

**Problem:** Design system specifies primary CTAs are full-width on mobile. `align-self: flex-start` makes them auto-width. On the intro screen, "Let's begin ✦" and "Learn more about koad:io" should both span the full container width on mobile — it reads as more decisive and is easier to tap.

**Fix:**
```css
/* Mobile: full-width CTAs */
.intro-actions .btn-primary,
.intro-actions .btn-secondary {
  align-self: stretch;
  text-align: center;
}

/* Desktop: auto-width */
@media (min-width: 640px) {
  .intro-actions .btn-primary,
  .intro-actions .btn-secondary {
    align-self: flex-start;
    text-align: left;
  }
}
```

The blog link (`btn-blog-link`) can remain auto-width — it reads as a text link, not a primary action.

---

### P2 — `overflow-x: hidden` on body element

**Location:** `alice.css:33-39`
```css
html, body {
  ...
  overflow-x: hidden;
}
```

**Problem:** `overflow-x: hidden` on `body` creates a new stacking context on iOS Safari, which can cause `position: sticky` (used by `.screen-header`) and `position: fixed` (used by `.alice-bar`) to misbehave — specifically, sticky elements may stop sticking when the page scrolls.

**Fix:** Remove from `body`. If horizontal overflow needs to be clipped, apply to `#app` instead:
```css
html, body { overflow-x: unset; }
#app { overflow-x: hidden; }
```

---

### P3 — Intro screen: "kingofalldata.com" eyebrow

**Location:** `index.html:33`, `alice.css:126-132`
```html
<p class="intro-eyebrow" id="intro-eyebrow">kingofalldata.com</p>
```

**Observation:** Showing the domain URL as the eyebrow above Alice's name is unusual — the user is already on `kingofalldata.com`. It reads as a self-reference rather than context.

**Recommendation (defer to Veritas/Faber for copy decision):** Consider `koad:io` or remove entirely. Alice's name is the first thing that should land. The eyebrow's job here is context — "you are here in the koad:io ecosystem" — not confirmation of the domain.

This is a copy decision, not a CSS fix. Raise with Veritas or Faber before changing.

---

### P3 — Intro screen may clip content on very small or large-text screens

**Location:** `alice.css:116-124`
```css
#screen-intro {
  justify-content: center;
  align-items: center;
  padding: calc(var(--alice-spacing-lg) + 3px) var(--alice-spacing) var(--alice-spacing-lg);
  ...
  min-height: 100vh;
}
```

**Problem:** `justify-content: center` with `min-height: 100vh` vertically centers the content. On screens with very large text (accessibility font size increase) or on short landscape-mode phones, the CTA buttons may be pushed off-screen without a scrollbar appearing. The content does not overflow gracefully.

**Fix:**
```css
#screen-intro {
  justify-content: flex-start;
  padding-top: max(calc(var(--alice-spacing-lg) + 3px), 10vh);
  padding-bottom: var(--alice-spacing-lg);
  overflow-y: auto;
}
```

This allows the intro screen to scroll if needed while still appearing vertically centered on screens where content fits.

---

### P3 — GPG signature block: no copy affordance

**Location:** `alice.css:708-727` (`.cert-signature`)

The GPG signature renders at 0.65rem — acceptably small for a cryptographic artifact. But there is no copy button. Users who want to verify the certificate externally (the whole point of GPG signing) have to manually select and copy dense monospace text.

**Recommendation:** Add a "Copy signature" button below the cert-signature block. Copy behavior: same pattern as key fingerprints — adjacent "Copied!" toast, 1.5s fade. This can be a small text-link button rather than a full `.btn-secondary`.

---

### P3 — Blog eyebrow "Reality Pillar" is internal vocabulary

**Location:** `index.html:162`
```html
<p class="blog-eyebrow">Reality Pillar</p>
```

**Problem:** "Reality Pillar" is Faber's internal content strategy vocabulary (from STRATEGY.md). First-time visitors will not understand it. It reads as jargon.

**Recommendation (copy decision for Faber/Veritas):** `koad:io, built in public.` is already the subheading — the eyebrow should reinforce this, not add confusion. Consider `From the builders` or simply remove the eyebrow label and let the heading speak.

---

## What This Review Does Not Cover

- JavaScript (`app.js`, `curriculum.js`, `blog.js`) — Vulcan's territory
- The 12-level curriculum content — Faber/Veritas
- Service worker caching strategy — Vulcan
- Namespace pages (`page-namespace.html`) — separate issue, requires full implementation

---

## Handoff to Vulcan

Priority order for implementation:
1. P1 fixes (focus indicator, prefers-reduced-motion) — ship-blocking accessibility
2. P1+P2 touch targets (send button, back button)
3. P2 — `overflow-x` body fix
4. P2 — Mobile CTA full-width
5. P2 — Magic colors (after color-mix() support decision)
6. P3 — Post Veritas review on copy items (eyebrow, blog label)
7. P3 — Copy signature affordance on certificate

Cross-reference: koad/vulcan issue for integration. Tag this brief.

---

*UI review by Muse — 2026-04-04*
