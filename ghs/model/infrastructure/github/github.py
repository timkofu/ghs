import os
import math
import asyncio
from datetime import datetime
from typing import AsyncGenerator

from github import Github

from ghs.model.domain.project import Project


class GitHubAPI:

    __clots__ = ("ghh",)

    def __init__(
        self,
    ) -> None:
        self.ghh: Github = Github(login_or_token=os.getenv("GH_AUTH_TOKEN"))

    async def fetch_stars(self) -> AsyncGenerator[dict[str, str], None]:
        """Returns a sett of Project objects"""

        user = await asyncio.get_running_loop().run_in_executor(
            None, self.ghh.get_user  # get the owner of the auth token
        )

        stars = await asyncio.get_running_loop().run_in_executor(None, user.get_starred)
        pages: int = math.ceil(stars.totalCount / 30)  # GitHub pagination count

        for page in range(pages):
            for project in await asyncio.get_event_loop().run_in_executor(
                None, stars.get_page, page
            ):

                p = Project(
                    name=project.name.capitalize(),
                    description=str(project.description),  # Sometimes it's None
                    url=project.html_url,
                    star_count=project.stargazers_count,
                    add_time=datetime.now(),
                    fork_count=project.forks_count,
                ).dict()

                # The URL is now validated, let's turn it into a string
                p["url"] = str(p["url"])

                yield p
