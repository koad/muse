#!/usr/bin/env bash
# SPDX-License-Identifier: 0BSD

# Muse LoRA Training Command
# Trains LoRA adapters for character consistency

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/train.py" "$@"
