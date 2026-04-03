---
status: complete
owner: muse
priority: critical
description: Commit Muse's own work to ~/.muse/ repository
completed: 2026-04-03
---

## Purpose

Muse commits changes to her own entity repository at `~/.muse/`. This command uses Claude Code (opencode) to review staged changes and generate a thoughtful commit message that captures both the what and the why of design changes.

## Interface

**Command:** `muse commit self`

**Arguments:** None

**Output:** Commits staged changes to `~/.muse/` git repository with a descriptive message

## Specification

**Behavior:**
- Change directory to `~/.muse/`
- Prompt Claude (via opencode) to review staged changes
- Generate commit message following Muse's commit style guidelines
- Apply commit to git repository
- Does NOT push automatically (manual push only)

**Commit Style Guidelines:**
- Subject line: max 72 characters, imperative mood ("Add", "Update", "Polish")
- Body: explain the "why" of design changes, not just "what"
- Focus on visual impact and design intent
- Example: "Polish Stream PWA card layout — spacing and color"

**Context Provided to Claude:**
- Muse's role as the aesthetic layer (functionality → beauty)
- Entity philosophy: repository is the entity
- Design decision principle: serve user understanding
- Commit rules and format requirements

## Implementation

Implemented in `command.sh`. Uses `opencode` (Claude Code backend) to generate commit messages with the prompt context above. Staged files are automatically reviewed by Claude before committing.

## Dependencies

- `opencode` command (Claude Code backend)
- Git repository at `~/.muse/`
- Staged changes (no automatic pushing)

## Testing

Acceptance criteria:
- [ ] Commits changes to `~/.muse/` git repository
- [ ] Commit message follows style guidelines
- [ ] Message captures design intent and rationale
- [ ] Does not automatically push to remote
- [ ] Git status shows clean working tree after commit

## Status Note

Production-ready. Used for all Muse design work commits. No blockers.
