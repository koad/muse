# Alice UI Design Brief

**Status:** Design Direction  
**Date:** 2026-04-03  
**Audience:** Vulcan (PWA integration), Juno (approval)  
**Entity:** Muse  
**References:** PROJECT-08: Alice, koad:io Design System

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

### Screen 1: Alice Introduction

**Context:** Human lands in Alice's space for the first time. They meet her voice. No friction — just invitation.

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

**Notes:**
- Simple, warm greeting. No logo spam, no sales language.
- Amber accent bar signals "this is Alice's space."
- Primary action is warm and inviting, not corporate.
- Secondary option respects that they might need context first.
- Mobile: Full-height, single column, thumb-reachable button.

---

### Screen 2: Level Progression View (The Journey)

**Context:** Human has completed or is working through levels. They see their path.

```
┌──────────────────────────────────────┐
│ ← Back                         Alice  │
├──────────────────────────────────────┤
│                                      │
│  Your Path to Mastery               │
│  ═══════════════════════════════════│
│                                      │
│   ✦ Level 1: What is sovereignty?   │ ← Complete (gold ✦, muted text)
│     ✓ Completed in 8 min            │
│                                      │
│   ✦ Level 2: What is an entity?     │ ← Complete
│     ✓ Completed in 12 min           │
│                                      │
│   ◆ Level 3: Keys & identity        │ ← Current (amber ◆, bright)
│     In progress — you're reading... │    Conversation below
│                                      │
│   ○ Level 4: The daemon             │ ← Locked (hollow ○, grayed)
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

**Notes:**
- Journey visualization: completed levels appear faded with checkmarks, current level is bright with amber accent, locked levels are hollow.
- Spatial layout — human can see where they are in the journey at a glance.
- Completion times create a sense of real progress (not fake, actual durations).
- Current level expands to show Alice's message and next action.
- Mobile: Single column, smooth scroll through the path. Completed levels collapse to save space.

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
│  This certifies that [Name]         │
│  has completed the koad:io          │
│  sovereignty curriculum and         │
│  demonstrated mastery.              │
│                                      │
│  Signed by: Alice                   │
│  Date: April 3, 2026                │
│                                      │
│  Signature (GPG):                   │
│  -----BEGIN PGP SIGNATURE-----      │
│  iD8DBQBJHf4xLd5jR5XkN4QRAh93Ak...  │
│  -----END PGP SIGNATURE-----        │
│                                      │
│  ───────────────────────────────── │
│                                      │
│                    ┌──────────────┐  │
│                    │ Share cert   │  │ ← Gold button
│                    └──────────────┘  │
│                    ┌──────────────┐  │
│                    │ Verify (GPG) │  │ ← Secondary button
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
- GPG signature is visible and readable — no hiding the crypto, it's the point.
- Share and Verify buttons respect that the human will want to prove this to others.
- Final action (Meet Juno) is warm and forward-looking, not a goodbye.
- Mobile: Certificate scrolls vertically, signature is readable, buttons are thumb-reachable.
- Desktop: Could layout as a formal certificate view, but still warm in tone.

---

## Implementation Notes for Vulcan

### Component Structure

```
<AliceContainer>
  <AliceIntro />         // First-time entry
  <AliceJourney />       // Level progression view
    ├── <LevelList />    // Completed, current, locked
    └── <CurrentLesson />
      ├── <AliceConversation />
      └── <HumanInput />
  <AliceGraduation />    // Certificate moment
</AliceContainer>
```

### Data Structure

Each level needs:
- `id`: 1-12
- `title`: Human-readable level name
- `description`: One-line descriptor for list view
- `content`: Alice's conversational content (markdown or rich text)
- `duration`: Estimated time to complete
- `interactions`: Optional branching questions or checks

The certificate needs:
- `humanName`: Learner's identity
- `completedDate`: Timestamp
- `aliceSignature`: GPG signature (Alice entity signs this)
- `verificationUrl`: Public GPG endpoint

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

1. **Vulcan:** Integrate Alice UI components into the PWA (kingofalldata.com).
2. **Curriculum Content:** Finalize the 12 level scripts — Alice's actual dialogue.
3. **Certificate Signing:** Implement GPG signing flow for Alice entity.
4. **Testing:** Human testing with first cohort through the full 12 levels.

---

**Design Direction:** Muse  
**Date:** 2026-04-03
