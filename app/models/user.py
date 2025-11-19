from datetime import datetime

from beanie import Document
from models.enums import Role
from pydantic import BaseModel


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


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool
