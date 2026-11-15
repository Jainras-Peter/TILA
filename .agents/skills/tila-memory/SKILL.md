---
name: tila-memory
description: Read and append TILA docs/brain task-history, roadmap, gaps, and ADRs so agents remember prior work across chats.
---

# TILA memory

## Before work

1. Read `docs/brain/roadmap.md` and `docs/brain/gaps.md`.
2. Read `docs/brain/task-history/<slug>.md` if present.
3. Prefer `/start-task <slug>` to create from `_TEMPLATE.md` when missing.

## After work (`/handoff`)

Append a dated section to the task-history file:

```markdown
### YYYY-MM-DD — <status>

- What changed
- Decisions
- Files touched
- Validation
- Next steps
- Corrections (ai_value → human_value + rationale) if any
```

Also:

- Update roadmap phase status when a phase moves.
- Add/close items in `gaps.md`.
- Write `docs/brain/decisions/ADR-XXXX-title.md` for lasting architecture choices.

## Rules

- Append-only history (never rewrite prior sections).
- Key by feature slug, not conversation id.
- Do not store secrets in brain files.
