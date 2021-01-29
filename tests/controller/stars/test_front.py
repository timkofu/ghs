
import os
from functools import partial

import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

import asyncpg

from ghs.controller.stars.front import Pager
from ghs.model.database.database import Database

pytestmark = pytest.mark.asyncio


class TestFront:

    async def test_front(self) -> None:

        dbh = Database()
        await dbh.init_db(partial(
            asyncpg.connect, user="testdb", password="testdb", database="testdb"
        ))

        assert Pager(dbh=dbh)
