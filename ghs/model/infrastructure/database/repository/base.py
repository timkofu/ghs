import os
from typing import Union
from datetime import datetime


from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Base:

    __slots__ = ("engine", "session")

    def __init__(self) -> None:
        self.engine = create_async_engine(  # type:ignore
            os.getenv("DATABASE_URL"), poolclass=NullPool
        )

    async def add(
        self, domain_object: dict[str, Union[int, str, datetime]]
    ) -> dict[str, str]:
        raise NotImplementedError

    async def get(
        self, filter: dict[str, Union[int, str, datetime]]
    ) -> dict[str, Union[int, str, datetime]]:
        raise NotImplementedError
