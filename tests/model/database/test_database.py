
import os
from functools import partial

import asyncpg

from ghs.model.database.database import Database

import pytest
pytestmark = pytest.mark.asyncio


@pytest.mark.skipif(os.getenv('CI', '0') != '0', reason="No PostgreSQL DB on GH Actions CI/CD")
class TestDatabase:

    # A fresh connection is made for each test, and thats fine for now
    conn = partial(asyncpg.connect, user="testdb", password="testdb", database="testdb")

    async def test_create(self) -> None:

        dbh = Database(db_handle=await self.conn())

        result = await dbh.create(('INSERT INTO pro_lang(name) VALUES($1)', 'Python'))
        assert result == "INSERT 0 1"

        with pytest.raises(ValueError):
            await dbh.create(('SELECT * FROM pro_lang',))

    async def test_read(self) -> None:

        dbh = Database(db_handle=await self.conn())

        result = await dbh.read("SELECT name from pro_lang")
        assert result[0].get('name') == 'Python'

        with pytest.raises(ValueError):
            await dbh.read("INSERT INTO pro_lang(name) VALUES('Javascript')")

    async def test_update(self) -> None:

        dbh = Database(db_handle=await self.conn())

        result = await dbh.update("UPDATE pro_lang SET name='Rust' WHERE name='Python'")
        assert result == 'UPDATE 1'

        with pytest.raises(ValueError):
            await dbh.update('SELECT name FROM pro_lang')

    async def test_delete(self) -> None:

        dbh = Database(db_handle=await self.conn())

        result = await dbh.delete('DELETE FROM pro_lang')
        assert result == 'DELETE 1'

        with pytest.raises(ValueError):
            await dbh.delete('SELECT name FROM pro_lang')
