# TILA architecture (agent)

Canonical docs:

- [docs/vision.md](../docs/vision.md)
- [docs/architecture.md](../docs/architecture.md)
- [docs/backend.md](../docs/backend.md)
- [docs/frontend.md](../docs/frontend.md)
- [docs/persistence.md](../docs/persistence.md)
- [docs/ai.md](../docs/ai.md)
- [docs/jobs.md](../docs/jobs.md)

When adding a Mongo collection or data-access path, follow `docs/persistence.md`: repository only; camelCase collections/fields; SCREAMING_SNAKE enums. Do not query Mongo from routes, controllers, or the frontend.
