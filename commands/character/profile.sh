#!/usr/bin/env bash
# SPDX-License-Identifier: 0BSD

# Muse Character Profile Creator
# Creates comprehensive character profiles for each entity

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Just call the Python script
exec python3 "$SCRIPT_DIR/profile.py" "$@"
