# Start Task

Prepare agent context for a feature slug before analysis or implementation.

## Input

Feature slug from the user (e.g. `auth-login`, `notebook-crud`). If missing, ask for one.

## Steps (read-only except creating a missing task-history file)

1. Read `AGENTS.md`.
2. Read `docs/brain/README.md`, `docs/brain/roadmap.md`, `docs/brain/gaps.md`.
3. If `docs/brain/task-history/<slug>.md` exists, read it fully.
4. If missing, create it by copying `docs/brain/task-history/_TEMPLATE.md`, set `slug`, `status: planned`, `started-at` (ISO), and a one-line Goal from the user request.
5. Skim the docs pages relevant to the request (backend/frontend/ai/persistence/design).
6. Summarize for the user:
   - Current roadmap phase status
   - Prior decisions / corrections from task-history
   - Relevant gaps
   - Recommended next command: `/analyse`

## Rules

- Do not implement code in this command.
- Task-history is append-only after creation; only fill the template header when creating.
- Prefer existing patterns; note scaffold vs implemented areas honestly.
