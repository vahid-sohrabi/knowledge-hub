# app/api/controllers/question_api.py
from fastapi import APIRouter, Query
from typing import Optional
from app.services.pipeline.rag_pipeline import RAGPipeline


class QuestionAPI:
    """
    API class for asking questions to RAG pipeline.
    """

    def __init__(self, pipeline: RAGPipeline):
        self.pipeline = pipeline
        self.router = APIRouter(prefix="/rag/query", tags=["RAG QA"])
        self.router.add_api_route("/", self.ask_question, methods=["GET"])

    async def ask_question(self, question: str = Query(..., description="User question"),
                           top_k: Optional[int] = Query(None, description="Number of top results to retrieve")):
        answer = self.pipeline.answer(query=question, top_k=top_k)
        return {"answer": answer}
