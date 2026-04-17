# muse image generate

Generate brand-consistent images using fal.ai Flux API with modular prompt composition.

## Usage

```bash
muse image generate "description" [options]
```

## Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--style` | default, editorial, technical, atmospheric, abstract | default | Visual language |
| `--type` | thumbnail-blog, thumbnail-social, hero-banner, card, avatar, quote-card | thumbnail-blog | Composition and dimensions |
| `--palette` | brand, warm, trust, alert, info, alice | brand | Color palette |
| `--output` | path | auto-generated | Where to save |
| `--draft` | (flag) | - | Use Flux Schnell (fast, cheap) instead of Pro |
| `--model` | fal.ai model ID | fal-ai/flux-pro/v1.1 | Override model |

## Examples

```bash
# Blog thumbnail with brand defaults
muse image generate "mesh network with glowing interconnected nodes"

# Social card for Alice product
muse image generate "warm conversation bubble with inner light" --palette alice --type thumbnail-social

# Quick draft (cheap, fast)
muse image generate "digital fortress on horizon" --style atmospheric --draft

# Custom output path
muse image generate "trust bond visualization" --style technical --output ~/media/trust.png
```

## How It Works

Prompts are assembled from fragments: `STYLE + TYPE + PALETTE + DESCRIPTION`

All fragments derive from koad's outfit `{ h: 222, s: 22 }`. The description is the only freeform part — everything else ensures brand consistency.

Each image is saved with a `.json` sidecar containing the full prompt and metadata for reproducibility.

## Credentials

Set `FAL_KEY` in `~/.muse/.credentials` or `~/.koad-io/.credentials`:

```
FAL_KEY=your-api-key-here
```
