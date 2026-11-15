# Backend

Python 3.12 + FastAPI. Package root: `API/app`.

## Layers

| Layer | Path | Allowed dependency | Must not |
|-------|------|--------------------|----------|
| Routes | `app/api/v1/*.py` | Controllers | Services, repositories |
| Controllers | `app/controllers/` | Services | Repositories, motor |
| Services | `app/services/` | Repositories, AI gateway, domain | FastAPI, motor |
| Repositories | `app/repositories/` | Database / motor / domain | Controllers, services |
| AI gateway | `app/ai/gateway/` | External LLM SDKs (HTTP) | Used as the only LLM door |
| Core | `app/core/` | Config / infrastructure | — |
| Factories | `app/factories/` | Embeddings, vector, loaders, chunkers | Second LLM stack |
| Workers | `app/workers/` | Services | — |

Services may orchestrate without a repository (external calls, pure orchestration).

**Executable:** `API/tests/unit/architecture/test_import_boundaries.py` (AST). Shrink `ROUTE_ALLOWLIST` over time (`auth.py` / `users.py` currently mount FastAPI Users routers directly).

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
cd API && venv/bin/pytest tests/unit/architecture -q
```

From root: `npm run test:api`, `npm run test:arch`, `npm run lint`, `npm run check`.

Pre-commit (lint-staged): `ruff check --fix` + `ruff format` on staged Python.  
CI / `npm run check`: verify only (`ruff check`, `ruff format --check`, arch tests).
