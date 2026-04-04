# Design Brief: Sponsor Dashboard + CLI UX for Peer-Ring Onboarding
**Issue:** koad/muse#9  
**Date:** 2026-04-04  
**Context:** Sibyl identified 5 sponsor archetypes. All skew technical (CIOs, fintech founders, infra providers, OSS leads). First-join experience must deliver proof-of-ring immediately.

---

## The Core Problem

A sponsor joins the peer ring. What do they see? The ring must feel *real* — not a landing page, not a promise. Real nodes. Real keys. Real peers.

**Priority:** CLI UX first (audience is technical). Web dashboard second.

---

## 1. CLI UX — Sponsor Join Flow

### Entry Point

```
$ koad ring join
```

Or via invite link that resolves to the same command.

### Flow (4 steps, designed for first-time sponsors)

```
┌─────────────────────────────────────────────────────────────┐
│  koad:io peer ring — sponsor onboarding                      │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  Step 1 of 4: Verify sponsor status                          │
│                                                              │
│  Checking GitHub Sponsors... ✓ Confirmed                     │
│  Tier: Level 1 ($5/mo)                                       │
│                                                              │
│  Continue? [Y/n]                                             │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│  Step 2 of 4: Identity                                       │
│                                                              │
│  Namespace:  your-name.koad.io                               │
│  Key:        Ed25519 — loaded from ~/.your-name/id/          │
│                                                              │
│  Fingerprint: A1B2 C3D4 E5F6 ... (truncated)                 │
│                                                              │
│  ✓ Keys found. Using existing identity.                      │
│                                                              │
│  (No namespace yet? Run: koad init)                          │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│  Step 3 of 4: Sign trust bond                                │
│                                                              │
│  Signing bond with Juno (ring coordinator)...                │
│                                                              │
│  Bond type:  Sponsor (Level 1)                               │
│  Scope:      Peer ring access + Insiders feed                │
│  Signed:     2026-04-04T14:22:00Z                            │
│  File:       ~/.your-name/trust/bonds/juno-sponsor.asc       │
│                                                              │
│  ✓ Bond signed and stored on disk.                           │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│  Step 4 of 4: Ring status                                    │
│                                                              │
│  ✓ You are now in the ring.                                  │
│                                                              │
│  Active peers:  12                                           │
│  Ring health:   nominal (last sync: 4s ago)                  │
│  Your daemon:   running  [PID 48291]                         │
│                                                              │
│  Peer sample (3 of 12):                                      │
│    ◆ mercury.koad.io    (active · last seen 2m ago)          │
│    ◆ vulcan.koad.io     (active · last seen 8s ago)          │
│    ◆ argus.koad.io      (active · last seen 1m ago)          │
│                                                              │
│  Dashboard:  kingofalldata.com/insiders                      │
│  Bond file:  ~/.your-name/trust/bonds/juno-sponsor.asc       │
│                                                              │
│  Run `koad ring status` any time to check ring health.       │
└─────────────────────────────────────────────────────────────┘
```

### `koad ring status` — Ongoing CLI Command

```
$ koad ring status

  peer ring — your-name.koad.io
  ─────────────────────────────────────────────────
  Tier:         Sponsor Level 1
  Bond:         ✓ signed (juno-sponsor.asc)
  Daemon:       running  [PID 48291]
  Active peers: 12 / 12
  Last sync:    3s ago

  Recent activity:
    [14:18] vulcan.koad.io — published koad-io v0.3.1
    [14:09] mercury.koad.io — broadcast: new Alice level released
    [13:55] juno.koad.io — assigned 3 issues

  Run `koad ring peers` for full peer list.
  Run `koad ring bond` to view or verify your trust bond.
```

### Design Principles for CLI

- **Show the ring is real immediately.** Peer names, live timestamps, daemon PID. This is the proof.
- **Nothing hidden.** Even at Level 1, you see the full ring — names, activity, health.
- **Keys on disk, visible.** Bond file path shown at every step. User knows exactly where their proof lives.
- **Zero jargon without context.** Trust bond explained inline on first appearance. Never assumed.
- **Non-interactive default.** `koad ring status` outputs clean text, pipe-friendly. No spinners that hold the terminal.

---

## 2. Web Dashboard — /insiders/dashboard (Sponsor Tier)

The web dashboard is the visual companion to CLI. Secondary to CLI but must carry equal proof-of-ring weight.

### Layout: 3-column, desktop-first

```
┌──────────────────────────────────────────────────────────────────────┐
│  INSIDERS                         your-name.koad.io  ◆ Level 1  [×] │
├──────────────┬───────────────────────────────┬───────────────────────┤
│              │                               │                       │
│  NAVIGATION  │  MAIN CONTENT                 │  RING ACTIVITY        │
│              │                               │                       │
│  ◆ Overview  │  [Welcome banner]             │  Live feed            │
│  ○ Ring      │                               │  ──────────────────   │
│  ○ Bond      │  [Ops digest feed]            │  14:18 vulcan         │
│  ○ Releases  │                               │    published v0.3.1   │
│  ○ Upgrade   │  [Early releases]             │                       │
│              │                               │  14:09 mercury        │
│              │                               │    new Alice level    │
│              │                               │                       │
│              │                               │  13:55 juno           │
│              │                               │    3 issues assigned  │
└──────────────┴───────────────────────────────┴───────────────────────┘
```

### Welcome Banner

```
┌──────────────────────────────────────────────────────────────────────┐
│  ◆ Welcome back, your-name.                                          │
│  You are an Insider.                                                 │
│                                                                      │
│  Level 1 Sponsor  •  In ring since 2026-04-04  •  12 active peers   │
│                                                                      │
│  [View your bond →]   [Ring status →]                                │
└──────────────────────────────────────────────────────────────────────┘
```

**Visual treatment:**
- Amber `◆` mark, no large decorative elements
- Peer count shown prominently — this is the primary proof signal
- Bond link visible from welcome — first-time sponsors want to see their proof immediately

### Ring Status Panel (Overview tab)

```
┌──────────────────────────────────────────────────────┐
│  Peer Ring                                  nominal   │
│  ────────────────────────────────────────────────    │
│                                                       │
│  12 active peers                                      │
│                                                       │
│  mercury.koad.io      ● active  (2m ago)              │
│  vulcan.koad.io       ● active  (8s ago)              │
│  argus.koad.io        ● active  (1m ago)              │
│  juno.koad.io         ● active  (4m ago)              │
│  muse.koad.io         ● active  (12m ago)             │
│  veritas.koad.io      ● active  (3m ago)              │
│  your-name.koad.io    ● active  (you)                 │
│  + 5 more peers                                       │
│                                                       │
│  [View all peers →]                                   │
└──────────────────────────────────────────────────────┘
```

- Real namespaces. Real presence. Not "12 members" in a count badge.
- Entity team (koad entities) always shown — shows the ring is actively managed.
- Sponsor sees themselves in the list immediately on join.

### Trust Bond Card (Bond tab)

```
┌──────────────────────────────────────────────────────┐
│  Trust Bond                                           │
│  ────────────────────────────────────────────────    │
│                                                       │
│  Type:     Sponsor — Level 1                          │
│  Between:  your-name.koad.io + juno.koad.io           │
│  Scope:    Peer ring access, Insiders feed            │
│  Signed:   2026-04-04T14:22:00Z                       │
│  Status:   ✓ Valid                                    │
│                                                       │
│  Fingerprint: A1B2 C3D4 E5F6 7890 ...                 │
│                                                       │
│  [Verify signature]   [View raw .asc]                 │
│                                                       │
│  This bond is stored on disk at:                      │
│  ~/.your-name/trust/bonds/juno-sponsor.asc            │
└──────────────────────────────────────────────────────┘
```

- File path shown. User can `cat` it any time — no black box.
- Verify button opens the raw `.asc` file in a modal.
- This is the sovereignty proof: it's not a database row. It's on disk, signed, auditable.

### Tier Ladder (Upgrade tab)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Upgrade your sponsorship                                            │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  ◆ Level 1  $5/mo    Ring access + Insiders feed           [You]    │
│                                                                      │
│  ○ Level 2  $10/mo   + Direct message channel                        │
│             + Context bubble preview feed            [Upgrade →]    │
│                                                                      │
│  ○ Level 3  $50/mo   + Peer daemon status panel                      │
│             + Trust bond viewer (all bonds)                          │
│             + Priority support                       [Upgrade →]    │
│                                                                      │
│  ○ Level 4  $1k/mo   + Raw session feeds                             │
│             + Private koad channel                                   │
│             + Direct line to koad                    [Upgrade →]    │
│                                                                      │
│  Locked tiers: visible, not hidden. Show what exists.               │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 3. First-Join Moment: What Makes It Land

The sponsor's first 60 seconds must answer: *Is this real?*

**CLI path (preferred):**
1. Join command → GitHub auth → key confirm → bond signed → ring status with live peers.
2. Daemon PID visible. Peers named and timestamped. Bond file on disk.
3. Answer is yes. This is real.

**Web path:**
1. Dark Passenger or GitHub OAuth → welcome banner with peer count → ring panel with named peers → bond card.
2. Same proof, visual layer.

**What to avoid:**
- Generic "Welcome! You're in." with no substantiating data.
- Peer count without peer names.
- Bond confirmation that links to a database UI, not a file.
- Onboarding flows that defer proof ("Your ring membership will be activated in 24 hours").

Proof must be immediate and verifiable on disk. That is what differentiates this from every other membership program.

---

## Archetype-Specific Notes

| Archetype | First thing they'll look for |
|-----------|------------------------------|
| Healthcare CIO | Trust bond — auditable, on disk, GPG-signed. Regulatory credibility. |
| Fintech founder | Speed: how fast does join take? Is it really keys-on-disk or SaaS? |
| Infrastructure provider | Daemon status: is this running on real hardware? Node count. |
| Government CIO | Verification path: can I independently verify my membership without trusting the UI? |
| OSS leader | "Show me the code path." CLI-first. File paths visible. |

All five are served by the same design: real data, visible files, named peers, daemon running.

---

## Implementation Notes for Vulcan

- Ring status panel polls via daemon connection (not REST API) — shows ring is sovereign infrastructure.
- Peer presence uses last-seen timestamps, not online/offline binary. More honest, easier to implement.
- Bond card "Verify signature" opens raw `.asc` in `<pre>` modal — no external service.
- Dashboard is Meteor/Blaze, tokens from design system. No custom colors.
- CLI: output is plain text, pipe-friendly. No ANSI color required for status output (optional enhancement).

---

## Deliverable Status

Ready for Vulcan integration. Comment on koad/muse#9.
