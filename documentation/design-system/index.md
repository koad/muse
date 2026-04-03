---
status: in-progress
date: 2026-04-03
owner: muse
---

# Design System Documentation

Design system tokens and specifications.

## Core Tokens

- **Colors:** Light/dark theme palettes, semantic colors (primary, success, warning, error, etc.)
- **Typography:** Font families, scales, weights, line heights
- **Spacing:** Base unit (4px), multipliers, margin/padding scales
- **Components:** Button, card, input, typography variants

## Files

- Design system specification: `~/.muse/briefs/comprehensive-koad-io-design-system-spec.md`
- CSS custom properties: embedded in application stylesheets

## Current Status

Comprehensive design system spec completed (2026-04-02). CSS implementation ongoing across products.

## Adding to the System

When adding new tokens:
1. Document token name, value, and semantic meaning
2. Create CSS custom property
3. Update all products using the token
4. Test in both light and dark themes
5. Document in this index
