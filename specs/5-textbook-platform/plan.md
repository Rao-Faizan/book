# Implementation Plan: Textbook Platform (RAG & Personalization)

## 1. High-Level Architecture

This module implements the "Intelligent Layer" on top of the static book content. It involves building a separate FastAPI backend service that integrates with the Docusaurus frontend.

### Directory Structure
We will create a new root-level directory `platform/` alongside `book/` and `book_material/`.

```
platform/
├── backend/            # FastAPI Service
│   ├── app/
│   │   ├── api/        # Endpoints
│   │   ├── core/       # Config, Security
│   │   ├── services/   # Gemini, Qdrant, Neon logic
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── scripts/            # Ingestion Scripts
│   └── ingest_book.py  # Crawls docs/ and populates Qdrant
└── frontend-components/ # React components to drop into Docusaurus
    ├── ChatWidget.tsx
    ├── Personalizer.tsx
    └── AuthProfile.tsx
```

## 2. Component Breakdown

### Phase 1: Backend Skeleton & Environment
- **Goal**: Setup FastAPI with Gemini and Qdrant connections.
- **Tasks**:
    - Configure `google-generativeai` SDK.
    - Configure `qdrant-client`.
    - Setup Neon DB connection string.

### Phase 2: Knowledge Ingestion (RAG Core)
- **Goal**: Index the book content.
- **Tasks**:
    - Write a script to parse `.mdx` files from `book/docs/`.
    - Chunk text (Overlap: 50 tokens, Chunk Size: 500 tokens).
    - Generate Embeddings (`text-embedding-004`).
    - Upsert to Qdrant Cloud.

### Phase 3: The Brain (Gemini Integration)
- **Goal**: Answer questions.
- **Tasks**:
    - Implement `/chat/rag` endpoint.
    - Logic: Search Qdrant -> Build Prompt -> Call `gemini-2.5-flash`.
    - Implement Function Calling for `code_explainer` and `ros_command_lookup`.

### Phase 4: User Layer (Auth & Profile)
- **Goal**: Identify the reader.
- **Tasks**:
    - Setup **better-auth** (client & server).
    - Create `user_profiles` table in Neon.
    - Implement API to store/retrieve "Hardware Access" and "Python Level".

### Phase 5: Intelligent Features (Personalization/Translation)
- **Goal**: Adapting content.
- **Tasks**:
    - Implement `/personalize` endpoint: Fuses original text + User Profile -> Gemini Rewrite.
    - Implement `/translate` endpoint -> Gemini Translation.
    - Build Frontend React Components (Floating Chat, Toolbar Actions).

## 3. Execution Flow

1.  **Backend Setup**: Initialize the FastAPI project structure.
2.  **Database Init**: Run SQL migrations on Neon and Create Collection on Qdrant.
3.  **Ingestion**: Run the ingestion script to populate the vector DB.
4.  **API Dev**: Implement the 4 core endpoints.
5.  **Frontend Integration**: Add the Chat Widget and Context Menu to Docusaurus (using Swizzling or React Components).

## 4. Dependencies

-   **Cloud Keys**: `GOOGLE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`, `NEON_DATABASE_URL`.
-   **Python**: 3.10+.
-   **Node**: For Docusaurus frontend customization.

## 5. Success Indicators

-   **Ingestion**: 100% of chapters indexed in Qdrant.
-   **Query**: "How do I install Isaac Sim?" returns specific steps from Chapter 12.
-   **Profile**: User can log in and save their "Jetson Orin" preference.
-   **Rewrite**: Clicking "simplify" successfully returns a beginner-friendly version of a complex paragraph.
