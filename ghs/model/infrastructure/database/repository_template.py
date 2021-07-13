import os

from sqlalchemy.ext.asyncio import create_async_engine


class RepositoryBase:

    __slots__ = ("engine",)

    def __init__(self) -> None:
        self.engine = create_async_engine(os.getenv("DATABASE_URL"))  # type:ignore
