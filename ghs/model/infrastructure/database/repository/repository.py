import os
from importlib import import_module
from typing import Any, AsyncGenerator

from sqlalchemy.pool import NullPool
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Repository:

    __slots__ = ("engine", "session", "_don")

    def __init__(self) -> None:
        self.engine = create_async_engine(  # type:ignore
            os.getenv("DATABASE_URL"), poolclass=NullPool
        )
        self.session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession  # type: ignore
        )  # type:ignore
        self._don: str

    @property
    def domain_object_name(self) -> str:
        return self._don

    @domain_object_name.setter
    def domain_object_name(self, value: str) -> None:
        value = value.lower()
        if value not in ("programminglanguage", "project"):
            raise ValueError("Correct options: Project, ProgrammingLanguage")
        self._don = value

    async def _get_orm_and_domain_objects(self) -> tuple[Any, Any]:
        orm_object = getattr(
            import_module("ghs.model.infrastructure.database.orm.model"),
            self._don.capitalize(),
        )
        domain_object = getattr(
            import_module(f"ghs.model.domain.{self._don}"),
            self._don.capitalize(),
        )
        return orm_object, domain_object

    async def add(
        self,
        object_details: dict[str, Any],
    ) -> dict[str, str]:

        orm_object, domain_object = await self._get_orm_and_domain_objects()  # type: ignore
        # Validate details
        try:
            domain_object(**object_details).dict()  # type:ignore
        except Exception as e:
            raise ValueError(f"Invalid object details: {str(e)}")

        # INSERT is always UPSERT
        # query = (
        #     insert(orm_object)
        #     .values(**object_details)
        #     .on_conflict_do_update(index_elements=["name"], set_=object_details)
        #     .returning(orm_object.c.id)
        # )

        return {"its": "true"}

    async def get(  # type:ignore
        self, filter: dict[str, Any]
    ) -> AsyncGenerator[dict[str, Any], None]:

        orm_object, domain_object = await self._get_orm_and_domain_objects()  # type: ignore

        async with self.session() as session:  # type: ignore
            async with session.begin():  # type: ignore

                query = select(orm_object)  # type:ignore

                if filter:  # If filter is not empty
                    project_fields = domain_object.schema()["required"]  # type: ignore
                    if not all(k in project_fields for k in filter.keys()):
                        raise ValueError("Invalid domain object key:value pair(s).")
                    for column, value in filter.items():
                        query = query.filter(  # type:ignore
                            getattr(orm_object, column).like(f"%{value}%")
                        )  # type:ignore

                result = await session.execute(query)  # type: ignore

                for r in result:  # type:ignore
                    yield r.dict()  # type:ignore
