from typing import Any


class BaseHTTPException(Exception):
    def __init__(self, detail: Any, status_code: int):
        self.detail: Any = detail
        self.status_code: int = status_code