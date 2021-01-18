
import os

import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from pytest_mock.plugin import MockerFixture
from ghs.controller.stars.update import Update
from ghs.controller.stars.fetch import Fetch

from pytest_mock import mocker, MockerFixture

pytestmark = pytest.mark.asyncio


class TestUpdate:

    async def test_update(self, mocker: MockerFixture) -> None:
        fetcher = mocker.patch("ghs.controller.stars.fetch.Fetch")
        fetcher._fetch_stars.return_value = [mocker.patch("github.Repository.Repository", autospec=True)]
        assert Update(fetcher=fetcher)
