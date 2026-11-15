# TILA docs (agent)

Do **not** load every doc. Resolve a route from [docs/context-routing.json](docs/context-routing.json) via `.agents/skills/tila-context/SKILL.md`, then read only those paths. Index: [docs/README.md](docs/README.md).

Canonical docs by area:

- [docs/vision.md](docs/vision.md) — product purpose and hard boundaries
- [docs/architecture/overview.md](docs/architecture/overview.md) — Angular + FastAPI + Mongo + RAG
- [docs/architecture/backend-architecture.md](docs/architecture/backend-architecture.md) — layering; **read before adding an endpoint**
- [docs/architecture/frontend-architecture.md](docs/architecture/frontend-architecture.md) — SPA structure and data flow
- [docs/architecture/ai-architecture.md](docs/architecture/ai-architecture.md) — **read before any LLM/RAG change**; gateway is canonical
- [docs/architecture/data-flow.md](docs/architecture/data-flow.md) — Auth / ingest / RAG / chat flows
- [docs/architecture/dependency-map.md](docs/architecture/dependency-map.md) — blast radius before changing a module
- [docs/architecture/persistence.md](docs/architecture/persistence.md) — Mongo naming and repository rules
- [docs/architecture/collections/README.md](docs/architecture/collections/README.md) — collections, fields, indexes
- [docs/architecture/errors.md](docs/architecture/errors.md) — error envelope and exceptions
- [docs/architecture/config.md](docs/architecture/config.md) — env → settings; no ad-hoc getenv
- [docs/architecture/jobs.md](docs/architecture/jobs.md) — **read before adding a background job**
- [docs/architecture/design.md](docs/architecture/design.md) — **read before any UI change**
- [docs/modules/](docs/modules/) — per-feature ownership and contracts
- [docs/decisions/](docs/decisions/) — ADRs (why)
- [docs/brain/README.md](docs/brain/README.md) — roadmap / gaps / task-history (what happened)

## Workspace structure

| Path | Role |
|------|------|
| `API/` | FastAPI API, AI gateway, workers |
| `Web/` | Angular SPA |
| `docs/` | Architecture, modules, decisions, brain |
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
- `os.getenv` outside central config (see [docs/architecture/config.md](docs/architecture/config.md))
- Frontend components using raw `HttpClient` / `fetch`
- Raw hex colours / one-off type sizes when tokens exist in [docs/architecture/design.md](docs/architecture/design.md)

## Config

Settings live in `API/app/core/config.py` (target) and env via `API/.env`. See [docs/architecture/config.md](docs/architecture/config.md).

## Persistence naming

When adding or changing Mongo state, follow [docs/architecture/persistence.md](docs/architecture/persistence.md):

- Collections and fields: `camelCase`
- Closed-set values: `SCREAMING_SNAKE`
- Every user-owned query filters by `userId`
- Auth collections (`users`, `accessTokens`) follow FastAPI Users / Beanie naming (ADR-0003)

## Errors

Raise typed exceptions from `app/core/exceptions.py`. Map to the envelope in [docs/architecture/errors.md](docs/architecture/errors.md). Do not leak internals.

## LLM / AI

`app/ai/gateway` is the only LLM door. RAG and document processing use factories. Details: [docs/architecture/ai-architecture.md](docs/architecture/ai-architecture.md).

## Frontend data

Data flows through feature `*-feature.service.ts` and `core/services/api.service.ts`. Standalone components only. See [docs/architecture/frontend-architecture.md](docs/architecture/frontend-architecture.md).

## Dev commands

From repo root (`TILA/`):

```bash
npm run setup    # once
npm run dev      # API :8000 + Angular :4200
npm run lint     # ruff + eslint (verify)
npm run check    # lint + format --check + arch tests + tsc
```

**Architecture is executable:** Web ESLint and API AST tests enforce AGENTS rules.  
`git commit` runs Husky → lint-staged (auto-fix staged files). Do **not** use `--no-verify`.  
CI (`.github/workflows/check.yml`) runs full `npm run check` so hooks cannot be bypassed on merge.

## Feature workflow

1. `/StartTask <feature-slug>` — context-routing + brain + task-history
2. `/MakePlan` — read-only plan (cite dependency-map when relevant)
3. Human approves the plan
4. `/ImplementPlan` — implement only the approved plan
5. `/ReviewCode` then `/TestCode`
6. `/Handoff` — append task-history; update roadmap/gaps/ADRs as needed

## Module-level AGENTS.md

`API/AGENTS.md` and `Web/AGENTS.md` take precedence for work in those folders. Read them before editing files there.
