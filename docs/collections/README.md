# Collections

Mongo collections for TILA. Auth collections are owned by **FastAPI Users + Beanie**; other app collections stay Motor repositories with camelCase fields (see [persistence.md](../persistence.md)).

| Collection | Purpose | Key fields | Indexes |
|------------|---------|------------|---------|
| `users` | Accounts (FastAPI Users / Beanie) | `email`, `hashed_password`, `username`, `name`, `is_active`, `is_superuser`, `is_verified` | unique `email` (case-insensitive), unique `username` |
| `accessTokens` | Active auth sessions (DatabaseStrategy) | `token`, `user_id`, `created_at` | unique `token` |
| `notebooks` | Learning workspaces | `userId`, `title`, `createdAt` | `userId + createdAt` |
| `documents` | Uploaded materials | `userId`, `notebookId`, `status`, `storageKey` | `notebookId`, `userId + status` |
| `documentChunks` | Chunk metadata | `documentId`, `notebookId`, `index`, `textPreview` | `documentId`, `notebookId` |
| `conversations` | Chat threads | `userId`, `notebookId`, `title` | `userId + updatedAt` |
| `messages` | Chat messages | `conversationId`, `role`, `content`, `createdAt` | `conversationId + createdAt` |

### Auth naming exception

`users` and `accessTokens` follow FastAPI Users / Beanie field names (`snake_case` / library conventions), not TILA camelCase. Do not dual-case. Stock adapter stores the opaque session `token` string (not a hash) — see [ADR-0003](../brain/decisions/ADR-0003-fastapi-users-cookie-db.md).

`refreshTokens` from earlier plans is **not** used; sessions are `accessTokens`.

### Document status (closed set)

`UPLOADING` | `PROCESSING` | `READY` | `FAILED`

### Message role (closed set)

`USER` | `ASSISTANT` | `SYSTEM`

Update this file when adding a collection or index.
