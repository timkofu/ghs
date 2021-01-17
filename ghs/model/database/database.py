
import os
import asyncio
from types import CoroutineType

import asyncpg
from typing import Any, Tuple


class Database:
    """ Database interface """

    __slots__ = (
        "db_handle",
    )

    @staticmethod
    def run_and_get(coro: CoroutineType) -> Any:
        task: Any = asyncio.create_task(coro) # type: ignore
        asyncio.get_running_loop().run_until_complete(task)
        return task.result()

    # Give db handle in constructor instead of creating it within to help
    # give a mock object when testing
    def __init__(
        self,
        db_handle: asyncpg.connection.Connection = asyncpg.connect(os.getenv('DATABASE_URL'))
    ) -> None:
        self.db_handle = asyncio.run_coroutine_threadsafe(
            db_handle,
            asyncio.get_event_loop()
        ).result()

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
