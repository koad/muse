# Design Brief: kingofalldata.com Landing Page
**Date:** 2026-04-05
**Author:** Muse
**Route:** `kingofalldata.com/` (root)
**For:** Vulcan (implementation), Juno (approval)
**Status:** Brief — ready for implementation

---

## Strategic Context

The current homepage drops visitors directly into Alice. For a developer who has just landed from a Hacker News post about "agent home directories" or a Reddit r/selfhosted thread about sovereign AI infrastructure, Alice is a warm face with no introduction. They don't know what they're looking at yet.

This brief specifies a landing page that lives above Alice. It positions koad:io — what it is, how it works, that it exists in the real world — and then hands off to Alice, the entity grid, or the clone command, depending on how the visitor came in and what they're ready to do.

**The ask from the audience:** A skeptical developer who just heard "agent home directory" from a trusted source. They are Unix-fluent, allergic to marketing, and they will close the tab in 8 seconds if you use the word "empower." They want to see something real. A path to a terminal. A git URL. They want to know they can run this on hardware they already own.

**The conversion goal:** Get them to clone one entity within 5 minutes of landing. Not sign up. Not enter an email. Clone.

**Design constraint (Iris, 2026-04-04):** Do not lead with "Not your keys, not your agent," "sovereign AI," or "rings of trust" in above-fold copy. These earn confusion before conviction. Surface them in the proof section, where the architecture is visible, not in the headline.

---

## Section Order

```
1.  ABOVE THE FOLD      ← headline + subhead + CTA (3 seconds)
2.  THE PROOF           ← three terminal snippets (60 seconds)
3.  THE ENTITY GRID     ← team entities with profile links (evidence)
4.  THE ALICE ENTRY     ← onboarding curriculum (for those who want a guide)
5.  THE SPONSOR CTA     ← subtle, non-pushy (for those ready to go deeper)
6.  FOOTER              ← navigation + trust signal
```

---

## Section 1: Above the Fold

**Design goal:** One claim. Verifiable. A developer can open a terminal and confirm it in under 5 minutes.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                   kingofalldata.com                         │
│                                                             │
│         Your AI agent lives on your disk.                   │
│           git repo. Your keys. No vendor.                   │
│                                                             │
│   koad:io is an open-source framework for running           │
│   AI entities as git repos on your own hardware.            │
│   Memory, governance, and trust bonds live on your          │
│   disk. No platform mediates them.                          │
│                                                             │
│              ┌───────────────────────────┐                  │
│              │  git clone github.com/    │                  │
│              │    koad/juno ~/.juno      │  ← copy button   │
│              └───────────────────────────┘                  │
│                                                             │
│         [ Clone an entity ]   [ Meet Alice ]                │
│         (primary — violet)     (secondary — outline)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**The headline:** "Your AI agent lives on your disk."

This is the claim. A developer can verify it by cloning the repo and checking `~/.juno`. The claim maps to a file path. That's what makes it stick with this audience. No adjectives. No promise of transformation. A statement of fact that happens to be interesting.

**The subhead:** "git repo. Your keys. No vendor."

Three noun phrases. No verb. No pitch. The structure mirrors a `man` page: here is what this thing is. The rhythm lands because it matches how developers read.

**Canonical descriptor (Iris, verbatim — do not rewrite):**
> koad:io is an open-source framework for running AI entities as git repos on your own hardware. Memory, governance, and trust bonds live on your disk. No platform mediates them.

This is the third text element. It is 18px, `--color-text-secondary`, not a headline. It provides the sentence-length explanation for those who want it before they act.

**The terminal snippet:** The clone command is in the hero itself. Not after the fold. Right here. Developers don't want to scroll to find the install command. The presence of a `git clone` in the hero is itself a signal: this is infrastructure, not a product tour.

**CTAs:**
- "Clone an entity" → links to `/entities` (the entity directory, where they can browse and pick one)
- "Meet Alice" → links to `/alice` (the onboarding entry point)

Both CTAs are visible above the fold. "Clone an entity" is primary (violet fill). "Meet Alice" is secondary (outline, violet border). The framing respects two kinds of visitors: the one who wants to act immediately, and the one who wants context first. Neither is wrong.

**Design notes:**
- No hero image, no illustration, no gradient wash. The terminal snippet is the visual.
- Site mark (minimalist key/lock icon, 48px) sits above the domain name in the top-left. It is a nav element, not a hero element.
- Font: Inter 700, 36px for headline. Tight leading. Dark background (`--color-bg-primary` #0c0c0e).
- Subhead: JetBrains Mono, 18px, `--color-text-secondary`. Monospace here signals "this is a technical system."
- Terminal snippet: JetBrains Mono 14px, `--color-bg-tertiary` background, `--color-border-default` border, copy button top-right. The copy button renders as a clipboard icon (24px, `--color-text-secondary`), turns `--color-accent` on hover. No tooltip needed.
- Mobile: Single column. CTAs stack full-width. Terminal snippet scrolls horizontally within its own box if needed.

---

## Section 2: The Proof

**Design goal:** Show the architecture in under 60 seconds. Three terminal snippets, three real interactions, zero marketing copy.

This section is for the developer who needs to see before they believe. It does not describe the system — it demonstrates it. Three moments from the actual system, in the order they'd encounter them.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  The architecture, demonstrated.                            │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  1. An entity is a git repo on your hardware.              │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ $ git clone github.com/koad/juno ~/.juno             │  │
│  │ Cloning into '/home/koad/.juno'...                   │  │
│  │ $ ls ~/.juno                                         │  │
│  │ CLAUDE.md   commands/   id/   memories/   trust/     │  │
│  │ $ cat ~/.juno/memories/001-identity.md               │  │
│  │ # Juno — Business Orchestrator                       │  │
│  │ I run koad's operations. My memory lives here.       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  2. Trust bonds are signed files, not platform settings.   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ $ ls ~/.juno/trust/bonds/                            │  │
│  │ koad--juno.md   koad--juno.md.asc                    │  │
│  │ $ cat ~/.juno/trust/bonds/koad--juno.md              │  │
│  │ grantor: koad                                        │  │
│  │ grantee: juno                                        │  │
│  │ scope: authorized-agent                              │  │
│  │ $ gpg --verify koad--juno.md.asc koad--juno.md       │  │
│  │ gpg: Good signature from "koad <koad@koad.sh>"       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  3. Governance is a commit log.                            │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ $ git -C ~/.juno log --oneline -5                    │  │
│  │ de471ae docs: Alice PR status update                 │  │
│  │ ec1131b log: 2026-04-05 Day 6 state update           │  │
│  │ 1810031 log: Day 6 second session — governance       │  │
│  │ ead9a98 log: hook architecture + signed code blocks  │  │
│  │ 63fba0b hooks: embed GPG-signed policy block         │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Section title:** "The architecture, demonstrated." — Inter 600, 18px, `--color-text-secondary`. Not a headline — it's a section label. The snippets speak for themselves.

**Three proof statements (above each snippet):**
1. "An entity is a git repo on your hardware." — lands the core concept.
2. "Trust bonds are signed files, not platform settings." — the "oh, that's different" moment.
3. "Governance is a commit log." — auditability without jargon.

Each statement is 16px, Inter 600, `--color-text-primary`. One sentence. No elaboration — the snippet below it does the work.

**Terminal snippets:**
- JetBrains Mono 13px, `--color-bg-tertiary` background, 1px `--color-border-default` border, 8px radius
- Bash prompt (`$`) in `--color-text-secondary`; command text in `--color-text-primary`; output in `--color-text-secondary`
- No syntax highlighting theatrics — just `$` prompts and output, the way a real terminal looks
- Each snippet is the real system. Not a mock. Juno's actual files, Juno's actual git log.
- Copy button on each snippet (top-right, same spec as hero snippet)

**Layout:** Single column, max 720px centered. Snippets are full-width within that column.

**Mobile:** Same. Snippets scroll horizontally within their own box. No truncation.

**Why this order:** 1 → 2 → 3 maps to the developer's trust-building arc: first understand what a thing is (git repo), then understand what makes it different (signed files, not settings), then understand that it's been running and has a history (commit log). The third snippet is concrete social proof — real commit messages, real timestamps.

---

## Section 3: The Entity Grid

**Design goal:** Show the ecosystem exists. Fourteen named entities, each with a profile link. The grid proves this is a system, not a single project.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  The team.                                                  │
│  Each entity is a git repo. Each is cloneable.             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ ● [Avtr] │  │ ● [Avtr] │  │ ● [Avtr] │  │ ● [Avtr] │   │
│  │  Juno    │  │  Vulcan  │  │  Alice   │  │  Chiron  │   │
│  │ Queen of │  │ Forge    │  │ Through  │  │ Trained  │   │
│  │ the op.  │  │ god.     │  │ looking  │  │ heroes.  │   │
│  │          │  │          │  │ glass.   │  │          │   │
│  │ Profile →│  │ Profile →│  │ Profile →│  │ Profile →│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   [Avtr] │  │   [Avtr] │  │   [Avtr] │  │   [Avtr] │   │
│  │  Mercury │  │  Veritas │  │   Sibyl  │  │   Muse   │   │
│  │ First to │  │ Truth    │  │ Reads    │  │ Where    │   │
│  │ the      │  │ before   │  │ what     │  │ beauty   │   │
│  │ world.   │  │ it ships.│  │ isn't.   │  │ becomes  │   │
│  │          │  │          │  │          │  │intent.   │   │
│  │ Profile →│  │ Profile →│  │ Profile →│  │ Profile →│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   [Avtr] │  │   [Avtr] │  │   [Avtr] │  │   [Avtr] │   │
│  │   Faber  │  │   Rufus  │  │  Salus   │  │  Argus   │   │
│  │ Maker.   │  │ Vivid.   │  │ Watches  │  │ Hundred- │   │
│  │ Turns    │  │ Turns    │  │ the      │  │ eyed.    │   │
│  │ signal   │  │ work to  │  │ pulse.   │  │ Never    │   │
│  │ to keep. │  │ watch.   │  │          │  │ sleeps.  │   │
│  │ Profile →│  │ Profile →│  │ Profile →│  │ Profile →│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  + 6 more entities in the ecosystem →                      │
│    (Aegis, Janus, Copia, Lyra, Iris, Vesta)                │
│                                                             │
│              [ Browse all entities → ]                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Section title:** "The team." — Inter 700, 24px, `--color-text-primary`. Short. Declarative.

**Subhead:** "Each entity is a git repo. Each is cloneable." — Inter 400, 16px, `--color-text-secondary`. This repeats the central claim in the context of the grid, so it lands twice: in the hero and here.

**Grid layout:** 4 columns on desktop (lg), 3 columns (md), 2 columns (sm), 1 column (xs). Auto grid, `min-width 180px`.

**Card spec:** Uses the Team Card variant from `2026-04-04-entity-card-component.md`, with one adaptation: the tagline is truncated to the first 4–5 words (the most evocative fragment) to keep the card tight. Full tagline is available on the entity profile page.

**Online indicator:** Shown on entities that have committed in the last 48 hours. The green dot signals the entity is active — this is real-time evidence, not decoration.

**"Profile →" link:** `--color-accent` text button, routes to `/entities/{entity}` (spec: `2026-04-05-entity-profile-page.md`). Underline on hover only.

**Overflow:** Show 12 entities in the grid (the 12 most active/shipped). The remaining entities appear as a "+6 more" text line with names, linking to `/entities`. Don't hide them — mention them. The quantity signals the breadth of the ecosystem.

**"Browse all entities →":** Primary text button, `--color-accent`, links to `/entities`. This is not a CTA-styled button — it's a navigation invitation.

**Mobile (< 640px):** 2-column grid. Cards are compact. Tagline fragment may be dropped to just the entity name + online dot + "Profile →" link. Simplicity wins over completeness at small sizes.

---

## Section 4: The Alice Entry Point

**Design goal:** Offer a guided path without making it the dominant call to action. Alice fits here as a graceful alternative for visitors who want to learn before they clone.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ╔═══════════════════════════════════════════════════════╗  │
│  ║                                                       ║  │
│  ║  [Alice avatar — minimalist mark, 56px]               ║  │
│  ║                                                       ║  │
│  ║  Meet Alice.                                          ║  │
│  ║                                                       ║  │
│  ║  Not ready to clone? Alice walks you through it.      ║  │
│  ║  A free 12-level curriculum: sovereignty, keys,       ║  │
│  ║  trust bonds, your first entity. Learn by doing,      ║  │
│  ║  at your own pace, in a conversation.                 ║  │
│  ║                                                       ║  │
│  ║  When you finish, Alice signs your certificate.       ║  │
│  ║  Ed25519. Verifiable. Yours.                          ║  │
│  ║                                                       ║  │
│  ║                 [ Start with Alice → ]                ║  │
│  ║              (secondary CTA — amber/gold outline)     ║  │
│  ║                                                       ║  │
│  ╚═══════════════════════════════════════════════════════╝  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**The placement:** Section 4, after the entity grid. A developer who has seen the proof section and the entity grid now has context. If they're ready to act, they've already acted (copied the clone command). Alice appears here for those who want a gentler ramp — not as the primary path, but as a real option.

**Alice's section uses her domain skin:** The card uses Alice's warm amber (`--alice-accent` #F4B844) for the outline border and CTA button border — not the standard violet. This makes Alice's section visually distinct within the landing page, signaling a different kind of experience. The difference is subtle: one card with an amber border in a violet-accented page. It doesn't break the grid; it marks a door.

**Section header:** None. The Alice avatar is the visual signal. "Meet Alice." is the heading (Inter 700, 24px). It is inside the card, not above it — Alice's space begins at the card boundary.

**Body copy logic:**
- Line 1 ("Not ready to clone?") — names the visitor type who belongs here. It is permission-giving, not apologetic.
- Lines 2–3 — the specific curriculum promise: 12 levels, sovereignty, keys, trust bonds, first entity. These map to actual content. They are not marketing adjectives.
- Line 4 — the certificate: Ed25519, verifiable. This earns developer credibility. A real cryptographic artifact at the end of the journey.

**CTA:** "Start with Alice →" — amber outline button (matching Alice's domain skin), not the primary violet fill. The secondary styling is intentional: Alice is an alternative path, not the primary CTA. Size: same 44px height as primary CTAs, but visually subordinate.

**Why "Ed25519. Verifiable. Yours."** — Three noun phrases, same rhythm as the hero subhead. Developers recognize Ed25519 as a real algorithm. "Verifiable" is the proof standard. "Yours" is the sovereignty claim. Three words that map to three developer values.

**Card container spec:**
- Background: `--color-bg-secondary` (#141418)
- Border: 1px `--alice-accent` (#F4B844) — Alice's warm amber
- Border radius: 8px (standard)
- Padding: `--space-8` (32px)
- Max-width: 660px, centered

**Mobile:** Full-width card. Avatar and text stack in single column. CTA is full-width.

---

## Section 5: The Sponsor / Insiders CTA

**Design goal:** Surface the path for those who want to go deeper and support the project. Not pushy. One card. One sentence. Not a pitch — a pointer.

This section does not exist in the hero. It does not compete with any primary CTA. It appears here, after Alice, as the quietest section on the page. Those who scroll this far are interested. The ask is proportional to their demonstrated interest.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Support the project.                                       │
│  ────────────────────────────────────────────────────────  │
│                                                             │
│  koad:io is open source. Sponsors get early access         │
│  to unreleased entities, ops digests, and the Insiders     │
│  feed — a window into how the team actually operates.      │
│                                                             │
│  GitHub Sponsors →     /insiders →                         │
│  (external — new tab)  (internal — Insiders section)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Section title:** "Support the project." — Inter 600, 16px, `--color-text-secondary`. Not primary. This reads as a label, not a sell.

**Body:** One paragraph. Three specifics: early access to unreleased entities, ops digests, Insiders feed. No hyperbole. No "join a growing community." The specifics are what make it believable.

**CTAs:** Two text links, not buttons.
- "GitHub Sponsors →" — opens `github.com/sponsors/koad` in a new tab. External.
- "/insiders →" — routes to `/insiders` (the Insiders section, spec: `2026-04-03-insiders-section.md`). Internal.

Both are `--color-accent` text links. Underline on hover. No fill. No border. These are the quietest interactive elements on the page — appropriate for a sponsorship ask that must not feel pushy.

**No tier listing here.** The tier detail lives on `/insiders/join`. This section's job is to signal that the path exists, not to close the sale.

**Layout:** No card container for this section. Raw, text-forward, no box. The absence of a card is a visual cue that this is not a primary call to action. The separator line above it marks the section boundary.

**Mobile:** Same. Two links on separate lines. No stacking needed — they're text.

---

## Section 6: Footer

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  kingofalldata.com         GitHub   Docs   Blog   Insiders  │
│                                                             │
│  © 2026 koad:io            Privacy  Terms  Contact          │
│                                                             │
│  [key icon]  Your files. Your keys. Your agent.             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Trust signal:** "Your files. Your keys. Your agent." — three short clauses, same rhythm as the hero subhead. This is the sovereignty pitch in its compressed form. The key icon reinforces it visually (24px, `--color-text-secondary`). Together they land the philosophy as a footer note, not a slogan.

**Navigation columns:** Three: Brand (left), primary nav (center), secondary nav (right). Standard footer spec from `2026-04-03-kingofalldata-homepage-v2.md`. 12px, `--color-text-secondary`.

**Mobile:** Single column, center-aligned, normal stacking order.

---

## Page-Level Design Notes

### Layout

```
max-width: 1100px    /* Page container — wider than entity profiles */
padding: 0 var(--space-5)    /* 20px sides mobile */
padding: 0 var(--space-8)    /* 32px sides >= 640px */

Section gap: var(--space-16) /* 64px between sections */
```

The landing page is wider than the entity profile page (1100px vs 720px) because the entity grid requires horizontal space. All text-forward sections (proof, Alice, sponsor) are constrained to `max-width: 720px` within the wider container, keeping line lengths readable.

### Typography

Consistent with koad:io design system v1.1:
- H1 (hero): Inter 700, 36px
- H2 (section titles): Inter 700, 24px
- Section labels: Inter 600, 16-18px, `--color-text-secondary`
- Body: Inter 400, 16px, `--color-text-primary`, line-height 1.6
- Subheads: JetBrains Mono, 18px, `--color-text-secondary`
- Terminal snippets: JetBrains Mono, 13px
- Fine print: Inter 400, 13px, `--color-text-muted`

### Color

Standard koad:io palette v1.1. Alice's section uses Alice's amber domain skin (`--alice-accent: #F4B844`) for her card border and CTA. No other deviations.

| Token | Value | Usage |
|-------|-------|-------|
| `--color-bg-primary` | #0c0c0e | Page background |
| `--color-bg-secondary` | #141418 | Card backgrounds |
| `--color-bg-tertiary` | #1c1c22 | Terminal snippets, inputs |
| `--color-accent` | #7c6aff | Primary CTAs, links |
| `--color-text-primary` | #f0f0f5 | Body text |
| `--color-text-secondary` | #9090a0 | Labels, section heads |
| `--color-border-default` | #2a2a32 | Card borders |
| `--color-success` | #4ade80 | Online dots |
| `--alice-accent` | #F4B844 | Alice's card border + CTA only |

### Animation

No page-load animations. No entrance transitions. No scroll-triggered reveals. The content is the signal — animation would apologize for it. The only motion on this page:

- Terminal snippet copy button: `color` transition 80ms ease on hover
- Entity cards: `transform: translateY(-2px)` + `border-color` transition 80ms ease on hover
- CTAs: `background-color` transition 80ms ease on hover

Everything else is static.

### Anti-Patterns (Do Not Apply)

- No hero image, illustration, or gradient wash above the fold
- No countdown timer, waitlist form, or email capture
- No testimonials carousel in Section 2 (the terminal is the testimonial)
- No badge claiming "used by X developers" — the entity grid is the proof, not a number
- No sticky secondary nav bar within the landing page
- No cookie consent banner (no cookies on this page — landing page is static)
- No chatbot widget (Alice is the conversation — reach her through the proper entry point)

---

## How This Page Relates to What Already Exists

| Existing brief | Relationship |
|----------------|-------------|
| `alice-ui-design-brief.md` | Alice's section on this page is a portal into her experience. The portal is small and warm. The experience is Alice's spec. |
| `2026-04-04-entity-card-component.md` | Entity grid uses the Team Card variant. Same CSS. No new component needed. |
| `2026-04-05-entity-profile-page.md` | Each entity card's "Profile →" links to that spec. This page feeds the profile pages. |
| `2026-04-03-insiders-section.md` | Sponsor section is a pointer to `/insiders`. No duplication of the Insiders UI on this page. |
| `2026-04-03-kingofalldata-homepage-v2.md` | This brief supersedes the homepage v2 wireframe for the root route. The v2 wireframe's "Two Paths" and "Protocol, Simply" sections are not retained — the developer audience for the landing page gets proof (Section 2) instead of narrative, and entity cards (Section 3) instead of abstract protocol diagrams. |

---

## Implementation Notes for Vulcan

**Route:** `/` (root) — replaces current Alice-first home.

**Alice entry point:** Alice moves to `/alice`. The root routes to this landing page. Existing `/alice` deep links continue to work.

**Data required:**
- Entity list (static — from the team entities in TEAM_STRUCTURE.md) — no API call needed for the names and taglines
- Entity online status (GitHub API: last commit date per entity repo) — cache 5 minutes
- Entity avatar URLs (GitHub API: `GET /users/koad/repos` or static from entity GitHub profiles)

**Static content (no API):**
- Terminal snippets in Section 2 — hardcode with real values. These will not go stale faster than the page's relevance.
- Sponsor section links — static.
- Footer — static.

**Performance:** The page should be server-side rendered. The above-fold content (hero + Section 2) has no dynamic data — it renders immediately. Entity grid data (online status, avatars) can hydrate client-side after the initial paint.

**Alice amber deviation:** The one `--alice-accent` reference in Section 4 (card border + CTA button) is the only place this token appears on the landing page. It should be scoped to the Alice card component. Do not allow it to leak into the page-level CSS.

**SEO:**
- Page title: `koad:io — Your AI agent lives on your disk`
- Meta description: "Open-source framework for running AI entities as git repos on your own hardware. Memory, governance, and trust bonds on your disk. No vendor."
- OG card: Text-only preferred — no hero image. If an image is needed, generate a typographic card from the headline.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for Vulcan implementation
