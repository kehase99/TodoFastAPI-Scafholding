from app.repositories.project import ProjectRepository

from .orm_service import ORMService


class ProjectService(ORMService[ProjectRepository]): ...
