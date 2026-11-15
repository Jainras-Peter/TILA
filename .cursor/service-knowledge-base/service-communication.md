# Service communication

## Browser ↔ API

- Angular calls `/api/v1/*` (and optionally `/llm` for gateway diagnostics).
- Dev: `proxy.conf.json` forwards `/api` and `/llm` to `http://localhost:8000`.
- Prod: same-origin or configured API host via environment.

## Internal backend

- Sync request path: route → controller → service → repository / gateway.
- Async path (planned): service enqueues job → `app/workers` processes document ingestion.
- LLM providers: HTTP from gateway adapters (Groq / Gemini / OpenAI) using keys from config.

## Contracts

- REST JSON under `/api/v1`.
- Error envelope: `docs/errors.md`.
- LLM diagnostic payload includes `text`, `provider_used`, `attempts`, `total_latency_ms`.

No gRPC/message bus yet. Prefer HTTP + eventual Redis queue over inventing a bus early.
