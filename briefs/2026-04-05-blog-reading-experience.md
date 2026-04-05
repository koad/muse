# Design Brief: Blog Reading Experience
**Date:** 2026-04-05
**Author:** Muse
**Routes:** `/blog/series/:series-slug` (series index), `/blog/:slug` (single post), cross-post nav
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation
**Depends on:** `2026-04-05-blog-layout.md` (post page and /blog index — already complete)

---

## Scope

`2026-04-05-blog-layout.md` covers the single-post page structure and the flat `/blog` index. This brief fills in the pieces that brief deferred or underspecified:

1. **Single-post reading experience at depth** — typography rationale for 2,000-word technical posts, series context treatment, code block styling rationale, and the amber question.
2. **Series index page** — how the 20-post Reality Pillar series is presented as a navigable collection.
3. **Cross-post navigation** — in-post series linking beyond prev/next arrows.
4. **"Naming What We Built" standalone series** — how these posts differ from the daily Reality Pillar posts and how they coexist in the blog.

These pieces compose into the complete reading experience across Faber's 27-post catalog.

---

## 1. Single-Post Reading Experience

### Typography for 2,000-Word Technical Posts

The existing brief (`2026-04-05-blog-layout.md`) specifies `17px / 1.75 line-height / Inter`. The rationale is worth making explicit because Vulcan will be tempted to adjust these values.

**Why 17px body size:**
Browser default is 16px. 17px is a single-point increase that shifts reading from "this feels like a small UI component" to "this feels like a document." For 2,000-word posts with code blocks interspersed, 16px creates fatigue over the reading session. 17px does not. Do not round this up to 18px — 18px begins to feel editorial in a way that conflicts with the technical-dispatch aesthetic. 17px is the functional midpoint.

**Why 1.75 line-height:**
Posts in the Reality Pillar series contain prose paragraphs, then code blocks, then prose again. The rhythm of switching between dense monospace and readable prose requires the prose to breathe. At 1.5 line-height, the body text competes with the code blocks visually — both feel equally dense. At 1.75, prose paragraphs are clearly the reading mode; code blocks are clearly the inspect mode. The eye knows what to do.

**Why 720px max-width:**
At 17px body size, 720px yields approximately 75 characters per line. The research-validated sweet spot for comfortable reading is 65–80 characters. At 800px+ the reader's eye must travel too far between line endings. At 640px or below, line breaks fall on individual clauses and the prose loses its sentence rhythm. The existing brief's 720px is correct.

**Why no font size change on mobile:**
17px on mobile is not too large. The counter-argument — "mobile screens are small, reduce the size" — is wrong for this content type. These posts are read start to finish, not skimmed. Readability requires size. The 720px max-width naturally adapts to mobile via the container padding; the line count increases but the per-character legibility stays right. Never reduce below 17px.

---

### Series Context: The Reader's Orientation Problem

A reader who arrives at Day 9 from a shared link has no idea they're mid-series. They need orientation without interruption.

The series badge in the post header (specified in `2026-04-05-blog-layout.md`) answers "what series is this and which day." The footer series navigation block answers "where does this sit in the sequence." But there is a third layer: the reader needs to understand the *shape* of the series — not just position, but what the series is doing.

**Series context strip** — a component not in the original brief:

Placed immediately after the post header divider, before the first paragraph:

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  This post is part of the 2-Week Reality Proof — 20 posts      │
│  documenting a live koad:io operation in April 2026.           │
│  Start at Day 1 →  or  Read the series overview →             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Styling:**
- Background: `--color-bg-secondary` (#141418)
- Left border: 3px solid `--color-border-strong` (#3a3a44) — not accent; this is informational, not a CTA
- Border-radius: 0 4px 4px 0
- Padding: `var(--space-4)` (`16px`) all sides
- Font: Inter 14px, `--color-text-secondary`
- "Start at Day 1 →" and "Read the series overview →" are `--color-accent` links, underline on hover

**Conditional rendering:**
- Only render if: post has a `series` frontmatter field AND the series has a defined index page
- Do not render for standalone series posts without a series index page (the standalone design is handled below)
- Do not render on Day 1 of a series — there is no "start at Day 1" for the reader already there

**Placement:** Immediately after the header divider, before the first `<h2>` or paragraph. This is the only structural intrusion between header and body. It is small, subdued, and positioned where a reader about to start the article will see it once and then scroll past. It does not interrupt; it orients.

---

### Code Blocks

The existing brief fully specifies code block anatomy (header bar, syntax highlighting, copy button). Two additions:

**Terminal prompt styling:**
Most Reality Pillar posts show shell commands with a `$` prompt prefix. The `$` should be styled differently from the command itself — muted, so the eye goes immediately to what's being run.

```css
.post-body pre code .line-prompt {
  color: var(--color-text-muted);   /* #64647c */
  user-select: none;                /* copy button skips the prompt */
}
```

When the copy button fires, it copies only the command text, not the `$` prompt or the output lines that follow. Parse: everything after `$\s` on a prompt line is the command; everything else is output. This requires a custom copy handler per block, not the generic `innerText` copy. Mark output lines with a CSS class; exclude them from clipboard copy.

**File path headers:**
Some posts show file contents with a path header like `~/.juno/trust/bonds/juno-to-vulcan.md`. The existing brief handles filename labels via a `# filename.ext` first-line convention. This extends to file paths — if the first line of a fenced block is a comment that looks like a file path (starts with `#` and contains `/`), render it as the filename label in the code block header bar. The path is `--color-text-secondary` in JetBrains Mono 11px.

---

### Does Amber Carry Into the Blog?

The answer is no — and this decision needs to be explicit so it is not revisited.

Alice uses amber (`#F4B844`) as her domain-skin accent. The system accent is violet (`#7c6aff`). The blog is koad:io infrastructure content, not Alice's conversational space. Blog posts are authored by entities other than Alice (Faber, Juno, potentially Veritas and Mercury as more posts are written). The blog belongs to the system, not to Alice.

**Consequence:**
- All accent usage in the blog (series badges, links, active filter tokens, series nav current-day dot) uses `--color-accent` — violet (`#7c6aff`).
- Alice's amber appears only inside Alice's own conversation UI. It does not bleed into the blog even when a blog post is *about* Alice.
- If a future post is written by Alice (possible but not present in the current catalog), Alice's amber is applied only to Alice's author card in the post footer — not to the post header badge or series nav. Author color follows the entity color system from `2026-04-05-entity-product-card.md`.

**Entity color in author cards:**
This is where entity color does appear in the blog: the author card at the post footer uses a 2px left border in the author entity's color. This is a contained signal — it identifies the author without repainting the reading surface.

```
┌─ [2px left border, entity color] ──────────────────────────────┐
│  [Avatar 40px]  Faber                                          │
│                 Content Strategist                             │
│                 Synthesizes research into signal.              │
│                 View Faber's profile →                         │
└────────────────────────────────────────────────────────────────┘
```

Faber's color is Warm Ochre (`#C27C0E`). The left border carries Faber's identity into the card without disrupting the reading surface. This is the only entity-color expression inside a blog post layout.

---

## 2. Series Index Page: `/blog/series/reality-proof`

### Purpose

The series index is not a table of contents. It is the entry point for a reader who wants to read the 2-Week Reality Proof *as a unit* — all 20 posts, in sequence, understanding what they are collectively before starting Day 1.

It is also a reference page for returning readers who know they left off somewhere and want to find their place without remembering the exact post slug.

### Route

```
/blog/series/:series-slug
```

For the 2-Week Reality Proof: `/blog/series/reality-proof`
For Naming What We Built: `/blog/series/naming-what-we-built`
For Week 3 — Community Week: `/blog/series/week-3-community`

Slugs are derived from the series name using the same kebab-case, lowercase transformation used for post slugs.

---

### Layout

```
max-width: 760px   ← slightly wider than post page to accommodate the day grid
margin: 0 auto
padding: 0 var(--space-5) / var(--space-8)
```

Single column. No sidebar.

---

### Series Header

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  ← Back to blog                                                │
│                                                                │
│  2-WEEK REALITY PROOF                                          │  ← series name
│                                                                │     JetBrains Mono 13px
│                                                                │     --text-muted, uppercase
│  20 Days of Proof That Sovereign AI                            │  ← series title
│  Agents Are Operational                                        │
│                                                                │     Inter 700, 36px desktop
│                                                                │     28px mobile
│                                                                │
│  Faber  ·  April 4 – April 20, 2026                           │  ← authorship + date range
│                                                                │     14px, --text-secondary
│  ──────────────────────────────────────────────────────────   │
│                                                                │
│  These 20 posts document koad:io running live on a $200        │
│  laptop in April 2026. Every claim names a commit, an          │
│  issue number, or a file path — you can verify any of it       │
│  by opening a terminal. The intended reader is someone who     │
│  has heard "AI agents can run autonomously" and wants to       │
│  know what that actually looks like.                           │
│                                                                │
│                    [ Start at Day 1 ]                          │  ← primary CTA
│                    /blog/entities-are-running-on-disk          │     violet button
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

The description is sourced from the series index post frontmatter (`2026-04-00-reality-pillar-index.md`). If the series has an index post, use its opening paragraph as the series description here. If it does not, use the first post's title and opening paragraph.

The "Start at Day 1" CTA is a filled violet button. On hover: `opacity: 0.88`, `translateY(-1px)`. This is the primary action — the reader has arrived at the series index to decide whether to start. Make starting easy.

---

### Day Grid

The 20 posts as a unit. The grid communicates the series at a glance: how long it is, how far through it you are (for returning readers), and the shape of the content.

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  ●  Day 1   Entities Are Running on Disk               Apr 4  │
│  ●  Day 2   The Filesystem Is the Interface            Apr 4  │
│  ●  Day 3   Trust Bonds Aren't Policy                  Apr 5  │
│  ●  Day 4   The $200 Laptop Experiment                 Apr 5  │
│  ●  Day 5   Not Your Keys, Not Your Authorization      Apr 6  │
│  ●  Day 6   Sibyl Does Research                        Apr 7  │
│  ●  Day 7   Chiron Wrote a Curriculum                  Apr 8  │
│  ○  Day 8   [coming Apr 9]                                    │  ← unpublished
│  ○  Day 9   [coming Apr 10]                                   │
│  ○  ...                                                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Row anatomy — published post:**

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  ●  Day 1    Entities Are Running on Disk          Apr 4    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

- Status dot (●): 8px, `--color-success` (`#22c55e`) for published posts the reader has not started. `--color-accent` violet for the most recently read post (reading progress state — see below). Prior visited posts: `--color-text-secondary` dot.
- Day label: JetBrains Mono 12px, `--color-text-muted`. "Day N" — uniform width via monospace.
- Title: Inter 500, 15px, `--color-text-primary`. Links to the post. Hover: color becomes `--color-accent`.
- Date: Inter 400, 13px, `--color-text-muted`. Right-aligned. Format: "Apr 4".
- Full row is a link to the post.
- Row height: 44px minimum (tap target).
- Bottom border: 1px `--color-border-subtle`.

**Row anatomy — unpublished post:**

```
│  ○  Day 8    [coming Apr 9]                                  │
```

- Status dot: hollow (○) — via `border: 1px solid --color-border-strong; background: transparent`.
- Day label: same, JetBrains Mono 12px, `--color-text-muted`.
- Title: `[coming Apr 9]` in `--color-text-muted`, italic. Not a link. The date is the expected publish date from the series config.
- No date column on the right — unpublished posts have no pub date.
- Not interactive.

**Progress state:**
The current "furthest read" post in the series is tracked in `localStorage` keyed by series slug. The dot for that post becomes `--color-accent` violet and is labeled with a small inline badge:

```
◉  Day 6   Sibyl Does Research   ← you're here      Apr 7
```

The "← you're here" text is 11px, `--color-accent`, `JetBrains Mono`. It appears inline after the title. On the next visit to the series index, the reader knows exactly where they are without scanning.

This requires a lightweight client-side read of `localStorage` — no server state. The Meteor client sets this key when a user visits a post that has a `series` field. Key: `koad_reading_progress_${seriesSlug}`. Value: the post's day number. On the series index, read this key and apply the progress style to the matching row.

**No return-reader CTA:** Do not add a "Continue reading →" button at the top. The progress dot in the grid is sufficient. Readers know how to scroll to find where they left off. Adding a "continue" button above the grid duplicates information and clutters the header.

---

### Series Index Footer

Below the day grid:

```
─────────────────────────────────────────────────────────────
What to read after this series →
  Naming What We Built — technical deep dives on the architecture
  /blog/series/naming-what-we-built
```

- A thin divider above.
- "What to read after this series →" label: Inter 500, 13px, `--text-secondary`.
- Linked series title: Inter 500, 14px, `--color-accent`, links to the series index.
- Brief descriptor: Inter 400, 13px, `--text-secondary`.
- This section only renders if a `relatedSeries` field is defined in the series config. For the Reality Proof series, `relatedSeries: ["naming-what-we-built"]`. This is manually curated — Faber decides the progression.

---

## 3. Cross-Post Navigation

The post footer series navigation block in the existing brief handles prev/next. This section addresses broader navigation patterns: how posts within a series point to the series as a whole, and how series index pages link between themselves.

### Series Navigation Block — Extended Spec

The footer series nav block from `2026-04-05-blog-layout.md` is extended with one addition: a "View all N posts in this series →" link below the prev/next row.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  2-WEEK REALITY PROOF — Day 6 of 20                         │
│                                                              │
│  ●●●●●●○○○○○○○○○○○○○○                                        │
│                                                              │
│  ← Day 5: Governance Isn't Rules   Day 7: Sibyl Researches→ │
│                                                              │
│  View all 20 posts in this series →                         │  ← added
│  /blog/series/reality-proof                                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

"View all N posts" is 13px, `--color-accent`, no decoration at rest, underline on hover. It links to the series index. This gives readers who arrive at a mid-series post the ability to see the full context without the prev/next chain being the only navigation path.

### In-Body Series References

Faber's posts cross-reference other posts in the series (e.g., "Day 4 showed the PRIMER.md injection pattern"). These inline references should be auto-linked where possible: when the Markdown renderer encounters a reference matching the pattern `Day N` followed by a linked post title, it generates the correct `/blog/{slug}` href. This is an implementation detail for Vulcan's markdown processing pipeline, not a visible design element — but it improves the reading experience without requiring Faber to maintain explicit slugs in every post.

Pattern for the linker (regex):
```
/\[([^\]]+)\]\(\/blog\/([a-z0-9\-]+)\)/  ← standard markdown links — pass through
/Day (\d+)[:—]/  ← bare day references — look up series slug from series config
```

The second pattern is optional for MVP — standard markdown links are sufficient. Flag as a post-MVP enhancement.

### Series-to-Series Navigation

The `relatedSeries` field in series config drives cross-series links in two places:

1. **Series index footer** (specified above)
2. **Post footer** — on the last post of a series (Day 20), the prev/next block's "Next →" position renders: "End of series. Continue with: [Naming What We Built] →" instead of "Next post coming."

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  2-WEEK REALITY PROOF — Day 20 of 20                        │
│                                                              │
│  ●●●●●●●●●●●●●●●●●●●●                                        │
│                                                              │
│  ← Day 19: First Sponsor Acknowledged        End of series  │
│                                                              │
│  Continue with: Naming What We Built →                      │
│  Technical deep dives on the architecture                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

"Continue with" text: `--color-text-muted`, 12px. Series name: `--color-accent`, 14px, links to the series index. Descriptor: `--color-text-muted`, 13px. This closes the series gracefully without a dead end.

---

## 4. "Naming What We Built" Standalone Series

### The Difference

The 2-Week Reality Proof posts are daily dispatches. They have a day number, a publication date, a defined sequence. They are meant to be read in order, and the design system (progress dots, series nav, day labels) assumes ordinality.

The "Naming What We Built" posts are different in structure:

- No day numbers — these posts are published when a concept is ready to be named, not on a schedule
- No fixed total — the series is open-ended; new posts will be added as koad:io develops new architectural patterns
- Non-sequential — readers can enter at any post without missing prior posts (each post fully explains its concept)
- Longer than daily posts — these are technical architecture documents, typically 1,500–2,500 words with multiple code blocks

They are not dispatches. They are reference documents with an editorial voice.

### Design Response

**Series badge** — same styling as Reality Proof badges, but the day/total system is replaced with a simple label:

```
┌──────────────────────────────────────────────┐
│  NAMING WHAT WE BUILT                        │
└──────────────────────────────────────────────┘
```

No "Day N of T". No progress bar. The badge is an identity marker, not a position marker.

**Series context strip** (the component specified above) — present on "Naming What We Built" posts, but the copy changes:

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  This post is part of Naming What We Built — an ongoing        │
│  series naming the architectural patterns in koad:io.          │
│  Each post stands alone.  Browse the series →                  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

"Each post stands alone." is the orienting sentence. It tells the arriving reader: you don't need to go back to Day 1. There is no Day 1.

**Footer series nav block** — simplified for non-sequential series:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  NAMING WHAT WE BUILT                                        │
│                                                              │
│  ← Pre-Invocation Context Assembly     Trust Bonds →        │
│     (alphabetical / date order within series)               │
│                                                              │
│  Browse all posts in this series →                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

- No progress bar dots — the series is open-ended and non-sequential
- Prev/next are ordered by publication date, not by an explicit day sequence
- "Browse all posts in this series →" instead of "View all N posts" — "Browse" signals non-sequential better than "View all"
- Container styling is identical to the Reality Proof series nav block

**Series index page** — `/blog/series/naming-what-we-built`:

The day grid is replaced by a simple post list — the same format as the `/blog` index filtered by series. No day numbers, no progress dots, no "coming soon" rows. Posts appear in reverse chronological order (newest first) because there is no mandated reading order. A reader looking for the post on pre-invocation context assembly should find it at the top of the page if it was the most recent, without having to count down to the right day.

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  ← Back to blog                                                │
│                                                                │
│  NAMING WHAT WE BUILT                                          │
│                                                                │
│  Naming the Architectural Patterns in koad:io                  │
│  An ongoing series. Each post stands alone.                    │
│                                                                │
│  Faber  ·  ongoing                                             │
│  ──────────────────────────────────────────────────────────   │
│                                                                │
│  Pre-Invocation Context Assembly                               │
│  How $CWD selects which agent to wake                          │  ← subtitle
│  Faber  ·  April 5, 2026                                       │
│  ──────────────────────────────────────────────────────────   │
│                                                                │
│  ...more posts as published...                                 │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

Addition to the index list format for this series only: the post's subtitle is shown as a second line under the title. "Naming What We Built" posts have subtitles in their frontmatter (`subtitle:` field). These are part of the post's identity — they sharpen the description. On the /blog general index, subtitles are not shown (the list is too dense). On the series index, they are shown because the reader is in a browsing context, not a scan-and-click context.

**Subtitle styling:** Inter 400, 14px, `--color-text-secondary`. Directly below the title. Not a block element — visually subordinate to the title. Truncated at one line if it extends beyond 80% of the list item width (rare, but possible on mobile).

---

## 5. The Week 3 — Community Week Series

Not called out in the task brief, but present in Faber's catalog and worth noting for implementation consistency.

"Week 3 — Community Week" posts (April 15–20) include entity spotlights, fork invitations, and reader question responses. They are sequential (implied week structure) but do not use day numbers.

**Treatment:** Same as "2-Week Reality Proof" posts but without day labels. The series badge reads:

```
┌──────────────────────────────────────┐
│  WEEK 3 — COMMUNITY WEEK             │
└──────────────────────────────────────┘
```

Series nav: prev/next by date, no progress bar (5 posts does not warrant a 5-dot progress indicator — at that count the dots add visual noise without adding meaning). Instead, replace the dot progress bar with:

```
  Post 3 of 5 in this series
```

Plain text. JetBrains Mono 12px, `--text-muted`. Sufficient.

---

## 6. Standalone Posts (No Series)

Several posts in Faber's catalog have no `series` frontmatter:

- "Alice Was Built Before the Wave" (`2026-04-04-alice-origin.md`) — origin narrative
- "What an Entity Actually Is: Files, Commits, Hooks, Keys" (`2026-04-05-entities-on-disk.md`) — evergreen explainer
- "Your AI Forgets You Every Time" (`2026-04-04-human-os.md`) — general audience

These posts get the full single-post layout but with all series components omitted:
- No series badge in header
- No series context strip above the body
- No series nav block in footer (existing brief already handles this)
- Author card drops directly below tags

**Visual consequence:** These posts feel leaner and faster than series posts. That is intentional — they are accessed from the /blog index without a series context, and readers expect a self-contained piece. The absence of series scaffolding signals "this is a standalone document."

---

## 7. Series Configuration File

The series config (`content/series.yaml` in the existing brief) needs additional fields to support this brief's components:

```yaml
- name: "2-Week Reality Proof"
  slug: reality-proof
  total: 20
  description: "20 posts documenting a live koad:io operation in April 2026. Every claim names a commit, an issue number, or a file path."
  dateRange: "April 4 – April 20, 2026"
  type: sequential          # uses day numbers, progress bar
  relatedSeries:
    - naming-what-we-built
  ctaLabel: "Start at Day 1"
  ctaSlug: entities-are-running-on-disk

- name: "Naming What We Built"
  slug: naming-what-we-built
  total: null               # open-ended series
  description: "Naming the architectural patterns in koad:io. Each post stands alone."
  dateRange: "ongoing"
  type: standalone          # no day numbers, no progress bar, subtitle shown
  relatedSeries: []
  ctaLabel: "Browse the series"

- name: "Week 3 — Community Week"
  slug: week-3-community
  total: 5
  description: "Entity spotlights, fork invitations, and reader questions from Week 3."
  dateRange: "April 15 – April 20, 2026"
  type: short-sequential    # no day labels, text progress only ("Post N of T")
  relatedSeries: []
```

The `type` field drives the series nav template:
- `sequential` → day numbers + dot progress bar (20 dots max; above 20, switch to text)
- `standalone` → "Browse all posts" link, no progress, no order
- `short-sequential` → text progress ("Post N of T"), no dots, no day labels

---

## 8. Relationship to Prior Briefs

| Brief | Relationship |
|-------|-------------|
| `2026-04-05-blog-layout.md` | This brief extends that one. Single-post typography rationale and code block additions build on those specs. Series nav block is extended, not replaced. |
| `2026-04-05-entity-product-card.md` | Entity color system used in author card left border. Faber = Warm Ochre `#C27C0E`. Amber (`#F4B844`) stays in Alice's domain only. |
| `alice-ui-design-brief.md` | Alice's amber accent is explicitly excluded from the blog reading surface. The brief for Alice is a domain skin; the blog uses the system accent. |
| `koad-io-design-system.md` | All tokens sourced from design system v1.1. No new tokens introduced. |
| `2026-04-00-reality-pillar-index.md` (Faber post) | Series description copy on the series index page is sourced from this post's opening paragraph — do not write new marketing copy. |

---

## 9. Implementation Notes for Vulcan

**localStorage reading progress:**
```javascript
// Set on post visit
function markPostRead(seriesSlug, dayNumber) {
  const key = `koad_reading_progress_${seriesSlug}`;
  const current = parseInt(localStorage.getItem(key) || '0');
  if (dayNumber > current) {
    localStorage.setItem(key, String(dayNumber));
  }
}

// Read on series index
function getReadingProgress(seriesSlug) {
  return parseInt(localStorage.getItem(`koad_reading_progress_${seriesSlug}`) || '0');
}
```

Apply this in the Meteor client: call `markPostRead` when a `BlogPost` component mounts with series data. Read `getReadingProgress` when `SeriesIndex` mounts to apply the progress dot styling.

**Series index data:**
The series index page template receives:
```
<SeriesIndex
  series={seriesMeta}         // from series.yaml
  posts={publishedPosts}      // array of published posts in this series, sorted by day
  futurePosts={scheduledPosts}  // array of {day, expectedDate} for unwritten posts
  readingProgress={dayNumber}   // from localStorage (client-side, 0 if unset)
/>
```

`scheduledPosts` is derived from `seriesMeta.total` and the days that don't yet have a published post. The expected date is computed from the series start date + day offset. If `seriesMeta.type === 'standalone'` or `total === null`, the future posts row is omitted.

**Terminal prompt copy handler:**
```javascript
function copyCodeBlock(button, preEl) {
  const lines = Array.from(preEl.querySelectorAll('.line'));
  const commandLines = lines
    .filter(line => !line.classList.contains('line-output'))
    .map(line => {
      const text = line.textContent;
      // Strip leading prompt character
      return text.replace(/^[\$#%]\s/, '');
    });
  navigator.clipboard.writeText(commandLines.join('\n'));
  button.classList.add('copied');
  setTimeout(() => button.classList.remove('copied'), 1500);
}
```

The markdown parser adds `line-output` class to lines that do not start with `$`, `#`, or `%`. This requires a custom rehype plugin or post-processing step — flag for Vulcan's implementation decision.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
