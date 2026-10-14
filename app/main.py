from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.errors import register_exception_handlers

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(api_router)
register_exception_handlers(app)


@app.get("/health", tags=["operacion"])
def health() -> dict[str, str]:
    return {"status": "ok"}
