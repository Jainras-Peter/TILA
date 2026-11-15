# Data store

- **Application SoR:** MongoDB (Motor). Connection owned by `app/core/database.py`.
- **Access:** repositories only (`app/repositories/*`).
- **Naming:** camelCase collections/fields; SCREAMING_SNAKE enums. See `docs/persistence.md`.
- **Ownership:** filter by `userId` for user resources.
- **Collections:** listed in `docs/collections/README.md` (users, notebooks, documents, documentChunks, conversations, messages, refreshTokens).
- **Vectors:** separate vector store abstraction (`app/ai/vectorstores`); chunk metadata may live in Mongo.
- **Files:** storage abstraction (`app/storage`) — local now, S3 later; do not keep durable blobs only on ephemeral disk in production designs.
- **docker-compose Mongo:** not filled yet — see `docs/brain/gaps.md`.
