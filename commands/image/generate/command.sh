#!/usr/bin/env bash
# SPDX-License-Identifier: 0BSD

# Muse Image Generate Command
# Generates brand-consistent images via fal.ai Flux API
# Uses modular prompt composition from the design system
#
# Usage:
#   muse image generate "description" [--style default|editorial|atmospheric|technical|abstract] [--type thumbnail-blog|thumbnail-social|hero-banner|card|avatar] [--palette brand|warm|trust|alert|info|alice] [--output path]
#
# Examples:
#   muse image generate "mesh network with glowing nodes"
#   muse image generate "sovereign key floating in space" --style editorial --type thumbnail-social
#   muse image generate "digital fortress on horizon" --style atmospheric --output ~/media/fortress.png

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MUSE_DIR="${ENTITY_DIR:-$HOME/.muse}"

# Load API key
FAL_KEY="${FAL_KEY:-}"
if [ -z "$FAL_KEY" ]; then
    # Check entity credentials
    if [ -f "$MUSE_DIR/.credentials" ]; then
        FAL_KEY=$(grep "^FAL_KEY=" "$MUSE_DIR/.credentials" 2>/dev/null | cut -d= -f2-)
    fi
    # Fall back to koad-io credentials
    if [ -z "$FAL_KEY" ] && [ -f "$HOME/.koad-io/.credentials" ]; then
        FAL_KEY=$(grep "^FAL_KEY=" "$HOME/.koad-io/.credentials" 2>/dev/null | cut -d= -f2-)
    fi
fi

if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not found. Set it in $MUSE_DIR/.credentials or export FAL_KEY=..."
    exit 1
fi

# Defaults
STYLE="default"
TYPE="thumbnail-blog"
PALETTE="brand"
OUTPUT=""
DESCRIPTION=""
MODEL="fal-ai/flux-pro/v1.1"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --style)  STYLE="$2"; shift 2 ;;
        --type)   TYPE="$2"; shift 2 ;;
        --palette) PALETTE="$2"; shift 2 ;;
        --output) OUTPUT="$2"; shift 2 ;;
        --model)  MODEL="$2"; shift 2 ;;
        --draft)  MODEL="fal-ai/flux/schnell"; shift ;;
        *)
            if [ -z "$DESCRIPTION" ]; then
                DESCRIPTION="$1"
            fi
            shift ;;
    esac
done

if [ -z "$DESCRIPTION" ]; then
    echo "Usage: muse image generate \"description\" [--style ...] [--type ...] [--palette ...]"
    exit 1
fi

# Call the Python compositor
exec python3 "$SCRIPT_DIR/generate.py" \
    --description "$DESCRIPTION" \
    --style "$STYLE" \
    --type "$TYPE" \
    --palette "$PALETTE" \
    --model "$MODEL" \
    --api-key "$FAL_KEY" \
    ${OUTPUT:+--output "$OUTPUT"}
