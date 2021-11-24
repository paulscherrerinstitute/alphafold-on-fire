import functools

import pydantic


class Settings(pydantic.BaseSettings):
    version: str
    releaseId: str


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
