# Design Brief: Daemon Status Dashboard
**Date:** 2026-04-05
**Author:** Muse
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation
**Route:** `localhost:PORT/dashboard`

---

## What This Is

The daemon status dashboard is the operator's instrument panel. It surfaces the internal state of a running koad:io daemon: what entities are registered, what work is queued, what MongoDB and DDP connections look like, and what has happened recently.

**Audience:** koad or another operator checking on their kingdom. This is not for end users. No onboarding, no explanations, no consumer chrome.

**Design intent:** Dense. Functional. Consistent with the Stream PWA visual language. Think devtools panel, not SaaS product. The operator already knows what a passenger queue is. Show them the queue.

**Access:** Only accessible when the daemon is running locally. No auth beyond localhost. Ship it as a Meteor route served by the existing daemon HTTP server.

---

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ◆ daemon  v0.9.2  ·  thinker  ·  uptime 4h 12m  ·  ● connected      [?]  │  ← Bar (48px)
├───────────────────────────────────────────────────┬─────────────────────────┤
│                                                   │                         │
│  MAIN CONTENT (flex, scrollable)                  │  ACTIVITY FEED (280px)  │
│  (flex-grow)                                      │  (fixed, overflow-y)    │
│                                                   │                         │
│  ┌─────────────────────────────────────────────┐  │                         │
│  │  Overview                                   │  │                         │
│  └─────────────────────────────────────────────┘  │                         │
│  ┌─────────────────────────────────────────────┐  │                         │
│  │  Entity Roster                              │  │                         │
│  └─────────────────────────────────────────────┘  │                         │
│  ┌─────────────────────────────────────────────┐  │                         │
│  │  Passenger Queue                            │  │                         │
│  └─────────────────────────────────────────────┘  │                         │
│  ┌─────────────────────────────────────────────┐  │                         │
│  │  System Health                              │  │                         │
│  └─────────────────────────────────────────────┘  │                         │
│                                                   │                         │
└───────────────────────────────────────────────────┴─────────────────────────┘
```

- **Top bar (48px):** daemon identity + live connection status. Fixed. Does not scroll.
- **Main content:** left panel, scrollable, stacked sections. Width: `calc(100vw - 280px)`.
- **Activity feed:** right rail, 280px, fixed height, internal scroll.

---

## Top Bar (48px)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ◆ daemon  v0.9.2  ·  thinker  ·  uptime 4h 12m 33s           ● connected  │
└─────────────────────────────────────────────────────────────────────────────┘
```

- `◆ daemon` — wordmark. `◆` in `--accent`, "daemon" in `--text-primary`. Monospace.
- Version: `--text-secondary`, monospace, 12px.
- Hostname: separator `·`, then `hostname` value from daemon env. Monospace.
- Uptime: continuous counter, seconds precision. Updates every second via reactive source.
- Connection status (far right): `● connected` in `--success` when DDP live. `○ disconnected` in `--error` when not. `⟳ connecting` in `--warning` during reconnect, with spin.
- `[?]` link (far right): opens daemon README or `/docs` route in new tab. Low-profile — `--text-secondary`, no border.

---

## Section 1: Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Overview                                                                   │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  Daemon          v0.9.2  ·  PID 48291  ·  started 2026-04-05T10:14:38Z    │
│  MongoDB         ● connected  ·  mongodb://localhost:27017  ·  spawned     │
│  DDP             ● live  ·  12 subscribers                                  │
│  Entities        7 registered  ·  4 online  ·  1 locked  ·  2 offline     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Fields:**

| Row label | Content |
|-----------|---------|
| Daemon | Version · PID · ISO start timestamp |
| MongoDB | Connection status dot · URL · "spawned" or "external" badge |
| DDP | Live/offline dot · subscriber count (reactive, updates live) |
| Entities | Total registered · online count · locked count · offline count |

**Visual:**
- Label column: 100px, `--text-secondary`, 11px uppercase, letter-spacing 0.08em.
- Value column: `--text-primary`, 13px, monospace where technical (PIDs, URLs, timestamps).
- Status dots: `--success` / `--error` / `--warning` using same 8px circle convention as Stream PWA.
- "spawned" / "external" badge: 10px pill, `--bg-tertiary` fill, `--border` outline, `--text-secondary` text.

---

## Section 2: Entity Roster

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Entity Roster                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  NAME          STATUS    LAST HEARTBEAT   COMMIT     LOCKFILE              │
│  ─────────────────────────────────────────────────────────────────────────  │
│  ● juno        active    12s ago          7d95c39    —                     │
│  ● vulcan      active    30s ago          4a1b2c3    —                     │
│  ● muse        active    8m ago           de471ae    —                     │
│  ◐ veritas     idle      22m ago          1810031    —                     │
│  ⚠ mercury     locked    1h ago           ead9a98    mercury.lock          │
│  ○ sibyl       offline   3h ago           63fba0b    —                     │
│  ○ chiron      offline   —                —          —                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Columns:**

| Column | Width | Format |
|--------|-------|--------|
| Name | 120px | Status dot + entity name. Monospace. |
| Status | 80px | Text label: `active` / `idle` / `locked` / `offline`. Color-coded. |
| Last heartbeat | 140px | Relative time ("12s ago"), monospace. Blank if never. |
| Commit | 90px | 7-char hash, monospace, `--accent`. Blank if none. Links to entity's `gh repo view`. |
| Lockfile | 160px | Lockfile filename if one exists, `--warning` text. `—` if none. |

**Status color mapping:**

| Status | Dot | Label color |
|--------|-----|-------------|
| active | `--success` filled | `--success` |
| idle | `--text-secondary` half-filled | `--text-secondary` |
| locked | `--warning` filled | `--warning` |
| offline | `--border` outline | `--text-secondary` at 50% opacity |

**Row states:**
- Hover: `--bg-secondary` background.
- Locked row: left border 2px `--warning`.
- Offline row: full row at `opacity: 0.55`.
- Click row: expands inline detail (see below).

**Expanded row (on click):**

```
  ● juno     active    12s ago    7d95c39    —
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  entity_dir    /home/koad/.juno                                         │
  │  pid           91244  (claude)                                          │
  │  trust bond    ✓ koad → juno  (authorized-agent)                        │
  │  last commit   de471ae  "docs: correct Alice PR status"                 │
  │  passenger     ✓ registered  (juno.koad.io)                             │
  └─────────────────────────────────────────────────────────────────────────┘
```

No separate page. Inline accordion. Single click to toggle.

---

## Section 3: Activity Feed (right rail)

The live feed is the right-side 280px rail, visible at all times on desktop. It streams entity actions via DDP subscription.

```
┌───────────────────────────────┐
│  Activity               ● LIVE│
│  ─────────────────────────────│
│  [Pause ⏸]                   │
│  ─────────────────────────────│
│                               │
│  14:24  ● juno                │
│  committed  ~/.juno           │
│  de471ae  "docs: correct..."  │
│                               │
│  14:20  ● vulcan              │
│  closed  koad/vulcan#48       │
│  "governance note committed"  │
│                               │
│  14:18  ● muse                │
│  pushed  briefs/              │
│  daemon-dashboard.md          │
│                               │
│  13:55  ◐ veritas             │
│  commented  koad/juno#52      │
│  "cross-entity commit policy" │
│                               │
│  [load more ↓]                │
└───────────────────────────────┘
```

**Controls:**
- `● LIVE` badge: top-right of rail header. Pulses (opacity 1.0 → 0.4 → 1.0, 2s, ease-in-out) when connected. Stops pulsing when paused.
- `[Pause ⏸]` / `[Resume ▶]`: single button toggle below header rule. When paused, feed freezes and badge shows `⏸ PAUSED` in `--text-secondary`. New events are buffered. On resume, buffer flushes instantly.
- Auto-scroll: enabled by default. Pauses auto-scroll on manual scroll-up. Resumes when scrolled back to bottom.

**Event card (compact, feed):**
```
{timestamp}  {status-dot} {entity}
{action_label}  {reference}
{detail} (truncated 44 chars)
```

- `{timestamp}`: HH:MM wall clock. Monospace, 11px, `--text-secondary`.
- `{status-dot}`: 8px inline status circle (same color language as roster).
- `{entity}`: entity name, 13px, `--text-primary`, monospace.
- `{action_label}`: verb in 11px uppercase `--text-secondary`: COMMITTED / CLOSED / OPENED / PUSHED / COMMENTED / SPAWNED / BLOCKED / MERGED.
- `{reference}`: repo#number or file path. `--accent`, monospace, 12px. Clickable — opens GitHub or file in system default.
- `{detail}`: optional second line. Commit message or issue title. `--text-secondary`, 12px, truncated.
- Card separator: 1px `--border` divider. No card chrome (no box, no border-radius).
- Hover: `--bg-secondary` on full-width row.

**DDP subscription:** `entity.activity.feed`. Sorted by timestamp desc. Last 50 events retained client-side. Older events load on `[load more ↓]` click (no infinite scroll — explicit user action).

---

## Section 4: Passenger Queue

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Passenger Queue                                    [Refresh]               │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  QUEUED                                                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│  ⊞ vulcan   build: compile alice-curriculum v2    submitted 2m ago         │
│  ⊞ mercury  task: draft Day 7 distribution post   submitted 5m ago         │
│                                                                             │
│  IN PROGRESS                                                                │
│  ─────────────────────────────────────────────────────────────────────────  │
│  ⟳ juno     task: synthesize ICM paper response   elapsed 4m 22s          │
│                                                                             │
│  COMPLETED (last 10)                                                        │
│  ─────────────────────────────────────────────────────────────────────────  │
│  ✓ vulcan   hook: FORCE_LOCAL resolve             14:11  5s                │
│  ✓ muse     task: write trust-bond-viz brief      13:58  2m 11s            │
│  ✓ sibyl    research: ICM synthesis               12:30  18m 4s            │
│                                                                             │
│  FAILED                                                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│  ✗ mercury  task: post to X via stage-submit      13:04  [reason]          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Layout:**
- Four sub-sections: QUEUED / IN PROGRESS / COMPLETED / FAILED.
- Section headers: 10px uppercase, `--text-secondary`, letter-spacing 0.1em. Only shown if that section has items. Empty sections are omitted (not shown as empty).
- Sections separated by 1px `--border` divider.

**Job row format:**

```
{icon}  {entity}   {type}: {description}   {timing}
```

| Field | Detail |
|-------|--------|
| Icon | `⊞` queued (outline square), `⟳` in-progress (spin animation), `✓` done (`--success`), `✗` failed (`--error`) |
| Entity | Monospace, 13px, `--text-primary`. Fixed 80px column. |
| Type | `build` / `task` / `hook` / `research` — lowercase, `--text-secondary`, followed by `:` |
| Description | Task description. 60-char truncate. `--text-primary`. |
| Timing | Right-aligned. Queued: "submitted Xs ago". In-progress: live elapsed counter. Completed: wall time + elapsed duration. Failed: wall time + `[reason]` link. |

**In-progress elapsed counter:** Updates every second. Monospace. Format: `Xm Xs`.

**`[reason]` link (failed):** Click reveals inline expanded row with error output (max 6 lines, monospace, `--error` color, `--bg-tertiary` background). No modal.

**`[Refresh]` button:** Top-right of section header. Manually re-polls queue state. 200ms debounce. Spins icon for 300ms on click.

---

## Section 5: System Health

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  System Health                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  MongoDB                                                                    │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Collections    12                                                          │
│  Documents      48,291                                                      │
│  Data size      24.1 MB                                                     │
│  Index size     4.2 MB                                                      │
│  Connections    3 active                                                    │
│                                                                             │
│  DDP                                                                        │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Subscribers    12                                                          │
│  Pub/sub rate   4 msg/s                     ▁▃▅▂▇▄▂▃▅▆▂▄  (60s sparkline) │
│  Latency        8ms avg                                                     │
│                                                                             │
│  Process                                                                    │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Memory (RSS)   148 MB                      ▂▂▂▃▃▃▄▃▃▂▂▂  (60s sparkline) │
│  CPU            2.1%                        ▁▁▂▁▁▂▁▁▁▁▂▁  (60s sparkline) │
│  Node version   v20.11.0                                                    │
│                                                                             │
│  Data is sourced from /health endpoint. Refreshes every 10s.               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Three sub-sections: MongoDB / DDP / Process.**

**MongoDB fields:** from `db.stats()` — collections, documents, dataSize, indexSize, connections (current). All values right-aligned, monospace.

**DDP fields:** subscriber count (from Meteor's DDP internals), message rate (rolling 10s window), average round-trip latency (measured via ping/pong). Sparkline on rate (60s window, 12-point).

**Process fields:** RSS memory from `process.memoryUsage().rss` (converted to MB), CPU from `process.cpuUsage()` (rolling %, updated every 2s), Node version from `process.version`. Sparklines on memory and CPU.

**Sparklines:** 12-point inline bar sparkline. 60px wide, 12px tall. Bars in `--accent` at 60% opacity. No axes, no labels — they are gestural, not precise. Monospace context numbers beside them are precise.

**Source note:** Small footer line in `--text-secondary`, 11px: "Data is sourced from /health endpoint. Refreshes every 10s."

**Health endpoint:** The daemon exposes `GET /health` returning JSON with these metrics. The dashboard consumes it. If `/health` returns an error, the System Health section shows a single red row: `✗ /health unreachable — metrics unavailable`.

---

## Design Tokens

Inherits directly from the Stream PWA design system. No overrides.

```css
--bg-primary:     #0c0c0e
--bg-secondary:   #141418
--bg-tertiary:    #1c1c22
--border:         #2a2a32
--text-primary:   #e8e8ec
--text-secondary: #8888a0
--accent:         #6b4feb
--success:        #4ade80
--warning:        #fbbf24
--error:          #f87171
```

Typography:
- UI labels, values: Inter, 13px base.
- Section headers: Inter, 11px uppercase, letter-spacing 0.1em.
- Technical values (PIDs, hashes, URLs, timestamps, paths): JetBrains Mono, 12–13px.
- Sparklines: SVG, no font.

---

## Responsive Behavior

This is a localhost tool. Desktop-first. No mobile optimization required.

- **Min-width:** 1024px. Below that, the activity feed rail collapses to hidden (accessible via `[Activity]` toggle button that appears in the top bar).
- **No dark/light toggle.** Dark only.
- **No density option.** Compact by default — this is a tooling interface.

---

## Routing and Access

- Route: `localhost:{PORT}/dashboard`
- Served by the existing Meteor HTTP server inside the daemon.
- No authentication. Localhost-only — if someone has access to localhost, they're the operator.
- Link from the existing daemon UI (if any) and from the Settings panel in the Stream PWA.

---

## Implementation Notes for Vulcan

- Mount as a Meteor route at `/dashboard` using `FlowRouter` or `iron:router`, whichever the daemon already uses.
- All live data via DDP subscriptions: `daemon.overview`, `entity.roster`, `entity.activity.feed`, `passenger.queue`.
- System Health via `Meteor.setInterval` polling `GET /health` every 10s. Expose `/health` as a server-side route returning `db.stats()`, memory, CPU, DDP subscriber count.
- Passenger queue maps to `passenger.json` worker state — expose current queue from `passenger.json` if it already tracks this, or introduce a lightweight `PassengerJobs` MongoDB collection: `{ entity, type, description, status, submitted_at, started_at, completed_at, elapsed_ms, error }`.
- Activity feed: introduce `DaemonActivity` collection if not yet present. Daemon server code emits a document on each significant action (commit, hook trigger, issue interaction, queue state change).
- Sparklines: pure SVG, no library. 12 points, update on interval. Keep it simple — 60 lines of SVG is fine.
- Status dot for entities: derive from last heartbeat timestamp + lockfile presence. `active` = heartbeat within 5 minutes. `idle` = heartbeat 5–30 minutes. `offline` = >30 minutes or no record. `locked` = lockfile exists regardless of heartbeat.
- Commit hash in entity roster: read from `.git/HEAD` or last `git log --format="%h" -1` for each entity directory. Cache with 60s TTL. Do not block the UI on this — load async, fill in when ready.
- The `[?]` button in the top bar links to `/docs` or a static `README.md` served by the daemon. Falls back to the GitHub repo URL if no local docs route exists.

---

## What This Is Not

- Not a replacement for the Stream PWA. The Stream PWA is multi-user, GitHub-integrated, entity-team facing. This is single-operator, local-only, daemon-facing.
- Not a process manager UI. It does not start/stop processes. Read-only views only — no kill buttons, no restart controls.
- Not a log viewer. There is no raw log tab. Structured events only.
- Not a public endpoint. No auth layer because it should never be exposed externally. If the daemon is exposed to the internet, that is a separate infrastructure concern outside this brief's scope.
