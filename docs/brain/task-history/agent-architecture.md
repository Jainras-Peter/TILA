---
slug: agent-architecture
status: done
started-at: 2026-11-15
last-phase: handoff
product: TILA
branches: []
---

## Goal

Give TILA the same agent-facing architecture as Atlas: AGENTS.md, docs/, brain memory, .cursor rules/commands/hooks, skills, and a single `npm run dev` for API + Angular.

## Notes

### 2026-11-15 — implemented

- Root `package.json` + `Makefile` + `scripts/dev-preflight.mjs` (concurrently).
- Backend `pyproject.toml`, Makefile, `.python-version` 3.12; frontend `proxy.conf.json` + env `apiBaseUrl`.
- Moved `TILA.knowledge.md` / `TILA.Architecture.md` to `docs/archive/` (git mv).
- Added docs pages, AGENTS.md / CLAUDE.md / module AGENTS.md.
- Added `.cursor/` knowledge base, rules, commands, hooks.
- Added brain (roadmap, gaps, ADR-0001, ADR-0002) and skills under `.agents/skills/`.
- Decisions: gateway canonical (ADR-0001); npm+concurrently runner (ADR-0002).
- Deferred: deleting duplicate LLM scaffold; filling docker-compose; wiring Mongo.

### 2026-11-15 — verified

- `npm install` + `npm run setup:api` + `npm run setup:web` succeeded (Python 3.12 venv).
- `npm run dev` brought API `:8000` (`Application startup complete`) and Angular `:4200` (`Application bundle generation complete`).
- Smoke: `GET /` → online JSON; `GET :4200` → 200; `pytest` → 5 passed.
- Fixed gateway `.env` path to resolve `API/.env` (was one parent too high).
- Dry-run task file created: `docs/brain/task-history/auth-login.md`.
- Workspace symlink: `TILA_Workspace/.cursor` → `TILA/.cursor`.

### 2026-11-15 — folder rename

- `git mv TILA-Backend → API`, `TILA-Frontend → Web`.
- Updated package.json, preflight, hooks, rules, docs, AGENTS.md, skills references.

### Next

- Implement product features starting with `/start-task auth-login` → `/analyse`.
