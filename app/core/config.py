from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve repo root (two levels up from this file: app/core/config.py -> app/ -> repo root)
ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE)
        if ENV_FILE.exists()
        else None,  # <- load .env if it exists, otherwise use env vars
        case_sensitive=False,
        extra="ignore",
        env_ignore_empty=True,  # Ignore empty environment variables
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
