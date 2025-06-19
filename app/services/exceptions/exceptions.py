from app.repositories.exceptions import BaseHTTPException

class APIAuthExceptionError(BaseHTTPException):
    def __init__(self, detail, status_code: int):
        super().__init__(detail, status_code)