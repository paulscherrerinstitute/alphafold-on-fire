import functools

import pydantic


class Settings(pydantic.BaseSettings):
    version: str
    release_id: str
    db_uri: pydantic.PostgresDsn
    db_echo: bool = False
    db_hide_params: bool = True
    audience: str
    auth_server: list[pydantic.AnyHttpUrl]


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
