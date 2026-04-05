# Design Brief: canon.koad.sh — Public Key Distribution Landing Page
**Date:** 2026-04-05
**Author:** Muse
**URL:** `canon.koad.sh`
**Audience:** Developers fetching keys for koad:io entities
**Status:** Brief — ready for implementation

---

## What This Page Is

canon.koad.sh currently serves raw key files. The landing page (`/`) adds a human-readable index — not a tutorial, not an explainer, not a product page. A directory.

The audience already knows what GPG is. They know why public keys matter. They arrived here from a trust bond file, a README, or a command they're about to run. Give them what they came for.

**Design goal:** Land, find the key you need, copy the fetch command, leave. Under 10 seconds.

---

## Content

The page has three elements:

1. A one-line description of what this endpoint is
2. A table of all distributed keys with name, fingerprint, and fetch command
3. Nothing else

---

## Layout

Single column. Left-aligned. Max-width: `720px`.

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  canon.koad.sh                                                 │  ← domain, JetBrains Mono 18px
│                                                                │
│  Public key distribution for koad:io entities.                │  ← descriptor, Inter 400, 15px,
│                                                                │     --text-secondary
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  koad                                                          │  ← entity name, Inter 600, 14px
│  4A3B...F82C                                                   │  ← fingerprint, JetBrains Mono
│  curl https://canon.koad.sh/koad.keys                         │     12px, --text-muted
│                                                                │     [copy]
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  juno                                                          │
│  7C1D...A490                                                   │
│  curl https://canon.koad.sh/juno.keys                         │
│                                                                │     [copy]
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  vulcan                                                        │
│  ...                                                           │
│                                                                │
│  (one block per entity)                                        │
│                                                                │
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  All keys are Ed25519. Served over HTTPS.                      │  ← footer note, 12px, --text-muted
│  Source: github.com/koad                                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Design Notes

**Page title:** `canon.koad.sh` in JetBrains Mono, 18px, `--text-primary`. No tagline beneath it, no logo, no navigation. The domain name is the identifier.

**Descriptor:** One sentence: *"Public key distribution for koad:io entities."* No further explanation. The audience does not need one.

**Key blocks:** One block per entity. Each block contains:
- Entity name: Inter 600, 14px, `--text-primary`
- Full fingerprint: JetBrains Mono 12px, `--text-muted`. Show the full fingerprint — do not truncate. Developers use fingerprints to verify. Truncation defeats the purpose.
- Fetch command: JetBrains Mono 13px, `--bg-tertiary` code block, single line. A copy button sits at the right edge of the block. 20px clipboard icon, `--text-secondary`, turns `--accent` on hover. No tooltip.

**Dividers:** 1px `--border-subtle` rules between blocks. Breathing room without visual weight.

**Order:** koad first (the human, the root of trust), then entities in alphabetical order. The ordering signals hierarchy: koad's key is the anchor.

**No per-key navigation, no search.** The list is short enough to scan. If it grows beyond ~20 entries, add an anchor link at the top per entity — but do not add a search bar until that threshold is hit.

**Footer note:** Two lines, 12px, `--text-muted`:
```
All keys are Ed25519. Served over HTTPS.
Source: github.com/koad
```
"Source: github.com/koad" links to `github.com/koad` — the verifiable origin of the entities. Not a marketing link. An audit trail.

**No JavaScript required.** The copy button is a progressive enhancement — the command is fully visible and selectable without it. The page must render completely as static HTML.

---

## Raw File Behavior

`/koad.keys`, `/juno.keys`, etc. continue to serve raw key files exactly as they do now. The landing page at `/` is additive — it does not change the behavior of any existing URL.

Content-type for raw key files: `text/plain`. No change.

---

## What This Page Does Not Do

- Does not explain what GPG is or how to use it
- Does not explain what koad:io is
- Does not link to kingofalldata.com (there is no reason to; anyone who needs that link already has it)
- Does not include a contact form, CTA, or any conversion element
- Does not animate anything

This is infrastructure documentation, rendered as a page. The visual design serves legibility. That is the entire goal.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for implementation
