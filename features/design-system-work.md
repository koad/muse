---
status: in-progress
owner: muse
priority: critical
description: Define and maintain design system tokens (color, typography, spacing)
started: 2026-04-01
---

## Purpose

Establish and evolve the koad:io design system — a single source of truth for colors, typography scales, spacing scales, and component patterns. A cohesive design system ensures visual consistency across all products and makes refinements fast and reliable.

## Specification

**Inputs:**
- Brand direction (from Iris or Juno)
- Product requirements and constraints
- Stakeholder feedback on visual coherence

**Outputs:**
- Design system specification document (tokens, patterns, usage guidelines)
- CSS custom properties file for all tokens
- Component pattern documentation
- Design direction specification

**Behavior:**
- Define core tokens: color palette (light/dark), typography (scales, weights), spacing (base unit and multiples)
- Create CSS custom properties that can be applied across products
- Document usage patterns (when to use which color, spacing rule, etc.)
- Evolve system based on product feedback
- Maintain consistency across all koad:io products

## Implementation

Design system files at:
- `~/.muse/design-system/` - design system specifications and tokens
- Token definitions in CSS custom properties
- Design direction documents in `~/.muse/briefs/`

## Dependencies

- Brand strategy (from Iris)
- Product-level feedback (from Juno and other entities)
- Accessibility requirements (WCAG color contrast)

## Testing

Acceptance criteria:
- [ ] All tokens documented with usage examples
- [ ] CSS custom properties defined and tested
- [ ] Color contrasts meet WCAG AA standards
- [ ] Typography scales are readable at all sizes
- [ ] Spacing scales follow a consistent multiplier (e.g., 4px base unit)
- [ ] Component patterns are reusable across projects

## Status Note

In-progress. Comprehensive design system spec recently completed (2026-04-02). Ongoing refinement as products use and provide feedback on token adequacy.
