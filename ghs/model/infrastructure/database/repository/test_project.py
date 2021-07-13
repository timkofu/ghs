import pytest

from ghs.model.infrastructure.database.repository.project import Project


pytestmark = pytest.mark.asyncio


class TestProject:
    async def test_get_with_correct_params(self) -> None:
        ...

    async def test_get_with_incorrect_params(self) -> None:
        ...

    async def test_add_with_correct_params(self) -> None:
        ...

    async def test_add_with_incorrect_params(self) -> None:
        ...
