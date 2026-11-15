# TILA Backend

FastAPI backend for TILA (Teaching & Intelligent Learning Assistant).

## Quick start

From the repo root (`TILA/`):

```bash
npm run setup:api
npm run dev:api
```

API: `http://localhost:8000`  
Docs: `http://localhost:8000/docs`  
LLM gateway test: `GET /llm?prompt=hello`

## Layout

- `app/api` — route definitions
- `app/controllers` — HTTP adapters
- `app/services` — business logic
- `app/repositories` — Mongo access
- `app/ai/gateway` — canonical LLM door (retries + fallback)
- `app/core` — config, security, exceptions, database

See [../AGENTS.md](../AGENTS.md) and [../docs/architecture/backend-architecture.md](../docs/architecture/backend-architecture.md).
