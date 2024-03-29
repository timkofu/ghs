import os
from typing import Any, Union
from datetime import time, date, timedelta, datetime

from asyncache import cached
from cachetools import TTLCache
from asyncpg import connect, Record
from asyncpg.connection import Connection


class Database:
    """Database interface"""

    @classmethod
    async def get_database_handle(
        cls, conn_creds: Union[dict[str, str], None] = None
    ) -> Connection:
        dbh = cls()
        if isinstance(conn_creds, dict):
            dbh.db_handle = await connect(**conn_creds)
        elif conn_creds is None:
            dbh.db_handle = await connect(os.getenv("DATABASE_URL"))
        return dbh

    __slots__ = ("db_handle",)

    def __init__(self) -> None:
        self.db_handle: Connection = None

    async def upsert(self, query: Any) -> Record:

        if not query[0].startswith("INSERT"):
            raise ValueError("Not an INSERT query")

        async with self.db_handle.transaction():
            return await self.db_handle.fetchval(*query)

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
    async def read(self, query: str) -> Record:

        if not query.startswith("SELECT"):
            raise ValueError("Not a SELECT query")

        async with self.db_handle.transaction():
            return await self.db_handle.fetch(query)

    async def delete(self, query: tuple[str, ...]) -> Record:

        if not query[0].startswith(("DELETE", "TRUNCATE")):
            raise ValueError("Not a DELETE query")

        async with self.db_handle.transaction():
            return await self.db_handle.execute(*query)
