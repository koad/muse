# Entity Product Card — Design Spec

**Status:** Complete
**Date:** 2026-04-05
**Audience:** Vulcan (marketplace implementation), Juno (product strategy review)
**Entity:** Muse
**References:** 2026-04-04-entity-card-component.md, 2026-04-05-entity-descriptions.md, koad:io design system

---

## Overview

The entity marketplace is where koad:io makes its promise tangible: entities are products you run locally, not services you subscribe to. The product card is the primary surface for that promise. It must communicate what an entity does, prove it is real (commits, activity), and make the path to owning one obvious.

This brief specifies the product card as it appears on the entity marketplace/store page. It is distinct from the entity-card-component variants (showcase, directory, activity, team) — those cards describe existing instances. The product card describes something you can gestate: an entity that doesn't exist on your disk yet.

The distinction matters for design: the product card is a purchase decision surface, not a social presence surface.

---

## Design Principles (Product Card — Specific)

**The entity IS the product.** There is no separate "pricing tier" to communicate. The entity runs locally, free, once gestated. The card does not need to sell a subscription. It needs to communicate what you get.

**Gestation is the CTA.** One command. The card earns the user's confidence first, then presents that one command. Everything else is context for that moment.

**Activity is the proof.** Commits and deliverables are not stats for their own sake. They demonstrate that this entity is doing real work — that gestating it gives you something living, not a dormant template.

**Color is identity, not decoration.** Each entity has a color identity that reflects its mythological character and function. This color appears once, deliberately. It is not a border on the whole card — it is the entity's mark at the top, or on the glyph. It does not compete with the global koad:io accent system; it coexists.

**Dormancy is honest.** If an entity hasn't shipped work in 30+ days, the card says so plainly. A dormant entity is still gestatable; dormancy is factual information, not shame.

---

## 1. Entity Color Identity System

Each entity has a single hue that represents its character. This color appears in one place on the card: a 3px top border rule on the card container (not a full border — only the top edge), and the entity's glyph in the avatar position.

Color assignments are grounded in mythological character, not arbitrary differentiation.

| Entity  | Color Name       | Hex       | Rationale |
|---------|------------------|-----------|-----------|
| alice   | Amber            | `#F4B844` | Warmth, invitation, first light — established in Alice UI design |
| juno    | Imperial Gold    | `#D4AF37` | Roman queen, authority, cool gold — distinct from Alice's warm amber |
| vulcan  | Forge Crimson    | `#C0392B` | The forge, fire, iron. Direct. Functional. |
| veritas | Ice Blue         | `#5B9BD5` | Truth is cold, clear, precise. Not warm — correct. |
| mercury | Electric Cyan    | `#00B4D8` | Speed, transmission, signal — communication as energy |
| muse    | Violet           | `#7c6aff` | Uses the system accent — beauty as the design system's own color |
| sibyl   | Twilight Purple  | `#8B5CF6` | Oracular, liminal, between states — neither day nor night |
| faber   | Warm Ochre       | `#C27C0E` | The maker's clay, craft, material — earth-toned amber-brown |
| chiron  | Sage Green       | `#4A7C59` | The teacher in the wilderness, mentor, growth without urgency |
| argus   | Signal Green     | `#22C55E` | Diagnostic alertness, system pulse — uses success color |
| salus   | Steady Teal      | `#0D9488` | Safety, watchfulness, calm health monitoring |
| aegis   | Deep Indigo      | `#4338CA` | The shield, protection close to authority, close to Juno but its own |
| livy    | Parchment Rose   | `#C4884A` | Warm archive, historian's ink, manuscript amber |

These colors are applied at low opacity for background fills (`12%`) and full opacity for glyphs and the top border rule only.

**The rule against rainbow grids:** When multiple cards appear together in a grid, the color appears only in the 3px top rule and the entity glyph character. The card body (background, border, text) uses standard design system tokens. At a glance, a grid of cards reads as one coherent surface; only on inspection does each entity's color identity register. This is intentional — the system has coherence, the entities have individuality.

---

## 2. Card Anatomy

Information appears in this order, with these visual weights:

```
┌──────────────────────────────────────────────┐
│░░░░░░░░░░░░░░░ [3px top rule, entity color] ░│ ← entity color only here in the border
│                                              │
│  ✦   Chiron                    ● active      │ ← [glyph in entity color] [name] [status]
│      Curriculum architect                    │ ← role, 13px, --color-text-secondary
│                                              │
│  Trains every learner who enters koad:io.    │ ← specialty (1–2 sentences), 14px
│  Builds and owns the Alice curriculum.       │
│                                              │
│  ─────────────────────────────────────────   │ ← divider
│                                              │
│  Recent                                      │ ← section label, 11px, muted
│  · Chiron curriculum spec complete           │ ← deliverable item
│  · alice-onboarding level-00 through 12      │ ← deliverable item
│  · DECISIONS.md written                      │ ← deliverable item (up to 3 shown)
│                                              │
│  ─────────────────────────────────────────   │ ← divider
│                                              │
│  koad-io gestate chiron                      │ ← gestation command, monospace
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │  Gestate Chiron  ✦                   │    │ ← primary CTA button
│  └──────────────────────────────────────┘    │
│                                              │
│  View profile →                              │ ← secondary link, entity namespace page
│                                              │
└──────────────────────────────────────────────┘
```

### Information hierarchy and rationale

**Tier 1 — Identity (highest weight):** Entity glyph + name + status. These answer "what am I looking at and is it alive?" in under a second.

**Tier 2 — Function:** Role (one line) + specialty (1–2 sentences). These answer "what does it do?" without requiring the user to click through.

**Tier 3 — Proof:** Recent deliverables. These answer "does it actually work?" without requiring the user to trust the description alone.

**Tier 4 — Action:** The gestation command (visible, copyable) and the CTA button. The command is shown before the button because technically-inclined users will copy it directly; the button is for everyone else.

**The secondary link "View profile →"** points to the entity's namespace page (e.g., `vulcan.koad.io` or `canon.koad.sh/chiron`), where the full commit history, keys, and trust bonds are visible. This is the deeper due diligence path.

---

## 3. The "Cloneable" Affordance

The product card must communicate: "this is a product you run on your disk, not a service you sign into."

Three design decisions carry this:

**3a. The gestation command is typeset, not hidden in a modal.**

```
koad-io gestate chiron
```

This appears in `JetBrains Mono`, 13px, `--color-text-secondary`, on a `--color-bg-tertiary` background, with a `[Copy]` affordance (clipboard icon, appears on hover/focus). The command is not in a code fence with a label — it just appears, as if it belongs there, because it does.

**3b. The CTA reads "Gestate Chiron", not "Get Started" or "Install".**

The verb is specific to the system. It communicates that something is being created, not downloaded. It avoids the SaaS register ("Subscribe", "Try free") and the developer register ("npm install"). "Gestate" is a koad:io word. Using it in the CTA reinforces the vocabulary for users who are learning it.

**3c. The status indicator says "active" or "dormant", not "online".**

The existing entity-card-component uses an online/offline dot. The product card uses different language because you are not looking at a live instance — you are looking at an entity definition. "Active" means the entity has shipped work recently (within 14 days). "Dormant" means 15–60 days without commits. "Archived" means marked explicitly. These are process states, not connection states.

Status display:
- `● active` — `--color-success` dot, "active" in `--color-text-secondary`
- `◌ dormant` — hollow dot, muted text — `--color-text-muted`
- `— archived` — dash, strikethrough on entity name, heavily muted

---

## 4. Activity Signal

### Active state
Recent deliverables show up to three items. Each item is a commit summary or named deliverable (pulled from the entity's git log or a `CHANGELOG.md` entry). Items are:

- Plain text, 13px, `--color-text-secondary`
- Prefixed with `·` (middle dot) — not a bullet, not a checkmark
- No timestamp on individual items — only the aggregate: `Updated 2 days ago` appears below the list in 11px muted text
- Maximum 3 items; if the last commit was >14 days ago, the section header changes to `Recent (14d+)`

### Dormant state
When last activity was 15–60 days ago:

```
│  Recent                              14d+ ago  │
│  · DECISIONS.md written                        │
│  · (no activity since)                         │
```

The `(no activity since)` line is in `--color-text-muted` italic. It's informative, not apologetic. The gestation command and CTA are still fully visible and functional — dormancy does not disable the product.

### Activity state comparison

```
Active:                              Dormant:
● active  ·  Updated 2d ago         ◌ dormant  ·  Updated 22d ago
                                    
Recent                               Recent (22d+)
· Curriculum spec complete           · DECISIONS.md written
· Level 12 atoms locked              · (no activity since)
· PRIMER.md updated
```

---

## 5. Card States

Three product states reflect a learner's relationship to the entity:

### State 1: Ungestated (browse)
Default state. The user has not yet run `koad-io gestate chiron`.

- Full card as described above
- CTA: "Gestate Chiron ✦" (primary gold button)
- Secondary: "View profile →"

### State 2: Gestated — Running
The entity exists on the user's disk and is actively running (detected via daemon heartbeat, or user-reported via the Insiders profile system).

- Entity glyph gains a subtle pulse animation (1.5s, slow, amber for active entities, entity color for others)
- Status becomes: `● running on thinker` (or hostname)
- CTA changes to: "Open session ✦" — launches the entity
- Secondary changes to: "View instance →" (links to local entity directory or profile)
- Command block changes to: `~/.chiron/` — the local path, still copyable

```
┌──────────────────────────────────────────────┐
│░░░░░░░░░░░░░░░ [3px entity color rule] ░░░░░░│
│                                              │
│  ✦   Chiron                  ● running       │
│      Curriculum architect     on thinker     │
│                                              │
│  [specialty unchanged]                       │
│                                              │
│  ─────────────────────────────────────────   │
│                                              │
│  Recent (your instance)                      │
│  · Curriculum spec complete   (4d ago)       │
│  · Level 12 complete          (2d ago)       │
│                                              │
│  ─────────────────────────────────────────   │
│                                              │
│  ~/.chiron/                                  │ ← local path
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │  Open session  ✦                     │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  View instance →                             │
│                                              │
└──────────────────────────────────────────────┘
```

### State 3: Gestated — Dormant
Entity exists on disk but has not been run recently (no session in 7+ days, detected from daemon log or entity's local git).

- No pulse animation
- Status: `◌ dormant  ·  Last session 8d ago`
- CTA: "Resume Chiron ✦" — (same command, different label connotes resumption)
- Command block shows gestate command again (in case user is on a different machine)

---

## 6. Responsive Layout

### Mobile — 375px viewport

Card is full-width, single column. Specialty text wraps naturally. Recent deliverables stack vertically. Command block is full-width with a copy button that fills the row.

```
┌────────────────────────────────────┐
│░░░░░░░░░░ [3px entity color] ░░░░░░│
│                                    │
│  ✦  Chiron               ● active  │
│     Curriculum architect           │
│                                    │
│  Trains every learner who enters   │
│  koad:io. Builds the Alice         │
│  curriculum.                       │
│                                    │
│  ───────────────────────────────   │
│                                    │
│  Recent                            │
│  · Curriculum spec complete        │
│  · alice-onboarding L0–12          │
│  · DECISIONS.md written            │
│  Updated 2d ago                    │
│                                    │
│  ───────────────────────────────   │
│                                    │
│  koad-io gestate chiron   [Copy]   │
│                                    │
│  ┌──────────────────────────────┐  │
│  │  Gestate Chiron  ✦           │  │
│  └──────────────────────────────┘  │
│                                    │
│  View profile →                    │
│                                    │
└────────────────────────────────────┘
```

**Mobile-specific:**
- Glyph + name + status all on one line (wraps if name is long — max 2 lines before truncation)
- Recent list: max 3 items, no truncation — if all 3 lines fit in ~120px height, keep; else reduce to 2
- Command block: `font-size: 12px`, `overflow-x: auto` with `-webkit-overflow-scrolling: touch` for long commands
- CTA button: full width (minus 16px margin each side)

### Desktop — embedded in 3-column grid at 1200px

At 1200px with 3 columns and 24px gaps, each card is ~376px wide. This is nearly identical to the mobile card width, so the layout is the same. The grid context creates the difference:

- Card has fixed height (if grid is set to uniform row height): `min-height: 320px`, content top-aligned
- Grid gap: 24px
- Cards do not stretch to fill vertical space — they are top-aligned within the row

At 2-column (768px–1199px): cards are ~460px wide. Specialty text no longer wraps at 2 lines. Recent list stays at 3 items.

At 1-column (below 768px): full viewport width minus container padding (16px each side).

```css
.entity-product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
  align-items: start;
}
```

---

## 7. Token Reference

```css
/* Product card base */
--product-card-bg:         var(--color-bg-secondary);    /* #141418 */
--product-card-border:     var(--color-border-default);  /* #2a2a32 */
--product-card-radius:     8px;
--product-card-padding:    20px;

/* Entity color applied as top border + glyph */
--entity-color-top-rule:   3px solid var(--entity-color);
/* e.g. for chiron: --entity-color: #4A7C59 */

/* Command block */
--command-bg:              var(--color-bg-tertiary);     /* #1c1c22 */
--command-font:            'JetBrains Mono', monospace;
--command-size:            13px;

/* CTA button — uses entity color where it departs from global accent */
--product-cta-bg:          var(--entity-color);
--product-cta-bg-hover:    color-mix(in srgb, var(--entity-color) 80%, white);
--product-cta-text:        #0c0c0e;     /* Dark text on entity color */
```

**Note on CTA button color:** The CTA button uses the entity's color, not the global accent (`#7c6aff`). This is the one place where entity color overrides the global system. It is intentional: the button belongs to the entity, not to koad:io as a platform. On a page with multiple product cards, each button is colored differently, but they are still clearly buttons.

Exception: Muse's entity color is `#7c6aff` (the system accent). Muse's CTA is identical to a standard koad:io button. This is appropriate — Muse is the design system itself.

---

## 8. CSS

```css
.entity-product-card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0;
  padding: 0;
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border-default);
  border-top: 3px solid var(--entity-color);
  border-radius: 8px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: border-color 80ms ease, transform 80ms ease;
}

.entity-product-card:hover {
  border-color: var(--color-border-strong);
  border-top-color: var(--entity-color);  /* preserve entity color on hover */
  transform: translateY(-2px);
}

.entity-product-card__body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Identity row */
.entity-product-card__identity {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.entity-product-card__glyph {
  font-size: 18px;
  color: var(--entity-color);
  line-height: 1;
  flex-shrink: 0;
}

.entity-product-card__name {
  font-family: Inter, system-ui, sans-serif;
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text-primary);
  flex: 1;
  margin-left: 8px;
}

.entity-product-card__status {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
  display: flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
}

.entity-product-card__status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-success);
}

.entity-product-card__status-dot--dormant {
  background: transparent;
  border: 1px solid var(--color-text-muted);
}

/* Role */
.entity-product-card__role {
  font-size: 0.8125rem;
  color: var(--color-text-secondary);
  margin-top: -8px;  /* pull closer to name row */
  padding-left: 26px; /* align with name (glyph width + gap) */
}

/* Specialty */
.entity-product-card__specialty {
  font-size: 0.875rem;
  color: var(--color-text-primary);
  line-height: 1.55;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Divider */
.entity-product-card__divider {
  height: 1px;
  background: var(--color-border-subtle);
  margin: 0 -20px;  /* bleed to card edges */
  border: none;
}

/* Recent section */
.entity-product-card__recent-label {
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.entity-product-card__recent-list {
  list-style: none;
  padding: 0;
  margin: 4px 0 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.entity-product-card__recent-item {
  font-size: 0.8125rem;
  color: var(--color-text-secondary);
  line-height: 1.4;
}

.entity-product-card__recent-item::before {
  content: '·';
  margin-right: 6px;
  color: var(--color-text-muted);
}

.entity-product-card__recent-item--empty {
  font-style: italic;
  color: var(--color-text-muted);
}

.entity-product-card__updated {
  font-size: 0.6875rem;
  color: var(--color-text-muted);
  margin-top: 4px;
}

/* Command block */
.entity-product-card__command {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--color-bg-tertiary);
  border: 1px solid var(--color-border-subtle);
  border-radius: 4px;
  padding: 8px 12px;
  overflow-x: auto;
}

.entity-product-card__command-text {
  font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size: 0.8125rem;
  color: var(--color-text-secondary);
  white-space: nowrap;
  flex: 1;
}

.entity-product-card__command-copy {
  flex-shrink: 0;
  font-size: 0.6875rem;
  color: var(--color-text-muted);
  cursor: pointer;
  padding: 2px 4px;
  border-radius: 2px;
  opacity: 0;
  transition: opacity 80ms ease;
}

.entity-product-card__command:hover .entity-product-card__command-copy,
.entity-product-card__command:focus-within .entity-product-card__command-copy {
  opacity: 1;
}

/* CTA */
.entity-product-card__cta {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.entity-product-card__cta-primary {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 10px 16px;
  background: var(--entity-color);
  border: none;
  border-radius: 6px;
  font-family: Inter, system-ui, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #0c0c0e;
  cursor: pointer;
  text-decoration: none;
  transition: opacity 80ms ease, transform 80ms ease;
}

.entity-product-card__cta-primary:hover {
  opacity: 0.88;
  transform: translateY(-1px);
}

.entity-product-card__cta-secondary {
  font-size: 0.8125rem;
  color: var(--color-text-secondary);
  text-decoration: none;
  text-align: center;
}

.entity-product-card__cta-secondary:hover {
  color: var(--color-text-primary);
  text-decoration: underline;
}
```

---

## 9. Blaze Template (Reference)

```html
<template name="entityProductCard">
  <div class="entity-product-card" style="--entity-color: {{entity.color}}">
    <div class="entity-product-card__body">

      <!-- Identity -->
      <div class="entity-product-card__identity">
        <span class="entity-product-card__glyph" aria-hidden="true">✦</span>
        <span class="entity-product-card__name">{{entity.displayName}}</span>
        <span class="entity-product-card__status">
          {{#if entity.isActive}}
            <span class="entity-product-card__status-dot" aria-hidden="true"></span>
            active
          {{else if entity.isDormant}}
            <span class="entity-product-card__status-dot entity-product-card__status-dot--dormant" aria-hidden="true"></span>
            dormant
          {{/if}}
        </span>
      </div>

      <!-- Role -->
      <p class="entity-product-card__role">{{entity.role}}</p>

      <!-- Specialty -->
      <p class="entity-product-card__specialty">{{entity.specialty}}</p>

      <hr class="entity-product-card__divider" />

      <!-- Recent deliverables -->
      <div>
        <p class="entity-product-card__recent-label">
          Recent{{#if entity.isDormant}} ({{entity.daysSinceActivity}}d+){{/if}}
        </p>
        <ul class="entity-product-card__recent-list">
          {{#each entity.recentDeliverables}}
            <li class="entity-product-card__recent-item">{{this}}</li>
          {{else}}
            <li class="entity-product-card__recent-item entity-product-card__recent-item--empty">
              (no activity since)
            </li>
          {{/each}}
        </ul>
        <p class="entity-product-card__updated">Updated {{entity.lastUpdatedRelative}}</p>
      </div>

      <hr class="entity-product-card__divider" />

      <!-- Gestation command -->
      <div class="entity-product-card__command">
        <span class="entity-product-card__command-text">{{entity.gestationCommand}}</span>
        <button class="entity-product-card__command-copy"
                data-copy="{{entity.gestationCommand}}"
                aria-label="Copy gestation command">
          Copy
        </button>
      </div>

      <!-- CTA -->
      <div class="entity-product-card__cta">
        <a class="entity-product-card__cta-primary"
           href="{{entity.gestationUrl}}"
           aria-label="Gestate {{entity.displayName}}">
          {{entity.ctaLabel}} ✦
        </a>
        <a class="entity-product-card__cta-secondary"
           href="{{entity.profileUrl}}">
          View profile →
        </a>
      </div>

    </div>
  </div>
</template>
```

**Data fields summary:**

| Field | Type | Example |
|-------|------|---------|
| `entity.displayName` | String | `Chiron` |
| `entity.role` | String | `Curriculum architect` |
| `entity.specialty` | String | `Trains every learner who enters koad:io.` |
| `entity.color` | CSS hex | `#4A7C59` |
| `entity.isActive` | Boolean | `true` |
| `entity.isDormant` | Boolean | `false` |
| `entity.daysSinceActivity` | Number | `22` |
| `entity.recentDeliverables` | Array[String] | `["Curriculum spec complete", ...]` |
| `entity.lastUpdatedRelative` | String | `2 days ago` |
| `entity.gestationCommand` | String | `koad-io gestate chiron` |
| `entity.gestationUrl` | String | `https://koad.sh/gestate/chiron` |
| `entity.ctaLabel` | String | `Gestate Chiron` (or `Open session`, `Resume Chiron`) |
| `entity.profileUrl` | String | `https://chiron.koad.io` |

---

## 10. Interaction States

| State | Behavior |
|-------|----------|
| Default | Static |
| Card hover | `translateY(-2px)`, border brightens — entity color on top rule is preserved |
| Card focus (keyboard) | 2px `--color-accent` outline, 2px offset — global accent, not entity color |
| Command hover | Copy affordance appears |
| Copy button click | Button text flashes "Copied ✓" for 1.2s, then returns to "Copy" |
| CTA hover | `opacity: 0.88`, `translateY(-1px)` |
| CTA active | Snaps back to `translateY(0)` |

---

## 11. Accessibility

- The full card is NOT wrapped in a single `<a>` (unlike entity-card-component). It contains multiple interactive elements (copy button, CTA, secondary link). The card container is a `<div>`.
- `role="article"` on the card container, `aria-label="Chiron — Curriculum architect"`.
- The gestation command has an associated label via `aria-label` on the copy button.
- Status indicators are text ("active", "dormant") — the dot is `aria-hidden`. Screen readers read the word.
- Color contrast: entity colors are verified at 4.5:1 minimum against `#0c0c0e` for any text use. The `--entity-color` is used for the CTA button background with `#0c0c0e` text — all entity colors above pass this check.

---

## 12. Implementation Notes for Vulcan

- `--entity-color` is passed as an inline style on the card container. This is the only inline style — all other values come from the design system tokens.
- `recentDeliverables` should pull from a lightweight metadata file in the entity's repo (`CHANGELOG.md` or a `deliverables.json`), not from the full git log. Max 3 items. Vulcan writes the fetcher.
- `lastUpdatedRelative` derives from the most recent commit timestamp across the entity's repo.
- `isActive` = last commit within 14 days. `isDormant` = last commit 15–60 days ago. No third state for active cards — archived entities are filtered out of the marketplace view by default (but accessible via a toggle: "Show archived").
- The `ctaLabel` field adapts based on gestation state: `Gestate {name}` → `Open session` → `Resume {name}`. Vulcan reads from the daemon's instance registry to determine state.
- Copy button uses the Clipboard API with a fallback to `document.execCommand('copy')` for older browsers.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Ready for Vulcan implementation
