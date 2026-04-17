#!/usr/bin/env python3
"""
Muse LoRA Training Command
Trains LoRA adapters for character consistency using Flux.2 on fal.ai

Usage:
    muse lora train <entity> [--epochs N] [--trigger "trigger word"]
    muse lora list
    muse lora generate <entity> "prompt"
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from pathlib import Path

# Configuration
MUSE_DIR = Path(os.environ.get("ENTITY_DIR", os.path.expanduser("~/.muse")))
CHARACTERS_DIR = MUSE_DIR / "characters"
LORA_DIR = MUSE_DIR / "loras"
LORA_DIR.mkdir(exist_ok=True)

# fal.ai API endpoints
FAL_API_BASE = "https://fal.run"


def upload_image(image_path: str, api_key: str) -> str:
    """Upload image to fal.ai and return URL."""
    url = f"{FAL_API_BASE}/fal-ai/flux-lora-fast-training/upload/image"
    
    with open(image_path, "rb") as f:
        import mimetypes
        content_type = mimetypes.guess_type(image_path)[0] or "image/png"
        
        boundary = "----WebKitFormBoundary" + os.urandom(12).hex()
        
        body = b""
        body += f"--{boundary}\r\n".encode()
        body += f'Content-Disposition: form-data; name="file"; filename="{os.path.basename(image_path)}"\r\n'.encode()
        body += f"Content-Type: {content_type}\r\n\r\n".encode()
        body += f.read()
        body += f"\r\n--{boundary}--\r\n".encode()
        
        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Authorization": f"Key {api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
            },
            method="POST",
        )
        
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result.get("url", "")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            print(f"Upload error {e.code}: {body}", file=sys.stderr)
            return ""


def train_lora(entity: str, trigger_word: str, epochs: int, api_key: str) -> dict:
    """Train a LoRA for a character."""
    entity_dir = CHARACTERS_DIR / entity
    
    if not entity_dir.exists():
        print(f"Error: Entity '{entity}' not found", file=sys.stderr)
        sys.exit(1)
    
    # Get portrait images
    portraits = sorted(entity_dir.glob("portrait-*.png"))
    if not portraits:
        print(f"Error: No portraits found for {entity}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Training LoRA for {entity}")
    print(f"Trigger word: {trigger_word}")
    print(f"Epochs: {epochs}")
    print(f"Found {len(portraits)} portrait(s)")
    
    # Upload images
    print("\nUploading images...")
    image_urls = []
    for portrait in portraits:
        print(f"  Uploading {portrait.name}...")
        url = upload_image(str(portrait), api_key)
        if url:
            image_urls.append(url)
            print(f"    -> {url}")
        else:
            print(f"    FAILED")
    
    if not image_urls:
        print("Error: Failed to upload any images", file=sys.stderr)
        sys.exit(1)
    
    # Start training
    print("\nStarting training...")
    train_url = f"{FAL_API_BASE}/fal-ai/flux-lora-fast-training"
    
    payload = {
        "image_urls": image_urls,
        "trigger_word": trigger_word,
        "num_epochs": epochs,
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        train_url,
        data=data,
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            request_id = result.get("request_id", "")
            print(f"Training started. Request ID: {request_id}")
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Training error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)


def check_training_status(request_id: str, api_key: str) -> dict:
    """Check training status."""
    status_url = f"{FAL_API_BASE}/fal-ai/flux-lora-fast-training/status/{request_id}"
    
    req = urllib.request.Request(
        status_url,
        headers={"Authorization": f"Key {api_key}"},
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Status error {e.code}: {body}", file=sys.stderr)
        return {}


def wait_for_training(request_id: str, api_key: str, poll_interval: int = 30) -> dict:
    """Wait for training to complete."""
    print("\nWaiting for training to complete...")
    
    while True:
        status = check_training_status(request_id, api_key)
        state = status.get("status", "unknown")
        
        print(f"  Status: {state}")
        
        if state == "COMPLETED":
            print("\nTraining complete!")
            return status
        elif state == "FAILED":
            print("\nTraining failed!", file=sys.stderr)
            print(json.dumps(status, indent=2), file=sys.stderr)
            sys.exit(1)
        
        print(f"  Sleeping {poll_interval}s...")
        time.sleep(poll_interval)


def save_lora(entity: str, result: dict, trigger_word: str):
    """Save trained LoRA to disk."""
    lora_file = LORA_DIR / f"{entity}.safetensors"
    
    lora_info = {
        "entity": entity,
        "trigger_word": trigger_word,
        "request_id": result.get("request_id", ""),
        "lora_url": result.get("lora", {}).get("lora_file_url", ""),
        "trained_at": datetime.now().isoformat(),
    }
    
    # Update entity profile
    profile_file = CHARACTERS_DIR / entity / "profile.json"
    if profile_file.exists():
        with open(profile_file) as f:
            profile = json.load(f)
        
        profile["lora"] = {
            "trained": True,
            "file": str(lora_file),
            "trigger_word": trigger_word,
            "trained_at": datetime.now().isoformat(),
            "lora_url": lora_info["lora_url"],
        }
        profile["updated"] = datetime.now().isoformat()
        
        with open(profile_file, "w") as f:
            json.dump(profile, f, indent=2)
        
        print(f"Updated profile: {profile_file}")
    
    # Save LoRA info
    info_file = lora_file.with_suffix(".json")
    with open(info_file, "w") as f:
        json.dump(lora_info, f, indent=2)
    
    print(f"\nLoRA trained: {lora_file}")
    print(f"Info: {info_file}")


def list_loras():
    """List all trained LoRAs."""
    print("Trained LoRAs:")
    print()
    
    for lora_file in sorted(LORA_DIR.glob("*.safetensors")):
        info_file = lora_file.with_suffix(".json")
        if info_file.exists():
            with open(info_file) as f:
                info = json.load(f)
            print(f"  {info['entity']}")
            print(f"    Trigger: {info['trigger_word']}")
            print(f"    Trained: {info['trained_at']}")
            print()
        else:
            print(f"  {lora_file.stem} (no info)")


def generate_with_lora(entity: str, prompt: str, api_key: str):
    """Generate image using a character's LoRA."""
    # Get LoRA info
    info_file = LORA_DIR / f"{entity}.json"
    if not info_file.exists():
        print(f"Error: No LoRA found for {entity}", file=sys.stderr)
        print(f"Run 'muse lora train {entity}' first", file=sys.stderr)
        sys.exit(1)
    
    with open(info_file) as f:
        lora_info = json.load(f)
    
    trigger_word = lora_info["trigger_word"]
    
    # Compose prompt with trigger
    full_prompt = f"{trigger_word}, {prompt}"
    
    print(f"Generating with {entity} LoRA...")
    print(f"Prompt: {full_prompt}")
    
    # Call Flux with LoRA
    url = f"{FAL_API_BASE}/fal-ai/flux-pro/v1.1"
    
    payload = {
        "prompt": full_prompt,
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
            images = result.get("images", [])
            if images:
                return images[0].get("url", "")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Generation error {e.code}: {body}", file=sys.stderr)
        return ""


def get_api_key():
    """Get fal.ai API key from credentials."""
    # Check MUSE credentials
    muse_creds = MUSE_DIR / ".credentials"
    if muse_creds.exists():
        with open(muse_creds) as f:
            for line in f:
                if line.startswith("FAL_KEY="):
                    return line.split("=", 1)[1].strip()
    
    # Check koad-io credentials
    koad_creds = Path.home() / ".koad-io" / ".credentials"
    if koad_creds.exists():
        with open(koad_creds) as f:
            for line in f:
                if line.startswith("FAL_KEY="):
                    return line.split("=", 1)[1].strip()
    
    return os.environ.get("FAL_KEY", "")


def main():
    parser = argparse.ArgumentParser(description="Muse LoRA training")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # train command
    train_parser = subparsers.add_parser("train", help="Train LoRA for entity")
    train_parser.add_argument("entity", help="Entity name")
    train_parser.add_argument("--trigger", default=None, help="Trigger word")
    train_parser.add_argument("--epochs", type=int, default=10, help="Training epochs")
    train_parser.add_argument("--wait", action="store_true", help="Wait for completion")
    
    # list command
    subparsers.add_parser("list", help="List trained LoRAs")
    
    # generate command
    gen_parser = subparsers.add_parser("generate", help="Generate with LoRA")
    gen_parser.add_argument("entity", help="Entity name")
    gen_parser.add_argument("prompt", help="Generation prompt")
    
    args = parser.parse_args()
    
    api_key = get_api_key()
    if not api_key:
        print("Error: FAL_KEY not found in credentials", file=sys.stderr)
        sys.exit(1)
    
    if args.command == "train":
        # Get trigger word from entity profile if not provided
        trigger = args.trigger
        if not trigger:
            profile_file = CHARACTERS_DIR / args.entity / "profile.json"
            if profile_file.exists():
                with open(profile_file) as f:
                    profile = json.load(f)
                    trigger = profile.get("name", args.entity.capitalize())
            else:
                trigger = args.entity.capitalize()
        
        result = train_lora(args.entity, trigger, args.epochs, api_key)
        
        if args.wait:
            status = wait_for_training(result["request_id"], api_key)
            save_lora(args.entity, status, trigger)
        else:
            save_lora(args.entity, result, trigger)
            print("\nNote: LoRA may take a few minutes to train.")
            print("Run 'muse lora status <request_id>' to check progress.")
    
    elif args.command == "list":
        list_loras()
    
    elif args.command == "generate":
        image_url = generate_with_lora(args.entity, args.prompt, api_key)
        if image_url:
            print(f"\nGenerated: {image_url}")
        else:
            print("Generation failed", file=sys.stderr)
            sys.exit(1)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
