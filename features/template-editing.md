---
status: in-progress
owner: muse
priority: high
description: Edit Meteor/Blaze templates for UI structure and component changes
started: 2026-04-01
---

## Purpose

Modify Meteor/Blaze template files to implement UI structure changes, add or refine components, and improve markup semantics. Template editing is part of Muse's implementation work when CSS alone is insufficient.

## Specification

**Inputs:**
- Meteor/Blaze template file path
- Required changes (component additions, restructuring, semantic improvements)
- Design specifications or mockups

**Outputs:**
- Updated `.html` (Blaze template) or `.js` files
- Markup remains semantic and accessible
- No backend logic changes (Vulcan's territory)

**Behavior:**
- Read existing template structure
- Make minimal changes needed to achieve design goal
- Preserve existing functionality
- Use semantic HTML for accessibility
- Keep template logic simple (complex logic → Vulcan)
- Test rendering at all breakpoints

## Implementation

Ongoing work across Meteor/Blaze applications. Examples:
- Entity card component template refinements (2026-04-02)
- Stream PWA template structure improvements
- kingofalldata.com homepage template updates

## Dependencies

- Meteor/Blaze template system
- Design specifications (from design direction documents)
- Functional requirements from Vulcan/product

## Testing

Acceptance criteria:
- [ ] Template renders correctly at all breakpoints
- [ ] Existing functionality preserved
- [ ] Markup is semantic and accessible
- [ ] No console errors
- [ ] Visual output matches design specification
- [ ] Template logic remains clear and maintainable

## Status Note

Active. Regular template refinements as UI improvements are designed and implemented. Work is coordinated with Vulcan when backend logic changes are needed.
