---
name: tila-rag-pipeline
description: Extend TILA document processing / RAG using factories for loaders, chunkers, embeddings, and vector stores; LLM answers via the gateway only.
---

# TILA RAG pipeline

Use when working on ingestion, retrieval, or grounded answers.

## Preconditions

Resolve context via `docs/context-routing.json` (rag route). At minimum read `docs/modules/rag.md`, `docs/architecture/ai-architecture.md`, `docs/architecture/jobs.md`, `docs/architecture/data-flow.md`, `docs/architecture/dependency-map.md`, and ADR-0001.

## Ingestion sketch

```text
upload → storage → loader → clean → chunker → embedding → vector store → update document status
```

Use factories:

- `document_loader_factory` / loaders under `document_processing/`
- `chunking_factory`
- `embedding_factory`
- `vector_store_factory`

Long work belongs in `app/workers` (enqueue from service; do not block the request).

## Query sketch

```text
question → embed → similarity search → context builder → LLMService.generate → answer
```

LLM only through `app/ai/gateway`.

## Do not

- Call Groq/Gemini/OpenAI SDKs from RAG services.
- Store vectors as the only copy of document text without Mongo metadata for chunks/documents.
- Extend `app/ai/llm/*`.
