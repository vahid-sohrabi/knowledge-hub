from pydantic import BaseModel
from typing import Optional


class FileMetadata(BaseModel):
    """
    Metadata for uploaded files.
    """
    doc_id: Optional[str] = None
    description: Optional[str] = None
