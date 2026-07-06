from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from app.core.config import settings
from app.core.logging import logger

class DocumentLoader:   
    def __init__(self):
        self.data_path = Path(settings.DATA_PATH)
    def load_documents(self) -> list[Document]:
        documents: list[Document] = []
        if not self.data_path.exists():
            logger.warning(f"Directory not found: {self.data_path}")
            return documents
        pdf_files = sorted(self.data_path.rglob("*.pdf"))
        logger.info(f"Found {len(pdf_files)} PDF(s).")
        for pdf in pdf_files:
            try:
                logger.info(f"Loading: {pdf}")
                loader = PyPDFLoader(str(pdf))
                docs = loader.load()
                documents.extend(docs)
                logger.info(f"Loaded {len(docs)} pages from {pdf.name}")
            except Exception as e:
                logger.error(f"Failed to load {pdf}: {e}")
        logger.info(f"Total pages loaded: {len(documents)}")

        return documents
