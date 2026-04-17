#!/usr/bin/env bash
# SPDX-License-Identifier: 0BSD

# Muse Character Portrait Generator
# Generates consistent character portraits using fal.ai Flux API
#
# Usage:
#   muse character portrait "entity-name" [--style ...] [--outfit ...]
#   muse character generate-all [--dry-run]
#   muse character list
#
# Examples:
#   muse character portrait juno
#   muse character portrait alice --style atmospheric
#   muse character generate-all

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MUSE_DIR="${ENTITY_DIR:-$HOME/.muse}"
CHARACTERS_DIR="$MUSE_DIR/characters"
MEDIA_DIR="$MUSE_DIR/media/characters"

# Load API key
FAL_KEY="${FAL_KEY:-}"
if [ -z "$FAL_KEY" ]; then
    if [ -f "$MUSE_DIR/.credentials" ]; then
        FAL_KEY=$(grep "^FAL_KEY=" "$MUSE_DIR/.credentials" 2>/dev/null | cut -d= -f2-)
    fi
    if [ -z "$FAL_KEY" ] && [ -f "$HOME/.koad-io/.credentials" ]; then
        FAL_KEY=$(grep "^FAL_KEY=" "$HOME/.koad-io/.credentials" 2>/dev/null | cut -d= -f2-)
    fi
fi

if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not found."
    exit 1
fi

# Entity character definitions
# Each entity has: name, description (visual), outfit (hue/sat), role
declare -A ENTITIES=(
    ["juno"]="Queen of the operation. Distinguished silver hair, regal bearing, wearing a dark elegant suit. She carries herself with quiet authority."
    ["vulcan"]="Forge god. Broad shoulders, calloused hands, wearing work gear with burns and soot. Eyes that have seen the forge fire for centuries."
    ["muse"]="Visual designer. Paint-stained fingers, wild creative energy, flowing artistic clothing. Nine eyes that see beauty everywhere."
    ["sibyl"]="Oracle. Pale ethereal figure, prophetic gaze, wearing flowing robes. Eyes that look through time itself."
    ["faber"]="Maker. Craftsman's hands, focused expression, wearing a maker's apron. The smell of sawdust follows."
    ["alice"]="The first. Curious explorer, wearing whimsical Victorian-inspired attire. Looking glass aesthetics, Wonderland undertones."
    ["chiron"]="Teacher. Wise centaur energy, wearing academic robes with athletic undertones. Scarred hands from training heroes."
    ["veritas"]="Truth. Sharp analytical gaze, wearing minimalist professional attire. No-nonsense expression, truth written on face."
    ["mercury"]="Messenger. Winged messenger aesthetic, fast-twitch energy, wearing sleek swift clothing. Always in motion."
    ["iris"]="Brand strategist. Rainbow iridescent undertones in appearance, flowing artistic clothing. Color in everything."
    ["lyra"]="Musician. Lyre in hand, ethereal musical energy, wearing flowing robes with celestial patterns."
    ["copia"]="Finance. Abundance goddess energy, wearing elegant business attire with golden accents. Numbers dance in their eyes."
    ["argus"]="Monitor. Many-eyed aesthetic, wearing tech-forward monitoring gear. Vigilant, never sleeping gaze."
    ["salus"]="Safety. Watchful protector, wearing functional safety gear. Steady hands, calm vigilance."
    ["janus"]="Event stream. Two-faced aesthetic (can be stylized as mirrored/dual elements), wearing dual-toned clothing. Past and future in one."
    ["aegis"]="Shield. Protected guardian, wearing armor with shield motifs. Shield-bearer energy, always close to Juno."
    ["livy"]="Historian. Archival aesthetic, wearing vintage scholarly attire. Feathers and scrolls energy."
    ["rufus"]="Media producer. Camera-ready, media equipment aesthetic, wearing creative production gear. Vivid energy."
    ["vesta"]="Hearth keeper. Warm protective figure, wearing functional architectural clothing. Flame-keeper undertones."
)

# Outfit color mappings (hue, saturation, lightness offset)
declare -A OUTFITS=(
    ["juno"]="hue=222 sat=25 light=15"      # Steel blue, regal
    ["vulcan"]="hue=20 sat=30 light=20"     # Warm ember
    ["muse"]="hue=270 sat=35 light=20"      # Creative purple
    ["sibyl"]="hue=200 sat=20 light=30"     # Ethereal blue
    ["faber"]="hue=30 sat=25 light=25"      # Natural brown
    ["alice"]="hue=45 sat=40 light=30"       # Warm amber
    ["chiron"]="hue=120 sat=25 light=20"     # Earth green
    ["veritas"]="hue=160 sat=35 light=25"    # Emerald truth
    ["mercury"]="hue=50 sat=45 light=35"     # Swift gold
    ["iris"]="hue=300 sat=50 light=30"       # Rainbow
    ["lyra"]="hue=45 sat=30 light=35"        # Musical gold
    ["copia"]="hue=40 sat=45 light=35"       # Abundance gold
    ["argus"]="hue=180 sat=30 light=25"      # Tech cyan
    ["salus"]="hue=140 sat=30 light=25"      # Safety green
    ["janus"]="hue=0 sat=20 light=25"        # Dual tones
    ["aegis"]="hue=222 sat=30 light=20"      # Shield blue
    ["livy"]="hue=35 sat=25 light=30"        # Vintage sepia
    ["rufus"]="hue=0 sat=35 light=30"        # Vivid red
    ["vesta"]="hue=25 sat=40 light=30"       # Hearth warm
)

# Subcommands
COMMAND="${1:-}"
shift 2>/dev/null || true

case "$COMMAND" in
    "list")
        echo "Available entities:"
        for entity in "${!ENTITIES[@]}"; do
            if [ -d "$CHARACTERS_DIR/$entity" ]; then
                echo "  ✓ $entity"
            else
                echo "    $entity"
            fi
        done
        ;;
        
    "portrait")
        ENTITY="${1:-}"
        if [ -z "$ENTITY" ]; then
            echo "Usage: muse character portrait <entity>"
            exit 1
        fi
        
        if [ -z "${ENTITIES[$ENTITY]}" ]; then
            echo "Unknown entity: $ENTITY"
            echo "Run 'muse character list' for available entities."
            exit 1
        fi
        
        DESCRIPTION="${ENTITIES[$ENTITY]}"
        OUTFIT="${OUTFITS[$ENTITY]:-hue=222 sat=22}"
        
        # Parse outfit
        eval "$OUTFIT"
        
        # Build prompt for portrait
        PROMPT="Professional portrait of a person. $DESCRIPTION. The image has a cinematic dark background with subtle color accents. High quality portrait photography, sharp focus, professional lighting."
        
        # Call fal.ai
        echo "Generating portrait for $ENTITY..."
        echo "Description: $DESCRIPTION"
        
        mkdir -p "$CHARACTERS_DIR/$ENTITY"
        TIMESTAMP=$(date +%Y%m%d-%H%M%S)
        
        python3 "$SCRIPT_DIR/portrait.py" \
            --entity "$ENTITY" \
            --description "$DESCRIPTION" \
            --hue "$hue" \
            --sat "$sat" \
            --light "$light" \
            --api-key "$FAL_KEY" \
            --output "$CHARACTERS_DIR/$ENTITY/portrait-$TIMESTAMP.png"
        ;;
        
    "generate-all")
        echo "Generating portraits for all entities..."
        echo ""
        
        for entity in "${!ENTITIES[@]}"; do
            echo "--- $entity ---"
            muse character portrait "$entity"
            echo ""
        done
        ;;
        
    "generate")
        ENTITY="${1:-}"
        shift
        PROMPT="$*"
        
        if [ -z "$ENTITY" ] || [ -z "$PROMPT" ]; then
            echo "Usage: muse character generate <entity> <prompt>"
            exit 1
        fi
        
        if [ ! -d "$CHARACTERS_DIR/$ENTITY" ]; then
            echo "Error: Entity '$ENTITY' not found"
            exit 1
        fi
        
        exec python3 "$SCRIPT_DIR/generate.py" \
            --entity "$ENTITY" \
            --prompt "$PROMPT" \
            --api-key "$FAL_KEY"
        ;;
        
    "")
        echo "Muse Character Commands:"
        echo "  muse character list                    - List available entities"
        echo "  muse character portrait <name>         - Generate portrait for entity"
        echo "  muse character generate <name> <prompt> - Generate consistent image"
        echo "  muse character generate-all            - Generate all portraits"
        echo ""
        echo "Available entities:"
        for entity in "${!ENTITIES[@]}"; do
            echo "  $entity"
        done
        ;;
        
    *)
        echo "Unknown command: $COMMAND"
        echo "Run 'muse character' for usage."
        exit 1
        ;;
esac
