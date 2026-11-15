# TILA Frontend (agent)

Takes precedence for files under `Web/`. Root rules: [../AGENTS.md](../AGENTS.md).

## Read first

1. [../docs/frontend.md](../docs/frontend.md)
2. [../docs/design.md](../docs/design.md) before UI changes
3. Landing + navbar under `src/app/features/landing` and `src/app/layout/navbar` as the best live UI patterns

## Rules

- Standalone components only
- HTTP via `ApiService` / feature services — not raw `HttpClient` in templates/components
- Models in `core/models`
- `takeUntilDestroyed` for subscriptions
- Dev proxy: `proxy.conf.json` (`/api`, `/llm` → `:8000`)

## Scaffold reality

Most feature folders are `.gitkeep` placeholders. Landing page is the working reference. Follow its structure when adding pages.

## Commands

```bash
npm start -- --proxy-config proxy.conf.json
# or from repo root: npm run dev:web
```
