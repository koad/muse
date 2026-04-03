---
status: complete
owner: muse
priority: critical
description: Create design direction documents that guide implementation work
completed: 2026-04-03
---

## Purpose

Produce comprehensive design direction specifications before implementation. Design direction documents communicate the intent, rationale, and detailed specifications for visual and UX improvements. They serve as blueprints for CSS, template, and interaction work.

## Specification

**Inputs:**
- Design brief or assignment from Juno
- Existing product state and constraints
- Brand direction (from Iris, if applicable)

**Outputs:**
- Markdown design direction document with:
  - Design philosophy/intent
  - Visual specifications (colors, typography, spacing)
  - Layout decisions and rationale
  - Responsive breakpoint behavior
  - Component patterns
  - Interaction specifications

**Behavior:**
- Understand the problem and current state
- Define visual direction (philosophy, not decoration)
- Specify all colors, typography, spacing using design system tokens
- Document layout decisions and responsive behavior
- Include wireframes or mockups when layout changes are significant
- Provide clear rationale for design choices
- Make the document detailed enough that implementation is straightforward

## Implementation

Design direction documents stored in `~/.muse/briefs/`. Examples:
- koad:io design system spec (2026-04-02)
- kingofalldata.com design direction (2026-04-01)
- Stream PWA design direction documents

## Dependencies

- Access to current product code/designs
- Design system tokens (if already defined)
- Brand direction (from Iris)

## Testing

Acceptance criteria:
- [ ] Document clearly explains design intent and rationale
- [ ] All visual specifications detailed (colors, typography, spacing)
- [ ] Responsive behavior documented for all breakpoints
- [ ] Enough detail for implementation to proceed without clarification
- [ ] Includes rationale for design choices
- [ ] Uses design system tokens consistently

## Status Note

Mature and ongoing. Multiple design direction documents produced. Core capability for Muse's work.
