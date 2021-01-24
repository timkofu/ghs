
import os
import math
import asyncio
import logging
from typing import List, AsyncGenerator, Set

import github
from asyncpg import Record
from github import Github
from github.Repository import Repository

from ghs.controller.commons import DEBUG
from ghs.model.database.database import Database


class Update:
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

        user: github.NamedUser.NamedUser = await asyncio.get_running_loop().run_in_executor(
            None, self.ghh.get_user, str(os.getenv('GH_USERNAME'))
        )
        stars: github.PaginatedList.PaginatedList[Repository] = await asyncio.get_running_loop().run_in_executor(
            None, user.get_starred
        )
        pages: int = math.ceil(stars.totalCount / 30)  # GitHub pagination count

        for page in range(pages):

            yield await asyncio.get_event_loop().run_in_executor(None, stars.get_page, page)

            await asyncio.sleep(1)  # Give GH server a break

    async def stars(self) -> None:

        await self.dbh.init_db()
        current_stars: Set[str] = set()  # For use in removing unstared projects

        async for projects in self._fetch_stars():

            for project in projects:

                project_name = project.name.capitalize()
                current_stars.add(project_name)

                project_details = (
                    project_name,
                    str(project.description).replace("'", "''"),  # May be None, in which case 'None'
                    project.html_url,
                    project.get_stargazers().totalCount,
                    project.get_forks().totalCount,
                )

                query: str = """
                    INSERT INTO project(
                        name, description, url, initial_stars,
                        current_stars, initial_fork_count,
                        current_fork_count
                    ) VALUES ({0}) ON CONFLICT (name) DO UPDATE
                    SET name='{1}', description='{2}', current_stars={3}, current_fork_count={4}
                    RETURNING project_id
                """.format(
                    "'{0}','{1}','{2}',{3},{4},{5},{6}".format(
                        project_details[0],
                        project_details[1],
                        project_details[2],
                        project_details[3],
                        project_details[3],
                        project_details[4],
                        project_details[4],
                    ),
                    project_details[0], project_details[1], project_details[3], project_details[4]
                ).strip()

                if DEBUG:
                    logging.getLogger("uvicorn").info(query)

                project_id: int = await self.dbh.upsert((query,))
                # will implement batch inserts later

                # create programming language(s) if not exists
                for language in project.get_languages():

                    language_id: int = await self.dbh.upsert((
                        f"""INSERT INTO pro_lang(name) values('{language}') ON CONFLICT (name) DO UPDATE
                        SET name = EXCLUDED.name
                        RETURNING language_id
                        """.strip(),  # Need to set it (name) so RETURNING can work
                    ))

                    # Create many-to-many relationship
                    query = f"INSERT INTO pr_pl values({language_id}, {project_id}) ON CONFLICT DO NOTHING"
                    if DEBUG:
                        logging.getLogger("uvicorn").info(query)
                    await self.dbh.upsert((query,))

        # Now we remove unstarred repos
        stored_stars: Set[str] = {p['name'] for p in await self.dbh.read("SELECT name FROM project")}
        fallen_stars: Set[str] = stored_stars - current_stars

        for star in fallen_stars:
            await self.dbh.delete(f"DELETE FROM project WHERE name = '{star}'")
