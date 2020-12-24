
import os

import asyncpg
from typing import Tuple


class Database:
    """ Database interface """

    __slots__ = (
        "db_handle",
    )

    # Give db handle in constructor instead of creating it within to help
    # give a mock object when testing
    def __init__(
        self,
        db_handle: asyncpg.connection.Connection = asyncpg.connect(os.getenv('DATABASE_URL'))
    ) -> None:
        self.db_handle = db_handle

    async def create(self, query: Tuple[str, ...]) -> asyncpg.Record:

        if not query[0].startswith('INSERT'):
            raise ValueError("Not an INSERT query")

        return await self.db_handle.execute(*query)

    async def read(self, query: str) -> asyncpg.Record:

        if not query.startswith('SELECT'):
            raise ValueError("Not a SELECT query")

        return await self.db_handle.fetch(query)

    async def update(self, query: str) -> asyncpg.Record:

        if not query.startswith('UPDATE'):
            raise ValueError("Not an UPDATE query")

        return await self.db_handle.execute(query)

    async def delete(self, query: str) -> asyncpg.Record:

        if not query.startswith('DELETE'):
            raise ValueError("Not a DELETE query")

        return await self.db_handle.execute(query)
