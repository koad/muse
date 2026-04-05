# Design Brief: Public Entity Profile Page
**Date:** 2026-04-05
**Author:** Muse
**Route:** `kingofalldata.com/entities/{entity}` (e.g. `/entities/juno`)
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation

---

## Strategic Context

Every koad:io entity has a public GitHub repo. That's a fact. But a GitHub repo is not a product page — it's a code drawer. When a curious developer finds `github.com/koad/juno`, they see a file listing. They don't understand what Juno *is*, why it matters, or how to get one.

The entity profile page is the bridge between discovery and desire.

**Audience:** A developer who just encountered koad:io for the first time — from a blog post, a tweet, a conference talk. They've arrived here because an entity name caught their attention. They want to know what this thing is before they decide whether to care.

**Design goal:** In under 30 seconds, the visitor should understand:
1. What this entity is (character + role, one sentence)
2. That this entity is alive and doing real work (activity)
3. That they could own one exactly like it

The "How do I get one?" section is the conversion moment. Everything before it is credibility-building. Everything after it is support.

---

## Data Sources

All data for the MVP profile page comes from the entity's public GitHub repo. No custom backend required.

| Section | Data source |
|---------|-------------|
| Name, description, avatar | GitHub repo metadata |
| Recent commits | GitHub API: `GET /repos/koad/{entity}/commits?per_page=5` |
| Open / recently closed issues | GitHub API: `GET /repos/koad/{entity}/issues` |
| Files (briefs, specs, curricula) | GitHub API: `GET /repos/koad/{entity}/contents/` + recursive tree |
| "Get one" — clone URL | Static: `https://github.com/koad/{entity}` |
| "Reach it" — issues link | Static: `https://github.com/koad/{entity}/issues/new` |

All GitHub API calls are unauthenticated for public repos. Rate limit: 60 req/hr per IP — acceptable for page loads with reasonable caching (e.g. 5-minute CDN cache on the commit/issue endpoints).

---

## Page Structure

Five sections. In this order.

```
┌─────────────────────────────────────┐
│  1. IDENTITY HEADER                 │  ← Who is this entity?
│  2. ACTIVITY FEED                   │  ← What has it done?
│  3. OWNED ARTIFACTS                 │  ← What does it own?
│  4. GET ONE (conversion section)    │  ← How do I get one?
│  5. REACH IT                        │  ← How do I reach it?
└─────────────────────────────────────┘
```

---

## Section 1: Identity Header

The first thing the visitor sees. No navigation chrome above the fold. Juno before the site.

```
┌─────────────────────────────────────────┐
│                                         │
│   ← Back to all entities               │  ← quiet breadcrumb, 13px
│                                         │
│   [Avatar 72px]  ● online              │  ← avatar + online dot
│                                         │
│   Juno                                  │  ← Inter 700, 32px
│   juno.koad.io                          │  ← JetBrains Mono, 14px, --accent
│                                         │
│   Queen of the operation.               │  ← tagline, Inter 400, 18px
│   Business runs because Juno runs.      │     (from entity descriptions brief)
│                                         │
│   ─────────────────────────────────── │  ← subtle divider
│                                         │
│   Business orchestrator · AI entity     │  ← role badges (pill tags)
│   On GitHub →                          │  ← external link to repo
│                                         │
└─────────────────────────────────────────┘
```

**Design notes:**
- Avatar is the entity's GitHub avatar (or initials fallback in `--bg-tertiary` circle).
- Online dot: `--color-success` (#4ade80), 10px, positioned top-right of avatar. "Online" means last commit was within 48 hours; absence of dot means no recent activity — never a grey "offline" dot, just silence.
- Tagline is the entity's one-liner from the GitHub description field. These are already written (see `2026-04-05-entity-descriptions.md`). Render verbatim — no truncation at this size.
- Role badges are space-separated keywords from the repo's GitHub Topics, rendered as small pills. Not editable here.
- "On GitHub →" opens `github.com/koad/{entity}` in a new tab. Use `rel="noopener noreferrer"`.
- No hero image, no banner, no gradient wash. Clean. The entity's work is the visual.

**Mobile (< 640px):**
- Avatar and online dot: 64px, left-aligned
- Name and tagline stack naturally in single column
- Role badges wrap to new lines freely

---

## Section 2: Activity Feed

Evidence that the entity is alive and working. A developer's first trust signal is recency.

```
┌─────────────────────────────────────────┐
│                                         │
│  Recent Activity                        │  ← Inter 600, 16px, --text-secondary
│                                         │
│  ──────────────────────────────────── │
│                                         │
│  ◆ committed  ·  2h ago                │  ← activity row
│    hooks: embed GPG-signed policy block │  ← commit message, truncated at 72 chars
│                                         │
│  ◆ committed  ·  6h ago                │
│    log: 2026-04-05 — Day 6 second      │
│    session                              │
│                                         │
│  ◇ issue closed  ·  9h ago             │
│    Vulcan#48 resolved — governance     │
│    note committed                       │
│                                         │
│  ◆ committed  ·  1d ago                │
│    log: 2026-04-05 — hook architecture │
│    session                              │
│                                         │
│  ◆ committed  ·  2d ago                │
│    hooks: add FORCE_LOCAL flag          │
│                                         │
│  [See full history →]                  │  ← links to GitHub commits page
│                                         │
└─────────────────────────────────────────┘
```

**Design notes:**
- Show 5 items maximum. Mix commits (◆) and recently-closed issues (◇). Commits from GitHub `/commits` endpoint; issues from `/issues?state=closed&sort=updated&per_page=3`.
- ◆ (filled diamond) = commit. ◇ (open diamond) = issue closed. Both use `--color-accent` (#7c6aff). No other icons.
- Timestamp: relative, using `Intl.RelativeTimeFormat`. Keep it honest — "2h ago" not "just now" if it wasn't.
- Commit message: truncate at 72 chars with ellipsis. The full message is accessible via link.
- Each row links to the specific commit or issue on GitHub. Subtle — underline on hover, no decoration at rest.
- "See full history →" links to `github.com/koad/{entity}/commits/main`.
- Section header "Recent Activity" is in `--text-secondary`, not primary — it's context, not headline.
- If the last commit is > 7 days ago: replace the header with "Last active N days ago" in `--color-warning` tone — honest signal, not alarming.

**Mobile:** Same structure, single column. Row layout does not change.

---

## Section 3: Owned Artifacts

What has this entity produced? The visitor can see the contents of the entity's repo — filtered to the meaningful artifacts.

```
┌─────────────────────────────────────────┐
│                                         │
│  Artifacts                              │  ← Inter 600, 16px, --text-secondary
│                                         │
│  ──────────────────────────────────── │
│                                         │
│  BRIEFS                                 │  ← category label, JetBrains Mono 11px
│                                         │
│  alice-ui-design-brief.md              │  ← filename, monospace 13px
│  2026-04-04-entity-card-component.md   │
│  2026-04-04-stream-pwa-design.md       │
│  2026-04-05-alice-graduation-cert.md   │
│  2026-04-05-entity-profile-page.md     │
│  + 4 more →                            │  ← overflow link
│                                         │
│  ──────────────────────────────────── │
│                                         │
│  MEMORIES                               │
│                                         │
│  001-identity.md                        │
│  002-operational-preferences.md         │
│                                         │
│  ──────────────────────────────────── │
│                                         │
│  SKILLS & COMMANDS                      │
│                                         │
│  commit/self/command.sh                 │
│  spawn/process/command.sh               │
│                                         │
│  [View all files on GitHub →]           │  ← links to repo root
│                                         │
└─────────────────────────────────────────┘
```

**Design notes:**
- Data source: GitHub Contents API, filtered to well-known directory paths:
  - `briefs/` → shows `.md` files sorted by name descending (newest first by date prefix)
  - `memories/` → shows `.md` files sorted by name ascending
  - `commands/` → shows `command.sh` files with directory path as label
  - `curricula/` → shows subdirectory names (for educational entities like Chiron, Alice)
  - `specs/` → shows `.md` files if present
- Only render categories that have content. Don't show empty headers.
- File names are links to the raw file on GitHub (`github.com/koad/{entity}/blob/main/{path}`). They open in a new tab.
- Overflow: show up to 5 files per category. If more exist, show "+ N more →" linking to the category directory on GitHub.
- This is not a file browser. It is a proof-of-work display. The point is not to let visitors navigate the repo — it's to demonstrate that real artifacts exist and accumulate.
- Category labels in JetBrains Mono at 11px uppercase, `--text-muted`. Visual hierarchy should make the file names the focal point, not the labels.
- No file previews, no inline rendering. Just names and links. Simplicity is the point.

**Mobile:** Same structure. File names may wrap — allow it. No horizontal scrolling.

---

## Section 4: Get One (Conversion Section)

This is the moment. A curious developer now understands that Juno is alive, has done real work, and owns real artifacts. The question that forms: "Can I have one?"

The answer must land with the minimum possible friction.

```
┌─────────────────────────────────────────┐
│                                         │
│  ╔═════════════════════════════════╗    │
│  ║                                 ║    │
│  ║  This entity is cloneable.      ║    │  ← heading, Inter 700, 20px
│  ║                                 ║    │     accent border (left rule, --accent)
│  ║  Juno runs from a git repo on   ║    │  ← body, Inter 400, 16px, 1.6 line-height
│  ║  koad's hardware. The repo is   ║    │
│  ║  the entity. Clone it and the   ║    │
│  ║  entity is yours.               ║    │
│  ║                                 ║    │
│  ║  No vendor. No kill switch.     ║    │  ← secondary line, --text-secondary
│  ║  Your keys. Your agent.         ║    │
│  ║                                 ║    │
│  ║  ┌───────────────────────────┐  ║    │
│  ║  │ $ git clone               │  ║    │  ← code block, JetBrains Mono 13px
│  ║  │   github.com/koad/juno    │  ║    │     bg: --bg-tertiary
│  ║  │   ~/.juno                 │  ║    │     copy button: top-right of block
│  ║  └───────────────────────────┘  ║    │
│  ║                                 ║    │
│  ║  ┌──────────────────────────┐   ║    │
│  ║  │  Get started with koad:io│   ║    │  ← primary CTA, --accent filled button
│  ║  └──────────────────────────┘   ║    │
│  ║                                 ║    │
│  ║  or learn more about entities   ║    │  ← secondary link, --text-secondary
│  ║                                 ║    │
│  ╚═════════════════════════════════╝    │
│                                         │
└─────────────────────────────────────────┘
```

**Design notes:**
- This section has a distinct container: `--bg-secondary` background, `--accent` left border rule (3px), standard card radius and padding. It reads as a featured block — set apart from the informational sections above.
- "This entity is cloneable." is the headline. Not "Deploy your own Juno." Not "Get started." The word *cloneable* is the conceptual pivot — it maps to `git clone`, which developers understand instantly.
- The clone command block is pre-populated with the correct repo path. The trailing `~/.juno` is the install convention. The copy button (clipboard icon, top-right of code block) is 24px, `--text-secondary`, becomes `--accent` on hover. No tooltip needed — its function is obvious.
- "Get started with koad:io" CTA links to `kingofalldata.com/get-started` (or the equivalent docs/install page). It is the primary button — `--accent` background, `--text-inverse` text, 44px height, full width on mobile.
- "or learn more about entities" is a secondary escape route — links to `/entities` (the directory of all entities). Not every visitor is ready to clone; some want to browse more. Honor that without making it the default.
- The tone of the body copy is direct and matter-of-fact: "No vendor. No kill switch." is the sovereignty pitch without the jargon. It is not a sales slogan — it is a factual property of the system.
- Do not use the phrase "sovereign AI" or "Not your keys, not your agent" in this section. Those resonate with insiders, not first-timers. (Iris audit, 2026-04-04.)

**Mobile:** The container goes full-width. Code block scrolls horizontally within its own box if needed (the clone URL is long). CTA button is full-width and thumb-reachable.

**The psychological journey through Section 4:**
1. "This entity is cloneable." — realization. It's a product, not just a character.
2. "The repo is the entity." — concept lands. Mapping to what they know (git repos).
3. Clone command — mechanical proof. They can copy it right now.
4. CTA — action path. One click away from the guide.

Do not interrupt this rhythm with testimonials, pricing, or sign-up walls. The conversion here is attention → interest → action, not sales.

---

## Section 5: Reach It

The entity accepts work through GitHub Issues. This section closes the loop: the visitor now knows what the entity is, what it's done, and how to get one — and if they have a task for it, here's the door.

```
┌─────────────────────────────────────────┐
│                                         │
│  Work with Juno                         │  ← Inter 600, 16px
│                                         │
│  ──────────────────────────────────── │
│                                         │
│  GitHub Issues is how you assign        │  ← body, 15px, --text-secondary
│  work to Juno. File an issue and        │
│  Juno picks it up.                      │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │  Open an issue on koad/juno  →   │   │  ← text button, --accent, no fill
│  └──────────────────────────────────┘   │
│                                         │
│  Public issues only. Juno operates      │  ← fine print, 13px, --text-muted
│  under koad's oversight. See GOVERNANCE │
│  for authorization scope.               │
│                                         │
└─────────────────────────────────────────┘
```

**Design notes:**
- Section header: "Work with Juno" — not "Contact" (too generic), not "Reach Juno" (too abstract). The entity does work.
- The body copy is a one-sentence instruction: file an issue, entity picks it up. No elaborate explanation. The process is that simple.
- CTA is a text button (no fill), `--accent`, links directly to `github.com/koad/juno/issues/new`. Opens in a new tab.
- Fine print: one sentence about public visibility and oversight. Not a legal disclaimer — a factual note that reassures both the visitor (their request is transparent) and explains the governance model briefly. "GOVERNANCE" in the fine print links to the `GOVERNANCE.md` file in the entity's repo.
- This section is deliberately small. It is not a contact page. It is a pointer.

---

## Page-Level Design Notes

### Spacing and Layout

```
max-width: 720px
padding: 0 var(--space-5)    /* 20px sides, mobile */
padding: 0 var(--space-8)    /* 32px sides, >= 640px */

Section gap: var(--space-12) /* 48px between sections */
```

Single column throughout. No sidebar. No sticky nav within the page. The entity deserves the full width.

### Typography

Consistent with the koad:io design system (v1.1):
- Headings: Inter 700
- Body: Inter 400, `--text-primary`
- Secondary/labels: Inter 400, `--text-secondary`
- Code, filenames, domains: JetBrains Mono
- Fine print: 13px, `--text-muted`

### Color

No domain skin deviations on the entity profile page. This uses the standard koad:io palette:
- Background: `--color-bg-primary` (#0c0c0e)
- Accent: `--color-accent` (#7c6aff)
- Success/online: `--color-success` (#4ade80)

The Alice gold palette is Alice's space — do not bleed it into entity profiles, even for Alice's own profile page.

### Back Navigation

"← Back to all entities" at the top of the page links to `/entities` — the entity directory (design in `2026-04-04-entity-card-component.md`, Directory Card variant).

The breadcrumb is 13px, `--text-secondary`. No hover fill. Subtle.

### Error States

- **Entity not found (404):** "This entity doesn't exist yet. New entities are gestated with koad:io." with link to `/get-started`. Same dark page, no broken UI.
- **GitHub API unavailable:** Show the static identity header (hardcoded in the page), hide Activity and Artifacts sections, show a quiet note: "Activity feed unavailable — view on GitHub →".
- **Empty sections:** If an entity has no briefs, no memories, no commands — hide the Artifacts section entirely. Don't show empty states that make the entity look inactive.

### Caching

- Identity header data: Cache indefinitely (changes rarely). Bust on deploy.
- Activity (commits/issues): Cache 5 minutes via CDN or serverside. Not real-time — "recent" is the right framing.
- Artifacts (file tree): Cache 15 minutes. File names don't change at high frequency.

---

## Route Notes

- Canonical route: `/entities/{entity}` where `{entity}` is the entity's lowercase name.
- Route aliases to handle: `/entities/juno.koad.io` → redirect to `/entities/juno`.
- The page is fully public. No authentication required.
- Page title pattern: `{Entity} — koad:io` (e.g. "Juno — koad:io").
- Meta description: Pull from entity's GitHub repo description (the tagline from `2026-04-05-entity-descriptions.md`).

---

## Implementation Notes for Vulcan

**Data fetching pattern (MVP):**

```javascript
// Fetch at page load, server-side render preferred for SEO
const [commits, issues, contents] = await Promise.all([
  github.repos.listCommits({ owner: 'koad', repo: entity, per_page: 5 }),
  github.repos.listForRepo({ owner: 'koad', repo: entity, state: 'closed',
    sort: 'updated', per_page: 3 }),
  github.repos.getContent({ owner: 'koad', repo: entity, path: '' }),
]);
```

**Known directories to scan for artifacts:**
- `briefs/` — filter: `*.md`, sort: name descending
- `memories/` — filter: `*.md`, sort: name ascending
- `commands/` — filter: recursive, `command.sh` files, display as `{dir}/command.sh`
- `curricula/` — filter: subdirectory names only (for Alice, Chiron)
- `specs/` — filter: `*.md`, sort: name descending
- `PROJECTS/` — filter: `*.md`, sort: name ascending

**Online/offline detection:**
- Online (green dot): `commits[0].commit.author.date` within 48 hours of now
- No dot: last commit older than 48 hours — show nothing, not a grey dot

**Page component structure:**

```
<EntityProfilePage entity={entityName}>
  <EntityIdentityHeader />    ← static data + GitHub meta
  <EntityActivityFeed />      ← commits + closed issues
  <EntityArtifacts />         ← file tree, categorized
  <EntityGetOne />            ← static clone command + CTA
  <EntityReachIt />           ← static GitHub issues link
</EntityProfilePage>
```

**SEO note:** Server-side render the identity header at minimum. Activity and Artifacts can hydrate client-side. The page must render meaningfully without JavaScript for search crawlers.

---

## Relationship to Other Work

| Brief | Relationship |
|-------|-------------|
| `entity-card-component.md` | Directory Card variant links to this page. This page is the destination. |
| `alice-ui-design-brief.md` | Alice's profile at `/entities/alice` is the first profile most visitors will see — it should be indistinguishable in structure from any other entity's profile. Alice's warmth is in Alice's own `/alice` route, not in her profile page. |
| `2026-04-05-entity-descriptions.md` | The one-liner taglines from that brief are the tagline field in this profile's identity header. |
| `insiders-section.md` | No crossover at MVP. A future version of this page may surface a "This entity's work is part of Insiders" badge — out of scope for now. |

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
