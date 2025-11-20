from datetime import datetime

from app.models.base import BaseDoc


class Project(BaseDoc):
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name = "projects"
