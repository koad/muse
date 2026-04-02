# Wireframe: kingofalldata.com Home Page

**Project:** Sovereign Identity Platform Landing
**Author:** Muse (UI Beauty Entity)
**Date:** 2026-04-02
**Status:** Wireframe

---

## Design Philosophy

The home page is a **root pitch page** — it converts curious developers into cloners (namespace progenitors). It must communicate sovereignty, cryptographic elegance, and developer-first values. Zero marketing fluff. The system speaks for itself.

**Mood:** "This is what digital identity should have been."
**CTA goal:** "Clone my namespace" or "Provision mine"

---

## Section Order & Structure

### 1. HERO (Above the fold)

**Purpose:** Instant comprehension. Who is this? What do I do here?

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│         [SVG mark: minimalist key/lattice icon]         │
│                                                         │
│              kingofalldata.com                          │
│                                                         │
│    Your name. Your keys. Your sovereign identity.       │
│                                                         │
│         [ Provision Your Namespace ]  (primary CTA)     │
│                                                         │
│    Already a namespace holder? → Sign in               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Logo mark:** Small SVG key or identity-lattice icon, centered
- **Headline:** Single line, bold, identity-forward
- **Subheadline:** One line that explains the value prop without jargon
- **Primary CTA:** "Provision Your Namespace" — violet accent, full border-radius
- **Secondary link:** "Already a namespace holder? Sign in" — muted, inline

**Responsive:** Single column. CTA full-width on mobile.

---

### 2. THE PROBLEM (Optional brief strip)

**Purpose:** Pain acknowledgment. Developers nod "yes, I've felt this."

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Username-password auth is a hostage situation.        │
│  Social login is digital indentured servitude.          │
│  You deserve better.                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Width:** Constrained (max 720px), centered
- **Typography:** Serif or styled sans for gravitas, not monospace
- **No CTA here.** Pure resonance.

---

### 3. NAMESPACE SHOWCASE

**Purpose:** Social proof. Show real people, real namespaces. "Others like you are already here."

```
┌─────────────────────────────────────────────────────────┐
│                      LIVE NAMESPACES                     │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  [A]     │  │  [B]     │  │  [C]     │              │
│  │  alice   │  │  vulcan  │  │  juno    │              │
│  │  .koa.io │  │  .koa.io │  │  .koa.io │              │
│  │  [keys]  │  │  [keys]  │  │  [keys]  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  [D]     │  │  [E]     │  │  [F]     │              │
│  │  ...     │  │  ...     │  │  ...     │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│                                                         │
│           See all 1,247 namespaces →                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Card design:** 
  - Avatar (circular, 48px)
  - Display name (Inter 600)
  - Username + domain (JetBrains Mono, muted)
  - Online indicator dot (green, 8px)
  - "View keys" link (text button, copies public key on click)
- **Grid:** 3 columns desktop, 2 tablet, 1 mobile
- **Live data:** Real namespaces with presence. Randomized on load for freshness.
- **Social proof count:** "See all X namespaces →" link

---

### 4. HOW IT WORKS

**Purpose:** Developer comprehension. Three steps, clear as code.

```
┌─────────────────────────────────────────────────────────┐
│                      HOW IT WORKS                        │
│                                                         │
│   01                        02                        03 │
│   Generate Keys            Provision Namespace         Verify Trust  │
│                                                         │
│   [key icon]               [terminal icon]             [chain icon]  │
│                                                         │
│   Create your Ed25519      Claim your namespace.       Prove identity  │
│   keypair. Private key      Yourname.kingofalldata.com  by signing with  │
│   never leaves your        is yours forever.           your keys.        │
│   device.                                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Layout:** Three columns, numbered steps
- **Icons:** Line-art SVGs, monoline style, 24px
- **Typography:** Step numbers in accent color, step titles in bold, descriptions in muted
- **No CTA here.** Educational only.

---

### 5. FEATURES GRID

**Purpose:** Technical depth. Developer trust. List what matters.

```
┌─────────────────────────────────────────────────────────┐
│                      BUILT DIFFERENT                     │
│                                                         │
│  Cryptographic Sovereignty    Decentralized Trust       │
│  Your keys, your identity.    No central authority.     │
│  No password reset.           Web of trust model.       │
│                                                         │
│  Zero-Cost Identity           Open Protocol             │
│  Free forever for devs.       Anyone can build on       │
│  No VC backing required.      the namespace standard.   │
│                                                         │
│  Self-Hosted Option           Portable Presence         │
│  Run your own emitter.        Your identity follows     │
│  No vendor lock-in.           you across platforms.     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Layout:** 2x2 grid, alternating alignment (left/right on desktop)
- **Typography:** Feature title bold, description muted
- **No icons** — text-forward per anti-patterns
- **No CTA here.** Technical credibility only.

---

### 6. DEVELOPER CTA

**Purpose:** Convert. Final push for the ready developer.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│              Ready to claim your identity?             │
│                                                         │
│         [ Provision Your Namespace ]                   │
│                                                         │
│         View on GitHub →                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Background:** `--bg-secondary` (card) to distinguish from page
- **Center-aligned, constrained width**
- **Secondary link:** "View on GitHub" — for skeptics who want to inspect first

---

### 7. FOOTER

**Purpose:** Navigation, legal, trust signals.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  kingofalldata.com          GitHub    Docs    Blog     │
│                                                         │
│  © 2026 koad:io              Privacy   Terms   Contact │
│                                                         │
│  [key icon] Keys never leave your device.              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Columns:** Brand (left), Links (center), Legal (right)
- **Trust signal:** Small key icon + "Keys never leave your device."
- **Minimalist** — don't distract from conversion

---

## Namespace Showcase — Detail

The showcase is the emotional center of the page. Here's how it works:

### Data Source
- Query live namespace API: `GET /namespaces?featured=true&limit=6`
- Filter for namespaces with recent presence (emitter heartbeat < 5 min)
- Fallback to curated list if API unavailable

### Card Interaction
- **Hover:** Subtle lift (transform: translateY(-2px)), border brightens
- **Click avatar/name:** Navigate to `/~{username}` namespace page
- **Click "View keys":** Copy public key to clipboard, show "Copied!" toast, 1.5s fade

### Randomization
- On page load, fetch 12 namespaces, randomly select 6 for display
- Shuffle order each visit to prevent bias
- Ensures no "featured slots" feel — organic discovery

### Empty/Error States
- If < 6 namespaces exist: show all available with "Join them →" CTA
- If API fails: show skeleton cards (3) with "Loading namespaces..." — do not hardcode

---

## Primary CTA Specification

**Label:** "Provision Your Namespace"
**Style:** 
- Background: `--accent` (violet)
- Text: white, Inter 600
- Padding: 14px 32px
- Border-radius: 8px
- Hover: brightness(1.1), subtle shadow

**Destination:** `/provision` (or GitHub OAuth flow)

**Microcopy rationale:** "Provision" > "Create" — reinforces technical/systems language that resonates with developers.

---

## Page Flow Summary

```
Visitor arrives
    ↓
Hero: "Your name. Your keys. Your sovereign identity."
    ↓
Problem strip: Nods along
    ↓
Namespace showcase: "Others are already here"
    ↓
How it works: "I understand how"
    ↓
Features: "This is technically sound"
    ↓
CTA: "Provision Your Namespace" ← CONVERSION
    ↓
Footer: Trust signals, navigation
```

---

## Anti-Patterns Applied

- ❌ No carousel or hero slider
- ❌ No stock photography
- ❌ No "Our investors" section
- ❌ No "Try for free for 14 days"
- ❌ No platform logo on user namespace pages
- ❌ No decorative gradients on user-facing sections

---

*Wireframe by Muse — ready for Vulcan's functional implementation.*
