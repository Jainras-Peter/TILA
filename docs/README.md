# TILA docs (Context Engineering)

Agents must **not** load every document. Resolve a route from [context-routing.json](context-routing.json), then read only `default` + that route’s `always` (and `optional` when UI/design is in scope). Skill: `.agents/skills/tila-context/SKILL.md`.

## Layout

| Area | Purpose |
|------|---------|
| [architecture/](architecture/) | How the whole system works |
| [modules/](modules/) | How individual features work |
| [decisions/](decisions/) | Why a particular approach was chosen (ADRs) |
| [brain/](brain/) | What happened during development (roadmap, gaps, task-history) |
| [vision.md](vision.md) | Product purpose and hard boundaries |
| [archive/](archive/) | Historical source docs (not primary) |

## Architecture

| Doc | When |
|-----|------|
| [architecture/overview.md](architecture/overview.md) | System shape |
| [architecture/backend-architecture.md](architecture/backend-architecture.md) | Before adding an endpoint |
| [architecture/frontend-architecture.md](architecture/frontend-architecture.md) | Before SPA work |
| [architecture/ai-architecture.md](architecture/ai-architecture.md) | Before LLM/RAG changes |
| [architecture/data-flow.md](architecture/data-flow.md) | Auth / ingest / RAG / chat flows |
| [architecture/dependency-map.md](architecture/dependency-map.md) | Blast radius before changing a module |
| [architecture/persistence.md](architecture/persistence.md) | Mongo naming and repositories |
| [architecture/collections/README.md](architecture/collections/README.md) | Collections and indexes |
| [architecture/errors.md](architecture/errors.md) | Error envelope |
| [architecture/config.md](architecture/config.md) | Env → settings |
| [architecture/jobs.md](architecture/jobs.md) | Background workers |
| [architecture/design.md](architecture/design.md) | UI tokens |

## Modules

| Doc | Status |
|-----|--------|
| [modules/auth.md](modules/auth.md) | partial / implemented MVP |
| [modules/notebooks.md](modules/notebooks.md) | scaffold |
| [modules/documents.md](modules/documents.md) | scaffold |
| [modules/rag.md](modules/rag.md) | scaffold |
| [modules/chat.md](modules/chat.md) | scaffold |

## Decisions

| ADR | Topic |
|-----|--------|
| [ADR-0001](decisions/ADR-0001-llm-gateway-canonical.md) | LLM gateway canonical |
| [ADR-0002](decisions/ADR-0002-dev-runner.md) | npm + concurrently runner |
| [ADR-0003](decisions/ADR-0003-fastapi-users-cookie-db.md) | FastAPI Users cookie + DB sessions |

## Brain

| Doc | Purpose |
|-----|---------|
| [brain/README.md](brain/README.md) | How memory works |
| [brain/roadmap.md](brain/roadmap.md) | Phase status |
| [brain/gaps.md](brain/gaps.md) | Open gaps / risks |
| [brain/task-history/](brain/task-history/) | Append-only feature logs |

## Workflow

`/StartTask` → resolve routing → load context → `/MakePlan` → approve → `/ImplementPlan` → `/ReviewCode` / `/TestCode` → `/Handoff`.
