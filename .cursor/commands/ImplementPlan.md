# Implement Approved Plan

Implement ONLY the approved implementation plan from the current conversation, then produce an implementation report.

## Core Rule

Do not redesign the solution. Do not add unrelated refactors, cleanups, or architecture changes.

---

## 1. Read the Plan First

Confirm requirements, files, patterns, expected behaviour, edge cases, and validation. If there is no clear plan in this conversation, STOP and ask for `/MakePlan` (or the approved plan).

## 2. Re-Validate

Re-open relevant files. Confirm the pattern still applies. Do not implement from stale assumptions.

## 3. Follow TILA Patterns

- Backend: router → controller → service → repository; LLM via gateway
- Frontend: standalone + feature service + ApiService
- Naming/persistence/errors per `docs/`
- Do not introduce a new pattern when an existing one fits

## 4. Implement Only What Was Planned

Modify only what is necessary. No drive-by upgrades, renames, or contract changes unless planned. Cover planned edge cases in the same change set when they require code.

## 5. Required Extra Changes

If a missing file/change is truly required: keep it minimal, mention it in the final report.

## 6. Validation

- Format/lint with project tools (`ruff`, `tsc` when applicable)
- Run relevant tests (`pytest`, feature checks)
- Review diff for debug code, secrets, unrelated edits

## 7. Final Implementation Report

### 1. Implementation Summary
### 2. File-by-File Changes (what / why / pattern / important logic)
### 3. Final Flow
### 4. Edge Cases Implemented
### 5. Tests and Validation
### 6. Changed Files
### 7. Deviations From Plan
### 8. Risks / Manual Verification

## Final Rule

Implement the approved plan only. Afterward, suggest `/ReviewCode`, then `/TestCode`, then `/Handoff` to record memory.
