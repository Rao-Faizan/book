---
id: 002
title: Clarify Command Prerequisites Failure Repeated
stage: spec
date: 2025-12-07
surface: agent
model: claude-opus-4-5-20251101
feature: physical-ai-robotics-textbook
branch: 1-ai-robotics-book
user: unknown
command: /sp.clarify
labels: ["prerequisites", "failure", "repeated"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
null
tests:
null
---

## Prompt

```
Aap `Spec-Kit Plus` ke liye ek **Unified Specification Prompt** de sakte hain, jahan aap sari requirements aur technical decisions (jaise Gemini ka use) ko ek jagah jama kar dein.

Yeh prompt aapko ek **detailed technical specification** banane mein madad karega.

-----

## 📝 Unified Technical Specification Prompt

Aap is prompt ko apne AI tool (jese Claude Code ya Spec-Kit Plus) mein istemal kar sakte hain:

```
"Generate a detailed, technical specification for the 'Physical AI & Humanoid Robotics' textbook platform. This specification must cover all required features and bonus scoring elements, outlining the complete system architecture and data flows.

### Project Context:
Textbook built on **Docusaurus**. The core requirement is bridging the gap between digital content and physical AI concepts.

### Technology Stack Decisions:
1.  **LLM/AI Engine:** Google Gemini SDK (using `text-embedding-004` and `gemini-2.5-flash`).
2.  **Backend/API:** **FastAPI**.
3.  **Vector Database:** **Qdrant Cloud Free Tier** (vector size must be **768**).
4.  **Transactional DB:** **Neon Serverless Postgres**.
5.  **Authentication:** **better-auth.com**.

### Core Deliverable: Integrated RAG Chatbot (100 Points)
1.  **Functionality:** The chatbot must answer questions based *only* on the textbook content stored in Qdrant.
2.  **Selected Text RAG:** Implement a feature where the user can select text on the page, and the chatbot answers based *only* on that specific context (bypassing Qdrant search).
3.  **Data Flow:** Describe the API structure for query processing (Frontend -> FastAPI -> Qdrant -> Gemini -> Frontend).

### Bonus Features (Score Optimization):

#### 1. Reusable Intelligence (50 Points)
* **Requirement:** Implement at least two reusable **Agent Skills/Tools** (using Gemini Function Calling equivalent).
* **Examples:** A `code_explainer(code_snippet)` tool and a `ros_command_lookup(topic)` tool.

#### 2. Authentication and Profile Collection (50 Points)
* Integrate **better-auth** for Signup/Signin.
* **Data Collection:** At Signup, capture and store the user's **Software Background** (e.g., Python expertise level) and **Hardware Access** (e.g., RTX 4080 or Jetson Orin availability) in **Neon Postgres**.

#### 3. Content Personalization (50 Points)
* Implement a frontend button to trigger content personalization for the logged user.
* **Logic:** The system must use the user's background (stored in Neon) to send a context-aware prompt to Gemini, asking it to **rewrite the current chapter section** (e.g., simplify the explanation for a beginner).

#### 4. Urdu Translation (50 Points)
* Implement a frontend button to translate the current chapter content to **Urdu** on demand using the Gemini API.

### Required Output Sections:
1.  System Architecture Diagram (showing data flow).
2.  API Endpoints Table (for RAG, Auth, Personalization, Translation).
3.  Qdrant Collection Schema (including payload metadata).
4.  Data Models (for User Profile storage in Neon).
"
```

## Response snapshot

The prerequisite script `.specify/scripts/powershell/check-prerequisites.ps1` failed to execute again. The error indicates 'pwsh' (PowerShell) is still not found in the environment.

## Outcome

- ✅ Impact: Unable to proceed with /sp.clarify due to repeated prerequisite script failure.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: User needs to troubleshoot PowerShell PATH or execution environment.
- 🧠 Reflection: The user confirmed PowerShell is installed, but the tool execution environment does not recognize 'pwsh'. This suggests a PATH issue or an environmental difference between the user's shell and the tool's execution context.

## Evaluation notes (flywheel)

- Failure modes observed: Persistent script execution environment issue (missing pwsh in PATH).
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
