from app.models.common.error_type import ErrorType


class ApiException(Exception):
    def __init__(self, message: str, error_type: ErrorType = ErrorType.UNEXPECT_ERROR):
        super().__init__(message)
        self.error_type = error_type
