# Wireframe: kingofalldata.com Homepage v2 — Sovereign Web Portal

**Project:** kingofalldata.com (homepage revision)  
**Author:** Muse (UI Beauty Entity)  
**Date:** 2026-04-03  
**Status:** Wireframe  
**Scope:** Two entry paths (AI/entity + collaboration), Alice onboarding, trust positioning

---

## Strategic Context

kingofalldata.com is now the **entry portal for the sovereign web** — not just a namespace provisioning page. The site demonstrates the protocol through two equal entry paths:

1. **AI/Entity side** (Personas 1–3): Profile → daemon → entities → ring
2. **Collaboration side** (Persona 4): Profile → Dark Passenger extension → ring

Both lead to the same infrastructure. The homepage must signal this without jargon.

**One-liner (Iris):**
> The entry point for a sovereign web — where your identity is a git repo, your network is a ring of trust, and your kingdom is whatever you make of it.

---

## Section Order & Structure

### 1. HERO (Above the fold)

**Purpose:** Instant clarity. Sovereignty + two paths. Not a SaaS onboarding — a declaration.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│            [SVG: minimalist key/lattice icon]               │
│                                                              │
│                    kingofalldata.com                         │
│                                                              │
│          Your identity. Your network. Your kingdom.          │
│                                                              │
│   The sovereign web starts with a git repo and a set of     │
│                         keys.                               │
│                                                              │
│         [ Claim Your Namespace ]  [ Meet Alice ]            │
│         (primary - violet)         (secondary - outline)     │
│                                                              │
│          Already a namespace holder? → Sign in              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Mark: Minimalist key or lattice icon, centered, 64px
- Headline: "Your identity. Your network. Your kingdom." — 32px, bold (Inter 700), dark
- Subhead: "The sovereign web starts with a git repo and a set of keys." — 18px, muted secondary color
- Primary CTA: "Claim Your Namespace" — violet (`--color-accent`), full padding, 44px+ touch target
- Secondary CTA: "Meet Alice" — outline variant, `--color-accent` border and text
- Sign-in link: Muted, secondary color, inline

**Responsive:** Single column on mobile. CTAs stack vertically on mobile (full-width each).

---

### 2. TWO PATHS (Visual & Narrative)

**Purpose:** Clarify entry points. Developer (AI/entity) and researcher (collaboration) paths are equally valid.

```
┌──────────────────────────────────────────────────────────────┐
│                      TWO WAYS IN                             │
│                                                              │
│  ╔═══════════════════════╦═══════════════════════╗          │
│  ║    AI & Entities      ║  Sovereign Collab     ║          │
│  ║                       ║                       ║          │
│  ║ Build multi-agent     ║ Research & annotate   ║          │
│  ║ systems with real     ║ the web with your     ║          │
│  ║ identity & governance ║ team. No platform.    ║          │
│  ║                       ║                       ║          │
│  ║ → Start with Juno     ║ → Install extension   ║          │
│  ║   (daemon setup)      ║   (zero friction)     ║          │
│  ║                       ║                       ║          │
│  ╚═══════════════════════╩═══════════════════════╝          │
│                                                              │
│   Both paths lead to the same protocol.                      │
│   One entry. Two expressions.                               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Two-column grid, centered, max 900px width
- Cards: `--color-bg-secondary` background, `--color-border-default` border, 8px radius
- Titles: 18px bold, `--color-text-primary`
- Body: 14px, `--color-text-secondary`
- Links: Text button, `--color-accent`, underline on hover
- Mobile: Stack vertically

**Why this placement:** Immediately after hero. Visitors choose their path without friction. Not "advanced setup" — presented as equally valid.

---

### 3. THE PROTOCOL, SIMPLY

**Purpose:** How it works, in plain language. Builds confidence without jargon.

```
┌──────────────────────────────────────────────────────────────┐
│                   THE PROTOCOL, SIMPLY                       │
│                                                              │
│   A profile is an identity.                                  │
│   Every person or entity has an identity repo. Yours         │
│   belongs to you, cryptographically.                         │
│                                                              │
│   Two profiles is a channel.                                 │
│   Any two identities can connect directly. No                │
│   centralized permission system.                             │
│                                                              │
│   A daemon is a live node.                                   │
│   Run the daemon and your kingdom activates. Your            │
│   ring of trust becomes operational.                         │
│                                                              │
│   A ring is a trust network.                                 │
│   You are the center of your ring. Others are centers        │
│   of theirs. Where rings overlap, trust flows through.       │
│                                                              │
│   The adventure portal.                                      │
│   Two live nodes with daemons have a permanent              │
│   bidirectional channel. Not a session. A portal.            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Width: Constrained, max 720px, centered
- Typography: 14px body, `--color-text-primary`
- Paragraph spacing: `--space-8`
- No icons, no ctas — pure narrative
- Background: Transparent (inherit from page)

**Why this content:** Visitors need to understand what they're claiming. This section is the explanation without marketing spin.

---

### 4. LIVE NAMESPACE SHOWCASE

**Purpose:** Social proof. Show real nodes in the network. "Others are already here."

```
┌──────────────────────────────────────────────────────────────┐
│                    LIVE NAMESPACES                           │
│                 The network is real.                         │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ [AVATAR]   │  │ [AVATAR]   │  │ [AVATAR]   │             │
│  │  alice     │  │  juno      │  │  vulcan    │             │
│  │ .koa.io    │  │ .koa.io    │  │ .koa.io    │             │
│  │ ●          │  │ ●          │  │ ●          │             │
│  │ 2m ago     │  │ 5m ago     │  │ now        │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ [AVATAR]   │  │ [AVATAR]   │  │ [AVATAR]   │             │
│  │ ...        │  │ ...        │  │ ...        │             │
│  │ .koa.io    │  │ .koa.io    │  │ .koa.io    │             │
│  │ ●          │  │ ●          │  │ ●          │             │
│  │ 12m ago    │  │ 28m ago    │  │ 3m ago     │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│                                                              │
│              See all 1,247 live namespaces →                │
│                                                              │
│  [Copy button on hover reveals: "View keys" - copies pk]    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Kept from v1 with minor updates to presence display
- Cards show:
  - Avatar (circular, 48px)
  - Display name (Inter 600, 14px)
  - Namespace + domain (JetBrains Mono, 12px, muted)
  - Online indicator dot (green, 8px) + timestamp ("2m ago")
  - Hover state: Border brightens, "View keys" button appears
- Grid: 3 columns (lg), 2 (md), 1 (sm)
- Data source: Live namespace API, randomized on each load
- Subhead: "The network is real." — signals this is not a demo

**Why keep this:** Proof of life. The network is operational. New visitors see immediate social proof.

---

### 5. ALICE: THE ON-RAMP

**Purpose:** Introduce the free onboarding experience. "You're not alone in this."

```
┌──────────────────────────────────────────────────────────────┐
│                        MEET ALICE                            │
│                                                              │
│   ╔═══════════════════════════════════════════════════╗     │
│   ║  [ALICE AVATAR: minimalist AI entity mark]       ║     │
│   ║                                                   ║     │
│   ║  Alice is your guide into the sovereign web.     ║     │
│   ║                                                   ║     │
│   ║  A free 12-level school. Learn by doing:         ║     │
│   ║  - Create your first namespace                   ║     │
│   ║  - Understand trust bonds & signatures           ║     │
│   ║  - Set up a daemon                              ║     │
│   ║  - Invite your first peer                        ║     │
│   ║  - Build your kingdom at your own pace           ║     │
│   ║                                                   ║     │
│   ║           [ Start with Alice ]                   ║     │
│   ║          (secondary CTA - matches hero)          ║     │
│   ║                                                   ║     │
│   ╚═══════════════════════════════════════════════════╝     │
│                                                              │
│  Or jump straight to provisioning if you know the way.      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Card: `--color-bg-secondary`, `--color-border-default` (1px), padding `--space-6`
- Alice avatar: Centered, minimalist mark, 64px
- Title: "Meet Alice" — 24px bold
- Body: 14px, muted secondary
- CTA: "Start with Alice" — secondary variant (outline, accent color)
- Background: Optional subtle accent glow (very subtle, `--color-accent-subtle`)
- Mobile: Full width, card layout

**Why now:** After protocol explanation. Visitors who want structure get Alice. Those who want autonomy skip straight to provisioning. No judgment.

**Content note:** Alice is a free 12-level journey, not a paywall. This page signals "we support you learning this."

---

### 6. TRUST & GOVERNANCE

**Purpose:** Technical credibility. Why this is different — trust bonds, signatures, git history.

```
┌──────────────────────────────────────────────────────────────┐
│              TRUST & GOVERNANCE, NOT PLATFORMS               │
│                                                              │
│  Cryptographic Sovereignty       Auditable Authority         │
│  Your keys, your identity.       Every decision committed    │
│  No password reset.              to disk & signed. Full      │
│  No recovery email.              git history of governance.  │
│                                                              │
│  Trust Bonds on Disk             Decentralized Network       │
│  Relationships are files.        No single authority.        │
│  GPG-signed. Portable.           Web of trust, not vendor.   │
│  You know who you trust.         Rings overlap. No center.   │
│                                                              │
│  Self-Hosted Option              Open Protocol              │
│  Run your daemon locally.         Anyone can build on        │
│  Or use the starter daemon.       this standard.             │
│  You choose.                      No lock-in.               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Layout: 3-column grid (lg), 2 (md), 1 (sm)
- Each item: Heading bold (16px), description (14px muted)
- No icons — text-forward per design system
- No CTAs here — technical positioning only

**Why this section:** Builds developer trust. The claims are specific and auditable. Developers nod "yes, this is different."

---

### 7. FOOTER CTA

**Purpose:** Convert the ready. Final push.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│         Ready to claim your identity and your ring?         │
│                                                              │
│              [ Claim Your Namespace ]                        │
│                                                              │
│              View on GitHub →    Docs →    Blog →           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Background: `--color-bg-secondary` (card styling to distinguish)
- Center-aligned, max 600px width
- Padding: `--space-12` top/bottom
- Primary CTA: Same as hero
- Secondary links: Muted, inline

---

### 8. FOOTER

**Purpose:** Navigation, legal, trust signals.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  kingofalldata.com           GitHub   Docs    Blog          │
│                                                              │
│  © 2026 koad:io              Privacy  Terms   Contact       │
│                                                              │
│  [key icon] Your keys never leave your device.              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Three columns: Brand (left), primary links (center), secondary links (right)
- Trust signal: Key icon + message reinforces sovereignty
- Font: 12px, muted secondary
- Mobile: Stack vertically, center-align

---

## Key Design Decisions

**1. Two paths, equal prominence**
- Old: Namespace provisioning was the sole CTA
- New: "Claim your namespace" AND "Meet Alice" are presented as equally valid
- Why: Personas 4 (researchers) enter through Alice/Dark Passenger, not direct provisioning
- Rationale: Iris's two-entry strategy requires homepage to signal both paths

**2. Alice as a primary CTA (secondary variant)**
- Old: No Alice mention on homepage
- New: Dedicated Alice section + secondary CTA in hero
- Why: Alice is the onboarding vehicle. Free tier. Guides users through sovereignty
- Design note: "Meet Alice" uses secondary CTA style (outline, accent color) to avoid overload but make it visible

**3. Dark Passenger not featured on MVP**
- Old: N/A
- New: Dark Passenger is noted in the "Two paths" section but not a primary CTA
- Why: It's a phase 2 feature. Extension-based collaboration is powerful but requires daemon already running
- Constraint: Don't promise power-user features the MVP can't deliver

**4. Live namespace showcase retained**
- Old: Social proof via 6-card grid of live namespaces
- New: Same pattern, now with "The network is real" subhead to reinforce that this is operational
- Why: Proof of life is the strongest signal koad:io can give

**5. Protocol explanation moved higher**
- Old: "How it works" was step-by-step technical detail
- New: "The Protocol, Simply" is narrative explanation (profile → channel → daemon → ring → portal)
- Why: Visitors need conceptual clarity before deciding whether to claim a namespace
- Difference: Not "how do I use this" but "what is this fundamentally"

**6. No vendor positioning**
- Old: "Provision Your Namespace" focused on namespace provisioning
- New: Reframed as "Claim Your Namespace" — emphasizes sovereignty, not service feature
- Copy: "Your kingdom" language (Iris) replaces "your namespace" language
- Why: Ownership > feature acquisition

---

## Page Flow (Full Journey)

```
Visitor arrives at kingofalldata.com
    ↓
Hero: "Your identity. Your network. Your kingdom."
    ↓
Two paths clarified: AI/entities or collaboration
    ↓
Protocol explanation: How it works conceptually
    ↓
Live namespace showcase: Others are doing this already
    ↓
Alice intro: Want a guide? Free 12-level school
    ↓
Trust & governance: Why this is technically different
    ↓
Final CTA: "Claim Your Namespace"
    ↓
Footer: Navigation, legal, trust signal
```

---

## Responsive Considerations

- Hero CTAs stack vertically on mobile (full-width each)
- Two paths cards stack vertically on sm (single column)
- Namespace showcase: 1 column (xs), 2 columns (sm), 3 columns (md+)
- Grid items (trust & governance): 1 column (sm), 2 (md), 3 (lg)
- All text readable on 320px width (minimum touch target 44×44px)

---

## Implementation Notes for Vulcan

- Reuse namespace showcase component from v1 (no changes to data fetching or card logic)
- Alice section: Image/mark asset needed from Iris brand if available
- Two paths cards: Use existing card component + BEM modifier classes
- Primary CTA destinations: "Claim Your Namespace" → `/provision` (GitHub OAuth flow)
- Secondary CTA destinations: "Meet Alice" → `/alice/start` or similar journey entry
- Trust signal in footer: Verify key icon asset matches design system
- Dark mode: Test all sections on both dark and light themes

---

## Anti-Patterns Applied

- ❌ No carousel or hero slider
- ❌ No stock photography
- ❌ No "Try for free for 14 days" countdown
- ❌ No platform branding on sovereign sections (Alice is koad-branded because it's onboarding)
- ❌ No vendor lock-in language ("managed by us")
- ❌ No power-user features (Dark Passenger) on MVP landing

---

*Wireframe by Muse — revised for sovereign web portal positioning. Ready for Vulcan integration.*
