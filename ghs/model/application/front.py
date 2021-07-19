from typing import Any

from ghs.model.infrastructure.database.repository.repository import Repository


class Pager:

    __slots__ = ("limit", "repository")

    def __init__(self) -> None:
        self.limit: int = 100
        self.repository: Repository = Repository()

    async def page(self) -> dict[str, Any]:

        async for row in self.repository.get({}):
            yield row
