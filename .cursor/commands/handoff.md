# Handoff

Persist what was done so the next chat/agent can continue. Uses `.agents/skills/tila-memory/SKILL.md`.

## Steps

1. Identify the feature slug (ask if unclear).
2. Open `docs/brain/task-history/<slug>.md` (create from template if missing).
3. **Append** a new section (do not rewrite earlier sections) with:
   - Date / status
   - What was done
   - Decisions made
   - Files touched
   - Tests / validation run (include `/TestCode` verdict when available)
   - Open questions / next steps
   - Corrections (if human overrode the AI)
4. Update `docs/brain/roadmap.md` phase status if a phase moved.
5. Update `docs/brain/gaps.md` if new gaps appeared or were closed.
6. If a lasting architecture choice was made, add `docs/brain/decisions/ADR-XXXX-....md` and link it from the task-history entry.
7. For large features, ensure `docs/stories/<slug>/HANDOFF.md` exists or is updated.

## Output

Short confirmation: path to task-history entry, roadmap/gaps/ADR changes, suggested next slug or command.

## Rules

- Append-only history.
- No unrelated refactors.
- Do not delete prior notes.
- Feature workflow reminder: `/StartTask` → `/MakePlan` → `/ImplementPlan` → `/ReviewCode` → `/TestCode` → `/Handoff`.
