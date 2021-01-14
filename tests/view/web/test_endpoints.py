
from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import pytest
import nest_asyncio

nest_asyncio.apply()
pytestmark = pytest.mark.asyncio


class TestEndPoints:

    async def test_front(self) -> None:

        client: TestClient = TestClient(app)

        response = client.get("/")
        assert response.status_code == 200
