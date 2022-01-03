from functools import lru_cache

from pydantic import BaseSettings, FilePath


class Settings(BaseSettings):
    GOOGLE_APPLICATION_CREDENTIALS: FilePath


@lru_cache
def get_settings():
    return Settings()  # type:ignore
