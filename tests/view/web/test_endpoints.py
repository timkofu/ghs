
from requests.models import Response
from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import pytest
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
