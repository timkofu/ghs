import os

import pytest

if os.getenv("CI"):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from ghs.model.database.database import Database

pytestmark = pytest.mark.asyncio


class TestDatabase:
    async def test_upsert(self) -> None:

        dbh = await Database.get_database_handle(
            conn_creds=dict(user="testdb", password="testdb", database="testdb")
        )

        result = await dbh.upsert(
            ("INSERT INTO pro_lang(name) VALUES($1) RETURNING language_id", "Python")
        )
        assert isinstance(result, int)

        with pytest.raises(ValueError):
            await dbh.upsert(("SELECT * FROM pro_lang",))

    async def test_read(self) -> None:

        dbh = await Database.get_database_handle()

        result = await dbh.read("SELECT name from pro_lang")
        # assert result[0].get("name") == "Python"
        assert isinstance(result, list)

        with pytest.raises(ValueError):
            await dbh.read("INSERT INTO pro_lang(name) VALUES('Javascript')")

    async def test_delete(self) -> None:

        dbh = await Database.get_database_handle()

        result = await dbh.delete(("TRUNCATE pro_lang CASCADE",))
        assert result in ("DELETE 1", "TRUNCATE TABLE")

        # with pytest.raises(ValueError):
        assert await dbh.read("SELECT name FROM pro_lang") == []
