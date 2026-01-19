from typing import Any

from app.models.user import User
from app.repositories.user import UserRepository

from .orm_service import ORMService


class UserService(ORMService[UserRepository]):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(repository=repository)

    async def create(self, data: dict[str, Any]) -> User:
        user = User(**data)
        return await self.repository.create(user)

    async def get(self, id_: Any) -> User | None:
        return await self.repository.get(id=id_)

    async def list(
        self, *, limit: int = 50, offset: int = 0, filters: dict[str, Any] | None = None
    ) -> list[User]:
        return await self.repository.list(skip=offset, limit=limit)

    async def update(self, id_: Any, data: dict[str, Any]) -> User | None:
        return await self.repository.update(id=id_, patch=data)

    async def delete(self, id_: Any) -> bool:
        return await self.repository.delete(id=id_)
