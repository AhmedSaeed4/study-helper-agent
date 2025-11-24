
# 🏗️ ARCHITECTURAL BLUEPRINT: Study Notes Assistant (MVP)

**SYSTEM ROLE:** You are a Senior Python Solutions Architect.
**DEVELOPMENT ENVIRONMENT:**
*   **Project Status:** `uv` project initialized. Root directory active.
*   **Knowledge Source:** **Context7** (You **MUST** query this for `openai-agents` SDK syntax).
*   **Constraint:** **PURE SDK IMPLEMENTATION**. You are strictly forbidden from importing the standard `openai` library. All AI interactions must flow through the `openai-agents` abstractions.

---

## 📜 THE CONSTITUTION (System Rules)
1.  **Verification First:** Before writing code for the Agent, you must query Context7 to verify the exact import paths (e.g., `from openai_agents import Agent` vs `from openai_agents.core import Agent`).
2.  **Dependency Rigor:** Use only `uv add` for package installation.
3.  **State Persistence:** The Streamlit app must not re-read the PDF on every interaction. Use `st.session_state`.
4.  **Error Resilience:** All file operations and API calls must have `try/except` blocks.

---

## 📅 DETAILED EXECUTION PLAN

### 🔹 PHASE 1: SCAFFOLDING & DEPENDENCIES
**Objective:** Establish the directory structure and install libraries in the existing `uv` environment.

**Instructions to CLI:**
1.  **Package Installation:** Generate the exact command to install the required stack:
    *   `openai-agents` (The AI Engine)
    *   `streamlit` (The Frontend)
    *   `pypdf` (The PDF Parser)
    *   `python-dotenv` (Security/Config)
    *   *Command:* `uv add <packages>`

2.  **File System Structure:** Generate shell commands to create this specific tree:
    ```text
    /project_root
    ├── .env                  # API Keys
    ├── app.py                # Main Application Entry Point
    ├── /agent
    │   ├── __init__.py
    │   └── logic.py          # The 'Brain' (Pure SDK logic)
    └── /utils
        ├── __init__.py
        └── pdf_processor.py  # Data Ingestion Logic
    ```

### 🔹 PHASE 2: INGESTION LAYER (`utils/pdf_processor.py`)
**Objective:** Convert raw PDF binary data into clean, analyzed text.

**Instructions to CLI:**
Write a Python script that implements:
*   **Function:** `get_pdf_content(file_obj) -> str`
*   **Implementation Details:**
    1.  Initialize `PdfReader` from `pypdf`.
    2.  Loop through every page in the document.
    3.  Extract text and append to a buffer.
    4.  **Cleaning:** Replace multiple newlines (`\n\n\n`) with single newlines to save token usage.
    5.  **Exception Handling:** Wrap the logic in a block that catches `Exception` and returns a string starting with "Error: ...".

### 🔹 PHASE 3: INTELLIGENCE LAYER (`agent/logic.py`)
**Objective:** encapsulated the `openai-agents` SDK logic.

**Instructions to CLI:**
1.  **Context7 Lookup:** First, perform a tool call to Context7 with the query: *"Show me the basic usage example for creating an Agent in openai-agents python SDK."*
2.  **Code Construction:** Based on the retrieved syntax, write `agent/logic.py`:
    *   **Class:** `StudyBuddy`
    *   **`__init__`**: Load `OPENAI_API_KEY` from environment. Initialize the `Agent` object with a specific model (e.g., `gpt-4o-mini` or `gpt-3.5-turbo`) and a System Instruction: *"You are a helpful academic tutor."*
    *   **Method:** `ask_agent(prompt: str, context: str) -> str`
    *   **Logic:**
        1.  Combine inputs: `full_prompt = f"CONTEXT:\n{context}\n\nUSER REQUEST:\n{prompt}"`
        2.  Pass `full_prompt` to the SDK's run function.
        3.  Return the string response.

### 🔹 PHASE 4: EXPERIENCE LAYER (`app.py`)
**Objective:** Build a reactive UI that separates data loading from generation.

**Instructions to CLI:**
Write `app.py` with the following workflow:
1.  **Initialization:** Set Page Config (Title: "StudyGenius"). Load Environment variables.
2.  **Session Management:** Check `if "pdf_data" not in st.session_state`.
3.  **Sidebar (Input):**
    *   `st.file_uploader` for PDFs.
    *   If a file is uploaded **AND** it's different from what's in state:
        *   Call `utils.pdf_processor.get_pdf_content`.
        *   Store result in `st.session_state["pdf_data"]`.
        *   Show a success toast/message: "PDF Processed!".
4.  **Main Area (Interaction):**
    *   Check if `pdf_data` exists. If not, show "Please upload a file."
    *   **Tab 1: Smart Summary**
        *   Button: "Generate Study Sheet".
        *   On Click: Display a spinner ("Analyzing document..."). Call `StudyBuddy.ask_agent` with the prompt: *"Analyze the context and provide a structured summary with: 1. Executive Brief, 2. Key Concepts (Bullet points), 3. Important Dates/Figures."*
    *   **Tab 2: Quiz Generator**
        *   Button: "Generate Exam".
        *   On Click: Display a spinner ("Drafting questions..."). Call `StudyBuddy.ask_agent` with the prompt: *"Create a 5-question Multiple Choice Quiz based strictly on the text. Format: Question, Options, Correct Answer, Explanation."*

---

**🚀 MASTER COMMAND FOR GEMINI:**
"Gemini, acknowledge this Blueprint. Your first action is to query **Context7** to learn the correct import syntax for `openai-agents`. Once verified, output the **Phase 1** commands (shell) and the **Phase 2** code (Python)."