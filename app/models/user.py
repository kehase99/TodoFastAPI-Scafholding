from datetime import datetime

from app.models.base import BaseDoc
from app.models.enums import Role


class Users(BaseDoc):
    username: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name = "users"
