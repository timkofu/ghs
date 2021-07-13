import os
from typing import Any
from datetime import time, date, timedelta, datetime

from asyncache import cached
from cachetools import TTLCache
from asyncpg import (
    connect,
)

from asyncpg.connection import Connection


class Repository:
    """Database interface"""

    @classmethod
    async def get_database_handle(cls, conn_creds: dict[str, str]) -> object:
        dbh = cls()
        if conn_creds:
            dbh.db_handle = await connect(**conn_creds)
        else:
            dbh.db_handle = await connect(
                str(os.getenv("DATABASE_URL")).replace(
                    "+asyncpg", ""
                )  # Workaround as I move to SQLAlchemy
            )
        return dbh

    __slots__ = ("db_handle",)

    def __init__(self) -> None:
        self.db_handle: Connection

    async def upsert(self, query: Any) -> Any:

        if not query[0].startswith("INSERT"):
            raise ValueError("Not an INSERT query")

        async with self.db_handle.transaction():  # type: ignore
            return await self.db_handle.fetchval(*query)  # type: ignore

    # Cache results from now untill a minute before midnight, as the stars
    # are updated at midnight.
    @cached(
        cache=TTLCache(
            maxsize=128,
            ttl=(
                (
                    datetime.combine((date.today() + timedelta(days=1)), time())
                    - timedelta(minutes=1)
                )
                - datetime.utcnow()
            ).seconds,
        )
    )
    async def read(self, query: str) -> Any:

        if not query.startswith("SELECT"):
            raise ValueError("Not a SELECT query")

        async with self.db_handle.transaction():  # type: ignore
            return await self.db_handle.fetch(query)  # type: ignore

    async def delete(self, query: tuple[str, ...]) -> Any:

        if not query[0].startswith(("DELETE", "TRUNCATE")):
            raise ValueError("Not a DELETE query")

        async with self.db_handle.transaction():  # type: ignore
            return await self.db_handle.execute(*query)  # type: ignore
