from typing import Any, AsyncGenerator

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from ..orm.model import Project as PR
from ghs.model.domain.project import Project as DPR


class Project(Base):
    async def add(self, domain_object: dict[str, Any]) -> dict[str, str]:
        return DPR(**domain_object).dict()

    async def get(  # type:ignore
        self, filter: dict[str, Any]
    ) -> AsyncGenerator[dict[str, Any], None]:

        project_fields = DPR.schema()["required"]
        if not all(k in project_fields for k in filter.keys()):
            raise ValueError("Invalid filter field value(s).")

        async with self.session() as session:  # type: ignore
            async with session.begin():  # type: ignore

                query = select(PR)  # type:ignore
                for column, value in filter.items():
                    query = query.filter(  # type:ignore
                        getattr(PR, column).like(f"%{value}%")
                    )  # type:ignore

                result = await session.execute(query)  # type: ignore

                for r in result:  # type:ignore
                    yield r.dict()  # type:ignore
