# app/api/controllers/rag_controller.py
from fastapi import APIRouter, UploadFile, File
from typing import Optional
from app.services.pipeline.rag_pipeline import RAGPipeline
import os


class RAGController:
    """
    Controller for handling file ingestion and question answering
    using the RAGPipeline.
    """

    def __init__(self):
        self.router = APIRouter(prefix="/rag", tags=["RAG"])
        self.pipeline = RAGPipeline()

        # Define routes
        self.router.add_api_route("/upload/", self.upload_file, methods=["POST"])
        self.router.add_api_route("/query/", self.ask_question, methods=["GET"])

    async def upload_file(self, file: UploadFile = File(...), doc_id: Optional[str] = None):
        """
        Upload a file, ingest it using RAGPipeline, and store embeddings in Qdrant.
        """
        doc_id = doc_id or file.filename
        temp_path = f"temp_{file.filename}"

        # Save file temporarily
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        try:
            # Ingest the file
            self.pipeline.ingest_file(file_path=temp_path, doc_id=doc_id)
        finally:
            # Remove temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)

        return {"message": f"File '{file.filename}' uploaded and processed successfully."}

    async def ask_question(self, question: str, top_k: Optional[int] = None):
        """
        Receive a user question and return an answer using RAGPipeline.
        """
        answer = self.pipeline.answer(query=question, top_k=top_k)
        return {"answer": answer}
