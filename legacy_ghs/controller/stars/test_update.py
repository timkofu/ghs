import os

import pytest

if os.getenv("CI"):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from pytest_mock import MockerFixture
from legacy_ghs.controller.stars.update import Update

pytestmark = pytest.mark.asyncio


class TestUpdate:
    async def test_fetch_stars(self, module_mocker: MockerFixture) -> None:

        ghh = module_mocker.patch("github.Github", autospec=True)("doesitmatter?")
        fetch = Update(
            ghh=ghh,
            conn_creds=dict(user="testdb", password="testdb", database="testdb"),
        )

        assert await fetch.stars() is None
