# muse lora

Train LoRA adapters for consistent character generation.

## Commands

### train

Train a LoRA for a specific entity:

```bash
muse lora train <entity> [--trigger "word"] [--epochs N] [--wait]
```

**Arguments:**
- `entity` — The character to train (e.g., juno, alice, vulcan)

**Options:**
- `--trigger` — Trigger word (defaults to entity name)
- `--epochs` — Training epochs (default: 10)
- `--wait` — Wait for training to complete

**Example:**
```bash
muse lora train juno --trigger "queen of operations" --wait
```

### list

List all trained LoRAs:

```bash
muse lora list
```

### generate

Generate an image using a character's LoRA:

```bash
muse lora generate <entity> "prompt"
```

**Example:**
```bash
muse lora generate juno "queen working at her desk in a dark office"
```

## How It Works

1. **Portrait Collection** — Uses existing portraits from `~/.muse/characters/{entity}/`
2. **Upload** — Images are uploaded to fal.ai
3. **Training** — Flux.2 LoRA training trains on the portraits
4. **Storage** — Trained LoRA saved to `~/.muse/loras/{entity}.safetensors`
5. **Profile Update** — Entity profile updated with LoRA metadata

## Profile Updates

After training, the entity's `profile.json` is updated with:

```json
{
  "lora": {
    "trained": true,
    "file": "~/.muse/loras/{entity}.safetensors",
    "trigger_word": "juno",
    "trained_at": "2026-04-08T20:15:00Z"
  }
}
```

## Workflow

```
Generate portraits → Train LoRA → Generate with consistency
```

Once trained, you can generate new images of the character in any pose/context while maintaining their visual identity.
