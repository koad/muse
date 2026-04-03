#!/usr/bin/env bash
set -euo pipefail
# Muse — interactive or prompt-driven
# Usage: muse                               → interactive Claude Code session
#        PROMPT="polish this UI" muse       → non-interactive, identity + prompt
#        echo "polish this UI" | muse       → non-interactive, stdin

IDENTITY="$HOME/.muse/memories/001-identity.md"

PROMPT="${PROMPT:-}"
if [ -z "$PROMPT" ] && [ ! -t 0 ]; then
  PROMPT="$(cat)"
fi

cd "$HOME/.muse"

if [ -n "$PROMPT" ]; then
  exec claude -p "$(cat "$IDENTITY")

$PROMPT"
else
  exec claude . --model sonnet
fi
