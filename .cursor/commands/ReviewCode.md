# Review Code

Review implemented changes against the approved plan and TILA architecture. READ-ONLY — do not modify files.

## 1. Understand the Changes

Inspect working tree / diff. Understand intent. Compare against the approved `/MakePlan` output and `/ImplementPlan` report when available.

## 2. Architecture Invariants

Check evidence against:

- Backend layering: router → controller → service → repository (no Mongo outside repositories)
- LLM only via `app/ai/gateway`
- Frontend HTTP only via `ApiService` / feature services
- Naming: collections/fields `camelCase`; closed-set values `SCREAMING_SNAKE`
- User data scoped by `userId`
- Errors: typed exceptions + envelope per `docs/errors.md`
- Config via `app/core/config.py` / `.env` — no scattered `os.getenv`

## 3. TILA Bug Hunt

Look for evidence-based issues, including:

- Business logic in controllers or routes
- Services importing FastAPI for domain work
- Missing ownership filters on reads/writes
- Wrong or missing error envelopes
- FE subscription leaks (prefer `takeUntilDestroyed`)
- Bypassing repository / gateway / ApiService
- Contract drift (FE/BE field or enum mismatch)
- Unhandled edge cases from the plan

## 4. Correctness and Requirement Coverage

Logic bugs, missing conditions, duplicated logic, unintended changes, gaps vs the approved plan.

## 5. Frontend / Backend specifics

Only apply checks that match the changed stack (RxJS cleanup, FastAPI validation, Angular standalone patterns, pytest layout, etc.).

## 6. Suggested Improvements

List non-blocking improvements separately from findings (clarity, testability, future hardening). Do not require them for PR readiness unless they are also blockers.

## Severity

- BLOCKER — must fix before PR
- HIGH — strongly recommended
- MEDIUM — before merge
- LOW — minor

Only report evidence-based issues.

## Output

### 1. PR Readiness (READY / READY WITH WARNINGS / NOT READY)
### 2. Change Summary
### 3. Findings
### 4. Architecture / Pattern Compliance
### 5. Requirement Coverage
### 6. Edge-Case Coverage
### 7. Suggested Improvements
### 8. Test Coverage Notes
### 9. Unintended Changes
### 10. Final PR Checklist

## Final Rule

Do not modify anything. Next command: `/TestCode`.
