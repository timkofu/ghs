import os
from typing import Union
from datetime import datetime


from sqlalchemy.ext.asyncio import create_async_engine


class Base:

    __slots__ = ("engine",)

    def __init__(self) -> None:
        self.engine = create_async_engine(os.getenv("DATABASE_URL"))  # type:ignore

    async def add(
        self, domain_object: dict[str, Union[int, str, datetime]]
    ) -> dict[str, str]:
        raise NotImplementedError

    async def get(
        self, filter: dict[str, Union[int, str, datetime]]
    ) -> dict[str, Union[int, str, datetime]]:
        raise NotImplementedError
