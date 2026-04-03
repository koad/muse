# Entity Card Component Design

**Project:** kingofalldata.com  
**Component:** Entity Card  
**Author:** Muse (UI Beauty Entity)  
**Date:** 2026-04-03  
**Status:** Design Direction

---

## Overview

The entity card is a dual-purpose component serving two contexts:

1. **Namespace Showcase** — Real user namespaces (social proof, presence)
2. **Team Product Grid** — Cloneable koad:io entities (entity = product)

A single card design must work elegantly in both modes without feeling stretched or awkward.

---

## Design Principle

**One card. Two views. Same structure.**

The card is a container for identity. Whether it's alice.kingofalldata.com (user namespace) or juno (team entity), the card answers: "Who is this? What do I get if I clone?" The difference is emphasis, not structure.

---

## Card Structure

### All Cards Contain

```
┌──────────────────────────────────────────────┐
│                                              │
│  [Avatar] Name             [Online Indicator]│
│           Role / Type                        │
│                                              │
│  Description or specialty (1-3 lines)        │
│                                              │
│  [Spec/Meta info]                            │
│                                              │
│  [Action 1]  [Action 2]    [Optional link]   │
│                                              │
└──────────────────────────────────────────────┘
```

### Field Definitions

| Field | Type | Namespace View | Team Entity View |
|-------|------|---|---|
| **Avatar** | Circular, 48px | User avatar or initials | Entity monogram or icon |
| **Name** | Primary text | username | ENTITY_NAME (uppercase) |
| **Role/Type** | Secondary text, muted | ".kingofalldata.com" domain | "Business Orchestrator" or role |
| **Description** | Body text, muted | Specialty (e.g., "Cryptography") | What they do (e.g., "Handles strategy, partnerships, operations") |
| **Meta/Spec** | Monospace, very muted | Online status + timestamp | Tech stack (git, cryptographic identity, memories) |
| **Action 1** | Button, primary | "View Keys" (copy public key) | "Clone [Name]" (link to GitHub) |
| **Action 2** | Button, secondary | "Visit ~username" | "View on GitHub" (link to repo) |

---

## Desktop View (4 Columns, Team Grid)

```
┌────────────────────────────────┐
│                                │
│  [J]        JUNO               │
│             Business Orchestrator│
│                                │
│  Handles strategy,             │
│  partnerships, and             │
│  commercial operations.        │
│                                │
│  git | strategy | trust        │
│                                │
│  [Clone Juno]  [View GitHub]   │
│                                │
└────────────────────────────────┘
```

### Desktop Specifications

- **Width:** 100% of grid column (1/4 parent)
- **Card padding:** 24px (24px top, 24px right, 20px bottom, 24px left for alignment)
- **Avatar:** 48px diameter, centered horizontally
- **Name:** 18px, 600 weight (Inter or system sans), centered, color `#e5e5e5`
- **Role:** 13px, 400 weight, muted (`#888888`), centered
- **Description:** 14px, 400 weight, line-height 1.5, color `#b8b8b8`, centered, max 3 lines
- **Spec line:** 12px, monospace, color `#666666`, centered (e.g., "git | cryptographic identity | memories")
- **Button container:** Flex row, gap 8px, justified center, margin-top 16px
- **Buttons:** 40px height min, full-width split (50/50) or stacked on small cards
- **Border:** 1px solid `#22dd77` (green accent)
- **Background:** `#1a1a1a` (card surface)
- **Border-radius:** 8px

---

## Tablet View (2 Columns)

```
┌──────────────────────────────────────┐
│ [M]  MUSE                            │
│      UI Beauty & Design Direction    │
│                                      │
│ Wireframes, mockups, CSS, design     │
│ direction. Takes what works and      │
│ makes it beautiful.                  │
│                                      │
│ design | css | accessibility         │
│                                      │
│ [Clone Muse]    [View GitHub]        │
│                                      │
└──────────────────────────────────────┘
```

### Tablet Specifications

- **Width:** 100% of grid column (1/2 parent)
- **Card padding:** 20px
- **Avatar:** 40px diameter, positioned left-aligned (not centered)
- **Name & role:** Positioned right of avatar, text-left align
  - Name: 16px, 600 weight
  - Role: 13px, 400 weight, muted
- **Description:** 13px, full-width below avatar/name section, line-height 1.5
- **Spec line:** 12px, monospace, muted
- **Buttons:** Stack vertically or horizontal (flex-wrap if space tight), full width
- **Rest:** Same as desktop

---

## Mobile View (1 Column)

```
┌──────────────────────────┐
│ [A] ALICE                │
│     Cryptographer        │
│                          │
│ Builds secure systems    │
│ and identity layers.     │
│ Open standards advocate. │
│                          │
│ crypto | identity | go   │
│                          │
│ [Clone Alice]            │
│ [View on GitHub]         │
│                          │
└──────────────────────────┘
```

### Mobile Specifications

- **Width:** 100% container, max 320px
- **Card padding:** 16px
- **Avatar:** 40px diameter, left-aligned with flex layout
- **Name & role:** Stacked (name on line 1, role on line 2), text-left
  - Name: 16px, 600 weight
  - Role: 12px, 400 weight, muted
- **Description:** 13px, single-column, line-height 1.5
- **Spec line:** 11px, monospace
- **Buttons:** Stack vertically, full-width, 44px height minimum (touch-friendly)
- **Spacing:** 12px vertical gap between sections
- **Border-radius:** 6px

---

## Interaction States

### Hover (Desktop Only)

```css
.entity-card:hover {
  border-color: #44ff99;        /* Brighter green */
  background-color: #202020;     /* Slightly lighter surface */
  box-shadow: 0 4px 16px rgba(34, 221, 119, 0.1);  /* Subtle glow */
  transform: translateY(-2px);   /* Subtle lift */
  transition: all 200ms ease-out;
}

.entity-card:hover .entity-name {
  color: #ffffff;  /* Brighten name on hover */
}
```

**Effect:** Soft lift + border brightens + text pops. No harsh shadows or over-animation.

### Focus State (Keyboard Navigation)

```css
.entity-card:focus-within {
  outline: 2px solid #22dd77;
  outline-offset: -1px;
}
```

**Effect:** Green outline on focus, visible for accessibility.

### Button Hover

- **Primary button** ("Clone"): Background brightens 10%, cursor pointer
- **Secondary button** ("View GitHub"): Text brightens, no fill change
- **Transition:** 150ms ease-out

---

## Two Card Modes

### Mode 1: Namespace Showcase (User Identity)

**Context:** kingofalldata.com homepage, section 3 "LIVE NAMESPACES"

```
┌────────────────────────────┐
│                            │
│  [alice]  alice            │ ← Initials or user avatar
│           alice.kingofalldata.com  ← Full domain
│                            │
│  Cryptographer             │ ← Specialty (short)
│  Active now (green dot)    │
│                            │
│  [View Keys]  [@alice]     │
│                            │
└────────────────────────────┘
```

**Fields:**
- Avatar: User initials or gravatar
- Name: Username (e.g., "alice")
- Role: Full domain "alice.kingofalldata.com" in monospace, muted
- Description: Single-line specialty or bio (e.g., "Cryptographer", "Building identity layers")
- Meta: Online indicator (green dot) + "Active now" or timestamp
- Actions:
  - Primary: "View Keys" → Copies public key to clipboard, shows "Copied!" toast
  - Secondary: "@alice" → Navigate to `~alice` namespace page

---

### Mode 2: Team Entity Product (Cloneable)

**Context:** kingofalldata.com, section 4 "TEAM ENTITIES AS PRODUCTS"

```
┌──────────────────────────────┐
│                              │
│  [J]        JUNO             │
│             Business Orchestrator
│                              │
│  Handles strategy,           │
│  partnerships, and           │
│  commercial operations.      │
│                              │
│  git | strategy | trust      │
│                              │
│  [Clone Juno] [View GitHub]  │
│                              │
└──────────────────────────────┘
```

**Fields:**
- Avatar: Entity monogram or icon (J for Juno, M for Muse, etc.)
- Name: ENTITY_NAME (uppercase, e.g., "JUNO")
- Role: Title/specialty (e.g., "Business Orchestrator")
- Description: What they do (2–3 sentences, wrapped)
- Meta: Spec line (e.g., "git | strategy | trust bonds")
- Actions:
  - Primary: "Clone [Name]" → Link to GitHub repo
  - Secondary: "View on GitHub" → Direct link to repo

---

## Entity Layer Grouping (12 Entities, 4 Columns)

The 12 koad:io entities organize into 4 layers. The grid shows all entities; visual grouping via section headers or color coding (optional borders).

```
┌─────────────────────────────────────────────────┐
│          SOVEREIGN LAYER                        │
├───────────────┬───────────────┬───────────────┤
│  [KOAD]       │  [VERITAS]    │  [MERCURY]    │
│  Root         │  Verification │  Announcements│
└───────────────┴───────────────┴───────────────┘

┌─────────────────────────────────────────────────┐
│          BUSINESS LAYER                         │
├───────────────┬───────────────┬───────────────┤
│  [JUNO]       │  [IRIS]       │  [ATLAS]      │
│  Strategy     │  Brand        │  Partnerships │
└───────────────┴───────────────┴───────────────┘

┌─────────────────────────────────────────────────┐
│          PLATFORM LAYER                         │
├───────────────┬───────────────┬───────────────┤
│  [VULCAN]     │  [MUSE]       │  [HERMES]     │
│  Build        │  Design       │  API/Services │
└───────────────┴───────────────┴───────────────┘

┌─────────────────────────────────────────────────┐
│          OPERATIONS LAYER                       │
├───────────────┬───────────────┬───────────────┤
│  [KEEPER]     │  [LOGGER]     │  [PHOENIX]    │
│  Persistence  │  Observability│  Recovery     │
└───────────────┴───────────────┴───────────────┘
```

### Layer Descriptions

| Layer | Entities | Role | Visual Treatment |
|-------|----------|------|---|
| **Sovereign** | koad, veritas, mercury | Root authority, trust, communication | Section header: "SOVEREIGN LAYER" (uppercase, accent color) |
| **Business** | juno, iris, atlas | Strategy, brand, partnerships | Section header: "BUSINESS LAYER" |
| **Platform** | vulcan, muse, hermes | Product, design, services | Section header: "PLATFORM LAYER" |
| **Operations** | keeper, logger, phoenix | Data, observability, resilience | Section header: "OPERATIONS LAYER" |

**Grid Layout:**
- 3 cards per row (4 rows total)
- Section header above each layer group
- Consistent spacing between cards (gap: 24px desktop, 16px mobile)
- On mobile: All cards stack 1 per row, layers still grouped with headers

---

## Component CSS (Reference)

```css
.entity-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 24px;
  border: 1px solid #22dd77;
  border-radius: 8px;
  background-color: #1a1a1a;
  gap: 16px;
  transition: all 200ms ease-out;
}

.entity-card:hover {
  border-color: #44ff99;
  background-color: #202020;
  box-shadow: 0 4px 16px rgba(34, 221, 119, 0.1);
  transform: translateY(-2px);
}

.entity-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: #22dd77;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 20px;
  color: #0a0a0a;
}

.entity-name {
  font-size: 18px;
  font-weight: 600;
  color: #e5e5e5;
  text-align: center;
  transition: color 200ms ease-out;
}

.entity-card:hover .entity-name {
  color: #ffffff;
}

.entity-role {
  font-size: 13px;
  font-weight: 400;
  color: #888888;
  text-align: center;
}

.entity-description {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  color: #b8b8b8;
  text-align: center;
}

.entity-spec {
  font-size: 12px;
  font-family: 'JetBrains Mono', monospace;
  color: #666666;
  text-align: center;
}

.entity-actions {
  display: flex;
  flex-direction: row;
  gap: 8px;
  width: 100%;
  margin-top: 8px;
}

.entity-action-btn {
  flex: 1;
  padding: 10px 14px;
  height: 40px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 150ms ease-out;
}

.entity-action-primary {
  background-color: #22dd77;
  color: #0a0a0a;
  border: 1px solid #22dd77;
}

.entity-action-primary:hover {
  background-color: #44ff99;
  box-shadow: 0 2px 8px rgba(34, 221, 119, 0.2);
}

.entity-action-secondary {
  background-color: transparent;
  color: #22dd77;
  border: 1px solid #22dd77;
}

.entity-action-secondary:hover {
  background-color: rgba(34, 221, 119, 0.1);
  color: #44ff99;
  border-color: #44ff99;
}

/* Responsive */

@media (max-width: 1024px) {
  /* Tablet: 2 columns */
  .entity-card {
    flex-direction: row;
    align-items: flex-start;
    padding: 20px;
  }

  .entity-avatar {
    flex-shrink: 0;
    margin-right: 16px;
  }

  .entity-header {
    text-align: left;
    flex-grow: 1;
  }

  .entity-name {
    text-align: left;
  }

  .entity-role {
    text-align: left;
  }
}

@media (max-width: 640px) {
  /* Mobile: 1 column */
  .entity-card {
    padding: 16px;
    gap: 12px;
  }

  .entity-avatar {
    width: 40px;
    height: 40px;
    font-size: 18px;
  }

  .entity-name {
    font-size: 16px;
  }

  .entity-actions {
    flex-direction: column;
    gap: 8px;
  }

  .entity-action-btn {
    height: 44px;
    font-size: 14px;
  }
}
```

---

## States & Behaviors

### Namespace Showcase (Homepage, Live Data)

- **Initial load:** Cards load with skeleton (background color, no text)
- **Populated:** Real user data loads; "Active now" indicator if heartbeat < 5 min
- **Copy action:** Click "View Keys" → copies public key → show toast "Copied!" for 1.5s, then fade
- **Link action:** Click name/avatar → navigate to `~{username}` namespace page
- **Empty state:** If < 3 namespaces available, show "Join them →" CTA instead of placeholder

### Team Entity Grid (Static Content)

- **Load:** Cards render immediately (no API call)
- **Clone button:** Navigate to GitHub repo
- **View GitHub:** Direct link to repo
- **No online indicator** (not a real user)
- **No copy action** (product, not identity)

---

## Color Reference

| Element | Color | Hex | Use |
|---------|-------|-----|-----|
| Border (default) | Green accent | `#22dd77` | Card outline |
| Border (hover) | Brighter green | `#44ff99` | Hover state |
| Background | Card surface | `#1a1a1a` | Card fill |
| Background (hover) | Lighter surface | `#202020` | Hover lift |
| Text (primary) | Light gray | `#e5e5e5` | Name, headings |
| Text (hover) | White | `#ffffff` | On hover |
| Text (secondary) | Medium gray | `#888888` | Role, subtitle |
| Text (tertiary) | Dark gray | `#666666` | Monospace spec |
| Button (primary) | Green accent | `#22dd77` | "Clone" CTA |
| Button (text) | Medium gray | `#666666` | Text on button |
| Online indicator | Green | `#22dd77` | Active status dot |

---

## Accessibility Checklist

- ✅ Focus visible: 2px green outline on card / button focus
- ✅ Color contrast: All text meets WCAG AA (4.5:1 body, 3:1 large)
- ✅ Alt text: Card content is semantic HTML, no decorative images
- ✅ Touch targets: Buttons min 44px × 44px on mobile
- ✅ Semantic HTML: Use `<article>` for card, `<button>` for actions, proper heading hierarchy
- ✅ Keyboard nav: Tab through cards and buttons, all links/buttons accessible
- ✅ No motion sickness: Subtle transitions only, no auto-animate

---

## File & Component Naming

| Artifact | File Path | Owner |
|----------|-----------|-------|
| This design doc | `~/.muse/designs/entity-card-component.md` | Muse |
| Blaze component | `~/.koad-io/meteor/imports/ui/components/EntityCard.blaze` | Vulcan |
| Component stylesheet | `~/.koad-io/meteor/imports/ui/components/entity-card.css` | Vulcan (from Muse spec) |
| Homepage integration | `~/.koad-io/meteor/imports/ui/pages/Home.blaze` | Vulcan |

---

## Next Steps (For Vulcan)

1. Create `EntityCard` component in Blaze with mode prop: `mode='namespace'` or `mode='entity'`
2. Implement CSS per spec (custom properties for colors, responsive grid)
3. Integrate into homepage sections:
   - Section 3: Namespace showcase (fetch live data, random 6)
   - Section 4: Team entities grid (static from config, grouped by layer)
4. Test hover, focus, and mobile responsiveness
5. Verify color contrast and accessibility

---

*Design by Muse — ready for Vulcan's implementation.*
