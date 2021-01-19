
import os
from functools import partial

import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

import asyncpg
from pytest_mock import module_mocker, MockerFixture

from ghs.controller.stars.fetch import Fetch
from ghs.model.database.database import Database

pytestmark = pytest.mark.asyncio


class TestFetch:

    async def test_fetch_stars(self, module_mocker: MockerFixture) -> None:

        ghh = module_mocker.patch('github.Github', autospec=True)("doesitmatter?")
        dbh = Database()
        await dbh.init_db(partial(
            asyncpg.connect, user="testdb", password="testdb", database="testdb"
        ))
        fetch = Fetch(ghh=ghh, dbh=dbh)

        assert await fetch.stars() is None
