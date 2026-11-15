# Module: Documents

| | |
|--|--|
| **Status** | `scaffold` — folder layout only; upload/storage/worker not wired |
| **Dependency-map node** | `Documents` / `Storage` / `DocWorker` |
| **ADRs** | Storage strategy ADR **not decided** (see [../brain/gaps.md](../brain/gaps.md)) |

## Owned paths (intended)

| Area | Paths |
|------|--------|
| API | `document_*` schemas/models/repos/services/controllers, `api/v1/documents.py`, `app/storage/`, `app/workers/document_worker.py`, `app/document_processing/` |
| Web | `features/document/` |

## Contracts (planned)

- Upload creates a document record + storage object; status `UPLOADING` → `PROCESSING` → `READY` / `FAILED`.
- Ingest is a background job (`document.ingest`), not a long request handler ([../architecture/jobs.md](../architecture/jobs.md)).
- Collection: `documents` (+ later `documentChunks` metadata).

## Required context

- [auth.md](auth.md), [notebooks.md](notebooks.md)
- [../architecture/data-flow.md](../architecture/data-flow.md)
- [../architecture/jobs.md](../architecture/jobs.md)
- [../architecture/persistence.md](../architecture/persistence.md)
- [../architecture/dependency-map.md](../architecture/dependency-map.md)

## Before you change this

- Storage key / path format changes break existing blobs and workers.
- Status enum changes need FE + worker + API agreement (`SCREAMING_SNAKE`).
- RAG ingest depends on this module; do not bypass Auth/`userId` scoping.
