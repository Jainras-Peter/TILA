# Persistence

Primary store: **MongoDB** via Motor. Only repositories talk to the database.

## Ownership

| Collection | Owner | Access |
|------------|-------|--------|
| Application collections | Matching `*Repository` | Services call repositories; never controllers/routes |

`app/core/database.py` owns the connection/client only. Do not put query logic there.

## Naming

- **Collection names:** `camelCase` (`notebooks`, `documentChunks`, `refreshTokens`).
- **Document fields:** `camelCase` (`userId`, `notebookId`, `createdAt`).
- **Closed-set values:** `SCREAMING_SNAKE` (`PROCESSING`, `READY`, `FAILED`). Pattern: `STATUSES` list + `Status` type alias + const map where useful.
- No dual-casing. After a rename, migrate or drop local data; do not keep legacy spellings.

## Resource ownership

Every user-owned query filters by `userId` (from the authenticated principal). Never trust a client-supplied owner id alone.

## Indexes

Document indexes in [collections/README.md](collections/README.md). Prefer compound indexes that match list filters (`userId` + sort field).

## Vector data

Embeddings live in the vector store abstraction (`app/ai/vectorstores`), not as the system of record for documents. Chunk metadata may live in Mongo (`documentChunks`); vectors live in Chroma/FAISS/etc.

## Migrations

Schema is document-oriented. Breaking field changes need an explicit migration note in `docs/brain/gaps.md` or a task-history entry. Alembic is present for future SQL needs; Mongo is the current SoR.
