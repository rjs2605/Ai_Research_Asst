from langchain_ollama import ChatOllama
from app.core.config import settings

def get_llm() -> ChatOllama:
    return ChatOllama(
        model=settings.OLLAMA_MODEL,
        temperature=0,
    )
