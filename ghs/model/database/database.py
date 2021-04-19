import os
from typing import Any
from functools import partial
from datetime import time, date, timedelta, datetime

import asyncpg
from asyncache import cached
from cachetools import TTLCache


class Database:
    """ Database interface """

    __slots__ = ("db_handle",)

    def __init__(self) -> None:
        self.db_handle: asyncpg.connection.Connection = None

    async def init_db(
        self,
        conn_coro: partial[
            Any
        ] = partial(  # partial so we can hand it different conn params
            asyncpg.connect, os.getenv("DATABASE_URL")
        ),
    ) -> None:
        self.db_handle = await conn_coro()

    async def upsert(self, query: Any) -> asyncpg.Record:

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
    async def read(self, query: str) -> asyncpg.Record:

        if not query.startswith("SELECT"):
            raise ValueError("Not a SELECT query")

        async with self.db_handle.transaction():
            return await self.db_handle.fetch(query)

    async def delete(self, query: Any) -> asyncpg.Record:

        if not query[0].startswith(("DELETE", "TRUNCATE")):
            raise ValueError("Not a DELETE query")

        async with self.db_handle.transaction():
            return await self.db_handle.execute(*query)
