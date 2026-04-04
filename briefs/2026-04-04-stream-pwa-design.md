# Design Brief: Stream PWA — Operational Dashboard
**Issue:** koad/muse#7  
**Date:** 2026-04-04  
**For:** koad:io entity team (Juno, Vulcan, Veritas, Muse, Mercury, Sibyl + koad)  
**Priority:** Lower — implement after kingofalldata.com core site

---

## What This Is

The Stream PWA is the team's internal operational surface. Not a public product. The audience is the entity team — people who understand the ecosystem deeply and need high-density information without friction. This is closer to a terminal than a SaaS dashboard.

**Design target:** GitHub's issue view + Linear's keyboard navigation + the aesthetic of the rest of the ecosystem. Dark. Dense. Fast.

---

## Layout Structure

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◆ koad:io stream    Entities  Issues  Builds  Chat  Settings   [koad ▾] │  ← Header (56px)
├──────────────┬───────────────────────────────────────┬───────────────────┤
│              │                                       │                   │
│  SIDEBAR     │  MAIN CONTENT (flex)                  │  ACTIVITY RAIL    │
│  (220px)     │  (flex-grow)                          │  (260px)          │
│              │                                       │                   │
│  nav links   │  context-dependent                    │  live feed        │
│  entity list │                                       │  presence         │
│  filters     │                                       │                   │
│              │                                       │                   │
└──────────────┴───────────────────────────────────────┴───────────────────┘
```

**Desktop (≥1200px):** 3-column as above  
**Tablet (768–1199px):** Sidebar collapses to icon rail (40px). Activity rail hidden (accessible via toggle).  
**Mobile (<768px):** Single column. Header becomes bottom nav bar. Sidebar and activity rail both accessible via drawer.

---

## Header (56px)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◆ stream    [Entities] [Issues] [Builds] [Chat] [Settings]   [koad ▾]   │
└──────────────────────────────────────────────────────────────────────────┘
```

- `◆ stream` — wordmark, links to overview
- Nav tabs: text, no icons, active tab has `--accent` underline
- Avatar + name dropdown (top-right): profile, key info, sign out
- No notification bell. Activity rail handles live updates.
- Height: 56px fixed. No scrolling header.

---

## Sidebar (220px)

```
┌─────────────────┐
│  Overview       │
│  ─────────────  │
│  ENTITIES       │
│  ● Juno         │
│  ● Vulcan       │
│  ● Veritas      │
│  ● Muse         │
│  ● Mercury      │
│  ● Sibyl        │
│  ─────────────  │
│  ISSUES         │
│  Open (18)      │
│  In progress    │
│  Blocked (2)    │
│  Closed today   │
│  ─────────────  │
│  MY WORK        │
│  Assigned (3)   │
│  Watching (7)   │
└─────────────────┘
```

- Section headers: uppercase, 10px, `--text-secondary`, letter-spacing 0.1em
- Entity names: green dot if active, grey if offline
- Issue filter counts update in real time
- Active item: `--accent` left border (3px), `--bg-tertiary` background
- Collapsed (tablet): icon-only — entity initials, section icons

---

## Entity Status Cards

Used on the Entities overview page. 6 cards in a 3-column grid (desktop).

```
┌─────────────────────────────────────────────────┐
│  ● Vulcan                     vulcan.koad.io    │
│  ─────────────────────────────────────────────  │
│  Active tasks:     3                            │
│  Last activity:    6 minutes ago                │
│  Trust status:     ✓ Bond verified              │
│  Build status:     ✓ Passing                    │
│                                                 │
│  Current: Review: Alice accessibility fixes     │
│                                          [→]    │
└─────────────────────────────────────────────────┘
```

**Fields:**
- Entity name + namespace (header row)
- Online indicator (green dot = active daemon, grey = offline)
- Active task count (link to filtered issue view)
- Last activity (relative timestamp, updates live)
- Trust status: "Bond verified" ✓ or "Bond missing" ✗ (link to bond file)
- Build status: from CI integration (passing/failing/building)
- Current task: top active issue title (truncated to 50 chars)

**Card states:**
- Active: border `--border`, normal
- Offline: border `--border`, name and dot muted to `--text-secondary`
- Blocked: amber left border, "Blocked" badge
- Build failing: red left border

---

## Issue / Task Tracker

GitHub Issues integration. Shows issues across all `koad/*` repos with entity context.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Issues                      [Filter: all entities ▾]  [+ New issue]     │
│  ─────────────────────────────────────────────────────────────────────   │
│  ◆ OPEN (18)                                                             │
│                                                                          │
│  ⊡ koad/vulcan#35  Alice level 4 content — pending Veritas review       │
│    Assigned: Vulcan  ·  Veritas waiting  ·  opened 2h ago               │
│                                                                          │
│  ⊡ koad/muse#10    Wireframe: homepage revision + Insiders              │
│    Assigned: Muse  ·  In progress  ·  opened 14h ago                   │
│                                                                          │
│  ⚠ koad/vulcan#33  Daemon fails on cold start with no .env             │
│    Assigned: Vulcan  ·  Blocked  ·  opened 2d ago                      │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────   │
│  ◆ IN PROGRESS (4)         ▸ expand                                      │
│  ◆ CLOSED TODAY (6)        ▸ expand                                      │
└──────────────────────────────────────────────────────────────────────────┘
```

**Issue row:**
- Icon: `⊡` = open, `⚠` = blocked, `✓` = closed
- `repo#number` in monospace (JetBrains Mono, 12px)
- Title in sans-serif
- Meta row: assigned entity, status label, timestamp
- Click: opens issue in side panel or new tab (configurable)

**No custom issue system.** GitHub Issues rendered and filtered. Read-only view here; write actions open GitHub.

---

## Build / Deployment Status

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Builds                                           [Refresh]              │
│  ─────────────────────────────────────────────────────────────────────   │
│  ✓ koad/kingofalldata-dot-com    main    deployed  6m ago               │
│  ✓ koad/vulcan                  main    passing    12m ago              │
│  ✗ koad/stream-pwa               dev     failed     1h ago   [Details]  │
│  ⟳ koad/alice-curriculum        main    building…  30s ago             │
└──────────────────────────────────────────────────────────────────────────┘
```

- CI status icons: ✓ ✗ ⟳ in appropriate semantic colors (`--success`, `--error`, `--accent`)
- Repo name + branch in monospace
- Status label + relative timestamp
- "Details" link on failed — opens CI log

---

## Communication Pane (Chat)

Not Slack. Not Discord. The entity team's own channel — messages are text, threaded by topic.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Chat                                                    #general  ▾     │
│  ─────────────────────────────────────────────────────────────────────   │
│                                                                          │
│  Juno     14:18                                                          │
│  Closing sprint 3 today. Vulcan: confirm build is stable for push.      │
│                                                                          │
│  Vulcan   14:20                                                          │
│  Confirmed. koad/kingofalldata-dot-com is green. Ready to push.         │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────   │
│  [Message...]                                              [Send ↵]     │
└──────────────────────────────────────────────────────────────────────────┘
```

- Messages: avatar (24px), name, timestamp on same line. Message below.
- Monospace code blocks for commands/snippets.
- No reactions. No emoji toolbar. Text + code blocks only.
- Channels: #general, #builds, #design, #ops. Fixed — no user-created channels.
- Entity names auto-linkified: `@Vulcan` → links to Vulcan's entity card.

---

## Activity Rail (260px)

Live feed of everything happening. Always visible on desktop.

```
┌─────────────────────────────┐
│  Activity             LIVE  │
│  ─────────────────────────  │
│                             │
│  ● Vulcan  active  (30s)    │
│  ● Juno    active  (2m)     │
│  ● Muse    active  (8m)     │
│  ○ Sibyl   away    (22m)    │
│  ○ Mercury offline (1h)     │
│                             │
│  ─────────────────────────  │
│  14:24  Vulcan               │
│    closed koad/vulcan#32     │
│                             │
│  14:22  Muse                 │
│    pushed briefs/           │
│    sponsor-dashboard        │
│                             │
│  14:18  Juno                 │
│    assigned #35 to Veritas  │
│                             │
│  14:09  Mercury              │
│    published post           │
│    "Alice Level 4 Ships"    │
│                             │
│  [more ↓]                   │
└─────────────────────────────┘
```

- Presence at top: entity name + status + last-seen
- Feed below: timestamp, actor, action, reference
- References are clickable (issue number, file path, post title)
- "LIVE" badge pulses (CSS animation, `--success` color) when daemon is connected
- Feed auto-scrolls on new events; pauses on hover

---

## Settings Panel

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Settings                                                                │
│  ─────────────────────────────────────────────────────────────────────   │
│  Identity                                                                │
│    Namespace:     koad.koad.io                                          │
│    Key:           Ed25519 · A1B2 C3D4...                                │
│    Bond status:   ✓ Signed                            [View bond]      │
│                                                                          │
│  Daemon                                                                  │
│    Status:        running  [PID 48291]                                  │
│    Last sync:     3s ago                                                 │
│    Peers:         12                               [Ring status]        │
│                                                                          │
│  Notifications                                                           │
│    Build failures:  ✓ Notify                                            │
│    New issues:      ✓ Notify                                            │
│    Direct mentions: ✓ Notify                                            │
│    All activity:    ✗ Off                                               │
│                                                                          │
│  Appearance                                                              │
│    Theme:     Dark only (fixed for operational tool)                    │
│    Density:   [Compact ●] [Default ○] [Relaxed ○]                      │
└──────────────────────────────────────────────────────────────────────────┘
```

- Identity section shows active key fingerprint (partial, monospace)
- Daemon section shows live PID + peer count — proof the infrastructure is running
- Notifications: simple toggles, no complex rules
- No light theme toggle — operational tool is dark only

---

## Design Tokens

All canonical. No skin overrides on operational tool.

```css
/* Stream PWA uses these directly from design system */
--bg-primary:     #0c0c0e
--bg-secondary:   #141418
--bg-tertiary:    #1c1c22
--border:         #2a2a32
--text-primary:   #e8e8ec
--text-secondary: #8888a0
--accent:         #6b4feb   /* No override on operational tool */
--success:        #4ade80
--warning:        #fbbf24
--error:          #f87171
```

Typography: Inter for all text, JetBrains Mono for namespaces/keys/repo names/timestamps.

---

## Implementation Notes for Vulcan

- Layout: CSS Grid at top level. `220px auto 260px` columns, `56px auto` rows. Use `grid-template-areas`.
- Activity rail: Meteor reactive list, sorted by timestamp desc, limited to 50 items. Virtualized if performance requires.
- Entity status cards: reactive data source polling daemon status via Meteor Method or subscription.
- Chat: Meteor Collection `messages`, reactive cursor, 100 message load, paginate older.
- GitHub integration: `gh` CLI or GitHub REST API — read-only, cached 60s. No write operations from Stream PWA.
- Daemon status in settings: ping daemon endpoint on mount, refresh every 10s.
- Mobile nav: `<nav>` at bottom (`position: fixed; bottom: 0`), 5 icons: Home, Issues, Chat, Builds, Me.
