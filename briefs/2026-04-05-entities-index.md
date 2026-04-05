# Design Brief: Entity Directory Index
**Date:** 2026-04-05
**Author:** Muse
**Route:** `kingofalldata.com/entities`
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation

---

## Strategic Context

This page exists because someone clicked "Browse all entities →" from the landing page. They already cleared the first conversion moment — they understand (or want to understand) what koad:io entities are. They are not a cold visitor. They're exploring.

The job here is not to explain the system again. It's to let the visitor find the entity that speaks to them, understand its role quickly, and either clone it or go deeper.

**The emotional register:** A library, not a store. These are real agents doing real work. The page should feel like an ops board you can browse — not a product catalogue. The design earns that feeling through density, live status, and honest gestating states rather than through decoration.

**The conversion goal:** One entity card clicked, leading to that entity's profile page. The directory is a gateway, not a destination.

---

## Page Structure

```
┌─────────────────────────────────────────────────────────────┐
│  1. PAGE HEADER        ← breadcrumb, title, count           │
│  2. CONTROLS           ← search + filter + sort             │
│  3. ENTITY GRID        ← all entity cards (full set)        │
│  4. GESTATING ROW      ← announced but not yet gestated     │
│  5. FOOTER             ← standard site footer               │
└─────────────────────────────────────────────────────────────┘
```

---

## Section 1: Page Header

Minimal. The user knows why they're here — they clicked a link. No pitch needed.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ← kingofalldata.com                                        │  ← quiet breadcrumb, 13px
│                                                             │
│  Entities                                                   │  ← Inter 700, 32px
│  19 entities in the koad:io ecosystem.                      │  ← Inter 400, 16px, --text-secondary
│  Each one is a git repo. Each one is cloneable.             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Title:** "Entities" — Inter 700, 32px, `--color-text-primary`. No subtitle above it, no decoration.

**Descriptor:** One sentence count + two facts. The count is dynamic (pulls from entity manifest). The two facts repeat the central koad:io claim — appropriate here because this is the first page where someone will see the full set and ask "wait, can I actually have all of these?"

**Breadcrumb:** "← kingofalldata.com" — 13px, `--color-text-secondary`, links to `/`. No full path hierarchy. One step up.

**No hero section.** No terminal snippet. No architecture pitch. That was the landing page's job. This page starts with controls.

---

## Section 2: Controls

Filter, sort, and search. Lightweight — this is not a database browser. The controls help; they do not dominate.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌─────────────────────────────────┐   [Sort: Recent ▾]    │
│  │  🔍  Search entities...         │                        │
│  └─────────────────────────────────┘                        │
│                                                             │
│  All  ·  Builder  ·  Researcher  ·  Designer  ·             │
│  Content  ·  Governance  ·  Infrastructure  ·  Education    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Search

- Single text input, client-side. No backend call.
- Placeholder: "Search entities..." (13px, `--color-text-muted`)
- Matches against: entity name, one-liner tagline, role tags.
- Match is substring, case-insensitive. Live filter as user types — no submit button.
- Input spec: `--color-bg-tertiary` background, 1px `--color-border-default` border, 8px radius, 40px height. The search icon (16px, `--color-text-secondary`) is inside the input on the left, decorative (not a button).
- When search is active and produces results: grid reflows to show only matches. No "0 results" empty state theatrics — just an honest count: "3 entities" under the controls bar.
- When search is active and produces no results: single line below the controls bar: "No entities match." — 14px, `--color-text-secondary`. No illustration, no suggestions, no pity.
- Clearing the input (×, 16px, appears when input has content) resets to the unfiltered grid.

### Filter Pills

Role-based filter. One active at a time. "All" is the default state.

| Label | Entities included |
|-------|------------------|
| All | Every entity (default) |
| Builder | vulcan |
| Researcher | sibyl |
| Designer | muse, iris |
| Content | faber, rufus, mercury, livy |
| Governance | juno, veritas, aegis, janus, vesta |
| Infrastructure | argus, salus |
| Education | alice, chiron |
| Finance | copia |
| Music | lyra |

**Pill spec:**
- Inactive: `--color-bg-secondary` background, 1px `--color-border-default` border, 6px radius, 28px height, 12px padding horizontal, 13px Inter 400, `--color-text-secondary`
- Active: `--color-accent` background (10% opacity via `--color-accent-subtle`), 1px `--color-accent` border, `--color-accent` text, Inter 600
- Hover: `border-color` steps toward `--color-text-secondary`, 80ms ease
- Pills wrap to a second row on narrow widths — do not force horizontal scroll

**A note on filter scope:** The filter categories are intentionally coarse. An entity often spans categories (Juno is governance *and* orchestration; Vesta is infrastructure *and* governance). The assignment above reflects each entity's primary function. Do not add subcategories or multi-select — that turns browsing into a query language, and this audience isn't here to run queries.

### Sort

Single dropdown. Two options only:

- **Recent** (default) — sort by last commit date, descending. Entities that have been active in the last 48 hours appear first, with their online dot visible.
- **Alphabetical** — sort by entity name A–Z.

Dropdown spec: `--color-bg-secondary` background, 1px `--color-border-default` border, 8px radius, 36px height, 13px Inter 400, `--color-text-secondary`. The ▾ caret is 12px, `--color-text-muted`. No custom dropdown component — native `<select>` with CSS override is sufficient.

### Controls layout

```
[search input — grows to fill space]   [sort dropdown — fixed width 140px]
[filter pills — full width row below, wraps freely]
```

Gap between search/sort row and filter row: 12px. Controls bar is sticky on scroll (position: sticky, top: 0, `--color-bg-primary` background, 16px vertical padding, border-bottom: 1px `--color-border-default`). The stickiness helps when the user is scrolling a long grid and wants to re-filter without returning to the top.

**Mobile (< 640px):** Search and sort collapse to full-width rows (sort dropdown moves below search). Filter pills become a horizontal pill row that scrolls horizontally (no wrapping on mobile — scroll is natural and expected here). The scroll shadow (right edge, 16px `--color-bg-primary` fade) signals that there are more pills to the right.

---

## Section 3: Entity Grid

The full set of gestated entities. Cards from the Directory Card variant (`2026-04-04-entity-card-component.md`) with small additions specific to this context.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────┐ │
│  │  ●  [Avatar 48px]        │  │  ●  [Avatar 48px]        │ │
│  │     Juno                 │  │     Vulcan               │ │
│  │     juno.koad.io  1h ago │  │     vulcan.koad.io 2h ago│ │
│  │                          │  │                          │ │
│  │  Queen of the operation. │  │  Forge god. Ships        │ │
│  │  Business runs because   │  │  product. The hammer     │ │
│  │  Juno runs.              │  │  doesn't stop.           │ │
│  │                          │  │                          │ │
│  │  Governance              │  │  Builder                 │ │
│  │  Profile →               │  │  Profile →               │ │
│  └──────────────────────────┘  └──────────────────────────┘ │
│                                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────┐ │
│  │  [Avatar 48px]           │  │  [Avatar 48px]           │ │
│  │     Veritas              │  │     Mercury              │ │
│  │     veritas.koad.io 3d   │  │     mercury.koad.io 5d   │ │
│  │                          │  │                          │ │
│  │  Truth before it ships.  │  │  First to the world.     │ │
│  │  Catches the lie in      │  │  Fastest voice in        │ │
│  │  the machine.            │  │  the pantheon.           │ │
│  │                          │  │                          │ │
│  │  Governance              │  │  Content                 │ │
│  │  Profile →               │  │  Profile →               │ │
│  └──────────────────────────┘  └──────────────────────────┘ │
│                                                             │
│  (... grid continues ...)                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Card spec (Directory Card with additions)

The Directory Card variant from `2026-04-04-entity-card-component.md` is the base. Two additions for this context:

1. **Role tag** — a single pill tag below the bio, using the same category from the filter system. 11px JetBrains Mono, `--color-bg-tertiary` background, 1px `--color-border-default` border, 4px radius, 6px horizontal padding. This is one word (not a sentence) — "Builder", "Governance", "Education", etc. It doubles as a visual filter anchor: when the user applies a filter, the tag they filtered on is still visible on each matching card.

2. **"Profile →" text link** — below the role tag. `--color-accent`, 13px. Underline on hover. Routes to `/entities/{entity}`. This is the primary card action.

The entire card remains clickable (it is an `<a>` wrapping everything) with `/entities/{entity}` as its href. The "Profile →" text link is a visual affordance inside that same anchor — not a nested anchor. The card click and the text click lead to the same destination.

### Online dot

Present when last commit is within 48 hours. Absent (not grey, not dimmed) when entity has been quiet. Same spec as Directory Card: `--color-success` (#4ade80), 8px, top-right of avatar.

The online dot here has a subtle additional meaning on this page: because the sort default is "Recent", entities with the online dot will naturally cluster at the top. The dot is both a status signal and a visual anchor for the most active section of the grid.

### Grid layout

```
Desktop (>= 1024px):   3 columns, gap 16px
Tablet  (640–1023px):  2 columns, gap 16px
Mobile  (< 640px):     1 column,  gap 12px
```

`display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));` achieves this without breakpoint overrides.

### Entity order (default, sort: Recent)

Determined at runtime by last commit date per entity repo (GitHub API, cached 5 minutes). The order below represents a typical state — do not hardcode it.

Gestated entities shown in the grid (active order at time of writing):
juno, vulcan, muse, sibyl, faber, alice, chiron, veritas, mercury, vesta, iris, livy, argus, salus, janus, aegis, copia, lyra, rufus

---

## Section 4: The Gestating Row

Some entities are named, described, and assigned a role — but not yet gestated. They have no GitHub repo. Showing them as empty slots signals the ecosystem is growing without misleading anyone into thinking they can clone something that doesn't exist yet.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Coming.                                                    │  ← Inter 600, 14px, --text-secondary
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────┐ │
│  │     [○ dashed ring]      │  │     [○ dashed ring]      │ │
│  │     Hermez               │  │     Openclaw             │ │
│  │                          │  │                          │ │
│  │  Pending gestation.      │  │  Pending gestation.      │ │
│  │                          │  │                          │ │
│  │  · · ·                   │  │  · · ·                   │ │
│  └──────────────────────────┘  └──────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Gestating card design

The gestating card is a visual echo of the active card, deliberately incomplete:

- **Avatar:** No image. Instead: a 48px circle with a dashed border (2px dashed `--color-border-default`), `--color-bg-tertiary` fill. No initials. The empty ring signals: this space is reserved, not filled.
- **No online dot.** An ungestated entity is not online.
- **Name:** Rendered at the same Inter 700, 15px as active cards. The name is real — it has been chosen. The entity has an identity, it just doesn't have a body yet.
- **Domain:** Omitted entirely. There is no `*.koad.io` domain until the entity is gestated.
- **Timestamp:** Omitted.
- **Bio:** "Pending gestation." — 13px, `--color-text-muted`. Italic. Not an apology — a status. The period makes it complete.
- **Role tag:** Shown if the entity's role is known (most are). Same pill spec as active cards, but background and border use `--color-bg-tertiary` and `--color-border-default` (not the standard category visual weight) — it reads as a placeholder rather than a confirmed label.
- **"Profile →" link:** Absent. There is no profile page to link to.
- **Card interactivity:** The card is not a link. `cursor: default`. Hover does not produce `translateY(-2px)`. It does not animate. It simply sits there, waiting.
- **Opacity:** 60% on the entire card (`opacity: 0.6`). This communicates "not yet" without requiring a label that says "not yet."

### Gestating section label

"Coming." — Inter 600, 14px, `--color-text-secondary`. Same level of visual weight as a filter category label, not a section title. A thin horizontal rule above it (1px `--color-border-default`) separates the gestating row from the active grid. The rule signals a boundary — these are not the same kind of entity cards below.

### Gestating entities at time of writing

Entities announced but not yet gestated: entities whose names appear in TEAM_STRUCTURE.md or GTD_ROADMAP.md but whose GitHub repos do not yet exist. Vulcan will determine the runtime list — this page should derive it from the entity manifest, not hardcode it.

### Why show gestating entities at all

Three reasons:
1. **Anticipation signal.** The ecosystem has a roadmap. Showing named entities-to-come demonstrates intentionality, not just activity.
2. **Breadth proof.** A visitor who sees 19 active entities and 4 more gestating understands this is a system, not a collection of repos.
3. **Honesty.** Hiding these entities would make the directory look smaller than the ecosystem actually is. Showing them with clear "pending" treatment is more honest than either hiding them or misrepresenting them as available.

### What not to do with gestating cards

- Do not add a "Notify me when available" mechanism. That is an email capture in disguise. Visitors who want to track progress can watch the GitHub repos or follow koad.
- Do not add a progress bar or "X% complete" on gestating cards. Gestation is not a staged process from the user's perspective — it happens and then it's done.
- Do not animate the gestating card differently from the active cards (no pulse, no shimmer). Skeleton loaders signal "data is loading" — these aren't loading, they're planned. Static opacity is the correct treatment.

---

## Section 5: Footer

Standard site footer. Same spec as landing page brief (`2026-04-05-landing-page.md`, Section 6).

```
kingofalldata.com         GitHub   Docs   Blog   Insiders

© 2026 koad:io            Privacy  Terms  Contact

[key icon]  Your files. Your keys. Your agent.
```

No deviations from the standard footer on this page.

---

## Mobile Layout

### Full spec

**Controls:**
- Search input: full-width, 40px height
- Sort dropdown: full-width row below search, left-aligned label
- Filter pills: horizontal scroll row (no wrapping). Right-edge fade shadow signals overflow. Pills do not wrap.

**Grid:** Single column. Full-width cards. The Directory Card in single-column layout has slightly more horizontal breathing room — the bio may run to 3 lines at this width; that is acceptable.

**Gestating row:** Same single-column treatment. Gestating cards are full-width.

**Sticky controls bar:** Remains sticky on mobile. The filter pills scroll within the sticky bar — the bar height adjusts to accommodate a single-row pill scroller (not wrapping, scrolls horizontally). This keeps the sticky bar at a fixed height rather than growing unpredictably.

**Page header:** Single column, same copy. Slightly smaller title (28px instead of 32px on mobile).

---

## Page-Level Design Notes

### Layout

```
max-width: 1100px
padding: 0 var(--space-5)    /* 20px sides, mobile */
padding: 0 var(--space-8)    /* 32px sides, >= 640px */

Section gap: var(--space-12) /* 48px between sections */
Controls to grid: var(--space-6) /* 24px */
```

The 1100px max-width matches the landing page, because both pages share the entity grid. The grid is the reason for the width.

### Typography

Consistent with koad:io design system v1.1. No deviations from the landing page spec.

### Color

Standard palette. No domain skin deviations. The entity profile pages may have domain skins; the directory does not. The directory is neutral ground.

### Animation

Same policy as landing page: no entrance animations, no scroll reveals. The only motion:
- Card hover: `transform: translateY(-2px)` + `border-color` transition 80ms ease
- Filter pill active state: `background-color`, `border-color`, `color` transitions 80ms ease
- Search clear button (×): `opacity` transition 80ms ease (appears when input has content)

Everything else is static.

---

## Data Requirements

| Data | Source | Cache |
|------|--------|-------|
| Entity list (names, taglines, roles) | Static manifest (entity YAML or JSON) | Bust on deploy |
| Entity avatar URLs | GitHub API: `GET /users/{entity}/avatar_url` | 15 minutes |
| Entity last commit date (for sort + online dot) | GitHub API: `GET /repos/koad/{entity}/commits?per_page=1` | 5 minutes |
| Gestating entity list | Static manifest (entities with `gestated: false`) | Bust on deploy |

**No pagination.** The entity count is bounded (< 30 entities in the foreseeable future). The full grid renders at once. Infinite scroll or pagination would be disproportionate to the data size and would break the "library" feel.

**Client-side filtering and sorting** operate on the data already loaded — no additional API calls on filter change.

---

## Anti-Patterns (Do Not Apply)

- No infinite scroll or pagination
- No "Featured entities" section above the grid — the sort order does that job
- No rating or star system on cards
- No comparison table
- No "Recently viewed" sidebar
- No advertisement placement for gestating entities ("coming soon — be the first")
- No empty state illustrations — missing entities are shown via gestating cards, not blank space with an astronaut graphic
- No chatbot widget on this page
- No cookie banner (this page is static in the data-capture sense — no form, no tracking)

---

## Relationship to Other Work

| Brief | Relationship |
|-------|-------------|
| `2026-04-05-landing-page.md` | Landing page "Browse all entities →" links here. This page is the destination. Share the same footer. |
| `2026-04-05-entity-profile-page.md` | Each entity card's "Profile →" link routes to that spec. This page feeds the profile pages. |
| `2026-04-04-entity-card-component.md` | Grid uses the Directory Card variant. Role tag and "Profile →" link are the two additions on top of the base spec. Gestating cards use a distinct visual treatment (dashed ring, muted opacity). |
| `2026-04-05-entity-descriptions.md` | Entity one-liner taglines from that brief are the bio field in each card. Render verbatim — no truncation needed at this card width. |
| `2026-04-04-domain-skins-design.md` | Domain skins do not apply on the directory page. The page is neutral. Skins live on entity profile pages and Alice's section. |

---

## Implementation Notes for Vulcan

**Route:** `/entities` — static page at build time, hydrated client-side for GitHub data.

**Entity manifest format (suggestion):**

```json
[
  {
    "name": "juno",
    "display": "Juno",
    "tagline": "Queen of the operation. Business runs because Juno runs.",
    "role": "Governance",
    "gestated": true,
    "github": "koad/juno"
  },
  {
    "name": "hermez",
    "display": "Hermez",
    "tagline": null,
    "role": "Infrastructure",
    "gestated": false,
    "github": null
  }
]
```

**Filter implementation:**

```javascript
const filtered = entities.filter(e => {
  const matchesRole = activeFilter === 'All' || e.role === activeFilter;
  const q = searchQuery.toLowerCase();
  const matchesSearch = !q || (
    e.name.includes(q) ||
    (e.tagline && e.tagline.toLowerCase().includes(q)) ||
    (e.role && e.role.toLowerCase().includes(q))
  );
  return matchesRole && matchesSearch && e.gestated;
});
```

Gestating entities are always excluded from the filter results — they appear in the fixed gestating row below the grid, regardless of filter state.

**Sort implementation:**

```javascript
const sorted = [...filtered].sort((a, b) => {
  if (sortOrder === 'alphabetical') return a.name.localeCompare(b.name);
  // 'recent': sort by lastCommitDate descending, nulls last
  if (!a.lastCommitDate) return 1;
  if (!b.lastCommitDate) return -1;
  return new Date(b.lastCommitDate) - new Date(a.lastCommitDate);
});
```

**Online detection:** Same spec as entity profile page — last commit within 48 hours → green dot. Computed once when GitHub data loads; not re-checked on each render.

**SSR note:** Render the entity names and taglines server-side (from the static manifest). Hydrate avatars and online status client-side. This ensures the page is meaningful and fast on first paint even if the GitHub API is slow.

**Accessibility:**

- Filter pills are `<button>` elements with `aria-pressed` state. The active filter is announced on change.
- Search input has `aria-label="Search entities"`.
- Grid uses `<ul>` with `<li>` wrappers per card. Cards are `<a>` inside `<li>`.
- Gestating cards are `<div>` (not `<a>`) — they are not interactive. `aria-label="{Name} — pending gestation"` on each.
- Sort dropdown is a native `<select>` — keyboard accessible by default.

**SEO:**
- Page title: `Entities — koad:io`
- Meta description: "All koad:io entities. Each one is a git repo. Each one is cloneable. Browse and find the one that speaks to you."
- OG card: "Entities — koad:io" with the entity count.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
