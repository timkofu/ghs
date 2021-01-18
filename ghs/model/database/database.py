
import os
import asyncio
from types import CoroutineType

import asyncpg
import nest_asyncio
from typing import Tuple

nest_asyncio.apply()


class Database:
    """ Database interface """

    __slots__ = (
        "db_handle",
    )

    def __init__(
        self,
        db_handle: asyncpg.connection.Connection = asyncio.get_event_loop().run_until_complete(
            asyncpg.connect(os.getenv('DATABASE_URL'))
        )  # candidate for the optimization stage (should work with one loop)
    ) -> None:
        self.db_handle = db_handle

    async def create(self, query: Tuple[str, ...]) -> asyncpg.Record:

        if not query[0].startswith('INSERT'):
            raise ValueError("Not an INSERT query")

        # async with self.db_handle.transaction():
        return await self.db_handle.execute(*query)

    async def read(self, query: str) -> asyncpg.Record:

        if not query.startswith('SELECT'):
            raise ValueError("Not a SELECT query")

        # async with self.db_handle.transaction():
        return await self.db_handle.fetch(query)

    async def update(self, query: str) -> asyncpg.Record:

        if not query.startswith('UPDATE'):
            raise ValueError("Not an UPDATE query")

        # async with self.db_handle.transaction():
        return await self.db_handle.execute(query)

    async def delete(self, query: str) -> asyncpg.Record:

        if not query.startswith('DELETE'):
            raise ValueError("Not a DELETE query")

        # async with self.db_handle.transaction():
        return await self.db_handle.execute(query)
