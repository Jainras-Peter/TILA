# Jobs / background workers

Document ingestion and embedding are expensive. Architecture supports workers under `app/workers/`.

## Planned flow

```text
Upload document
  → Create document record (status UPLOADING/PROCESSING)
  → Enqueue job
  → Worker: extract → chunk → embed → vector store
  → Update document status READY or FAILED
```

## Contract (when implementing)

| Item | Rule |
|------|------|
| Job name | `<domain>.<verb>` e.g. `document.ingest` |
| Payload | Include `userId`, `documentId`, `notebookId` |
| Idempotency | Safe to retry; status transitions must not double-embed blindly |
| Location | Single-domain handlers in `app/workers/`; orchestration stays in services |
| Observability | Structured logs with `documentId` and attempt |

First implementation may be in-process; keep the service boundary so a queue (Celery / ARQ / Redis) can replace it later.

Do not run long ingestion inside a request handler beyond enqueue + acknowledge.
