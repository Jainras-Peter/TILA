# Module: Notebooks

| | |
|--|--|
| **Status** | `scaffold` — empty placeholders / routes not fully implemented |
| **Dependency-map node** | `Notebooks` |
| **ADRs** | none yet |

## Owned paths (intended)

| Area | Paths |
|------|--------|
| API | `schemas/notebook.py`, `models/notebook.py`, `repositories/notebook_repository.py`, `services/notebook_service.py`, `controllers/notebook_controller.py`, `api/v1/notebooks.py` |
| Web | `features/notebook/`, `core/models/notebook.model.ts` |

## Contracts (planned)

- CRUD under `/api/v1/notebooks`.
- Collection: `notebooks` with `userId`, `title`, `createdAt`.
- Every query scoped by authenticated `userId`.

## Required context

- [auth.md](auth.md) (ownership + protected routes)
- [../architecture/backend-architecture.md](../architecture/backend-architecture.md)
- [../architecture/persistence.md](../architecture/persistence.md)
- [../architecture/collections/README.md](../architecture/collections/README.md)
- [../architecture/dependency-map.md](../architecture/dependency-map.md)

## Before you change this

- Documents and chat will hang off `notebookId`; changing notebook delete semantics needs cascade/orphan policy.
- Prefer implementing against Auth patterns already in the tree before inventing new ownership rules.
