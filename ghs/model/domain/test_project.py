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
            initial_stars=1,
            current_stars=2,
            initial_forks=0,
            current_forks=1,
            programming_language="Python",
            added_on=datetime.utcnow(),
        )

    async def test_incorrect_data(self) -> None:

        with pytest.raises(ValidationError):  # type: ignore
            assert Project(
                name="name",
                description="this is a test project entity",
                url="localhost",
                stars=1,
                forks=1,
                added_on=datetime.utcnow(),
            )
