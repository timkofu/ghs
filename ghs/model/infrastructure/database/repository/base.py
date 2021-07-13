import os

from sqlalchemy.ext.asyncio import create_async_engine


class Base:

    __slots__ = ("engine",)

    def __init__(self) -> None:
        self.engine = create_async_engine(os.getenv("DATABASE_URL"))  # type:ignore

    async def add(self, project: dict[str, str]) -> dict[str, str]:
        raise NotImplementedError

    async def get(self, filter: dict[str, str]) -> dict[str, str]:
        raise NotImplementedError
