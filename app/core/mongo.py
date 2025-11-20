import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import settings
from app.models.task import Task

_client: AsyncIOMotorClient | None = None


async def _wait_for_mongo(
    client: AsyncIOMotorClient, *, attempts: int = 10, delay: float = 0.5
) -> None:
    """Wait until Mongo responds to ping (helpful with Docker)."""
    mongo_uri = settings.mongodb_uri()

    client = AsyncIOMotorClient(mongo_uri)
    for count in range(attempts):
        try:
            await client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return
        except Exception as e:
            error = e
            count = count + 1
            if count >= 9:
                print(
                    f"MongoDB did not become ready after {attempts} try error: {error}"
                )
                return
            await asyncio.sleep(delay)


async def init_db() -> None:
    mongo_uri = settings.mongodb_uri()

    client = AsyncIOMotorClient(mongo_uri)
    await init_beanie(database=client.blog, document_models=[Task])


async def get_db() -> AsyncIOMotorDatabase | None:
    """
    Access the initialized Motor database. Call within app lifespan.
    """

    return None


@asynccontextmanager
async def beanie_lifespan() -> AsyncIterator[None]:
    """
    Creates Motor client from settings, waits for Mongo,
    initializes **Beanie** with your Document models, then closes on shutdown.
    """
    # set up client / beanie initialization here
    yield
    # cleanup / close client here
