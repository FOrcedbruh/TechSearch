from app.services.base import BaseService
from app.utils import TecDocClient, VehicleType
from app.services.exceptions import APIAuthExceptionError
from app.dto.selection_vehicle.responses import ManufacturerModel

class SelectionVehicleService(BaseService):

    async def get_manufacturer_list(self, vehicle_type: VehicleType) -> list[ManufacturerModel]:
        async with TecDocClient() as client:
            res = await client.get_manufacturers_list(vehicle_type)
        if res["status_code"] == 401:
            raise APIAuthExceptionError(
                status_code=res["status_code"],
                detail=res["data"]
            )
        return res["data"]["list"]
