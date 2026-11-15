# TILA Backend (agent)

Takes precedence for files under `API/`. Root rules: [../AGENTS.md](../AGENTS.md).

## Read first

Prefer `docs/context-routing.json` for the feature slug. At minimum:

1. [../docs/architecture/backend-architecture.md](../docs/architecture/backend-architecture.md)
2. [../docs/architecture/ai-architecture.md](../docs/architecture/ai-architecture.md) for LLM/RAG
3. [../docs/architecture/persistence.md](../docs/architecture/persistence.md) for Mongo
4. [../docs/architecture/errors.md](../docs/architecture/errors.md) and [../docs/architecture/config.md](../docs/architecture/config.md)
5. [../docs/architecture/dependency-map.md](../docs/architecture/dependency-map.md) for blast radius

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
