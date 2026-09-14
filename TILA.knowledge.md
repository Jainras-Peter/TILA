# TILA — Teaching & Intelligent Learning Assistant

## 1. Project Overview

TILA (Teaching & Intelligent Learning Assistant) is an AI-powered learning platform designed to help students learn from their own study materials.

The core idea is:

> A student provides the learning material, and TILA becomes an AI tutor that understands, retrieves, explains, and teaches from that material.

TILA combines:

- Document Management
- AI-powered Document Understanding
- Retrieval-Augmented Generation (RAG)
- AI Chat
- Notebook-based Learning
- Question Answering
- Summarization
- Quiz Generation
- Learning Assistance
- Future Agentic AI capabilities

The application should be built as an industry-level, scalable, maintainable and modular AI application.

---

# 2. Main Product Concept

Users can create multiple notebooks based on subjects or learning topics.

Example:

```text
Physics Notebook
│
├── Chapter 1.pdf
├── Chapter 2.pdf
├── Chapter 3.pdf
└── Notes.pdf
The user can interact with TILA using these documents.

Example questions:

"Explain Newton's second law in simple terms."

"What are the important concepts from Chapter 2?"

"Compare Chapter 1 and Chapter 3."

"Create 10 MCQs from Chapter 3."

"Summarize this chapter."

"Explain this topic like I am a beginner."

TILA should retrieve relevant information from the user's learning materials and use an LLM to generate grounded responses.

3. Core Domain Entities

The initial core entities are:

User

Represents an application user.

Responsibilities:

User account
Authentication
User ownership
User resources
User preferences
Notebook

A Notebook is a logical learning workspace.

A user can create multiple notebooks.

Example:

User
│
├── Physics
├── Mathematics
├── Machine Learning
└── System Design

Each notebook can contain multiple documents.

Document

Represents a learning document uploaded by a user.

Example:

Notebook: Physics

Documents:
├── Chapter1.pdf
├── Chapter2.pdf
└── Chapter3.pdf

A document belongs to a Notebook.

Possible future formats:

PDF
TXT
DOCX
PPTX
Images
Other educational formats
Document Chunk

Large documents are divided into smaller chunks during the RAG ingestion pipeline.

Example:

Document
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Chunking
   ↓
Document Chunks
   ↓
Embeddings
   ↓
Vector Database

Document chunks are used for semantic retrieval.

4. High-Level Architecture

TILA follows a client-server architecture.

                    ┌─────────────────────┐
                    │      Frontend       │
                    │      Angular        │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │      Backend        │
                    │      FastAPI        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
          MongoDB           AI / RAG       File Storage
              │                │
              │        ┌───────┴────────┐
              │        │                │
              │        ▼                ▼
              │    Embeddings          LLM
              │        │                │
              │        ▼                ▼
              │    Vector DB       AI Provider
              │
              ▼
        Application Data

The architecture should remain modular so individual technologies can be replaced later.

5. Frontend
Technology
Angular
TypeScript
Tailwind CSS
AI-oriented UI components
Responsive UI

The frontend should be designed as a modern AI application.

The UI should prioritize:

Clean visual hierarchy
Good color grading
Accessibility
Responsive design
AI interaction
Learning experience
Component reusability
6. Frontend Major Modules

The frontend will eventually contain modules for:

Authentication
Dashboard
Notebook
Document
AI Chat
RAG
Learning
Quiz
Study Tools
User Profile
Settings
Authentication

Features:

Registration
Login
Logout
Session management
Token management
Dashboard

Features:

Recent notebooks
Recent documents
Learning activity
AI interactions
Quick actions
Notebook

Features:

Create notebook
Update notebook
Delete notebook
View notebook
Manage documents
AI chat
Search
Learning tools
Document

Features:

Upload document
View document
Delete document
Processing status
Document metadata
Document-based AI interaction
AI Assistant

Future AI capabilities include:

Document Q&A
General learning questions
Explanation
Summarization
Quiz generation
Question generation
Study assistance
Future AI agents

The frontend should be designed so new AI capabilities can be added without tightly coupling components.

7. Backend
Technology

Primary backend technology:

Python
FastAPI

The backend exposes APIs consumed by the Angular frontend.

The backend should follow a layered architecture.

The primary request flow is:

Router
   ↓
Middleware
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
8. Backend Architecture Layers
Router

Responsible for:

API route definitions
API versioning
Request routing
Connecting routes to controllers

Example:

/api/v1/auth
/api/v1/users
/api/v1/notebooks
/api/v1/documents
/api/v1/chat
/api/v1/rag
Middleware

Middleware handles cross-cutting concerns.

Initial/future middleware may include:

Authentication middleware
Authorization middleware
Rate limiting
Request timeout
Request validation
Logging
Error handling
Request tracing
CORS
Security headers

Middleware should remain independent from business logic.

Controller

Controllers handle HTTP-level concerns.

Responsibilities:

Receive requests
Validate request input
Call services
Convert service results into HTTP responses
Return appropriate status codes

Controllers should NOT contain business logic.

Service

Services contain application/business logic.

Examples:

UserService
NotebookService
DocumentService
ChatService
RAGService
AIService
EmbeddingService
StorageService

Services should not directly depend on HTTP-specific implementation details.

Repository

Repositories handle database access.

Responsibilities:

Create
Read
Update
Delete
Query
Database-specific operations

The Repository Pattern should be used to separate business logic from database implementation.

Example:

Service
   ↓
Repository Interface
   ↓
MongoDB Repository

This allows database implementation to change without heavily modifying business logic.

9. Factory Pattern

Factory Pattern should be used where multiple implementations/providers are expected.

The most important use cases are AI-related services.

LLM Factory

Conceptually:

LLM Factory
│
├── Groq
├── Gemini
├── HuggingFace
├── Local LLM
└── Future Providers

Application logic should depend on an LLM abstraction rather than directly depending on one provider.

Embedding Factory

Conceptually:

Embedding Factory
│
├── HuggingFace
├── Local Embedding Model
└── Future Providers
Storage Factory

Potential future implementations:

Storage Factory
│
├── Local Storage
├── Cloud Storage
└── Future Providers

Factories should only be introduced where they provide real extensibility.

Avoid unnecessary design patterns.

10. RAG Architecture

RAG is one of the core components of TILA.

Document Ingestion Pipeline
User Uploads Document
        ↓
File Storage
        ↓
Document Processing
        ↓
Text Extraction
        ↓
Text Cleaning
        ↓
Chunking
        ↓
Embedding Generation
        ↓
Vector Database
Query Pipeline

When a user asks a question:

User Question
      ↓
Query Processing
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Relevant Document Chunks
      ↓
Context Construction
      ↓
LLM
      ↓
Generated Answer

The RAG pipeline should remain modular.

11. AI Layer

TILA should support multiple AI providers.

Potential providers:

Groq
Gemini
Hugging Face
Local LLMs
Future providers

The AI layer should contain abstractions for:

LLM

Responsible for:

Text generation
Question answering
Summarization
Explanation
Quiz generation
Learning assistance
Embedding Model

Responsible for:

Document embeddings
Query embeddings
Semantic representation
Vector Store

Responsible for:

Storing embeddings
Similarity search
Retrieving relevant document chunks

The application should not be tightly coupled to one provider.

12. Database

Primary application database:

MongoDB

MongoDB will store application/domain data such as:

Users
Notebooks
Documents
Document metadata
Document chunk metadata
Sessions
Conversations
Messages
Learning data
Future application entities

Vector storage should be handled by a dedicated vector-storage solution when appropriate.

13. File Storage

Uploaded documents should not depend permanently on the backend server's local filesystem.

Conceptual architecture:

Frontend
   ↓
Backend
   ↓
Storage Service
   ↓
Object / Cloud Storage

The storage implementation should be abstracted so that the provider can be changed later.

14. Authentication & Security

Authentication is a core backend responsibility.

The system should eventually support:

User registration
Login
Password hashing
Access tokens
Refresh tokens/session management
Authentication middleware
Authorization
Protected APIs
Resource ownership
Rate limiting
Request validation
Secure configuration

Users must only be able to access resources they are authorized to access.

15. API Design

The backend APIs should follow REST principles.

API versioning should be used.

Base structure:

/api/v1

Possible domains:

/api/v1/auth
/api/v1/users
/api/v1/notebooks
/api/v1/documents
/api/v1/chat
/api/v1/rag
/api/v1/learning

The API structure should allow new modules to be added without restructuring existing modules.

16. Background Processing

Document ingestion and AI operations can be computationally expensive.

The architecture should therefore support background processing.

Conceptual flow:

Upload Document
      ↓
Create Document Record
      ↓
Create Processing Job
      ↓
Background Worker
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
Vector Storage
      ↓
Update Document Status

The first implementation can be simple, but the architecture should allow background workers/queues to be introduced later.

17. Error Handling

The backend should use centralized error handling.

API responses should follow a consistent format.

Example:

{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "Document not found"
  }
}

Internal implementation details and sensitive information should not be exposed to clients.

18. Configuration Management

Configuration should never be hard-coded.

Examples:

Database URL
JWT configuration
LLM API keys
Embedding configuration
Vector database configuration
Storage configuration
Rate limits
Timeouts
Application settings

Use:

Environment Variables
        ↓
Centralized Configuration
        ↓
Application

Secrets must not be committed to source control.

19. Logging & Observability

The application should eventually support:

Structured logging
Request IDs
Error tracking
API latency monitoring
AI request monitoring
RAG retrieval metrics
Token usage monitoring
Health checks
Service status monitoring

AI-specific observability is important because AI requests can fail for reasons different from traditional APIs.

20. Testing Strategy

The architecture should make testing easy.

Backend

Eventually include:

Unit tests
Service tests
Repository tests
API/integration tests
Authentication tests
RAG tests
AI provider tests
Frontend

Eventually include:

Component tests
Service tests
API integration tests
End-to-end tests

Business logic should be isolated enough to test without running the entire system.

21. Scalability Requirements

TILA should be designed with future scalability in mind.

Important considerations:

Stateless APIs
Database indexing
Connection pooling
Caching
Background processing
Queue-based processing
Horizontal scaling
External file storage
Vector database
AI provider abstraction
Rate limiting
Timeouts

Do not implement every scalability feature immediately.

The architecture should simply avoid preventing them later.

22. Clean Architecture Principles

The project should follow:

Separation of concerns
SOLID principles
Dependency inversion
High cohesion
Low coupling
DRY
Reusable components
Clear module boundaries
Testability
Extensibility

Avoid over-engineering.

Only introduce abstractions, factories, interfaces, or additional layers when they provide a meaningful architectural benefit.

23. Development Phases

The project will be developed incrementally.

Phase 1 — Foundation
Project Setup
        ↓
Frontend Structure
        ↓
Backend Structure
        ↓
Configuration
        ↓
Database Setup
        ↓
Basic API Setup
Phase 2 — Authentication
Registration
Login
Authentication
Authorization
Session / Token Management
Phase 3 — Notebook
Create Notebook
Read Notebook
Update Notebook
Delete Notebook
Phase 4 — Documents
Upload
Storage
Document Metadata
Processing Status
Delete
Retrieve
Phase 5 — Document Processing
PDF Processing
Text Extraction
Text Cleaning
Chunking
Phase 6 — RAG
Embeddings
Vector Database
Semantic Search
Context Retrieval
RAG Pipeline
Phase 7 — AI Chat
LLM Integration
Prompt Management
RAG Chat
Conversation Management
Streaming Responses
Phase 8 — Learning Features
Summarization
Quiz Generation
Question Generation
Explanations
Study Assistance
Phase 9 — Agentic AI

Future capabilities may include:

AI Agents
Tool Calling
Planning
Memory
Multi-step Reasoning
Learning Agents
Personalized Study Agents
24. Future TILA Ecosystem

The long-term architecture may evolve into:

TILA
│
├── Authentication
├── User Management
├── Notebook Management
├── Document Management
├── Document Processing
├── RAG
├── Embeddings
├── Vector Search
├── AI / LLM
├── AI Chat
├── Summarization
├── Quiz Generation
├── Study Planning
├── Learning Analytics
├── Personalized Learning
└── AI Agents

The initial architecture should make this evolution possible without requiring a complete rewrite.

25. Key Architectural Principle

TILA should NOT be treated as:

CRUD Application + Chatbot

It should be designed as:

AI-Native Learning Platform

The architecture must therefore give first-class consideration to:

AI providers
RAG
Document processing
Vector search
AI conversations
Background jobs
Streaming
Observability
Scalability
Security

At the same time, avoid premature complexity.

The goal is:

Simple foundation → Modular architecture → Incremental complexity → Production-ready AI platform

26. Current Development Objective

The immediate objective is to establish the frontend and backend project structure.

The folder structure should:

Follow clean architectural boundaries.
Support the Router → Middleware → Controller → Service → Repository flow.
Support Repository Pattern where appropriate.
Support Factory Pattern for interchangeable providers.
Keep AI/RAG components modular.
Support future background processing.
Support authentication and security middleware.
Support API versioning.
Keep configuration centralized.
Be easy to test.
Be easy to extend.
Avoid unnecessary over-engineering.

The exact frontend and backend folder structure will be defined separately.