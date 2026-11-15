# Gaps and risks

## Active

- **Duplicate LLM stack:** `app/ai/gateway` is canonical, but empty/legacy `app/ai/llm/*` and `app/factories/llm_factory.py` still exist. Do not extend them. Cleanup requires a separate approved task (no deletes in this restructuring).
- **Empty scaffolds:** ~127 empty `.py` files under `API/app`. Feature folders in Angular are mostly `.gitkeep`. Agents must treat them as placeholders, not finished APIs.
- **Config split:** Gateway still loads `.env` in `app/ai/gateway/config.py`. Target is `app/core/config.py` (pydantic-settings) for all settings.
- **docker-compose / Dockerfile:** Files exist but are empty — no Mongo/API container path yet.
- **Mongo partially wired:** Beanie init + FastAPI Users `users` / `accessTokens` via `MONGODB_URI`. Other Motor repositories remain empty; docker-compose Mongo path still missing.
- **Access token storage:** FastAPI Users Beanie adapter stores opaque session tokens (not hashes). Accept for MVP; revisit if threat model requires hashed tokens.
- **Auth gaps:** no forgot/reset password, no email verification, no multi-device session UI.
- **Workspace Cursor root:** Prefer opening `TILA/` as the Cursor folder, or symlink `TILA_Workspace/.cursor → TILA/.cursor`, so commands/rules load. If the workspace root stays `TILA_Workspace`, create/maintain that symlink.
- **Python version:** Pin is 3.12 (`.python-version`). Host may have 3.14; RAG libs often lack 3.14 wheels.
- **Frontend tests:** `npm run test:web` needs Chrome/Karma setup; may fail until test runner is configured.
- **Alembic present:** `alembic.ini` exists while SoR is Mongo — clarify or remove in a later cleanup.
- **Pending ADRs:** storage strategy (local vs S3) and background-job runner (in-process vs Redis/ARQ/Celery) are not decided — do not invent production locks without an ADR under `docs/decisions/`.
- **Dependency tooling:** Import Linter / Pydeps / Madge / Dependency Cruiser deferred; use `docs/architecture/dependency-map.md` + `scripts/scan-api-imports.py` for now.

## Closed

- (none yet beyond documenting agent architecture / context engineering)
