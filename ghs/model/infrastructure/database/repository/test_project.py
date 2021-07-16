from datetime import datetime

import pytest
from pydantic.error_wrappers import ValidationError

from ghs.model.infrastructure.database.repository.project import Project


pytestmark = pytest.mark.asyncio


class TestProject:

    proj = Project()

    async def test_add_with_correct_params(self) -> None:
        assert await self.proj.add(
            domain_object={
                "name": "name",
                "description": "this is a test project entity",
                "url": "http://local.host",
                "initial_stars": 1,
                "current_stars": 2,
                "initial_forks": 0,
                "current_forks": 1,
                "programming_language": "Python",
                "added_on": datetime.utcnow(),
            }
        )

    async def test_add_with_incorrect_params(self) -> None:
        with pytest.raises(ValidationError):  # type: ignore
            assert await self.proj.add(
                domain_object={
                    "name": "name",
                    "description": "this is a test project entity",
                    "url": "http://local.host",
                    "initial_stars": "one",
                    "current_stars": 2,
                    "initial_forks": 0,
                    "current_forks": 1,
                    "programming_language": "Python",
                    "added_on": datetime.utcnow(),
                }
            )

    async def test_get_with_correct_params(self) -> None:
        assert [i async for i in self.proj.get({"name": "Python"})] == []

    async def test_get_with_incorrect_params(self) -> None:
        with pytest.raises(ValueError):  # type:ignore
            assert [i async for i in self.proj.get({"faith": "Christian"})]
