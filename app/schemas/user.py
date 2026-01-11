# from __future__ import annotations
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.enums import Role
from app.schemas.common import ResponseEnvelope

T = TypeVar("T")


class UserPostRequest(BaseModel):
    """Schema for creating a user via POST /users.

    Fields:
    - username (public API name; stored internally as full_name)
    - email
    - password
    - roles (optional)

    Extra fields are ignored to keep the payload strict but flexible.
    """

    model_config = ConfigDict(extra="ignore")
    username: str
    email: EmailStr
    password: str
    # roles:


class UserRead(BaseModel, Generic[T]):
    """Shape of user returned by the API (no password)."""

    id: str = Field(serialization_alias="id")
    username: str
    email: EmailStr
    roles: Role


class UserPostResponse(ResponseEnvelope[UserRead]):
    """Envelope wrapping the created user with status and message."""
