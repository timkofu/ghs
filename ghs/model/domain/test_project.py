from datetime import datetime

import pytest
from pydantic.error_wrappers import ValidationError

from .project import Project


pytestmark = pytest.mark.asyncio


class TestProject:
    async def test_correct_date(self) -> None:

        assert Project(
            id=1,
            name="name",
            description="this is a test project entity",
            url="http://local.host",
            initial_stars=1,
            current_stars=2,
            add_time=datetime.now(),
            initial_fork_count=0,
            current_fork_count=1,
        )

    async def test_incorrect_data(self) -> None:

        with pytest.raises(ValidationError):  # type: ignore
            assert Project(
                id=1,
                name="name",
                description="this is a test project entity",
                url="localhost",
                initial_stars=1,
                current_stars=2,
                add_time=datetime.now(),
                initial_fork_count=0,
                current_fork_count=1,
            )
