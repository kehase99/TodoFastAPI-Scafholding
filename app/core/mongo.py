import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, cast

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import settings
from app.models.audit import Audit
from app.models.project import Project
from app.models.task import Task
from app.models.user import User

_client: AsyncIOMotorClient | None = None
_database: AsyncIOMotorDatabase | None = None


async def _wait_for_mongo(
    client: AsyncIOMotorClient, *, attempts: int = 10, delay: float = 0.5
) -> None:
    """Wait until Mongo responds to ping (helpful with Docker)."""
    for _ in range(attempts):
        try:
            await client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return
        except Exception as e:
            error = e
            await asyncio.sleep(delay)

    raise RuntimeError(
        f"MongoDB did not become ready after {attempts} times try error: {error}"
    )


async def get_db() -> AsyncIOMotorDatabase | None:
    """
    Access the initialized Motor database. Call within app lifespan.
    """

    return _database


document_models = [Task, Project, User, Audit]


@asynccontextmanager
async def beanie_lifespan() -> AsyncIterator[None]:
    """
    Creates Motor client from settings, waits for Mongo,
    initializes **Beanie** with your Document models, then closes on shutdown.
    """
    global _client, _database
    _client = AsyncIOMotorClient(settings.mongodb_uri())
    _database = _client(settings.database_name)

    await _wait_for_mongo(_client)
    await get_db()
    # set up client / beanie initialization here
    await init_beanie(database=cast(Any, _database), document_models=document_models)
    yield
    # cleanup / close client here
    _client.close()
