from datetime import datetime

import pytest
from typing import Any, AsyncGenerator

from ghs.model.domain.project import Project
from ghs.model.application.update import Update

pytestmark = pytest.mark.asyncio


class _FakeGitHub:
    async def fetch_stars(self) -> AsyncGenerator[dict[str, str], None]:
        project = Project(
            name="project",
            description="project",  # Sometimes it's None
            url="https://local.host",
            initial_stars=1,
            current_stars=2,
            initial_forks=1,
            current_forks=2,
            programming_language="Python",
            added_on=datetime.now(),
        ).dict()

        # The URL is now validated, let's turn it into a string
        project["url"] = str(project["url"])

        yield project


class _FakeRepository:
    async def get(self, filter: dict[str, str]) -> dict[str, Any]:
        return {"some": "thing"}

    async def add(self, object_details: dict[str, Any]) -> dict[str, str]:
        return {"another": "thing"}


class TestUpdate:
    async def test_fetch_stars(self) -> None:

        fetch = Update()
        # duck_typing :)
        fetch.ghh = _FakeGitHub()  # type:ignore
        fetch.repository = _FakeRepository()  # type:ignore

        assert await fetch.stars() is None
