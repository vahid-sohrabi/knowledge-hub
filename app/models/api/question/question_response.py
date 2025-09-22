from typing import Optional, List
from pydantic import BaseModel


class AnswerItem(BaseModel):
    answer: str
    score: Optional[float] = None
    source: Optional[str] = None


class QuestionResponse(BaseModel):
    question: str
    top_k: Optional[int]
    answers: List[AnswerItem]
