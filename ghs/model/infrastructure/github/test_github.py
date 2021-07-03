import pytest

from ghs.model.infrastructure.github.github import GitHub

pytestmark = pytest.mark.asyncio


async def test_github_api() -> None:
    assert GitHub()
