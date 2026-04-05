# Chiron Curriculum Browser — Design Spec

**Status:** Complete
**Date:** 2026-04-05
**Audience:** Vulcan (PWA implementation), Chiron (curriculum format alignment), Juno (approval)
**Entity:** Muse
**References:** 2026-04-05-alice-conversation-ui.md, alice-ui-design-brief.md (Screen 2), Chiron SPEC.md, Chiron level-00.md through level-12.md, koad/vulcan#36

---

## Overview

This brief specifies the curriculum browser: the surfaces that let a learner see the full alice-onboarding journey, understand where they are in it, enter or resume a level, and navigate atom structure within a conversation. It is the bridge between orientation (the full map) and immersion (the conversation view).

The conversation view is fully specified in `2026-04-05-alice-conversation-ui.md`. This document specifies everything before and between those conversations: the map of the whole journey, the entry card for each level, how atom navigation surfaces inside the conversation, and how completion and locking are communicated.

The curriculum has 13 levels (0 through 12) and 60 atoms total. Levels gate sequentially from Level 1 onward — Level 4 requires completion of Levels 1, 2, and 3. Level 0 and Level 1 are both available to any new learner. The UI must communicate this structure without overwhelming someone who just arrived.

---

## Design Principles (Curriculum Browser — Specific)

These extend the Alice UI Design Brief principles. They govern everything in this document.

**The map is orientation, not gamification.** The curriculum browser shows the learner where they are, what's ahead, and what's available. It does not award badges, display streaks, or show percentages. It does not compete with the conversation for the learner's attention — it serves them when they need orientation, then sends them back into the conversation.

**Locking is a fact, not a punishment.** Level 5 is locked because Level 4 isn't finished. That's information, presented plainly. The UI communicates this without drama: a muted state, a clear prerequisite note. Curiosity about what's locked is welcome; frustration about being blocked is avoidable.

**Alice's color is amber.** Every progress indicator, active state, and completion mark uses `#F4B844`. This is Alice's presence in the layout, even when the conversation isn't open.

**Prose descriptions, not tags or chips.** Each level entry has a name and a sentence describing what it covers. Not keyword chips. Not topic tags. A sentence — written in the same voice as the curriculum itself.

**No grading, no scoring.** Completion is binary: done or not done. Alice determined it. The UI shows done/not-done and nothing else. No score, no percentage, no "you got 3 of 4 atoms" breakdown.

**Mobile-first.** The map view must work at 375px viewport width. Every affordance specified below has been designed for mobile first, then extended for desktop.

---

## Section 1: Curriculum Map View

### 1a. Purpose and Entry

The curriculum map is Screen 2 in the Alice UI Design Brief. This document fully specifies it.

The learner reaches the map by:
- Arriving at the Alice page for the first time
- Tapping `← Journey` from within a conversation
- Returning after a session gap (the PWA opens here if no conversation is in progress)

The map shows the full 13-level journey on one scrollable surface. It is spatial: the learner can see what they've done, where they are, and what's ahead — all at once, without navigating between screens.

### 1b. Full-Screen Layout (Desktop)

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│   alice                                                              │ ← Identity mark
│   ────────────────────────────────────────────────────────────────  │ ← Thin rule
│   koad:io Human Onboarding                                           │ ← Curriculum title
│   13 levels  ·  ~4.5 hours  ·  60 atoms                             │ ← Curriculum metadata
│                                                                      │
│                                                                      │
│   ── completed ──────────────────────────────────────────────────   │ ← Section divider
│                                                                      │
│   ✦ Level 0    The First File                      10 min  3 atoms  │ ← Completed level
│   ✦ Level 1    First Contact — What Is This?       15 min  4 atoms  │
│   ✦ Level 2    What Is an Entity?                  20 min  5 atoms  │
│                                                                      │
│   ── in progress ────────────────────────────────────────────────   │ ← Section divider
│                                                                      │
│   ◆ Level 3    Your Keys Are You                   20 min  5 atoms  │ ← Current level
│                atom 2 of 5 · in progress                            │   (amber, bright)
│                [ Continue conversation ]                             │
│                                                                      │
│   ── ahead ──────────────────────────────────────────────────────   │ ← Section divider
│                                                                      │
│   · Level 4    How Entities Trust Each Other       35 min  7 atoms  │ ← Unlocked, not started
│   · Level 5    Commands and Hooks                  20 min  4 atoms  │
│   · Level 6    The Daemon and the Kingdom          25 min  5 atoms  │
│   · Level 7    Peer Rings                          20 min  4 atoms  │
│   · Level 8    The Entity Team                     20 min  4 atoms  │
│   · Level 9    GitHub Issues                       18 min  4 atoms  │
│   · Level 10   Context Bubbles                     20 min  4 atoms  │
│   · Level 11   Running an Entity                   25 min  5 atoms  │
│                                                                      │
│   ── locked ─────────────────────────────────────────────────────   │ ← Section divider
│                                                                      │
│   ○ Level 12   The Commitment                      25 min  4 atoms  │ ← Locked level
│                Requires Level 11                                     │   (muted, open ring)
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

Note on sections: the "ahead" section only appears if there are unlocked-but-not-started levels between the current and the next locked level. If the learner has not started at all, "in progress" is absent. If the learner has completed everything through Level 11 and Level 12 is locked, "in progress" is absent. The section structure adapts to the learner's actual state.

**Level row anatomy:**
- Status glyph (left): `✦` completed (amber), `◆` in progress (amber, bright), `·` ahead (muted), `○` locked (muted)
- Level number + title: 15px, `#f0ede5` for available/in-progress, `#333333` for locked
- Metadata right: estimated minutes and atom count, 12px, `#555555`
- Progress line (in-progress level only): `atom N of M · in progress`, 12px, `#F4B844` at 60% opacity — appears below the level title, indented to the title's left edge
- Action (in-progress level only): `[ Continue conversation ]` — small amber button, inline below the progress line

**Section dividers:**
- Three states: "completed", "in progress", "ahead", "locked"
- Thin rule (`#1a1a1a`) with the label centered in it, 11px, `#444444` — low contrast, serves as organization not as header

**The ✦ glyph:** The same amber diamond used in the conversation completion ceremony. On the map it marks every completed level. The visual continuity means: what you earned in the ceremony is what you see on the map. The glyph is Alice's — it represents her assessment that this level is done.

### 1c. Mobile Layout (375px)

```
┌─────────────────────────────────────┐
│  alice                              │
│  ─────────────────────────────────  │
│  koad:io Human Onboarding           │
│  13 levels · ~4.5 hrs               │
│                                     │
│  ── completed ──────────────────    │
│                                     │
│  ✦  L0   The First File        10m  │
│  ✦  L1   First Contact         15m  │
│  ✦  L2   What Is an Entity?    20m  │
│                                     │
│  ── in progress ────────────────    │
│                                     │
│  ◆  L3   Your Keys Are You     20m  │
│       atom 2/5 · in progress        │
│       [ Continue ]                  │
│                                     │
│  ── ahead ──────────────────────    │
│                                     │
│  ·  L4   Trust Bonds           35m  │
│  ·  L5   Commands & Hooks      20m  │
│  ·  L6   Daemon & Kingdom      25m  │
│  ·  L7   Peer Rings            20m  │
│  ·  L8   The Entity Team       20m  │
│  ·  L9   GitHub Issues         18m  │
│  ·  L10  Context Bubbles       20m  │
│  ·  L11  Running an Entity     25m  │
│                                     │
│  ── locked ─────────────────────    │
│                                     │
│  ○  L12  The Commitment        25m  │
│       Requires L11                  │
│                                     │
└─────────────────────────────────────┘
```

Mobile compression:
- `Level N` → `LN` (abbreviated)
- Level full title may wrap to two lines at 375px — acceptable, no truncation
- Atom count drops from the row at 375px (present in the entry card instead)
- The `[ Continue conversation ]` button shortens to `[ Continue ]`
- Section divider text remains, but rule extends only to container edge

### 1d. A New Learner's Map (First Arrival)

When the learner has not started anything, the map is simpler:

```
── available ──────────────────────────────────────────────────────
                                                                  
  ·  Level 0    The First File                     10 min  3 atoms
  ·  Level 1    First Contact — What Is This?      15 min  4 atoms
                                                                  
── ahead ──────────────────────────────────────────────────────────
                                                                  
  ·  Level 2    What Is an Entity?                 20 min  5 atoms
  ·  Level 3    Your Keys Are You                  20 min  5 atoms
     [... levels 4 through 12 ...]
```

Both Level 0 and Level 1 are available without prerequisites. They both appear in the top section with the `·` glyph (not yet started, but available). The remaining levels appear in "ahead" at reduced opacity — visible, legible, but not the focus.

**Why show the whole journey on first arrival:** The learner deserves to know what they're committing to before they start. Showing all 13 levels, with time estimates, answers the question "how long is this?" without requiring them to ask. Seeing the full journey makes Level 12 feel like a real destination rather than something that appears once they earn it.

### 1e. Curriculum Header

```
alice
──────────────────────────────────────────────────────
koad:io Human Onboarding
13 levels  ·  ~4.5 hours  ·  60 atoms
```

- `alice` in amber (`#F4B844`), 13px. This is her name marking the space — same as her name marker in the conversation view.
- Thin amber rule below her name: `#F4B844` at 20% opacity. Quiet.
- Curriculum title: 20px, `#f0ede5`. The only large text on this screen.
- Metadata line: 12px, `#555555`. Level count, estimated total time, total atom count. Factual. No "Start your journey!" copy.

The curriculum header does not change as the learner progresses. It always shows the full scope of the curriculum. The learner's progress is communicated by the level rows below it, not by the header.

---

## Section 2: Level Entry Card

### 2a. Purpose

When a learner taps a level row in the map, a level entry card appears. This is the bridge between seeing the level on the map and entering the conversation. It gives the learner enough context to begin with intention: what they're about to learn, how long it will take, what is expected of them, and (if returning) where they left off.

The entry card is a full-screen overlay, not a modal dialog. It has its own back button and a clear primary action.

### 2b. Layout — Unlocked Level, Not Started

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ← Back to journey                                                   │ ← Back link, muted
│                                                                      │
│  Level 4                                                             │ ← Level number, 13px amber
│  How Entities Trust Each Other                                       │ ← Level title, 24px
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │ ← Thin rule
│                                                                      │
│  35 min  ·  7 atoms                                                  │ ← Metadata, muted
│                                                                      │
│  Trust bonds are the authorization layer of koad:io. In this        │ ← Learning objective,
│  level you'll learn what a trust bond is, why bonds are signed       │   prose, 16px
│  files rather than database records, and what it means for a        │
│  bond to authorize something.                                        │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  What Alice expects                                                  │ ← Exit criteria label,
│                                                                      │   12px, muted
│  By the end, you should be able to describe a trust bond in         │ ← Prose exit criterion,
│  your own words and explain why bonds are signed.                    │   15px
│                                                                      │
│                                                                      │
│                         ┌──────────────────┐                         │ ← Primary action
│                         │  Begin Level 4 ✦ │                         │   centered, amber
│                         └──────────────────┘                         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**Learning objective copy:** Written in plain English by Chiron, drawn from the level's learning objective field. Not the same as the YAML `title` — a full sentence describing what the learner will be able to do afterward.

**Exit criteria copy:** A plain-language, single sentence derived from the level's exit criteria list. Not the full checklist — a prose synthesis. Alice's judgment is what matters; this tells the learner what they're aiming for without implying they need to hit a checkbox.

**"What Alice expects" label:** Small, muted. It is not "Requirements" or "You must be able to." It is "what Alice expects" — her framing, not a grading rubric.

**Primary button:** `Begin Level N ✦` — amber fill, centered, 16px. The `✦` glyph connects the action visually to the completion ceremony (where the same glyph appears). Starting a level and completing it are bookended by the same mark.

### 2c. Layout — Level In Progress (Returning)

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ← Back to journey                                                   │
│                                                                      │
│  Level 3                                                             │
│  Your Keys Are You                                                   │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  In progress  ·  atom 2 of 5  ·  started 2 days ago                 │ ← Progress metadata
│                                                                      │
│  Your keys are your cryptographic identity — not an account,         │ ← Learning objective
│  not a username. In this level you'll understand what that           │
│  means and why it cannot be taken from you.                          │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  Where you left off                                                  │ ← Return context label
│                                                                      │
│  You were on atom 2: "Your Key Is Your Identity."                    │ ← Atom name, quoted
│  Alice was asking about what happens when someone loses              │ ← Last exchange summary
│  their keys.                                                         │   (from conversation log)
│                                                                      │
│                                                                      │
│                         ┌──────────────────┐                         │
│                         │  Continue ✦      │                         │ ← Primary action
│                         └──────────────────┘                         │
│                                                                      │
│                         View full conversation                       │ ← Secondary action, muted
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**"Where you left off" section:** A two-line summary of the last exchange — the atom name and a brief description of where the conversation paused. This is generated by Alice from the conversation log on the return visit. It is not a static field; it requires Alice to read the log and summarize.

The atom name is quoted in light type. The following sentence is Alice's voice: "Alice was asking about…" — not "Last message:". The return is framed as an ongoing dialogue, not a record retrieval.

**"View full conversation":** A muted secondary link below the primary button. Takes the learner directly into the conversation view scrolled to the bottom, without Alice generating a return greeting. For learners who remember exactly where they were and just want to continue typing.

**Primary button text changes:** `Continue ✦` instead of `Begin Level N ✦`. When you're returning, you're continuing.

### 2d. Layout — Completed Level

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ← Back to journey                                                   │
│                                                                      │
│  ✦  Level 2  ·  Completed                                            │ ← Amber glyph + status
│  What Is an Entity?                                                  │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  20 min  ·  5 atoms  ·  completed 6 days ago                        │ ← Metadata with completion
│                                                                      │
│  "You can navigate ~/.alice/, explain what lives in each             │ ← Learner's own words,
│   directory, and describe why an entity's identity is built          │   if captured at completion
│   from files rather than server records."                            │
│                                                                      │
│                         ┌──────────────────┐                         │
│                         │  Review ↩        │                         │ ← Review action, muted
│                         └──────────────────┘                         │   amber outline (not fill)
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**Learner's own words:** If the exit criterion conversation included a moment where the learner articulated the level's core idea in their own words (which Alice records), that is surfaced here as a pull-quote. This is their record of understanding, not a system-generated summary. The quotation marks make clear it is their voice.

If no such quote is available in the log, this section is omitted — no placeholder, no gap indicator.

**Review button:** Amber outline (not fill). Not a primary action. The learner can review the conversation, but the presumption is they're moving forward. Reviewing a completed level is an available choice, not the default.

### 2e. Mobile Entry Card

The entry card is full-screen on mobile. The same sections appear in the same order. The learning objective wraps naturally to the viewport width. The `← Back to journey` link is always visible at the top. The primary button is at the bottom, fixed if the content is long enough to require scrolling.

---

## Section 3: Atom Navigation Within Conversation

### 3a. The Ambient Surface (Already Specified)

The `alice-conversation-ui.md` specifies the ambient atom counter in the conversation header:

```
← Journey          Level 3: Your Keys Are You      atom 2 of 5
```

This is the primary atom navigation affordance during a live conversation. The counter updates when Alice transitions to the next atom. No further atom navigation surface is needed during an in-progress conversation.

### 3b. Can the Learner See Upcoming Atoms?

No. Upcoming atoms within a level are not surfaced in the conversation view. The learner sees their current position (`atom 2 of 5`) but not the names or topics of atoms 3, 4, and 5.

**Why:** The curriculum is designed as a guided dialogue, not a chapter-by-chapter syllabus. If the learner can see "Atom 4: Operational Verification" coming, they might try to jump ahead in the conversation, skip Alice's questions, or pre-answer without genuinely working through the intermediate steps. Alice's pacing is the pacing. Revealing the full atom list would undermine that.

The atom count (`of 5`) tells the learner there are 5 atoms. They know roughly how far they are. That is enough ambient information without spoiling the conversation structure.

**The exception:** The level entry card shows the learning objective — what the learner will be able to do after the level — but not the atom list. This gives intentionality without roadmapping the conversation.

### 3c. Can Learners Navigate Back to a Previous Atom?

Learners can scroll back through the conversation to read earlier exchanges in any atom. The conversation is a scrollable document; nothing is hidden.

What learners cannot do: jump Alice back to a previous atom's topic via navigation UI. There is no "go back to atom 1" button. If the learner wants to revisit something, they type it. "I want to go back to what you said about keys being identity" — Alice responds. The navigation is conversational, not mechanical.

**Why:** The conversation is the artifact. Mechanical atom navigation would imply that atoms are discrete menu items rather than a flowing dialogue. Alice decides when an atom is complete; she can also be asked to return to a topic if the learner needs it. That is a more natural and respectful interaction than a back-button.

### 3d. Atom Progress Peek (Optional Surface — Deferred)

A deferred design option, not included in v1:

A learner could hold down (long-press) the atom counter to see a pop-up list of all atoms in the current level with their names, the current atom highlighted, and completed atoms marked. This would require Chiron's atom format to include a short display name for each atom.

This is available as a v2 addition if user testing reveals learners want more orientation. In v1, the counter is ambient and that is sufficient.

---

## Section 4: Completion States

### 4a. Completed Level in the Map

A completed level in the map view:

```
✦ Level 2    What Is an Entity?                 20 min  5 atoms
```

- `✦` in amber (`#F4B844`), 14px
- Level number: 11px, amber, lighter weight
- Level title: 15px, `#f0ede5`, standard weight
- Metadata (time, atoms): 12px, `#555555`
- No special background. No green bar. No checkmark badge. The `✦` is enough.

The entire row is tappable. It leads to the completed level entry card (Section 2d).

**Why no additional ornamentation:** The `✦` is Alice's glyph — it appeared in the level completion ceremony, it marks the moment in the conversation, and it marks the level on the map. That continuity is the design. Adding another layer of completion indicator (a green background, a progress ring, a checkmark) would dilute the meaning of the glyph and clutter the list.

### 4b. Completed Curriculum State

When a learner completes Level 12 (the final level), the graduation flow handles the ceremony (specified in `2026-04-05-alice-graduation-certificate.md`). After that flow, the learner returns to the map. The map's completed-curriculum state:

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  alice                                                               │
│  ────────────────────────────────────────────────────────────────   │
│  koad:io Human Onboarding                                            │
│  13 levels  ·  4.5 hours  ·  60 atoms  ·  ✦ Complete               │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  ✦ Level 0     The First File                      10 min  3 atoms  │
│  ✦ Level 1     First Contact — What Is This?       15 min  4 atoms  │
│  ✦ Level 2     What Is an Entity?                  20 min  5 atoms  │
│  ✦ Level 3     Your Keys Are You                   20 min  5 atoms  │
│  ✦ Level 4     How Entities Trust Each Other       35 min  7 atoms  │
│  ✦ Level 5     Commands and Hooks                  20 min  4 atoms  │
│  ✦ Level 6     The Daemon and the Kingdom          25 min  5 atoms  │
│  ✦ Level 7     Peer Rings                          20 min  4 atoms  │
│  ✦ Level 8     The Entity Team                     20 min  4 atoms  │
│  ✦ Level 9     GitHub Issues                       18 min  4 atoms  │
│  ✦ Level 10    Context Bubbles                     20 min  4 atoms  │
│  ✦ Level 11    Running an Entity                   25 min  5 atoms  │
│  ✦ Level 12    The Commitment                      25 min  4 atoms  │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  [ View your certificate ]                                           │ ← Amber button, left-aligned
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

Changes from the in-progress map:
- Metadata line gains `·  ✦ Complete` — the only addition. Everything else is the same.
- The three-section structure (completed / in progress / ahead) collapses to a single flat list. All 13 rows, all marked `✦`. No section dividers needed; they served a purpose that no longer exists.
- A single action appears below the list: `[ View your certificate ]`. This is a quiet amber button — not a ceremony (the ceremony already happened), just an available path for the learner who wants to return to their certificate.

**Why no additional completion ceremony on the map:** The graduation flow was the ceremony. The map, afterward, is a record. It should be still and clear, not another celebration. The learner can look at 13 `✦` glyphs and feel the weight of that without the UI telling them to feel it.

---

## Section 5: Locked Level Affordance

### 5a. The Design Problem

A locked level must communicate: you cannot enter this yet. It must do so without:
- Making the learner feel punished
- Hiding the level's existence or content preview
- Creating a "wall" aesthetic that signals hostile gatekeeping
- Using jargon ("you need N points" / "unlock with completion")

### 5b. Locked Level in the Map

```
○  Level 12   The Commitment                     25 min  4 atoms
              Requires Level 11
```

- `○` open ring glyph, `#444444` — visually suggests "not yet filled"
- Level number and title: `#333333` — present but receded, notably dimmer than the available levels at `#f0ede5`
- Metadata (time, atoms): `#2e2e2e` — barely visible; the learner can read it but it is not calling for attention
- Prerequisite note: `Requires Level 11` — 11px, `#444444`, indented below the title. Short. Plain. Not "LOCKED — complete previous levels first."

The entire row is tappable. Tapping a locked level opens a locked level entry card (Section 5c). It does not produce a blocking modal or an error. The level opens; it just opens in a different state.

**Why show locked levels at all:** The learner deserves to see the full shape of the journey. Hiding Level 12 until it's available would be paternalistic. Showing it — visibly receded, clearly marked as ahead — invites the learner to be curious about what's coming. "The Commitment" as a level title is interesting. The learner may wonder what that means. That wonder is a motivator, not a wall.

**The `○` glyph:** Open ring — the negative space of `✦`. Visual vocabulary that connects locked (ring) to completed (glyph) in the same family. The filled version (completion) feels like the destination of the empty version (locked). The learner subconsciously reads: that will be filled someday.

### 5c. Locked Level Entry Card

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ← Back to journey                                                   │
│                                                                      │
│  ○  Level 12                                                         │ ← Open ring glyph, muted
│  The Commitment                                                      │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  25 min  ·  4 atoms                                                  │ ← Metadata, muted
│                                                                      │
│  This level is the culmination of the curriculum. You'll make a      │ ← Learning objective,
│  cryptographically signed commitment to operating with               │   prose, available to read
│  sovereignty — the same kind of commitment that anchors every        │
│  trust bond in the system.                                           │
│                                                                      │
│  ──────────────────────────────────────────────────────────────────  │
│                                                                      │
│  To begin this level, complete Level 11 first.                       │ ← Plain prerequisite,
│                                                                      │   12px, muted
│                                                                      │
│                         ┌──────────────────────┐                     │ ← Navigate to Level 11
│                         │  ← Go to Level 11    │                     │   amber outline button
│                         └──────────────────────┘                     │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**The locked card shows the full learning objective.** This is intentional. The learner should know what they're working toward — reading it might be the thing that motivates them to complete the prerequisite. Gatekeeping the description itself would be unnecessarily restrictive.

**The action button navigates to the prerequisite level.** It does not show a disabled "Begin Level 12" button with a tooltip. It shows `← Go to Level 11` — directing the learner toward what they can do, not toward what is blocked. The affordance is forward-pointing, not wall-indicating.

**"To begin this level, complete Level 11 first."** Plain sentence. No alert icon. No red text. No lock icon graphic. Just the sentence. The sentence is enough.

### 5d. Levels 0 and 1 — The Open Entry Points

Level 0 and Level 1 have no prerequisites. On the map, both show as `·` (available, not started) for a new learner. The locked affordance never applies to them.

If a learner somehow navigates to Level 1's entry card without having completed Level 0 — for instance, by jumping directly to a URL — they simply see Level 1's entry card with `Begin Level 1 ✦`. Level 0 is recommended but not technically gated.

---

## Section 6: State Data Vulcan Reads

The curriculum browser reads from Alice's learner state at `~/.alice/learners/{uuid}/curricula/alice-onboarding/`. Vulcan reads; Alice writes.

```
~/.alice/learners/{uuid}/curricula/alice-onboarding/
├── progress.json          ← Level and atom completion state
├── conversation.jsonl     ← Full conversation log (used for "where you left off")
├── certificate.md         ← Written by Alice on Level 12 completion
└── certificate.md.asc     ← Alice's Ed25519 signature over the certificate
```

**progress.json structure (what Vulcan reads):**

```json
{
  "curriculum_id": "a9f3c2e1-7b4d-4e8a-b5f6-2d1c9e0a3f7b",
  "learner_uuid": "...",
  "levels": {
    "0": { "status": "complete", "completed_at": "2026-04-03T14:22:00Z", "atoms_complete": 3 },
    "1": { "status": "complete", "completed_at": "2026-04-03T14:44:00Z", "atoms_complete": 4 },
    "2": { "status": "complete", "completed_at": "2026-04-04T10:11:00Z", "atoms_complete": 5 },
    "3": { "status": "in_progress", "started_at": "2026-04-04T10:15:00Z", "current_atom": 2, "atoms_complete": 1 },
    "4": { "status": "available" },
    "5": { "status": "available" },
    "12": { "status": "locked", "requires": [11] }
  }
}
```

**Curriculum map rendering logic:**

1. For each level (0–12), read status from progress.json
2. `complete` → `✦` glyph, full brightness, completed at timestamp for entry card
3. `in_progress` → `◆` glyph, full brightness, current_atom for progress line and entry card
4. `available` → `·` glyph, muted
5. `locked` → `○` glyph, dimmed, requires array for prerequisite note

**"Where you left off" (entry card, in-progress levels):**

Vulcan reads the last N lines of conversation.jsonl to find the learner's last exchange. The atom name comes from the curriculum spec for the current atom index. The exchange summary is generated by Alice on the return visit (not statically stored).

---

## Section 7: Motion and Timing

The curriculum browser uses the same motion philosophy as the conversation view: purposeful, not decorative.

| Transition | Timing | Notes |
|------------|--------|-------|
| Map page load | Instant render | No staggered animation; content is orientation, not presentation |
| Completed levels appearance on load | Instant | Already earned; not re-presented as achievement |
| Level entry card open (tap on row) | 200ms slide up from bottom | Sheet pattern; the row the learner tapped stays visible above |
| Level entry card close (back tap) | 200ms slide down | Returns to map; map position preserved |
| Map section dividers | Render with content | No animated appearance |
| ✦ on completed level (first render after ceremony) | Fade in 400ms | Only on the first map load after completing a level; subsequent loads instant |
| Locked level entry card | Same slide-up as entry card | No additional animation; the open ring glyph does not animate |

**`prefers-reduced-motion`:** All slide transitions become instant cuts. The `✦` fade on first appearance becomes instant. Everything functions identically; just without motion.

---

## Section 8: Accessibility

**Map view:**
- Each level row: `role="listitem"` within a `role="list"`. The list has `aria-label="Alice curriculum levels"`.
- Level row `aria-label`: `"Level 4: How Entities Trust Each Other. 35 minutes. 7 atoms. Available."` — status word at the end.
- Locked row `aria-label`: includes `"Locked. Requires Level 11."` at the end.
- In-progress row `aria-label`: includes `"In progress. Atom 2 of 5."` at the end.
- Completed row `aria-label`: includes `"Complete."` at the end.
- Status glyphs (`✦`, `◆`, `·`, `○`) are `aria-hidden`. The status information is carried by the `aria-label`, not the glyph.

**Entry card:**
- `role="dialog"` with `aria-label` matching the level title.
- Focus moves into the card on open; returns to the level row on close.
- Primary button is always the last focusable element before close (natural tab order).

**Color contrast:**
- Available level text (`#f0ede5` on `#0a0a0a`): 16.5:1, AAA
- Locked level text (`#333333` on `#0a0a0a`): 2.5:1 — this is intentionally low contrast to communicate muted state; the `aria-label` carries the accessibility information
- Muted metadata (`#555555` on `#0a0a0a`): 4.6:1, AA
- Amber glyphs (`#F4B844` on `#0a0a0a`): 8.2:1, AAA

Note on locked level contrast: WCAG AA requires 4.5:1 for text. The `#333333` locked level title falls below this. The design rationale is that the muted appearance communicates "not yet available" and the `aria-label` provides full accessible text. Vulcan should confirm with Alice's accessibility review whether an alternative solution is needed (e.g., `#3a3a3a` which reaches 3.1:1 and may be acceptable for large decorative text if the accessible label is complete).

---

## Section 9: Component Summary for Vulcan

```
<CurriculumMap>
  ├── <CurriculumHeader />
  │     ├── <AliceNameMark />        // "alice" in amber, matching conversation header
  │     ├── <CurriculumTitle />      // "koad:io Human Onboarding"
  │     └── <CurriculumMeta />       // "13 levels · ~4.5 hours · 60 atoms [· ✦ Complete]"
  │
  ├── <LevelSection label="completed" />    // conditionally rendered
  ├── <LevelSection label="in progress" />  // conditionally rendered
  ├── <LevelSection label="ahead" />        // conditionally rendered
  ├── <LevelSection label="locked" />       // conditionally rendered
  │
  ├── <LevelRow />                  // one per level, variant: complete/in-progress/available/locked
  │     ├── <StatusGlyph />         // ✦ ◆ · ○
  │     ├── <LevelTitle />
  │     ├── <LevelMeta />           // time + atoms
  │     ├── <ProgressLine />        // in-progress levels only
  │     └── <ContinueButton />      // in-progress levels only
  │
  └── <CurriculumCompleteAction />  // "View your certificate" — complete state only


<LevelEntryCard variant="not-started|in-progress|complete|locked">
  ├── <BackLink />                  // "← Back to journey"
  ├── <LevelIdentifier />           // "Level N" + status glyph
  ├── <LevelTitle />
  ├── <LevelMetaLine />             // time · atoms [· completion/start date]
  ├── <LearningObjective />         // prose paragraph
  ├── <ExitCriterionSummary />      // "What Alice expects" — not-started/in-progress only
  ├── <WhereYouLeftOff />           // in-progress only
  ├── <LearnersOwnWords />          // complete only, if available from log
  ├── <PrerequisiteNote />          // locked only
  └── <PrimaryAction />             // Begin / Continue / Review / Go to prerequisite
```

---

## Section 10: Open Questions (Deferred to Implementation)

1. **"Where you left off" generation.** The entry card for an in-progress level shows the last exchange topic. Generating that summary requires Alice to read the conversation log and produce one sentence. The UX is specified; the generation mechanism is Alice's responsibility.

2. **Atom display names in Chiron's format.** Section 3d (atom peek, deferred v2) and the entry card's "where you left off" atom name reference require a short display name per atom. Chiron's current format uses atom slug (e.g., `1.1`, `1.2`) with a full heading. A `display_name` field (max 40 characters) per atom would support these surfaces without requiring the full heading to be truncated by the UI.

3. **Locked level contrast.** See Section 8 — the `#333333` locked text is below WCAG AA. Confirm acceptable threshold with Alice's a11y review.

4. **Learner's own words capture.** The completed level entry card shows the learner's words if captured. This requires Alice to tag a specific exchange in the conversation log as "learner articulation of level objective." The tagging mechanism is Alice's responsibility to specify.

5. **"Ahead" section collapsibility.** If a learner is on Level 4, the "ahead" section contains 8 levels. On mobile, this is a long scroll. A v2 option: collapse "ahead" to 3 levels with a "Show all 8 levels ahead" expansion link. Not included in v1 — show all.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Ready for Vulcan implementation — extends alice-ui-design-brief.md Screen 2
