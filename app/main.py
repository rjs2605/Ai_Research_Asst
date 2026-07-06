from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Research Assistant",
    version="1.0.0",
    description="RAG + Ollama + FastAPI",
)
app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "AI Research Assistant is running 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
