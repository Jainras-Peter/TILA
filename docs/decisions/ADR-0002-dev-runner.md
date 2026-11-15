# ADR-0002: One-command local dev via npm + concurrently

- **Status:** Accepted
- **Date:** 2026-11-15

## Context

Atlas uses `pnpm dev` + Turborepo to run multiple Node apps. TILA mixes Python (FastAPI) and Angular, so Turborepo cannot orchestrate the API process.

## Decision

Use a root `TILA/package.json` with `concurrently` so `npm run dev` starts:

- `uvicorn app.main:app --reload` on :8000
- `ng serve` on :4200 with `proxy.conf.json` for `/api` and `/llm`

Also provide a thin root `Makefile` (`make dev` → `npm run dev`). Pin backend Python to 3.12.

## Consequences

- Developers run `npm run setup` once, then `npm run dev`.
- Mongo via docker-compose remains a later gap.
- No requirement to adopt a JS monorepo for the Python API.
