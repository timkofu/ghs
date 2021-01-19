
import os
import asyncio
from functools import partial
from types import resolve_bases
from typing import Any, Coroutine

import asyncpg
import nest_asyncio
from typing import Tuple

nest_asyncio.apply()


class Database:
    """ Database interface """

    __slots__ = (
        "db_handle",
    )

    def __init__(self) -> None:
        self.db_handle: asyncpg.connection.Connection = None

    async def init_db(self, conn_coro: partial[Any] = partial(  # partial so we can hand it different conn params
        asyncpg.connect, os.getenv('DATABASE_URL')
    )) -> None:
        self.db_handle = await conn_coro()

    async def create(self, query: Tuple[str, ...]) -> asyncpg.Record:

        if not query[0].startswith('INSERT'):
            raise ValueError("Not an INSERT query")

        async with self.db_handle.transaction():
            return await self.db_handle.execute(*query)

    async def read(self, query: str) -> asyncpg.Record:

        if not query.startswith('SELECT'):
            raise ValueError("Not a SELECT query")

        async with self.db_handle.transaction():
            return await self.db_handle.fetch(query)

    async def update(self, query: str) -> asyncpg.Record:

        if not query.startswith('UPDATE'):
            raise ValueError("Not an UPDATE query")

        async with self.db_handle.transaction():
            return await self.db_handle.execute(query)

    async def delete(self, query: str) -> asyncpg.Record:

        if not query.startswith('DELETE'):
            raise ValueError("Not a DELETE query")

        async with self.db_handle.transaction():
            return await self.db_handle.execute(query)
