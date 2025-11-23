from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, TEXT, IndexModel

from app.models.base import BaseDoc


class Project(BaseDoc):
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "projects"
        indexes: ClassVar[list[IndexModel]] = [
            IndexModel([("description", TEXT), ("created_at", ASCENDING)])
        ]
