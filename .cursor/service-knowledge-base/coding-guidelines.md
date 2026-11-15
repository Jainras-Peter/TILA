# Coding guidelines

- Prefer existing project patterns over generic industry patterns.
- Backend layering: router → controller → service → repository.
- Controllers have no business logic; services do not import FastAPI for domain work.
- LLM: `app/ai/gateway` only. Do not extend `app/ai/llm/*`.
- Config via `app/core/config.py` / `.env` — no scattered `os.getenv`.
- Errors: typed exceptions + envelope (`docs/errors.md`).
- Frontend: standalone components; HTTP through `ApiService` / feature services.
- Subscriptions: `takeUntilDestroyed`.
- Tests: pytest (backend), follow existing test layout under `tests/`.
- Lint: `ruff` for Python; `tsc --noEmit` for Angular.
- Feature workflow: start-task → analyse → approve → dotask → checkcode → handoff.
