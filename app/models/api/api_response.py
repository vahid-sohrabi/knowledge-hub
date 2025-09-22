from typing import TypeVar, Generic, Optional, List
from pydantic import BaseModel
from app.models.common.status import Status
from app.models.common.error_type import ErrorType

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    status: Status
    message: Optional[str] = None
    error_type: Optional[ErrorType] = None
    data: Optional[T] = None
    validation_errors: Optional[List[str]] = None

    @classmethod
    def ok(cls, data: T):
        return cls(status=Status.OK, message=None, data=data, error_type=None)

    @classmethod
    def error_message(cls, message: str):
        return cls(status=Status.ERROR, message=message, data=None, error_type=None)

    @classmethod
    def error_type(cls, error_type: ErrorType):
        return cls(status=Status.ERROR, message=error_type.value, error_type=error_type, data=None)
