import enum
from typing import Any

import pydantic


class Status(str, enum.Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"


class Health(pydantic.BaseModel):
    status: Status
    version: str
    releaseId: str
    checks: dict[str, list[dict[str, Any]]]
