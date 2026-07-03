from app.rag.chain import RAGChain


def main():
    rag = RAGChain()
    while True:
        question = input("\nAsk (type 'exit' to quit): ")
        if question.lower() == "exit":
            break
        answer = rag.ask(question)
        print("\n")
        print("=" * 80)
        print(answer)
        print("=" * 80)

if __name__ == "__main__":
    main()