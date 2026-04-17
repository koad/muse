#!/usr/bin/env python3
"""
Muse Image Generator — fal.ai Flux API with modular prompt composition.

Assembles brand-consistent prompts from style/type/palette fragments,
calls fal.ai, saves the result with its prompt metadata.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# ── Prompt Fragment Library ──────────────────────────────────────────────
# Derived from koad's outfit { h: 222, s: 22 } — muted steel-blue, desaturated

STYLES = {
    "default": (
        "rendered in a minimal dark-mode aesthetic with clean geometric forms "
        "and matte surfaces. The lighting is low-key and understated, with "
        "occasional subtle luminous edges in muted steel-blue. The overall "
        "feeling is digital-native and desaturated."
    ),
    "editorial": (
        "rendered as a sophisticated editorial illustration with flat color "
        "blocks and fine precise linework against a dark background. The "
        "treatment is understated and magazine-quality, with selective use "
        "of color for emphasis."
    ),
    "technical": (
        "rendered as a technical diagram with a blueprint aesthetic. "
        "The background is dark with muted steel-blue accent lines forming "
        "precise geometric constructions. The palette is desaturated and "
        "the overall feel is engineered and exact."
    ),
    "atmospheric": (
        "rendered as a cinematic wide shot with volumetric lighting and "
        "a dark moody atmosphere. Deep shadows are accented by muted "
        "steel-blue rim lighting. There is subtle film grain and shallow "
        "depth of field. The tones are cool and desaturated throughout."
    ),
    "abstract": (
        "rendered as abstract generative art with flowing data streams "
        "and particle systems against a dark void. Luminous elements glow "
        "in muted steel-blue. The composition balances mathematical "
        "precision with organic flow, keeping saturation low."
    ),
}

TYPES = {
    "thumbnail-blog": {
        "fragment": "The composition is horizontal with a single clear focal point. There is negative space on the left third suitable for text overlay. The image should read clearly at small sizes.",
        "width": 1600, "height": 900,
    },
    "thumbnail-social": {
        "fragment": "The composition is square with a bold central subject. The contrast is high and the image is punchy enough to work at small sizes on social media.",
        "width": 1024, "height": 1024,
    },
    "hero-banner": {
        "fragment": "The composition is ultra-wide and cinematic with layered depth and atmospheric perspective. The lower third is kept clear as a safe zone for text.",
        "width": 1680, "height": 720,
    },
    "card": {
        "fragment": "The composition is vertical with the subject in the upper two-thirds. The bottom third fades to a subtle gradient suitable for text overlay.",
        "width": 900, "height": 1200,
    },
    "avatar": {
        "fragment": "The composition is a centered square with a portrait or symbol that works well when cropped to a circle at small sizes.",
        "width": 512, "height": 512,
    },
    "quote-card": {
        "fragment": "The composition is minimal with large areas of negative space and subtle texture, designed for text to be overlaid in the center.",
        "width": 1080, "height": 1080,
    },
    "wallpaper": {
        "fragment": "The composition is a wide cinematic scene showing the full figure of the subject in their environment, not too close and not too far. The subject is clearly visible and active, engaged in their work. The scene has depth, atmosphere, and environmental detail that fills the frame edge to edge. Suitable as a desktop wallpaper.",
        "width": 1920, "height": 1080,
    },
}

PALETTES = {
    "brand": (
        "The color palette is strictly limited to deep near-black backgrounds "
        "with muted steel-blue accents. All tones are cool and desaturated. "
        "The feeling is understated and professional with no vivid or warm colors."
    ),
    "warm": (
        "The color palette uses a warm dark background with amber accents "
        "and soft cream highlights. There is a gentle ember glow throughout."
    ),
    "trust": (
        "The color palette is anchored on a deep black base with emerald "
        "green accents that suggest verification, security, and growth."
    ),
    "alert": (
        "The color palette uses a dark base with coral red accents "
        "that feel urgent and attention-demanding."
    ),
    "info": (
        "The color palette uses a dark base with sky blue accents "
        "that feel calm, informational, and clear."
    ),
    "alice": (
        "The color palette uses a dark background with warm amber as the "
        "primary accent color, creating a golden glow that feels inviting "
        "and conversational."
    ),
}


def compose_prompt(description, style, type_name, palette):
    """Assemble a full prompt from fragments + description.

    Flux uses T5-XXL which understands natural language well.
    Order: subject/description first (most important), then scene/composition,
    then style/mood, then palette constraints. Written as prose, not tags.
    """
    style_fragment = STYLES.get(style, STYLES["default"])
    type_info = TYPES.get(type_name, TYPES["thumbnail-blog"])
    palette_fragment = PALETTES.get(palette, PALETTES["brand"])

    prompt = f"{description}. {type_info['fragment']} {style_fragment} {palette_fragment}"
    return prompt, type_info["width"], type_info["height"]


def call_fal(prompt, width, height, model, api_key):
    """Call fal.ai API and return image URL."""
    url = f"https://fal.run/{model}"

    payload = {
        "prompt": prompt,
        "image_size": {"width": width, "height": height},
        "num_images": 1,
        "enable_safety_checker": False,
    }

    # Add model-specific params
    if "schnell" in model:
        payload["num_inference_steps"] = 4
    else:
        payload["num_inference_steps"] = 28
        payload["guidance_scale"] = 3.5

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)


def download_image(url, output_path):
    """Download image from URL to local path."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        with open(output_path, "wb") as f:
            f.write(resp.read())


def main():
    parser = argparse.ArgumentParser(description="Muse image generator")
    parser.add_argument("--description", required=True)
    parser.add_argument("--style", default="default")
    parser.add_argument("--type", default="thumbnail-blog", dest="type_name")
    parser.add_argument("--palette", default="brand")
    parser.add_argument("--model", default="fal-ai/flux-pro/v1.1")
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    # Compose prompt
    prompt, width, height = compose_prompt(
        args.description, args.style, args.type_name, args.palette
    )

    print(f"Style:   {args.style}")
    print(f"Type:    {args.type_name}")
    print(f"Palette: {args.palette}")
    print(f"Size:    {width}x{height}")
    print(f"Model:   {args.model}")
    print(f"Prompt:  {prompt[:120]}...")
    print()
    print("Generating...")

    # Call API
    result = call_fal(prompt, width, height, args.model, args.api_key)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        media_dir = Path.home() / ".muse" / "media" / "generated"
        media_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_path = media_dir / f"{timestamp}-{args.style}-{args.type_name}.png"

    # Download image
    images = result.get("images", [])
    if not images:
        print("Error: No images returned", file=sys.stderr)
        sys.exit(1)

    image_url = images[0].get("url", "")
    download_image(image_url, output_path)
    print(f"Saved:   {output_path}")

    # Save prompt metadata alongside
    meta_path = output_path.with_suffix(".json")
    meta = {
        "prompt": prompt,
        "style": args.style,
        "type": args.type_name,
        "palette": args.palette,
        "description": args.description,
        "model": args.model,
        "width": width,
        "height": height,
        "timestamp": datetime.now().isoformat(),
        "fal_response": {k: v for k, v in result.items() if k != "images"},
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Meta:    {meta_path}")


if __name__ == "__main__":
    main()
