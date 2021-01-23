
import os
import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import nest_asyncio

nest_asyncio.apply()
pytestmark = pytest.mark.asyncio


class TestCron:

    client: TestClient = TestClient(app)

    async def test_update(self) -> None:

        response = self.client.get("/update/test")
        assert response.status_code == 403
