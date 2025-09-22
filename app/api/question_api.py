from fastapi import APIRouter
from app.models.api.question.question_request import QuestionRequest
from app.models.api.question.question_response import QuestionResponse, AnswerItem


class QuestionAPI:
    """
    API class for asking questions to a RAG pipeline.
    """

    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.router = APIRouter(prefix="/rag/query", tags=["RAG QA"])
        self.router.add_api_route("/", self.ask_question, methods=["POST"])

    async def ask_question(self, request: QuestionRequest) -> QuestionResponse:
        answers = self.pipeline.answer(query=request.question, top_k=request.top_k)

        if isinstance(answers, str):
            answers = [AnswerItem(answer=answers)]
        elif isinstance(answers, list):
            answers = [
                AnswerItem(answer=a) if isinstance(a, str) else AnswerItem(**a)
                for a in answers
            ]

        return QuestionResponse(
            question=request.question,
            top_k=request.top_k,
            answers=answers
        )
