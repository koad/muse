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

---

## Extension: Auth Flow, Tier States, Dark Passenger UX, Gated Content UI

**Updated:** 2026-04-05  
**Reason:** koad/vulcan#32 — filling in the gaps Vulcan needs to build  
**Design language:** Consistent with Alice gold palette (`#F4B844`) and Stream PWA dark foundation

---

## Section 4: Auth Flow — GitHub OAuth

### 4a. First-time login

When a user arrives at `/insiders` for the first time and clicks "Sign in with GitHub":

**Step 1 — GitHub redirect**

```
[user clicks button]
  → redirect to GitHub OAuth consent screen
  → scope: read:user, read:org (minimum required)
  → GitHub Sponsors sponsorship status is checked server-side
```

The user never sees this in the UI — it is a standard OAuth redirect. No custom interstitial.

**Step 2 — Return to kingofalldata.com/insiders/auth/callback**

Server receives the OAuth code, exchanges for token, queries GitHub Sponsors API for sponsorship tier. Three outcomes:

```
A) Is a sponsor  → create session, resolve tier, redirect to /insiders/dashboard
B) Has GitHub but no sponsorship  → redirect to /insiders/welcome?status=not-a-sponsor
C) OAuth error / denial  → redirect to /insiders?error=auth_denied
```

**Step 3A — First-time sponsor: Welcome interstitial**

Shown once, on first successful login only. Not shown on returning sessions.

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Welcome to the Insider community.                    │
│                                                        │
│  You're now verified as a GitHub Sponsor.             │
│  Your tier: Level 2 — Insider                         │
│                                                        │
│  Here's what you have access to:                      │
│                                                        │
│  ✓ Early releases (before public)                     │
│  ✓ Weekly ops digest                                  │
│  ✓ Direct message channel with koad                   │
│  ✓ Context bubble preview feed                        │
│                                                        │
│  Higher tiers unlock trust bond viewer,               │
│  session feeds, and the private channel.              │
│                                                        │
│  [ Enter the Insiders Feed → ]  (primary, gold)       │
│                                                        │
│  kingofalldata.com / Insiders                         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Background: `#0a0a0a` (portal dark, same as Alice)
- Title: 22px, `#f0ede5`
- "Your tier" badge: `#F4B844` background, `#0a0a0a` text, 12px bold, border-radius 4px, padding 2px 8px
- Checkmarks: `#F4B844` (gold — consistent with Alice success language here, not green, because this is welcome warmth not operational status)
- Primary CTA: full background `#F4B844`, text `#0a0a0a`, 16px bold — the one warm solid button in the ecosystem
- Shown once only — server sets `insiders.first_login_seen = true` on session

**Step 3B — Not a sponsor: Soft redirect**

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  You're logged in as @username.                       │
│                                                        │
│  You don't have an active sponsorship on              │
│  GitHub Sponsors. That's the key to the               │
│  Insiders section.                                    │
│                                                        │
│  No pressure — the path in is open.                   │
│                                                        │
│  [ Become a Sponsor on GitHub ]  (primary gold CTA)   │
│                                                        │
│  [ Continue browsing as a visitor → ]  (text link)    │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- No shame, no accusation. Tone: informational, welcoming.
- "Become a Sponsor" CTA: same gold solid button style
- "Continue browsing" is a ghost link — sends them back to the main portal, no session created
- GitHub avatar is shown (32px, circular) next to @username to confirm the correct account logged in
- Provides an easy escape if wrong account: "Wrong account? Sign in with a different one →" (small, muted, below CTAs)

---

### 4b. Returning user login

Returning users with a valid session are redirected immediately from `/insiders` to `/insiders/dashboard` — no auth screen shown. The sign-in page is only for unauthenticated users.

**Session persistence:**
- Session cookie: 30-day expiry, refreshed on each visit
- No "remember me" checkbox — always remembers (Insiders section is low-risk)
- If session expires, user lands at `/insiders` with a subtle banner: "Your session expired. Sign in again." (12px, muted, above the auth buttons)

**Returning user with lapsed sponsorship:**
If a returning user's GitHub sponsorship has lapsed since last login:

```
┌────────────────────────────────────────────────────────┐
│  ⚠  Your sponsorship has ended.                       │
│                                                        │
│  You still have access to Level 1 content.            │
│  Renew your sponsorship to restore your Level 2+      │
│  access.                                              │
│                                                        │
│  [ Renew on GitHub Sponsors → ]  (gold CTA)           │
│  [ Continue with Level 1 access ]  (ghost link)       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Banner: `--color-bg-secondary` with amber left border (4px, `#fbbf24`)
- Warning icon (`⚠`) in amber
- Does NOT immediately revoke access — L1 is always available
- Shown inline in dashboard header on first return visit after lapse; dismissed on click or after 10s

---

### 4c. Post-auth landing

**Successful sponsor login → `/insiders/dashboard`**

The dashboard is the default landing after any successful auth. Tabs are visible immediately. The welcome banner (section 2a) is shown at top if this is first login, otherwise it is replaced by a compact identity strip.

**Compact identity strip (returning users, shown instead of full welcome banner):**

```
┌────────────────────────────────────────────────────────┐
│  [ avatar 24px ]  @username   ·   Level 2 — Insider   │
│                                          [ Settings ]  │
└────────────────────────────────────────────────────────┘
```

- Background: transparent (blends into dashboard header)
- Avatar: GitHub avatar, 24px circle
- @username: 14px, `--color-text-secondary`, monospace
- Tier badge: inline, 12px, `#F4B844` text (no background on compact variant — only filled on welcome screen)
- Settings: text link, 12px, muted

---

## Section 5: Tier States — Complete Visual Matrix

Five user states exist. Each produces a different view of the dashboard.

### State 0: Not logged in

- User sees: `/insiders` sign-in screen only (Section 1)
- No dashboard access
- No teaser content — the sign-in page is the full surface
- The "Not a sponsor yet?" link goes to `/insiders/join`

---

### State 1: Logged in, no sponsorship

Reached when: GitHub OAuth succeeds but no active sponsorship found.

**Dashboard access:** None. User is redirected to the "not a sponsor" screen (Section 4a, Step 3B).

**Exception:** If user previously had a sponsorship and it has now lapsed, they land on the dashboard with a lapsed-sponsorship warning banner and L1 access only (same as State 2 below but with the renewal prompt).

---

### State 2: Level 1 — Supporter (free tier / first sponsor entry point)

Reached when: GitHub sponsorship active at the $0 or lowest tier.

**Dashboard shows:**
- Welcome banner with "Level 1 — Supporter" badge (green border, same as Section 2a)
- Feed: visible — ops digest posts are readable
- Releases: visible — early release cards are readable
- Tier & Upgrades panel: Current tier highlighted (L1), L2–L4 shown greyed with upgrade CTAs

**What is locked:**
- Direct message channel (L2)
- Context bubble preview feed (L2)
- Trust bond viewer (L3)
- Session feeds (L4)
- Private koad channel (L4)

**Identity strip tier badge:**
```
Level 1 · Supporter
```
Badge color: `--color-success` (green) text, no filled background — clean, verified, but not warm gold (gold is reserved for Alice and the welcome moment)

---

### State 3: Level 2 — Insider ($10/mo)

Reached when: GitHub sponsorship at Insider tier.

**Dashboard shows:**
- Welcome banner with "Level 2 — Insider" badge
- Feed: fully readable
- Releases: fully readable
- Direct message channel: unlocked (new tab in nav: "Channel")
- Context bubble preview feed: unlocked (appears in Feed section as a separate subsection)
- Tier panel: L1 + L2 unlocked (green checkmarks), L3–L4 greyed

**Channel tab (appears at L2+):**

```
┌────────────────────────────────────────────────────────┐
│  DIRECT CHANNEL                                        │
│                                                        │
│  A direct line to koad and the team.                  │
│  Messages are read by humans, not bots.               │
│                                                        │
│  ─────────────────────────────────────────────────   │
│                                                        │
│  koad   [3d ago]                                       │
│  Hey — if you're exploring the Dark Passenger docs,   │
│  the updated spec is at /docs/dp/v2. LMK if anything  │
│  is unclear.                                           │
│                                                        │
│  ─────────────────────────────────────────────────   │
│  [Message koad...]                      [Send ↵]      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

Design follows Stream PWA chat conventions: entity name + timestamp, message below, no emoji toolbar.

---

### State 4: Level 3 — Architect ($50/mo)

Reached when: GitHub sponsorship at Architect tier.

**Dashboard shows:**
- L1 + L2 content, plus:
- Trust Bond Viewer tab: unlocked
- Trust bond cards are at full opacity (no longer greyed)
- "Verify Signature" and "View Bond Details" buttons are active

**Trust bond viewer at full access:**

```
┌────────────────────────────────────────────────────────┐
│  YOUR TRUST BONDS                                      │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ Sponsor Bond                               │       │
│  │ Issued by: koad                            │       │
│  │ Type: GitHub Sponsors                      │       │
│  │ Tier: Architect                            │       │
│  │ Status: ● Active (verified)                │       │
│  │ Signed: 2026-04-01                        │       │
│  │                                            │       │
│  │ ✓ koad has signed a trust bond with you   │       │
│  │                                            │       │
│  │ [ Verify Signature ]  [ View Bond Details ]│       │
│  └────────────────────────────────────────────┘       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes for verified state:**
- Card: full opacity, `--color-bg-secondary`, left border 2px `--color-success`
- Status dot: green (`#4ade80`) inline before "Active"
- "✓ koad has signed..." — 13px, `--color-success`
- Buttons: text style, `#F4B844` on hover (gold hover consistent with Insiders warm accent)

---

### State 5: Level 4 — Sovereign ($1k/mo)

Reached when: GitHub sponsorship at Sovereign tier.

**Dashboard shows:**
- All previous content, plus:
- Session Feeds tab: unlocked
- Private Channel tab: unlocked (separate from L2 Direct Channel — this is read-only, koad's own unfiltered feed)

**Session feeds at full access:**

```
┌────────────────────────────────────────────────────────┐
│  LIVE SESSION FEEDS                                   │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ ● Alice Session          alice@koa.io      │       │
│  │ ─────────────────────────────────────────  │       │
│  │ Uptime:         47d 3h                     │       │
│  │ Last activity:  2m ago                     │       │
│  │ Inference mode: Daemon-local               │       │
│  │ Tasks open:     3                          │       │
│  │                                            │       │
│  │ [ View Session Logs ]  (text button)       │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ ◐ Juno Session           juno@koa.io       │       │
│  │ idle 12m · last: assigned koad/vulcan#35   │       │
│  │ [ View Session Logs ]                      │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

Uses Stream PWA state indicators (●/◐/○/⚠) — sovereign users are deeply familiar with the ecosystem and expect operational language.

---

### Tier state summary table

| State | Auth? | Tier | Feed | Releases | Channel | Trust Bonds | Session Feeds |
|-------|-------|------|------|----------|---------|-------------|---------------|
| 0 | No | — | — | — | — | — | — |
| 1 | Yes | None | — | — | — | — | — |
| 2 | Yes | L1 Supporter | ✓ | ✓ | locked | locked | locked |
| 3 | Yes | L2 Insider | ✓ | ✓ | ✓ | locked | locked |
| 4 | Yes | L3 Architect | ✓ | ✓ | ✓ | ✓ | locked |
| 5 | Yes | L4 Sovereign | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Section 6: Dark Passenger Connection UX

### 6a. Entry point

Dark Passenger login is the second option on the `/insiders` sign-in screen. It is not an OAuth flow — it is a local daemon handshake.

When a user clicks "Use Dark Passenger":

**Case A: User has a running Dark Passenger daemon**

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Connecting to Dark Passenger...                      │
│                                                        │
│  ○ ─────────────── ●  (animated progress bar)         │
│                                                        │
│  Checking localhost:4747                              │
│                                                        │
└────────────────────────────────────────────────────────┘
```

The page attempts a local WebSocket handshake to the Dark Passenger daemon (default: `ws://localhost:4747`). The daemon performs namespace key verification and returns a signed token.

On success (< 3s typical):

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  ✓ Dark Passenger connected.                         │
│                                                        │
│  Namespace: koad.koad.io                              │
│  Key: Ed25519 · A1B2 C3D4...                          │
│  Tier: Level 3 — Architect (from trust bond)          │
│                                                        │
│  [ Enter the Insiders Feed → ]  (gold CTA)            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Connecting state: Animated single horizontal bar, `#F4B844` progress color on dark track — 1.5s loop, doesn't complete until response received
- Success state: ✓ icon in `#F4B844`, namespace and key in JetBrains Mono 12px
- Tier badge: inline, `#F4B844` text, 12px bold
- Auto-advances after 1.5s of displaying success (no click required) — feels authoritative
- "Wrong namespace? Disconnect and choose a different one →" text link in muted, below the entry button

---

**Case B: Daemon not detected (localhost:4747 unavailable)**

Shown after a 4s timeout or immediate connection refusal.

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Dark Passenger isn't running.                        │
│                                                        │
│  Dark Passenger is the local daemon that manages       │
│  your koad:io identity on your machine. It needs      │
│  to be running for sovereign login to work.           │
│                                                        │
│  ──────────────────────────────────────────────────   │
│                                                        │
│  Already have koad:io?                                │
│                                                        │
│  1. Open a terminal                                   │
│  2. Run: koad start                                   │
│  3. Return here and click Try Again                   │
│                                                        │
│  [ Try Again ]  (secondary, outline)                  │
│                                                        │
│  ──────────────────────────────────────────────────   │
│                                                        │
│  New to koad:io?                                      │
│                                                        │
│  Get the framework — it takes 5 minutes to install.  │
│  Or sign in with GitHub to use Insiders without it.  │
│                                                        │
│  [ Install koad:io → ]  (text link)                   │
│  [ Sign in with GitHub instead → ]  (text link)      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- No error styling — this is not an error, it is an expected state for new users
- Tone: calm, instructional. "Dark Passenger isn't running." — declarative statement, no apology
- Three-step terminal instructions: numbered list, monospace for `koad start`
- "Try Again" is a polling re-attempt — re-runs the connection check without full page reload
- "Install koad:io" links to docs installation page
- "Sign in with GitHub instead" returns the user to the standard OAuth path — this is the graceful fallback
- Section separator between "already have it" and "new to it" — two different audiences, don't blur them

---

**Case C: Daemon running but namespace not in sponsor registry**

The daemon is running and key verification succeeds, but the namespace has no active sponsorship bond on record.

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Connected: koad.koad.io                              │
│                                                        │
│  Your namespace is verified, but it doesn't have      │
│  a current sponsorship bond with koad.                │
│                                                        │
│  To get Insider access via Dark Passenger, your       │
│  namespace needs to appear in koad's trust bond       │
│  registry.                                            │
│                                                        │
│  ──────────────────────────────────────────────────   │
│                                                        │
│  Option A: Become a GitHub Sponsor, then request      │
│  a trust bond via the Insiders request form.          │
│                                                        │
│  [ Become a Sponsor on GitHub → ]                     │
│                                                        │
│  ──────────────────────────────────────────────────   │
│                                                        │
│  Option B: Sign in with GitHub to check your          │
│  sponsor status directly.                             │
│                                                        │
│  [ Sign in with GitHub → ]                            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Namespace shown at top confirms the connection worked — user knows their daemon is healthy
- Explains the bond model without jargon ("trust bond registry" is used but immediately explained by context)
- Two options — doesn't corner the user; maybe they sponsored via GitHub and just haven't linked the bond yet

---

### 6b. Dark Passenger status display (once logged in)

For users authenticated via Dark Passenger, the compact identity strip (Section 4c) shows daemon status in addition to name and tier:

```
[ avatar ]  koad.koad.io   ·   Level 3 — Architect   ·   ● Daemon connected
```

- "Daemon connected" uses Stream PWA `● active` green dot + label
- If the daemon disconnects mid-session: dot turns grey, label reads "○ Daemon offline" — the session itself stays valid (it was established), but a banner appears if the user tries to access features requiring live daemon data (trust bond verification, session feeds)

**Mid-session daemon disconnect banner:**

```
┌────────────────────────────────────────────────────────┐
│  ○  Dark Passenger connection lost.                   │
│  Live features paused. Reconnect to resume.           │
│                                [ Try Reconnect ]      │
└────────────────────────────────────────────────────────┘
```

- Banner: amber left border, `--color-bg-secondary`, inline at top of content area (not a modal — doesn't block reading)
- Auto-retries silently every 30s; banner dismisses when reconnected
- Static content (feed posts, releases) remains fully readable — only live features are affected

---

### 6c. Dark Passenger connection port configuration

Not shown in main UI. For power users who run daemon on a non-default port, a small "advanced" link appears in the daemon-not-detected screen (Case B):

```
Running on a custom port?  [ Configure connection → ]
```

Clicking reveals an inline text input:

```
Daemon host:port  [ localhost:______ ]   [ Connect ]
```

- Input: 6-character monospace port number field
- On submit: re-runs the connection check against the custom endpoint
- Value persisted to localStorage as `dp.custom_port`
- Not surfaced prominently — this is an escape hatch, not a primary path

---

## Section 7: Gated Content UI

### 7a. Locked content block — visual anatomy

A locked content block is used when a tier-gated section exists in the page flow but the current user's tier doesn't grant access. The pattern applies to any block: an ops post, a channel, a trust bond card, a session feed entry.

**Full locked block:**

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  LEVEL 3 FEATURE  ·  ARCHITECT                       │
│                                                        │
│  ┌────────────────────────────────────────────┐       │
│  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │       │
│  │ (CONTENT VISIBLE AT 20% OPACITY — blurred) │       │
│  │ ░░░░░░░░░ TRUST BOND VIEWER ░░░░░░░░░░░░░  │       │
│  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │       │
│  └────────────────────────────────────────────┘       │
│                                                        │
│  Unlock this with Level 3 — Architect.               │
│                                                        │
│  [ Upgrade to Architect ($50/mo) → ]  (gold outline)  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Anatomy:**

1. **Tier label strip** — above the blurred block. Small caps, `--color-text-secondary`, 11px:
   `LEVEL 3 FEATURE  ·  ARCHITECT`

2. **Blurred content preview** — the actual component, rendered at:
   - `opacity: 0.20`
   - `filter: blur(3px)`
   - `pointer-events: none`
   - `user-select: none`
   This is enough to show the shape and density of what's behind the lock without revealing readable content. The human brain reads "there is something here" without reading what it is.

3. **Lock overlay** — centered over the blurred preview:
   - Lock glyph (SVG, 20px, `--color-text-secondary`)
   - No text — the tier label above already explains it

4. **Unlock copy** — below the block, 14px, `--color-text-secondary`:
   `Unlock this with Level 3 — Architect.`

5. **Unlock CTA** — primary action:
   - Outline button style: `border: 1px solid #F4B844`, text `#F4B844`, background transparent
   - Hover: `background: rgba(244, 184, 68, 0.08)`
   - Label: `Upgrade to Architect ($50/mo) →`
   - Links to GitHub Sponsors at the relevant tier

---

### 7b. Locked content — two CTA variants

The CTA differs based on what's required to unlock:

**Variant A: Upgrade required (sponsor at higher tier)**

```
[ Upgrade to [Tier Name] ([price]/mo) → ]
```

Used when: user is logged in but at a lower tier than required.

**Variant B: Install daemon required (Dark Passenger)**

Some features (session feeds, trust bond verification) require a live daemon connection even when the tier is sufficient. If a user has the right tier but no daemon connected:

```
┌────────────────────────────────────────────────────────┐
│  LEVEL 3 FEATURE  ·  REQUIRES DARK PASSENGER          │
│                                                        │
│  [blurred preview]                                     │
│                                                        │
│  This feature works with your local Dark Passenger    │
│  daemon. Your tier is high enough — you just need     │
│  the daemon running.                                  │
│                                                        │
│  [ Connect Dark Passenger → ]  (gold outline)         │
│  [ Learn what Dark Passenger is → ]  (text link)      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Design notes:**
- Tier label strip reads `LEVEL 3 FEATURE  ·  REQUIRES DARK PASSENGER` instead of just the tier name
- Distinguishes clearly: "you have the access level, you need the tool"
- "Connect Dark Passenger" → triggers the connection flow (Section 6a) inline — doesn't redirect to sign-in
- "Learn what Dark Passenger is" → links to docs; essential for users who've paid for Architect but haven't installed the daemon yet

---

### 7c. Inline locked snippet (compact variant)

For use inside a feed or list where only one item in a sequence is locked — don't use a full locked block, use the compact inline variant:

```
┌──────────────────────────────────────────────────────┐
│ ░░░ [locked post title blurred] ░░░                 │
│ Level 2 required  ·  [ Upgrade → ]                  │
└──────────────────────────────────────────────────────┘
```

**Rules for when to use compact vs. full:**
- Compact: item appears in a list/feed alongside unlocked items (preserves layout rhythm)
- Full: item is a standalone section header or primary dashboard feature (trust bonds, session feeds, channel)

---

### 7d. Unlock animation

When a user upgrades their tier (by completing the GitHub Sponsors flow and returning to the dashboard), the previously-locked blocks animate in:

1. Blur transitions out: `filter: blur(3px) → blur(0)` over 600ms, ease-out
2. Opacity transitions up: `0.20 → 1.0` over 600ms, same timing
3. Lock glyph fades out simultaneously
4. Gold border pulse: newly-unlocked block gets a 2px `#F4B844` border that pulses once (opacity 1 → 0 over 1.2s) — a single pulse, not a loop
5. Toast appears (bottom-right): "Level [N] unlocked." — 3s auto-dismiss, `--color-bg-secondary` background, `#F4B844` left border

**Implementation note for Vulcan:**
- The upgrade flow is external (GitHub Sponsors page). The return URL should include a query param: `/insiders/dashboard?tier_upgraded=true`
- On mount with `tier_upgraded=true`: immediately trigger unlock animations on all newly-accessible blocks, then remove the param from URL (replaceState)

---

### 7e. Design token additions (Insiders-specific)

Supplementing the tokens listed in the base brief. The Insiders section inherits the portal's dark foundation but introduces Alice's warm gold for CTAs and welcome moments:

```css
/* Insiders section — gold accent (from Alice palette) */
--insiders-gold:          #F4B844;   /* primary CTA, welcome badge, hover on text links */
--insiders-gold-hover:    #E8A738;   /* gold pressed/hover state */
--insiders-gold-subtle:   rgba(244, 184, 68, 0.08);  /* CTA hover background */
--insiders-gold-dim:      rgba(244, 184, 68, 0.20);  /* locked block border when highlighted */

/* Lock state */
--insiders-locked-opacity: 0.20;    /* blurred content at this opacity */
--insiders-locked-blur:    3px;     /* blur amount on locked previews */
```

**Gold use rules:**
- Gold CTAs (`#F4B844`): upgrade actions, "Enter feed" on welcome screen, Dark Passenger connect
- Gold text: tier badges on welcome/first-login screen only — elsewhere tiers use `--color-success` (green) to match operational language
- No gold in nav, breadcrumbs, or informational text — it is reserved for action

---

## Revised Implementation Notes for Vulcan (koad/vulcan#32)

Supersedes the Implementation Notes in the base brief. Read alongside it.

**Auth:**
- GitHub OAuth: standard OAuth2 flow. Server-side code exchange. Use `@octokit/rest` to hit `GET /user/sponsorship_tiers/{sponsor}` to verify active sponsorship and read tier.
- Dark Passenger: browser-side WebSocket to `ws://localhost:4747`. Page sends a challenge nonce; daemon returns signed response with namespace key. Server verifies signature against namespace key in sponsor registry.
- Session: 30-day JWT cookie. Refresh on each visit. Store `{ github_login, tier, auth_method, first_login_seen, dp_namespace? }`.

**Tier resolution:**
- GitHub OAuth path: tier from GitHub Sponsors API → map to L1/L2/L3/L4
- Dark Passenger path: tier from trust bond registry (koad's trust/ dir), keyed by namespace
- If both methods used by same person: GitHub is canonical; DP is supplemental (daemon features)

**Locked block implementation:**
- Render all content server-side regardless of tier. Apply `.is-locked` CSS class based on `tier` value.
- `.is-locked > .locked-content` gets `opacity: var(--insiders-locked-opacity); filter: blur(var(--insiders-locked-blur)); pointer-events: none;`
- Unlock CTA is a sibling element, always rendered at full opacity outside the locked-content wrapper.
- Do NOT use `display: none` or conditional rendering for locked content — the blurred preview is intentional and load-bearing for the upgrade UX.

**Dark Passenger connection flow:**
- On page load (for DP-capable users): check `localStorage.dp.custom_port` for custom port; default to 4747.
- WebSocket connection is attempted only when user explicitly clicks "Use Dark Passenger" — never auto-attempted on page load.
- Reconnect interval (for already-authenticated DP sessions): 30s passive retry. Display banner on disconnect (Section 6b).

**Unlock animation:**
- Listen for `?tier_upgraded=true` on dashboard mount. Cross-reference against previous tier stored in session. Animate every block where `prev_tier < block_required_tier <= new_tier`.
- Remove query param with `history.replaceState` after animation triggers.

---

*Extended by Muse — 2026-04-05 — for koad/vulcan#32 implementation readiness.*
