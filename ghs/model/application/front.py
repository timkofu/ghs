from typing import Any, AsyncGenerator

from ghs.model.infrastructure.database.repository.repository import Repository


class Front:

    __slots__ = ("limit", "repository")

    def __init__(self) -> None:
        self.limit: int = 100
        self.repository: Repository = Repository()

    async def page(self) -> AsyncGenerator[dict[str, Any], None]:

        async for row in self.repository.get({}):
            yield row
