# Vision

TILA (Teaching & Intelligent Learning Assistant) is an AI-powered learning platform. A student provides learning material; TILA becomes a tutor that understands, retrieves, explains, and teaches from that material.

## Product idea

Users create notebooks (subjects / topics). Each notebook holds documents (PDF, TXT, DOCX, …). Users ask grounded questions such as:

- Explain Newton's second law in simple terms.
- What are the important concepts from Chapter 2?
- Create 10 MCQs from Chapter 3.
- Summarize this chapter.

TILA retrieves relevant chunks from the user's materials and uses an LLM to answer.

## Core entities

| Entity | Role |
|--------|------|
| User | Account, auth, ownership, preferences |
| Notebook | Learning workspace owned by a user |
| Document | Uploaded material belonging to a notebook |
| DocumentChunk | Split text used for embeddings and retrieval |
| Conversation / Message | Chat history scoped to a notebook or document |

## Hard boundaries

- TILA is an **AI-native learning platform**, not "CRUD + chatbot".
- Answers must be grounded in the user's materials when RAG applies.
- Users may only access resources they own (`userId` scoping everywhere).
- Secrets never live in source control.
- Prefer modular providers (LLM, embedding, storage, vector store) over hard-wiring one vendor.

## Out of scope (for now)

- Multi-tenant SaaS billing
- Shared / collaborative notebooks
- Mobile native apps

## Principle

Simple foundation → modular architecture → incremental complexity → production-ready AI platform.

Avoid premature complexity. Introduce factories and abstractions only where they provide real extensibility.
