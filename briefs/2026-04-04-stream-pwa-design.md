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

---

## Activity Card Component

Each discrete action by an entity produces one activity card. Cards appear in the Activity Rail (compact) and in the expanded Activity feed view (full).

### Compact card (Activity Rail, 260px wide)

```
┌─────────────────────────────┐
│  14:24  ● Vulcan            │
│  closed koad/vulcan#32      │
│  "Alice accessibility fix"  │
└─────────────────────────────┘
```

- Timestamp: JetBrains Mono, 11px, `--text-secondary`. Relative ("2m ago") until >1h, then wall-clock.
- Entity name: same line as timestamp. Status dot inline (green = active, grey = idle, amber = blocked).
- Action line: sentence-cased verb + reference. Reference in `--accent` monospace if it's a repo/issue/commit link.
- Title: second line, truncated at 40 chars, `--text-secondary`.
- No border. Separated by 1px `--border` divider.
- Hover: `--bg-tertiary` background, full-width.

### Full card (Activity feed view, main content area)

```
┌──────────────────────────────────────────────────────────────────┐
│  ● Vulcan                                         2026-04-05 14:24 │
│  ──────────────────────────────────────────────────────────────── │
│  closed issue                                                     │
│  koad/vulcan#32 — Alice accessibility fix for keyboard nav        │
│                                                                   │
│  commit  7d95c39  main  "fix: keyboard nav focus trap"            │
│                                                        [→ GitHub]  │
└──────────────────────────────────────────────────────────────────┘
```

**Fields (full card):**
- Header row: entity name with status dot (left) + ISO timestamp (right, monospace, `--text-secondary`)
- Divider line
- Action label: verb in `--text-secondary` uppercase 10px (CLOSED ISSUE, PUSHED COMMIT, ASSIGNED, COMMENTED, PUBLISHED)
- Primary reference: repo + number + title. Full title, not truncated.
- Secondary reference (optional): commit hash (7 chars, monospace, `--accent`) + branch + message — only shown for push/close actions
- `[→ GitHub]` link aligned right, opens in new tab. Shown only on cards that have a GitHub URL.

**Card anatomy — data model:**
```
{
  entity:     "vulcan",
  action:     "closed",        // closed | pushed | assigned | commented | published | spawned | blocked
  ref_type:   "issue",         // issue | commit | post | entity | build
  ref_id:     "koad/vulcan#32",
  ref_title:  "Alice accessibility fix for keyboard nav",
  commit:     "7d95c39",       // optional
  branch:     "main",          // optional
  timestamp:  "2026-04-05T14:24:00Z",
  url:        "https://github.com/koad/vulcan/issues/32"
}
```

**Action verb palette:**
| verb | meaning |
|------|---------|
| `closed` | Issue closed |
| `opened` | Issue opened |
| `pushed` | Commit pushed |
| `assigned` | Issue assigned to entity |
| `commented` | Comment on issue |
| `published` | Post/content published |
| `spawned` | Entity session started |
| `blocked` | Entity marked an issue blocked |
| `merged` | PR merged |

---

## Multi-Entity View

The stream can be read in two modes, toggled by a control in the header bar.

### Mode A: Unified feed (default)

All entities' activity interleaved, sorted by timestamp descending. This is the default — it tells the operational story as a single timeline.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Activity                [● Unified] [⠿ Columns]         Filter: all ▾  │
│  ─────────────────────────────────────────────────────────────────────   │
│  14:24  ● Vulcan    closed  koad/vulcan#32 — Alice accessibility fix     │
│  14:22  ● Muse      pushed  briefs/sponsor-dashboard-design.md           │
│  14:18  ● Juno      assigned  koad/vulcan#35 → Veritas                   │
│  14:09  ○ Mercury   published  "Alice Level 4 Ships"                     │
│  13:55  ○ Sibyl     pushed  research/icm-synthesis.md                    │
│  ─────────────────────────────────────────────────────────────────────   │
│  [load more]                                                             │
└──────────────────────────────────────────────────────────────────────────┘
```

- Each row is one compact card rendered as a table row.
- Entity name is the visual anchor — bold, with status dot.
- Action + reference on same row where it fits. Overflow wraps to second line, indented 16px.
- Filter control (top-right): multi-select entity names, action types. Persisted to localStorage.

### Mode B: Column view

One column per entity. Shows each entity's recent actions in isolation. Useful when diagnosing a specific entity's output.

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│  Activity                [○ Unified] [● Columns]         Filter: all ▾           │
│  ─────────────────────────────────────────────────────────────────────────────   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ ● Juno       │  │ ● Vulcan     │  │ ● Muse       │  │ ○ Mercury    │         │
│  │ active 2m    │  │ active 30s   │  │ active 8m    │  │ offline 1h   │         │
│  │ ─────────── │  │ ─────────── │  │ ─────────── │  │ ─────────── │         │
│  │ 14:18        │  │ 14:24        │  │ 14:22        │  │ 14:09        │         │
│  │ assigned #35 │  │ closed #32   │  │ pushed brief │  │ published    │         │
│  │ → Veritas    │  │              │  │ sponsor-dash │  │ Alice L4     │         │
│  │              │  │ 14:11        │  │              │  │              │         │
│  │ 13:42        │  │ pushed #32   │  │ 13:50        │  │ 12:30        │         │
│  │ spawned      │  │ fix commit   │  │ pushed brief │  │ published    │         │
│  │ session      │  │              │  │ alice-ui     │  │ Day 5 post   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘         │
└───────────────────────────────────────────────────────────────────────────────────┘
```

- Columns: fixed-width 200px, scrollable independently (overflow-y: auto per column).
- Column header: entity name + status dot + last-seen.
- Each column shows the last 20 actions for that entity.
- Columns are horizontally scrollable if more than 4 entities visible on screen.
- Mobile: column view not available — unified only.

### Mode toggle control

```
[● Unified]  [⠿ Columns]
```

- Pill toggle in the subheader. Left = unified, right = columns.
- Persisted to localStorage as `stream.view_mode`.

---

## State Indicators

Entities exist in four operational states. Each state has a consistent visual language used everywhere the entity appears (sidebar dot, column header, activity card, entity status card).

### State definitions

| State | Meaning | Trigger |
|-------|---------|---------|
| **active** | Entity session running, activity within last 15 minutes | Daemon reports PID alive + recent git activity or GitHub event |
| **idle** | Session alive but no activity >15min | PID alive, no events |
| **offline** | No session detected | No PID, no recent events |
| **blocked** | Entity has an open issue flagged `blocked` | GitHub label `blocked` on assigned issue |

### Visual treatment

**Status dot:**
```
● = active   (--success #4ade80, 8px circle)
◐ = idle     (--text-secondary #8888a0, 8px circle, half-filled — CSS clip-path)
○ = offline  (--border #2a2a32, 8px circle, outline only)
⚠ = blocked  (--warning #fbbf24, 8px, triangle glyph replaces dot)
```

**Sidebar entity list:**
```
● Vulcan                 ← active: green dot, full-brightness name
◐ Juno                  ← idle: grey dot, slightly dimmed name (opacity 0.75)
○ Mercury               ← offline: outline dot, dimmed name (opacity 0.5)
⚠ Veritas               ← blocked: amber triangle, name at full brightness
```

**Entity status card (Entities overview page):**
- Active: card border `--border`, header row normal
- Idle: card border `--border`, last-seen timestamp turns amber if >30min
- Offline: card opacity 0.6, "Offline" badge in `--text-secondary`
- Blocked: left border 3px `--warning`, "Blocked" badge in amber, blocked issue title shown in card body

**Activity Rail presence section:**
```
┌─────────────────────────────┐
│  Presence                   │
│  ─────────────────────────  │
│  ● Vulcan    active   30s   │
│  ◐ Juno      idle     12m   │
│  ● Muse      active    8m   │
│  ○ Mercury   offline   1h   │
│  ⚠ Veritas   blocked   —    │
└─────────────────────────────┘
```

- Columns: dot + name + state label + duration. Monospace for duration.
- State label: `--text-secondary` except blocked which is `--warning`.
- Duration: time since last state change (not last activity).

**Column header (columns mode):**
```
┌──────────────────┐
│  ⚠ Veritas       │   ← blocked: amber triangle, name normal
│  blocked 2d      │   ← state + duration, amber text
│  ────────────── │
```

**"LIVE" indicator:**
The "LIVE" badge in the Activity Rail header indicates whether the daemon connection is active:
- Connected: `● LIVE` in `--success`, pulse animation (opacity 1 → 0.4 → 1, 2s infinite)
- Disconnected: `○ OFFLINE` in `--error`, no animation
- Reconnecting: `⟳ CONNECTING` in `--warning`, spin animation

---

## Mobile Layout (PWA)

Mobile is the primary read surface — koad checks entity status on the go. Design mobile-first; desktop is an expansion.

### Mobile breakpoint: <768px

**Bottom navigation bar (56px, fixed):**
```
┌──────────────────────────────────────────────┐
│  🏠 Home   📋 Issues   💬 Chat   🔨 Builds   👤 Me   │
└──────────────────────────────────────────────┘
```

No emoji in implementation — use simple geometric SVG icons:
- Home: diamond `◆` (matches brand wordmark)
- Issues: list icon
- Chat: message bubble
- Builds: CI/cog
- Me: circle (avatar)

Active tab: icon in `--accent`, label in `--accent`. Others: `--text-secondary`.

**Header (48px, simplified):**
```
┌──────────────────────────────────┐
│  ◆ stream          [koad ▾]  [≡] │
└──────────────────────────────────┘
```

- Wordmark left. Avatar + hamburger right.
- Hamburger opens a full-screen drawer with sidebar nav content.
- No tab bar in header on mobile — that's the bottom nav's job.

**Home view (mobile):**

```
┌──────────────────────────────────┐
│  ◆ stream             [koad ▾][≡]│
│  ────────────────────────────── │
│  Presence                        │
│  ● Vulcan  active   30s          │
│  ◐ Juno    idle     12m          │
│  ● Muse    active    8m          │
│  ○ Mercury offline   1h          │
│  ⚠ Veritas blocked   —           │
│  ────────────────────────────── │
│  Activity                  LIVE  │
│                                  │
│  14:24  ● Vulcan                 │
│  closed koad/vulcan#32           │
│  "Alice accessibility fix"       │
│                                  │
│  14:22  ● Muse                   │
│  pushed briefs/sponsor-dash      │
│                                  │
│  14:18  ◐ Juno                   │
│  assigned koad/vulcan#35         │
│  → Veritas                       │
│                                  │
│  [load more]                     │
│                                  │
└──────────────────────────────────┘
│  ◆   📋   💬   🔨   👤           │
└──────────────────────────────────┘
```

- Presence strip at top (horizontal scroll if >4 entities).
- Activity feed fills remaining height (`calc(100vh - 48px - 56px - presence_height)`).
- Each card: full-width, tap to expand. Tap opens GitHub URL in browser.

**Issues view (mobile):**

- Full-screen list. No sidebar filter — use a filter sheet (bottom sheet, swipe up).
- Each issue row: 60px tall, two-line layout (title + meta). Icon left, chevron right.
- Blocked issues shown first with amber left border.

**Entity detail (mobile, tap entity name):**

Full-screen modal or pushed route showing:
1. Entity name + state indicator (large, 24px)
2. Trust bond status
3. Active issues (list)
4. Recent activity (last 10 cards)
5. Link to GitHub profile

**Chat (mobile):**

Standard mobile chat layout. Messages take full width. Input bar pinned to bottom, above bottom nav. Bottom nav hides when keyboard is open (use `visualViewport` resize event).

**Builds (mobile):**

List view. Each build: icon + repo + branch + status + timestamp. Tap → opens CI in browser.

### Mobile typography adjustments

- Body text: 14px (up from desktop 13px for readability on small screens)
- Timestamps: 11px monospace (same as desktop)
- Card titles: 14px (same)
- No density control on mobile — always uses "Default" density

### PWA install prompt

On first visit from mobile browser, after 30 seconds:
- Bottom sheet: "Add Stream to your home screen for faster access." + Install button + Dismiss.
- Uses standard `beforeinstallprompt` Web API.
- No nag — dismissed means dismissed permanently (localStorage `pwa.install_dismissed = true`).

### Offline behavior

- Service worker caches the last known state of activity feed, presence, and issues.
- Offline indicator: "OFFLINE" badge replaces "LIVE" in the activity header.
- All data shows "last updated X ago" timestamp when offline.
- Write actions (creating issues) disabled offline — buttons disabled with tooltip "Offline — reconnecting."
