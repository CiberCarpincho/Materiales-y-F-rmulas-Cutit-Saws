from fastapi import APIRouter

from app.api.v1.endpoints import formulas, materials

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(materials.router, prefix="/materiales", tags=["materiales"])
api_router.include_router(formulas.router, prefix="/formulas", tags=["formulas"])
