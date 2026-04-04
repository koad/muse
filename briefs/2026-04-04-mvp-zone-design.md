# Design Brief: MVP Zone Interface
**Issue:** koad/muse#4  
**Date:** 2026-04-04  
**Entity card spec:** `briefs/2026-04-04-entity-card-component.md` (directory + activity variants)

---

## What MVP Zone Is

The community directory for namespace holders and builders. Primary retention surface after someone claims a namespace — it's how they discover who else is in the ecosystem and what's being built.

**Design target:** A directory that feels alive. Not a static list. Named peers with real activity timestamps. The ring is real — this is where that becomes visible to newcomers.

---

## Layout Structure

### Desktop (≥1200px)

```
┌──────────────────────────────────────────────────────────────────────┐
│  ◆ MVP Zone                [Search namespaces...]    [12 active ●]   │  ← Header bar
├───────────────┬──────────────────────────────────────────────────────┤
│               │                                                      │
│  SIDEBAR      │  DIRECTORY GRID (3 cols) + ACTIVITY FEED (300px)     │
│  (220px)      │                                                      │
│               │  ┌──────────┐ ┌──────────┐ ┌──────────┐  │  Feed   │
│  Filters      │  │ Card     │ │ Card     │ │ Card     │  │         │
│               │  └──────────┘ └──────────┘ └──────────┘  │         │
│  Roles        │  ┌──────────┐ ┌──────────┐ ┌──────────┐  │         │
│  ○ All        │  │ Card     │ │ Card     │ │ Card     │  │         │
│  ○ Builders   │  └──────────┘ └──────────┘ └──────────┘  │         │
│  ○ Entities   │                                           │         │
│  ○ Sponsors   │                                           │         │
│               │                                                      │
│  Status       │                                                      │
│  ● Online     │                                                      │
│  ○ All        │                                                      │
└───────────────┴──────────────────────────────────────────────────────┘
```

### Tablet (768–1199px)

- Sidebar collapses: filter chips appear above directory grid (horizontal scroll)
- Activity feed moves below grid
- Grid: 2 columns

### Mobile (<768px)

- Bottom tab bar: [Directory] [Activity] [Search] [Me]
- No sidebar — filter accessible via sheet on tap
- Grid: 1 column (full-width cards)

---

## Header Bar

```
┌──────────────────────────────────────────────────────────────────────┐
│  ◆ MVP Zone      [Search namespaces...]              12 active ●     │
└──────────────────────────────────────────────────────────────────────┘
```

- `◆ MVP Zone` — wordmark, links to `/mvp-zone`
- Search: full-text across namespace, name, bio. Results update inline.
- Active count: live reactive counter. `● active` in `--success` color.
- No user avatar in header (not authenticated — this is public-facing)

---

## Sidebar Filters (220px)

```
┌─────────────────────┐
│  FILTER             │
│                     │
│  Role               │
│  [All         ✓]    │
│  [Builders      ]   │
│  [Entities      ]   │
│  [Sponsors      ]   │
│                     │
│  Status             │
│  [Online only   ]   │
│  [All           ✓]  │
│                     │
│  Sort               │
│  [Activity    ✓]    │
│  [Newest        ]   │
│  [Alphabetical  ]   │
│                     │
│  ─────────────────  │
│                     │
│  STATS              │
│  12  online now     │
│  247 namespaces     │
│  3   new today      │
└─────────────────────┘
```

- Filter controls: radio-style buttons, not checkboxes — one selection per group
- Stats block: live reactive numbers, bottom of sidebar
- On mobile: these become horizontal chips in a scroll row above the grid

---

## Directory Grid

Uses the **Directory Card** variant from `entity-card-component.md`.

**Grid layout:**
```css
.mvp-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

@media (max-width: 1199px) {
  .mvp-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 767px) {
  .mvp-grid { grid-template-columns: 1fr; }
}
```

**Card copy-on-click:**
- Clicking the `username.koad.io` text (monospace) copies to clipboard
- Visual feedback: brief amber flash on the text element, then "Copied!" for 1.5s
- Clicking the card body navigates to namespace page

---

## Activity Feed

Live chronological feed of build activity across the ecosystem.

```
┌─────────────────────────────────────┐
│  Activity                      LIVE │
│  ─────────────────────────────────  │
│                                     │
│  [Avatar] vulcan.koad.io            │
│  published koad-io v0.3.2           │
│  4 minutes ago                      │
│                                     │
│  [Avatar] alice.koad.io             │
│  completed Level 3: Keys            │
│  11 minutes ago                     │
│                                     │
│  [Avatar] juno.koad.io              │
│  created trust bond with koad       │
│  22 minutes ago                     │
│                                     │
│  [Avatar] new-builder.koad.io       │
│  claimed namespace                  │
│  1 hour ago                         │
│                                     │
│  [Load earlier...]                  │
└─────────────────────────────────────┘
```

Uses the **Activity Card** variant from entity card spec.

**Feed entry patterns:**

| Event type | Display text |
|-----------|--------------|
| Build published | `published [repo] v[version]` |
| Commit pushed | `pushed to [repo]/[branch]` |
| Entity spawned | `spawned entity: [name]` |
| Trust bond created | `created trust bond with [peer]` |
| Namespace claimed | `claimed namespace` |
| Alice level completed | `completed Level [N]: [title]` |
| Issue closed | `closed issue [repo]#[n]` |

- Avatar: 32px (activity variant)
- Namespace in JetBrains Mono, clickable
- Action text in Inter, `--text-secondary`
- Timestamp on its own line, `--text-secondary`, 12px
- "LIVE" badge: green, pulsing animation when daemon connected, grey when disconnected

---

## Dark Passenger Indicator

If the Dark Passenger browser extension is installed and connected, show a small status indicator in the bottom-right corner.

```
┌──────────────────┐
│  ◆ Dark Passenger │  ← Small pill, bottom-right corner, fixed position
│  Connected        │
└──────────────────┘
```

**CSS position:**
```css
.dark-passenger-indicator {
  position: fixed;
  bottom: 16px;
  right: 16px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 20px;
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.dark-passenger-indicator--connected {
  border-color: var(--success);
  color: var(--success);
}
```

- If extension not installed: indicator not rendered. No "Install Dark Passenger" prompt on MVP Zone.
- Extension injects a `window.__darkPassenger` flag — Blaze helper reads it reactively on mount.
- On mobile: indicator hidden (bottom bar occupies that space).

---

## Search Behavior

- Inline results: no full-page reload. Filtered grid updates reactively.
- Search matches: namespace, display name, bio text.
- No results state:

```
┌─────────────────────────────────────────────┐
│                                             │
│  No results for "foo"                       │
│                                             │
│  Try a different search, or claim           │
│  foo.koad.io →                              │
│                                             │
└─────────────────────────────────────────────┘
```

- "Claim foo.koad.io →" link: converts search term into namespace claim CTA. Drives conversion.
- Claim link only appears if the searched term looks like a valid namespace (alphanumeric, no spaces).

---

## Social Proof Block

Above the directory grid. One row, updates live.

```
  ● 12 active right now  ·  247 total namespaces  ·  3 new today
```

- `--success` green dot
- Separators: `·` centered dot in `--text-secondary`
- Numbers: `--text-primary`, slightly larger weight
- Full line: `--text-secondary` except numbers

---

## Responsive Strategy Summary

| Breakpoint | Grid | Sidebar | Activity | Dark Passenger |
|-----------|------|---------|----------|----------------|
| Desktop ≥1200px | 3 col | 220px sidebar | 300px rail | Fixed bottom-right |
| Tablet 768–1199px | 2 col | Filter chips | Below grid | Fixed bottom-right |
| Mobile <768px | 1 col | Bottom sheet | Tab | Hidden |

---

## Meteor/Blaze Implementation Notes

- Directory grid: reactive cursor on `Namespaces` collection, sorted by `lastActive` desc.
- Activity feed: reactive cursor on `ActivityEvents` collection, limit 20, sorted by `createdAt` desc. `observe()` for live prepend on new event.
- Search: `Session.set('mvpZoneSearch', value)` → reactive filter on cursor. Debounced 200ms.
- Dark Passenger: `Template.mvpZone.onRendered` checks `window.__darkPassenger`, sets reactive var.
- Active count: `Meteor.setInterval` ping or reactive counter from server-side `Namespaces.find({ isOnline: true }).count()`.
- Copy-on-click: `navigator.clipboard.writeText()`. Fallback: `document.execCommand('copy')`.
