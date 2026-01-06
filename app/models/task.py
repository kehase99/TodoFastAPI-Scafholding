from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, TEXT, IndexModel

from app.models.base import BaseDoc
from app.models.enums import TaskStatus


class Task(BaseDoc):
    description: str
    project_id: int
    assigned_to: int
    status: TaskStatus
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "tasks"
        indexes: ClassVar[list[IndexModel]] = [
            IndexModel([("description", TEXT), ("created_at", ASCENDING)])
        ]
