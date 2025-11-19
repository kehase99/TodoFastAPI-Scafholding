from datetime import datetime

from beanie import Document


class Project(Document):
    name: str
    description: str
    owner_id: int
    created_at: datetime
    update_at: datetime
    is_active: bool

    class Settings:
        name = "projects"
