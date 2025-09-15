# app/api/controllers/file_upload_api.py
from fastapi import APIRouter, UploadFile, File
from typing import Optional
import os
from app.services.pipeline.rag_pipeline import RAGPipeline


class FileUploadAPI:
    """
    API class for uploading files and ingesting into RAG pipeline.
    """

    def __init__(self, pipeline: RAGPipeline):
        self.pipeline = pipeline
        self.router = APIRouter(prefix="/rag/upload", tags=["RAG Upload"])
        self.router.add_api_route("/", self.upload_file, methods=["POST"])

    async def upload_file(self, file: UploadFile = File(...), doc_id: Optional[str] = None):
        doc_id = doc_id or file.filename
        temp_path = f"temp_{file.filename}"

        # Save file temporarily
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        try:
            self.pipeline.ingest_file(file_path=temp_path, doc_id=doc_id)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        return {"message": f"File '{file.filename}' uploaded and processed successfully."}
