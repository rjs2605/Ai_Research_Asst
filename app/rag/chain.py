from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.llm.ollama_client import get_llm


PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


class RAGChain:

    def __init__(self):
        self.llm = get_llm()

    def run(self, question: str, context: str):

        chain = (
            PROMPT
            | self.llm
            | StrOutputParser()
        )

        return chain.invoke(
            {
                "question": question,
                "context": context,
            }
        )