from datetime import datetime

from beanie import Document
from pydantic import BaseModel


class Audit(Document):
    actor: int
    action: str
    deatil: str
    created_at: datetime
    update_at: datetime

    class Settings:
        name = "audits"


class CreateAuditRequest(BaseModel):
    actor: int
    action: str
    deatil: str
    created_at: datetime
    update_at: datetime


class AuditResponse(BaseModel):
    id: int
    actor: int
    action: str
    deatil: str
    created_at: datetime
    update_at: datetime
