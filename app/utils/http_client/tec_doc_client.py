from app.utils.http_client.base_http_client import  BaseHttpClient
from httpx import AsyncClient
from typing import Self

class TecDocClient(BaseHttpClient):

    async def __aenter__(
        self,
        base_url: str,
    ) -> Self:
        self.client = AsyncClient(
            base_url=base_url,
        )
        return self

    async def __aexit__(self, *args):
        ...