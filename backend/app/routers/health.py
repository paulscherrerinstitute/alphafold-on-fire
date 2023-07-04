import time

import fastapi
import sqlalchemy as sa
from fastapi import responses
from sqlalchemy.ext.asyncio import AsyncSession

from app import config, database, schemas

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
    db: AsyncSession = fastapi.Depends(database.get_db),
) -> schemas.Health:
    response.headers["Cache-Control"] = "max-age=3600"

    stmt = sa.text("SELECT now(), pg_postmaster_start_time()")
    t0 = time.perf_counter_ns()
    result = await db.execute(stmt)
    response_time_ns = time.perf_counter_ns() - t0
    now, start = result.one()

    content = {
        "status": schemas.Status.PASS,
        "version": settings.version,
        "releaseId": settings.release_id,
        "checks": {
            "postgresql:responseTime": [
                {
                    "componentType": "datastore",
                    "observedValue": response_time_ns / 1000000,
                    "observedUnit ": "ms",
                    "time": now,
                }
            ],
            "postgresql:uptime": [
                {
                    "componentType": "datastore",
                    "observedValue": now - start,
                    "observedUnit ": "s",
                    "time": now,
                }
            ],
        },
    }
    return schemas.Health(**content)
