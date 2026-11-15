# Frontend

Angular 18 standalone + Tailwind. Package root: `Web/src/app`.

## Structure

| Area | Path | Role |
|------|------|------|
| Core | `core/` | Guards, interceptors, models, `ApiService`, `AuthService`, `ThemeService` |
| Features | `features/<name>/` | Pages, components, `*-feature.service.ts` |
| Layout | `layout/` | Navbar, sidebar, footer |
| Shared | `shared/` | Reusable UI, pipes, directives |
| Environments | `environments/` | `apiBaseUrl` |

## Data flow

```text
Page / Component
  → FeatureService (features/*/services)
  → ApiService (core/services/api.service.ts)
  → HttpClient (+ auth / error interceptors)
  → /api/v1/* (proxied to :8000 in dev)
```

Rules:

- Standalone components only.
- No raw `HttpClient` in components or pages.
- Models live in `core/models`.
- Use `takeUntilDestroyed` for subscriptions.
- Feature folders: `pages/`, `components/`, `services/` as needed. No barrel files required.

## Recipe: add a feature

1. Model in `core/models/<name>.model.ts` if new entity.
2. Methods on `ApiService` or a focused feature service.
3. Standalone page component under `features/<name>/pages/`.
4. Route in `app.routes.ts` with guard if authenticated.
5. Shared UI in `shared/components` only when reused twice+.
6. Follow [design.md](design.md) tokens.

Skill: `.agents/skills/tila-angular-feature/SKILL.md`.

## Dev

```bash
npm run setup:web
npm run dev:web   # :4200, proxy /api and /llm → :8000
```

`environment.development.ts` and `environment.ts` set `apiBaseUrl: '/api/v1'`.
