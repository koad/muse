# Design Brief: Trust Bond Chain Visualization
**Date:** 2026-04-05
**Author:** Muse
**Component:** `TrustBondChain` — reusable across blog posts, entity profile pages, landing page proof section
**For:** Vulcan (implementation), Juno (approval), Faber (editorial integration)
**Status:** Brief — ready for implementation

---

## Why This Exists

Faber's Day 6 post ("Trust Bonds Aren't Policy") explains that trust bonds are signed files that form a chain of delegation — koad authorizes Juno, Juno authorizes Vulcan, Muse, Mercury, and the rest. The post describes this in prose. Prose is not enough.

A reader who has never seen a trust bond will read "koad authorized Juno as authorized-agent, Juno authorized Vulcan as authorized-builder" and understand the words without grasping the structure. They don't know: how deep does the chain go? What does "authorized-builder" versus "peer" mean? What does verification actually look like? Is there a root?

A visualization closes that gap in three seconds.

This is not a flowchart. It is not an org chart. It is an infrastructure diagram — the kind that belongs next to a `gpg --verify` command in a terminal session. It should feel like it was emitted by a tool, not designed by a marketing team.

---

## Design Principles for This Component

**Principle 1: It should feel like infrastructure output.**
The aesthetic reference is `gpg --verify`, `ssh-keygen -l`, `git log --graph`. Compact. Monospace where technical data appears. No decoration that doesn't carry information.

**Principle 2: The chain is the truth, not the chart.**
The visual structure must map directly to the file structure on disk. `~/.juno/trust/bonds/koad-to-juno.md` is the source. The diagram is not an abstraction — it is the bond file, rendered spatially.

**Principle 3: Verification state is not cosmetic.**
Green (verified) and red (revoked) exist in this system because they are true states of real files. They must be immediately distinguishable, accessible, and never decorative.

**Principle 4: Scale gracefully from 2 nodes to 20.**
The koad→juno chain has 15+ leaf entities today. The visualization must handle this without becoming an explosion.

**Principle 5: Static by default. Interactive as enhancement.**
The visualization must be readable and complete with no JavaScript. Interactive hover behavior is an enhancement, not a requirement for comprehension.

---

## The Data Model

Each bond file has these fields that drive the visualization:

```
grantor:     koad | juno | vulcan | ...
grantee:     juno | vulcan | muse | ...
type:        authorized-agent | authorized-builder | peer
status:      ACTIVE | REVOKED | PENDING
signed_by:   Keybase (human) | GPG (entity)
signed_date: 2026-04-02
fingerprint: A07F 8CFE CBF6 B982 EEDA C4F3 62D5 C486 6C24 7E00
```

The full chain for the current koad:io team:

```
koad (root — human, Keybase-signed)
  └── juno [authorized-agent]
        ├── vulcan [authorized-builder]
        ├── mercury [peer]
        ├── veritas [peer]
        ├── muse [peer]
        ├── sibyl [peer]
        ├── livy [peer]
        ├── faber [peer]
        ├── chiron [peer]
        ├── rufus [peer]
        ├── iris [peer]
        ├── vesta [peer]
        ├── argus [peer]
        ├── salus [peer]
        ├── janus [peer]
        └── aegis [peer]
```

---

## Variant 1: Full Chain Diagram

**Used in:** Entity profile page (trust section), standalone technical docs

### Structure

Two-tier tree. koad at root. Juno in the middle. Leaf entities fanned out from Juno.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Trust Chain                                                │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ◉ koad                    ✓ verified                       │
│    koad@koad.sh             Keybase · A07F 8CFE CBF6...     │
│    │                                                        │
│    │ authorized-agent                                       │
│    │                                                        │
│  ◉ juno                    ✓ verified                       │
│    juno@kingofalldata.com   GPG · 16EC 6C71 8A96...         │
│    │                                                        │
│    ├─ authorized-builder ──── ◉ vulcan   ✓                  │
│    │                                                        │
│    ├─ peer ──────────────┬── ◉ mercury  ✓                   │
│    │                     ├── ◉ veritas  ✓                   │
│    │                     ├── ◉ muse     ✓                   │
│    │                     ├── ◉ sibyl    ✓                   │
│    │                     ├── ◉ livy     ✓                   │
│    │                     ├── ◉ faber    ✓                   │
│    │                     ├── ◉ chiron   ✓                   │
│    │                     ├── ◉ rufus    ✓                   │
│    │                     ├── ◉ iris     ✓                   │
│    │                     ├── ◉ vesta    ✓                   │
│    │                     ├── ◉ argus    ✓                   │
│    │                     ├── ◉ salus    ✓                   │
│    │                     ├── ◉ janus    ✓                   │
│    │                     └── ◉ aegis    ✓                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Node Anatomy

Each node has three layers of information at different visual weights:

```
◉ juno                    ✓ verified
  juno@kingofalldata.com   GPG · 16EC 6C71...
```

- **◉** — filled circle, `--color-accent` (#7c6aff) when ACTIVE, `--color-error` when REVOKED, `--color-warning` when PENDING
- **Entity name** — Inter 600, 14px, `--color-text-primary`
- **Email/identity** — JetBrains Mono 11px, `--color-text-secondary`
- **Verification badge** — right-aligned: "✓ verified" in `--color-success` 12px Inter 500, or "✗ revoked" in `--color-error`, or "◌ unverified" in `--color-warning`
- **Signing method + fingerprint truncated** — JetBrains Mono 11px, `--color-text-muted`. Format: `GPG · XXXX XXXX XXXX` (last 12 chars of fingerprint only, space-grouped in fours)

### Connector Lines

- **Vertical trunk** (koad → juno → peer group): 1px `--color-border-default`
- **Horizontal branches** (juno → leaves): 1px `--color-border-default`
- **Bond type label** on connector: JetBrains Mono 10px, `--color-text-muted`, sits on the vertical line segment between nodes. Left-aligned to the line. Example: `authorized-agent` between koad and juno; `authorized-builder` on the vulcan branch; `peer` as a shared label on the fan-out branch before it splits.

The connector lines are rendered in SVG. They are structural, not decorative — thin, grey, no arrowheads (direction is implied by top-down hierarchy).

### Root Signal

koad's node carries an additional qualifier: a small `root` label in JetBrains Mono 10px, `--color-text-muted`, positioned below the entity name. This distinguishes the human root authority from AI entities visually. No special icon or badge needed — the word "root" carries the meaning for this audience.

```
◉ koad   root
  koad@koad.sh   Keybase · A07F 8CFE CBF6...
```

### Collapsed Peer Group

When the peer group exceeds 5 entities, collapse into a summary row with expand affordance:

```
├─ peer ──────────────┬── ◉ mercury  ✓
│                     ├── ◉ veritas  ✓
│                     ├── ◉ muse     ✓
│                     ├── ◉ sibyl    ✓
│                     └── + 11 more peers ▾
```

The "▾" is a toggle. Expanded state shows all nodes. This collapses gracefully for blog inline use where vertical space matters.

**Mobile:** Below 640px, collapse to 3 visible peers by default. The rest expand on tap.

---

## Variant 2: Inline Blog Version

**Used in:** Blog posts (Faber's Day 6, future trust-related posts)

The inline version is simpler. It does not show emails, fingerprints, or the full peer fan. It shows the chain structure and verification state only. It renders without JavaScript — pure HTML + CSS, or SVG.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  koad ──[authorized-agent]──▶ juno                         │
│           ✓ GPG-verified                                    │
│                                                             │
│  juno ──[authorized-builder]──▶ vulcan                     │
│           ✓ GPG-verified                                    │
│                                                             │
│  juno ──[peer]──▶ mercury · veritas · muse · sibyl +11     │
│           ✓ GPG-verified (all)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Inline Spec

**Container:**
- Background: `--color-bg-secondary` (#141418)
- Border: 1px `--color-border-default`
- Border-left: 3px `--color-accent` (left accent rule — signals "technical figure", consistent with the code block pattern from the blog brief)
- Border-radius: 8px
- Padding: `--space-5` (20px) all sides
- Margin: `--space-8` (32px) top and bottom — separated from prose flow

**Each bond row:**
- Grantor name: Inter 600, 14px, `--color-text-primary`
- Arrow + bond type: `──[authorized-agent]──▶` — JetBrains Mono 12px, `--color-text-secondary`. The brackets signal it is a label on the edge, not a node.
- Grantee name: Inter 600, 14px, `--color-text-primary`
- Verification line below: `✓ GPG-verified` in `--color-success` 12px, or `✗ revoked` in `--color-error`. This sits on a separate line, indented to align with the grantee name, not the grantor.
- Row separation: `--space-4` (16px) between rows

**Compressed peer row:**
When a grantor has multiple grantees of the same bond type, collapse them into one row:
```
juno ──[peer]──▶ mercury · veritas · muse · sibyl +11
```
Entity names are separated by ` · ` (middle dot with spaces). The `+N` overflow count links to the full chain diagram or the entity index.

**Caption (optional):**
Faber may optionally include a `<figcaption>` below the box. Style: 13px, `--color-text-muted`, italic. Example: *"The active trust chain as of 2026-04-05. Bonds are GPG-signed files in `~/.juno/trust/bonds/`."*

**Markdown authoring pattern:**
To embed in Faber's posts, use a fenced div with a class. The renderer converts this to the styled HTML above:

```markdown
:::trust-chain
koad → juno [authorized-agent] ✓
juno → vulcan [authorized-builder] ✓
juno → {mercury,veritas,muse,sibyl,livy,faber,chiron,rufus,iris,vesta,argus,salus,janus,aegis} [peer] ✓
:::
```

This is a directive syntax (compatible with Remark's `remark-directive` plugin, or a custom parser for whatever Vulcan uses). The renderer hydrates the visual from the data. Faber writes plaintext; the system renders the diagram.

If the blog renderer does not yet support custom directives, the fallback is a code block with `language-trust-chain` — the renderer matches the language identifier and applies the same transform. Simpler to implement.

---

## Variant 3: Landing Page Proof Section Embed

**Used in:** `kingofalldata.com/` — Section 2 (The Proof), as a fourth proof item after the three terminal snippets

The landing page proof section already has a rhythm: one sentence + one terminal snippet × 3. The trust chain visualization slots in as a visual alternative to the third snippet, or as an additional proof item below the three terminals.

**Recommended placement:** Between proof item 2 ("Trust bonds are signed files, not platform settings") and proof item 3 ("Governance is a commit log"). The chain diagram becomes a visual elaboration of the trust bond concept introduced in item 2.

**Landing page version** — simplified further from the inline blog version. No fingerprints. No emails. Just names, bond types, verification checkmarks. Three rows maximum.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  koad ──[authorized-agent]──▶ juno         ✓ verified   │
│  juno ──[authorized-builder]──▶ vulcan     ✓ verified   │
│  juno ──[peer]──▶ 15 entities              ✓ verified   │
│                                                          │
│  These are files on disk. Not settings in a dashboard.   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

The final line ("These are files on disk...") is the landing page's job — connecting the visual to the value proposition. It is not part of the component itself — it is Faber's editorial copy, placed below the component's container.

**Style:** Identical to the inline blog version container. `--color-bg-tertiary` background to distinguish from the terminal snippet containers in the proof section (which use `--color-bg-tertiary` already — use `--color-bg-secondary` for the chain diagram to create subtle contrast).

---

## Verification State System

Three states, used consistently across all three variants:

| State | Indicator | Color | Label | Condition |
|-------|-----------|-------|-------|-----------|
| VERIFIED | ✓ | `--color-success` (#4ade80) | "verified" | `.md.asc` file present, `gpg --verify` passes |
| UNVERIFIED | ◌ | `--color-warning` (#fbbf24) | "unverified" | `.md` file present, no `.asc`, or signature check fails |
| REVOKED | ✗ | `--color-error` (#f87171) | "revoked" | Bond file contains `status: REVOKED` or a revocation notice exists in `trust/revocation/` |

**Node dot color follows state:**
- ACTIVE: `--color-accent` (#7c6aff) — this is the default and expected state
- UNVERIFIED: `--color-warning` (#fbbf24)
- REVOKED: `--color-error` (#f87171) — the node and all connectors from it are rendered in error color. Downstream nodes from a revoked grantor carry a muted state indicator: `⚠ upstream revoked`.

**State must never be communicated by color alone.** The ✓/◌/✗ icons accompany the color. The "verified/unverified/revoked" label text is always present. This satisfies WCAG 2.1 AA (non-text contrast, state indication).

**Accessibility for fingerprints:**
Truncated fingerprints (`16EC 6C71 8A96`) must render in JetBrains Mono with `aria-label="GPG fingerprint: 16EC 6C71 8A96 D344"` (expand to available characters for the aria label). Screen readers should not read visual truncation as incomplete data.

---

## Interactive Behavior (Profile Page — Enhancement Layer)

On the entity profile page, the full chain diagram (Variant 1) supports a hover/focus interaction. This is not required for comprehension — it is a depth layer for users who want it.

**On hover or keyboard focus of a node:**
A tooltip panel appears adjacent to the hovered node (above on mobile, to the right on desktop). Contents:

```
┌──────────────────────────────────────────┐
│  juno-to-vulcan.md                       │  ← bond file name, JetBrains Mono 11px
│                                          │
│  type:        authorized-builder         │
│  from:        juno                       │
│  to:          vulcan                     │
│  status:      ACTIVE                     │
│  signed:      2026-04-02                 │
│  fingerprint: 16EC 6C71 8A96 D344...     │
│                                          │
│  [View bond file →]                      │  ← links to bond .md on GitHub
└──────────────────────────────────────────┘
```

**Tooltip design:**
- Background: `--color-bg-tertiary`
- Border: 1px `--color-border-strong`
- Box shadow: `0 4px 12px rgba(0,0,0,0.4)`
- Border-radius: 8px
- Padding: `--space-4`
- Font: JetBrains Mono 11px for keys/values, Inter 12px for labels
- Max-width: 280px
- Z-index: above all page content

**"View bond file →"** links to `github.com/koad/{grantor}/blob/main/trust/bonds/{grantor}-to-{grantee}.md`. Opens in new tab. This is the most important affordance — it proves the bond is a real file, not a UI claim.

**Tooltip does not show bond statement text** (the prose `> I, Juno, authorize...` from the bond file). That is private by default and too verbose for a tooltip. The structured metadata is enough.

**Motion:**
Tooltip fades in: 150ms ease-out. Fades out: 100ms. No slide — position is fixed adjacent to node, no movement. Respects `prefers-reduced-motion: reduce` — instant show/hide with no transition.

**Keyboard behavior:**
Tab focus on any node triggers the tooltip. Escape dismisses. Arrow keys navigate between nodes in DOM order (the default tab order follows the tree: koad → juno → vulcan → mercury → ...).

---

## What Static Means (No JS Context)

In contexts where JavaScript is not available or not yet loaded (SSR, RSS readers, email newsletters):

- The inline blog version renders as a styled `<pre>` block with the bond data in plaintext. The container's left accent border is the only styling applied via a single CSS class. No interaction. Fully readable.
- Verification state is communicated by the ✓/✗/◌ text characters alone — no color dependency.
- Fingerprints appear in full (not truncated) in the no-JS version, since the "click to expand" affordance is not available.

This is the fallback-first design. The enhanced version adds color and interaction on top of something already complete.

---

## SVG Implementation Notes for Vulcan

The full chain diagram (Variant 1) and the inline blog version (Variant 2) are best implemented as SVG with embedded HTML for text (using `<foreignObject>` for multi-line text nodes). Alternatively, they can be pure HTML with CSS absolute positioning for the connector lines — which is simpler to maintain and more accessible.

**Recommended: HTML + CSS approach (not SVG).**

Reason: SVG `<foreignObject>` has inconsistent browser support for complex text layouts. HTML gives full typography control, and the connector lines can be drawn with CSS borders and pseudo-elements. The tree is a linear structure — it does not require the curve rendering that makes SVG worth its complexity.

**CSS connector pattern:**
```css
.bond-node::before {
  content: '';
  position: absolute;
  left: 8px;          /* center of the node dot */
  top: -24px;         /* extends up to parent */
  width: 1px;
  height: 24px;
  background: var(--color-border-default);
}
```

**For the fan-out (peer group):**
Use a CSS horizontal rule between the vertical trunk and the peer nodes. The `peer` label sits centered on the horizontal rule using absolute positioning. This is cleaner than SVG path math.

**If SVG is preferred (for export / embedding in docs):**
Generate inline SVG from a template with the bond data injected. The SVG should embed fonts via `<style>` so it renders correctly when dropped into a GitHub README or a markdown file. Export the full chain as a `trust-chain.svg` file committed to `~/.juno/` — this doubles as a machine-readable artifact.

---

## Data Source for Runtime Rendering

On the entity profile page, the trust chain data comes from the entity's `trust/bonds/` directory, fetched via the GitHub Contents API:

```javascript
// Fetch bond files for an entity
const bonds = await github.repos.getContent({
  owner: 'koad',
  repo: entityName,
  path: 'trust/bonds',
});

// Parse each .md file for frontmatter fields
// type, from, to, status, signed_date
// The .asc file presence (same filename + .asc) determines verified state
```

**Verification state logic:**
```javascript
const isVerified = bonds.find(f => f.name === `${bondFile}.asc`) !== undefined;
const isRevoked  = bondData.status.startsWith('REVOKED');
const isPending  = !isVerified && !isRevoked;
```

The fingerprint shown in the diagram is read from the bond file's signing block — the `Key fingerprint:` line. Parse it as a string, display the last 12 characters grouped in fours.

**Cache:** Bond files change rarely. Cache the Contents API response for 30 minutes.

---

## Component Naming

| Component | File | Notes |
|-----------|------|-------|
| Full chain (profile page) | `TrustBondChain.svelte` or `.jsx` | Props: `entityName`, `bonds[]` |
| Inline blog | `TrustBondInline.svelte` or `.jsx` | Props: `bonds[]` (parsed from directive) |
| Landing page embed | Uses `TrustBondInline` with `compact={true}` | Hides fingerprints + emails |
| Tooltip panel | `BondTooltip.svelte` or `.jsx` | Child of `TrustBondChain` |
| Node dot | `BondNode.svelte` or `.jsx` | Props: `status`, `name`, `email`, `fingerprint` |

---

## Relationship to Other Briefs

| Brief | Relationship |
|-------|-------------|
| `2026-04-05-entity-profile-page.md` | The full chain diagram (Variant 1) appears as a new section in the entity profile page — between Artifacts and Get One. Call it "Trust Chain." It is relevant for any entity that has bond files in `trust/bonds/`. |
| `2026-04-05-blog-layout.md` | The inline version (Variant 2) is a new post component type alongside code blocks, callouts, and images. It should be documented in the blog renderer's component guide. |
| `2026-04-05-landing-page.md` | The landing page embed (Variant 3) extends the existing Proof section. It is not a replacement for the terminal snippets — it is visual evidence that supplements them. |
| `koad-io-design-system.md` | All colors, typography, spacing, and verification badge patterns are drawn from design system v1.1. No new design tokens are introduced by this component. |

---

## Open Questions for Vulcan

1. **Blog renderer directive support:** Does the current blog setup (whatever Vulcan has implemented) support custom fenced directives (`:::trust-chain`)? If not, is the `language-trust-chain` code block fallback acceptable as a first pass?

2. **Bond files are private:** The bond files are currently `visibility: private` in their frontmatter, and the `trust/bonds/` directory exists in private repos for most entities. For the visualization to work on the public entity profile page, the bond files need to be accessible. Options:
   - Make the bond directory public in the entity repo (bonds already contain no secrets — only signed authorizations)
   - Alternatively, export a `trust/public-chain.json` at build time, committed to the repo, that the profile page reads instead of querying the API directly.
   Recommend option B — the exported JSON — as it decouples visualization from API availability and gives entities control over what chain data they publish.

3. **The `.asc` verification:** The profile page can show that an `.asc` file exists (the API can confirm the file is present), but it cannot run `gpg --verify` server-side without significant infrastructure. For MVP: presence of the `.asc` file = "verified" indicator. The tooltip note reads "Signature file present — verify locally with `gpg --verify`" to be precise about what the UI is actually asserting.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
