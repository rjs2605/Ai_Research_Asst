from fastapi import APIRouter

from app.schemas.request import QuestionRequest
from app.schemas.response import QuestionResponse
from app.services.rag_service import RAGService
from app.rag.vectorstore import VectorStore
router = APIRouter()

rag = RAGService()


@router.post("/ask", response_model=QuestionResponse)
async def ask(request: QuestionRequest):

    answer = rag.ask(request.question)

    return QuestionResponse(answer=answer)




@router.delete("/reset-db")
async def reset():

    VectorStore().reset()

    return {
        "message": "Vector database deleted."
    }