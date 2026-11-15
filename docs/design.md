# Design

TILA is a calm learning product UI: clear hierarchy, accessible contrast, Tailwind utility classes.

## Tokens (establish in `styles/` as you build)

Prefer CSS variables / Tailwind theme keys over raw hex in components:

| Role | Use |
|------|-----|
| Background | Page / surface |
| Foreground | Primary text |
| Muted | Secondary text, hints |
| Accent | Primary CTA |
| Destructive | Delete / errors |
| Border | Dividers |

Avoid inventing one-off palette colours per feature. If a token is missing, add it to the shared styles once.

## Typography

Use a small set of size/weight roles (e.g. display, title, body, caption) via Tailwind classes defined in the shared stylesheet — do not sprinkle arbitrary `text-[13px]` in feature templates.

## Components

- Shared primitives live in `shared/components`.
- Layout chrome in `layout/`.
- Feature-specific UI stays under `features/<name>/components`.
- Loading / empty / error states should be consistent across features.

## Motion

Use motion sparingly for presence (page enter, chat message appear). Prefer CSS/Angular animations already in the project over new libraries.

## Brand test

Landing and first authenticated shell should read as TILA, not a generic dashboard template.
