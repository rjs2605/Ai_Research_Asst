from app.rag.loader import DocumentLoader
from app.rag.splitter import DocumentSplitter
from app.rag.vectorstore import VectorStore


def main():

    loader = DocumentLoader()
    documents = loader.load_documents()

    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    vectorstore = VectorStore()
    vectorstore.create(chunks)

    print("=" * 60)
    print(f"Pages  : {len(documents)}")
    print(f"Chunks : {len(chunks)}")
    print("Vector DB Created Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()