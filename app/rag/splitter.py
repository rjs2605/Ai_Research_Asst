from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.logging import logger

class DocumentSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        chunks = self.splitter.split_documents(documents)
        logger.info(f"Created {len(chunks)} chunks.")
        
        return chunks
