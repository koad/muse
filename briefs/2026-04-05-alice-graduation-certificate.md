# Alice Graduation Certificate — Design Spec

**Status:** Complete  
**Date:** 2026-04-05  
**Audience:** Vulcan (PWA integration), Alice (signing implementation), Juno (approval)  
**Entity:** Muse  
**References:** alice-ui-design-brief.md (Screen 4), Chiron DECISIONS.md, koad/vulcan#36

---

## Overview

The graduation certificate is the culmination of the alice-onboarding curriculum. When a learner completes all 13 levels (Level 0 through Level 12), Alice writes `certificate.md` to disk, signs it with her Ed25519 key, and the PWA enters the graduation screen. This document specifies the full design system for that moment: the PWA graduation screen, the verify flow, the shareable card, and the printable artifact.

This spec extends Screen 4 from the Alice UI Design Brief with precise layout, interaction, and format specifications.

---

## Design Principles (Certificate-Specific)

Carry all principles from the Alice UI Design Brief forward. These additions apply to the certificate in particular:

- **The signature is the soul.** Alice's Ed25519 signature is not decorative — it is the core fact. The design honors it. It is visible, readable, and explainable, not buried in a modal or reduced to a checkmark.
- **Sovereign by default.** The certificate lives on disk first, on a screen second. The `.md` file is the canonical artifact. The PWA renders it; it does not produce it.
- **Verifiable by a stranger.** Anyone who receives a shared certificate image or link should be able to independently confirm Alice's signature. The design carries the full verification path without requiring trust in any third party.
- **The human's name, front and center.** The display name the learner chose is the hero element. This is their moment.

---

## Section 1: PWA Graduation Screen

### 1a. The Arrival Moment

Before the certificate is shown, Alice speaks. This is the transition beat — the human should feel something before the certificate appears.

```
┌──────────────────────────────────────────┐
│                                          │
│              ✦                           │ ← Single amber glyph, centered
│                                          │   Fade in over 800ms. No animation loop.
│  Alice                                   │
│  ──────────────────────────────────────│
│                                          │
│  "You did it.                            │
│                                          │
│   You moved from curious to sovereign.  │
│   You didn't just learn about your      │
│   keys — you held them. You didn't      │
│   just read about trust — you built     │
│   bonds.                                 │
│                                          │
│   You understand what it means to own   │
│   your world.                            │
│                                          │
│   I'm signing your certificate now.     │
│   This is real. This is forever."        │
│                                          │
│  ──────────────────────────────────────│
│                                          │
│  [Signing animation — 1.5s]              │ ← Amber pulse on Alice's name glyph.
│  Certificate ready ✦                     │   Then resolves: "Certificate ready ✦"
│                                          │
│                      ┌────────────────┐  │
│                      │ See my cert ✦  │  │ ← Gold button, appears after signing anim
│                      └────────────────┘  │
│                                          │
└──────────────────────────────────────────┘
```

**Signing animation detail:**
- Duration: ~1.5 seconds total.
- Alice's `✦` glyph pulses amber (opacity 0.5 → 1.0 → 0.5 → 1.0), 3 beats.
- Below: a single line of muted text cycles: "Signing..." → "Certificate ready ✦"
- No progress bar. No spinner. The pulse conveys something happening — not a loading state.
- The button appears on completion, not before.

---

### 1b. The Certificate Display

After tapping "See my cert", the certificate is revealed in full. It scrolls vertically on mobile.

```
┌──────────────────────────────────────────┐
│                                          │
│  ┌──────────────────────────────────┐    │
│  │                                  │    │ ← Certificate frame
│  │  ✦  ALICE SOVEREIGNTY MASTERY  ✦ │    │   Amber top/bottom borders (2px)
│  │     ─────────────────────────   │    │   Dark background (#0a0a0a)
│  │                                  │    │   Subtle inner padding (24px)
│  │  This certifies that             │    │
│  │                                  │    │
│  │         Jordan                   │    │ ← Display name: 28-32px, warm white
│  │         ────────────────────     │    │   Underlined in amber. This is the hero.
│  │                                  │    │
│  │  has completed the               │    │
│  │  alice-onboarding curriculum     │    │
│  │  and demonstrated mastery of     │    │
│  │  koad:io sovereignty principles. │    │
│  │                                  │    │
│  │  ─────────────────────────────   │    │
│  │                                  │    │
│  │  Completed     April 5, 2026     │    │ ← 14px, muted (#f0ede5 at 70% opacity)
│  │  Learner ID    a9f3c2e1-7b4d-…  │    │   Truncated UUID, tap to expand
│  │  Signed by     Alice             │    │
│  │                                  │    │
│  │  Signature (Ed25519):            │    │ ← 12px label, alice-subtle color
│  │  ┌────────────────────────────┐  │    │
│  │  │ U1NIU0lHAAAAAQAAADMAAAALc… │  │    │ ← Space Mono 11px, truncated at ~32 chars
│  │  │ ──  tap to expand  ──      │  │    │   Monospace, amber on dark bg
│  │  └────────────────────────────┘  │    │
│  │                                  │    │
│  │  Verify: canon.koad.sh/alice     │    │ ← Small amber link, 12px
│  │                                  │    │
│  │  ✦  ─────────────────────────  ✦ │    │ ← Footer rule with glyphs
│  │                                  │    │
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Share certificate               │    │ ← Gold button, full width
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Verify signature                │    │ ← Secondary button, outlined amber
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Download certificate            │    │ ← Tertiary, text link style
│  └──────────────────────────────────┘    │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  "Your sovereignty begins here.          │
│   Let me introduce you to the rest       │
│   of your team."                         │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Meet Juno ✦                     │    │ ← Gold button — forward momentum
│  └──────────────────────────────────┘    │
│                                          │
└──────────────────────────────────────────┘
```

**Typography on the certificate frame:**

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Header: "ALICE SOVEREIGNTY MASTERY" | 13px, all-caps, letter-spacing 0.15em | Medium | `#F4B844` (amber) |
| Display name | 28-32px | Regular | `#f0ede5` |
| Body copy ("has completed...") | 16px | Regular | `#f0ede5` at 85% opacity |
| Labels (Completed, Learner ID, etc.) | 12px | Regular | `#555555` (alice-subtle) |
| Values (date, UUID, etc.) | 12px | Medium | `#f0ede5` at 70% opacity |
| Signature block | 11px, Space Mono | Regular | `#F4B844` at 80% opacity |
| Verify link | 12px | Regular | `#F4B844` |

**Certificate frame border:**
- Top: 2px solid `#F4B844`
- Bottom: 2px solid `#F4B844`
- Left/Right: 1px solid `#2a2a2a`
- Border-radius: 4px
- Background: `#0a0a0a`
- Inner padding: 24px on desktop, 20px on mobile

**UUID display:**
- Truncated to first segment: `a9f3c2e1-7b4d-…`
- Tap/click to expand full UUID inline
- Full UUID is selectable text (for manual verification)

**Signature block:**
- Shows first ~32 characters of the base64 payload
- Tap "tap to expand" reveals the full `-----BEGIN SSH SIGNATURE-----` block in a scrollable mono panel
- Full block is selectable/copyable

---

## Section 2: The Verify Flow

Tapping "Verify signature" opens a bottom sheet (mobile) or inline expansion panel (desktop).

### 2a. Verify Panel

```
┌──────────────────────────────────────────┐
│  Verify Alice's signature                │ ← Panel title, 16px
│  ──────────────────────────────────────  │
│                                          │
│  This certificate was signed by Alice    │
│  using her Ed25519 key. You can verify   │
│  this yourself — no trust required.      │
│                                          │
│  ── What was signed ──────────────────   │ ← Section label, alice-subtle
│                                          │
│  Alice signed a canonical string         │
│  containing:                             │
│                                          │
│   • Your display name: Jordan            │
│   • Your learner ID: a9f3c2e1-7b4d-…    │
│   • Completion date: 2026-04-05          │
│   • Curriculum: alice-onboarding         │
│                                          │
│  ── Alice's public key ───────────────   │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ ssh-ed25519 AAAAC3NzaC1lZDI1NT…   │  │ ← Mono, copyable, truncated
│  │           [Copy key] [View full]   │  │
│  └────────────────────────────────────┘  │
│                                          │
│  Full public key: canon.koad.sh/alice    │ ← Amber link                                          │
│                                          │
│  ── Verify locally (3 steps) ─────────   │
│                                          │
│  1.  Save the certificate file:          │
│      certificate.md                      │
│      [Download file]                     │
│                                          │
│  2.  Save Alice's public key:            │
│      alice.pub                           │
│      [Download key]                      │
│                                          │
│  3.  Run in your terminal:               │
│  ┌────────────────────────────────────┐  │
│  │ ssh-keygen -Y verify \             │  │ ← Copyable code block
│  │   -f alice.pub \                   │  │   Space Mono 12px
│  │   -I alice@kingofalldata.com \     │  │   Amber on dark
│  │   -n file \                        │  │
│  │   -s certificate.md.sig \          │  │
│  │   < certificate.md                 │  │
│  └────────────────────────────────────┘  │
│  [Copy command]                          │
│                                          │
│  ── Or check online ───────────────────   │
│                                          │
│  canon.koad.sh/verify?cert=a9f3c2e1…    │ ← Amber link
│                                          │
│  Paste your certificate and Alice's      │
│  public key to verify without a          │
│  terminal.                               │
│                                          │
│                      ┌────────────────┐  │
│                      │    Done ✦      │  │ ← Closes panel
│                      └────────────────┘  │
└──────────────────────────────────────────┘
```

### 2b. Verify Flow Logic

The verify flow has three paths, offered in order of independence:

1. **Local terminal verification (preferred).** Three-step instructions with downloadable files and a copyable `ssh-keygen -Y verify` command. No server involved. The learner can do this on any machine.

2. **Online verification endpoint.** `canon.koad.sh/verify` accepts the certificate content and Alice's public key and returns a verification result. This is a convenience, not a trust requirement — the endpoint is open-source and replaceable.

3. **Alice's public key at `canon.koad.sh/alice`.** The canonical location for Alice's current ed25519 public key. A learner who receives a certificate from someone else can fetch this key and verify locally without ever touching the PWA.

**What the verify panel does NOT do:**
- It does not auto-verify in the background and show "Verified ✓" as a fait accompli. The human should verify, not be told the system verified.
- It does not require login, cookies, or account creation.
- It does not send the certificate or signature data to any analytics endpoint.

---

## Section 3: Shareable Card

### 3a. Card Anatomy

The shareable card is a fixed-size image (1200×630px for Open Graph / social share, square 1080×1080px as alternate). Generated client-side via canvas or server-side on demand.

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ✦  ─────────────────────────────────────────────────────────────  ✦│ ← Amber rule
│                                                                      │
│                                                                      │
│                       ALICE SOVEREIGNTY MASTERY                     │ ← 18px caps, amber
│                                                                      │
│                                                                      │
│                             Jordan                                   │ ← 52px, warm white
│                         ─────────────────                            │ ← Amber underline
│                                                                      │
│            has demonstrated mastery of koad:io sovereignty.         │ ← 18px, muted
│                                                                      │
│                                                                      │
│  ─────────────────────────────────────────────────────────────────   │
│                                                                      │
│  Completed April 5, 2026                                             │ ← 14px left
│  Signed by Alice · Ed25519                                           │ ← 14px left
│  Verify: canon.koad.sh/alice                                         │ ← 14px left, amber
│                                                                      │
│  ✦  ─────────────────────────────────────────────────────────────  ✦│ ← Amber rule
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**Card colors (same system):**
- Background: `#0a0a0a`
- Text: `#f0ede5`
- Accent/rules: `#F4B844`
- Muted text: `#555555`

**Card dimensions:**
- OG/social: 1200×630px
- Square: 1080×1080px
- Print (A4-equivalent): 2480×1754px (300dpi)

**Card does NOT show:**
- The learner's UUID (too long, not social-friendly)
- The raw signature (not shareable-friendly)
- Any branding beyond "Alice — kingofalldata.com"
- A QR code pointing to the verify URL (optional extension, not in v1)

**Card does show:**
- Display name (large, hero)
- Completion date
- "Signed by Alice · Ed25519" (establishes authenticity without clutter)
- Verify URL (short, memorable: `canon.koad.sh/alice`)

### 3b. Insiders Section Profile Integration

For learners who have an Insiders section account, the certificate card appears in their profile. See `2026-04-03-insiders-section.md` for the full Insiders spec.

In the Insiders profile context, the certificate is displayed as a pinned card in the learner's profile row:

```
┌──────────────────────────────────────────┐
│  Jordan                                  │
│  Sovereign since April 2026              │ ← Derived from completedDate
│                                          │
│  ┌──────────────────────────────────┐    │
│  │ ✦ Alice Mastery                  │    │ ← Certificate badge, compact
│  │   april-onboarding complete      │    │
│  │   April 5, 2026 · Verified ✦     │    │
│  └──────────────────────────────────┘    │
│                                          │
│  [View full certificate]                 │ ← Amber link, opens graduation screen
│                                          │
└──────────────────────────────────────────┘
```

### 3c. Share Sheet Flow

Tapping "Share certificate" opens a share sheet:

```
┌──────────────────────────────────────────┐
│  Share your certificate                  │
│  ──────────────────────────────────────  │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  [Certificate card preview]      │    │ ← 240px tall preview
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Copy link                       │    │ ← Copies canon.koad.sh/cert/{uuid}
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Save image                      │    │ ← Downloads card PNG
│  └──────────────────────────────────┘    │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Share via OS share sheet…       │    │ ← Native share API, passes image
│  └──────────────────────────────────┘    │
│                                          │
│  [ Cancel ]                              │
│                                          │
└──────────────────────────────────────────┘
```

**Shareable link structure:** `canon.koad.sh/cert/{uuid}`

That URL renders the certificate card as a web page with full Open Graph metadata (title, description, image). The page shows:
- The certificate card (rendered from the certificate data served by canon.koad.sh)
- A "Verify this certificate" link
- A "Start learning" CTA pointing back to alice on kingofalldata.com

The UUID in the URL is the public-facing stable ID. The display name and completion date are fetched from Alice's learner record at `canon.koad.sh`. Alice syncs completed certificates to canon.koad.sh as part of the signing flow.

---

## Section 4: Printable / Downloadable Certificate

### 4a. Design

The downloadable certificate is a standalone artifact: a PDF or high-resolution PNG, A4 landscape orientation (297×210mm at 300dpi = 3508×2480px).

```
┌────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                    │
│  ────────────────────────────────────────────────────────────────────────────────  │ ← 3px amber rule
│                                                                                    │
│                                                                                    │
│     ✦  ALICE SOVEREIGNTY MASTERY  ✦                                                │ ← 22px caps, centered, amber
│                                                                                    │
│                                                                                    │
│                        This certifies that                                         │ ← 16px, muted, italic
│                                                                                    │
│                                                                                    │
│                              Jordan                                                │ ← 64px, warm white, centered
│                        ──────────────────────                                      │ ← 200px amber underline
│                                                                                    │
│                                                                                    │
│        has completed the alice-onboarding curriculum and demonstrated              │ ← 18px centered
│         mastery of the principles of sovereignty in the koad:io ecosystem.        │
│                                                                                    │
│                                                                                    │
│  ────────────────────────────────────────────────────────────────────────────────  │ ← 1px rule
│                                                                                    │
│                                                                                    │
│  Completed: April 5, 2026           Learner ID: a9f3c2e1-7b4d-4c6a-b8d2-…         │ ← 12px, two columns
│  Signed by: Alice                   Verify: canon.koad.sh/alice                   │
│                                                                                    │
│                                                                                    │
│  Signature (Ed25519):                                                              │ ← 10px label
│  -----BEGIN SSH SIGNATURE-----                                                     │ ← 9px Space Mono
│  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAg...                                  │
│  -----END SSH SIGNATURE-----                                                       │
│                                                                                    │
│                                                                                    │
│  ────────────────────────────────────────────────────────────────────────────────  │ ← 3px amber rule
│                                                                                    │
│     ✦                              kingofalldata.com                          ✦    │ ← Footer, 11px muted
│                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────┘
```

**Print design notes:**
- Background: `#0a0a0a` (dark print — intentional, this is a digital-native artifact, not a traditional paper certificate)
- If the learner wants a "light" version for physical print, a `prefers-color-scheme: light` variant uses `#fafaf7` background with `#1a1a1a` text and `#b8890e` amber. Offered as a toggle on the download screen: "Dark (digital) / Light (print)".
- Font: system sans-serif for body; Space Mono for the signature block.
- The full Ed25519 signature block IS shown on the printable artifact. The whole point of printing it is that it's a complete, standalone verifiable record.
- Learner ID is shown in full on the printable artifact (not truncated — there's space, and this is a document).

### 4b. Download Flow

Tapping "Download certificate" opens a minimal options panel:

```
┌──────────────────────────────────────────┐
│  Download your certificate               │
│  ──────────────────────────────────────  │
│                                          │
│  Format                                  │
│  ○ PDF (recommended)                     │
│  ○ PNG (high-resolution image)           │
│  ○ Markdown (raw certificate file)       │
│                                          │
│  Style                                   │
│  ● Dark (digital)                        │
│  ○ Light (print-friendly)                │
│                                          │
│                      ┌────────────────┐  │
│                      │  Download ✦    │  │
│                      └────────────────┘  │
└──────────────────────────────────────────┘
```

**The Markdown option** downloads the raw `certificate.md` file as written by Alice. This is the canonical artifact. It contains:
- `humanName`: display_name
- `completedDate`: ISO-8601
- `aliceSignature`: the Ed25519 signature block
- `verificationUrl`: canon.koad.sh/alice

The PDF and PNG formats are rendered from this source of truth.

---

## Section 5: The `certificate.md` File Structure

This section is for Alice's reference when writing the file. The design renders from this structure.

```markdown
---
humanName: Jordan
completedDate: 2026-04-05T14:32:00Z
curriculum: alice-onboarding
levelsCompleted: 13
learnerId: a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a
aliceSignature: |
  -----BEGIN SSH SIGNATURE-----
  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAg[...]
  -----END SSH SIGNATURE-----
verificationUrl: https://canon.koad.sh/alice
issuedBy: Alice
issuedAt: 2026-04-05T14:32:01Z
---

# Certificate of Mastery

This certifies that **Jordan** has completed the alice-onboarding curriculum
and demonstrated mastery of koad:io sovereignty principles.

**Completed:** 2026-04-05  
**Learner ID:** a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a  
**Signed by:** Alice  
**Verify:** https://canon.koad.sh/alice
```

The signature is over the canonical string:
```
alice-onboarding:Jordan:a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a:2026-04-05T14:32:00Z
```
i.e., `{curriculum}:{humanName}:{learnerId}:{completedDate}`. This is what Alice signs, and what the verify flow instructs the learner to reconstruct.

---

## Section 6: Component Summary for Vulcan

### New components required

```
<AliceGraduation>
  ├── <GraduationArrival />           // Alice's speech + signing animation
  ├── <CertificateDisplay />          // The framed certificate
  │     ├── <CertificateFrame />      // Visual container with amber borders
  │     ├── <LearnerName />           // Hero display name
  │     ├── <CertificateMeta />       // Date, UUID (truncated), signed-by
  │     └── <SignatureBlock />        // Truncated sig + expand-on-tap
  ├── <VerifyPanel />                 // Bottom sheet / inline
  │     ├── <WhatWasSigned />
  │     ├── <AlicePublicKey />        // Copyable key, link to canon
  │     └── <VerifyInstructions />    // 3-step local + online path
  ├── <ShareSheet />                  // Copy link, save image, OS share
  ├── <DownloadOptions />             // PDF/PNG/Markdown + Dark/Light
  └── <MeetJuno />                    // Forward CTA after graduation
```

### State reads (Vulcan reads, Alice writes)

All from `~/.alice/learners/{uuid}/curricula/alice-onboarding/certificate.md`:

| Field | Use |
|-------|-----|
| `humanName` | Hero display on certificate and card |
| `completedDate` | Shown on certificate, card, profile badge |
| `aliceSignature` | Shown in SignatureBlock, used in verify instructions |
| `verificationUrl` | Shown as link on certificate, card, in verify panel |
| `learnerId` | Shown truncated on screen, full in download and verify panel |

Vulcan does not call any signing API. The certificate file exists on disk, written and signed by Alice. Vulcan renders it.

---

## Animations and Motion

| Moment | Motion |
|--------|--------|
| Arrival (signing) | Alice glyph ✦ pulses amber, 3 beats, 1.5s total |
| Certificate reveal | Fade-in over 400ms, slight scale 0.97→1.0 (feels like it's being placed) |
| Share sheet open | Slide up from bottom (mobile), fade in (desktop) |
| Verify panel open | Same as share sheet |
| UUID expand (tap) | Inline expand, smooth height animation (~200ms) |
| Sig block expand | Same |

**Respect `prefers-reduced-motion`:** If set, all animations collapse to instant state changes. No motion is required for function.

---

## Accessibility

- Certificate frame uses `role="region"` with `aria-label="Certificate of Mastery"`.
- Display name has sufficient contrast against dark background (WCAG AA, 4.5:1 minimum).
- Amber accent (#F4B844) on dark (#0a0a0a): contrast ratio ~8.2:1 — passes AAA.
- Signature block is marked as `aria-label="Ed25519 signature, expandable"`.
- All buttons have clear focus states (amber ring, 2px offset).
- Download format radio buttons are keyboard-navigable.
- The "signing animation" is decorative — `aria-hidden="true"` on the animation element. The status text ("Certificate ready ✦") is in a live region (`aria-live="polite"`).

---

**Design Direction:** Muse  
**Date:** 2026-04-05  
**Status:** Ready for Vulcan implementation
