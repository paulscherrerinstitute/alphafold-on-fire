import fastapi

from app import config
from app.routers import health

settings = config.get_settings()
app = fastapi.FastAPI(title="alphafold-on-fire", version=settings.releaseId)


app.include_router(health.router, prefix="/health", tags=["health"])


@app.get("/")
async def get_root() -> dict[str, str]:
    return {"msg": "hello world"}
