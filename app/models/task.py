from datetime import datetime

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
        name = "tasks"
