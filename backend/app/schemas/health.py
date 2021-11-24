import enum

import pydantic


class Status(str, enum.Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"


class Health(pydantic.BaseModel):
    status: Status
    version: str
    releaseId: str
