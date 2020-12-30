
from .fetch import Fetch


class Update:

    __slots__ = ("fetcher",)

    def __init__(self, fetcher: Fetch = Fetch()):
        self.fetcher = fetcher

    async def update(self) -> None:

        async for projects in self.fetcher._fetch_stars():
            passs
