-----------------------------------------------------------------------------------------------------------------------------------
HOW TO RUN THIS
------------------------------------------------------------------------------------------------------------------------------------
# 🚀 AI Research Assistant - Setup & Run Guide

This guide explains how to set up and run the AI Research Assistant project from scratch.

---

# Prerequisites

Make sure the following are installed:

- Python 3.12
- Git
- uv
- Ollama

---

# Step 1: Clone the Repository

```bash
git clone https://github.com/rjs2605/Ai_Research_Asst.git

cd Ai_Research_Asst
```

---

# Step 2: Create a Virtual Environment

```bash
uv venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# Step 3: Install Dependencies

```bash
uv sync
```

This installs all the required Python packages.

---

# Step 4: Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

---

# Step 5: Download the LLM

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama list
```

Expected output:

```
NAME
llama3.2
```

---

# Step 6: Start Ollama

```bash
ollama serve
```

Keep this terminal running.

---

# Step 7: Add Your PDF Files

Place all PDF files inside:

```
data/documents/
```

Example:

```
data/
└── documents/
    ├── rag.pdf
    ├── llm.pdf
    ├── ai.pdf
    └── sample.pdf
```

---

# Step 8: Create the Vector Database

Run:

```bash
uv run -m scripts.ingest
```

Expected output:

```
Found 4 PDF(s)

Loaded 85 pages

Created 247 chunks

Vector Database Created
```

---

# Step 9: Start the FastAPI Server

```bash
uv run uvicorn app.main:app --reload
```

Expected output:

```
INFO: Uvicorn running on:

http://127.0.0.1:8000
```

---

# Step 10: Open Swagger UI

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

# Step 11: Test the API

Select:

```
POST /ask
```

Request:

```json
{
    "question":"What is Retrieval-Augmented Generation?"
}
```

Example Response:

```json
{
    "answer":"Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models..."
}
```

---

# Updating Documents

Whenever you add new PDF files:

1. Copy PDFs into:

```
data/documents/
```

2. Rebuild the vector database:

```bash
uv run -m scripts.ingest
```

3. Restart FastAPI if it's already running.

---

# Common Commands

Create virtual environment

```bash
uv venv
```

Install dependencies

```bash
uv sync
```

Run ingestion

```bash
uv run -m scripts.ingest
```

Start FastAPI

```bash
uv run uvicorn app.main:app --reload
```

Run the chatbot script

```bash
uv run -m scripts.chat
```

---

# Troubleshooting

## ModuleNotFoundError

Run:

```bash
uv sync
```

---

## Ollama Connection Error

Ensure Ollama is running:

```bash
ollama serve
```

---

## Model Not Found

Download the model:

```bash
ollama pull llama3.2
```

---

## No Documents Found

Verify that PDF files are placed in:

```
data/documents/
```

---

# You're Ready!

Your AI Research Assistant is now ready to answer questions using your own PDF documents.
