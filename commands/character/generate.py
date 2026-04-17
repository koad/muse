#!/usr/bin/env python3
"""
Muse Character Consistency Generator
Uses Flux.2 reference images for consistent character generation.

This doesn't require LoRA training - it uses Flux.2's built-in
image reference capability for character consistency.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# Configuration
MUSE_DIR = Path(os.environ.get("ENTITY_DIR", os.path.expanduser("~/.muse")))
CHARACTERS_DIR = MUSE_DIR / "characters"
OUTPUT_DIR = MUSE_DIR / "media" / "characters"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FAL_API_BASE = "https://fal.run"


def upload_image(image_path: str, api_key: str) -> str:
    """Upload image to fal.ai and return URL."""
    import base64
    
    # Read and encode image
    with open(image_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")
    
    # Use the image-to-image endpoint with base64 input
    # We'll include it in the generation call instead
    return f"data:image/png;base64,{img_data}"


def generate_with_reference(entity: str, prompt: str, style: str, api_key: str) -> str:
    """Generate image using reference portrait."""
    entity_dir = CHARACTERS_DIR / entity

    if not entity_dir.exists():
        print(f"Error: Entity '{entity}' not found", file=sys.stderr)
        sys.exit(1)

    # Get latest portrait
    portraits = sorted(entity_dir.glob("portrait-*.png"))
    if not portraits:
        print(f"Error: No portraits found for {entity}", file=sys.stderr)
        sys.exit(1)

    reference = portraits[-1]
    print(f"Using reference: {reference.name}")

    # Upload reference image
    print("Uploading reference...")
    ref_url = upload_image(str(reference), api_key)
    if not ref_url:
        print("Failed to upload reference", file=sys.stderr)
        sys.exit(1)
    print(f"Reference URL: {ref_url}")

    # Generate with Flux.2 Pro with image input (using image-to-image)
    url = f"{FAL_API_BASE}/fal-ai/flux-pro/v1.1-ultra"

    payload = {
        "prompt": prompt,
        "image_size": {"width": 1024, "height": 1024},
        "num_images": 1,
        "enable_safety_checker": False,
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "image_url": ref_url,
    }

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
            images = result.get("images", [])
            if images:
                return images[0].get("url", "")
            return ""
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Generation error {e.code}: {body}", file=sys.stderr)
        return ""


def download_image(url: str, output_path: Path):
    """Download image from URL."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        with open(output_path, "wb") as f:
            f.write(resp.read())


def get_api_key():
    """Get fal.ai API key from credentials."""
    muse_creds = MUSE_DIR / ".credentials"
    if muse_creds.exists():
        with open(muse_creds) as f:
            for line in f:
                if line.startswith("FAL_KEY="):
                    return line.split("=", 1)[1].strip()

    koad_creds = Path.home() / ".koad-io" / ".credentials"
    if koad_creds.exists():
        with open(koad_creds) as f:
            for line in f:
                if line.startswith("FAL_KEY="):
                    return line.split("=", 1)[1].strip()

    return os.environ.get("FAL_KEY", "")


def main():
    parser = argparse.ArgumentParser(description="Generate with character consistency")
    parser.add_argument("--entity", required=True, help="Entity name")
    parser.add_argument("--prompt", required=True, help="Generation prompt")
    parser.add_argument("--style", default="portrait", help="Style (portrait, scene, action)")
    parser.add_argument("--output", help="Output path")
    parser.add_argument("--api-key", required=True, help="API key")

    args = parser.parse_args()

    api_key = args.api_key

    print(f"Generating consistent image for {args.entity}")
    print(f"Prompt: {args.prompt}")
    print()

    image_url = generate_with_reference(args.entity, args.prompt, args.style, api_key)

    if not image_url:
        print("Generation failed", file=sys.stderr)
        sys.exit(1)

    # Download image
    if args.output:
        output_path = Path(args.output)
    else:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_path = OUTPUT_DIR / f"{args.entity}-{timestamp}.png"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    download_image(image_url, output_path)

    print(f"\nGenerated: {output_path}")

    # Save metadata
    meta_path = output_path.with_suffix(".json")
    meta = {
        "entity": args.entity,
        "prompt": args.prompt,
        "reference_portrait": str(sorted(CHARACTERS_DIR / args.entity / "portrait-*.png")[-1]),
        "image_url": image_url,
        "generated_at": datetime.now().isoformat(),
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)


if __name__ == "__main__":
    main()
