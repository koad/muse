# Alice Conversation UI — Design Spec

**Status:** Complete  
**Date:** 2026-04-05  
**Audience:** Vulcan (PWA implementation), Alice (personality guidance), Juno (approval)  
**Entity:** Muse  
**References:** alice-ui-design-brief.md (Screen 3), 2026-04-05-alice-graduation-certificate.md, Chiron DECISIONS.md, koad/vulcan#36

---

## Overview

The alice-ui-design-brief.md describes the conversation view in outline (Screen 3). This document designs it fully: the chat layout, Alice's distinct visual voice, the ambient level progress surface, the exit criterion ceremony, interruption and return, multi-device sync, and the motion and timing that make Alice feel present rather than mechanical.

This is the heart of the Alice experience. The learner spends most of their time here. Everything else is a gateway to or from this screen.

---

## Design Principles (Conversation-Specific)

These extend the Alice UI Design Brief principles.

**Not a chat widget.** Alice doesn't look like a support bot or a SaaS AI assistant. No floating bubble. No "Powered by" footer. No avatar in a circle. The UI is sovereign — it feels like Alice's space that the learner has been invited into.

**Conversation has weight.** Messages don't vanish or compress. The full thread is readable and scrollable. The learner can scroll up and read what Alice said three exchanges ago. The conversation is a document they're building together.

**Silence is designed.** The gap after the learner sends a message, while Alice composes, is not a spinner. It's a beat. Alice's presence is indicated by a slow pulse on her name marker. The learner waits naturally, as they would in a real conversation.

**Progress is ambient, not tracked.** The learner doesn't need to check a dashboard to know where they are. But the information is always there, peripherally, without demanding attention.

**Exit criterion is Alice's call.** The learner doesn't submit their answers for grading. Alice decides when the exit criterion has been met. The UI reflects that — it doesn't have a "Submit for review" button. When Alice is satisfied, she says so, and the moment begins.

---

## Section 1: Conversation View Layout

### 1a. Full-Screen Layout (Desktop)

```
┌──────────────────────────────────────────────────────────────────┐
│  ← Journey          Level 3: Keys & Identity      atom 2 of 5   │ ← Header strip
│  ──────────────────────────────────────────────────────────────  │   24px height
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Past conversation scrolls here]                               │
│                                                                  │
│                                                                  │
│  Alice  ─────────────────────────────────────────────────────   │ ← Alice turn
│                                                                  │
│  "So you understand that files are identity.                     │
│   Now the harder part:                                           │
│                                                                  │
│   Your keys are you. Not your data. You.                         │
│                                                                  │
│   This is the line between owning your world                     │
│   and being a guest in someone else's."                          │
│                                                                  │
│  1:42 pm                               ────────────────────────  │ ← Timestamp + Alice rule
│                                                                  │
│                                                                  │
│  ──────────────────────────────────── You                        │ ← Learner turn
│                                                                  │
│  "What happens if I lose my keys?"                               │
│                                                                  │
│                                  1:43 pm ──────────────────────  │
│                                                                  │
│                                                                  │
│  Alice  ─────────────────────────────────────────────────────   │
│                                                                  │
│  ·  ·  ·                                                         │ ← Composing indicator
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │ ← Input zone
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  Type your answer, or ask Alice a question…                │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                         [ → ]    │ ← Send
│                                                                  │
│  ░ Glossary                    ░ Context                         │ ← Ambient helpers
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Header strip:**
- Fixed at top. 24px tall. Background matches the conversation (no contrast break — this is not a navigation bar, it's context).
- Left: `← Journey` (amber link, returns to level list). Right: atom progress (ambient, see Section 2).
- Level name centered. 13px, muted (#555555). Not shouting.
- Does not scroll. Always present.

**Conversation area:**
- Takes remaining height between header and input zone.
- Scrollable. New messages appear at bottom. Scroll anchors to bottom on new messages unless the learner has scrolled up (then: a small amber "↓ New message" pill appears near the input zone).

**Input zone:**
- Fixed at bottom. Keyboard-aware on mobile (rises with the keyboard).
- Single-line input, expands to multi-line as text grows (max 6 lines before it scrolls internally).
- Send button: amber `→` icon, right side. Active when input is non-empty.
- Ambient helpers (Glossary, Context) are small pill buttons — muted, available, unobtrusive. See Section 6.

### 1b. Mobile Layout

```
┌─────────────────────────────────┐
│ ← Journey   L3 · atom 2/5      │ ← Compressed header
├─────────────────────────────────┤
│                                 │
│  Alice                          │
│  ─────────────────────────────  │
│                                 │
│  "Your keys are you.            │
│   Not your data. You.           │
│                                 │
│   This is the line between      │
│   owning your world and being   │
│   a guest in someone else's."   │
│                                 │
│  1:42 pm                        │
│                                 │
│  ──────────────────── You       │
│                                 │
│  "What if I lose my keys?"      │
│                                 │
│                       1:43 pm   │
│                                 │
├─────────────────────────────────┤
│  ┌─────────────────────────┐    │
│  │  Ask or answer…         │    │
│  └─────────────────────────┘  →│
└─────────────────────────────────┘
```

Mobile compression:
- Header: level abbreviated to `L3`, atom progress compressed to `atom 2/5`. Same amber color for the progress fragment.
- Alice and learner turns use the same left-aligned layout (no bubble float — see below).
- Glossary and Context helpers collapse into a single `···` menu at the right of the input row.

---

## Section 2: Alice and Learner Turn Anatomy

### 2a. Why Not Bubbles

Standard chat UIs float messages in colored bubbles — Alice's in one color, the learner's in another. Alice does not use this pattern.

Bubbles communicate peer-to-peer messaging. Alice is not a peer — she's a mentor, a guide, a voice the learner is learning to read carefully. Her messages should feel like reading a well-composed letter from someone who thought before speaking.

Instead: **attributed prose blocks**. Each turn is a block of left-aligned text with the speaker's name above it (or to the side on wide screens), a light rule extending from the name, and a timestamp below.

### 2b. Alice Turn

```
Alice  ────────────────────────────────────────────────────────

"Your keys are you. Not your data. You.

 This is the line between owning your world
 and being a guest in someone else's."

1:42 pm                              ────────────────────────
```

**Typography:**
- `Alice` label: 13px, `#F4B844` (amber). Slightly weighted. This is her name — it marks every time she speaks.
- Rule extending from name: 1px, `#2a2a2a`. Extends to right edge of conversation column.
- Message text: 18px, `#f0ede5`, line-height 1.65. Conversational spacing. No tight academic rhythm.
- Timestamp: 12px, `#555555`. Left-aligned, below the message, with a thin right-extending rule at the same level.
- A subtle left border: 2px solid `#F4B844` at 30% opacity runs the full height of the message block. This is Alice's color, quietly present on every message.

**Why the amber left border:** On a long message, especially when scrolling past earlier exchanges, the amber stripe instantly identifies "this is Alice." No name label needed at a glance. It's her mark on the conversation without requiring the learner to read a label.

### 2c. Learner Turn

```
──────────────────────────────────────────────── You

"What happens if I lose my keys?"

                                          1:43 pm ─
```

**Typography:**
- `You` label: 13px, `#555555`. Right-aligned, with a rule extending left. The learner's label is quieter — this is Alice's space, the learner is visiting.
- Message text: 18px, `#f0ede5` at 85% opacity. Slightly dimmer than Alice's messages — not dramatically different, but enough to distinguish at a glance.
- Timestamp: right-aligned, 12px, `#555555`.
- No left border accent. The absence of the amber stripe marks this as the learner's turn.

### 2d. Composing Indicator

When Alice is composing a response, a composing indicator occupies the Alice turn slot:

```
Alice  ────────────────────────────────────────────────────────

  ·  ·  ·
```

Three dots, amber, animated at 400ms intervals (dot 1 brightens, then 2, then 3, cycling). Not a spinner. Not "Alice is typing…". Just the three dots — understated, present.

The amber left border is present on the composing state as well. Alice's mark is there even while she thinks.

Duration: composing state shows for the actual response latency. If the response is instant (cached or near-instant), the composing state shows for a minimum of 600ms to prevent jarring message flash. Alice doesn't blurt.

---

## Section 3: Level Progress — Ambient Surface

### 3a. Principle

While in conversation, the learner should know:
1. Which level they're on
2. Which atom within the level
3. That there are more atoms ahead, or that this is the last one

They should not be thinking about this. It should be peripheral — like a page number in a book. You glance at it if you're curious. You don't stare at it.

### 3b. The Header Atom Indicator

```
← Journey          Level 3: Keys & Identity      atom 2 of 5
```

- Centered level name: 13px, `#555555`. Present but not dominant.
- Right-aligned atom count: `atom 2 of 5`, 12px, `#F4B844` at 50% opacity. Amber but quiet. The color says "Alice" — the opacity says "peripheral."
- On mobile, this compresses: `L3 · atom 2/5`, all 12px, right-aligned.
- No progress bar. No percentage. The count is enough.

### 3c. Atom Transition

When one atom resolves and the next begins, the atom counter updates with a minimal animation: the old count fades out (200ms), the new count fades in. No ceremony. The conversation moves; the indicator follows.

The transition is Alice-initiated — she moves to a new atom in her response. The UI doesn't anticipate or announce it. The counter updates after Alice's first message of the new atom.

### 3d. What an Atom Boundary Looks Like in the Conversation

Atoms are not announced. There's no "Atom 3: The Daemon begins now" banner. The conversation continues. The only visible signal is the counter changing. Alice's message naturally shifts to the next topic.

If a learner scrolls back and wants to know where one atom ended and another began, that information is not surfaced inline. The conversation reads as a unified thread, not a segmented tutorial. The atom is an internal unit for pacing and exit-criterion tracking — not a learner-facing chapter heading.

---

## Section 4: The Exit Criterion Moment

### 4a. How Alice Decides

Alice monitors the conversation for the exit criterion of the current atom: has the learner demonstrated sufficient understanding? When she determines yes, she closes the atom. When all atoms in a level are closed, she closes the level.

The learner never submits for grading. There is no "Check my answer" button. Alice reads the conversation and decides. This is the UX implication of that design: the interface cannot have a grading affordance, because there is no grading affordance to offer.

### 4b. The Atom Completion Beat

When Alice closes an atom, her next message includes a quiet acknowledgment before moving to the next topic:

```
Alice  ────────────────────────────────────────────────────────

"That's exactly right. The key doesn't prove who you are —
 it is you. Once you have it, no one can take that from you.

 Let's move to something that builds on this."

1:47 pm                              ────────────────────────
```

No banner. No confetti. No "Atom 2 complete ✓" toast. Alice acknowledges in her voice and moves forward. The atom counter increments. The conversation continues.

**Why no UI ceremony at the atom level:** Atoms are small. There are 5 per level, 13 levels. Celebrating every atom would be infantilizing — it would feel like a kindergarten sticker chart. The ceremony is reserved for the level.

### 4c. The Level Completion Ceremony

When Alice closes the last atom in a level, something does happen. Not a popup — a beat in the conversation itself.

**Alice's message:**

```
Alice  ────────────────────────────────────────────────────────

"You've got it. Every part of this.

 Keys and identity — you know what they are, why they matter,
 and what it means that yours exist on your machine and
 nowhere else.

 That's Level 3 done."

2:01 pm                              ────────────────────────
```

**After a 1.2s pause, the conversation area transitions:**

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│                         ✦                                        │ ← Amber glyph, fades in
│                                                                  │   over 600ms. Centered
│                         Level 3 Complete                         │   in the conversation area.
│                         Keys & Identity                          │
│                                                                  │
│         ──────────────────────────────────────────────          │ ← Thin amber rule
│                                                                  │
│                                                                  │
│   "Level 4 is about the daemon — the thing that makes your       │ ← Alice's voice, 18px
│    kingdom run. Ready when you are."                             │   fades in below the rule
│                                                                  │
│                                                                  │
│                         ┌────────────────┐                       │
│                         │ Continue ✦     │                       │ ← Gold button, centered
│                         └────────────────┘                       │
│                                                                  │
│     or: ← Return to your journey                                 │ ← Muted secondary option
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

This is the ceremony for a completed level. The conversation area clears of the input zone and fills with the completion moment. It is spatial — the learner pauses, takes in the moment, then chooses to continue or step back.

**Motion:**
- The `✦` glyph fades in first (600ms).
- Level title and name fade in 200ms after (staggered).
- Amber rule draws from center outward (400ms).
- Alice's preview message fades in 400ms after the rule.
- Button appears last (200ms fade, after Alice's message fully appears).

**The completion moment is written to disk by Alice before this screen appears.** The level-N-complete.md record exists. The PWA reads it and renders the screen. If the learner closes the tab at this exact moment and returns, they land on the journey screen, Level 3 marked complete, Level 4 available.

**"Continue ✦"** opens Level 4's conversation.  
**"← Return to your journey"** returns to Screen 2 (the level list), where the updated state is visible.

### 4d. Level 12 (Final Level) Completion

Level 12 completion is handled by the graduation flow defined in `2026-04-05-alice-graduation-certificate.md`. The level completion moment is still present, but "Continue ✦" transitions directly to the graduation arrival screen rather than a new level.

---

## Section 5: Interruption and Return

### 5a. The Learner Closes the Tab

When the learner closes the tab mid-conversation, nothing special happens in the UI. The conversation state is persisted to disk as each exchange occurs (not on close). Alice writes each exchange to the learner's conversation log at `~/.alice/learners/{uuid}/curricula/alice-onboarding/conversation.jsonl` as it happens.

There is no "Are you sure you want to leave?" modal. No progress-loss warning. The conversation is safe because it is always already saved.

### 5b. Returning to an Active Conversation

When the learner returns to the Alice page while a conversation is in progress:

```
┌─────────────────────────────────────────────────────────────────┐
│  ← Journey          Level 3: Keys & Identity      atom 2 of 5  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Earlier messages — full history scrollable above]             │
│                                                                  │
│  ─────────────────────────────────────────────────────────────  │ ← Time gap rule
│  Yesterday, 1:43 pm                                              │ ← Relative timestamp
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  Alice  ──────────────────────────────────────────────────────  │
│                                                                  │
│  "Welcome back, Jordan.                                          │ ← Alice acknowledges return
│                                                                  │
│   We were talking about what it means for your keys to          │
│   be your identity. Do you want to pick up from there,          │
│   or should I quickly recap?"                                    │
│                                                                  │
│  2:14 pm                              ─────────────────────────  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Type your answer, or ask Alice a question…               │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Time gap rule:**
- If the learner returns after more than 1 hour, a horizontal time separator appears in the conversation: a thin rule with a relative timestamp ("Yesterday, 1:43 pm" / "3 days ago" / "Last week") centered in the rule. This is the only visual signal of time passing. It is muted (rule: `#2a2a2a`, text: `#555555`).

**Alice's return acknowledgment:**
- Alice notices the gap and opens with a warm return message. This is Alice's doing — she generates this message based on where the conversation was paused.
- The return message is not a canned "Welcome back!" — it references the last topic. This is Alice's personality in the UI.
- Alice offers the learner two paths: continue from where they were, or get a recap. The learner can type either, or just continue naturally.
- If the gap is less than 30 minutes, Alice does not comment on the return. The conversation resumes as if uninterrupted.

**Scroll position on return:**
- The conversation scrolls to the bottom (the most recent exchange). The learner is placed in context immediately.
- The history is scrollable upward if they want to review earlier exchanges.

### 5c. What the Learner Sees if They Return to the Journey List

If the learner navigates to the Alice page and looks at the journey list (Screen 2) while a conversation is in progress, Level 3 shows:

```
◆ Level 3: Keys & identity     ← Current (amber, bright)
  In progress — atom 2 of 5
  
  [ Continue conversation ]    ← Amber button, inline
```

The "Continue conversation" button brings them directly into the conversation view, positioned at the bottom of the existing thread.

---

## Section 6: Multi-Device

### 6a. The Design Problem

Alice's learner data lives at `~/.alice/` on the learner's local machine. This is sovereign storage — the learner's device, their data. The conversation history, completion records, and certificate all live there.

But learners are not single-device people. They start on a desktop at home. They pick up on their phone on the train. They finish on a laptop at work.

The conversation must follow them. The question is: how?

### 6b. The Sync Model

Alice uses a **pull-based peer sync model**. No central server holds the canonical copy of a learner's data. Each device holds a complete copy. When multiple devices are in use, they sync directly (or via a relay if direct is not possible).

**Three sync modes, offered in order of sovereignty:**

**Mode 1: Same machine, same browser.**
No sync needed. `~/.alice/` is the single source. This is the happy path and the most common early case.

**Mode 2: Same koad:io account, multiple devices.**
The learner's koad:io daemon (when running) handles sync. The conversation log, completion records, and identity file are replicated across devices via the learner's kingdom. This is the standard path for learners who have installed koad:io.

This is the intended long-term model. Getting through Alice's curriculum is the path to understanding koad:io — so a learner who has completed enough levels will likely have the daemon running. Sync becomes available precisely when it's most needed.

**Mode 3: No daemon — manual export/import.**
For learners early in the curriculum who don't yet have koad:io running on all devices:

```
┌─────────────────────────────────────────────────────────────────┐
│  Continue on another device                                      │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  Your progress lives on this device. To continue on another:    │
│                                                                  │
│  1.  Export your progress pack from this device.                 │
│      [ Download progress.alice ]  ← ~4KB encrypted archive      │
│                                                                  │
│  2.  On your other device, open Alice and import it:             │
│      [ Import progress ] (available on the Alice welcome screen) │
│                                                                  │
│  Your conversation history and completion records will           │
│  transfer. Your display name and learner ID will carry over.     │
│                                                                  │
│  "This is a temporary path. Once you have your kingdom           │
│   running, your progress syncs automatically."   — Alice        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

The `progress.alice` file is a small encrypted archive: conversation log, completion records, identity.md, and the certificate if earned. The encryption key is the learner's UUID itself (sufficient for this use case — this is not high-security data, just personal progress). No server involved.

**The PWA welcome screen has an "Import progress" option** in the corner — small, unobtrusive, for learners who know they need it. It is not in the primary flow.

### 6c. What Alice Says About Multi-Device

Alice doesn't make sync an alien concept. When a learner first asks about continuing on another device (or when Alice detects the conversation was last active on a different device signature), she explains it naturally:

> "Your progress lives on your device — that's what makes it yours. If you want to continue somewhere else, I can give you a progress pack to carry across. Or, once you have your kingdom running, it'll sync on its own. That's actually something we'll talk about in Level 6."

This is Alice's voice in the UI: she doesn't duck the architecture. She names it, grounds it in the curriculum, and offers the practical path. The design supports this by surfacing the export tool wherever the conversation might lead to it.

### 6d. Import Flow on a New Device

When a learner opens Alice for the first time on a new device and imports a `progress.alice` file:

```
┌─────────────────────────────────────────────────────────────────┐
│  Alice                                                           │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  "I found your progress from your other device.                  │
│                                                                  │
│   Welcome back, Jordan.                                          │
│                                                                  │
│   You're on Level 3, atom 2. Let's pick up from there."         │
│                                                                  │
│                         ┌────────────────┐                       │
│                         │ Continue ✦     │                       │
│                         └────────────────┘                       │
│                                                                  │
│  or: Start fresh with a new learner ID                           │ ← Rare case, offered
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

No friction. No re-authentication. Alice reads the imported data, addresses the learner by name, and opens the conversation at the correct position.

---

## Section 7: Alice's Voice in the Visual Design

### 7a. Personality Through Typography

Alice is patient. Her text breathes. The line height (1.65) is wider than the portal's tight monospace rhythm. Paragraphs have generous spacing between them. When Alice writes a short, declarative sentence — "Your keys are you. Not your data. You." — the whitespace around it gives it room to land.

Alice does not rush. When a message has two or three short paragraphs, they are separated by a full blank line in the rendered text. This is intentional. The formatting mirrors the pace of a person who thinks before speaking.

### 7b. Timing as Expression

| Moment | Timing |
|--------|--------|
| Composing indicator appears | After 200ms latency (never immediate — Alice pauses) |
| Composing minimum display | 600ms (Alice doesn't blurt) |
| Message text renders | Instant — but the composing indicator's minimum holds the beat |
| Atom transition indicator | 200ms fade out, 200ms fade in |
| Level completion ceremony | Staged over ~2.5s total (see Section 4c) |
| Return acknowledgment | Appears 800ms after page load (Alice noticed the return) |

These delays are not "loading" — they are rhythm. The 600ms composing minimum exists so that even fast responses arrive with the feeling that Alice considered them.

### 7c. The Amber Left Border as Heartbeat

Every Alice message carries a 2px amber left border at 30% opacity. On a dark background, this is subtle — not a loud bracket, not a highlighted block quote. It's just there.

The effect: scanning down a long conversation, the learner sees the amber thread on the left wherever Alice spoke. Their own messages have no border. The conversation visually encodes whose voice is whose without requiring labels to be read.

On the composing state, the amber border is present but the opacity drops to 15% — Alice's mark is there, but quiet while she thinks.

### 7d. Input Tone

The input placeholder text is written in Alice's voice:

- On a content atom: `"Type your answer, or ask Alice a question…"`
- On an open-ended reflection prompt: `"What are you thinking?"`
- On an assessment atom: `"Show Alice what you know."`
- After Alice asks a direct question: `"Your answer…"`

These rotate based on the atom type, set by the curriculum content layer. The placeholders are Alice speaking — not UI copy.

### 7e. Alice's Name Marker

The `Alice` label above each of her message blocks is the only "avatar" she has. No image. No icon. No circle with initials. Just her name, in amber, followed by a horizontal rule that extends to the right edge of the conversation column.

This is the visual equivalent of Alice leaning forward to speak. The rule draws the eye across the column — "something begins here." Her name is the anchor.

If in the future Alice gains a visual identity beyond her name (a glyph, a sigil), that element would go here. The slot is reserved. For now, her name is enough.

### 7f. Silence After the Exit Criterion

When the level completion ceremony begins (Section 4c), the input zone disappears. The learner cannot type. For the duration of the ceremony — roughly 2.5 seconds of staged animation — Alice has the floor completely. There is nothing for the learner to do except receive the moment.

This is intentional silence. The absence of the input zone is not an error state or a loading state. It is Alice saying: this moment is yours, just take it.

---

## Section 8: Accessibility

**Conversation navigation:**
- Tab order: header link → conversation area (scroll focus) → input → send → helpers.
- All timestamps have `aria-label` with full datetime for screen readers (not the visual "1:42 pm" short form).
- Alice turn and learner turn have `role="article"` with `aria-label="Alice" / "You"`.
- The composing indicator has `aria-live="polite"` with text "Alice is composing a response" (not the visual dots, which are `aria-hidden`).
- Level completion ceremony has `aria-live="assertive"` so screen readers announce the completion event.

**Color and contrast:**
- All body text (#f0ede5 on #0a0a0a): contrast 16.5:1, AAA.
- Muted text (#555555 on #0a0a0a): contrast 4.6:1, AA (acceptable for supplementary text at 12px).
- Amber (#F4B844 on #0a0a0a): contrast 8.2:1, AAA.
- The amber left border on Alice's messages is decorative — it carries no information that isn't also conveyed by the `Alice` label.

**Motion:**
- All staged animations (ceremony, composing transitions) respect `prefers-reduced-motion`. When set: composing indicator shows as static text "…"; ceremony renders instantly with no staged fade.
- No looping animations except the composing dots. These stop when the message arrives.

**Input:**
- Enter key sends the message (standard behavior).
- Shift+Enter inserts a newline.
- Escape key clears the input.
- The `← Journey` link returns to the level list — always accessible from keyboard.

---

## Section 9: Component Summary for Vulcan

```
<AliceConversation>
  ├── <ConversationHeader />
  │     ├── <JourneyLink />           // "← Journey" amber link
  │     ├── <LevelTitle />            // Current level name, muted center
  │     └── <AtomProgress />          // "atom 2 of 5", ambient right-aligned
  │
  ├── <ConversationThread />
  │     ├── <AliceTurn />             // Amber label, amber left border, message text
  │     ├── <LearnerTurn />           // Muted "You" label, right-rule, message text
  │     ├── <ComposingIndicator />    // Three amber dots, min 600ms display
  │     ├── <TimeGapRule />           // Separator for sessions > 1hr apart
  │     └── <NewMessagePill />        // "↓ New message" when scrolled up
  │
  ├── <LevelCompletionCeremony />     // Full-screen staged moment
  │     ├── <CompletionGlyph />       // ✦ amber, fades in
  │     ├── <CompletionTitle />       // "Level 3 Complete / Keys & Identity"
  │     ├── <CompletionRule />        // Amber rule draws from center
  │     ├── <NextLevelPreview />      // Alice's bridging message
  │     └── <CompletionActions />     // "Continue ✦" + "← Return to your journey"
  │
  └── <ConversationInputZone />
        ├── <MessageInput />          // Expanding textarea, dynamic placeholder
        ├── <SendButton />            // Amber → icon, active on non-empty input
        ├── <GlossaryHelper />        // Pill button, opens inline glossary
        └── <ContextHelper />         // Pill button, opens context recall
```

**State Alice writes (conversation layer):**
- `~/.alice/learners/{uuid}/curricula/alice-onboarding/conversation.jsonl` — append-only conversation log, one JSON line per exchange
- Each entry: `{ "ts": ISO-8601, "role": "alice"|"learner", "text": "...", "level": N, "atom": N }`

**State Vulcan reads:**
- Conversation log (for rendering thread on load)
- Completion records (for gating and progress indicators)
- Identity file (for display_name in return acknowledgment and header)

**State Vulcan does NOT write:**
- It does not write to the conversation log. Alice writes each exchange as it completes.
- It does not write completion records. Alice writes those.
- It reads everything; it writes nothing in `~/.alice/`.

---

## Section 10: Open Questions (Deferred to Implementation)

These are design decisions deferred to the implementation phase, not blocking the spec:

1. **Conversation log encryption.** The conversation log on disk is currently plaintext. For learners who want privacy on shared machines, an at-rest encryption option using the learner's UUID as key is a natural extension. Not required for v1.

2. **Alice's recap generation.** The return acknowledgment message references the last topic. This requires Alice to generate contextual text from the conversation log. The UX is specified; the generation mechanism is Alice's responsibility (not Vulcan's).

3. **Atom type schema.** The dynamic input placeholder (Section 7d) requires atom-type metadata in the curriculum content. Chiron's curriculum format should include an `atomType` field. If not present, Vulcan falls back to the default placeholder.

4. **Progress pack encryption key.** Using the UUID as the encryption key for the `progress.alice` export is sufficient for v1. A more robust key derivation scheme (UUID + device fingerprint) is a v2 consideration.

5. **Offline first.** The PWA should function fully offline once loaded — the conversation log and completion records are on disk. Service worker caching scope for Alice assets is a Vulcan implementation detail.

---

**Design Direction:** Muse  
**Date:** 2026-04-05  
**Status:** Ready for Vulcan implementation — extends alice-ui-design-brief.md Screen 3
