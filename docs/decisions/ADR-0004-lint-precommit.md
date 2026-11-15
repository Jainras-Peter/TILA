# ADR-0004: Executable architecture lint + pre-commit + CI

- **Status:** Accepted
- **Date:** 2026-11-15

## Context

Atlas enforces architecture with ESLint restricted imports, CI import tests, and Husky/lint-staged. TILA is Angular + FastAPI, so we copy the **guarantees**, not the Node monorepo tooling.

## Decision

1. **Web:** `@angular-eslint` flat config (`Web/eslint.config.mjs`) bans `HttpClient`/`fetch` outside `ApiService`/interceptors/bootstrap, and cross-feature imports.
2. **API:** AST-based pytest (`tests/unit/architecture/test_import_boundaries.py`) enforces layer direction; Ruff for quality/format.
3. **Pre-commit:** Husky + lint-staged auto-fixes staged files (`eslint --fix`, `ruff check --fix`, `ruff format`).
4. **Verify:** `npm run check` and GitHub Actions CI run verify-only (no rewrite) on the full tree.
5. Design-system ESLint and circular-dep tooling stay deferred (`docs/brain/gaps.md`).

## Consequences

- Agents and humans get the same commit gate.
- Skipping hooks locally still fails CI.
- Architecture docs must stay aligned with executable tests/rules.
