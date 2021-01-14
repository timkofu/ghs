
from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import pytest
import nest_asyncio

nest_asyncio.apply()
pytestmark = pytest.mark.asyncio


class TestCron:

    client: TestClient = TestClient(app)

    async def test_fetch(self) -> None:

        response = self.client.get('/fetch')
        assert response.status_code == 200

    async def test_update(self) -> None:

        response = self.client.get('/update')
        assert response.status_code == 200
