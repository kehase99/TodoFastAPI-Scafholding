from datetime import datetime
from time import timezone

from beanie import Document, Insert, Replace, Save, before_event
from pydantic import Field

utcnow = lambda: datetime.now(timezone.utc)


class BaseDoc(Document):
    created_at: datetime = Field(default_factory=utcnow, alias="createdAt")
    updated_at: datetime = Field(default_factory=utcnow, alias="updatedAt")
    is_active: bool = Field(default=True, alias="isActive")

    @before_event([Insert, Save, Replace])
    def _update_timestamp(self) -> None:
        self.updated_at = utcnow

    class Settings:
        validate_on_save = True
