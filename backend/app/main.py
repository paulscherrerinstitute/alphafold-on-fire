import fastapi

from app import config

settings = config.get_settings()
app = fastapi.FastAPI(title="alphafold-on-fire", version=settings.releaseId)


@app.get("/")
async def get_root() -> dict[str, str]:
    return {"msg": "hello world"}
