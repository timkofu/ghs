
import asyncpg
import pytest
from pytest_mock import module_mocker, MockerFixture

from ghs.controller.stars.fetch import Fetch
from ghs.model.database.database import Database

pytestmark = pytest.mark.asyncio


class TestFetch:

    async def test_fetch_stars(self, module_mocker: MockerFixture) -> None:

        ghh = module_mocker.patch('github.Github', autospec=True)("doesitmatter?")
        dbh = await asyncpg.connect(user="testdb", password="testdb", database="testdb")
        fetch = Fetch(ghh=ghh, dbh=Database(db_handle=dbh))

        assert await fetch.stars() is None
