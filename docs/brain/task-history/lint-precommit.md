---
slug: lint-precommit
status: done
started-at: 2026-11-15
last-phase: handoff
product: TILA
branches: []
---

## Goal

Make TILA architecture executable: Angular ESLint, AST pytest boundaries, Husky/lint-staged commit gate, and CI `npm run check`.

## Notes

### 2026-11-15 — implemented

- `Web/eslint.config.mjs` + deps; `AuthFeatureService` uses `ApiService.postText` (no direct HttpClient).
- `API/tests/unit/architecture/test_import_boundaries.py` (AST).
- Root husky + `lint-staged.config.mjs` (fix on commit; verify in check/CI).
- `.github/workflows/check.yml`, stop-check ESLint, ADR-0004, docs updated.

### Next

- Shrink `ROUTE_ALLOWLIST` when auth routes go through controllers.
- Design-system ESLint when type roles exist.
