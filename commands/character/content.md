# Muse Character System

Generates consistent character portraits and enables character-consistent image generation for all koad:io entities.

## Quick Start

```bash
# List available entities
muse character list

# Generate portrait for an entity
muse character portrait juno

# Generate new image with character consistency
muse character generate juno "queen juno at her command center"

# Generate all portraits
muse character generate-all
```

## Commands

### portrait

Generate a new portrait for an entity:

```bash
muse character portrait <entity> [--style cinematic|atmospheric|editorial|mystical]
```

Styles:
- `cinematic` (default) - Dramatic lighting, dark background
- `atmospheric` - Moody with volumetric lighting
- `editorial` - Magazine quality, sophisticated
- `mystical` - Ethereal with supernatural glow

### generate

Generate an image featuring a character with visual consistency:

```bash
muse character generate <entity> "<prompt>"
```

Uses Flux.2's reference image feature to maintain character identity.

### generate-all

Generate portraits for all 19 entities:

```bash
muse character generate-all
```

### list

Show all available entities and their status:

```bash
muse character list
```

## Directory Structure

```
~/.muse/
├── characters/
│   ├── juno/
│   │   ├── portrait-20260408-200943.png  # Generated portraits
│   │   ├── portrait-20260408-201403.png
│   │   └── profile.json                   # Character metadata
│   ├── vulcan/
│   ├── alice/
│   └── ...
├── commands/
│   └── character/
│       ├── command.sh
│       ├── portrait.py
│       ├── generate.py
│       └── profile.py
└── media/
    └── characters/
        └── juno-20260408-201551.png      # Generated consistent images
```

## Character Profiles

Each entity has a `profile.json` with:

```json
{
  "handle": "juno",
  "name": "Juno",
  "mythology": "Roman queen of the gods",
  "role": "Governance",
  "description": "Queen of the operation...",
  "keywords": ["operation", "business", "governance"],
  "outfit": {
    "hue": 222,
    "sat": 25,
    "light": 15,
    "palette": "brand"
  },
  "portraits": {
    "latest": "portrait-20260408-201403.png",
    "count": 2
  },
  "lora": {
    "trained": false,
    "file": null
  }
}
```

## Outfit System

Each character has an outfit defined by HSL values:

| Entity | Hue | Sat | Light | Palette |
|--------|-----|-----|-------|---------|
| juno | 222 | 25 | 15 | brand |
| vulcan | 20 | 30 | 20 | warm |
| alice | 45 | 40 | 30 | alice |
| ... | | | | |

The outfit colors are used in prompt generation to ensure visual consistency with the character's identity.

## Workflow

1. **Portrait Generation** → Create base portrait with outfit-aware coloring
2. **Profile Creation** → Store character metadata and portrait history
3. **Consistency Generation** → Use reference images for new poses/scenes
4. **LoRA Training** (future) → Train adapters for even stronger consistency

## API

Uses fal.ai Flux Pro API with:
- Prompt composition from outfit-aware fragments
- Reference image support via base64 encoding
- Automatic metadata storage alongside generated images
