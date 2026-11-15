# Collections

Planned Mongo collections (scaffold models exist under `API/app/models/`; many files are still empty placeholders).

| Collection | Purpose | Key fields | Indexes (planned) |
|------------|---------|------------|-------------------|
| `users` | Accounts | `email`, `passwordHash`, `createdAt` | unique `email` |
| `refreshTokens` | Session refresh | `userId`, `tokenHash`, `expiresAt` | `userId`, TTL `expiresAt` |
| `notebooks` | Learning workspaces | `userId`, `title`, `createdAt` | `userId + createdAt` |
| `documents` | Uploaded materials | `userId`, `notebookId`, `status`, `storageKey` | `notebookId`, `userId + status` |
| `documentChunks` | Chunk metadata | `documentId`, `notebookId`, `index`, `textPreview` | `documentId`, `notebookId` |
| `conversations` | Chat threads | `userId`, `notebookId`, `title` | `userId + updatedAt` |
| `messages` | Chat messages | `conversationId`, `role`, `content`, `createdAt` | `conversationId + createdAt` |

### Document status (closed set)

`UPLOADING` | `PROCESSING` | `READY` | `FAILED`

### Message role (closed set)

`USER` | `ASSISTANT` | `SYSTEM`

Update this file when adding a collection or index.
