
import os
import math
import asyncio
from typing import List, AsyncGenerator

import github
from github import Github
from github.Repository import Repository

from ghs.model.database.database import Database


class Fetch:
    ''' Fetch stars and store them in DB '''

    __slots__ = ('ghh', 'dbh')

    def __init__(
        self,
        ghh: Github = Github(login_or_token=os.getenv("GH_AUTH_TOKEN")),
        dbh: Database = Database()
    ) -> None:
        self.ghh = ghh
        self.dbh = dbh

    async def _fetch_stars(self) -> AsyncGenerator[List[Repository], None]:

        user: github.NamedUser.NamedUser = self.ghh.get_user(str(os.getenv('GH_USERNAME')))
        stars: github.PaginatedList.PaginatedList[Repository] = user.get_starred()
        pages: int = math.ceil(stars.totalCount / 30)
        asyncio_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        for page in range(pages):

            yield await asyncio_loop.run_in_executor(None, stars.get_page, page)

            await asyncio.sleep(1)  # Give GH server a break

    async def stars(self) -> None:

        await self.dbh.init_db()

        async for projects in self._fetch_stars():

            for project in projects:

                project_details = "({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
                    project.name.capitalize(),
                    project.description,
                    project.html_url,
                    project.get_stargazers().totalCount,
                    project.get_stargazers().totalCount,
                    project.get_forks().totalCount,
                    project.get_forks().totalCount,
                )

                await self.dbh.create((
                    """
                    INSERT INTO project(
                        name, description, url, initial_stars,
                        current_stars, fork_count, initial_fork_count,
                        current_fork_count
                    ) VALUES {}
                    """.format(project_details).strip(),
                ))
                # will implement batch inserts later

                # create programming language(s) if not exists
                for language in project.get_languages():
                    await self.dbh.create((
                        "INSERT INTO pro_lang(name) values($1) ON CONFLICT (name) DO NOTHING", language
                    ))
