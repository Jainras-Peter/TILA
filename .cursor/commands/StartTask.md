# Start Task

Prepare selective application context for a feature slug before planning or implementation.

## Input

Feature slug from the user (e.g. `auth-login`, `rag-ingest`). If missing, ask for one.

## Steps (read-only except creating a missing task-history file)

1. Resolve context via **Context Engineering** (`.agents/skills/tila-context/SKILL.md`):
   - Open `docs/context-routing.json`
   - Match slug (preferred) or keywords to a route
   - Read **only** `default` + that route’s `always`
   - Read `optional` only if the task clearly needs UI/design or those modules
   - Do **not** read every file under `docs/`
2. Read pointers if needed (short):
   - `.cursor/agent.md`, `.cursor/architecture.md`
   - `AGENTS.md`
3. Read brain memory:
   - `docs/brain/README.md`
   - `docs/brain/roadmap.md`, `docs/brain/gaps.md` (already in `default` when using routing)
   - If `docs/brain/task-history/<slug>.md` exists, read it fully
   - If missing, create it by copying `docs/brain/task-history/_TEMPLATE.md`, set `slug`, `status: planned`, `started-at` (ISO), and a one-line Goal from the user request
4. Read module agents when the task may touch that stack:
   - `API/AGENTS.md` and/or `Web/AGENTS.md`
5. Skim `docs/architecture/dependency-map.md` for blast radius (required for Auth, gateway, embeddings, workers, shared core).
6. Summarize **application info for this task**:
   - Route id matched + **Context loaded** (list concrete paths)
   - Current roadmap phase status
   - Prior decisions / corrections from task-history
   - Relevant gaps
   - Layers likely involved
   - Locked constraints (layering, gateway, ApiService, naming, `userId` scope)
7. Recommended next command: `/MakePlan`

## Rules

- Do not implement code in this command.
- Task-history is append-only after creation; only fill the template header when creating.
- Prefer existing patterns; note scaffold vs implemented areas honestly.
- Prefer docs from the routing list before scanning the whole repo.
