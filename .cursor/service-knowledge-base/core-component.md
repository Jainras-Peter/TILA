# Core components

| Component | Location | Role |
|-----------|----------|------|
| FastAPI app | `API/app/main.py` | App entry, CORS, router mount |
| LLM Gateway | `API/app/ai/gateway/` | Main + fallback LLM with retries |
| API v1 router | `API/app/api/v1/` | Versioned REST routes (mostly scaffold) |
| Controllers / Services / Repositories | `app/controllers`, `services`, `repositories` | Layered backend (mostly scaffold) |
| Angular app | `Web/src/app/` | SPA shell |
| Landing | `features/landing/` | Working marketing/landing page |
| Navbar | `layout/navbar/` | Working chrome |
| ApiService / AuthService | `core/services/` | Shared HTTP and auth (scaffold) |
| Dev runner | `TILA/package.json` | `npm run dev` starts API + web |

Implemented today: LLM gateway (+ tests), landing page, navbar, folder scaffolding. Most other modules are empty placeholders.
