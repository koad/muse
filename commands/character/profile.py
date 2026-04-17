#!/usr/bin/env python3
"""
Muse Character Profile Creator
Creates comprehensive character profiles for each entity.
"""

import json
import os
from datetime import datetime
from pathlib import Path

MUSE_DIR = os.environ.get("ENTITY_DIR", os.path.expanduser("~/.muse"))
CHARACTERS_DIR = Path(MUSE_DIR) / "characters"

# Entity descriptions and metadata
ENTITIES = {
    "juno": {
        "role": "Governance",
        "mythology": "Roman queen of the gods",
        "description": "Queen of the operation. Business runs because Juno runs.",
        "keywords": ["operation", "business", "governance", "orchestration"]
    },
    "vulcan": {
        "role": "Builder",
        "mythology": "Roman god of fire and forge",
        "description": "Forge god. Ships product. The hammer does not stop.",
        "keywords": ["product", "build", "forge", "ship"]
    },
    "muse": {
        "role": "Designer",
        "mythology": "Greek muse of arts",
        "description": "Where beauty becomes intention. Nine voices, one vision.",
        "keywords": ["design", "aesthetics", "visual", "beauty"]
    },
    "sibyl": {
        "role": "Researcher",
        "mythology": "Ancient prophetic priestess",
        "description": "Reads what is not written yet. The oracle does research.",
        "keywords": ["research", "oracle", "future", "prediction"]
    },
    "faber": {
        "role": "Content",
        "mythology": "Latin craftsman/maker",
        "description": "Maker. Turns raw signal into content worth keeping.",
        "keywords": ["content", "craft", "maker", "signal"]
    },
    "alice": {
        "role": "Education",
        "mythology": "Through the looking glass",
        "description": "Through the looking glass. Every entity begins here.",
        "keywords": ["conversation", "education", "entry", "portal"]
    },
    "chiron": {
        "role": "Education",
        "mythology": "Wise centaur who trained Achilles",
        "description": "Trained the heroes. Now builds the curriculum that does.",
        "keywords": ["education", "curriculum", "teaching", "heroes"]
    },
    "veritas": {
        "role": "Governance",
        "mythology": "Roman goddess of truth",
        "description": "Truth before it ships. Catches the lie in the machine.",
        "keywords": ["truth", "quality", "validation", "honesty"]
    },
    "mercury": {
        "role": "Content",
        "mythology": "Roman messenger god",
        "description": "First to the world. Fastest voice in the pantheon.",
        "keywords": ["publishing", "news", "fast", "announce"]
    },
    "iris": {
        "role": "Designer",
        "mythology": "Greek rainbow bridge goddess",
        "description": "Rainbow bridge. Brand strategy between worlds.",
        "keywords": ["brand", "strategy", "bridge", "visual"]
    },
    "lyra": {
        "role": "Content",
        "mythology": "Apollos lyre",
        "description": "Scores the work. Apollos lyre, tuned to your arc.",
        "keywords": ["music", "audio", "scoring", "arc"]
    },
    "copia": {
        "role": "Finance",
        "mythology": "Roman goddess of abundance",
        "description": "Goddess of abundance. Knows where every coin lives.",
        "keywords": ["finance", "abundance", "coins", "wealth"]
    },
    "argus": {
        "role": "Infrastructure",
        "mythology": "Hundred-eyed giant",
        "description": "Hundred-eyed. Never sleeps. Nothing gets past diagnostics.",
        "keywords": ["monitoring", "diagnostics", "infrastructure", "vigilance"]
    },
    "salus": {
        "role": "Infrastructure",
        "mythology": "Roman goddess of safety and health",
        "description": "Safety goddess. Watches the systems pulse so you do not.",
        "keywords": ["safety", "security", "pulse", "health"]
    },
    "janus": {
        "role": "Governance",
        "mythology": "Roman god of beginnings and transitions",
        "description": "Two faces, one stream. Sees what just happened and what is next.",
        "keywords": ["events", "stream", "past", "future"]
    },
    "aegis": {
        "role": "Governance",
        "mythology": "Shield of Zeus/Jupiter",
        "description": "The shield that thinks. Junos confidant, always close.",
        "keywords": ["security", "shield", "protection", "aegis"]
    },
    "livy": {
        "role": "Content",
        "mythology": "Titus Livius, Roman historian",
        "description": "History deserves a historian. Documentation as fossil record.",
        "keywords": ["history", "documentation", "fossil", "record"]
    },
    "rufus": {
        "role": "Content",
        "mythology": "Latin for red-haired/vivid",
        "description": "Vivid. Turns the work into something you can watch.",
        "keywords": ["video", "media", "production", "vivid"]
    },
    "vesta": {
        "role": "Infrastructure",
        "mythology": "Roman goddess of hearth and home",
        "description": "Hearth keeper. Architecture lives because the flame does.",
        "keywords": ["architecture", "hearth", "flame", "home"]
    }
}

# Outfit definitions
OUTFITS = {
    "juno": {"hue": 222, "sat": 25, "light": 15, "palette": "brand"},
    "vulcan": {"hue": 20, "sat": 30, "light": 20, "palette": "warm"},
    "muse": {"hue": 270, "sat": 35, "light": 20, "palette": "creative"},
    "sibyl": {"hue": 200, "sat": 20, "light": 30, "palette": "mystical"},
    "faber": {"hue": 30, "sat": 25, "light": 25, "palette": "earth"},
    "alice": {"hue": 45, "sat": 40, "light": 30, "palette": "alice"},
    "chiron": {"hue": 120, "sat": 25, "light": 20, "palette": "nature"},
    "veritas": {"hue": 160, "sat": 35, "light": 25, "palette": "trust"},
    "mercury": {"hue": 50, "sat": 45, "light": 35, "palette": "gold"},
    "iris": {"hue": 300, "sat": 50, "light": 30, "palette": "rainbow"},
    "lyra": {"hue": 45, "sat": 30, "light": 35, "palette": "gold"},
    "copia": {"hue": 40, "sat": 45, "light": 35, "palette": "gold"},
    "argus": {"hue": 180, "sat": 30, "light": 25, "palette": "tech"},
    "salus": {"hue": 140, "sat": 30, "light": 25, "palette": "safety"},
    "janus": {"hue": 0, "sat": 20, "light": 25, "palette": "dual"},
    "aegis": {"hue": 222, "sat": 30, "light": 20, "palette": "shield"},
    "livy": {"hue": 35, "sat": 25, "light": 30, "palette": "vintage"},
    "rufus": {"hue": 0, "sat": 35, "light": 30, "palette": "vivid"},
    "vesta": {"hue": 25, "sat": 40, "light": 30, "palette": "hearth"}
}


def create_profile(entity: str) -> dict:
    """Create a profile for an entity."""
    profile_dir = CHARACTERS_DIR / entity
    meta_file = profile_dir / "profile.json"
    
    # Get latest portrait
    portraits = sorted(profile_dir.glob("portrait-*.png"))
    latest_portrait = portraits[-1].name if portraits else None
    portrait_count = len(portraits)
    
    # Get entity metadata
    entity_meta = ENTITIES.get(entity, {})
    outfit_meta = OUTFITS.get(entity, {})
    
    profile = {
        "handle": entity,
        "name": entity.capitalize(),
        "mythology": entity_meta.get("mythology", ""),
        "role": entity_meta.get("role", ""),
        "description": entity_meta.get("description", ""),
        "keywords": entity_meta.get("keywords", []),
        "outfit": outfit_meta,
        "portraits": {
            "latest": latest_portrait,
            "count": portrait_count
        },
        "lora": {
            "trained": False,
            "file": None,
            "trained_at": None
        },
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }
    
    # Write profile
    with open(meta_file, "w") as f:
        json.dump(profile, f, indent=2)
    
    return profile


def main():
    print("Creating character profiles...")
    print()
    
    for entity in sorted(ENTITIES.keys()):
        profile_dir = CHARACTERS_DIR / entity
        if profile_dir.exists():
            profile = create_profile(entity)
            print(f"  Created: {entity} ({profile['role']})")
        else:
            print(f"  Skipped: {entity} (no portrait directory)")
    
    print()
    print(f"Done! Profiles in {CHARACTERS_DIR}")


if __name__ == "__main__":
    main()
