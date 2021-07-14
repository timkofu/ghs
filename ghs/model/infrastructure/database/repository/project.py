from typing import Union
from datetime import datetime

from .base import Base

# from ..orm.model import Project as PR
from ghs.model.domain.project import Project as DPR


class Project(Base):
    async def add(
        self, domain_object: dict[str, Union[int, str, datetime]]
    ) -> dict[str, str]:
        return DPR(**domain_object).dict()

    async def get(
        self, filter: dict[str, Union[int, str, datetime]]
    ) -> dict[str, Union[int, str, datetime]]:
        project_fields = DPR.schema()["required"]
        if not all(k in project_fields for k in filter.keys()):
            raise ValueError("Invalid filter field value(s).")

        return filter
