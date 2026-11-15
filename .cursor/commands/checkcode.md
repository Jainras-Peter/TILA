# Check Code Before PR

Review current changes before a Pull Request. READ-ONLY — do not modify files.

## 1. Understand the Changes

Inspect working tree / diff. Understand intent.

## 2. Compare Against TILA Patterns

Folder structure, layering, naming, error handling, config, tests, Angular standalone + services, gateway usage.

## 3–4. Correctness and Architecture

Logic bugs, missing conditions, wrong layer, duplicated logic, bypassing repositories/gateway/ApiService.

## 5. Frontend / Backend specifics

Only apply checks that match the changed stack (RxJS cleanup, FastAPI validation, ownership filters, etc.).

## 6. Tests, unintended changes, requirement coverage

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
### 4. Pattern Compliance
### 5. Requirement Coverage
### 6. Test Coverage
### 7. Unintended Changes
### 8. Final PR Checklist

## Final Rule

Do not modify anything.
