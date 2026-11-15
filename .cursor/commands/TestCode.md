# Test Code

Test the implemented feature against the approved plan’s happy path and edge cases. Produce a test report.

## Core Rule

Prefer running existing automated checks. Do not redesign the feature. Do not expand scope beyond validating what was planned and implemented.

---

## 1. Load Context

Read as needed:

- Approved `/MakePlan` output (especially Edge Cases and Validation Strategy)
- `/ImplementPlan` report and changed files
- Relevant tests under `tests/` and frontend test layout if present

## 2. Build the Test Matrix

Derive cases from:

- Happy path
- Every edge case listed in the plan
- Auth / ownership failures when applicable
- Validation and error-envelope paths
- Empty / not-found / forbidden UI or API behaviour when in scope

For each case: steps, expected result, automated vs manual.

## 3. Run Automated Checks

As applicable for the change set:

- Backend: `pytest` (targeted first, then broader if needed)
- Lint/type: `ruff`, `tsc --noEmit`, or `npm run check`
- Any existing feature tests that cover the changed paths

Record command, result, and evidence (pass/fail + key output).

## 4. Manual / Gap Verification

When automated coverage cannot prove a case (UI flows, external services, LLM):

- List precise manual steps
- Mark result as PASS / FAIL / NOT RUN
- Do not invent pass results without evidence

## 5. Test Report Output

### 1. Test Summary
### 2. Test Matrix (case / type / result / evidence)
### 3. Failures and Defects
### 4. Coverage Gaps
### 5. Commands Run
### 6. Verdict (PASS / PASS WITH GAPS / FAIL)
### 7. Recommended Next Steps

## Final Rule

After the report, suggest `/Handoff` to persist results in task-history. If verdict is FAIL, list the smallest fixes before re-running `/TestCode`.
