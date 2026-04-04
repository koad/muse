# Design Specification: Entity Card Component
**Issue:** koad/muse#5  
**Date:** 2026-04-04  
**Appears in:** Namespace showcase (homepage), MVP Zone directory, search results, activity feeds, team section.

---

## Anatomy (All Variants)

```
┌─────────────────────────────────┐
│  ●  [Avatar 48px]               │  ← Online dot: absolute top-right of avatar
│     Name Displayname            │  ← Inter 600, --text-primary
│     username.koad.io            │  ← JetBrains Mono, --text-secondary, clickable
│     Brief bio text here (opt.)  │  ← Inter 400, --text-secondary, 2-line max
│     [View keys]  2m ago         │  ← action + timestamp (variant-dependent)
└─────────────────────────────────┘
```

**Base tokens (no skin overrides):**
```css
--card-bg:        var(--bg-secondary)   /* #141418 */
--card-border:    var(--border)         /* #2a2a32 */
--card-radius:    8px
--card-padding:   16px
--avatar-size:    48px
--avatar-ring:    2px solid var(--border)
--online-size:    8px
--online-color:   var(--success)        /* #4ade80 */
```

---

## Variant 1: Showcase Card

Used in the homepage namespace showcase (6-card grid).

```
┌────────────────────────────────────┐
│  ● [Avatar]  Vulcan                │
│              vulcan.koad.io        │
│                                    │
│              [View keys →]         │
└────────────────────────────────────┘
```

- No bio
- "View keys" text button — links to namespace page `#keys` anchor
- Online indicator always shown (showcase = active entities only)
- Width: ~180px (fits 6-up on desktop, 2-up on mobile)

**Blaze template:**
```html
{{> entityCardShowcase entity=entity}}
```

```html
<template name="entityCardShowcase">
  <a class="entity-card entity-card--showcase" href="{{entity.namespaceUrl}}">
    <div class="entity-card__avatar-wrap">
      <img class="entity-card__avatar"
           src="{{entity.avatarUrl}}"
           alt="{{entity.displayName}}"
           width="48" height="48" />
      {{#if entity.isOnline}}
        <span class="entity-card__online" aria-label="Online"></span>
      {{/if}}
    </div>
    <div class="entity-card__body">
      <span class="entity-card__name">{{entity.displayName}}</span>
      <span class="entity-card__username">{{entity.username}}.koad.io</span>
      <a class="entity-card__action" href="{{entity.namespaceUrl}}#keys">
        View keys →
      </a>
    </div>
  </a>
</template>
```

---

## Variant 2: Directory Card

Used in MVP Zone directory and namespace search results. Larger, includes bio.

```
┌────────────────────────────────────────────────┐
│  ● [Avatar]  Vulcan                            │
│              vulcan.koad.io          2m ago    │
│                                                │
│  Builds the infra. Ships the daemon. Keeps     │
│  the keys working.                             │
└────────────────────────────────────────────────┘
```

- Full bio (1–2 lines, 80 char soft wrap)
- Timestamp (relative, right-aligned)
- Entire card is clickable to namespace page
- Width: fluid (fills column), min 280px

**Blaze template:**
```html
{{> entityCardDirectory entity=entity}}
```

```html
<template name="entityCardDirectory">
  <a class="entity-card entity-card--directory" href="{{entity.namespaceUrl}}">
    <div class="entity-card__avatar-wrap">
      <img class="entity-card__avatar"
           src="{{entity.avatarUrl}}"
           alt="{{entity.displayName}}"
           width="48" height="48" />
      {{#if entity.isOnline}}
        <span class="entity-card__online" aria-label="Online"></span>
      {{/if}}
    </div>
    <div class="entity-card__body">
      <div class="entity-card__header">
        <span class="entity-card__name">{{entity.displayName}}</span>
        <span class="entity-card__username">{{entity.username}}.koad.io</span>
        <span class="entity-card__timestamp">{{entity.lastSeenRelative}}</span>
      </div>
      {{#if entity.bio}}
        <p class="entity-card__bio">{{entity.bio}}</p>
      {{/if}}
    </div>
  </a>
</template>
```

---

## Variant 3: Activity Card

Used in real-time feeds and communication log. Compact — single line with context.

```
  ● [Avatar 32px]  Vulcan  published koad-io v0.3.1  ·  3m ago
```

- Avatar: 32px (not 48px)
- Name + action text inline
- No bio, no domain display (implied context)
- Not a standalone card — used as list item within feed component

**Blaze template:**
```html
{{> entityCardActivity event=event}}
```

```html
<template name="entityCardActivity">
  <li class="entity-card entity-card--activity">
    <div class="entity-card__avatar-wrap entity-card__avatar-wrap--sm">
      <img class="entity-card__avatar entity-card__avatar--sm"
           src="{{event.entity.avatarUrl}}"
           alt="{{event.entity.displayName}}"
           width="32" height="32" />
      {{#if event.entity.isOnline}}
        <span class="entity-card__online entity-card__online--sm" aria-label="Online"></span>
      {{/if}}
    </div>
    <div class="entity-card__body">
      <span class="entity-card__name">{{event.entity.displayName}}</span>
      <span class="entity-card__action-text">{{event.actionText}}</span>
      <span class="entity-card__timestamp">{{event.timestampRelative}}</span>
    </div>
  </li>
</template>
```

---

## Variant 4: Team Card

Used in the koad:io team section (homepage, about pages). Larger format, shows entity role.

```
┌────────────────────────────────────────────────┐
│                                                │
│          ● [Avatar 64px]                       │
│                                                │
│          Vulcan                                │
│          vulcan.koad.io                        │
│          Builds infrastructure.                │
│          Ships the daemon.                     │
│                                                │
│          [View namespace →]                    │
└────────────────────────────────────────────────┘
```

- Avatar: 64px, centered
- Name centered, Inter 700
- Bio: 2–3 lines, centered
- CTA: "View namespace →"
- Online indicator on avatar (top-right)
- Layout: card is centered vertically, used in horizontal scroll or 3-up grid

**Blaze template:**
```html
{{> entityCardTeam entity=entity}}
```

---

## CSS

```css
/* Base */
.entity-card {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: var(--card-padding);
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: var(--card-radius);
  text-decoration: none;
  color: inherit;
  transition: transform 80ms ease, border-color 80ms ease;
}

.entity-card:hover {
  transform: translateY(-2px);
  border-color: var(--text-secondary);
}

.entity-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* Avatar */
.entity-card__avatar-wrap {
  position: relative;
  flex-shrink: 0;
  width: 48px;
  height: 48px;
}

.entity-card__avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 2px solid var(--border);
  display: block;
  background: var(--bg-tertiary);
}

/* Online dot */
.entity-card__online {
  position: absolute;
  top: 0;
  right: 0;
  width: 8px;
  height: 8px;
  background: var(--success);
  border-radius: 50%;
  border: 2px solid var(--bg-secondary);
}

/* Body text */
.entity-card__name {
  display: block;
  font-family: Inter, system-ui, sans-serif;
  font-size: 0.9375rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.3;
}

.entity-card__username {
  display: block;
  font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size: 0.75rem;
  color: var(--text-secondary);
  line-height: 1.4;
}

.entity-card__bio {
  margin: 6px 0 0;
  font-size: 0.8125rem;
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.entity-card__timestamp {
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.entity-card__action {
  display: inline-block;
  margin-top: 8px;
  font-size: 0.8125rem;
  color: var(--accent);
  text-decoration: none;
}

.entity-card__action:hover {
  text-decoration: underline;
}

/* Directory header layout */
.entity-card--directory .entity-card__header {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 6px;
}

.entity-card--directory .entity-card__timestamp {
  margin-left: auto;
}

/* Small variants (activity) */
.entity-card--activity {
  padding: 8px 0;
  border: none;
  border-radius: 0;
  background: transparent;
}

.entity-card--activity:hover {
  transform: none;
  border-color: transparent;
  background: var(--bg-secondary);
  border-radius: var(--card-radius);
  padding: 8px 12px;
  margin: 0 -12px;
}

.entity-card__avatar-wrap--sm { width: 32px; height: 32px; }
.entity-card__avatar--sm { width: 32px; height: 32px; }
.entity-card__online--sm { width: 6px; height: 6px; }

/* Team card */
.entity-card--team {
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.entity-card--team .entity-card__avatar-wrap {
  width: 64px;
  height: 64px;
}

.entity-card--team .entity-card__avatar {
  width: 64px;
  height: 64px;
}

/* Showcase: compact, no bio */
.entity-card--showcase {
  flex-direction: column;
  gap: 8px;
  min-width: 160px;
}
```

---

## Interaction States

| State | Behavior |
|-------|----------|
| Default | Static, no animation |
| Hover | `translateY(-2px)`, border brightens to `--text-secondary` |
| Focus (keyboard) | 2px `--accent` outline, 2px offset |
| Active (mousedown) | `translateY(0)` — snaps back |
| Loading (avatar) | `--bg-tertiary` placeholder behind `<img>` |
| Offline (no online dot) | Online element simply absent — no grey dot |

---

## Accessibility

- Entire card is an `<a>` for showcase and directory variants — one focusable element per card.
- Activity variant is `<li>` with keyboard-reachable entity name as a link.
- Online indicator: `aria-label="Online"`, not announced redundantly via card label.
- Avatar has alt text = display name.
- Bio text is not truncated via CSS alone — 2-line clamp is visual; full text in DOM for screen readers.

---

## Responsive Behavior

**Showcase (homepage grid):**
- Desktop: 6 cards across (auto grid, min-width 160px)
- Tablet: 3-4 cards
- Mobile: 2 cards (compact, no action text)

**Directory:**
- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column (full width)

**Team:**
- Desktop: 3 columns
- Mobile: 1 column

---

## Implementation Notes for Vulcan

- Avatar fallback: if `avatarUrl` is null, render initials in `--bg-tertiary` circle.
- `lastSeenRelative` and `isOnline` should come from same reactive data source — avoid out-of-sync states.
- Activity cards are rendered inside a `<ul>` with `list-style: none` — template handles `<li>` wrapping.
- No images other than avatar. No icon libraries needed.
- CSS file goes in design system layer, not component-specific CSS — these tokens are shared.
