from datetime import datetime

from beanie import Document
from models.enums import TaskStatus
from pydantic import BaseModel


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


class CreateTaskRequest(BaseModel):
    description: str
    project_id: int
    assigned_to: int
    status: TaskStatus
    created_at: datetime
    update_at: datetime
    is_active: bool


class TaskResponse(BaseModel):
    id: int
    description: str
    project_id: int
    assigned_to: int
    status: TaskStatus
    created_at: datetime
    update_at: datetime
    is_active: bool
