import os

import pytest

if os.getenv("CI"):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)


from legacy_ghs.controller.stars.front import Pager

pytestmark = pytest.mark.asyncio


class TestFront:
    async def test_front(self) -> None:

        assert Pager(
            conn_creds=dict(user="testdb", password="testdb", database="testdb")
        )
