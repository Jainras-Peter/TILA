# Module: RAG

| | |
|--|--|
| **Status** | `scaffold` — factories/folders exist; pipeline not production-wired |
| **Dependency-map node** | `RAG` / `Processing` / `EmbedFactory` / `VectorStore` |
| **ADRs** | [ADR-0001](../decisions/ADR-0001-llm-gateway-canonical.md) (LLM door); embedding/vector ADRs pending |

## Owned paths (intended)

| Area | Paths |
|------|--------|
| API | `app/ai/rag/`, `app/ai/embeddings/`, `app/ai/vectorstores/`, `app/document_processing/`, related `app/factories/*` |
| Web | retrieval UX lives under chat/document features (no separate RAG SPA module yet) |

## Contracts (planned)

- Ingest: document → extract → chunk → embed → vector store (via factories).
- Query: question → embed → similarity search → context → **`LLMService` only** (gateway).
- Scope retrieval by `userId` / `notebookId` / `documentId` as applicable.

## Required context

- [documents.md](documents.md), [auth.md](auth.md), [chat.md](chat.md)
- [../architecture/ai-architecture.md](../architecture/ai-architecture.md)
- [../architecture/data-flow.md](../architecture/data-flow.md)
- [../architecture/jobs.md](../architecture/jobs.md)
- [../architecture/dependency-map.md](../architecture/dependency-map.md)
- [../decisions/ADR-0001-llm-gateway-canonical.md](../decisions/ADR-0001-llm-gateway-canonical.md)

## Before you change this

- Embedding model / dimension changes invalidate existing vectors → re-ingest required.
- Do not call provider SDKs from RAG services; use the gateway for generation.
- Do not extend `app/ai/llm/*` (legacy overlap).
- Vector store choice (Chroma/FAISS/etc.) needs an ADR before locking production paths.
