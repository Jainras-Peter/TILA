# Agent notes

TILA is a modular Angular + FastAPI learning platform. Prefer selective context via `docs/context-routing.json` (see `.agents/skills/tila-context/SKILL.md`).

Short pointers:

1. [docs/vision.md](../docs/vision.md)
2. [docs/architecture/overview.md](../docs/architecture/overview.md)
3. [docs/architecture/backend-architecture.md](../docs/architecture/backend-architecture.md)
4. [docs/architecture/frontend-architecture.md](../docs/architecture/frontend-architecture.md)
5. [docs/architecture/persistence.md](../docs/architecture/persistence.md)
6. [docs/architecture/ai-architecture.md](../docs/architecture/ai-architecture.md)
7. [docs/architecture/dependency-map.md](../docs/architecture/dependency-map.md)
8. [AGENTS.md](../AGENTS.md)

Locked flow: Router → Controller → Service → Repository. Only repositories query Mongo. LLM calls go through `app/ai/gateway`.

Naming: collections and fields `camelCase`; closed-set values `SCREAMING_SNAKE`. Scope user data by `userId` (Auth collections follow FastAPI Users / Beanie).

Memory: [docs/brain/README.md](../docs/brain/README.md). Decisions: [docs/decisions/](../docs/decisions/).
