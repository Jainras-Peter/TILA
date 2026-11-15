# Start Task

Prepare full application context for a feature slug before planning or implementation.

## Input

Feature slug from the user (e.g. `auth-login`, `notebook-crud`). If missing, ask for one.

## Steps (read-only except creating a missing task-history file)

1. Read the agent/docs stack in order:
   - `.cursor/agent.md`
   - `.cursor/architecture.md`
   - Relevant files under `.cursor/service-knowledge-base/`
   - `AGENTS.md`
   - Relevant `docs/*.md` for the request (vision, architecture, backend, frontend, persistence, collections, ai, jobs, errors as needed)
2. Read brain memory:
   - `docs/brain/README.md`
   - `docs/brain/roadmap.md`
   - `docs/brain/gaps.md`
   - If `docs/brain/task-history/<slug>.md` exists, read it fully
   - If missing, create it by copying `docs/brain/task-history/_TEMPLATE.md`, set `slug`, `status: planned`, `started-at` (ISO), and a one-line Goal from the user request
3. Read module agents when the task may touch that stack:
   - `API/AGENTS.md`
   - `Web/AGENTS.md`
4. Summarize **application info for this task**:
   - Current roadmap phase status
   - Prior decisions / corrections from task-history
   - Relevant gaps
   - Layers likely involved (frontend / backend / Mongo / AI gateway / workers / config)
   - Collections, APIs, or UI modules likely involved
   - Locked constraints that apply (router → controller → service → repository; gateway for LLM; ApiService for HTTP; camelCase / SCREAMING_SNAKE; `userId` scope)
5. Recommended next command: `/MakePlan`

## Rules

- Do not implement code in this command.
- Task-history is append-only after creation; only fill the template header when creating.
- Prefer existing patterns; note scaffold vs implemented areas honestly.
- Do not scan the whole repo; prefer docs and knowledge base first.
