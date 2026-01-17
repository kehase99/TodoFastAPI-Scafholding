from app.repositories.audit import AuditRepository

from .orm_service import ORMService


class AuditService(ORMService[AuditRepository]): ...
