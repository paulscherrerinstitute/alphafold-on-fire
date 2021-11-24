import fastapi
from fastapi import responses

from app import config, schemas

router = fastapi.APIRouter()


class HealthResponse(responses.JSONResponse):
    media_type = "application/health+json"


@router.get(
    "",
    response_class=HealthResponse,
    response_model=schemas.Health,
)
async def get_health(
    response: HealthResponse,
    settings: config.Settings = fastapi.Depends(config.get_settings),
) -> schemas.Health:
    response.headers["Cache-Control"] = "max-age=3600"

    content = {
        "status": schemas.Status.PASS,
        "version": settings.version,
        "releaseId": settings.releaseId,
    }
    return schemas.Health(**content)
