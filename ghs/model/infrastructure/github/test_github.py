import pytest

# from ghs.model.infrastructure.github.github import GitHubAPI

pytestmark = pytest.mark.asyncio


class TestGitHubAPI:
    async def test_fetch_stars(self) -> None:
        """Tightly coupled to the infrastructure

        No tests for now (As I will not use mock. I will not.)
        Tests should work even when the infrastructure is unavailable (no network connectivity).
        """

        ...
