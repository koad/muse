# Design Brief: Dark Passenger Browser Extension
**Date:** 2026-04-05
**Author:** Muse
**Spec origin:** VESTA-SPEC-036
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation

---

## What This Is

The Dark Passenger is a browser extension that overlays sovereign contextual data on the pages the user visits. Product safety records, ToS summaries, repair manuals, ownership provenance, signed data from community-curated datasets — all sourced from the user's local daemon, never from a remote server the extension controls.

It is the browser layer of the koad:io daemon architecture. The daemon is already DDP-connected and has `passenger.ingest.url` in its method catalog. The extension is the front end of that plumbing.

**Design intent:** This is a developer tool used by people who understand what a daemon is. It should feel like a browser devtools panel that happens to have a beautiful dark coat. Not a consumer privacy theater product. Not a tracker blocker with a shield logo. A window into sovereign data infrastructure.

---

## 1. Toolbar Icon

The icon is the primary ambient signal. The user glances at it without clicking. It must communicate the connection state and data-presence state at a glance.

### Icon Shape

A small filled hexagon — one interior dot (◉). The hexagon signals structure and deliberate geometry. The interior dot signals "entity present." This is the same node-dot visual language used in the trust bond chain diagram and the daemon passenger system. The icon reads as "something is here and it is watching with you."

At 16px (browser toolbar), the hexagon renders as a clean outlined shape with the interior dot. At 19px (retina/high-DPI toolbars), the dot interior is visible. Provide @1x and @2x SVG exports.

### States

| State | Color | Badge | Description |
|-------|-------|-------|-------------|
| **Active** | `#7c6aff` (accent) — full opacity | None | Daemon connected, datasets loaded, data available on current page |
| **Active — no data** | `#7c6aff` — 50% opacity | None | Daemon connected, no dataset match for current page |
| **Loading** | `#7c6aff` pulsing | None | Daemon connected, querying datasets |
| **Blocked** | `#f87171` (error) | `!` small red badge | A dataset flagged this page (e.g., ToS risk, known hazard) |
| **Inactive / disconnected** | `#64647c` (muted) | None | Daemon not reachable |

**Loading pulse:** The hexagon animates between 60% and 100% opacity, 1.4s cycle, `ease-in-out`. Suppressed under `prefers-reduced-motion`. This is the only animation the icon ever performs.

**The blocked badge (`!`):** Red filled circle, 6px diameter, positioned top-right of the hexagon. The badge is the only time color communicates something by itself — but the popup copy always restates it in text, satisfying WCAG non-text contrast requirements.

### On Click

Clicking the toolbar icon always opens the popup. No toggle. No direct state change on click. The popup is the control surface.

---

## 2. The Popup

The popup is the control surface. It opens when the user clicks the icon. It is 360px wide (max), dark by default. No min-height — it sizes to its content.

### Anatomy

```
┌──────────────────────────────────────────────┐
│  ◉ Dark Passenger              [⚙ Settings]  │   ← Header
│  daemon · thinker:3001                       │
├──────────────────────────────────────────────┤
│  CONNECTION                                  │   ← Status section
│  ● Connected  · juno (active passenger)      │
│  amazon.com/dp/B09XJ5...                     │   ← current URL, truncated, mono
├──────────────────────────────────────────────┤
│  ACTIVE ON THIS PAGE                         │   ← Datasets section
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │ ✓  iFixit Repair Data          on ●  │    │
│  │    2 annotations                     │    │
│  └──────────────────────────────────────┘    │
│  ┌──────────────────────────────────────┐    │
│  │ ✓  ToS;DR Summaries            on ●  │    │
│  │    1 annotation                      │    │
│  └──────────────────────────────────────┘    │
│  ┌──────────────────────────────────────┐    │
│  │ ○  Product Safety DB           off ○ │    │
│  │    no match                          │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  [Manage datasets →]                         │   ← Link to dataset panel
├──────────────────────────────────────────────┤
│  OVERLAY                                     │   ← Overlay control
│  Show on page   [toggle: ON]                 │
│  Show sidebar   [toggle: OFF]                │
└──────────────────────────────────────────────┘
```

### Sections

**Header**
- Left: hexagon icon (12px) + "Dark Passenger" Inter 600 14px `--color-text-primary`
- Right: settings gear icon (14px), `--color-text-secondary`, opens Settings tab
- Below title: daemon address in JetBrains Mono 11px `--color-text-muted` — e.g., `daemon · thinker:3001`. This is infrastructure, not marketing. It should always be visible.

**Connection section**
- Label: `CONNECTION` — Inter 600 10px uppercase, `--color-text-secondary`, letter-spacing 0.08em. Section label pattern consistent across the popup.
- Status row: 8px circle indicator (green = connected, grey = disconnected, amber = reconnecting) + "Connected" text 13px Inter. Then `·` separator + active passenger name. All on one line.
- Current URL: JetBrains Mono 11px, `--color-text-muted`, truncated at ~42 chars with ellipsis in middle (show domain and end of path). Not a link. Just state context.

**Active on this page**
- Shows datasets that have been evaluated for the current URL.
- Each dataset appears as a compact row: status icon (`✓` success or `○` no-match) + dataset name + an inline toggle (on/off pill) on the right.
- Below the name: annotation count in `--color-text-muted` 12px — e.g., "2 annotations" or "no match". This is what tells the user whether the overlay has anything to show.
- Dataset rows have a border `--color-border-subtle`, padding `--space-3`, border-radius 6px.
- Max 5 dataset rows shown. If more: "and 3 more →" link to dataset panel.

**"Manage datasets →"**
- Text link, `--color-accent`, 12px. Opens the full dataset panel (new tab within the extension popup, or separate extension page). Same session — no new browser tab.

**Overlay toggles**
- Two toggles: "Show on page" and "Show sidebar". Independent. Standard toggle switch component: 32×18px, `--color-accent` when on, `--color-bg-active` when off. No label wrapping — one line each.
- "Show on page" controls inline badges (annotations on page elements).
- "Show sidebar" controls the persistent sidebar panel on the right edge.

### Popup Behavior

- Opens at 360px wide. Max-height 480px with internal scroll on the datasets section if overflow.
- Closes when user clicks outside the popup or presses Escape.
- Retains last scroll position within the datasets list.
- Does not close when user changes a toggle — the change is immediate and the popup stays open.
- No loading skeleton. If data is not yet available, the dataset rows show "checking..." in `--color-text-muted`.

---

## 3. The Overlay

The overlay is what appears on the page itself. This is the most opinionated design decision in the extension.

**Primary use case:** A product page on a major retail site (Amazon, Best Buy, etc.). The URL matches a dataset. The dataset has annotations. The overlay must not break the page layout, must be dismissible, and must look like it belongs to the browsing infrastructure — not to the page itself.

### Primary Mode: Inline Badges

Inline badges are the default overlay mode ("Show on page" ON, "Show sidebar" OFF).

Badges are small floating markers that anchor to specific elements on the page. They appear as 20px × 20px circles positioned at the top-right corner of an annotated element. They use the koad:io accent color (`#7c6aff`) at 90% opacity, with a white icon or number inside.

**Badge variants:**

| Badge | Icon | Trigger |
|-------|------|---------|
| Repair data available | Wrench (SVG, 12px) | iFixit dataset has data for this product |
| ToS annotation | `≡` (3 lines, 10px) | ToS;DR annotation on this element or page |
| Safety flag | `!` (10px) | Product safety record present |
| Data count | Number (11px, mono) | Multiple datasets have data — badge shows count |

When a user hovers or focuses a badge, a tooltip card appears adjacent to it. The card content depends on the dataset type (see Tooltip Card spec below).

**Positioning:** Badges attach to the outermost bounding box of the annotated element. If the element scrolls off-screen, the badge scrolls with it (it is fixed relative to the element, not the viewport). If the annotated element is not in the visible DOM (e.g., inside a collapsed accordion), the badge appears at the top of the nearest visible ancestor.

**Badge rendering strategy:** The extension injects a minimal DOM node (`<dp-badge>` custom element) into the page. Shadow DOM scopes all styles — no risk of page CSS leaking in or badge CSS leaking out. The custom element registers a `MutationObserver` to re-anchor if the target element moves (e.g., lazy-loaded DOM rewrites).

**z-index:** Badges use `z-index: 2147483647` (max safe integer) to sit above the page. They do not use `position: fixed` — they scroll with the page content.

### Secondary Mode: Sidebar Panel

When "Show sidebar" is ON, a 280px panel anchors to the right edge of the viewport.

```
┌────────────────────────────────────┐
│  ◉ Dark Passenger         [×]      │   ← Header with close
│  amazon.com/dp/...                 │
├────────────────────────────────────┤
│  iFixit Repair Data                │   ← Dataset section
│  ─────────────────────────────     │
│  > Repairability score: 6/10       │
│    "Adhesive back panel            │
│     difficult to remove..."        │
│    [View full guide →]             │
├────────────────────────────────────┤
│  ToS;DR                            │   ← Dataset section
│  ─────────────────────────────     │
│  ⚠  "Tracks purchase history       │
│      for targeted advertising"     │
│     Class C (bad)                  │
├────────────────────────────────────┤
│  Product Safety                    │
│  ─────────────────────────────     │
│  No records found.                 │
└────────────────────────────────────┘
```

The sidebar is injected as a fixed-position panel using the same shadow DOM pattern as the badges. It does not resize or shift the page — it overlaps. The user can drag its top edge to resize height. A thin drag handle (4px, `--color-border-default`) spans the full top edge.

**Sidebar header:** Hexagon icon + "Dark Passenger" + current domain. Close button (`×`) collapses the sidebar (sets "Show sidebar" OFF in popup state).

**Dataset sections:** Each contributing dataset gets a labelled section with a 1px top border `--color-border-subtle`. Sections are collapsible — clicking the section title toggles the content. Collapsed state shows section title and annotation count only.

**Link styling within sidebar:** All external links (view full guide, source, etc.) in JetBrains Mono 11px `--color-info`, underline on hover. They open in new browser tabs — never navigate the current page.

### Tooltip Card (Badge Hover)

Tooltip appears on badge hover (160ms delay) or keyboard focus (instant). Positioned adjacent to the badge, preference: right, fallback: left if near right edge, fallback: below.

```
┌──────────────────────────────────────┐
│  iFixit Repair Data                  │   ← Dataset name Inter 600 13px
│  ───────────────────────────────     │
│  Repairability: 6/10                 │   ← Key data point, Inter 14px
│                                      │
│  "Adhesive back panel, battery       │   ← Summary in --color-text-secondary
│   requires heat gun to remove"       │
│                                      │
│  Signed: iFixit · 2026-03-14        │   ← Provenance, mono 11px muted
│                                      │
│  [Open in sidebar →]                 │   ← Toggle sidebar and scroll to section
└──────────────────────────────────────┘
```

**Tooltip spec:**
- Width: 240px
- Background: `--color-bg-tertiary` (#1c1c22)
- Border: 1px `--color-border-strong`
- Box shadow: `0 4px 16px rgba(0,0,0,0.5)`
- Border-radius: 8px
- Padding: `--space-4`
- Fade in: 150ms `ease-out`. Fade out: 100ms. No slide.
- Dismiss: Mouse leaves badge + tooltip, or Escape key.
- `prefers-reduced-motion`: instant show/hide, no transition.

**Provenance line** (`Signed: source · date`) always present. This is load-bearing — it tells the user whose claim they are reading. If the dataset is unsigned, the line reads `Unsigned data — verify manually` in `--color-warning`.

---

## 4. The Dataset Panel

The dataset panel is where users manage installed datasets. It is a full extension page (not a popup), opened from "Manage datasets →" in the popup.

### Layout

```
┌──────────────────────────────────────────────────────┐
│  ◉ Dark Passenger — Datasets                         │   ← Page title
│  [Installed ▾]   [Available]   [Add by URL]          │   ← Tabs
├──────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │  iFixit Repair Data                  [on  ●] │   │
│  │  Repair annotations for consumer products     │   │
│  │                                              │   │
│  │  Provenance                                  │   │
│  │  ───────────────────────────────────────     │   │
│  │  Source:    ifixit.com                       │   │
│  │  Entity:    ifixit · github.com/ifixit/...   │   │
│  │  Signed by: iFixit (GPG: A07F 8CFE CBF6...)  │   │
│  │  Updated:   2026-03-14                       │   │
│  │  Records:   47,823 products                  │   │
│  │                                              │   │
│  │  [View source →]  [Remove]                   │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │  ToS;DR Summaries                    [on  ●] │   │
│  │  Machine-readable ToS annotations            │   │
│  │  ...                                         │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Tabs

**Installed:** All datasets currently installed and registered with the local daemon. Shows full provenance for each.

**Available:** Curated index of datasets known to the daemon (fetched from daemon's dataset registry). Browse and install from here.

**Add by URL:** Manual install from a git repo URL or direct URL to a signed dataset manifest. Power-user path.

### Dataset Card (Installed)

Each installed dataset is a card at full panel width.

**Card header:**
- Left: Dataset name Inter 600 14px + short description 12px `--color-text-secondary`
- Right: Toggle switch (on/off). Turning off disables the dataset globally — no annotations from this dataset appear anywhere, regardless of popup per-page toggles.

**Provenance section:**
The provenance block is the most important part of the card. It answers: where did this data come from, who signed it, and can I verify it?

| Field | Value style | Notes |
|-------|-------------|-------|
| Source | `--color-info` 12px | The origin URL or org |
| Entity | JetBrains Mono 11px `--color-text-secondary` | The koad:io entity repo that distributed the dataset, if applicable |
| Signed by | JetBrains Mono 11px `--color-text-primary` | `Name (GPG: fingerprint-last-12)`. If unsigned: `⚠ No signature` in warning color |
| Updated | 12px date | Last dataset update |
| Records | 12px count | Total records in dataset, if available |

The provenance section is always visible — not collapsible. This is not optional data. The user must be able to see at a glance who is responsible for what they are reading on pages.

**Actions:**
- "View source →" — opens the dataset's source repo or manifest URL in a new tab. JetBrains Mono 11px `--color-info`.
- "Remove" — text button `--color-error`, small, right-aligned. Removes the dataset from the daemon (not just disables it). Confirmation step: "Remove iFixit Repair Data? This cannot be undone from this panel." Two buttons: "Cancel" (secondary) + "Remove" (danger).

### Available Tab

Grid of available dataset cards (2 columns on desktop, 1 on mobile panel). Each card: name, description, record count, provenance summary (source + signing entity). "Install" button primary.

On install, the daemon fetches and registers the dataset. Progress feedback: button text changes to "Installing..." then "Installed ✓".

### Add by URL

A single input field with a submit button.

```
Add dataset from URL or git repository:
┌─────────────────────────────────────────────┐ [Add]
│ https://github.com/org/dataset-repo         │
└─────────────────────────────────────────────┘

Datasets must be signed. Unsigned datasets will be flagged
on every annotation they produce.
```

Input: full-width, JetBrains Mono 12px for the URL value (it is a technical identifier). Add button: primary variant. Validation: must be a valid URL. After submit: shows a progress card with fetch and verification status. If signature verification fails: error state with "Dataset loaded, but unverified — annotations will be flagged."

---

## 5. Daemon Disconnected State

The disconnected state is what the user sees when the local daemon is not reachable. This is the most common first-run experience and the most common failure mode.

**Design principle:** Do not alarm. A disconnected daemon is not an error — it is an expected state for a tool that runs locally. The UI acknowledges it calmly and gives a concrete recovery path.

### Toolbar Icon (Disconnected)

Hexagon icon in `#64647c` (muted grey). No badge. No animation. The grey communicates "inactive" — the same way a disabled button looks. Not broken, just sleeping.

### Popup (Disconnected State)

```
┌──────────────────────────────────────────────┐
│  ◉ Dark Passenger              [⚙ Settings]  │
│  daemon · thinker:3001                       │
├──────────────────────────────────────────────┤
│  CONNECTION                                  │
│  ○ Not connected                             │
│                                              │
│  The local daemon is not reachable.          │
│  Dark Passenger needs the koad:io daemon     │
│  running on this machine to work.            │
│                                              │
│  Start it with:                              │
│  ┌──────────────────────────────────────┐   │
│  │ cd ~/.koad-io/daemon/src             │   │
│  │ meteor run --port 3001               │   │
│  └──────────────────────────────────────┘   │
│  [Copy command]                              │
│                                              │
│  Or check the koad:io docs for setup.        │
│  [koad:io daemon setup →]                    │
├──────────────────────────────────────────────┤
│  Retrying in 12s...        [Retry now]       │
└──────────────────────────────────────────────┘
```

**Copy the nuances of this state:**

"Not connected" — the status line. Grey circle, not red. Not "Error" or "Failed." The daemon not running is not an error in this system; it is a configuration state.

The command block is a `<pre>` styled like a terminal snippet: background `--color-bg-tertiary`, border-left 3px `--color-accent`, JetBrains Mono 11px, padding `--space-3`. The "Copy command" button copies the full startup command to clipboard — same copy-to-clipboard pattern used elsewhere in the design system (`toast("Copied!")`, fades after 1.5s).

The retry row: passive countdown text in `--color-text-muted` + a "Retry now" text button in `--color-accent`. The extension retries the DDP connection automatically every 15s. The countdown resets on manual retry.

**No overlay renders while disconnected.** Any existing inline badges are removed from the DOM as soon as disconnection is detected. The sidebar (if open) shows the disconnected state header and collapses its dataset sections.

### Settings: Daemon Address

In the Settings panel (reached from the gear icon), users can configure the daemon address:

```
Daemon address
┌───────────────────────────────────────┐
│ ws://localhost:3001/websocket          │
└───────────────────────────────────────┘

Default: ws://localhost:3001/websocket
This is the DDP endpoint of the koad:io daemon.
```

JetBrains Mono for the input value. The WebSocket URL is a technical identifier and deserves monospace. Default is shown below as a fallback reference. A "Reset to default" text link restores it.

---

## Extension Skin

The extension does not use a domain skin override. It runs entirely in the koad:io canonical palette:
- Background: `#0c0c0e`
- Cards/panels: `#141418`
- Accent: `#7c6aff`
- Success: `#4ade80`
- Warning: `#fbbf24`
- Error: `#f87171`
- All typography: Inter for UI, JetBrains Mono for technical data

The popup is narrow (360px) — the font scale shifts slightly. Body text throughout the popup is 13px (not the standard 14px) to preserve density without cramping. The 14px base applies to the dataset panel (full page, more room).

---

## Component Summary for Vulcan

| Component | Location | Notes |
|-----------|----------|-------|
| `Popup.svelte` (or `.jsx`) | Extension popup | 360px, sections: header, connection, datasets, overlay toggles |
| `DatasetRow.svelte` | Inside Popup | Name, toggle, annotation count |
| `OverlayBadge` (web component) | Injected into pages | Shadow DOM, custom element, z-index max |
| `OverlayTooltip` (web component) | Adjacent to badge | Shadow DOM, fade in/out, provenance line required |
| `Sidebar` (web component) | Right edge, fixed | Shadow DOM, collapsible dataset sections |
| `DatasetPanel.svelte` | Full extension page | Tabs: Installed / Available / Add by URL |
| `DatasetCard.svelte` | Inside DatasetPanel | Full provenance block, toggle, remove action |
| `DisconnectedState.svelte` | Used in Popup + Sidebar | Command block, retry countdown, copy button |
| `DaemonConnection.ts` | Background service worker | DDP client, retry logic, broadcasts state |

**DDP dependency:** The background service worker maintains the DDP connection. It broadcasts state changes (connected/disconnected, dataset results) to the popup and content script via `chrome.runtime.sendMessage`. The content script (injecting badges and sidebar) never opens its own DDP connection — all data flows through the service worker.

**Manifest V3 note:** The background service worker has a limited lifetime in MV3. The DDP connection must be re-established on each wakeup. The extension should use `chrome.alarms` to keep the service worker alive during active browsing sessions. This is an implementation concern but Vulcan needs to account for it — the UX of "reconnecting..." should be invisible to users in normal browsing but graceful on the first load.

---

## What This Is Not

- Not a tracker blocker. Does not intercept or block network requests.
- Not a privacy extension. Does not inspect page content for personal data.
- Not a content script that scrapes. It reads URLs and matches against datasets.
- Not dependent on any remote server. All data comes from the local daemon.
- Not persistent without the daemon. If the daemon stops, the overlay stops.

The extension is a window. The daemon is the intelligence. The browser is just the viewport.

---

## Relationship to Other Briefs

| Brief | Relationship |
|-------|-------------|
| `koad-io-design-system.md` | Full design system applies. No new tokens introduced. 13px body scale exception in popup noted above. |
| `2026-04-05-trust-bond-visualization.md` | Provenance display in dataset cards uses the same visual language as the trust bond node display — mono fingerprints, verification state icons. |
| Daemon architecture (memory 005) | The DDP method catalog (`passenger.ingest.url`, `passenger.check.url`) defines what the extension can ask the daemon. The UI must not promise capabilities the daemon does not have. |

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
