# from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import ResponseEnvelope


class ProjectPostRequest(BaseModel):
    """Schema for creating a project via POST /project."""

    model_config = ConfigDict(extra="ignore")
    name: str
    description: str
    owner_Id: str = Field(
        ..., validation_alias="ownerId", serialization_alias="onwerId"
    )


class ProjectRead(BaseModel):
    id: str = Field(serialization_alias="id")
    name: str
    description: str
    owner_Id: str = Field(serialization_alias="ownerId")


class ProjectPostResponse(ResponseEnvelope[ProjectRead]):
    """Envelope wrapping the created project."""
