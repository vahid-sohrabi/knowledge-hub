from fastapi import APIRouter, Depends
from app.services.pipeline.rag_pipeline import RAGPipeline
from app.models.api.upload.file_upload_request import FileUploadRequest
from app.models.api.upload.file_upload_response import FileUploadResponse
from app.utils.file.file_handler import FileHandler


class FileUploadAPI:
    """
    API router for handling file uploads to the RAG pipeline.
    Uses FileHandler utility for file operations.
    """
    def __init__(self, pipeline: RAGPipeline, file_handler: FileHandler = None):
        self.pipeline = pipeline
        self.file_handler = file_handler or FileHandler()
        self.router = APIRouter(prefix="/rag/upload", tags=["RAG Upload"])
        self.router.add_api_route("/", self.upload_file, methods=["POST"])

    async def upload_file(
        self,
        request: FileUploadRequest = Depends()
    ) -> FileUploadResponse:
        doc_id = request.metadata.doc_id

        # Delegate to FileHandler util
        temp_path = await self.file_handler.save_temp(request.file)

        try:
            self.pipeline.ingest_file(file_path=temp_path, doc_id=doc_id)
        finally:
            self.file_handler.delete(temp_path)

        return FileUploadResponse(
            filename=request.file.filename,
            doc_id=doc_id
        )
