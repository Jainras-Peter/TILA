---
name: tila-backend-endpoint
description: Add a FastAPI endpoint end-to-end using TILA layering (schema → route → controller → service → repository → test).
---

# TILA backend endpoint

Use when adding or extending a REST API under `API`.

## Preconditions

Read `docs/backend.md`, `docs/errors.md`, `docs/persistence.md`, and `API/AGENTS.md`.

## Steps

1. **Schema** — Pydantic models in `app/schemas/<domain>.py`.
2. **Repository** — if persistence changes, methods on `app/repositories/<domain>_repository.py` (Mongo only; filter `userId` when owned).
3. **Service** — business logic in `app/services/<domain>_service.py`; raise typed exceptions; call gateway for LLM, never vendor SDKs.
4. **Controller** — `app/controllers/<domain>_controller.py` maps request → service → response.
5. **Route** — `app/api/v1/<domain>.py`; wire auth deps; ensure router included from `app/api/v1/router.py` / `main.py`.
6. **Test** — service unit test and/or route test under `tests/`.
7. **Docs** — update `docs/collections/README.md` if a collection/index changed; append task-history via `/handoff`.

## Do not

- Put business logic in routes/controllers.
- Query Mongo outside repositories.
- Add a second LLM client stack.
- Invent folders outside the existing layout.
