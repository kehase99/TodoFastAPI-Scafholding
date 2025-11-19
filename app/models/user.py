from datetime import datetime

from beanie import Document
from models.enums import Role


class Users(Document):
    username: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name = "users"
