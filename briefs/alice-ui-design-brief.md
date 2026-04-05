# Alice UI Design Brief

**Status:** Updated — Chiron Decisions Incorporated  
**Date:** 2026-04-05 (original: 2026-04-03)  
**Audience:** Vulcan (PWA integration), Juno (approval)  
**Entity:** Muse  
**References:** PROJECT-08: Alice, koad:io Design System, koad/vulcan#36, chiron/curricula/alice-onboarding/DECISIONS.md

---

## Changelog

### 2026-04-05 Update

Three Chiron decisions (DECISIONS.md, 2026-04-05) have been settled and are now incorporated into this brief:

1. **Learner ID: UUIDv4, Alice-generated locally.** The learner is identified by a locally-generated UUID. Alice asks for a display name on first interaction ("What would you like me to call you?") and stores it alongside the UUID. The display name is what appears in Alice's conversation and on the certificate. The UUID is never surfaced to the learner — it is Alice's internal key.

2. **Gating: Strict.** A locked level cannot be loaded or previewed. The learner only sees the current level and the fact that a next level exists. However, **accelerated assessment** is the legitimate unlock path: if a learner claims prior knowledge, Alice conducts the exit-criteria assessment directly. If they pass, Alice writes the completion record and the next level becomes available normally. Vulcan does not need to model this case — it always resolves to a standard completion write.

3. **Completion writes: Alice writes to disk; Vulcan reads.** Vulcan does not write completion records. Alice writes markdown files to `~/.alice/learners/{uuid}/curricula/alice-onboarding/level-{N}-complete.md`. Vulcan reads them to determine gating state.

**UI impacts:** Screen 1 gains a name-prompt moment. Screen 2 gains an "I already know this" affordance on locked levels. The data model section is updated throughout.

---

## Vision

Alice is the voice of patience and warmth in the koad:io ecosystem. Her UI must feel like sitting across from a mentor, not operating a dashboard. Same dark foundation as the main portal, but warmer in accent, more conversational in rhythm, and spatial in its visualization of progress.

The interface should honor the philosophical journey the human is on — from curious stranger to sovereign operator — not just track completion metrics.

## Design Principles for Alice

### 1. **Conversation as Primary Interface**
- Alice communicates through dialogue. Her space is a chat interface, not a form.
- Her messages are warm, slightly personal, never jargon-heavy.
- The human can ask questions within the conversation flow.
- Scrolling through Alice's space reads like reading a letter you're writing together.

### 2. **Journey, Not Progress**
- The 12 levels should feel spatial — something you're moving through, not tracking.
- Visual language: a path, a stairway, a map. Not a percentage bar.
- Each level should have weight and presence.
- The human should feel their progression in their bones, not just see a number.

### 3. **Warmth Within Dark**
- Dark base (#0a0a0a, matching the main portal).
- Accent color: **warm amber/gold (#F4B844, #E8A738)** instead of the portal's violet.
- Alice's space is immediately visually distinct when you enter it — you know you're with Alice, not in the operational portal.
- Typography: same clean sans-serif (system default or space-mono), but warmer line height and letter spacing.

### 4. **Graduation as Sacred Moment**
- The certificate screen is not a reward popup — it's a ceremonial moment.
- The cryptographic signature is visible and honored — this is a real, verifiable, personal commitment from Alice.
- The human should want to screenshot it, share it, frame it.
- The graduation unlocks explicit introduction to Juno.

### 5. **Mobile-First, Everywhere-Readable**
- Alice's first users will be on phones in cafes, on couches, away from desks.
- Every screen is touch-optimized, readable at any size.
- Conversation UI adapts gracefully from mobile chat to desktop.
- No horizontal scrolling. Ever.

## Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| `alice-bg` | #0a0a0a | Background (same as portal) |
| `alice-text` | #f0ede5 | Primary text (slightly warmer than portal white) |
| `alice-accent` | #F4B844 | Interactive, focus, Alice's voice highlight |
| `alice-accent-dark` | #E8A738 | Hover, active state |
| `alice-border` | #2a2a2a | Subtle dividers |
| `alice-success` | #8ac926 | Level completion, checkmarks (warm green) |
| `alice-subtle` | #555555 | Secondary text, past levels |

## Typography

- **Font Family:** System sans-serif (Helvetica Neue, Segoe UI, system font) or Space Mono for code/keys.
- **Alice's voice:** 18-20px body text, line-height 1.6 (conversational, not cramped).
- **Headings:** Warmer, but restrained. 24-28px for level titles.
- **Interaction text:** Small and clear, never cute or diminishing.

---

## Key Screens

### Screen 1: Alice Introduction + Name Prompt

**Context:** Human lands in Alice's space for the first time. They meet her voice. No friction — just invitation. Then Alice immediately asks their name before anything else happens. This is how she establishes their learner identity locally.

**1a. First greeting:**

```
┌──────────────────────────────────────┐
│                                      │ ← Warm amber top accent bar
│  Kingofalldata.com                   │
│  ───────────────────────────────────│
│                                      │
│  Alice                               │
│  ────────────────────────────────── │
│                                      │
│  "Hi there. I'm Alice.               │
│                                      │
│   I help people like you understand  │
│   what it means to own your world.   │
│                                      │
│   Over 12 conversations, you'll      │
│   learn the philosophy and the       │
│   practice of sovereignty.           │
│                                      │
│   When you're done, you'll have      │
│   a certificate signed by me — your  │
│   first proof that you understand    │
│   koad:io.                           │
│                                      │
│   Ready?"                            │
│                                      │
│                    ┌──────────────┐  │
│                    │ Let's begin ✦│  │ ← Gold button, prominent
│                    └──────────────┘  │
│                                      │
│  or learn more about koad:io first   │ ← Subtle secondary link
│                                      │
└──────────────────────────────────────┘
```

**1b. Name prompt (immediately follows "Let's begin"):**

```
┌──────────────────────────────────────┐
│                                      │
│  Alice                               │
│  ────────────────────────────────── │
│                                      │
│  "Before we begin — what would       │
│   you like me to call you?"          │
│                                      │
│  ┌──────────────────────────────┐    │
│  │  Your name or handle...      │    │ ← Text input, focused
│  └──────────────────────────────┘    │
│                                      │
│                    ┌──────────────┐  │
│                    │ That's me ✦  │  │ ← Gold confirm button
│                    └──────────────┘  │
│                                      │
│  You can use any name or handle.     │ ← Reassuring note, 13px muted
│  This stays on your device.          │
│                                      │
└──────────────────────────────────────┘
```

**Notes:**
- Simple, warm greeting. No logo spam, no sales language.
- Amber accent bar signals "this is Alice's space."
- Primary action is warm and inviting, not corporate.
- Secondary option respects that they might need context first.
- **Name prompt is immediate, low-stakes, reassuring.** "This stays on your device" is true and important — the UUID and display_name live in Alice's local filesystem (`~/.alice/learners/{uuid}/identity.md`), not in any database.
- **What happens behind the scenes:** on confirming the name, Alice generates a UUIDv4 locally and writes `identity.md`. The UUID is never shown to the learner in normal flow. From this point on, Alice addresses the learner by their display_name.
- **Returning learner edge case:** If Alice cannot determine who the learner is (e.g. new device), she may ask "Have we spoken before? Do you have a learner ID?" — but this is recovery UX, not the normal path. Design for this edge case is deferred; the happy path is all that ships in Phase 1.
- Mobile: Full-height, single column, thumb-reachable button and input.

---

### Screen 2: Level Progression View (The Journey)

**Context:** Human has completed or is working through levels. They see their path.

**2a. The journey list:**

```
┌──────────────────────────────────────┐
│ ← Back                         Alice  │
├──────────────────────────────────────┤
│                                      │
│  Your Path, [Name]                  │ ← Uses display_name (e.g. "Your Path, Jordan")
│  ═══════════════════════════════════│
│                                      │
│   ✦ Level 1: What is sovereignty?   │ ← Complete (gold ✦, muted text)
│     ✓ Completed in 8 min            │
│                                      │
│   ✦ Level 2: What is an entity?     │ ← Complete
│     ✓ Completed in 12 min           │
│                                      │
│   ◆ Level 3: Keys & identity        │ ← Current (amber ◆, bright)
│     In progress — you're reading... │
│                                      │
│   ○ Level 4: The daemon             │ ← Locked
│     Already know this?              │ ← Subtle affordance (see 2b below)
│   ○ Level 5: Commands & skills      │
│   ○ Level 6: Trust bonds            │
│   ...                               │
│   ○ Level 12: Your kingdom is live  │
│                                      │
│  Progress: 3 of 12 levels           │ ← Subtle, not prominent
│                                      │
└──────────────────────────────────────┘

       ↓ (Scroll to active level)

┌──────────────────────────────────────┐
│                                      │
│  Level 3: Keys & Identity           │
│  ───────────────────────────────── │
│                                      │
│  Alice                              │
│  "So you understand that files are  │
│   identity. Now the harder part:    │
│                                      │
│   Your keys are you. Not your data. │
│   You.                              │
│                                      │
│   This is the line between owning   │
│   your world and being a guest in   │
│   someone else's."                  │
│                                      │
│  [Next: Let me show you your keys]  │ ← Interactive next step
│                                      │
└──────────────────────────────────────┘
```

**2b. Locked level with accelerated assessment affordance (tap to expand):**

When a learner taps a locked level, a small inline affordance appears — not a bypass, just an invitation to claim prior knowledge and be assessed:

```
┌──────────────────────────────────────┐
│   ○ Level 4: The daemon             │ ← Locked
│   ───────────────────────────────── │
│                                      │
│   This level unlocks after you      │ ← Inline expansion
│   complete Level 3.                 │
│                                      │
│   Already know this topic?          │
│   Tell Alice and she'll assess you. │
│   Pass and this level is unlocked.  │
│                                      │
│   [ Tell Alice I know this ]        │ ← Amber link, not a primary button
│                                      │
└──────────────────────────────────────┘
```

Tapping "Tell Alice I know this" drops the learner into the current lesson conversation with a pre-seeded message ("I already understand [Level N topic] — can you assess me?"). Alice conducts the assessment in the normal conversation flow. If the learner passes, Alice writes the completion record to disk and the level status updates to complete in the next render.

**Notes:**
- Journey visualization: completed levels appear faded with checkmarks, current level is bright with amber accent, locked levels are hollow.
- **Display name personalizes the journey header** — "Your Path, Jordan" feels owned. This uses the `display_name` from Alice's identity record for this learner.
- Spatial layout — human can see where they are in the journey at a glance.
- Completion times create a sense of real progress (not fake, actual durations).
- Current level expands to show Alice's message and next action.
- **Accelerated assessment affordance is subtle, not prominent.** It appears only when a locked level is tapped. The default UX does not show it — it is for learners who actively seek it. This matches Chiron's intent: accelerated assessment is a recovery path for prior-knowledge learners, not an escape hatch.
- **The locked state is honest.** "This level unlocks after you complete Level 3" is accurate and non-judgmental. No "coming soon" — it simply isn't available yet for this learner.
- Mobile: Single column, smooth scroll through the path. Completed levels collapse to save space. Tapping a locked level expands the inline affordance in place.

---

### Screen 3: Lesson Moment (In the Conversation)

**Context:** Human is mid-lesson with Alice. She's teaching, they're learning, they can ask questions.

```
┌──────────────────────────────────────┐
│ ← Back                   Level 6: TB  │ ← Breadcrumb
├──────────────────────────────────────┤
│                                      │
│  [Earlier messages scroll above...]  │
│                                      │
│                                      │
│  Alice                              │
│  "A trust bond is a promise written │
│   to disk. It's signed. It can't    │
│   be revoked — only extended or     │
│   replaced.                         │
│                                      │
│   Think of it like a contract, but  │
│   instead of between two lawyers,   │
│   it's between two people. Direct." │
│                                      │
│  13:42                              │ ← Timestamp (human, not UTC)
│                                      │
│                                      │
│  You                                │
│  [Text input field]                 │ ← Ask a question, move forward
│                                      │
│  ─────────────────────────────────│
│  [Previous answers to this Q]      │ ← Expandable, past context
│  [Glossary: trust bond]            │ ← Help, always available
│                                      │
│  Questions? Type here or continue →│ ← Soft prompt, not nagging
│                                      │
└──────────────────────────────────────┘
```

**Notes:**
- Conversation UI, not form UI. Alice speaks, human responds.
- Timestamps are human-friendly (1:42pm, not timestamps).
- Text input is always available for questions — the conversation is bidirectional.
- Expandable helpers (glossary, previous answers) are present but not intrusive.
- Mobile: Input field is bottom-sticky, keyboard-aware.
- Reading level: conversational, not academic. Alice uses "you," not "the user."

---

### Screen 4: Graduation & Certificate

**Context:** Human has completed all 12 levels. This is the ceremonial moment.

```
┌──────────────────────────────────────┐
│                                      │
│  ✦                                  │ ← Centered amber accent
│                                      │
│  Alice                              │
│                                      │
│  "You did it.                       │
│                                      │
│   You moved from curious to         │
│   sovereign. You didn't just learn  │
│   about your keys — you held them.  │
│   You didn't just read about trust  │
│   — you built bonds.                │
│                                      │
│   You understand what it means to   │
│   own your world.                   │
│                                      │
│   I'm signing your mastery          │
│   certificate now. This is real.    │
│   This is forever."                 │
│                                      │
│  ───────────────────────────────── │
│                                      │
│  CERTIFICATE OF MASTERY             │ ← Formal serif or caps
│                                      │
│  This certifies that [display_name] │ ← Uses learner's chosen name
│  has completed the koad:io          │
│  sovereignty curriculum and         │
│  demonstrated mastery.              │
│                                      │
│  Learner ID: a9f3c2e1-7b4d-...     │ ← UUID shown here — verifiable
│  Signed by: Alice                   │
│  Date: April 3, 2026                │
│                                      │
│  Signature (Ed25519):               │ ← Alice's ed25519 key, not GPG
│  -----BEGIN SSH SIGNATURE-----      │
│  U1NIU0lHAAAAAQAAADMAAAALc3No...    │
│  -----END SSH SIGNATURE-----        │
│                                      │
│  ───────────────────────────────── │
│                                      │
│                    ┌──────────────┐  │
│                    │ Share cert   │  │ ← Gold button
│                    └──────────────┘  │
│                    ┌──────────────┐  │
│                    │ Verify sig   │  │ ← Secondary button (Ed25519)
│                    └──────────────┘  │
│                                      │
│  Next step: Alice introduces Juno   │
│  → Juno helps you build your        │
│     kingdom and find your sponsors  │
│                                      │
│                    ┌──────────────┐  │
│                    │ Meet Juno ✦  │  │ ← Gold, inviting next step
│                    └──────────────┘  │
│                                      │
└──────────────────────────────────────┘
```

**Notes:**
- Ceremonial, not transactional. Alice speaks as a mentor honoring the achievement.
- Certificate is formal (all caps, clear signature) but still warm — this is real and verifiable.
- **Learner ID (UUID) appears on the certificate.** This is the stable, verifiable identifier — not the display name alone. Someone who wants to verify this certificate can check the UUID against Alice's learner records. The display name is what makes it personal; the UUID is what makes it trustworthy.
- **Signature is Alice's Ed25519 key**, not GPG. Alice signs the certificate file using `~/.alice/id/ed25519`. The "Verify (Ed25519)" button shows the raw signature block and links to Alice's public key endpoint.
- Share and Verify buttons respect that the human will want to prove this to others.
- Final action (Meet Juno) is warm and forward-looking, not a goodbye.
- Mobile: Certificate scrolls vertically, signature is readable, buttons are thumb-reachable.
- Desktop: Could layout as a formal certificate view, but still warm in tone.

---

## Implementation Notes for Vulcan

### Component Structure

```
<AliceContainer>
  <AliceIntro />              // First-time greeting
  <AliceNamePrompt />         // Collects display_name, generates UUID, writes identity.md
  <AliceJourney />            // Level progression view
    ├── <LevelList />         // Completed, current, locked
    │     └── <LockedLevel /> // Inline accelerated-assessment affordance on tap
    └── <CurrentLesson />
      ├── <AliceConversation />
      └── <HumanInput />
  <AliceGraduation />         // Certificate moment
</AliceContainer>
```

**State Alice manages (on disk):**
- `~/.alice/learners/{uuid}/identity.md` — display_name, created_at
- `~/.alice/learners/{uuid}/curricula/alice-onboarding/level-{N}-complete.md` — one per completed level
- `~/.alice/learners/{uuid}/curricula/alice-onboarding/certificate.md` — issued at Level 12

**State Vulcan reads (never writes):**
- All of the above — Vulcan's gating logic reads these files to determine level status

### Data Structure

**Learner identity (from `~/.alice/learners/{uuid}/identity.md`):**
- `learner_id`: UUIDv4 — Alice-generated at first interaction, never shown to learner in normal flow
- `display_name`: Human-supplied handle or name ("Jordan", "koad", whatever they chose) — used everywhere Alice addresses them
- `created_at`: ISO-8601 timestamp of first session

**Each level (from curriculum + learner state):**
- `id`: 0-12 (level 0 is "The First File" — prerequisite-free)
- `title`: Human-readable level name
- `description`: One-line descriptor for list view
- `content`: Alice's conversational content (markdown or rich text)
- `duration`: Estimated time to complete
- `status`: `locked | available | in-progress | complete`
- `completed_at`: ISO-8601 if complete (from completion record on disk)
- `interactions`: Optional branching questions or checks

**What determines `status`:** Vulcan reads `~/.alice/learners/{uuid}/curricula/alice-onboarding/level-{N}-complete.md`. If the file exists and is well-formed, the level is complete and the next is available. Alice writes these files; Vulcan reads them.

**The certificate (from `~/.alice/learners/{uuid}/curricula/alice-onboarding/certificate.md`):**
- `display_name`: Learner's chosen name (shown on certificate)
- `learner_id`: UUID (shown on certificate — this is the verifiable identifier)
- `completedDate`: Timestamp of Level 12 completion
- `aliceSignature`: Ed25519 signature from Alice's key at `~/.alice/id/ed25519` (Alice signs this, not Vulcan)
- `verificationUrl`: Public key endpoint for Alice's ed25519 public key

### CSS Custom Properties

```css
:root {
  --alice-bg: #0a0a0a;
  --alice-text: #f0ede5;
  --alice-accent: #F4B844;
  --alice-accent-dark: #E8A738;
  --alice-border: #2a2a2a;
  --alice-success: #8ac926;
  --alice-subtle: #555555;
  
  --alice-spacing: 1.5rem;
  --alice-line-height: 1.6;
}
```

### Accessibility

- All interactive elements have clear focus states (amber highlight).
- Conversation text is always readable (no contrast issues).
- Level progress uses icons (✦, ◆, ○) + text, not color alone.
- Keyboard navigation: Tab through conversation, Enter to send, Arrow keys to scroll levels.

---

## Deviations from Main Portal

| Aspect | Main Portal | Alice |
|--------|-------------|-------|
| **Accent Color** | Violet (#A78BFA) | Warm Gold (#F4B844) |
| **Primary Interaction** | Dashboard, commands | Conversation, dialogue |
| **Progress Language** | Tasks, metrics | Journey, levels |
| **Tone** | Sovereign, technical | Warm, mentoring |
| **Primary Device** | Desktop-first | Mobile-first |
| **Typography** | Space-mono, tight | System sans, relaxed |

---

## Next Steps

1. **Vulcan:** Integrate Alice UI components into the PWA (kingofalldata.com). Reference koad/vulcan#36 for the full progression system spec and API endpoints.
2. **Curriculum Content:** Chiron has authored all 12 levels. Content is complete at `~/.chiron/curricula/alice-onboarding/levels/`.
3. **Certificate Signing:** Alice signs with Ed25519 (`~/.alice/id/ed25519`). This is Alice's responsibility — Vulcan reads the resulting certificate file, does not produce it.
4. **Name prompt UX:** Build `<AliceNamePrompt />` as the gate between intro and Level 0. No learner session is established until display_name is provided and UUID is written.
5. **Testing:** Human testing with first cohort through the full 12 levels.

---

**Design Direction:** Muse  
**Original date:** 2026-04-03  
**Updated:** 2026-04-05 — Chiron decisions on learner ID, strict gating, and accelerated assessment incorporated
