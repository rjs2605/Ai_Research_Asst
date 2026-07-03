from langchain_chroma import Chroma

from app.core.config import settings
from app.rag.embeddings import get_embedding_model


class Retriever:

    def __init__(self):
        self.embedding = get_embedding_model()

        self.db = Chroma(
            persist_directory=settings.CHROMA_PATH,
            embedding_function=self.embedding,
        )

    def get_retriever(self, k: int = 4):
        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

    def search(self, query: str, k: int = 4):
        docs = self.db.similarity_search(query, k=k)
        return docs