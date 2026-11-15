# TILA docs (agent)

Canonical docs — read before working in the relevant area:

- [docs/vision.md](docs/vision.md) — product purpose and hard boundaries
- [docs/architecture.md](docs/architecture.md) — Angular + FastAPI + Mongo + RAG
- [docs/backend.md](docs/backend.md) — layering; **read before adding an endpoint**
- [docs/frontend.md](docs/frontend.md) — SPA structure and data flow
- [docs/persistence.md](docs/persistence.md) — Mongo naming and repository rules
- [docs/collections/README.md](docs/collections/README.md) — collections, fields, indexes
- [docs/ai.md](docs/ai.md) — **read before any LLM/RAG change**; gateway is canonical
- [docs/errors.md](docs/errors.md) — error envelope and exceptions
- [docs/config.md](docs/config.md) — env → settings; no ad-hoc getenv
- [docs/jobs.md](docs/jobs.md) — **read before adding a background job**
- [docs/design.md](docs/design.md) — **read before any UI change**
- [docs/brain/README.md](docs/brain/README.md) — how prior work is remembered

## Workspace structure

| Path | Role |
|------|------|
| `API/` | FastAPI API, AI gateway, workers |
| `Web/` | Angular SPA |
| `docs/` | Canonical product/tech docs + brain |
| `.cursor/` | Agent pointers, rules, commands, hooks |
| `.agents/skills/` | Reusable implementation skills |

Dependency direction (backend):

`api → controllers → services → repositories → core/database`

AI leaves services only via `app/ai/gateway` and `app/factories/*` (embeddings, vector, loaders, chunkers — not a second LLM stack).

Forbidden:

- Controllers with business logic
- Services importing FastAPI for domain logic
- Mongo access outside repositories
- New LLM clients outside `app/ai/gateway`
- Extending `app/ai/llm/*` or `app/factories/llm_factory.py` (legacy overlap; see gaps)
- `os.getenv` outside central config (see [docs/config.md](docs/config.md))
- Frontend components using raw `HttpClient` / `fetch`
- Raw hex colours / one-off type sizes when tokens exist in [docs/design.md](docs/design.md)

## Config

Settings live in `API/app/core/config.py` (target) and env via `API/.env`. See [docs/config.md](docs/config.md).

## Persistence naming

When adding or changing Mongo state, follow [docs/persistence.md](docs/persistence.md):

- Collections and fields: `camelCase`
- Closed-set values: `SCREAMING_SNAKE`
- Every user-owned query filters by `userId`

## Errors

Raise typed exceptions from `app/core/exceptions.py`. Map to the envelope in [docs/errors.md](docs/errors.md). Do not leak internals.

## LLM / AI

`app/ai/gateway` is the only LLM door. RAG and document processing use factories. Details: [docs/ai.md](docs/ai.md).

## Frontend data

Data flows through feature `*-feature.service.ts` and `core/services/api.service.ts`. Standalone components only. See [docs/frontend.md](docs/frontend.md).

## Dev commands

From repo root (`TILA/`):

```bash
npm run setup    # once
npm run dev      # API :8000 + Angular :4200
npm run check    # ruff + tsc
```

## Feature workflow

1. `/start-task <feature-slug>` — load brain + create/read task-history
2. `/analyse` — read-only plan from existing patterns
3. Human approves the plan
4. `/dotask` — implement only the approved plan
5. `/checkcode` — pre-PR review
6. `/handoff` — append task-history, update roadmap/gaps/ADRs as needed

## Module-level AGENTS.md

`API/AGENTS.md` and `Web/AGENTS.md` take precedence for work in those folders. Read them before editing files there.
