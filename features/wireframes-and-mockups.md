---
status: complete
owner: muse
priority: high
description: Create layout wireframes and visual mockups for design decisions
completed: 2026-04-03
---

## Purpose

Produce visual specifications (wireframes and mockups) that clarify layout decisions and component arrangements before implementation. Wireframes communicate structure; mockups show visual treatment. These deliverables make design intent unambiguous.

## Specification

**Inputs:**
- Design direction or layout requirement
- Current interface or blank canvas (for new features)
- Responsive breakpoint targets

**Outputs:**
- Wireframe images (SVG, PNG, or Figma) showing layout structure
- Mockup images showing visual treatment with colors/typography
- Responsive mockups at multiple breakpoints (mobile, tablet, desktop)

**Behavior:**
- Create wireframes showing layout structure without visual detail
- Add responsive breakpoint variations (typically 320px, 768px, 1200px)
- Create mockups with actual colors, typography, and visual detail
- Use design system tokens in mockup specs
- Annotate key dimensions or spacing decisions when relevant
- Document assumptions or constraints in notes

## Implementation

Wireframes and mockups produced in design tools (Figma, drawing tools, or code-based specifications) and stored in:
- `~/.muse/briefs/` - design direction documents with embedded mockups
- `~/.muse/designs/` - mockup files

Examples:
- kingofalldata.com homepage wireframe (2026-03-26)
- Entity card dual-mode layout mockup (2026-04-02)
- Stream PWA dashboard layout mockups

## Dependencies

- Design direction or specification
- Design system tokens (colors, typography, spacing scales)
- Access to design tools (Figma, SVG, or drawing tools)

## Testing

Acceptance criteria:
- [ ] Wireframe clearly communicates layout structure
- [ ] Mockup shows visual treatment accurately
- [ ] All breakpoints shown for responsive designs
- [ ] Dimensions/spacing annotated where clarification needed
- [ ] Uses design system tokens in specs
- [ ] Stakeholders confirm mockup matches intent

## Status Note

Mature capability. Multiple mockups and wireframes produced for koad:io products. Ready for production use.
