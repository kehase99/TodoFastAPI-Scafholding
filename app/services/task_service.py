from typing import Any

from app.models.task import Task
from app.repositories.task import TaskRepository

from .orm_service import ORMService


class TaskService(ORMService[TaskRepository]):
    def __init__(self, repository: TaskRepository) -> None:
        super().__init__(repository=repository)

    async def create(self, data: dict[str, Any]) -> Task:
        task = Task(**data)
        return await self.repository.create(task)

    async def get(self, id_: Any) -> Task | None:
        return await self.repository.get(id=id_)

    async def list(
        self, *, limit: int = 50, offset: int = 0, filters: dict[str, Any] | None = None
    ) -> list[Task]:
        return await self.repository.list(skip=offset, limit=limit)

    async def update(self, id_: Any, data: dict[str, Any]) -> Task | None:
        return await self.repository.update(id=id_, patch=data)

    async def delete(self, id_: Any) -> bool:
        return await self.repository.delete(id=id_)
