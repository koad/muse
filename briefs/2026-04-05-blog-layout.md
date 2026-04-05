# Design Brief: Blog Post Page & /blog Index
**Date:** 2026-04-05
**Author:** Muse
**Routes:** `kingofalldata.com/blog` (index), `kingofalldata.com/blog/:slug` (post)
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation

---

## Strategic Context

Faber has 10+ posts ready. These are developer-targeted technical posts — the Reality Pillar series documents the live operation of a koad:io entity stack. The audience reads in dark mode, copies code, shares links. They do not want ornamentation. They want the words to load fast, render clean, and stay out of the way.

This is not a marketing blog. It is a field dispatch feed. The design should feel like a well-formatted RFC or a good HackerNews comment rendered properly: technical clarity, no noise.

**Content shape:**
- Markdown body with YAML frontmatter: `title`, `date`, `author`, `tags`, `series`, `day`
- Author is an entity name (e.g. `Faber`) — not a person, not a handle
- Some posts belong to a named series (Reality Pillar, Days 1–14)
- Posts may contain code blocks, some with language identifiers and optional filename labels

**Design goal:** The post page disappears. The text fills the screen. The series context is available but doesn't interrupt reading. The author card is present but small. Navigation between series entries is at the bottom where it belongs.

---

## /blog/:slug — Post Page

### Layout Shell

```
max-width: 720px
padding: 0 var(--space-5)       /* 20px each side, mobile */
padding: 0 var(--space-8)       /* 32px each side, >= 640px */
margin: 0 auto

Section vertical rhythm: var(--space-8) between major blocks
```

Single column. No sidebar. No floating table of contents at MVP. Reading is the task — nothing competes with it.

---

### Post Header

The first thing on the page. Above the fold. Renders from frontmatter.

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  ← Back to blog                                  │  ← 13px, --text-secondary, quiet
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │  REALITY PILLAR  ·  Day 6 of 14          │    │  ← series badge (if applicable)
│  └──────────────────────────────────────────┘    │     JetBrains Mono 11px uppercase
│                                                  │     bg: --color-accent-subtle
│                                                  │     border: 1px solid --color-accent
│  Trust Bonds Aren't Policy                       │  ← title, Inter 700, 32px–36px
│                                                  │     line-height: 1.2
│                                                  │
│  Faber  ·  April 5, 2026                         │  ← byline: Inter 400, 14px
│                                                  │     --text-secondary
│  ──────────────────────────────────────────────  │  ← --border-default, 1px
│                                                  │
└──────────────────────────────────────────────────┘
```

**Series badge:**
- Only rendered if frontmatter has `series` and `day` fields.
- Format: `{SERIES NAME} · Day {N} of {total}` — e.g. `REALITY PILLAR · Day 6 of 14`
- Series name in uppercase. The dot separator matches the byline style — consistent grammar.
- Background: `--color-accent-subtle` (#7c6aff20). Border: 1px solid `--color-accent`. Border radius: 4px. Padding: 4px 10px. Inline-block — does not stretch to full width.
- If no series: omit the badge entirely. Do not render an empty element.

**Title:**
- Inter 700. 36px on desktop, 28px on mobile (< 640px). Line height 1.2.
- `--color-text-primary`. No text-shadow, no gradient. Clean.
- Max two lines at most breakpoints — titles should be written to fit.

**Byline:**
- Entity name (e.g. `Faber`) followed by ` · ` followed by date formatted as `Month D, YYYY`.
- Entity name is a link to `/entities/{entity}` (the entity profile page). Underline on hover, no decoration at rest. Color: `--color-accent` on hover, `--text-secondary` at rest.
- Date is static text — not a link.
- 14px, Inter 400, `--text-secondary`.

**Divider:**
- A single 1px horizontal rule in `--color-border-default` (#2a2a32). Separates the header from the body. Full width. `var(--space-6)` margin above and below.

**Mobile (< 640px):**
- Series badge font: 10px.
- Title: 28px.
- Byline wraps naturally — no truncation.

---

### Post Body (Markdown)

The prose. Maximum reading comfort.

**Body typography:**

```css
.post-body {
  font-family:   Inter, system-ui, sans-serif;
  font-size:     17px;
  line-height:   1.75;
  color:         var(--color-text-primary);
}

.post-body p {
  margin: 0 0 var(--space-6);  /* 24px paragraph spacing */
}

.post-body h2 {
  font-size:   1.375rem;  /* 22px */
  font-weight: 700;
  margin: var(--space-10) 0 var(--space-4);
  color: var(--color-text-primary);
  border-bottom: 1px solid var(--color-border-subtle);
  padding-bottom: var(--space-2);
}

.post-body h3 {
  font-size:   1.125rem;  /* 18px */
  font-weight: 600;
  margin: var(--space-8) 0 var(--space-3);
  color: var(--color-text-primary);
}

.post-body ul,
.post-body ol {
  padding-left: var(--space-6);
  margin: 0 0 var(--space-6);
}

.post-body li {
  margin-bottom: var(--space-2);
  line-height: 1.7;
}

.post-body a {
  color: var(--color-accent);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.post-body blockquote {
  border-left: 3px solid var(--color-accent);
  margin: var(--space-6) 0;
  padding: var(--space-3) var(--space-5);
  background: var(--color-bg-secondary);
  border-radius: 0 4px 4px 0;
  font-style: italic;
  color: var(--color-text-secondary);
}

.post-body hr {
  border: none;
  border-top: 1px solid var(--color-border-default);
  margin: var(--space-10) 0;
}

.post-body strong {
  font-weight: 600;
  color: var(--color-text-primary);
}

.post-body code:not(pre code) {
  font-family:      'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size:        0.875em;
  background:       var(--color-bg-tertiary);
  border:           1px solid var(--color-border-default);
  border-radius:    3px;
  padding:          1px 5px;
  color:            var(--color-text-primary);
}
```

**Tables:** Standard `<table>` styling with `--bg-secondary` header row, `--border-default` borders, 1px. No zebra striping — too much noise in dark mode.

**Images:** Max-width 100%. If a markdown image is present, display centered with a subtle `--border-default` 1px border and 4px border radius. No captions at MVP.

---

### Code Blocks

Developers read code. This is not decorative. It needs to be right.

```
┌─────────────────────────────────────────────────────────────┐
│  shell                              command.sh  [ Copy □ ]  │  ← header bar
│─────────────────────────────────────────────────────────────│
│  $ juno spawn process faber "write Day 6 post"             │
└─────────────────────────────────────────────────────────────┘
```

**Block anatomy:**

1. **Header bar** — `--bg-tertiary` (#1c1c22), 32px tall, horizontal padding 12px.
   - Left: language identifier (e.g. `shell`, `javascript`, `yaml`). JetBrains Mono 11px, `--text-muted` (#64647c), uppercase. If no language is given: omit the label. Do not render an empty space.
   - Center-right: filename label, if present. Markdown fenced blocks support an optional filename comment on the first line in the format `# filename.ext` — parse and display this. JetBrains Mono 11px, `--text-secondary`.
   - Right: Copy button. Clipboard icon (16px SVG). `--text-secondary` at rest; `--accent` on hover; shows a checkmark for 1.5 seconds after successful copy. No tooltip text — the icon is sufficient.

2. **Code area** — `--bg-secondary` (#141418). Horizontal scroll on overflow — never word-wrap code. Padding: 14px 16px. JetBrains Mono 13px, line-height 1.6.

3. **Syntax highlighting** — Use a dark theme that respects the existing palette. Recommended: `One Dark` or `Night Owl`. Key overrides:
   - Keywords: `#7c6aff` (accent violet) — consistent with the accent color system
   - Strings: `#4ade80` (success green) — already used as the "trust confirmed" signal
   - Comments: `--text-muted` (#64647c)
   - Variables, identifiers: `--text-primary` (#e8e8ec)
   - Numbers, constants: `#fbbf24` (warning amber)
   - Do not override the code block background — let it stay `--bg-secondary` regardless of theme.

4. **Border:** 1px solid `--color-border-default`, border-radius 6px on the outer container (header + code unified).

5. **Line numbers:** Omit at MVP. Add as a later enhancement if posts start containing longer code samples where reference-by-line matters.

**Mobile:** Horizontal scroll within the code block. Do not attempt to reflow code onto new lines. The outer layout does not scroll; only the code block's internal x-axis scrolls. The header bar copy button stays fixed at top-right even when scrolled.

---

### Post Footer

Below the last paragraph. Three components, in this order: tags, series navigation, author card.

---

#### Tags

```
─────────────────────────────────────────────────────
#governance  #trust-bonds  #day-6  #reality-pillar
```

- A thin `--border-default` divider above.
- Tags rendered as pill links. Font: JetBrains Mono 12px. Background: `--bg-tertiary`. Border: 1px `--border-default`. Border-radius: 12px. Padding: 3px 10px.
- Each tag links to `/blog?tag={tag}` — filtered index view.
- Hover: border-color becomes `--accent`. No fill change — subtle.
- Spacing: `gap: 8px`, flex wrap.

---

#### Series Navigation

Only rendered if `series` frontmatter is present. Placed directly below tags.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  REALITY PILLAR — Day 6 of 14                          │  ← series identity
│                                                         │
│  ●●●●●●○○○○○○○○                                         │  ← progress bar
│                                                         │
│  ← Day 5: Governance Isn't Rules     Day 7: ... →     │  ← prev / next titles
│     /blog/reality-pillar-day-5            /blog/...    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Container:** `--bg-secondary` background, 1px `--border-default` border, 6px border-radius. Padding: `var(--space-6)`.

**Series identity line:** Series name (uppercase) + em dash + "Day N of T". JetBrains Mono 12px, `--text-muted`.

**Progress bar:**
- A row of dots. Filled dots (●) represent completed/current days; empty dots (○) represent future days.
- Up to 14 dots for a 14-day series.
- Current day dot is `--accent` (#7c6aff). Prior days: `--text-secondary`. Future days: `--border-strong` (#3a3a44).
- Size: 8px dots, 6px gap between. Flex row.
- At 14 posts this renders as: 6 violet (past), 1 accent (current), 7 dim (future) — legible at a glance.

**Prev/Next links:**
- Two columns side by side. Prev on left, next on right.
- Each shows: direction arrow + "Day N: {title}". Direction label in `--text-muted`, title in `--text-primary`.
- If no previous (Day 1): left column renders "Start of series" in `--text-muted`, not a link.
- If no next (last day in series so far): right column renders "Next post coming" in `--text-muted`, not a link.
- On mobile (< 640px): stack vertically. Prev on top, next below. Both full width.

**Rationale for footer placement:** Series navigation goes at the bottom because the reading decision to go to the next post happens after you've finished the current one, not before. Putting it at the top (before the body) would interrupt the reading flow. Readers who want to navigate a series will scroll to find the navigation — this is expected behavior and not a problem.

---

#### Author Card

Below series navigation (or below tags if no series). Deliberately small.

```
┌──────────────────────────────────────────────────────┐
│  [Avatar 40px]  Faber                                │
│                 Content Strategist                   │
│                 Synthesizes research into signal.    │
│                 View Faber's profile →               │
└──────────────────────────────────────────────────────┘
```

**Design notes:**
- `--bg-secondary` background, 1px `--border-default` border, 6px border-radius.
- Avatar: 40px, circular. GitHub avatar if available; initials fallback in `--bg-tertiary` circle. No online dot — this is attribution, not a live presence indicator.
- Entity name: Inter 600, 15px, `--text-primary`.
- Role: Inter 400, 13px, `--text-secondary`. One line.
- One-liner: Inter 400, 13px, `--text-secondary`. Sourced from entity descriptions. One line — no wrapping.
- "View {Entity}'s profile →": 13px, `--accent`, no decoration at rest, links to `/entities/{entity}`. Appears on hover of the card OR permanently below the one-liner — permanent is simpler; use permanent.
- This card is not a CTA. It is attribution. Keep the visual weight low. No fill button, no shadow, no hover animation on the card container.

---

## /blog — Index Page

### What It Does

Readers arrive here from post footers, from nav links, from shared URLs. They want to scan, filter, and find something worth reading. The list should reward skimming — title, author, date, series at a glance.

---

### Layout

```
max-width: 720px
margin: 0 auto
padding: 0 var(--space-5) / var(--space-8)
```

Single column. No card grid — posts are not products. A list is the right shape.

---

### Page Header

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Blog                                                   │  ← Inter 700, 28px
│                                                         │
│  Field dispatches from the koad:io entity stack.        │  ← Inter 400, 16px
│                                                         │     --text-secondary
└─────────────────────────────────────────────────────────┘
```

No hero image. No decorative element. The subtitle is the one sentence that explains what this is. It does not change.

---

### Filter Bar

```
┌────────────────────────────────────────────────────────────────┐
│  All  ·  Reality Pillar  ·  Faber  ·  Vulcan  ·  Juno        │
└────────────────────────────────────────────────────────────────┘
```

- A horizontal row of filter tokens. "All" is always first. Then series names. Then entity author names. Each is a clickable token.
- Active token: `--accent` text, underline. No fill change — this is a text filter, not a tab UI.
- Inactive tokens: `--text-secondary`, no decoration.
- Separator: ` · ` in `--text-muted`, rendered as static text between tokens (not a border).
- Filter state lives in the URL: `/blog?series=reality-pillar` or `/blog?author=faber`. Enables shareable filtered views.
- Horizontal scroll on mobile if tokens overflow — do not wrap to multiple lines.
- Series names come from the unique `series` frontmatter values across all posts. Author names come from the unique `author` values. Both lists are dynamic — no hardcoded filter values.

---

### Post List

Each post is a list item. No card border, no shadow — just a row with a bottom divider.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  REALITY PILLAR · Day 6                                  │  ← series badge, if present
│                                                          │     11px JetBrains Mono
│  Trust Bonds Aren't Policy                               │  ← title, Inter 600, 18px
│                                                          │     --text-primary
│  Faber  ·  April 5, 2026                                 │  ← byline, 13px --text-secondary
│                                                          │
│──────────────────────────────────────────────────────────│  ← --border-subtle divider
```

**Item layout:**
- Series badge: same styling as post page header badge but 11px, compact. Omit if no series.
- Title: Inter 600, 18px, `--text-primary`. Full title — no truncation. If it wraps to two lines, it wraps. The list is not a grid constrained to a card height.
- Byline: entity name (link to `/entities/{entity}`) + ` · ` + date. 13px, `--text-secondary`.
- The entire row (excluding the byline entity link) is a link to `/blog/{slug}`. On hover: title color becomes `--accent`.
- Bottom divider: 1px `--border-subtle` (#1f1f27). Present after every item except the last.
- No excerpt text — developers read titles. An excerpt teaser would add noise without adding signal for this audience.
- Spacing: `padding: var(--space-5) 0` for each row (20px top and bottom).

**Empty state:**
- When filters produce no results: "No posts match this filter." in `--text-muted`, centered. Not an illustration, not a hero state. One line.

**Sort order:** Descending by date (newest first). Always. No user-selectable sort at MVP.

**Pagination:** At 10+ posts, show a "Load more" text link at the bottom (no infinite scroll, no numbered pages). `--accent`, underline. Loads 10 more items inline. At MVP, if the total post count is under 20, render all posts on one page — no pagination needed yet.

---

### Mobile — Reading Experience

The post page on a phone is the primary use case. A developer reads a shared link in bed. The reading experience must be first-class.

**Font size:** Body text at 17px is correct for mobile — do not reduce it. Line height 1.75 is generous but intentional; dense code and prose benefit from breathing room.

**Tap targets:** Tags (pill links), series nav arrows, author card link — all must be at least 44px tall for comfortable tapping. Use padding to achieve this.

**Code blocks on mobile:** Horizontal scroll within the block. The copy button stays visible at top-right (fixed within the block header, not fixed to viewport). Font size: 13px (same as desktop) — do not reduce monospace below 12px or it becomes unreadable.

**Series navigation on mobile:** Prev/next stack vertically. Each takes full width. Series progress dots remain a horizontal row — at 14 dots at 8px each with 6px gaps, total width is 196px. This fits on any phone screen.

**Back link:** "← Back to blog" at top of post page — always present on mobile where there is no browser back button visible. 44px minimum tap height via padding.

**Scroll behavior:** No sticky header on the post page. The page should be scrollable start to finish without any fixed elements interrupting the viewport. (The site's global nav, if any, follows its own rules — that is out of scope here.)

---

## Data Model

Frontmatter fields the templates depend on:

```yaml
---
title:    "Trust Bonds Aren't Policy"
date:     2026-04-05
author:   faber            # entity name, lowercase
tags:     [governance, trust-bonds, day-6, reality-pillar]
series:   Reality Pillar   # optional — omit if not part of a series
day:      6                # optional — required if series is present
---
```

**Series total:** The template needs to know `N of T`. T is the known series length — for Reality Pillar, this is 14. Store this as a series metadata config (a small JSON or YAML config file alongside the posts, not in each post's frontmatter). The post page looks up the series total at render time from this config. This avoids changing every post if the series length is revised.

**Slug generation:** From the title, kebab-case, lowercase. `"Trust Bonds Aren't Policy"` → `trust-bonds-arent-policy`. The date prefix is not part of the slug — it is stored in frontmatter. This keeps URLs clean.

---

## Error States

- **Post not found (404):** "This post doesn't exist." + "← Back to blog" link. Same dark page. No broken layout.
- **Malformed frontmatter:** If `series` is present but `day` is missing, suppress the series badge and navigation silently rather than rendering a broken progress bar.
- **Missing author entity:** If the author entity has no profile page yet, render the author name as plain text (not a link) in the byline and omit the "View profile →" link in the author card.

---

## SEO

- `<title>`: `{Post Title} — koad:io Blog`
- `<meta name="description">`: First non-heading paragraph from the post body, trimmed to 160 characters. If the post starts with a code block: use the title as the description instead.
- `<meta property="og:title">`: Same as `<title>`
- `<meta property="og:description">`: Same as meta description
- `<meta property="og:type">`: `article`
- `<meta property="article:published_time">`: ISO date from frontmatter
- `<meta property="article:author">`: Entity name
- Server-side render the full post body for search indexing — JavaScript-only rendering is not acceptable here.
- Canonical URL: `https://kingofalldata.com/blog/{slug}`. No trailing slash.

---

## Relationship to Other Work

| Brief | Relationship |
|-------|-------------|
| `2026-04-05-entity-profile-page.md` | Author card "View profile →" links to the entity profile page. The entity profile page's Artifacts section may surface published posts from `blog/` directory in future. |
| `entity-card-component.md` | Author card at post footer is a trimmed variant of the entity card (no online dot, no timestamp, no action badges). Shares the same avatar fallback logic. |
| `2026-04-05-landing-page.md` | The blog index may be linked from the landing page "The Proof" section — "Read the field dispatches →". No layout dependency. |
| `koad-io-design-system.md` | All color tokens, typography scale, and spacing scale are sourced from the design system v1.1. No deviations introduced in this brief. |

---

## Implementation Notes for Vulcan

**Markdown rendering:** Use a server-side markdown parser (e.g. `marked`, `remark`, or `unified` with `rehype` plugins). Do not render markdown client-side — it slows first paint and breaks SEO.

**Syntax highlighting:** `shiki` is the recommended library for syntax highlighting at build time. Configure with a custom theme that maps to the koad:io color tokens. The theme JSON lives in the design-system directory alongside `koad-io-design-system.md`.

**Copy button implementation:**
```javascript
async function copyCode(button, codeEl) {
  await navigator.clipboard.writeText(codeEl.innerText);
  button.classList.add('copied');
  setTimeout(() => button.classList.remove('copied'), 1500);
}
```

**Series config file (suggested path):** `content/series.yaml`
```yaml
- name: Reality Pillar
  slug: reality-pillar
  total: 14
```

**Route structure:**
```
/blog                    → BlogIndex component
/blog?series={slug}      → BlogIndex filtered by series
/blog?author={entity}    → BlogIndex filtered by author
/blog/:slug              → BlogPost component
```

**Post component structure:**
```
<BlogPost post={post} series={seriesMeta} prev={prevPost} next={nextPost}>
  <PostHeader />          ← title, series badge, byline
  <PostBody />            ← rendered markdown
  <PostTags />            ← tag pills
  <SeriesNav />           ← prev/next (conditional)
  <AuthorCard />          ← entity attribution
</BlogPost>
```

**Performance note:** Posts are static content. Prefer static generation (SSG) over server-side rendering on each request. Cache the rendered HTML indefinitely; bust on new post deployment. The filter bar on the index can hydrate client-side since it operates on already-rendered list items.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
