from ghs.model.infrastructure.database.orm.model import ProgrammingLanguage

from .base import Base


class ProgrammingLanguage(Base):
    async def get(self, filter: dict[str, str]) -> dict[str, str]:
        return await super().get(filter)

    async def add(self, project: dict[str, str]) -> dict[str, str]:
        return await super().add(project)
