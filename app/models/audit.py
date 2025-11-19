from datetime import datetime

from beanie import Document


class Audit(Document):
    actor: int
    action: str
    deatil: str
    created_at: datetime
    update_at: datetime

    class Settings:
        name = "audits"
