from pathlib import Path
import shutil

from langchain_chroma import Chroma
from langchain_core.documents import Document
from app.core.config import settings
from app.core.logging import logger
from app.rag.embeddings import get_embedding_model

class VectorStore:
    def __init__(self):
        self.embedding = get_embedding_model()
    def create(self, chunks: list[Document]):
        logger.info("Creating Chroma Database...")
        db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding,
            persist_directory=settings.CHROMA_PATH,
        )
        logger.info("Vector Database Created.")

        return db

    def load(self):
        return Chroma(
            persist_directory=settings.CHROMA_PATH,
            embedding_function=self.embedding,
        )
    def reset(self):
        chroma_path = Path(settings.CHROMA_PATH)
        if chroma_path.exists():
            shutil.rmtree(chroma_path)
        chroma_path.mkdir(parents=True, exist_ok=True)

        logger.info("Vector Database Reset.")
