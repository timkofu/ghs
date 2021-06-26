import os

import pytest

if os.getenv("CI"):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from asyncpg.connection import Connection

from legacy_ghs.model.database.database import Database

pytestmark = pytest.mark.asyncio


class TestDatabase:
    async def get_dbh(self) -> Connection:
        return await Database.get_database_handle(
            conn_creds=dict(user="testdb", password="testdb", database="testdb")
        )

    async def test_upsert(self) -> None:

        dbh = await self.get_dbh()

        result = await dbh.upsert(
            ("INSERT INTO pro_lang(name) VALUES($1) RETURNING language_id", "Python")
        )
        assert isinstance(result, int)

        # Test that the method only takes INSERT commands
        with pytest.raises(ValueError):
            await dbh.upsert(("SELECT * FROM pro_lang",))

    async def test_read(self) -> None:

        dbh = await self.get_dbh()

        result = await dbh.read("SELECT name from pro_lang")
        assert result[0].get("name") == "Python"
        # assert isinstance(result, list)

        with pytest.raises(ValueError):
            await dbh.read("INSERT INTO pro_lang(name) VALUES('Javascript')")

    async def test_delete(self) -> None:
        dbh = await self.get_dbh()

        result = await dbh.delete(("DELETE FROM pro_lang WHERE name = 'Python'",))
        assert result == "DELETE 1"

        assert await dbh.read("SELECT name FROM pro_lang") == []

        # Delete everything
        result = await dbh.delete(("TRUNCATE pro_lang CASCADE",))
        assert result == "TRUNCATE TABLE"
