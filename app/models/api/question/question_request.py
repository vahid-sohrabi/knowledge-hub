from typing import Optional
from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str
    top_k: Optional[int] = None
