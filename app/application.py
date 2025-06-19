from fastapi import FastAPI
from starlette.types import ASGIApp
from starlette.requests import Request
from starlette.exceptions import HTTPException
from fastapi import status
from app.utils import lifespan
from app.presentation import router
from app.repositories.exceptions import BaseHTTPException


def create_app() -> ASGIApp:
    app = FastAPI(
        docs_url="/openapi/",
        lifespan=lifespan,
    )
    app.include_router(router)

    @app.exception_handler(BaseHTTPException)
    async def exc_handler(request: Request, exc: BaseHTTPException):
        raise HTTPException(
            status_code=exc.status_code,
            detail=exc.detail
        )

    @app.get("/", status_code=status.HTTP_200_OK)
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app
