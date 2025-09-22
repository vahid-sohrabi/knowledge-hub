from enum import Enum


class ErrorType(str, Enum):
    VALIDATION_ERROR = "Validation common on fields"
    DATABASE_INTEGRATION_ERROR = "Server common"
    UNKNOWN_SERVER_ERROR = "Server common"
    CONNECTION_ERROR = "Module connection common"
    INVALID_DATA = "Invalid data"
    INVALID_PARAMETER = "Invalid parameter"
    DUPLICATE_ITEM = "Duplicate item"
    NULL_VALUE = "Invalid null value"
    UNEXPECT_ERROR = "An unexpected common occurred"
    TIMEOUT_ERROR = "Request timeout occurred"
    FILE_IS_TOO_LARGE = "The uploaded file exceeds the maximum allowed size"
    FILE_DOWNLOAD_FAILED = "Failed to download the requested file"
    FILE_DELETE_FAILED = "Failed to delete the specified file"
