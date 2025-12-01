from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import get_logger
from app.core.mongo import beanie_lifespan
from app.core.redis import redis_lifespan


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    try:
        await redis_lifespan()
        yield

    except Exception as e:
        print(f"Error in appliccation lifespan: {e}")
        raise
    finally:
        await beanie_lifespan()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.app_debug,
    lifespan=lifespan,
)

# Log configuration source on startup

logger = get_logger(__name__)
logger.info(f"🔧 Configuration: {settings.config_source}")


@app.get("/health")
async def health() -> dict:
    return {
        "status": "healthy",
        "config_source": settings.config_source,
        "app_name": settings.app_name,
        "version": settings.app_version,
    }


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
    )
