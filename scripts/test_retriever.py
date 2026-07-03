from app.rag.retriever import Retriever


def main():

    retriever = Retriever()
    question = input("Ask: ")
    docs = retriever.search(question)

    print("=" * 80)

    for i, doc in enumerate(docs, start=1):

        print(f"\nResult {i}")
        print("-" * 80)

        print(doc.page_content[:500])

        print("\nMetadata:")
        print(doc.metadata)

if __name__ == "__main__":
    main()