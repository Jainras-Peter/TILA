# Backend

Python 3.12 + FastAPI. Package root: `API/app`.

## Layers

| Layer | Path | Responsibility |
|-------|------|----------------|
| Routes | `app/api/v1/*.py` | Path, method, deps wiring; no logic |
| Controllers | `app/controllers/` | Parse/validate HTTP, call service, map to response |
| Services | `app/services/` | Business rules; no FastAPI imports for domain |
| Repositories | `app/repositories/` | Mongo only |
| Core | `app/core/` | Config, DB, security, exceptions, logging, lifespan |
| Middleware | `app/middleware/` | Auth, CORS, errors, rate limit, request id |
| AI gateway | `app/ai/gateway/` | Only LLM door |
| Factories | `app/factories/` | Embeddings, vector stores, loaders, chunkers |
| Workers | `app/workers/` | Background jobs |

## API versioning

Base: `/api/v1`. Domains: `auth`, `users`, `notebooks`, `documents`, `chat`, `search`, `ai`, `health`.

## Recipe: add an endpoint

1. Schema in `app/schemas/<domain>.py` (Pydantic).
2. Repository method in `app/repositories/<domain>_repository.py` if persistence changes.
3. Service method in `app/services/<domain>_service.py`.
4. Controller method in `app/controllers/<domain>_controller.py`.
5. Route in `app/api/v1/<domain>.py`; register on `app/api/v1/router.py` if new.
6. Auth dependency from `app/dependencies/auth.py` when protected.
7. Test under `tests/` (unit for service; integration for route when ready).
8. Raise typed exceptions from `app/core/exceptions.py` — never raw HTTPException for domain errors (except temporary legacy gateway routes).

Skill: `.agents/skills/tila-backend-endpoint/SKILL.md`.

## Config and errors

- Settings: [config.md](config.md) — `app/core/config.py` only.
- Errors: [errors.md](errors.md).

## Tests and lint

```bash
cd API && venv/bin/pytest
cd API && venv/bin/ruff check app tests
```

From root: `npm run test:api`, `npm run lint`.
