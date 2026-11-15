---
slug: context-engineering
status: done
started-at: 2026-11-15
last-phase: handoff
product: TILA
branches: []
---

## Goal

Introduce Context Engineering (selective doc loading) and a dependency map so agents load only relevant docs and understand blast radius before changing modules.

## Notes

### 2026-11-15 — implemented

- Restructured docs: `docs/architecture/*`, `docs/modules/*`, `docs/decisions/*` (ADRs moved from `brain/decisions/`), brain kept for roadmap/gaps/task-history.
- Added `docs/architecture/data-flow.md`, `docs/architecture/dependency-map.md`.
- Added `docs/context-routing.json` + skill `.agents/skills/tila-context/SKILL.md`.
- Updated `/StartTask`, `/MakePlan`, `memory.mdc`, `AGENTS.md`, module skills/paths.
- Added `scripts/scan-api-imports.py` → `docs/architecture/dependency-map.generated.md` (8 cross-package edges).
- Dry-run `rag-ingest` context: 13 targeted paths (auth + documents + ai + jobs + gateway ADR + dependency-map), not the full docs tree.
- Gaps: pending storage/jobs ADRs; heavier dep tooling deferred.

### Next

- Use `/StartTask rag-ingest` or `/StartTask auth-login` in real feature work to validate routing in practice.
