from fastapi import APIRouter

from .approximation import approximation_router

api_router = APIRouter(prefix="/api")
api_router.include_router(approximation_router)


@api_router.get("/health", status_code=200)
def health():
    return {"status": "ok"}
