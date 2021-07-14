from .base import Base
from ..orm.model import ProgrammingLanguage as PRL
from ghs.model.domain.programming_language import ProgrammingLanguage as DPRL


class ProgrammingLanguage(Base):
    async def get(self, filter: dict[str, str]) -> dict[str, str]:
        return DPRL(**filter).dict()

    async def add(self, domain_object: dict[str, str]) -> dict[str, str]:
        return DPRL(**domain_object).dict()
