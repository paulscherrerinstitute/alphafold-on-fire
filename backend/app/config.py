import functools

import pydantic


class Settings(pydantic.BaseSettings):
    version: str
    releaseId: str
    db_uri: pydantic.PostgresDsn
    db_echo: bool = False
    db_hide_params: bool = True


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
