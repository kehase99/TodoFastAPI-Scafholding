from beanie import Document
from models.base import BaseDoc
from models.enums import Role
from pydantic import BaseModel


class Users(Document):
    username: str
    email: str
    password: str
    roles: Role
    created_at: BaseDoc.created_at
    updated_at: BaseDoc.updated_at
    is_active: BaseDoc.is_active

    class Settings:
        name = "users"


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    roles: Role
    created_at: BaseDoc.created_at
    updated_at: BaseDoc.updated_at
    is_active: BaseDoc.is_active


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str
    roles: Role
    created_at: BaseDoc.created_at
    updated_at: BaseDoc.updated_at
    is_active: BaseDoc.is_active
