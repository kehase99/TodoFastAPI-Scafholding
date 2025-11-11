import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import get_logger

app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
    description=settings.app.description,
    debug=settings.app.debug,
)

# Log configuration source on startup

logger = get_logger(__name__)
# logger.info(f"🔧 Configuration: {settings.log.level}")
print(logger)


@app.get("/health")
async def health() -> dict:
    # print(settings.config_source)
    print(settings.app.name)
    print(settings.app.version)
    return {
        "status": "healthy",
        "config_source": "settings.config_source",
        "app_name": settings.app.name,
        "version": settings.app.version,
    }


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.app.host,
        port=settings.app.port,
    )
