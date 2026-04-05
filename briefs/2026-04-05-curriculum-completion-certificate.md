# Curriculum Completion Certificate — Design Spec

**Status:** Complete
**Date:** 2026-04-05
**Audience:** Vulcan (implementation), Alice (signing), Chiron (curriculum format), Juno (approval)
**Entity:** Muse
**References:** 2026-04-05-alice-graduation-certificate.md, 2026-04-05-chiron-curriculum-browser.md, koad:io design system

---

## Overview

This brief specifies the completion certificate as a design system component that can serve any Chiron curriculum. The Alice graduation ceremony — the conversation with Alice, the signing animation, the arrival moment — is already fully specified in `2026-04-05-alice-graduation-certificate.md`. That document covers one specific instance: Alice's onboarding curriculum.

This document asks a different question: what is the certificate as a format, a philosophy, and a persistent artifact? It addresses:

- What "certificate" means in a sovereignty-first system and whether it is the right word
- The file format and structure for any curriculum, not just Alice's
- What machine-verifiable means in practice
- The print and display layout divorced from the Alice-specific ceremony
- How the certificate links back to the curriculum browser

Read `2026-04-05-alice-graduation-certificate.md` for the full PWA graduation screen, the signing animation, the verify panel, and the shareable card. This document does not repeat those specifications. It sets the foundations they build on.

---

## 1. Is "Certificate" the Right Word?

### The honest problem

"Certificate" carries institutional weight: a university issues it, an authority vouches for you, a third party can check the registry. The certificate's value comes from the issuer's reputation, not from the document itself.

koad:io is sovereignty-first. The entity who signs the certificate is not a university. There is no registry you call to check it. Alice is a program running on your disk. What she signs, she signs with her own Ed25519 key — a key you can read, copy, and verify against yourself. The certificate's value comes from:

1. The fact of completion (Alice assessed it)
2. The signature (Alice's key, verifiable by anyone)
3. The learner's own knowledge (the only thing that can't be faked)

A traditional certificate is a proxy for trust in an institution. This document is not that. It is a signed record that Alice created and you own.

### Alternative framings considered

| Term | Why it fails | Why it works |
|------|-------------|--------------|
| Certificate | Implies institutional authority | Familiar, understood quickly |
| Record | Accurate, but flat — no weight | |
| Badge | Gamification register | |
| Proof | Accurate, slightly adversarial | |
| Declaration | Interesting, but one-sided | |
| Compact | Too legal | |
| Attestation | Accurate — an entity attesting a fact | Strong when you know the vocabulary |

### The recommendation: "Certificate" with honest framing

Keep the word "certificate." It communicates clearly and signals that the learner has completed something real. The honest framing lives in the design details:

- The certificate header reads **"Alice's Attestation"** (not "Certificate of Completion" or "Certificate of Achievement")
- The body text says: *"Alice has attested that [Learner] completed..."* — not "certifies", which implies institutional authority
- The verification path is prominent: the certificate explicitly tells the learner how to verify it themselves, and that Alice's word is sufficient for them to check — no external registry required

The word "certificate" in the UI (`[ View your certificate ]`, "Download certificate") is acceptable shorthand. The document itself uses "attestation" — this is the more accurate word and the one that teaches the learner something true about the system.

**For v1, default header:** `Alice's Attestation`  
**For future curricula by other entities:** `{Entity}'s Attestation`  
**Long form (full certificate body):** `{Entity} attests that...`

---

## 2. What Machine-Verifiable Means in Practice

A machine-verifiable certificate is one where:

1. The signed content (a canonical string) can be reconstructed from the visible data
2. The signer's public key is available at a stable, known location
3. A standard tool (not a custom verifier) can confirm the signature

### 2a. The canonical string

Alice signs a deterministic string assembled from the certificate's key fields:

```
{curriculum}:{displayName}:{learnerId}:{completedDate}
```

Example:
```
alice-onboarding:Jordan:a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a:2026-04-05T14:32:00Z
```

This string is:
- Deterministic (same inputs always produce the same string)
- Human-readable (a person can reconstruct it from the certificate's visible fields)
- Minimal (no implementation-specific metadata that could change across versions)
- Not the full certificate text (which might have formatting variations across renderings)

The canonical string format is documented in the certificate file itself.

### 2b. Alice's key location

Alice's Ed25519 public key lives at:
```
canon.koad.sh/alice
```

This is a raw text endpoint serving the public key in OpenSSH format. It is:
- Publicly accessible without authentication
- Stable — `canon.koad.sh` is the canonical key distribution endpoint for the koad:io ecosystem
- Human-readable (anyone can curl it and read it)

The key is also embedded in Alice's entity directory at `~/.alice/id/alice.pub` for anyone who has cloned Alice's repo.

### 2c. The verification command

Using standard OpenSSH tooling (available on any modern system, no special software required):

```bash
ssh-keygen -Y verify \
  -f alice.pub \
  -I alice@kingofalldata.com \
  -n file \
  -s certificate.md.sig \
  < certificate.md
```

Or, for the canonical string approach:

```bash
echo "alice-onboarding:Jordan:a9f3c2e1-…:2026-04-05T14:32:00Z" \
  | ssh-keygen -Y verify \
      -f alice.pub \
      -I alice@kingofalldata.com \
      -n file \
      -s certificate.sig \
      -
```

Both approaches are documented in the certificate file and in the verify panel (see `2026-04-05-alice-graduation-certificate.md`, Section 2).

### 2d. What verification proves

Verification proves that:
- Alice's key signed the canonical string at a specific time
- The canonical string includes this specific learner ID, display name, curriculum, and date
- The signature has not been tampered with

Verification does not prove:
- That the learner actually learned anything (Alice assessed this; you trust Alice or you don't)
- That the display name is the learner's legal name (it is whatever name they chose)
- That the learner ID corresponds to a real person (it is a UUID the system generated)

The certificate is honest about this. It attests to what Alice knows: that a process was completed, as Alice defined completion. It does not claim to know who the learner is as a human being.

### 2e. Why Ed25519, not GPG

The trust bond system (for inter-entity authorization) uses GPG clearsigned documents. Certificates use Ed25519/SSH signing instead. The reasons:

1. **Learner accessibility.** `ssh-keygen` is preinstalled on every Mac and most Linux systems. GPG requires installation and a key ring, which is a barrier for learners who are just finishing an onboarding curriculum.
2. **Consistency with Alice's key type.** Alice's primary identity key is Ed25519 (`~/.alice/id/alice_ed25519`). The certificate is signed with the same key type. One key, one identity.
3. **Simplicity of the signed payload.** Trust bonds are prose documents with complex field structures. Certificates have a canonical string — no need for GPG's document-signing features.
4. **Verifier availability.** `ssh-keygen -Y verify` is the simplest path for a learner verifying their first cryptographic signature. Meeting them at their first step with a familiar tool is correct design.

Future Chiron curricula that teach GPG specifically may use GPG signatures for their completion certificates. The format is extensible.

---

## 3. File Format

### 3a. The canonical file: `certificate.md`

The certificate is a Markdown file with a YAML front matter block. This format is:
- Human-readable in any text editor
- Renderable as a web page without conversion
- Parseable by any YAML/Markdown library
- Diffable in git

The file lives at:
```
~/.alice/learners/{learnerId}/curricula/{curriculumId}/certificate.md
```

Full file structure:

```markdown
---
schema: koad-io-certificate/1.0
entity: alice
entityKey: https://canon.koad.sh/alice
curriculum: alice-onboarding
curriculumTitle: koad:io Human Onboarding
levelsCompleted: 13
learnerId: a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a
displayName: Jordan
completedDate: 2026-04-05T14:32:00Z
issuedAt: 2026-04-05T14:32:01Z
canonicalString: "alice-onboarding:Jordan:a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a:2026-04-05T14:32:00Z"
signature: |
  -----BEGIN SSH SIGNATURE-----
  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAg[...]
  -----END SSH SIGNATURE-----
verifyWith: |
  ssh-keygen -Y verify -f alice.pub -I alice@kingofalldata.com -n file -s certificate.sig < certificate.md
---

# Alice's Attestation

Alice attests that **Jordan** completed the alice-onboarding curriculum
and demonstrated mastery of koad:io sovereignty principles.

**Completed:** 2026-04-05
**Learner ID:** a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a
**Issued by:** Alice
**Verify:** https://canon.koad.sh/alice

---

To verify this attestation without trusting any service:

1. Save this file as `certificate.md`
2. Fetch Alice's public key: `curl https://canon.koad.sh/alice > alice.pub`
3. Reconstruct the canonical string: `alice-onboarding:Jordan:a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a:2026-04-05T14:32:00Z`
4. Verify: (see `verifyWith` in the front matter above)

The signature is over the canonical string, not the full file.
This file may be copied, printed, or shared. The signature remains valid.
```

**Why `verifyWith` is in the front matter:** A learner who opens the raw file should see the verification command immediately, without scrolling through the prose. The front matter is also machine-parseable — a future tool could read the file and auto-run verification.

**Why `canonicalString` is in the front matter:** Transparency. The learner does not need to understand the construction algorithm. They can read the canonical string, see that it matches their name and date, and use it in the verification command directly.

### 3b. The companion signature file: `certificate.md.sig`

The signature in the front matter is for the canonical string only. For learners who want to verify the full document (not just the canonical fields), a companion `certificate.md.sig` file can be downloaded. This is an optional supplement, not the primary verification path.

The companion file approach:
```
~/.alice/learners/{learnerId}/curricula/{curriculumId}/certificate.md      ← document
~/.alice/learners/{learnerId}/curricula/{curriculumId}/certificate.md.sig  ← document signature
```

In the verify panel, the instructions cover both approaches: canonical string (simpler, recommended) and full document (complete, for the thorough learner).

---

## 4. Layout and Visual Design

The certificate design is fully specified for Alice's onboarding curriculum in `2026-04-05-alice-graduation-certificate.md`. The following section establishes the generalizable template for any Chiron curriculum.

### 4a. Certificate display — generalized template

```
┌──────────────────────────────────────────────┐
│ [3px top rule in entity color]               │
│                                              │
│  [glyph]  [CURRICULUM NAME IN CAPS]  [glyph] │ ← entity color, 13px, letter-spacing 0.15em
│           ─────────────────────────          │ ← thin rule
│                                              │
│  [Entity] attests that                       │ ← 16px, muted
│                                              │
│         [Display Name]                       │ ← Hero text, 28-32px, warm white
│         ───────────────────────              │ ← Amber underline (entity color)
│                                              │
│  completed [curriculum full title]           │ ← 16px body
│  and demonstrated mastery of                 │
│  [capability statement].                     │
│                                              │
│  ─────────────────────────────────────────   │
│                                              │
│  Completed     [date]                        │ ← 12px, two rows
│  Learner ID    [uuid, truncated]             │
│  Signed by     [Entity name]                 │
│  Verify        [entity canonical key URL]    │
│                                              │
│  Signature ([key type]):                     │ ← 11px label
│  ┌──────────────────────────────────────┐   │
│  │ [truncated signature, tap to expand] │   │ ← Space Mono 11px, entity color
│  └──────────────────────────────────────┘   │
│                                              │
│  [glyph]  ─────────────────────────  [glyph] │ ← footer rule
│                                              │
└──────────────────────────────────────────────┘
```

**Variable fields by curriculum:**

| Field | Alice onboarding | Next curriculum |
|-------|-----------------|-----------------|
| `[glyph]` | `✦` | Defined per entity — Alice owns `✦` |
| `[entity color]` | `#F4B844` | Per entity color system |
| `[CURRICULUM NAME]` | `ALICE SOVEREIGNTY MASTERY` | `[ENTITY] [CURRICULUM]` |
| `[Entity]` | `Alice` | Signing entity name |
| `[capability statement]` | `koad:io sovereignty principles` | Defined in curriculum metadata |
| `[entity canonical key URL]` | `canon.koad.sh/alice` | `canon.koad.sh/{entity}` |

**Invariant elements (all curricula):**
- Display name is always the hero text (largest, most prominent)
- Learner ID is always shown (truncated on screen, full in download)
- Signature is always visible (not hidden, not an asterisk — the signature IS the certificate)
- Verification path is always present — prominently, not buried

### 4b. Typography scale

Same as `2026-04-05-alice-graduation-certificate.md`, Section 1b. Repeated here for the generalized template:

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Curriculum header | 13px, all-caps, letter-spacing 0.15em | Medium | Entity color (`#F4B844` for Alice) |
| Display name | 28–32px | Regular | `#f0ede5` |
| Body copy | 16px | Regular | `#f0ede5` at 85% opacity |
| Labels | 12px | Regular | `--color-text-muted` |
| Values | 12px | Medium | `#f0ede5` at 70% opacity |
| Signature block | 11px, Space Mono | Regular | Entity color at 80% opacity |
| Verify link | 12px | Regular | Entity color |

### 4c. Certificate frame

Generalizing from Alice's certificate:

```css
.certificate-frame {
  border-top: 2px solid var(--entity-color);
  border-bottom: 2px solid var(--entity-color);
  border-left: 1px solid var(--color-border-default);
  border-right: 1px solid var(--color-border-default);
  border-radius: 4px;
  background: #0a0a0a;
  padding: 24px;
}

@media (max-width: 600px) {
  .certificate-frame {
    padding: 20px;
  }
}
```

The entity color is applied only to the top and bottom borders — the same pattern as the entity product card's top rule. This is the visual signature of the entity system: color at the top edge marks ownership without overwhelming the content.

---

## 5. Print Layout

### 5a. Design intent

The printable certificate is A4 landscape (297×210mm). The dark-on-black screen design inverts to a `#fafaf7` background with `#1a1a1a` text for print — offered as a toggle in the download options.

The print layout must work as a standalone document: anyone receiving a printed copy should be able to:
- Read the learner's name and what they completed
- Find the signature (visible, even if not scannable from print)
- Find the verification URL without needing the digital version

The full Ed25519 signature block IS printed. On paper, it is not interactive — no "tap to expand." It prints at a small size (8–9px, Space Mono) but legibly. A learner who prints and frames their certificate has the complete, standalone verifiable artifact on paper.

### 5b. Print layout

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ─────────────────────────────────────────────────────────────────    │ ← 3px rule (amber or #b8890e for print)
│                                                                        │
│                                                                        │
│     ✦  ALICE SOVEREIGNTY MASTERY  ✦                                    │ ← 22px caps, centered
│                                                                        │
│                                                                        │
│                    Alice attests that                                   │ ← 16px, muted, italic
│                                                                        │
│                                                                        │
│                          Jordan                                         │ ← 64px, centered
│                    ────────────────────                                 │ ← 200px amber underline
│                                                                        │
│                                                                        │
│     completed the alice-onboarding curriculum and demonstrated         │ ← 18px centered
│     mastery of koad:io sovereignty principles.                         │
│                                                                        │
│                                                                        │
│  ────────────────────────────────────────────────────────────────────  │ ← 1px rule
│                                                                        │
│  Completed: 2026-04-05        Learner ID: a9f3c2e1-7b4d-4c6a-b8d2-…  │ ← 12px, two columns
│  Signed by: Alice             Verify: canon.koad.sh/alice              │
│                                                                        │
│  Canonical string:                                                      │ ← 10px label
│  alice-onboarding:Jordan:a9f3c2e1-7b4d-4c6a-b8d2-3f1e0d9c8b7a:…      │ ← 9px Space Mono
│                                                                        │
│  Signature (Ed25519):                                                   │ ← 10px label
│  -----BEGIN SSH SIGNATURE-----                                          │ ← 9px Space Mono
│  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAg[...]                     │
│  -----END SSH SIGNATURE-----                                            │
│                                                                        │
│                                                                        │
│  ─────────────────────────────────────────────────────────────────    │ ← 3px rule
│                                                                        │
│     ✦                       kingofalldata.com                     ✦   │ ← Footer, 11px muted
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 5c. Print-specific notes

- **Canonical string is printed.** This is unique to the print layout relative to the screen layout. On screen, the canonical string is shown in the verify panel. On print, it is shown on the certificate itself so the document is fully self-contained.
- **Color mode:** Dark digital / light print — toggle in the download panel. Light print uses `#fafaf7` background, `#1a1a1a` text, `#b8890e` amber (darkened for WCAG print contrast). The dark version works on good inkjet/laser printers — specify it as the default, not the exception.
- **Fonts:** System sans-serif for body (prints without web font fetch); Space Mono for signature/canonical string blocks. Space Mono may need to be embedded in PDF export.
- **Learner ID:** Shown in full on the printed artifact. No truncation — this is a document.
- **QR code (optional, v2):** A QR code pointing to `canon.koad.sh/cert/{learnerId}` could appear in the bottom-right corner of the print layout. Omitted from v1. When added, it links to the web verification page, not to any account.

---

## 6. Curriculum Browser Integration

The `[ View your certificate ]` button in the curriculum browser (Section 4b of `2026-04-05-chiron-curriculum-browser.md`) links to the graduation screen. Its behavior:

**If the graduation ceremony has already been seen** (Alice has signed and the learner has gone through the arrival moment): the link goes directly to the certificate display (Section 1b of the graduation certificate spec), skipping the arrival/signing animation. The learner has already experienced that moment; they don't need it replayed.

**If the graduation ceremony has not yet been triggered** (Level 12 just completed, but the learner navigated away before the ceremony): the link triggers the full graduation arrival (Alice's speech, signing animation, then certificate display). This is the case where the learner earned it but hasn't seen it yet.

**Visual treatment of the `[ View your certificate ]` button:**

```
[ View your certificate  ✦ ]
```

- Amber fill button (entity color — same as the primary action buttons in Alice's UI)
- Full width of the curriculum map container on mobile
- Left-aligned (not centered) on desktop, matching the level row alignment
- The `✦` glyph is the connective tissue — it appears on every completed level, at the completion ceremony, and now on the button that leads to the certificate. One glyph = completion, consistently.
- Text: "View your certificate" — possessive, personal. Not "View the certificate" (impersonal) and not "Download certificate" (the screen is not primarily a download surface).

```css
.curriculum-certificate-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--entity-color);          /* Alice: #F4B844 */
  border: none;
  border-radius: 6px;
  font-family: Inter, system-ui, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #0c0c0e;
  text-decoration: none;
  cursor: pointer;
  transition: opacity 80ms ease;
}

.curriculum-certificate-cta:hover {
  opacity: 0.88;
}

@media (max-width: 640px) {
  .curriculum-certificate-cta {
    width: 100%;
    justify-content: center;
  }
}
```

---

## 7. Extending to Other Curricula

Chiron may author curricula that are signed by entities other than Alice. The certificate system is built for this from the start.

When a new Chiron curriculum completes, the certificate is issued by whichever entity delivered that curriculum. The certificate template above accepts `entity`, `entityKey`, `glyph`, and `entityColor` as variables. The `schema` version (`koad-io-certificate/1.0`) is fixed.

A future learner completing a Vulcan-taught "deploy your first daemon" curriculum would receive:

```markdown
---
schema: koad-io-certificate/1.0
entity: vulcan
entityKey: https://canon.koad.sh/vulcan
curriculum: vulcan-daemon-basics
curriculumTitle: Deploy Your First Daemon
...
signature: [Vulcan's Ed25519 signature]
---

# Vulcan's Attestation

Vulcan attests that **Jordan** completed the vulcan-daemon-basics curriculum
and demonstrated mastery of koad:io daemon operations.
```

The design system token `--entity-color` handles the visual change. Vulcan's forge crimson (`#C0392B`) replaces Alice's amber. The layout, the file structure, the verification path — all identical.

---

## 8. What This Brief Does Not Specify

The following are intentionally out of scope here — see referenced documents:

- The graduation arrival moment (Alice's speech, signing animation): `2026-04-05-alice-graduation-certificate.md`, Section 1a
- The verify panel (detailed step-by-step verification UI): `2026-04-05-alice-graduation-certificate.md`, Section 2
- The shareable card (social share image, OG dimensions): `2026-04-05-alice-graduation-certificate.md`, Section 3
- The download options panel (PDF/PNG/Markdown, Dark/Light toggle): `2026-04-05-alice-graduation-certificate.md`, Section 4b
- The Insiders section profile badge integration: `2026-04-05-alice-graduation-certificate.md`, Section 3b

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Ready for Vulcan implementation
