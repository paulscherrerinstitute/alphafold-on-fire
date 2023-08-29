import functools

import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    version: str
    release_id: str
    db_uri: pydantic.PostgresDsn
    db_echo: bool = False
    db_hide_params: bool = True
    audience: str
    auth_server: pydantic.AnyHttpUrl


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
