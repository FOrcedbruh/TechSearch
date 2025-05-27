from contextlib import asynccontextmanager
from starlette.types import ASGIApp


@asynccontextmanager
async def lifespan(app: ASGIApp):
    yield
