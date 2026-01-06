from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, TEXT, IndexModel

from app.models.base import BaseDoc
from app.models.enums import Role


class User(BaseDoc):
    username: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "users"
        indexes: ClassVar[list[IndexModel]] = [
            IndexModel([("name", TEXT), ("created_at", ASCENDING)])
        ]
