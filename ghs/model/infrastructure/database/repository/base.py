import os
from typing import Any, AsyncGenerator

from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Base:

    __slots__ = ("engine", "session")

    def __init__(self) -> None:
        self.engine = create_async_engine(  # type:ignore
            os.getenv("DATABASE_URL"), poolclass=NullPool
        )
        self.session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession  # type: ignore
        )  # type:ignore

    async def add(self, domain_object: dict[str, Any]) -> dict[str, str]:
        raise NotImplementedError

    async def get(self, filter: dict[str, Any]) -> AsyncGenerator[dict[str, Any], None]:
        raise NotImplementedError
