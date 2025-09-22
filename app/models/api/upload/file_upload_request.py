from typing import Optional
from fastapi import UploadFile, Form, File
from app.models.api.upload.file_metadata import FileMetadata


class FileUploadRequest:
    """
    Request model for file upload with optional metadata.
    Combines UploadFile (multipart/form-data) and metadata (from form fields).
    """
    def __init__(
        self,
        file: UploadFile = File(...),
        doc_id: Optional[str] = Form(None),
        description: Optional[str] = Form(None)
    ):
        self.file = file
        # Use FileMetadata model to hold metadata
        self.metadata = FileMetadata(
            doc_id=doc_id or file.filename,
            description=description
        )

    async def get_bytes(self) -> bytes:
        """
        Reads the uploaded file's content asynchronously.
        """
        return await self.file.read()
