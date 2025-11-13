from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve repo root (two levels up from this file: app/core/config.py -> app/ -> repo root)
ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"


# Application settings
class ApplicationSettings(BaseModel):
    name: str = Field("Todo App", alias="APP_NAME")
    version: str = Field("0.1.0", alias="APP_VERSION")
    description: str = Field(
        "A simple Todo FastAPI application", alias="APP_DESCRIPTION"
    )
    debug: bool = Field(True, alias="APP_DEBUG")
    host: str = Field("localhost", alias="APP_HOST")
    port: int = Field(8000, alias="APP_PORT")
    reload: bool = Field(True, alias="APP_RELOAD")
    api_docs_url: str = Field("/docs", alias="APP_API_DOCS_URL")
    redoc_url: str = Field("/redoc", alias="/redoc")
    scalar_url: str = Field("/scalar", alias="APP_SCALAR_URL")
    openapi_url: str = Field("/openapi.json", alias="APP_OPENAPI_URL")


# Security settings
class SecuritySettings(BaseModel):
    secret_key: str = Field(
        "my_super_secret_key_here_for_todo_app_fast_Api", alias="SECURITY_SECRET_KEY"
    )
    jwt_algorithm: str = Field("HS256", alias="SECURITY_JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(
        30, alias="SECURITY_ACCESS_TOKEN_EXPIRE_MINUTES"
    )


# Database settings
class DatabaseSettings(BaseModel):
    host: str = Field("localhost", alias="DATABASE_HOST")
    port: int = Field(27019, alias="DATABASE_PORT")
    name: str = Field("mydb", alias="DATABASE_NAME")
    user: str = Field("root", alias="DATABASE_USER")
    password: str = Field("example", alias="DATABASE_PASSWORD")
    auth_sorce: str = Field("admin", alias="DATABASE_AUTH_SOURCE")


# Redis settings
class RedisSettings(BaseModel):
    host: str = Field("localhost", alias="REDIS_HOST")
    port: int = Field(6379, alias="REDIS_PORT")
    password: str | None = Field(None, alias="REDIS_PASSWORD")
    db: int = Field(0, alias="REDIS_DB")
    username: str | None = Field(None, alias="REDIS_USERNAME")
    ssl: bool = Field(False, alias="REDIS_SSL")
    ssl_cert_reqs: str = Field(None, alias="REDIS_SSL_CERT_REQS")
    socket_connect_timeout: int = Field(5, alias="REDIS_SOCKET_CONNECT_TIMEOUT")
    socket_timeout: int = Field(5, alias="REDIS_SOCKET_TIMEOUT")
    connection_pool_max_connections: int = Field(
        50, alias="REDIS_CONNECTION_POOL_MAX_CONNECTIONS"
    )
    recode_responses: bool = Field(True, alias="REDIS_DECODE_RESPONSES")


# Logger settings
class LogSettings(BaseModel):
    level: Literal["trace", "debug", "info", "warning", "error", "critical"] = Field(
        "debug", alias="LOG_LEVEL"
    )
    format: Literal["text", "json", "csv"] = Field("text", alias="LOG_FORMAT")
    file: str = Field("/var/log/app.log", alias="LOG_FILE")
    retention: str = Field("7d", alias="LOG_RETENTION")
    rotation: str = Field("1d", alias="LOG_ROTATION")
    handlers: str = Field("console,file", alias="LOG_HANDLERS")
    date_format: str = Field("%Y-%m-%d %H:%M:%S", alias="LOG_DATE_FORMAT")


class Settings(BaseSettings):
    app: ApplicationSettings
    security: SecuritySettings
    database: DatabaseSettings
    redis: RedisSettings
    log: LogSettings
    model_config = SettingsConfigDict(
        env_nested_delimiter=("_"),
        env_file=str(ENV_FILE)
        if ENV_FILE.exists()
        else None,  # <- load .env if it exists, otherwise use env vars
        case_sensitive=False,
        extra="ignore",
        env_ignore_empty=True,  # Ignore empty environment variables
    )


# @lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
