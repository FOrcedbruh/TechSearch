from fastapi import APIRouter, Query, Depends
from app.utils import VehicleType
from app.dependencies import get_selection_vehicle_service
from app.services import SelectionVehicleService
from app.dto.selection_vehicle.responses import ManufacturerModel

router = APIRouter(prefix="/selection-vehicle", tags=["Selection Vehicle"])


@router.get("/manufacturer")
async def get_manufacturer_view(
    vehicle_type: VehicleType = Query(None),
    service: SelectionVehicleService = Depends(get_selection_vehicle_service)
) -> list[ManufacturerModel]:
    return await service.get_manufacturer_list(vehicle_type)