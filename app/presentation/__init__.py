from fastapi import APIRouter
from app.presentation.selection_vehicle.selection_vehicle import router as selection_vehicle_router

router = APIRouter(prefix="/api/v1")
router.include_router(selection_vehicle_router)