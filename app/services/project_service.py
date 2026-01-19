from typing import Any

from app.models.project import Project
from app.repositories.project import ProjectRepository

from .orm_service import ORMService


class ProjectService(ORMService[ProjectRepository]):
    def __init__(self, repository: ProjectRepository) -> None:
        super().__init__(repository=repository)

    async def create(self, data: dict[str, Any]) -> Project:
        project = Project(**data)
        return await self.repository.create(project)

    async def get(self, id_: Any) -> Project | None:
        return await self.repository.get(id=id_)

    async def list(
        self, *, limit: int = 50, offset: int = 0, filters: dict[str, Any] | None = None
    ) -> list[Project]:
        return await self.repository.list(skip=offset, limit=limit)

    async def update(self, id_: Any, data: dict[str, Any]) -> Project | None:
        return await self.repository.update(id=id_, patch=data)

    async def delete(self, id_: Any) -> bool:
        return await self.repository.delete(id=id_)
