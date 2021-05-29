
from _pytest.outcomes import importorskip


import os
import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)

from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import nest_asyncio

nest_asyncio.apply()
pytestmark = pytest.mark.asyncio


class TestEndPoints:

    client: TestClient = TestClient(app)

    async def test_front(self) -> None:

        response = self.client.get("/")
        assert response.status_code == 200

    async def test_heroku_insomnia(self) -> None:

        response = self.client.get('/heroku_insomnia')
        assert response.text == "I'm up!"

    async def test_update(self) -> None:

        response = self.client.get("/update/test")
        assert response.status_code == 403
