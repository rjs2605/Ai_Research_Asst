from app.rag.chain import RAGChain
from app.rag.loader import DocumentLoader
from app.rag.retriever import Retriever
from app.rag.splitter import DocumentSplitter
from app.rag.vectorstore import VectorStore


class RAGService:
    def ask(self, question: str):
        retriever = Retriever()
        docs = retriever.search(question)
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )
        chain = RAGChain()
        return chain.run(
            question=question,
            context=context,
        )
    def ingest(self):
        loader = DocumentLoader()
        docs = loader.load_documents()
        splitter = DocumentSplitter()
        chunks = splitter.split_documents(docs)
        vector = VectorStore()
        vector.create(chunks)

        return {
            "documents": len(docs),
            "chunks": len(chunks),
        }
