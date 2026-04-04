# Wireframe: kingofalldata.com Insiders Section

**Project:** Insiders (sponsor-gated content, tier-based access)  
**Author:** Muse (UI Beauty Entity)  
**Date:** 2026-04-03  
**Status:** Wireframe  
**Routes:** `/insiders`, `/insiders/dashboard`, `/insiders/join`  
**Spec reference:** koad/vulcan#32

---

## Strategic Context

The Insiders section is a sponsor community — a way for supporters to fund koad:io development and gain early access to features, ops digests, and trust verification tools.

**Two auth paths:**
- GitHub OAuth (checks sponsor status via GitHub Sponsors integration)
- Dark Passenger (sovereign verification via namespace keys + daemon)

**Design principle:** Show all tier content even to lower tiers. Never hide what exists. Greyed-out content with "Upgrade to unlock" invites them toward higher tiers.

---

## Section 1: Sign-In Screen (`/insiders`)

**Purpose:** Entry point. Unauthenticated users see two auth options.

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│                   INSIDER FEED                         │
│                                                        │
│   You're looking at the insider community —           │
│   early releases, ops digests, and trust tools.       │
│                                                        │
│   ╔════════════════════════════════════════════╗      │
│   ║  [ GitHub Mark ]  Sign in with GitHub      ║      │
│   ║  Checks your sponsor status on GitHub      ║      │
│   ║  Sponsors. Fast setup, zero new account.   ║      │
│   ╚════════════════════════════════════════════╝      │
│                                                        │
│   ╔════════════════════════════════════════════╗      │
│   ║  [ Key Icon ]  Use Dark Passenger          ║      │
│   ║  Verified by your namespace keys.          ║      │
│   ║  No OAuth. Proof of your sovereignty.      ║      │
│   ╚════════════════════════════════════════════╝      │
│                                                        │
│                                                        │
│   Not a sponsor yet? → Become one                     │
│                                                        │
│   Back to portal →                                    │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**

**Page layout:**
- Centered, max 500px width
- Padding: `--space-12` top/bottom
- Background: `--color-bg-primary`

**Title section:**
- "INSIDER FEED" — 24px bold, accent color (`--color-accent`)
- Tagline: "You're looking at the insider community..." — 16px, muted secondary, max 600px width

**Auth buttons (two-column grid on desktop, stacked on mobile):**
- Each button is a clickable card: `--color-bg-secondary` background, `--color-border-default` border
- Padding: `--space-6`
- Height: auto, min-height 120px (ensures touch target)
- Icon (left): 32px, accent color
- Icon + text: "Sign in with GitHub" or "Use Dark Passenger"
- Description (below button text): 13px, muted, explains the approach
- Hover: Border brightens to `--color-border-strong`, subtle shadow

**Sign-in button implementation:**
- GitHub: OAuth flow to GitHub Sponsors integration
- Dark Passenger: Trigger daemon connection + namespace key verification (TBD with Vulcan)

**Footer links:**
- "Not a sponsor yet? → Become one" — links to `/insiders/join`
- "Back to portal →" — links to `/`
- Font: 14px, accent color, underline on hover

---

## Section 2: Authenticated Dashboard (`/insiders/dashboard`)

**Purpose:** Tier-appropriate content display. Show progress. Allow upgrades.

### 2a. Welcome Banner

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  ✓ You're an Insider.                                │
│                                                        │
│  [ Level 1: Supporter ] (tier badge)                 │
│  Expires: 2026-05-03                                 │
│                                                        │
│  [ Upgrade to Level 2 ]  (secondary CTA if ready)    │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Background: `--color-bg-secondary` (card)
- Border: 1px `--color-success` (confirms verified status)
- Checkmark icon (16px, green) + text
- Tier badge: `--color-success-subtle` background, `--color-success` text/border, 14px bold
- Expiry timestamp: 12px, muted
- Upgrade CTA: Secondary variant, appears if tier < max

---

### 2b. Feed Section — "This Week's Ops Digest"

```
┌────────────────────────────────────────────────────────┐
│  THIS WEEK'S OPS DIGEST                               │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ [TIMESTAMP] 2026-04-03 12:45 UTC           │       │
│  │                                            │       │
│  │ Juno's Weekly Update                       │       │
│  │                                            │       │
│  │ This week we closed 3 trust bonds with     │       │
│  │ key infrastructure providers. The daemon   │       │
│  │ now supports... [read more]               │       │
│  │                                            │       │
│  │ Tags: #governance #infrastructure #ring   │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ [TIMESTAMP] 2026-04-02 08:30 UTC           │       │
│  │                                            │       │
│  │ Protocol Changelog: Channels v1.2          │       │
│  │                                            │       │
│  │ Breaking: Channel handshake now requires...│       │
│  │ [read more]                               │       │
│  │                                            │       │
│  │ Tags: #protocol #releases                 │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  [Show more posts] →                                  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Section title: 18px bold, muted secondary
- Feed items: `--color-bg-tertiary` background, `--color-border-default` border, padding `--space-4`
- Timestamp: 12px, muted, monospace (JetBrains Mono)
- Post title: 16px bold, accent color (links to full post)
- Preview text: 14px, muted
- Tags: 12px, muted, no background (not buttons, just labels)
- Hover on card: Border brightens, cursor pointer (links to full post)
- Pagination: "Show more posts →" text link at bottom

---

### 2c. Early Releases Section

```
┌────────────────────────────────────────────────────────┐
│  EARLY RELEASES                                        │
│  Latest from the registry. Insiders first.             │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ v1.2.0-beta.1 — Channel Handshake v2      │       │
│  │ Released 1d ago                            │       │
│  │                                            │       │
│  │ Breaking changes to channel initiation.    │       │
│  │ Guides: https://docs/channels/v2           │       │
│  │                                            │       │
│  │ [ View Release Notes ]  [ Download ]       │       │
│  │                                            │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ v1.1.5 — Stability patch                   │       │
│  │ Released 3d ago                            │       │
│  │ ...                                        │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  [See all releases] →                                 │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Section title: 18px bold, muted secondary
- Release cards: `--color-bg-tertiary`, `--color-border-default`, padding `--space-4`
- Version + title: 14px bold, accent color
- Metadata: "Released 1d ago" — 12px, muted
- Description: 14px, muted
- CTAs: Text buttons or small secondary buttons
- Hover: Card lifts slightly (transform: translateY(-2px))

---

### 2d. Tier Structure — Overview (Always Visible)

```
┌────────────────────────────────────────────────────────┐
│  YOUR TIER & UPGRADES                                 │
│                                                        │
│  Level 1: Supporter (Current)                         │
│  ✓ Early releases                                     │
│  ✓ Weekly ops digest                                 │
│  ✓ Member count                                      │
│  $0/mo (Forever free tier)                           │
│                                                        │
│  Level 2: Insider ($10/mo)                            │
│  ✓ Direct message channel                             │
│  ✓ Context bubble preview feed                        │
│  • Plus everything in Level 1                         │
│                                                        │
│  [ Upgrade to Level 2 ] (secondary CTA, faded)        │
│                                                        │
│  ────────────────────────────────────────────────      │
│                                                        │
│  Level 3: Architect ($50/mo)  [LOCKED - Upgrade]     │
│  ⊘ Peer daemon status panel                          │
│  ⊘ Trust bond viewer & signature verification        │
│  ⊘ Plus everything in Level 2                        │
│                                                        │
│  Level 4: Sovereign ($1k/mo)  [LOCKED - Upgrade]     │
│  ⊘ Raw session feeds                                 │
│  ⊘ Private koad channel                              │
│  ⊘ Plus everything in Level 3                        │
│                                                        │
│                                                        │
│  [ Learn More About Tiers ]                           │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**

**Current tier (unlocked):**
- Background: `--color-bg-secondary`, border `--color-success` (1px)
- Checkmarks: `--color-success`
- Price: Bold, accent color
- CTA: Secondary button (outline style)

**Locked tiers:**
- Background: `--color-bg-tertiary`, border `--color-border-default`
- Lock icon (12px) next to tier name
- Feature text: 14px, muted, `opacity: 50%` to show "this exists but greyed out"
- Checkmarks: Replaced with "⊘" (placeholder icon) — shows content exists but is locked
- Price: Still visible (important — let people see what they're working toward)
- CTA: "Upgrade to Level X" — secondary variant, slightly muted

**Design principle:**
- Never hide tier features behind a "click to see" dropdown
- Always show what exists at higher tiers
- Greyed-out state signals "upgrade for access" not "this doesn't exist yet"
- This builds desire for upgrades

---

### 2e. Tier 3 Detail — Trust Bond Viewer (Locked Example)

```
┌────────────────────────────────────────────────────────┐
│  YOUR TRUST BONDS  [LEVEL 3 FEATURE]                 │
│                      [UNLOCK]                         │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ (GREYED OUT AT 50% OPACITY)                │       │
│  │                                            │       │
│  │ Sponsor Bond: koad                         │       │
│  │ Type: GitHub Sponsors                      │       │
│  │ Status: Active (verified)                  │       │
│  │ Signed: 2026-04-01                        │       │
│  │                                            │       │
│  │ ✓ koad has signed a trust bond with you   │       │
│  │                                            │       │
│  │ [ Verify Signature ]  (text button)        │       │
│  │ [ View Bond Details ]  (text button)       │       │
│  │                                            │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  More bonds will appear here when you unlock L3.      │
│                                                        │
│  [ Upgrade to Architect ($50/mo) ]  (secondary CTA)   │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Card: `--color-bg-tertiary`, border `--color-border-default`, padding `--space-6`
- Entire card: `opacity: 50%` when locked (shows shape but greyed)
- Checkmark icon (green): Shows this is a verified bond
- Status badge: `--color-success-subtle` background, `--color-success` text
- Buttons: Text style ("Verify Signature", "View Bond Details")
- Context text below locked card: 14px, muted, explains "more content here at higher tier"
- Unlock CTA: Secondary variant, full contrast (not greyed)

**Interaction (when unlocked):**
- "Verify Signature" → Opens modal showing raw `.asc` file
- "View Bond Details" → Expands card to show full bond metadata

---

### 2f. Tier 4 Detail — Session Feeds (Locked Example)

```
┌────────────────────────────────────────────────────────┐
│  LIVE SESSION FEEDS  [LEVEL 4 FEATURE]               │
│                      [UNLOCK]                         │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ (GREYED OUT AT 50% OPACITY)                │       │
│  │                                            │       │
│  │ Alice Session (alice@koa.io)               │       │
│  │ Status: Live                               │       │
│  │ Uptime: 47d 3h                             │       │
│  │                                            │       │
│  │ Last activity: 2m ago                      │       │
│  │ Inference mode: Daemon-local               │       │
│  │                                            │       │
│  │ [ View Session Logs ]  (text button)       │       │
│  │                                            │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  koad's private channel (read-only invite) available  │
│  at Level 4.                                          │
│                                                        │
│  [ Become a Sovereign ($1k/mo) ]  (secondary CTA)     │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Same greyed-out pattern as Level 3 examples
- Card shows real session data format (at full opacity when unlocked)
- Status indicator: Green dot + "Live" for active sessions
- Metadata: 12px monospace for timestamps and technical data
- CTA context: Explains what's in the private channel
- Unlock CTA: Secondary, full contrast

---

### 2g. Member Count & Community Signal

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│          734 people are building sovereignty.         │
│                                                        │
│          [ Join them ]  [ Back to portal ]            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Centered, `--space-12` padding top/bottom
- Typography: 14px, muted secondary
- CTAs: Text links, inline
- Background: Transparent or very subtle `--color-accent-subtle`

---

## Section 3: Join Page (`/insiders/join`)

**Purpose:** Encourage sponsorship. Show value clearly. Make it easy to become a sponsor.

### 3a. Hero Section

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  BECOME AN INSIDER                                    │
│                                                        │
│  Support koad:io development and join a community    │
│  building the sovereign web.                          │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Title: 28px bold, accent color
- Subhead: 16px, muted secondary
- Centered, max 600px width
- Padding: `--space-12` top/bottom

---

### 3b. Tier Comparison Table

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  ┌─────────────┬──────┬──────┬──────┬──────────┐      │
│  │ Tier        │ L1   │ L2   │ L3   │ L4       │      │
│  │ Price       │ Free │$10/m │$50/m │ $1k/mo  │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Early       │  ✓   │  ✓   │  ✓   │   ✓     │      │
│  │ Releases    │      │      │      │         │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Ops Digest  │  ✓   │  ✓   │  ✓   │   ✓     │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Direct Chat │      │  ✓   │  ✓   │   ✓     │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Trust Bonds │      │      │  ✓   │   ✓     │      │
│  │ & Verify    │      │      │      │         │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Session     │      │      │      │   ✓     │      │
│  │ Feeds       │      │      │      │         │      │
│  ├─────────────┼──────┼──────┼──────┼──────────┤      │
│  │ Private     │      │      │      │   ✓     │      │
│  │ Channel     │      │      │      │         │      │
│  └─────────────┴──────┴──────┴──────┴──────────┘      │
│                                                        │
│  Level 1 is free forever. Upgrade anytime.            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Table: Simple HTML `<table>` with proper semantic markup
- Header row: Bold, background `--color-bg-secondary`, bottom border `--color-border-strong`
- Feature rows: Alternating background (none + very subtle `--color-bg-secondary`)
- Checkmarks: `--color-success` color, bold weight
- Empty cells: Not crossed-out, just empty (implies "not available" without negative imagery)
- Row text: 14px, left-aligned
- Responsive: On mobile, consider horizontal scroll or card layout (6 narrow columns become challenging)

---

### 3c. Call-to-Action Section

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│       Join the Insiders community. Fund             │
│       development. Shape the sovereign web.           │
│                                                        │
│  ┌──────────────────────────────────────────┐         │
│  │ [ GitHub Sponsors Logo ]                 │         │
│  │                                          │         │
│  │ [ Become a Sponsor on GitHub ]           │         │
│  │ (Primary CTA - links to GitHub Sponsors) │         │
│  └──────────────────────────────────────────┘         │
│                                                        │
│  Already a sponsor?  [ Sign In ]  →                  │
│                                                        │
│  Back to portal →                                     │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Title: 20px bold, muted secondary
- GitHub Sponsors logo: Include official mark (check GitHub brand guidelines)
- Primary CTA: "Become a Sponsor on GitHub" — full-width on mobile, max 400px on desktop
- Links to: `https://github.com/sponsors/koad`
- Secondary links: "Already a sponsor? Sign in" and "Back to portal"
- Padding: `--space-12` top/bottom

---

## Global Dashboard Features

### Header/Navigation (on all dashboard pages)

```
┌────────────────────────────────────────────────────────┐
│  kingofalldata.com / Insiders                          │
│                                                        │
│  [Avatar] yourname.koa.io    [ Settings ]  [ Sign out]│
│                                                        │
│  ──────────────────────────────────────────────────────│
│  Feed    Releases    Tier & Upgrades                  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Breadcrumb: "kingofalldata.com / Insiders" (14px, muted)
- Right side: Avatar (32px circular) + name + settings/sign-out links
- Tabs: Horizontal navigation (Feed, Releases, Tier & Upgrades)
  - Active tab: Text `--color-text-primary`, underline `--color-accent`
  - Inactive tab: Text `--color-text-secondary`
- Hover: Underline appears before click (indicates navigability)

---

## Interaction Patterns

### Authentication

**GitHub OAuth:**
- Redirects to GitHub's OAuth consent screen
- Checks if user is a GitHub Sponsor
- Returns tier information via API
- Stores session (JWT or Meteor.js Session)

**Dark Passenger:**
- Requires daemon running
- Triggers namespace key verification
- Checks if namespace is in koad's trust bonds (sponsor verification)
- Returns tier information via daemon

### Tier Unlocking

**When user upgrades:**
1. Redirect to GitHub Sponsors (if GitHub OAuth) or daemon payment processor (if Dark Passenger)
2. Confirm upgrade
3. Return to dashboard with new tier unlocked
4. Show unlock animation (subtle highlight on newly-available features)
5. Toast: "Welcome to Level X"

### Content Expansion

**When user clicks "Read more" on ops digest:**
- Navigate to `/insiders/posts/{post-id}`
- Show full markdown content
- Include related tags with links

**When user clicks "Verify Signature" on trust bond:**
- Open modal with raw `.asc` file
- Copy button: "Copy to clipboard"
- "Verify with GPG" link: Opens external resource or instructions

---

## Mobile Considerations

- Auth buttons (`/insiders`): Stack vertically, full-width
- Dashboard header: Collapse navigation into mobile menu (hamburger icon)
- Tier table: Horizontal scroll (or convert to card layout)
- Feed cards: Full-width with padding `--space-2`
- Touch targets: All buttons/links min 44×44px
- Spacing: Reduce `--space-12` to `--space-8` on mobile

---

## Implementation Notes for Vulcan

- **Auth integration:**
  - GitHub Sponsors: Use `@octokit/rest` for sponsor verification
  - Dark Passenger: Daemon-based verification (TBD with Vulcan team)
  
- **Tier gating:**
  - Pass `tier` value from auth response to template
  - Use `{{#if tier >= 2}}` conditionals for locked features
  - CSS class `.is-locked` for greyed-out state
  
- **Feed/Release data:**
  - Fetch from Juno's markdown posts repo
  - Create simple API endpoint `/api/insiders/posts` and `/api/insiders/releases`
  - Paginate with limit/offset
  
- **Trust bond viewer (Level 3):**
  - Query koad's trust bond registry (git repo with `.asc` files)
  - Parse YAML frontmatter for metadata
  - Display status from verification service
  
- **Session feeds (Level 4):**
  - Query live daemon status (requires daemon API access)
  - Real-time updates: Consider WebSocket for live status
  - Session data: Entity ID, uptime, last activity, mode

---

## Design Tokens Used

- Colors: `--color-bg-primary`, `--color-bg-secondary`, `--color-bg-tertiary`
- Text: `--color-text-primary`, `--color-text-secondary`, `--color-text-muted`
- Semantic: `--color-success`, `--color-accent`
- Spacing: `--space-2`, `--space-4`, `--space-6`, `--space-8`, `--space-12`
- Typography: Inter 600 (titles), Inter 400 (body), JetBrains Mono (technical data)

---

## Anti-Patterns Applied

- ❌ No hidden tier features (all visible, greyed if locked)
- ❌ No "limited time offer" or countdown timers
- ❌ No artificially-high tier prices to make upgrades seem reasonable
- ❌ No deceptive "most popular" badges on tiers
- ❌ No confusing billing cycles (simple $/month)
- ❌ No unsubscribe friction (easy to cancel, documented)

---

*Wireframe by Muse — ready for Vulcan Insiders feature implementation.*
