---
status: draft
owner: muse
priority: medium
description: Audit design consistency and quality across products
started: 2026-04-03
---

## Purpose

Systematically review products for design consistency, accessibility, and adherence to design system. Design audits identify gaps between current state and intended design direction, enabling targeted refinement work.

## Specification

**Inputs:**
- Target product or component set
- Design system specification
- Accessibility standards (WCAG 2.1)

**Outputs:**
- Audit report documenting:
  - Consistency issues (colors, typography, spacing deviations)
  - Accessibility gaps (contrast, navigation, semantics)
  - Design system token adherence
  - Recommendations for refinement

**Behavior:**
- Review visual state against design system tokens
- Check color contrast (WCAG AA minimum)
- Verify typography usage matches scales
- Audit spacing for consistency
- Review accessibility (keyboard nav, ARIA attributes, semantic HTML)
- Identify quick wins vs. larger refinement work
- Prioritize recommendations by impact and effort

## Implementation

Not yet built. Audit would be performed through:
- Manual visual review (screenshot comparison)
- Accessibility scanning tools (axe, Lighthouse)
- Design token compliance checking
- Documentation of findings in markdown or JSON report

## Dependencies

- Design system specification (complete as of 2026-04-02)
- Design direction documents
- Access to product code/live sites

## Testing

Acceptance criteria:
- [ ] Audit covers all major components/pages
- [ ] Issues are documented with specific examples
- [ ] Recommendations are actionable
- [ ] Report is clear and prioritized
- [ ] Stakeholders can act on findings

## Status Note

Planned feature. Would enable systematic design quality assurance across koad:io products. Current work is ad-hoc based on assignments from Juno.
