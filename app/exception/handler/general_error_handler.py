from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import traceback
from app.exception.api_exception import ApiException
from app.models.api.api_response import ApiResponse
from app.models.common.error_type import ErrorType
from app.utils.log.central_logger import CentralLogger
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import IntegrityError


class GeneralErrorHandler:
    def __init__(self):
        self.logger = CentralLogger()

    async def handle_exception(self, request: Request, exc: ApiException):
        """
        Centralized error handling for FastAPI routes.
        Logs the full traceback and returns a standardized ApiResponse.
        """
        # Log the full traceback
        tb = traceback.format_exc()
        self.logger.log_error(f"Exception at {request.url}:\n{tb}")

        # Default HTTP status code
        status_code = 500

        # Determine error type and prepare response
        if isinstance(exc, HTTPException):
            status_code = exc.status_code
            if status_code == 400:
                response = ApiResponse.error_message(str(exc.detail))
            else:
                response = ApiResponse.error_type(ErrorType.UNKNOWN_SERVER_ERROR)
        elif isinstance(exc, ValidationError):
            status_code = 400
            response = ApiResponse.error_type(ErrorType.VALIDATION_ERROR)
        elif isinstance(exc, IntegrityError):
            status_code = 400
            response = ApiResponse.error_type(ErrorType.DATABASE_INTEGRATION_ERROR)
        elif isinstance(exc, ApiException):
            status_code = 400
            response = ApiResponse.error_type(exc.error_type)
        else:
            response = ApiResponse.error_type(ErrorType.UNKNOWN_SERVER_ERROR)

        return JSONResponse(
            status_code=status_code,
            content=response.dict()
        )
