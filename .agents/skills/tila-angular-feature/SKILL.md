---
name: tila-angular-feature
description: Add an Angular standalone feature (model, feature service, page, route) following TILA frontend conventions.
---

# TILA Angular feature

Use when adding UI under `Web`.

## Preconditions

Read `docs/frontend.md`, `docs/design.md`, and `Web/AGENTS.md`. Use landing/navbar as live references.

## Steps

1. **Model** — `src/app/core/models/<name>.model.ts` if needed.
2. **API access** — methods on `ApiService` and/or `features/<name>/services/<name>-feature.service.ts`.
3. **Page** — standalone component under `features/<name>/pages/`.
4. **Route** — register in `app.routes.ts` with `authGuard` / `guestGuard` as appropriate.
5. **Shared UI** — only move to `shared/components` when reused twice+.
6. **Cleanup** — `takeUntilDestroyed` for subscriptions; follow design tokens.
7. **Handoff** — append `docs/brain/task-history/<slug>.md`.

## Do not

- Use `HttpClient` or `fetch` directly in components.
- Create NgModules for new features.
- Copy Atlas React/shadcn patterns into Angular.
