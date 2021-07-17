from datetime import datetime

import pytest
from pydantic.error_wrappers import ValidationError

from ghs.model.infrastructure.database.repository.repository import Repository


pytestmark = pytest.mark.asyncio


class TestRepository:

    repo = Repository()

    # ## PROJECT ## #
    async def test_project_add_with_correct_params(self) -> None:
        self.repo.domain_object_name = "Project"
        assert await self.repo.add(
            object_details={
                "name": "name",
                "description": "this is a test project entity",
                "url": "http://local.host",
                "initial_stars": 1,
                "current_stars": 2,
                "initial_forks": 0,
                "current_forks": 1,
                "programming_language": "Python",
                "added_on": datetime.utcnow(),
            },
        )

    async def test_project_add_with_incorrect_params(self) -> None:
        with pytest.raises(ValidationError):  # type: ignore
            assert await self.repo.add(
                object_details={
                    "name": "name",
                    "description": "this is a test project entity",
                    "url": "http://local.host",
                    "initial_stars": "one",
                    "current_stars": 2,
                    "initial_forks": 0,
                    "current_forks": 1,
                    "programming_language": "Python",
                    "added_on": datetime.utcnow(),
                },
            )

    async def test_project_get_with_correct_params(self) -> None:
        assert [i async for i in self.repo.get({"name": "Python"})] == []

    async def test_project_get_with_incorrect_params(self) -> None:
        with pytest.raises(ValueError):  # type:ignore
            assert [i async for i in self.repo.get({"faith": "Christian"})]

    # ## PROGRAMMING LANGUAGE ## #
    async def test_programming_language_add_with_correct_params(self) -> None:
        self.repo.domain_object_name = "Programminglanguage"
        assert await self.repo.add(
            object_details={"name": "name"},
        )

    async def test_programming_language_project_add_with_incorrect_params(self) -> None:
        with pytest.raises(ValidationError):  # type: ignore
            assert await self.repo.add(
                object_details={"panet": "Earth"},
            )

    async def test_programming_language_project_get_with_correct_params(self) -> None:
        assert [i async for i in self.repo.get({"name": "Python"})] == []

    async def test_programming_language_project_get_with_incorrect_params(self) -> None:
        with pytest.raises(ValueError):  # type:ignore
            assert [i async for i in self.repo.get({"faith": "Christian"})]
