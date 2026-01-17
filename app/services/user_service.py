from app.repositories.user import UserRepository

from .orm_service import ORMService


class UserService(ORMService[UserRepository]): ...
