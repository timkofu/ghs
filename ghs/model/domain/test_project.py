from datetime import datetime

import pytest
from pydantic.error_wrappers import ValidationError

from .project import Project


pytestmark = pytest.mark.asyncio


class TestProject:
    async def test_correct_date(self) -> None:

        assert Project(
            name="name",
            description="this is a test project entity",
            url="http://local.host",
            star_count=1,
            add_time=datetime.now(),
            fork_count=0,
        )

    async def test_incorrect_data(self) -> None:

        with pytest.raises(ValidationError):  # type: ignore
            assert Project(
                name="name",
                description="this is a test project entity",
                url="localhost",
                star_count=1,
                add_time=datetime.now(),
                fork_count=1,
            )
