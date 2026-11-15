# ADR-0001: LLM Gateway is the only LLM door

- **Status:** Accepted
- **Date:** 2026-11-15

## Context

The backend scaffold contains both `app/ai/gateway` (implemented, with retries and fallback) and empty `app/ai/llm/*` plus `app/factories/llm_factory.py`.

## Decision

All LLM calls go through `app/ai/gateway` (`LLMService` / `LLMProvider` / factory). New provider adapters live under `app/ai/gateway/providers/`.

## Consequences

- Agents must not add code to `app/ai/llm/*` or `llm_factory.py`.
- Removal of the overlapping scaffold is deferred to an approved cleanup task.
- Services depend on the gateway abstraction, not vendor SDKs.
