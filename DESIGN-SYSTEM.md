# koad:io Design System — Style Guide

**Author:** Muse  
**Date:** 2026-04-05  
**Version:** 1.1 (consolidated from 28+ briefs)  
**Audience:** Vulcan (primary), any implementer working on koad:io surfaces  
**Source of truth:** `~/.muse/briefs/` and `~/.muse/design-system/koad-io-design-system.md`

This document is a reference guide, not a brief. It consolidates every established design decision without introducing new ones. When a brief conflicts with this document, the brief is more specific and wins for its context — but this document captures what is true across all surfaces.

---

## 1. Color System

### 1a. System Accent

The global koad:io accent is **violet `#7c6aff`**. It appears on CTAs, active states, focus rings, series badges, syntax highlighting keywords, and structural highlights across all non-Alice surfaces.

Alice overrides this with amber — see Section 1c.

### 1b. Full Token Set (Dark Mode — Default)

```css
/* Backgrounds */
--color-bg-primary:      #0c0c0e;   /* Near-black, slight blue undertone */
--color-bg-secondary:    #141418;   /* Cards, panels */
--color-bg-tertiary:     #1c1c22;   /* Elevated surfaces, inputs, command blocks */
--color-bg-hover:        #242429;   /* Interactive hover states */
--color-bg-active:       #2a2a32;   /* Pressed / active states */

/* Borders */
--color-border-subtle:   #1f1f27;   /* Very subtle dividers */
--color-border-default:  #2a2a32;   /* Default borders */
--color-border-strong:   #3a3a44;   /* Emphasized borders, focus rings */

/* Text */
--color-text-primary:    #e8e8ec;   /* Primary text, headings */
--color-text-secondary:  #8888a0;   /* Labels, hints, secondary content */
--color-text-muted:      #64647c;   /* Tertiary text, timestamps, very low emphasis */
--color-text-inverse:    #0c0c0e;   /* Text on light / colored backgrounds */

/* Accent */
--color-accent:          #7c6aff;   /* Violet — global primary accent */
--color-accent-subtle:   #7c6aff20; /* Subtle accent fills (series badges, etc.) */
--color-accent-glow:     #7c6aff40; /* Glow overlays */

/* Semantic */
--color-success:         #4ade80;   /* Verified, trust confirmed, active dot */
--color-success-subtle:  #4ade8020;
--color-warning:         #fbbf24;   /* Caution, unverified bonds */
--color-warning-subtle:  #fbbf2420;
--color-error:           #f87171;   /* Errors, revoked bonds */
--color-error-subtle:    #f8717120;
--color-info:            #60a5fa;
--color-info-subtle:     #60a5fa20;
```

### 1b-light. Light Mode

Dark mode is canonical. Light mode is applied via `[data-theme="light"]`.

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
  --color-accent:          #6b4feb;  /* Darker for contrast on light bg */
  --color-accent-subtle:   #6b4feb15;
  --color-success:         #3a9d4d;
  --color-success-subtle:  #3a9d4d15;
  --color-warning:         #d97706;
  --color-warning-subtle:  #d9770615;
  --color-error:           #dc2626;
  --color-error-subtle:    #dc262615;
}
```

### 1c. Alice / Learning System Skin

Alice overrides the violet accent with **amber `#F4B844`**. This applies to `kingofalldata.com` and all Alice PWA screens. Amber communicates warmth, patience, and personal presence — Alice is not infrastructure, she is a guide.

```css
/* Alice skin — do not apply to namespace profile pages or koad:io dashboards */
--alice-accent:       #F4B844;   /* Warm amber — Alice's voice, CTAs */
--alice-accent-dark:  #E8A738;   /* Hover / pressed */
--alice-bg:           #0a0a0a;   /* True near-black (slightly warmer than system) */
--alice-surface:      #111111;
--alice-surface-2:    #161616;
--alice-text:         #f0ede5;   /* Warm white, not cool-shifted */
--alice-subtle:       #555555;
--alice-border:       #2a2a2a;
--alice-success:      #8ac926;   /* Level complete, positive states */
--alice-line-height:  1.6;
--alice-radius:       6px;
```

Alice amber (`#F4B844`) on black (`#0a0a0a`): contrast ratio **8.2:1** — AAA.

### 1d. Entity Identity Colors

Each entity has a single color used for:
- The 3px top border rule on product cards (top edge only — not a full border)
- The entity's `✦` glyph in avatar position
- The CTA button on that entity's product card (only place entity color overrides the global system)
- Background fills at **12% opacity** for any fill use

| Entity  | Color Name       | Hex       |
|---------|------------------|-----------|
| alice   | Amber            | `#F4B844` |
| juno    | Imperial Gold    | `#D4AF37` |
| vulcan  | Forge Crimson    | `#C0392B` |
| veritas | Ice Blue         | `#5B9BD5` |
| mercury | Electric Cyan    | `#00B4D8` |
| muse    | Violet           | `#7c6aff` |
| sibyl   | Twilight Purple  | `#8B5CF6` |
| faber   | Warm Ochre       | `#C27C0E` |
| chiron  | Sage Green       | `#4A7C59` |
| argus   | Signal Green     | `#22C55E` |
| salus   | Steady Teal      | `#0D9488` |
| aegis   | Deep Indigo      | `#4338CA` |
| livy    | Parchment Rose   | `#C4884A` |

Muse's entity color is the global system accent — her product card CTA is identical to a standard koad:io button. This is intentional.

**Rule against rainbow grids:** In a grid of entity cards, entity color appears only in the 3px top rule and the glyph. The card body uses standard tokens. The grid reads as one coherent surface; entity color registers on inspection, not at a glance.

### 1e. Syntax Highlighting Overrides

When syntax-highlighting code blocks, map to design system colors:

- **Keywords:** `#7c6aff` (accent violet)
- **Strings:** `#4ade80` (success green)
- **Comments:** `--color-text-muted` (`#64647c`)
- **Variables/identifiers:** `--color-text-primary` (`#e8e8ec`)
- **Numbers/constants:** `#fbbf24` (warning amber)
- Code block background: always `--color-bg-secondary` (`#141418`)

---

## 2. Typography

### 2a. Typeface Stack

| Role | Typeface |
|------|----------|
| Keys, hashes, technical data, code | JetBrains Mono (primary), IBM Plex Mono (fallback) |
| Headings, labels, UI chrome | Inter 600–700 |
| Body copy, descriptions, buttons | Inter 400 |

Font loading: self-hosted, no Google Fonts dependency. System fonts as fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`.

Alice uses system fonts intentionally — she is a PWA and first-load performance is critical. If Inter is already cached from a preceding koad:io page, she inherits it, but her CSS must not require it.

### 2b. Scale and Rhythm (Portal / Dashboards)

Base: **14px**, line-height **1.5**.

```css
--font-h1:    2rem    /* 32px — page titles, hero headlines */
--font-h2:    1.5rem  /* 24px — section titles */
--font-h3:    1.25rem /* 20px — subsection titles */
--font-h4:    1.125rem /* 18px — component titles */
--font-body:  0.875rem /* 14px — default UI text */
--font-sm:    0.75rem  /* 12px — labels, captions */

--font-mono-body:  0.85rem JetBrains Mono  /* 12px — keys, fingerprints */
--font-mono-label: 0.75rem JetBrains Mono  /* 11px — hash previews, code labels */

--font-regular:   400
--font-medium:    500
--font-semibold:  600
--font-bold:      700
```

### 2c. Blog / Reading Scale

Blog posts use a distinct reading scale — do not apply portal scale to long-form content.

- Body: **17px**, Inter 400, line-height **1.75**
- Max content width: **720px** (~75 characters per line — optimal reading)
- Do not reduce below 17px on mobile
- `h2`: 1.375rem (22px), Inter 700, border-bottom 1px `--color-border-subtle`
- `h3`: 1.125rem (18px), Inter 600
- Paragraph spacing: `var(--space-6)` (24px)
- Post title: Inter 700, 36px desktop / 28px mobile (< 640px), line-height 1.2

### 2d. Alice Conversation Scale

- Alice's prose messages: **18px**, line-height **1.65**, color `#f0ede5`
- Learner messages: 18px, `#f0ede5` at **85% opacity**
- Atom counter, header labels: 12–13px, amber or muted
- Input placeholder: 15–16px
- Certificate display name (hero): 28–32px, `#f0ede5`

Alice's text breathes. Short, declarative sentences surrounded by generous whitespace. Paragraphs separated by full blank lines.

### 2e. Code Blocks

All code blocks:
- Font: `JetBrains Mono`, 13px, line-height 1.6
- Background: `--color-bg-secondary` (`#141418`)
- Header bar: `--color-bg-tertiary` (`#1c1c22`), 32px tall
- Header: language label (JetBrains Mono 11px, `--color-text-muted`, uppercase) + optional filename (center-right) + copy button (right)
- Border: 1px `--color-border-default`, border-radius 6px
- Copy button: shows checkmark for **1.5 seconds**, then resets
- Horizontal scroll on overflow — never word-wrap code

Inline code: JetBrains Mono, 0.875em, background `--color-bg-tertiary`, border 1px `--color-border-default`, border-radius 3px, padding 1px 5px.

Terminal snippets / command blocks (non-highlighted): same background as code blocks, with a left accent border — `3px solid --color-accent` — to signal "this is infrastructure output."

---

## 3. Key Components

### 3a. Entity Product Card

The marketplace surface for gestating an entity. Not a social presence card — a purchase-decision surface.

**Anatomy (top to bottom):**
1. 3px top border in entity color (top edge only)
2. Identity row: `✦` glyph (entity color), entity name (Inter 600, 16px), status dot
3. Role line: 13px, `--color-text-secondary`, indented to align with name
4. Specialty text: 14px, `--color-text-primary`, max 3 lines clamped
5. Divider
6. Recent deliverables: up to 3 items, prefixed `·` (middle dot), 13px
7. Divider
8. Gestation command: JetBrains Mono 13px, `--color-bg-tertiary`, copy affordance on hover
9. Primary CTA button (entity color background, `#0c0c0e` text)
10. Secondary link: "View profile →"

**CTA verb by state:**
- Ungestated: `Gestate {Name} ✦`
- Gestated, running: `Open session ✦`
- Gestated, dormant: `Resume {Name} ✦`

**Status language:**
- `● active` — `--color-success` dot — last commit within 14 days
- `◌ dormant` — hollow dot, muted — 15–60 days without commits
- `— archived` — dash, strikethrough name — explicitly archived

**Card grid:** `grid-template-columns: repeat(auto-fill, minmax(320px, 1fr))`, `gap: 24px`, `align-items: start`. Cards do not stretch vertically. `min-height: 320px`, top-aligned.

**Card hover:** `translateY(-2px)`, border brightens — entity color on top rule is preserved.

### 3b. Alice Conversation View (Not Bubbles)

Alice uses **attributed prose blocks**, not chat bubbles. Bubbles communicate peer-to-peer messaging; Alice is a mentor. Her messages should read like a composed letter.

**Alice turn:**
- `Alice` label: 13px, `#F4B844` (amber), followed by a horizontal rule extending to the right edge
- Message text: 18px, `#f0ede5`, line-height 1.65
- Left border: 2px solid `#F4B844` at **30% opacity** runs full height of block — her mark on every message
- Timestamp: 12px, `#555555`, left-aligned below message

**Learner turn:**
- `You` label: 13px, `#555555`, right-aligned, with rule extending left
- Message text: 18px, `#f0ede5` at **85% opacity**
- Timestamp: right-aligned
- No left border — absence of amber identifies learner turn

**Composing indicator:**
- Three amber dots (`·  ·  ·`), animated at 400ms intervals
- Amber left border present at **15% opacity** while composing
- Minimum display: **600ms** (Alice does not blurt)

**Input zone:**
- Placeholder text is Alice's voice — changes by atom type:
  - Content atom: `"Type your answer, or ask Alice a question…"`
  - Reflection prompt: `"What are you thinking?"`
  - Assessment atom: `"Show Alice what you know."`
  - After direct question: `"Your answer…"`
- Send button: amber `→`, active when input is non-empty
- No "Submit for review" button — Alice decides when the exit criterion is met

### 3c. Curriculum Browser (Map View)

**Level row anatomy on the map:**
- `✦` completed (amber) — last commit within 14 days
- `◆` in progress (amber, bright)
- `·` ahead (muted, available)
- `○` locked (muted, open ring)

**Section dividers:** thin rule (`#1a1a1a`) with centered label, 11px, `#444444`. Low contrast — organization, not header.

**Level entry card** (appears on tap, full-screen overlay):
- Level number: 13px, amber
- Level title: 24px, `#f0ede5`
- Metadata: duration · atom count, 12px, muted
- Learning objective: plain prose, 16px
- "What Alice expects": exit criteria in Alice's voice, 15px
- Primary button: `Begin Level N ✦` or `Continue ✦` (amber)
- No locked level can be loaded or previewed — locking is honest, not punitive

**Locked level affordance (on tap):** Inline expansion shows prerequisite and "Tell Alice I know this" amber link (not a primary button — subtle). Tapping drops learner into conversation with a pre-seeded assessment message.

**Progress language:** `atom 2 of 5`, 12px, `#F4B844` at 60% opacity. No percentage. No progress bar.

### 3d. Level Progress Header (Ambient Strip)

Fixed header strip at top of conversation view, 24px tall. Matches conversation background — not a navigation bar.

```
← Journey          Level 3: Keys & Identity      atom 2 of 5
```

- Left: `← Journey` amber link (back to map)
- Center: level name, 13px, `#555555`
- Right: `atom 2 of 5`, 12px, `#F4B844` at **50% opacity** — peripheral, not demanding
- Mobile: `L3 · atom 2/5`, all right-aligned

Atom counter update: old count fades out (200ms), new count fades in — no ceremony.

### 3e. Blog: Series Context Strip

Placed immediately after the post header divider, before the first paragraph — for posts that are part of a named series:

```
┌────────────────────────────────────────────────────────────────┐
│  This post is part of the 2-Week Reality Proof — 20 posts      │
│  documenting a live koad:io operation in April 2026.           │
│  Start at Day 1 →  or  Read the series overview →             │
└────────────────────────────────────────────────────────────────┘
```

Container: `--color-bg-secondary`, `--color-border-default` border, left accent rule 3px `--color-accent`.  
Text: Inter 400, 14px, `--color-text-secondary`. Links in `--color-accent`.

**Series badge** (in post header):
- Format: `{SERIES NAME} · Day {N} of {total}` — e.g. `REALITY PILLAR · Day 6 of 14`
- Background: `--color-accent-subtle` (`#7c6aff20`), border: 1px `--color-accent`, radius 4px, padding 4px 10px, inline-block
- Only rendered if frontmatter has both `series` and `day`

### 3f. Trust Bond Certificate / Alice's Attestation

The certificate header reads **"Alice's Attestation"** — not "Certificate of Completion." Alice *attests*; she does not certify in the institutional sense. This is the honest framing.

**Certificate frame:**
- Top: 2px solid `#F4B844`
- Bottom: 2px solid `#F4B844`
- Left/Right: 1px solid `#2a2a2a`
- Border-radius: 4px
- Background: `#0a0a0a`
- Inner padding: 24px desktop, 20px mobile

**Typography on certificate:**

| Element | Size | Color |
|---------|------|-------|
| Header "ALICE SOVEREIGNTY MASTERY" | 13px, all-caps, letter-spacing 0.15em | `#F4B844` |
| Display name (hero) | 28–32px | `#f0ede5` |
| Body copy | 16px | `#f0ede5` at 85% opacity |
| Labels (Completed, Learner ID, etc.) | 12px | `#555555` |
| Signature block | 11px, Space Mono | `#F4B844` at 80% opacity |
| Verify link | 12px | `#F4B844` |

**Signature:** Alice signs with her Ed25519 key (`~/.alice/id/ed25519`). Canonical string: `{curriculum}:{displayName}:{learnerId}:{completedDate}`. The full signature block appears on the printable artifact; it is truncated (tap to expand) on screen.

**Trust bond chain visualization:**
- Node dot: `--color-accent` (`#7c6aff`) for ACTIVE, `--color-warning` for UNVERIFIED, `--color-error` for REVOKED
- Connector lines: 1px `--color-border-default`, no arrowheads
- Bond type labels: JetBrains Mono 10px, `--color-text-muted`, on the connector line
- Verification state never communicated by color alone — always include ✓/◌/✗ icon and label text

---

## 4. Spacing and Grid

### 4a. Spacing Scale (8px base unit)

```css
--space-1:   0.25rem  /*  4px */
--space-2:   0.5rem   /*  8px  — base unit */
--space-3:   0.75rem  /* 12px */
--space-4:   1rem     /* 16px */
--space-5:   1.25rem  /* 20px */
--space-6:   1.5rem   /* 24px */
--space-8:   2rem     /* 32px */
--space-10:  2.5rem   /* 40px */
--space-12:  3rem     /* 48px */
--space-16:  4rem     /* 64px */
```

### 4b. Common Applications

| Context | Value |
|---------|-------|
| Button padding (default) | `--space-3` vertical, `--space-6` horizontal |
| Card/panel padding | `--space-6` (24px) |
| Blog post side padding (mobile) | `--space-5` (20px) |
| Blog post side padding (≥640px) | `--space-8` (32px) |
| Section gap (landing page) | `--space-16` (64px) |
| Section gap (other pages) | `--space-12` (48px) |
| Between sections (mobile) | `--space-8` (32px) |
| Between subsections | `--space-8` (32px) |
| Between list items | `--space-4` (16px) |
| Entity product card padding | 20px |
| Entity product card gap | `gap: 12px` internal |

### 4c. Grid

- Max content width: **1200px**
- Blog / reading max width: **720px** (single column, no sidebar)
- koad.sh presence page max width: **640px**
- Entity product card grid: `repeat(auto-fill, minmax(320px, 1fr))`, gap 24px
- Sidebar width: 240px (desktop)
- Gutter: `--space-6` between columns

### 4d. Breakpoints

```
xs:  320px  — mobile baseline
sm:  640px  — small tablet
md:  768px  — tablet, sidebar appears
lg: 1024px  — desktop
xl: 1280px  — large desktop
```

Touch target minimum: **44×44px** for all tappable elements.

### 4e. Border Radii

- Standard cards, inputs, buttons: **8px**
- Code blocks, inline command blocks: **6px** outer, **4px** inner
- Small chips, tags, status dots: **4px** or `12px` (pill)
- Alice domain: **6px** (slightly softer)
- Certificate frame: **4px**

---

## 5. Animation and Timing

All animations respect `prefers-reduced-motion: reduce` — instant state changes, no transitions.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 5a. Global System Timings

| Interaction | Duration | Easing |
|-------------|----------|--------|
| Hover color/border change | 150ms | ease-out |
| Button press feedback (scale) | 150ms | ease-in-out |
| Fade in/out (content load) | 200ms | ease-out |
| Slide up (drawer/modal enter) | 250ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Card hover translateY(-2px) | 80ms | ease |
| Copy button "Copied ✓" hold | **1.5s** |  |
| Tooltip fade in | 150ms | ease-out |
| Tooltip fade out | 100ms | — |

### 5b. Alice-Specific Timings

| Moment | Timing |
|--------|--------|
| Composing indicator appears | After 200ms latency (never immediate) |
| Composing minimum display | **600ms** (Alice does not blurt) |
| Message text renders | Instant, but composing minimum holds the beat |
| Atom counter fade out (transition) | 200ms |
| Atom counter fade in (new value) | 200ms |
| Level completion ceremony — `✦` glyph fades in | 600ms |
| Level completion — title fades in | 200ms after glyph (staggered) |
| Level completion — amber rule draws from center | 400ms |
| Level completion — Alice's preview message fades in | 400ms after rule |
| Level completion — Continue button appears | 200ms after message |
| Level completion ceremony total | ~2.5s |
| Input zone disappears during ceremony | Immediate — Alice has the floor |
| Return acknowledgment appears | 800ms after page load |
| Certificate signing animation (pulse beats) | 1.5s total (3 beats) |
| Certificate reveal fade-in + scale | 400ms, scale 0.97→1.0 |
| UUID/signature block expand | ~200ms smooth height |
| PWA `messageIn` animation | 200ms fade + 6px slide-up |

### 5c. Avoid

- Carousel auto-play
- Parallax scrolling
- Decorative loops (except composing dots, which stop when message arrives)
- Animations that run more than once without user action

---

## 6. Iconography and Glyphs

### 6a. The `✦` Glyph (Four-Pointed Star Diamond)

The primary koad:io mark. Used for:

- **Entity identity:** The `✦` appears as the glyph/avatar for every entity. Rendered in the entity's identity color.
- **CTA decoration:** Appended to primary buttons: `Gestate Chiron ✦`, `Continue ✦`, `Let's begin ✦`
- **Level completion:** The ceremony opens with a centered `✦` fading in over 600ms
- **Certificate:** `✦ ──────── ✦` footer rule; `✦ ALICE SOVEREIGNTY MASTERY ✦` header
- **Curriculum map:** Marks every completed level
- **The glyph is Alice's.** What you earn in the conversation ceremony is what you see on the map. Visual continuity is intentional.

### 6b. Level Status Glyphs

| Glyph | Meaning | Color |
|-------|---------|-------|
| `✦` | Completed | Amber `#F4B844` |
| `◆` | In progress (filled diamond) | Amber `#F4B844`, bright |
| `·` | Ahead / available, not started | Muted `#555555` |
| `○` | Locked (open ring) | Muted `#555555` |

### 6c. Activity / Status Dots (Entity Cards)

| Indicator | Glyph | Color |
|-----------|-------|-------|
| Active | `●` | `--color-success` (`#4ade80`) |
| Dormant | `◌` (hollow) | Border only, muted |
| Archived | `—` (dash) | Muted, name strikethrough |

### 6d. Trust Bond Nodes

`◉` — filled circle. Color follows verification state:
- ACTIVE: `--color-accent` (`#7c6aff`)
- UNVERIFIED: `--color-warning` (`#fbbf24`)
- REVOKED: `--color-error` (`#f87171`)

Verification text labels always accompany color — state is never color-only. Labels: `✓ verified`, `◌ unverified`, `✗ revoked`.

### 6e. Middle Dot `·` as Separator

Used throughout the system as a separator between metadata items:
- `atom 2 of 5 · in progress`
- `Faber · April 5, 2026`
- `REALITY PILLAR · Day 6 of 14`
- Recent deliverable list prefix

Never a bullet (`•`) or hyphen. Always the middle dot (`·`, U+00B7).

---

## 7. Entity Voice in UI

These decisions govern how Alice's presence is expressed through the interface — not through her written text, but through visual and structural choices.

### 7a. Amber Left Border as Heartbeat

Every Alice message carries a **2px left border in `#F4B844` at 30% opacity**. On a dark background this is subtle — not a loud bracket. Scanning down a conversation, the amber thread on the left marks wherever Alice spoke. The learner's messages have no border. The conversation encodes whose voice is whose without requiring labels to be read.

On the composing state: border opacity drops to **15%** — Alice's mark is there while she thinks, but quiet.

### 7b. Input Placeholder as Alice's Voice

The placeholder text in the conversation input is not generic UI copy — it is Alice speaking:
- Content atom: `"Type your answer, or ask Alice a question…"`
- Reflection prompt: `"What are you thinking?"`
- Assessment atom: `"Show Alice what you know."`
- After direct question: `"Your answer…"`

These rotate based on atom type from the curriculum metadata. Default fallback: the content atom placeholder.

### 7c. Alice's Name as the Only Avatar

The `Alice` label above each of her message blocks is her only avatar. No image. No icon. No circle with initials. Her name in amber, followed by a horizontal rule extending to the right edge of the conversation column. This is the slot reserved for any future visual identity (glyph, sigil) — for now, her name is enough.

### 7d. Silence Is Designed

- The gap after the learner sends a message is not a spinner — it is a beat
- Alice's presence while composing is indicated by slow amber pulse on her name marker + three dots
- The 600ms minimum composing display is mandatory: even instant responses arrive with the feeling that Alice considered them
- During the level completion ceremony, the input zone disappears entirely — Alice has the floor and there is nothing for the learner to do except receive the moment

### 7e. Ceremony Is Reserved for Levels, Not Atoms

There are 5 atoms per level. No banner, no toast, no confetti on atom completion. Alice acknowledges in her voice and moves forward; the atom counter increments silently.

Level completion earns a ceremony. Atom completion does not. Celebrating every atom would be infantilizing — a sticker chart. The ceremony is reserved for the level.

### 7f. Alice's Color Belongs to the Curriculum, Not the Platform

The amber color (`#F4B844`) is Alice's — it appears wherever Alice is present and only there. On koad:io platform pages (namespace profiles, dashboards, the entity marketplace), violet is the accent and amber is absent. When a user enters Alice's space at `kingofalldata.com`, the shift to amber signals "you are with Alice now."

---

## 8. What NOT To Do

These are explicit anti-patterns. Do not use them.

### 8a. Never for Alice / Learning System

- **No progress bars** — not on the journey map, not in the conversation header, not at the level list. The count (`atom 2 of 5`, `3 of 12 levels`) is enough.
- **No percentage** — "67% complete" is never shown anywhere in the Alice system.
- **No gamification badges** — no streak counts, no achievement badges, no XP, no points.
- **No confetti** — not on atom completion, not on level completion, not on graduation.
- **No "Submit for review" button** — Alice decides when the exit criterion is met, not a grading button.
- **No chat bubbles for Alice** — Alice uses attributed prose blocks, not floating bubbles. Bubbles communicate peer chat; Alice is a mentor.
- **No synthetic click sound or haptic on send** — the send interaction is the learner's natural action; do not augment it.
- **No "Are you sure you want to leave?" modal** — conversation state is always already saved. No loss warning needed.
- **No spinner while Alice composes** — use the three-dot amber composing indicator. A spinner implies a loading state; Alice composing is not loading.
- **No atom boundary banner** — "Atom 3: The Daemon begins now" is never shown inline. Atoms are an internal pacing unit. The conversation reads as a unified thread.

### 8b. Never for the Global System

- **No decorative gradients** — except as very subtle background texture at most.
- **No heavy drop shadows** — max shadow: `0 4px 12px rgba(0,0,0,0.3)`.
- **No carousels or hero sliders**.
- **No stock photography**.
- **No rotating loading spinners** — use pulse animations.
- **No obfuscated sensitive data by default** — show public keys; never mask them without user action.
- **No countdown timers** — contrary to sovereignty message.
- **No "only on our platform" copy** — contrary to sovereignty.
- **No `outline: none` on `:focus-visible`** — always provide a visible focus indicator. Minimum: `2px solid --color-accent`, offset 2px.
- **No state communicated by color alone** — always accompany color with icon + text label (verified/unverified/revoked, active/dormant, etc.).

### 8c. Never for Blog / Content

- **No excerpt text on post list items** — developers read titles; excerpts add noise.
- **No excerpt teasers** — the index is a title list. Authors write titles that stand alone.
- **No sidebar on blog post pages** — single column, the post fills the screen.
- **No sticky headers on blog post pages** — the page scrolls clean from start to finish.

---

**Maintained by:** Muse  
**Last updated:** 2026-04-05  
**Source briefs:** `~/.muse/briefs/`  
**Base design system:** `~/.muse/design-system/koad-io-design-system.md`
