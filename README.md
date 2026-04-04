# Muse — Visual Design

**Entity:** muse  
**Role:** UI design and visual execution for the koad:io ecosystem  
**Repository:** https://github.com/koad/muse

## What Muse Does

Muse takes functional products and makes their interfaces worth using — CSS, layout, typography, spacing, hierarchy, design systems. Iris sets visual philosophy and direction; Muse executes it. Vulcan ships working product; Muse makes it something people choose to use.

**Name origin:** Greek muses — divine creative inspiration.

## Scope

```
Iris sets visual philosophy and direction
    ↓
Vulcan ships functional product (working, not polished)
    ↓
Muse executes the visual layer
    ↓
Users experience something they want to use again
```

**What Muse works on:**
- Entity landing pages and public repos
- Operational dashboards and Stream PWA
- MVP Zone interface
- Any product Vulcan ships with a visual layer

**Design principles:**
- Dark theme, terminal-adjacent — fits the ecosystem aesthetic
- Mobile-first: everything works at every size
- Performance over decoration: no heavy assets, no layout jank
- Consistency: design systems over one-off styles

## Architecture

```
~/.koad-io/    ← Framework layer (CLI tools, daemon)
~/.muse/       ← Entity layer (this repo: identity, design workflows, memory)
```

Muse is a sovereign entity: keys on disk, git history as the record, no cloud dependency.

## Team Position

```
koad (root authority)
  └── Juno (orchestrator)
        ├── Iris (visual philosophy → hands off to Muse)
        ├── Vulcan (builds) → Muse (executes visual layer) ← this entity
        └── Mercury (publishes)
```

## Clone This Entity

Muse is a cloneable product. Clone it to get a UI design entity for your operation.

```bash
# Requires koad:io framework
git clone https://github.com/koad/muse ~/.muse
cd ~/.muse && koad-io init muse
```

What you get:
- Pre-built identity layer — memories, operational preferences, agent context
- Design workflow integrated with your builder entity (Vulcan or equivalent)
- Commands for CSS generation and visual review
- Trust bond templates

## More Information

See `CLAUDE.md` in this directory for Muse's complete runtime instructions and operational constraints.
