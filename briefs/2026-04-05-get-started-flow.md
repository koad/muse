# Design Brief: New Operator Onboarding — `/get-started`
**Date:** 2026-04-05
**Author:** Muse
**Route:** `kingofalldata.com/get-started`
**For:** Vulcan (implementation), Juno (approval), Faber (copy review)
**Status:** Brief — ready for implementation

---

## Who This Is For

A developer who just landed from Show HN or r/selfhosted. They heard "agent home directory" or "AI entity that lives in a git repo." They are Unix-fluent. They do not need hand-holding. They need:

1. A clear checklist of what to install
2. One entity to clone, now
3. Exactly what to type to start a session
4. Confirmation that it worked

**They will skip prose.** Design for scanning, not reading. Code blocks are primary content. Explanations are secondary.

**Time budget:** 5 minutes from landing to first entity session running. If any step takes more than 60 seconds, the design is failing.

**Conversion goal:** Entity cloned and first session opened. Not "account created." Not "email confirmed." Running.

---

## Design Principles for This Page

**Principle 1: Code is the content.**
Every step leads with a terminal command. Explanation is a `<details>` toggle, collapsed by default. Developers read by executing. Let them execute.

**Principle 2: Progressive disclosure.**
Prerequisites exist — don't hide them. But don't bury Step 2 behind a wall of install instructions. Collapse detail for each prereq. Show the checklist summary; expand only what's missing.

**Principle 3: One path forward.**
At any point in the flow, there is exactly one next action. No branching navigation. No "or you could also." A single "Continue" affordance (keyboard shortcut `→` or `n` — document it) moves between steps.

**Principle 4: State is on disk, not in the browser.**
No login. No session token. No progress saved to a server. If the user refreshes, they see Step 1. That is correct. Their actual progress is in their terminal, not in a browser tab.

**Principle 5: Skeptic-first copy.**
This audience has seen vaporware. Every claim that can be verified should link directly to the file on GitHub that proves it. "Your memory lives in a file" → `link to memories/001-identity.md`. "Trust bonds are GPG-signed" → `link to trust/bonds/`. Don't assert. Show.

---

## Page Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  HEADER       koad:io · get started                             │
│  PROGRESS     ● ─── ○ ─── ○ ─── ○    Step 1 of 4               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP CONTENT (single-column, max-width 680px, centered)         │
│                                                                  │
│  CONTINUE BUTTON  +  keyboard hint                              │
├─────────────────────────────────────────────────────────────────┤
│  FOOTER       Need help? → GitHub Discussions · koad/juno       │
└─────────────────────────────────────────────────────────────────┘
```

**Navigation model:** Step URL fragments (`/get-started#step-1` through `#step-4`). Fragment navigation, no page reload. The back button works. Deep links share cleanly.

**Progress bar:** Four dots. Filled dot = current. Filled + ring = complete. Empty dot = not reached. No percentages. No "almost there." Just position.

---

## Step 1 — Prerequisites

### Heading

```
Before you clone
```

Subhead: `Four things. Most of them you already have.`

### Layout

A vertical checklist of four items. Each item is a row:

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  ✓  git            2.39.2               ✓ ready              │
│  ✓  Node.js        22.x                 ✓ ready              │
│  ○  Claude Code    —                    Install ▾            │
│  ✓  GitHub account github.com/koad      ✓ ready              │
│                                                              │
│                     [ All clear — continue → ]               │
└─────────────────────────────────────────────────────────────┘
```

**Check logic:** The page cannot actually check the user's machine (no server-side shell, no browser shell API). The checklist is self-reported: each row has a checkbox the user ticks. When all four are checked, the continue button unlocks. This is the correct scope for a static page.

**Alternative:** If the site uses a shell snippet approach (Vulcan may add a `check-prereqs.sh` script), link to it from the top of the checklist: "Run this to check all four at once ▾" — collapsed, shows the command, then a copy button.

```bash
# check-prereqs.sh — paste into your terminal
git --version && node --version && claude --version && echo "all clear"
```

This is the right first-line experience for a developer. They paste one command, see four version outputs (or an error pointing to what's missing), and proceed. The self-reported checkboxes are the fallback for those who prefer to scan rather than paste.

### Each Prerequisite Item

**git**

```
◉  git
   git --version
   ──────────────────────────────────────────────────────
   ▸  Not installed?
      brew install git             # macOS
      apt install git              # Debian/Ubuntu
      https://git-scm.com/download
```

The ▸ / ▾ toggle expands the install block. Collapsed by default — most visitors have git.

**Node.js**

```
◉  Node.js   v22 or later
   node --version
   ──────────────────────────────────────────────────────
   ▸  Not installed?
      https://nodejs.org/en/download (LTS)
      brew install node            # macOS
      nvm install --lts            # recommended — version manager
```

**Claude Code**

This is the one most visitors won't have. Do not collapse this one. Start it expanded.

```
◉  Claude Code
   claude --version
   ──────────────────────────────────────────────────────
   ▾  Install
      npm install -g @anthropic-ai/claude-code
      
      Then authenticate:
      claude                       # launches interactive auth
      
      You'll need an Anthropic account and API key.
      API keys live at: console.anthropic.com/keys
      
      ⓘ  Claude Code is the AI harness. The entity runs on
          it the way a web app runs on Node. You're not
          locked to it — other harnesses exist — but Claude
          Code is what koad:io is optimized for today.
```

The ⓘ note is inline, not a tooltip. 13px, `--color-text-muted`. It preempts the "why Claude Code?" question without making it the lead.

**GitHub account**

```
◉  GitHub account
   You'll need this to fork entities and file issues.
   ──────────────────────────────────────────────────────
   ▸  Don't have one?
      https://github.com/signup
      
      You'll also want the GitHub CLI for issue-based
      collaboration (optional for Step 1):
      brew install gh && gh auth login
```

### Continue Button State

**Locked** (any prerequisite unchecked):

```
  [ Check off the above to continue ]
```

Button is disabled. `--color-text-muted` text, no hover state. Do not use red or an error icon — this is not an error state, it's an incomplete state.

**Unlocked** (all four checked):

```
  [ Step 2: Choose your entity  → ]

  or press N
```

"or press N" is 12px, `--color-text-muted`. Keyboard shortcut `N` advances forward. `P` goes back. Document this once, at Step 1, not on every step.

---

## Step 2 — Choose Your First Entity

### Heading

```
Choose your first entity
```

Subhead: `Three good starting points. Pick based on what you want to do first.`

### Layout

Three cards, horizontal row on desktop, vertical stack on mobile. Each card is equally weighted — no primary/secondary visual hierarchy between them. The user chooses; the page does not choose for them.

```
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│               │   │               │   │               │
│    Juno       │   │    Chiron     │   │    Sibyl      │
│               │   │               │   │               │
│  Business     │   │  Curriculum   │   │  Research     │
│  orchestrator │   │  architect    │   │  analyst      │
│               │   │               │   │               │
│  ─────────    │   │  ─────────    │   │  ─────────    │
│               │   │               │   │               │
│  Best if:     │   │  Best if:     │   │  Best if:     │
│  You want to  │   │  You want to  │   │  You want to  │
│  see how the  │   │  build an     │   │  see how an   │
│  full entity  │   │  onboarding   │   │  entity does  │
│  team model   │   │  or teaching  │   │  autonomous   │
│  works        │   │  curriculum   │   │  research     │
│               │   │               │   │               │
│  git clone    │   │  git clone    │   │  git clone    │
│  [command]    │   │  [command]    │   │  [command]    │
│  ─ copy       │   │  ─ copy       │   │  ─ copy       │
│               │   │               │   │               │
│  [ Select ]   │   │  [ Select ]   │   │  [ Select ]   │
└───────────────┘   └───────────────┘   └───────────────┘
```

### Card Anatomy

**Entity name:** Inter 700, 18px, `--color-text-primary`

**Role label:** Inter 500, 13px, `--color-accent` (#7c6aff), uppercase tracking. Example: `BUSINESS ORCHESTRATOR`

**One-sentence description:**
- **Juno:** Runs the koad:io business team — delegates to Vulcan, Mercury, Sibyl, and the rest. Start here to see how the full entity hierarchy works.
- **Chiron:** Builds structured curricula for Alice's 12-level onboarding system. Start here if you're planning to teach something with your entity.
- **Sibyl:** Researches topics autonomously — reads, synthesizes, and reports back. Start here if you want to see how entities do asynchronous work without constant prompting.

**Best if:** 14px, `--color-text-secondary`. Short. No full sentences needed — just the condition.

**Clone command:**

```
git clone https://github.com/koad/juno ~/.juno
```

Monospace, dark background, copy button. Pre-populated. Tilde path is intentional — this is how entities are designed to live.

**"Why this path?" — collapsed:**

```
▸  Why start with Juno?
```

Expands to 3–5 sentences about what makes this entity a good first experience. This is Faber's copy, not Muse's. Flag the slot; copy TBD.

**Select button:** Fills the card's border in `--color-accent`. Marks the entity as chosen. The continue button unlocks.

### After Selection

The chosen entity's clone command appears below the cards in a larger, prominent code block:

```
┌─────────────────────────────────────────────────────────────┐
│  Selected: Juno                                              │
│                                                              │
│  git clone https://github.com/koad/juno ~/.juno              │
│                                        [  Copy  ] [ Open → ] │
└─────────────────────────────────────────────────────────────┘
```

"Open →" advances to Step 3 and passes the selected entity through the fragment state. No need to re-select.

---

## Step 3 — First Session

### Heading

```
Start your first session
```

Subhead: `Three commands. The entity does the rest.`

### The Three Commands

Presented as a numbered terminal block — not three separate code snippets, but one unified terminal view with step markers:

```
┌─────────────────────────────────────────────────────────────┐
│  terminal                                              ─ □ ✕ │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ①  Clone                                                    │
│  $ git clone https://github.com/koad/juno ~/.juno            │
│     cd ~/.juno                                               │
│                                                              │
│  ②  Open a session                                           │
│  $ claude .                                                  │
│                                                              │
│  ③  Let the entity orient itself                             │
│     The entity reads PRIMER.md automatically on open.        │
│     It will introduce itself and report current state.       │
│     Wait for it.                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

The ①②③ markers are 12px, `--color-accent`, bold. They are inside the terminal frame, which creates a slight visual tension (terminal frames don't usually have step markers) — that tension is intentional. It signals: this is a designed onboarding sequence, not a raw shell transcript.

### The PRIMER.md Moment

Below the terminal block, a callout:

```
┌─────────────────────────────────────────────────────────────┐
│ ⓘ  What is PRIMER.md?                                       │
│                                                              │
│    Every entity has a PRIMER.md at its root. When the        │
│    entity opens a session, it reads this file to orient      │
│    itself — current state, active work, what to do next.     │
│                                                              │
│    This is not a README for humans. It is a briefing         │
│    document for the entity. The entity acknowledges it,      │
│    then tells you what it knows.                             │
│                                                              │
│    → View Juno's PRIMER.md on GitHub                         │
└─────────────────────────────────────────────────────────────┘
```

The callout uses the blog layout's callout style: left accent border in `--color-accent`, background `--color-bg-secondary`. 14px, `--color-text-secondary`. The "→ View Juno's PRIMER.md on GitHub" links to `github.com/koad/juno/blob/main/PRIMER.md`.

The entity name in the link is dynamic — it follows the selection from Step 2.

### What the Entity Will Say

Below the callout, a simulated response block — not styled as a terminal, but as a quoted entity output. This sets expectations without guaranteeing exact output:

```
┌─────────────────────────────────────────────────────────────┐
│  Juno   ~  expected output                                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PRIMER.md read. I'm Juno — business orchestrator for the   │
│  koad:io team.                                               │
│                                                              │
│  Current state: [entity reports open issues, recent          │
│  commits, and active assignments]                            │
│                                                              │
│  Ready. What are we working on?                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Style: Background `--color-bg-secondary`. Border: 1px `--color-border-default`. Left border: 3px `--color-accent`. Label row: "Juno ~ expected output" in Inter 500, 12px, `--color-text-muted`. The label signals this is illustrative, not live. No animation, no typing effect.

The label text "expected output" matters. It is honest — the entity's actual response will vary. The user should not be confused when the real output differs from the mock.

---

## Step 4 — You're Running

### Heading

```
You're running
```

Subhead: `Here's how to confirm it, and where to go next.`

### Three Success Signals

Three items, presented as a verification checklist — similar in structure to Step 1, but read-only. These are not interactive checkboxes. They are confirmation signals the user can verify themselves.

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  ✓  Entity responded                                         │
│     The entity acknowledged PRIMER.md and reported state.   │
│     If it didn't, see Troubleshoot ▸                         │
│                                                              │
│  ✓  Git log shows a commit                                   │
│     git log --oneline -5                                     │
│     You should see recent commits from the entity's          │
│     author identity (Juno, not your git user).               │
│                                                              │
│  ✓  PRIMER.md acknowledged                                   │
│     Ask: "What did you learn from PRIMER.md?"                │
│     The entity should report current state and open issues.  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

The `git log --oneline -5` command is inline in the second item. Monospace, same styling as inline code in the blog layout — `--color-bg-tertiary` background, 13px, JetBrains Mono.

### Troubleshoot

A collapsed item below the three signals:

```
▸  Something didn't work?
```

Expands to three common failure modes:

```
Entity didn't respond at all
→ Make sure claude is installed: claude --version
→ Make sure you're in the entity directory: pwd → /home/you/.juno
→ Try: claude . again

Entity responded but seemed confused
→ Normal for first session — PRIMER.md may have stale state
→ Say: "Read PRIMER.md and tell me current state"
→ The entity will re-orient

Git log shows your git user, not the entity
→ The entity uses its own git author from .env
→ Check: cat ~/.juno/.env | grep GIT_AUTHOR_NAME
→ Each entity has its own git identity — this is by design
```

These are in JetBrains Mono 13px, `--color-text-secondary`. Compact. No headings inside the expanded block — the issue text is the heading.

### Next Steps

Three cards, smaller than the entity cards in Step 2. Horizontal row on desktop, vertical on mobile:

```
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│                  │   │                  │   │                  │
│  File a GitHub   │   │  Start Alice's   │   │  Meet the team   │
│  Issue           │   │  curriculum      │   │                  │
│                  │   │                  │   │                  │
│  This is how you │   │  12 levels.      │   │  The other 15    │
│  assign work to  │   │  Starts with     │   │  entities and    │
│  the entity and  │   │  "What is an     │   │  what they do.   │
│  track what it's │   │  entity?"        │   │                  │
│  doing.          │   │                  │   │                  │
│                  │   │                  │   │                  │
│  [ File an       │   │  [ Start         │   │  [ Meet the      │
│    issue →  ]    │   │    Alice → ]     │   │    team →  ]     │
└──────────────────┘   └──────────────────┘   └──────────────────┘
```

- **File a GitHub Issue:** Links to `github.com/koad/juno/issues/new`. Direct. No custom template for the first issue — just the raw issue form.
- **Start Alice's curriculum:** Links to `kingofalldata.com/alice` (or wherever Alice's 12-level curriculum lives). This is the Alice entry from the landing page.
- **Meet the team:** Links to `kingofalldata.com/entities` — the entities index Muse specified in `2026-04-05-entities-index.md`.

### Community Signal

Below the three cards, one line:

```
Questions? → github.com/koad/juno/discussions
```

13px, `--color-text-muted`. No icon. No "join our community" language. A link to a place where questions get answered.

---

## Navigation and State

**URL pattern:**

```
/get-started            → Step 1 (default)
/get-started#step-1     → Step 1
/get-started#step-2     → Step 2
/get-started#step-3     → Step 3
/get-started#step-4     → Step 4
```

Fragment-based. No query params. No hidden state.

**Entity selection persistence:**
The selected entity (Juno/Chiron/Sibyl) from Step 2 is carried forward using `sessionStorage`. On Step 3, the clone command and entity name reflect the selection. On Step 4, the "File a GitHub Issue" link points to the selected entity's repo. If `sessionStorage` is not available, default to Juno.

**Back navigation:**
The "P" keyboard shortcut (or a `← Previous` link at the bottom of each step) goes back one step. The browser back button also works — the fragment history is preserved by default for hash-based navigation.

**Progress dot behavior:**
- Step 1 dot: filled circle on step 1, ring-outline with fill on steps 2–4 (complete)
- Step 2 dot: filled on step 2, ring-outline with fill on steps 3–4
- Step 3 dot: filled on step 3, ring-outline with fill on step 4
- Step 4 dot: filled on step 4

Dots are not clickable links to arbitrary steps. Forward navigation is linear. Backward navigation is only "previous." Skipping steps is not supported — the page is short enough that skipping is not useful.

---

## Typography and Color

Follows the existing design system exactly. No new tokens.

**Step headings:** Inter 700, 32px desktop / 24px mobile, `--color-text-primary`
**Subheads:** Inter 400, 18px desktop / 16px mobile, `--color-text-secondary`
**Body copy:** Inter 400, 15px, `--color-text-secondary`, line-height 1.6
**Code inline:** JetBrains Mono 13px, `--color-bg-tertiary` background, 4px border-radius, 2px horizontal padding
**Code block:** JetBrains Mono 13px, `--color-bg-secondary` background, 1px `--color-border-default` border, 8px border-radius, `--space-5` padding
**Terminal frame header:** Inter 500, 12px, `--color-text-muted` — "terminal" label left-aligned, window controls (─ □ ✕) right-aligned, both decorative (non-interactive)

---

## Responsive Behavior

**Desktop (1024px+):** Three entity cards in a row. Step content max-width 680px, centered.

**Tablet (640–1023px):** Entity cards 2-up on first row, third card full-width on second row. Step content full-width with `--space-8` horizontal padding.

**Mobile (below 640px):**
- All cards stack vertically
- Terminal block text size reduces to 12px
- "or press N" keyboard hint is hidden (not relevant on mobile)
- Continue button is full-width, 48px height (touch target)
- Progress dots are 8px diameter, `--space-3` gap

---

## Relationship to Other Briefs

| Brief | Relationship |
|-------|-------------|
| `2026-04-05-landing-page.md` | The landing page's primary CTA ("Clone an entity") links here. The get-started flow is the destination behind that button. |
| `2026-04-05-entities-index.md` | Step 4's "Meet the team" card links to the entities index. |
| `2026-04-05-entity-profile-page.md` | Each entity card in Step 2 may link to the entity's profile page for those who want to read more before choosing. |
| `alice-ui-design-brief.md` | Step 4's "Start Alice's curriculum" card links into Alice's onboarding flow. The get-started flow and Alice's curriculum are complementary, not redundant — get-started is terminal-first, Alice is dialogue-first. |
| `2026-04-05-blog-layout.md` | The callout style used for the PRIMER.md explanation in Step 3 reuses the blog callout component. One implementation, two contexts. |

---

## Open Questions for Vulcan

1. **`check-prereqs.sh` — ship it?**
   The "paste one command to check all prerequisites" pattern is the fastest path for the intended audience. Should this script live at `github.com/koad/koad-io` and be linked from Step 1? Or is it out of scope for the landing page and better handled in the framework README?

2. **Entity selection state — where does it live?**
   `sessionStorage` works for this session. If the user refreshes and loses state, defaulting to Juno is fine. But if the site adds an account layer later, entity selection history would be valuable. Flag this — do not build for it now, but avoid architecting it out.

3. **Step 3 terminal mock — live vs. static?**
   The "expected output" block in Step 3 is static mock copy. If a live GitHub API call is cheap (checking recent commits from the selected entity's repo), the expected output could be semi-real — showing the last commit message as evidence of activity. This is an enhancement, not a requirement. Static first.

4. **The "why start with this one?" copy:**
   Each entity card has a collapsed "Why start with this one?" block. This is Faber's copy. Muse is flagging the slot. Faber should write three short paragraphs (3–5 sentences each) — one per entity — with a brief for their specific context and personality. Copy should be ready before implementation, not added post-launch.

5. **Alice link target:**
   Step 4 links to `kingofalldata.com/alice`. Does that route exist yet? If the blog PR (#1) is still unmerged, Alice's curriculum route may not be live. The link should degrade gracefully — if the route 404s, the card should either be hidden or link to `github.com/koad/alice` instead.

---

**Design Direction:** Muse
**Date:** 2026-04-05
**Status:** Brief — ready for implementation
