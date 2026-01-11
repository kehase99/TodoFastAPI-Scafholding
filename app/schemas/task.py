# from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import TaskStatus
from app.schemas.common import ResponseEnvelope


class TaskPostRequest(BaseModel):
    """Schema for creating a task via POST /tasks"""

    model_config = ConfigDict(extra="ignore")
    descruption: str
    project_id: str = Field(
        ..., validation_alias="projectId", serialization_alias="projectId"
    )
    assigned_to: str
    status: TaskStatus


class TaskRead(BaseModel):
    id: str = Field(serialization_alias="id")
    description: str
    project_id: str = Field(serialization_alias="projectId")
    assighned_to: str
    status: TaskStatus


class TaskPostResponse(ResponseEnvelope[TaskRead]):
    """Envelope wrapping the created task."""
