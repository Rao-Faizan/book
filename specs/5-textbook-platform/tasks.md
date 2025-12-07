# Tasks: Textbook Platform Implementation

**Branch**: `5-textbook-platform`
**Spec**: [spec.md](spec.md)

## Phase 1: Backend Infrastructure (FastAPI)
- [x] T001 [Backend] Initialize FastAPI project structure (app, routers, services)
- [x] T002 [Backend] Configure `settings.py` for env vars (Gemini, Qdrant, Neon)
- [x] T003 [Backend] Setup Qdrant Client singleton and health check endpoint
- [x] T004 [Backend] Setup Gemini `GenerativeModel` singleton ("gemini-2.5-flash")
- [x] T005 [Backend] Setup Neon Postgres connection (SQLAlchemy/AsyncPG)

## Phase 2: RAG Pipeline & Ingestion
- [x] T006 [Ingestion] Create `MDXParser` to extract clean text from docusaurus files
- [x] T007 [Ingestion] Implement `Chunker` (RecursiveCharacterTextSplitter)
- [x] T008 [Ingestion] Implement embedding generation (`text-embedding-004`)
- [x] T009 [Ingestion] Write `ingest.py` script to index all book chapters
- [x] T010 [API] Implement `/v1/chat/rag` endpoint (Search -> Prompt -> Generate)
- [x] T011 [API] Implement `/v1/chat/context` endpoint (Selected Text -> Generate)

## Phase 3: Agent Skills (Reusable Intelligence)
- [x] T012 [Skills] define `code_explainer` tool function schema
- [x] T013 [Skills] define `ros_command_lookup` tool function schema
- [x] T014 [API] Bind tools to Gemini chat session
- [ ] T015 [API] Verify tool execution in chat flow

## Phase 4: Authentication & User Profile
- [x] T016 [Auth] Configure **better-auth** server-side
- [x] T017 [DB] Create SQL migration for `user_profiles` table
- [x] T018 [API] Implement `POST /v1/profile` (Save expertise/hardware)
- [x] T019 [API] Implement `GET /v1/profile` (Retrieve context)

## Phase 5: Personalization & Translation
- [x] T020 [API] Implement `/v1/personalize` endpoint (Retrieve Profile -> Rewrite Prompt)
- [x] T021 [API] Implement `/v1/translate` endpoint (Urdu translation prompt)

## Phase 6: Frontend Integration (Docusaurus)
- [x] T022 [Frontend] Create `ChatWidget` React component
- [ ] T023 [Frontend] Integrate `better-auth` client for Login/Signup
- [ ] T024 [Frontend] Create `ProfileModal` to collect user preferences
- [ ] T025 [Frontend] Add "Ask AI" / "Explain" buttons to text selection menu
- [ ] T026 [Frontend] Add "Translate" button to page toolbar

## Phase 7: Deployment & Config
- [x] T027 [Ops] Create Dockerfile for FastAPI backend
- [x] T028 [Ops] Create `docker-compose.yml` for local dev (Frontend + Backend)
- [x] T029 [Ops] Switch to **SQLite** (fix Neon deployment blocker)
- [x] T030 [Ops] Switch to **Cohere** (fix Gemini missing key)
- [ ] T031 [Docs] Document API usage and Setup guide
