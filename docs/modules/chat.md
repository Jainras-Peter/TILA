# Module: Chat

| | |
|--|--|
| **Status** | `scaffold` — models/routes placeholders; LLM gateway exists for generation |
| **Dependency-map node** | `Chat` |
| **ADRs** | [ADR-0001](../decisions/ADR-0001-llm-gateway-canonical.md) |

## Owned paths (intended)

| Area | Paths |
|------|--------|
| API | `conversation` / `message` schemas-models-repos-services-controllers, `api/v1/chat.py`, prompts under `app/ai/prompts/` |
| Web | `features/chat/`, `core/models/chat.model.ts` |

## Contracts (planned)

- Conversations scoped to user (+ notebook/document context).
- Answer path uses RAG retrieval when grounded, then `LLMService.generate`.
- Collections: `conversations`, `messages` (`USER` / `ASSISTANT` / `SYSTEM` roles).

## Required context

- [auth.md](auth.md), [rag.md](rag.md), [documents.md](documents.md)
- [../architecture/ai-architecture.md](../architecture/ai-architecture.md)
- [../architecture/data-flow.md](../architecture/data-flow.md)
- [../architecture/errors.md](../architecture/errors.md)
- [../architecture/dependency-map.md](../architecture/dependency-map.md)

## Before you change this

- Chat depends on Auth (protected) and optionally RAG (retrieval quality).
- Gateway failure modes must map to the error envelope; do not leak provider stacks.
- Streaming (if added later) must stay behind the same gateway boundary.
