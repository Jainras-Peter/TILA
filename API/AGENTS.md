# TILA Backend (agent)

Takes precedence for files under `API/`. Root rules: [../AGENTS.md](../AGENTS.md).

## Read first

1. [../docs/backend.md](../docs/backend.md)
2. [../docs/ai.md](../docs/ai.md) for LLM/RAG
3. [../docs/persistence.md](../docs/persistence.md) for Mongo
4. [../docs/errors.md](../docs/errors.md) and [../docs/config.md](../docs/config.md)

## Layering

`api/v1 → controllers → services → repositories → core/database`

- Controllers: HTTP only
- Services: no FastAPI domain imports
- Repositories: only Mongo access
- LLM: `app/ai/gateway` only

## Scaffold reality

Many files under `app/` are empty placeholders. Prefer implementing the closest existing pattern (gateway is the best reference). Do not invent a parallel architecture.

## Commands

```bash
make run    # or from repo root: npm run dev:api
make test
make lint
```
