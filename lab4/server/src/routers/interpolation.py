from fastapi import APIRouter
from schemas.interpolation import (
    InterpolationRequest,
    InterpolationResponse,
    PointInterpolationRequest,
    PointInterpolationResponse,
)
from services.interpolation import InterpolationService

interpolation_router = APIRouter(prefix="/interpolation", tags=["Interpolation"])


@interpolation_router.post("/", response_model=InterpolationResponse)
async def interpolate(data: InterpolationRequest) -> InterpolationResponse:
    service = InterpolationService()
    return await service.interpolate(data)


@interpolation_router.post("/point", response_model=PointInterpolationResponse)
async def interpolate_point(data: PointInterpolationRequest) -> PointInterpolationResponse:
    service = InterpolationService()
    return await service.point_interpolate(data)
