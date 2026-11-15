# TILA architecture (agent)

Canonical docs:

- [docs/vision.md](../docs/vision.md)
- [docs/architecture/overview.md](../docs/architecture/overview.md)
- [docs/architecture/backend-architecture.md](../docs/architecture/backend-architecture.md)
- [docs/architecture/frontend-architecture.md](../docs/architecture/frontend-architecture.md)
- [docs/architecture/ai-architecture.md](../docs/architecture/ai-architecture.md)
- [docs/architecture/data-flow.md](../docs/architecture/data-flow.md)
- [docs/architecture/dependency-map.md](../docs/architecture/dependency-map.md)
- [docs/architecture/persistence.md](../docs/architecture/persistence.md)
- [docs/architecture/jobs.md](../docs/architecture/jobs.md)

When adding a Mongo collection or data-access path, follow `docs/architecture/persistence.md`: repository only; camelCase collections/fields; SCREAMING_SNAKE enums. Do not query Mongo from routes, controllers, or the frontend.

Load feature context via `docs/context-routing.json`, not the entire docs tree.
