from typing import Any

from app.models.audit import Audit
from app.repositories.audit import AuditRepository

from .orm_service import ORMService


class AuditService(ORMService[AuditRepository]):
    def __init__(self, repository: AuditRepository) -> None:
        super().__init__(repository=repository)

    async def create(self, data: dict[str, Any]) -> Audit:
        audit = Audit(**data)
        return await self.repository.create(audit)

    async def get(self, id_: Any) -> Audit | None:
        return await self.repository.get(id=id_)

    async def list(
        self, *, limit: int = 50, offset: int = 0, filters: dict[str, Any] | None = None
    ) -> list[Audit]:
        return await self.repository.list(skip=offset, limit=limit)

    async def update(self, id_: Any, data: dict[str, Any]) -> Audit | None:
        return await self.repository.update(id=id_, patch=data)

    async def delete(self, id_: Any) -> bool:
        return await self.repository.delete(id=id_)
