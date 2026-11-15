# AI layer

## Canonical LLM door

**Use `app/ai/gateway` for all LLM calls.**

- Interface: `LLMProvider`
- Request/response: `LLMRequest` / `LLMResponse`
- Factory: `LLMProviderFactory` (groq, gemini, openai)
- Orchestration: `LLMService` (retries, fallback, attempt logs)
- Config: gateway settings (eventually via `app/core/config.py` — see [config.md](config.md))
- Diagnostic routes: `/llm`, `/api/v1/llm`

### Resiliency

| Class | Examples | Behavior |
|-------|----------|----------|
| Retryable | 429, 408, 5xx, timeout, network | Retry same provider up to configured count |
| Permanent | 400, 401, 403, 404 | Skip remaining retries; switch to fallback |

See [../archive/TILA.Architecture.md](../archive/TILA.Architecture.md) for sequence diagrams.

## Overlapping scaffold (do not extend)

These empty/legacy paths overlap the gateway. Recorded in [../brain/gaps.md](../brain/gaps.md). Do **not** add new code there:

- `app/ai/llm/*`
- `app/factories/llm_factory.py`

Removal is a separate approved cleanup task.

## RAG and document processing

| Concern | Path |
|---------|------|
| Pipeline | `app/ai/rag/` |
| Embeddings | `app/ai/embeddings/` + `app/factories/embedding_factory.py` |
| Vector stores | `app/ai/vectorstores/` + `app/factories/vector_store_factory.py` |
| Loaders / chunkers | `app/document_processing/` + factories |
| Prompts | `app/ai/prompts/` |

Skill: `.agents/skills/tila-rag-pipeline/SKILL.md`.

## Rules for agents

- Services call `LLMService.generate(...)`, never a provider SDK directly.
- Do not read `process.env` / `os.getenv` inside providers for new settings — use config.
- Prefer structured attempt logging already on `LLMResponse`.
