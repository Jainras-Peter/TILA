# Agent notes

TILA is a modular Angular + FastAPI learning platform. Read these before changing data access or boundaries:

1. [docs/vision.md](../docs/vision.md)
2. [docs/architecture.md](../docs/architecture.md)
3. [docs/backend.md](../docs/backend.md)
4. [docs/frontend.md](../docs/frontend.md)
5. [docs/persistence.md](../docs/persistence.md)
6. [docs/collections/README.md](../docs/collections/README.md)
7. [docs/ai.md](../docs/ai.md)
8. [AGENTS.md](../AGENTS.md)

Locked flow: Router → Controller → Service → Repository. Only repositories query Mongo. LLM calls go through `app/ai/gateway`.

Naming: collections and fields `camelCase`; closed-set values `SCREAMING_SNAKE`. Scope user data by `userId`.

Memory of prior work: [docs/brain/README.md](../docs/brain/README.md).
