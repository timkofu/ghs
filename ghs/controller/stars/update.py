
from .fetch import Fetch


class Update:

    __slots__ = ("fetcher",)

    def __init__(self, fetcher: Fetch = Fetch()):
        self.fetcher = fetcher

    async def update(self) -> None:

        self.fetcher.dbh.init_db()

        async for projects in self.fetcher._fetch_stars():
            for project in projects:
                self.fetcher.dbh.update(
                    """
                        UPDATE project SET
                        current_stars = {},
                        current_fork_count = {}
                        WHERE name = {}
                    """.format(
                        project.get_stargazers().totalCount,
                        project.get_forks().totalCount,
                        project.name.capitalize()
                    )
                )
