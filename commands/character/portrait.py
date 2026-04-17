#!/usr/bin/env python3
"""
Muse Character Portrait Generator
Generates consistent character portraits with outfit-aware coloring.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from pathlib import Path


def hsl_to_color_name(h, s, l):
    """Convert HSL to approximate color name for natural language prompts."""
    # Normalize values
    h = h % 360
    s = max(0, min(100, s))
    l = max(0, min(100, l))
    
    # Determine base color
    if l < 20:
        base = "deep dark"
    elif l < 35:
        base = "dark"
    elif l < 50:
        base = "rich"
    elif l < 65:
        base = "medium"
    else:
        base = "light"
    
    # Determine hue name
    if h < 15 or h >= 345:
        hue_name = "red"
    elif h < 45:
        hue_name = "orange"
    elif h < 75:
        hue_name = "amber"
    elif h < 150:
        hue_name = "green"
    elif h < 195:
        hue_name = "cyan"
    elif h < 255:
        hue_name = "blue"
    elif h < 285:
        hue_name = "purple"
    elif h < 315:
        hue_name = "magenta"
    else:
        hue_name = "pink"
    
    # Determine saturation
    if s < 15:
        sat_desc = "muted"
    elif s < 35:
        sat_desc = "subtle"
    elif s < 55:
        sat_desc = "vivid"
    else:
        sat_desc = "bold"
    
    return f"{sat_desc} {base} {hue_name}"


def compose_portrait_prompt(description, hue, sat, light, style="cinematic"):
    """Compose a portrait prompt with outfit-aware coloring."""
    
    color_name = hsl_to_color_name(hue, sat, light)
    
    # Style variations
    styles = {
        "cinematic": (
            "Cinematic portrait photography with dramatic lighting. "
            "The subject emerges from a dark background with subtle rim lighting. "
            "Sharp focus, professional studio quality, shallow depth of field."
        ),
        "atmospheric": (
            "Atmospheric portrait with volumetric lighting. "
            "Moody dark background with subtle light rays. "
            "Cinematic film grain, shallow depth of field, dramatic shadows."
        ),
        "editorial": (
            "Editorial portrait in magazine style. "
            "Clean dark background, sophisticated lighting setup. "
            "High-end fashion photography aesthetic, sharp and professional."
        ),
        "mystical": (
            "Mystical portrait with ethereal lighting. "
            "Dark atmospheric background with supernatural glow effects. "
            "Otherworldly quality, dramatic and enigmatic mood."
        ),
    }
    
    style_fragment = styles.get(style, styles["cinematic"])
    
    # Compose full prompt
    prompt = (
        f"Professional portrait: {description}. "
        f"The subject has {color_name} accent colors in their appearance and clothing. "
        f"{style_fragment} "
        f"The color palette uses {color_name} tones against a dark near-black background."
    )
    
    return prompt


def call_fal(prompt, api_key, model="fal-ai/flux-pro/v1.1"):
    """Call fal.ai API and return result."""
    url = f"https://fal.run/{model}"
    
    payload = {
        "prompt": prompt,
        "image_size": {"width": 1024, "height": 1024},
        "num_images": 1,
        "enable_safety_checker": False,
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
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
    parser = argparse.ArgumentParser(description="Muse character portrait generator")
    parser.add_argument("--entity", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--hue", type=int, default=222)
    parser.add_argument("--sat", type=int, default=22)
    parser.add_argument("--light", type=int, default=20)
    parser.add_argument("--style", default="cinematic")
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    # Compose prompt
    prompt = compose_portrait_prompt(
        args.description,
        args.hue,
        args.sat,
        args.light,
        args.style
    )
    
    print(f"Entity:  {args.entity}")
    print(f"Hue:     {args.hue}")
    print(f"Sat:     {args.sat}")
    print(f"Light:   {args.light}")
    print(f"Style:   {args.style}")
    print(f"Prompt:  {prompt[:100]}...")
    print()
    print("Generating portrait...")
    
    # Call API
    result = call_fal(prompt, args.api_key)
    
    # Get image URL
    images = result.get("images", [])
    if not images:
        print("Error: No images returned", file=sys.stderr)
        sys.exit(1)
    
    image_url = images[0].get("url", "")
    
    # Create output directory
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Download image
    download_image(image_url, output_path)
    print(f"Saved:   {output_path}")
    
    # Save metadata
    meta_path = output_path.with_suffix(".json")
    meta = {
        "entity": args.entity,
        "prompt": prompt,
        "description": args.description,
        "outfit": {
            "hue": args.hue,
            "sat": args.sat,
            "light": args.light,
        },
        "style": args.style,
        "timestamp": datetime.now().isoformat(),
        "image_url": image_url,
    }
    
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Meta:    {meta_path}")
    
    # Update entity profile if exists
    entity_dir = output_path.parent
    profile_path = entity_dir / "profile.json"
    
    profile = {}
    if profile_path.exists():
        with open(profile_path) as f:
            profile = json.load(f)
    
    profile["latest_portrait"] = str(output_path.name)
    profile["latest_portrait_meta"] = str(meta_path.name)
    profile["updated"] = datetime.now().isoformat()
    
    with open(profile_path, "w") as f:
        json.dump(profile, f, indent=2)


if __name__ == "__main__":
    main()
