# SanS AI - Sanskrit Learning Chatbot

---

## 📜 Project Overview

**SanS AI** is a conversational AI system designed to make the profound wisdom of ancient Sanskrit texts accessible to a modern audience. This is a self project by **K . Kiran, IIT Kanpur**.

It leverages a **Retrieval-Augmented Generation (RAG)** architecture to provide accurate, context-aware, and citation-backed answers from a curated knowledge base of sacred Indian texts, including the **Bhagavad Gita, Ramayana, and the Yoga Sutras**.

---

## ✨ Key Features

-   **Multi-Modal Knowledge Base:** Users can select a specific text (e.g., Bhagavad Gita) to query, ensuring the AI provides domain-specific, highly relevant answers.
-   **Citation-Backed Responses:** Every answer is accompanied by the source document it was derived from, building user trust and fulfilling a core requirement of the problem statement.
-   **Cross-Lingual Understanding:** The system is designed to understand questions in plain English and retrieve answers from the original Sanskrit texts, seamlessly bridging the language gap for learners.
-   **Aesthetic & Intuitive UI:** The user interface is clean, modern, and easy to navigate, featuring a "Shloka of the Day" to engage users and promote daily learning.

---

## 🛠️ Tech Stack

The application is built on a robust client-server model, ensuring scalability and a smooth user experience.

### Backend

-   **Framework:** Python with FastAPI
-   **Core Logic:** LangChain for RAG pipeline orchestration
-   **LLM:** Google Gemini Pro
-   **Vector Database:** FAISS (Facebook AI Similarity Search) for efficient, local knowledge base storage
-   **Embeddings:** `google-generativeai-embeddings`

### Frontend

-   **Structure:** HTML5
-   **Styling:** Tailwind CSS for a modern, responsive design
-   **Interactivity:** Vanilla JavaScript using the Fetch API

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

-   Python 3.11+
-   A Google Gemini API Key

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a new file named `.env` in the root of the project.
    -   Add your Google Gemini API key to this file:
        ```
        GOOGLE_API_KEY="your_api_key_here"
        ```

5.  **Build the Knowledge Base:**
    -   Place your Sanskrit text files in the appropriate subdirectories within the `Corpus` folder (e.g., `Corpus/bhagavadgita`, `Corpus/ramayana`).
    -   Run the ingestion script to create the FAISS indexes. This only needs to be done once.
        ```bash
        python ingest.py
        ```

### Running the Application

1.  **Start the Backend Server:**
    ```bash
    uvicorn backend:app --reload
    ```
    The server will be running at `http://127.0.0.1:8000`.

2.  **Launch the Frontend:**
    -   Open the `index.html` file in your web browser (using the "Open with Live Server" extension in VS Code is recommended).

You can now interact with the SanS AI chatbot!
