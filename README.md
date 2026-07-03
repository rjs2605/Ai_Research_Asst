# 🚀 AI Research Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** application built with **FastAPI**, **LangChain**, **Ollama**, **ChromaDB**, and **Hugging Face Embeddings**.

The application retrieves relevant information from PDF documents and uses a locally hosted Large Language Model (LLM) via Ollama to generate accurate, context-aware responses.

---

# ✨ Features

- 📄 Load multiple PDF documents
- ✂️ Intelligent text chunking
- 🧠 Hugging Face Embeddings
- 🗂️ Chroma Vector Database
- 🔎 Semantic Similarity Search
- 🤖 Local LLM using Ollama
- ⚡ FastAPI REST API
- 📚 Modular project architecture
- 🐍 Python 3.12
- 📦 Dependency management with uv

---

# 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| FastAPI | REST API |
| LangChain | RAG Pipeline |
| Ollama | Local LLM |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| PyPDF | PDF Loading |
| uv | Package Manager |

---

# 📁 Project Structure

```
Ai_Research_Asst/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── llm/
│   ├── rag/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── data/
│   └── documents/
│
├── scripts/
│   └── ingest.py
│
├── chroma_db/
├── pyproject.toml
├── uv.lock
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/rjs2605/Ai_Research_Asst.git

cd Ai_Research_Asst
```

---

## Create Virtual Environment

```bash
uv venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv sync
```

---

# 🦙 Install Ollama

Download Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2
```

Run Ollama:

```bash
ollama serve
```

---

# 📄 Add Documents

Place all PDF files inside

```
data/documents/
```

---

# 📚 Create Vector Database

```bash
uv run -m scripts.ingest
```

---

# 🚀 Run FastAPI

```bash
uv run uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

## Health Check

```
GET /
```

Returns

```json
{
    "message": "AI Research Assistant is running 🚀"
}
```

---

## Health Status

```
GET /health
```

Returns

```json
{
    "status": "healthy"
}
```

---

## Ask Question

```
POST /ask
```

Request

```json
{
    "question":"What is Retrieval-Augmented Generation?"
}
```

Response

```json
{
    "answer":"Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models..."
}
```

---

# 🔄 RAG Workflow

```
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
Ollama
      │
      ▼
Final Answer
```

---

# 📸 Screenshots

Add screenshots here:

- Swagger UI
- API Response
- Terminal Output
- ChromaDB Ingestion

---

# 🔮 Future Improvements

- Docker Support
- Docker Compose
- GitHub Actions
- Streaming Responses
- Chat Memory
- Source Citations
- Hybrid Search
- Re-ranking
- Multi-user Support
- PDF Upload API
- Cloud Deployment

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository, create a new branch, and submit a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**R. Jeya Suriya**

- AI Engineer (Aspiring)
- Machine Learning Enthusiast
- LLM & RAG Developer
- Filmmaker

GitHub:
https://github.com/rjs2605
