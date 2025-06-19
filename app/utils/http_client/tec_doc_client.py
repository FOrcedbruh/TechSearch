from app.utils.http_client.base_http_client import  BaseHttpClient
from httpx import AsyncClient
from typing import Self, Any
from app.core import Settings
from enum import IntEnum

settings = Settings()

class VehicleType(IntEnum):
    PASSENGER = 1
    TRUCK = 2
    MOTOCYCLE = 3


class TecDocClient(BaseHttpClient):
    API_KEY: str = settings.external_api.api_key
    BASE_URL: str = settings.external_api.base_url

    async def __aenter__(
        self
    ) -> Self:
        self.client = AsyncClient(
            base_url=self.BASE_URL,
            headers={"X-Api-Key": self.API_KEY}
        )
        return self

    async def __aexit__(self, *args):
        await self.client.aclose()

    async def get_manufacturers_list(self, vehicle_type: VehicleType) -> dict[str, Any]:
        try:
            res = await self.client.get(
                url="/manufacturer",
                params={
                    "mfa_type": vehicle_type
                }
            )
        except Exception as e:
            raise e
        finally:
            return {
                "status_code": res.status_code,
                "data": res.json()
            }
        