---
status: complete
owner: muse
priority: critical
description: Write and maintain custom CSS for components and layouts
completed: 2026-04-03
---

## Purpose

Implement component styling, layout systems, responsive behavior, and visual effects using CSS (vanilla and CSS custom properties). CSS is foundational to Muse's work — every UI improvement involves CSS implementation.

## Specification

**Inputs:**
- Component or layout requirements (from design direction or mockup)
- Target breakpoints and responsive behavior
- Design tokens (colors, typography, spacing scales)

**Outputs:**
- Stylesheet files or inline style rules
- Responsive CSS that adapts to mobile/tablet/desktop
- CSS custom properties (variables) for design tokens
- Minimal bundle size (no bloat)

**Behavior:**
- Use CSS custom properties for consistency
- Mobile-first approach (base styles for mobile, then media queries for larger screens)
- Leverage existing design tokens when available
- Avoid CSS-in-JS bloat — prefer vanilla CSS with preprocessor if needed
- Support dark theme via CSS custom properties
- Ensure performance (no expensive selectors, efficient repaints)

## Implementation

CSS is implemented directly in component stylesheets and global style files across Meteor/Blaze applications. Examples include:
- Entity landing page layouts (responsive grid, typography)
- Stream PWA dashboard CSS (dark-theme support, dashboard grid)
- MVP Zone interface CSS (custom component styles)
- Design system CSS utilities

## Dependencies

- Browser CSS support (modern browsers, ES6+ target)
- Design system tokens
- Meteor/Blaze template context

## Testing

Acceptance criteria:
- [ ] Renders correctly at all breakpoints (320px, 768px, 1200px+)
- [ ] CSS properties valid and no console warnings
- [ ] Dark/light theme support verified
- [ ] No performance regression (Lighthouse CSS score)
- [ ] Cross-browser compatible (Firefox, Chrome, Safari, Edge)

## Status Note

Ongoing and mature. CSS implementation is core to Muse's daily work. No blockers.
