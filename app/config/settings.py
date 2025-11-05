from collections.abc import Callable
from typing import Any

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env') 
    pg_dsn: PostgresDsn
    cors_origins: list[str]

settings = Settings()

