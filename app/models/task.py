from datetime import datetime

from beanie import Document
from models.enums import TaskStatus


class Task(Document):
    description: str
    project_id: int
    assigned_to: int
    status: TaskStatus
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name = "tasks"
