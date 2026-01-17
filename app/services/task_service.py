from app.repositories.task import TaskRepository

from .orm_service import ORMService


class TaskService(ORMService[TaskRepository]): ...
