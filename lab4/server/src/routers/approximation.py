from fastapi import APIRouter
from schemas.approximation import ApproximationRequest, ApproximationResponse
from services.approximation import ApproximationService

approximation_router = APIRouter(prefix="/approximation", tags=["Approximation"])


@approximation_router.post("/", response_model=ApproximationResponse)
async def approximate(data: ApproximationRequest):
    service = ApproximationService()
    return await service.approximate(data)
