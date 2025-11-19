from datetime import datetime

from beanie import Document
from pydantic import BaseModel


class Project(Document):
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name = "projects"


class CreateProjectRequest(BaseModel):
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool
