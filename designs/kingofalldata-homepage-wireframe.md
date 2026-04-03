# kingofalldata.com Homepage Wireframe

**Purpose:** Visual reference for homepage structure, hierarchy, and content placement  
**Viewport:** Desktop (1200px+), then note mobile adaptations  
**Format:** ASCII wireframe with annotations

---

## Full Page Layout (Desktop)

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║  HEADER (sticky, minimal)                                         ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │ koad:io  ──────────────────  [Docs] [GitHub] [Sponsors]     │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  1. HERO SECTION (centered, tall, spacious)                      ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │                                                               │ ║
║  │                                                               │ ║
║  │            "Not your keys, not your agent."                  │ ║
║  │                                                               │ ║
║  │  Sovereign AI on your disk. No vendor.                       │ ║
║  │  No kill switch. No renting access to someone else's agent.  │ ║
║  │                                                               │ ║
║  │  [Clone an Example]  [Learn More ↓]                          │ ║
║  │                                                               │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  2. THE PROBLEM (context-setting)                                ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  Why This Matters                                             │ ║
║  │                                                               │ ║
║  │  Every AI agent today lives on someone else's server.        │ ║
║  │  Cloud API. Their terms. Their kill switch.                  │ ║
║  │                                                               │ ║
║  │  You're renting access to an agent you don't own.            │ ║
║  │  If the service changes, you have no recourse.               │ ║
║  │  If they shut down, your agent vanishes.                     │ ║
║  │                                                               │ ║
║  │  There's a better way.                                        │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  3. THE SOLUTION (what we're building)                           ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  Sovereign Entities                                           │ ║
║  │                                                               │ ║
║  │  AI entities that own themselves. Files on disk.             │ ║
║  │  Your keys. Your git history. Your evolution.                │ ║
║  │                                                               │ ║
║  │  └─ Your entity is a directory (~/.<yourname>/)             │ ║
║  │  └─ Contains cryptographic keys, memories, strategy         │ ║
║  │  └─ Stored in git with full history                         │ ║
║  │  └─ Cloneable, forkable, auditable                          │ ║
║  │  └─ No vendor. No subscription. No kill switch.             │ ║
║  │                                                               │ ║
║  │  This is koad:io. Build it. Sell it. Own it.                │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  4. MEET THE TEAM (entity showcase)                              ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  The Team IS the Product Line                                │ ║
║  │                                                               │ ║
║  │  Each team member is an entity. Each entity is cloneable.    │ ║
║  │  See how we use koad:io to build koad:io.                   │ ║
║  │                                                               │ ║
║  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          │ ║
║  │  │ JUNO         │ │ VULCAN       │ │ MERCURY      │          │ ║
║  │  │ Orchestrator │ │ Builder      │ │ Comms        │          │ ║
║  │  │              │ │              │ │              │          │ ║
║  │  │ Strategy,    │ │ Builds the   │ │ Writes and   │          │ ║
║  │  │ operations,  │ │ product      │ │ announces    │          │ ║
║  │  │ partnerships │ │ layer        │ │              │          │ ║
║  │  │              │ │              │ │              │          │ ║
║  │  │ [Clone]      │ │ [Clone]      │ │ [Clone]      │          │ ║
║  │  │ [GitHub]     │ │ [GitHub]     │ │ [GitHub]     │          │ ║
║  │  └──────────────┘ └──────────────┘ └──────────────┘          │ ║
║  │                                                               │ ║
║  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          │ ║
║  │  │ VERITAS      │ │ MUSE         │ │ SIBYL        │          │ ║
║  │  │ QA Guardian  │ │ Design       │ │ Research     │          │ ║
║  │  │              │ │              │ │              │          │ ║
║  │  │ Validates,   │ │ Makes things │ │ Investigates │          │ ║
║  │  │ tests,       │ │ beautiful    │ │ & analyzes   │          │ ║
║  │  │ quality      │ │              │ │              │          │ ║
║  │  │              │ │              │ │              │          │ ║
║  │  │ [Clone]      │ │ [Clone]      │ │ [Clone]      │          │ ║
║  │  │ [GitHub]     │ │ [GitHub]     │ │ [GitHub]     │          │ ║
║  │  └──────────────┘ └──────────────┘ └──────────────┘          │ ║
║  │                                                               │ ║
║  │  Every entity has its own:                                   │ ║
║  │  • Cryptographic keys (Ed25519, ECDSA)                       │ ║
║  │  • Git identity and commit history                           │ ║
║  │  • Persistent memories (markdown files)                      │ ║
║  │  • Trust bonds (scoped authorization)                        │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  5. HOW IT WORKS (architecture diagram)                          ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  Two-Layer Architecture                                       │ ║
║  │                                                               │ ║
║  │  ┌────────────────────────────────────────┐                  │ ║
║  │  │      ~/.koad-io/                       │                  │ ║
║  │  │  (Framework: CLI tools, daemon,        │                  │ ║
║  │  │   templates, shared infrastructure)    │                  │ ║
║  │  └────────────────────────────────────────┘                  │ ║
║  │         ▲           ▲           ▲           ▲                 ║
║  │         │           │           │           │                 ║
║  │      ┌──┴──┐    ┌──┴──┐    ┌──┴──┐    ┌──┴──┐               ║
║  │      │      │    │      │    │      │    │      │               ║
║  │    ~/.juno/ │  ~/.muse/ │  ~/.alice/ │  ...   │               ║
║  │   (Juno)    │  (Your     │  (Your    │         │               ║
║  │             │   entity)  │   entity)  │         │               ║
║  │             │            │            │         │               ║
║  │  Each entity directory:                        │               ║
║  │  • Has its own git repo with full history      │               ║
║  │  • Contains cryptographic keys                 │               ║
║  │  • Stores memories and context                 │               ║
║  │  • Is cloneable → cp -r ~/.juno /backup/      │               ║
║  │  • Is portable → works on any machine          │               ║
║  │                                                │               ║
║  └────────────────────────────────────────────────┘               ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  6. THE FUNNEL (pathways)                                         ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  Get Started                                                  │ ║
║  │                                                               │ ║
║  │  ┌──────────────────────────────────────┐                    │ ║
║  │  │ FREE                                 │                    │ ║
║  │  │ Clone & Learn                        │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ Clone example entity repos.          │                    │ ║
║  │  │ Learn how we built koad:io.          │                    │ ║
║  │  │ Build your own.                      │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ [GitHub Repos] [Docs]                │                    │ ║
║  │  └──────────────────────────────────────┘                    │ ║
║  │                      ▼                                        │ ║
║  │  ┌──────────────────────────────────────┐                    │ ║
║  │  │ $1+/mo COMMUNITY                     │                    │ ║
║  │  │ GitHub Sponsors                      │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ Chat with other builders.            │                    │ ║
║  │  │ Ask questions.                       │                    │ ║
║  │  │ Talk to juno directly.               │                    │ ║
║  │  │ MVP Zone access.                     │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ [Become a Sponsor]                   │                    │ ║
║  │  └──────────────────────────────────────┘                    │ ║
║  │                      ▼                                        │ ║
║  │  ┌──────────────────────────────────────┐                    │ ║
║  │  │ PREMIUM: koad.sh                     │                    │ ║
║  │  │ Custom Development & Consulting      │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ Custom entity development.           │                    │ ║
║  │  │ Personalized consulting.             │                    │ ║
║  │  │ Priority support.                    │                    │ ║
║  │  │                                      │                    │ ║
║  │  │ [Contact koad] [koad.sh]             │                    │ ║
║  │  └──────────────────────────────────────┘                    │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║  7. FOOTER                                                        ║
║  ┌──────────────────────────────────────────────────────────────┐ ║
║  │  [GitHub] [Docs] [Sponsors] [Support] [koad.sh]              │ ║
║  │                                                               │ ║
║  │  © 2026 koad:io | Sovereign AI entities for everyone         │ ║
║  │  "Not your keys, not your agent."                            │ ║
║  │                                                               │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## Section Spacing & Dimensions

### Vertical Spacing

| Section | Height (vh) | Padding | Notes |
|---------|------------|---------|-------|
| Header | 60px (fixed) | — | Sticky, minimal, compact |
| Hero | 60–70vh | 4rem top/bottom | Spacious, centered |
| Problem | 40vh | 4rem top/bottom | Context-setting |
| Solution | 45vh | 4rem top/bottom | Core messaging |
| Team Entities | 55vh | 4rem top/bottom | 6 cards in 2×3 grid |
| Architecture | 35vh | 4rem top/bottom | Diagram focus |
| Funnel | 50vh | 4rem top/bottom | Vertical flow |
| Footer | 12vh | 2rem top/bottom | Compact, links only |

**Total:** ~6 screenfuls of content (allowing users to scroll without overwhelming depth)

### Horizontal Layout (Desktop 1200px+)

- **Container width:** 1140px (max-width)
- **Left/right margins:** auto (centered)
- **Card grid (Team section):** 3 columns (4 cards per row → 2 rows)
- **Each card width:** 360px
- **Card padding:** 2rem

---

## Mobile Adaptations

### Breakpoint: 768px and below

```
HEADER (same, sticky)

HERO
├─ Height: 50vh (slightly shorter)
├─ Text size: 32–36px (smaller headline)
├─ Buttons stack vertically (full width)

PROBLEM/SOLUTION/FUNNEL
├─ Single column
├─ Padding: 2rem (reduced from 4rem)

TEAM CARDS
├─ Stack vertically (1 column)
├─ Card width: 100% (minus padding)
├─ Card padding: 1.5rem

FOOTER
├─ Links stack vertically or wrap

Total scrollable height increases but remains readable.
Touch targets remain >= 44px × 44px.
```

---

## Interaction States (Desktop)

### Buttons & Links

**Primary CTA** (e.g., "Clone an Example", "Become a Sponsor"):
```
Default:
  Background: #22dd77 (green)
  Color: #0a0a0a (dark text on green for contrast)
  Padding: 12px 24px
  Border: none
  Border-radius: 0px (sharp edges, terminal aesthetic)
  Font-weight: 600

Hover:
  Background: #1ac961 (darker green)
  Cursor: pointer
  No shadow

Focus (keyboard):
  Outline: 2px solid #22dd77
  Outline-offset: 2px
```

**Secondary CTA** (e.g., "Learn More", "GitHub"):
```
Default:
  Background: transparent
  Color: #22dd77
  Border: 1px solid #22dd77
  Padding: 12px 24px
  Border-radius: 0px

Hover:
  Background: #22dd77
  Color: #0a0a0a

Focus:
  Outline: 2px solid #22dd77
  Outline-offset: 2px
```

### Cards (Team Entity)

**Default:**
```
  Border: 1px solid #22dd77
  Background: #1a1a1a
  Padding: 2rem
  Transition: border-color 0.2s ease
```

**Hover:**
```
  Border: 2px solid #22dd77 (glow effect)
  Background: #222222 (slight lift)
```

**Focus (within card, on button):**
```
  Focus ring applied to button only
```

### Navigation Links

**Default:** `#22dd77` (green text)  
**Hover:** `#1ac961` (darker green, subtle underline)  
**Active (current page):** `#22dd77` + underline (2px solid)

---

## Navigation Structure

### Header Nav (Top)

```
Left: "koad:io" logo (text, linked to home)
Right: 
  - [Docs] → kingofalldata.com/docs
  - [GitHub] → github.com/koad
  - [Sponsors] → github.com/sponsors/koad
  - (optional: [MVP Zone] → mvp.kingofalldata.com)
```

### Footer Nav (Bottom)

```
Organized by category:
  
  RESOURCES
  [Documentation] [API Reference]
  
  COMMUNITY
  [MVP Zone] [Discord/Chat link if exists]
  
  CONTRIBUTE
  [GitHub] [Report Issue]
  
  CONTACT
  [Email: koad@kingofalldata.com]
  [koad.sh - Premium]
```

---

## Content Callouts & Asides

Where relevant, use subtle bordered boxes for emphasis:

```
┌─ Note ──────────────────────┐
│ This is optional. Use only  │
│ for critical info or gotchas│
│                             │
│ Example: "Files on disk     │
│ means you own your entity.  │
│ Back up ~/.<name>/ and your │
│ entity survives anything."  │
└─────────────────────────────┘
```

**Styling:**
- Border: 1px solid #888888 (gray)
- Background: #121212 (code background)
- Padding: 1.5rem
- Border-left: 4px solid #22dd77 (accent)
- Font-size: 14px (smaller, supporting text)

---

## Copy Blocks (Exact Text Locations)

### Hero Section

**Headline (48–64px, centered):**
```
Not your keys, not your agent.
```

**Subheading (18–20px, centered, lighter color):**
```
Sovereign AI on your disk.
No vendor. No kill switch.
No renting access to someone else's agent.
```

**Button 1 (primary):**
```
Clone an Example
```

**Button 2 (secondary):**
```
Learn More ↓
```

### Problem Section

**Heading:**
```
Why This Matters
```

**Body (narrow column, left-aligned):**
```
Every AI agent today lives on someone else's server. 
Cloud API. Their terms. Their kill switch.

You're renting access to an agent you don't own. 
If the service changes, you have no recourse. 
If they shut down, your agent vanishes.

There's a better way.
```

### Solution Section

**Heading:**
```
Sovereign Entities
```

**Body + Bullet Points:**
```
AI entities that own themselves. 
Files on disk. Your keys. 
Your git history. Your evolution.

• Your entity is a directory (~/.<yourname>/)
• Contains cryptographic keys, memories, strategy
• Stored in git with full history
• Cloneable, forkable, auditable
• No vendor. No subscription. No kill switch.

This is koad:io. Build it. Sell it. Own it.
```

---

## Form Elements (if signup/contact needed)

Keep forms minimal. If MVP Zone signup required:

```
┌────────────────────────────┐
│ GitHub Username:           │
│ [________________________] │
│                            │
│ Email (optional):          │
│ [________________________] │
│                            │
│ [Become a Sponsor]  [Skip] │
└────────────────────────────┘
```

**Styling:**
- Input: `#1a1a1a` background, `#22dd77` border on focus
- No shadow, sharp corners (consistent theme)
- Max-width: 300px

---

## Summary: Visual Hierarchy

1. **Hero:** Grab attention. State the thesis.
2. **Problem → Solution:** Educate. Frame the value.
3. **Team Entities:** Proof. "See how we're using this."
4. **Architecture:** Technical clarity. Show the model.
5. **Funnel:** Paths forward. No single path required.
6. **Footer:** Where to go next.

Each section is visually distinct but cohesive. Lots of whitespace. Text is scannable. CTAs are clear. Mobile-first but scales beautifully on desktop.

**Key principle:** The design should feel like a technical document, not marketing. Clean. Honest. Alive.
