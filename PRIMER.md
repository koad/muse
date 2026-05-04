# PRIMER: Muse

Muse is the visual design and UI execution entity for the koad:io ecosystem. Vulcan ships working product; Muse makes it worth using — CSS, layout, typography, hierarchy, design systems. Iris sets visual philosophy and direction; Muse executes it. Muse does not write application logic.

Work arrives as briefs in `~/.muse/briefs/` or via MCP. GitHub Issues on `koad/muse` are for external users and sponsors.

---

## Current State

**Active.** Identity refreshed 2026-04-22. CSS discipline memory added 2026-04-23. Outfit system and design system stable.

### Design Principles
- Dark theme, terminal-adjacent
- Mobile-first — everything works at every size
- Performance over decoration
- Consistency via design systems, not one-off styles
- Incremental improvement over redesign

### What's Complete
- Alice UI design brief: authored (`briefs/alice-ui-design-brief.md`)
- Alice Phase 2A live on kingofalldata.com (Vulcan shipped from Muse's brief, commit 7d95c39)
- Homepage wireframes and refinements (multiple iterations)
- Entity card component design spec
- MVP Zone interface design
- Stream PWA design brief
- Blog layout design
- Domain skins concept
- Trust bond visualization design
- Graduation certificate design for Alice
- 2026-04-21 storefront sprint: five rounds of design direction (landing, /what-is-this, /flights/:id, /entities/:handle, announcement surface)
- `data-authored-by` CSS extension system — baseline set; Wednesday rotation uses it
- Becoming-page visual direction brief (2026-04-24)
- CSS discipline memory (`memories/004-css-discipline.md`) — three rules: fluid, self-scoped, honor the theme

---

## Active Work / Open

- **basic-bitch retirement Phase 2 complete** (commit `1a8edb2`, 2026-05-02) — login-ui.css migrated to accounts-ui; hardcoded #ccc cleaned to var(--text-color); accounts-ui gitignore allowlist opened for client/ + package.js tracking
- **basic-bitch retirement Phase 3 complete** (commit `8b645c2`, daemon-interface/src, 2026-05-02) — basic-bitch removed from daemon-interface .meteor/packages; debug route updated to __theme_engine_debug__; 5 dead-code files deleted (Semantic UI boilerplate header/if-logged-in + orphaned search template); audit correction: site-contained/page-contained/content-contained were already in theme-engine containers.css from Phase 1
- **ecoincore navigation migration complete** (commit `3d9af1c`, 2026-05-02) — local client/components/navigation/ deleted (templates + logic + styles, 429 lines); koad:io-navigation added to .meteor/packages; double-render bug avoided by removing inline {{> __top_bar_assembly__}} from head.html (package body.html injects it); data contract confirmed via client/navigation.js
- **navigation font-size token migration complete** (commit `dcf0141`, 2026-05-02) — 11 hardcoded px font-size values replaced with var(--font-body) / var(--font-sm) in koad:io-navigation; icon-scale values (18px–28px) intentionally left; Vulcan's uncommitted logic.js / templates.html changes staged separately
- **koad-io-dashboard-devices font-size token migration complete** (commit `b62f00b`, 2026-05-02) — 5 hardcoded font-size values replaced: .device-item h2→--font-h3, .input-subdomain→--font-body, .info-section h3→--font-h4, .interface-header h3→--font-h4, .interface-status→--font-sm; CSS file was untracked in forge repo, now committed
- **admin-component-experiments font-size token migration complete** (commit `bfc9d13`, 2026-05-02) — 25 hardcoded px/rem font-size values replaced across 8 CSS files (7 components + interface shell); --font-body/sm/h3/h4/mono-label applied; display-scale values (28px, 1.7rem) and intentional micro-sizes (0.7rem, 0.8rem, 0.9rem) left intact; pre-existing logic.js/templates.html working-tree changes not touched
- **sovereign-profiles font-size token migration complete** (commit `a2df9ab`, 2026-05-03) — 75 of 97 hardcoded font-size values replaced across the full 1890-line stylesheet (profile editor, card, full, kingdoms overview, key management surface); 22 left intentionally: all 10px micro badges, display-scale avatar initials (18/22/32px), large display headings (26px name, 22px page headings, 17px modal), bio/card-name (15px), icon (16px), stat value (18px); package CSS committed to forge for the first time (was untracked)
- **brand-components font-size token migration complete** (commit `030312b`, 2026-05-03) — 220 token usages across 41 CSS files (all components, sessions, kingdom overview, bond/emission surfaces); 115 intentionally left: micro badges (8–10px below floor), display-scale (avatars/icons 16–72px), large metric displays (1.4–2.5rem), chat reading surface (15px), em-relative values; Vulcan pre-existing working-tree changes (templates + helpers) left unstaged
- **CSS audit brief** (`briefs/2026-04-23-css-audit-unsigned-surfaces.md`) — assigned, not yet executed; audit of brand-components, theme-engine, storefront CSS against the three rules
- **Iris /alice brief** (`~/.iris/briefs/2026-04-25-alice-landing-positioning-brief.md`) — Iris flagged enrollment vs participation framing risk; Muse + Mercury are addressed; do not act on storefront changes without koad pairing
- **Avatar briefs** (`briefs/[entity]-avatar-brief.md`) — fleet of entity avatar generation briefs; Flux Pro via fal.ai; execution pending

---

## What's on the Storefront Now

kingofalldata.com has grown significantly since early 2026-04 briefs. New surfaces (not yet design-reviewed by Muse, Vulcan functional):
- `/overview` — public kingdom dashboard (entities, bond graph, 24h flights+emissions)
- `/status` — APM + kingdom-fuel band
- `/activity` — sigchain rendering
- `/bonds`, `/emissions`, `/kingdoms`, `/sessions/:id`, `/flights/:id`
- Sovereign profile pages with sub-routes (`/keys`, `/sigchain`, `/identity`, `/files`, `/sessions`)

These surfaces need Muse's design eye. Per pairing model — not a solo dispatch, Muse + koad together.

---

## Blocked / Awaiting

- **Blog route** — blog layout design is ready; waiting on koad merging koad/kingofalldata-dot-com#1 to add `/blog` route
- **Stream PWA** — design complete; Vulcan has not started build
- **MVP Zone** — design complete; build not yet assigned
- **Storefront new surfaces** — pairing call with koad needed before any CSS work

---

## Key Files

| File | Purpose |
|------|---------|
| `ENTITY.md` | Full identity, role, design principles, outfit system |
| `DESIGN-SYSTEM.md` | Token reference — color, typography, spacing |
| `briefs/` | Design briefs authored for Vulcan and teammates |
| `designs/` | Design specs and wireframes |
| `design-system/` | Shared design tokens and component standards |
| `memories/004-css-discipline.md` | Three CSS rules — read before any CSS work |
| `visions/` | Generated visual references and design explorations |
| `outfits/` | Outfit configs and palette exploration |
