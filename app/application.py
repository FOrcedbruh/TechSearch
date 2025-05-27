from fastapi import FastAPI
from starlette.types import ASGIApp
from fastapi import status
from app.utils import lifespan
from app.presentation import router


def create_app() -> ASGIApp:
    app = FastAPI(
        docs_url="/openapi/",
        lifespan=lifespan,
        router=router,
    )

    @app.get("/", status_code=status.HTTP_200_OK)
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app
