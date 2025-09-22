from pydantic import BaseModel


class FileUploadResponse(BaseModel):
    filename: str
    doc_id: str
