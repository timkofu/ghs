import logging

from ghs.model.infrastructure.github.github import GitHubAPI
from ghs.model.infrastructure.database.repository.repository import Repository


class Update:
    """Fetch stars and store them in DB"""

    __slots__ = ("ghh", "repository")

    def __init__(
        self,
    ) -> None:
        self.ghh: GitHubAPI = GitHubAPI()
        self.repository: Repository = Repository()

    async def stars(self) -> None:

        logging.getLogger("uvicorn").info("GHS: Starting update ...")

        # current_stars: set[str] = set()  # For use in removing unstared projects

        async for project in self.ghh.fetch_stars():

            # Save the project
            self.repository.domain_object_name = "project"
            await self.repository.add(project)

            # Save a project's main programming language
            self.repository.domain_object_name = "programminglanguage"
            await self.repository.add({"name": project["programming_language"]})

            # Create many-to-many relationship

        # Now we remove unstarred repos

        logging.getLogger("uvicorn").info("GHS: Update completed successfuly ✨")
