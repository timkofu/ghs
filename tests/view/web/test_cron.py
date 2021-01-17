
import os

from starlette.testclient import TestClient

from ghs.view.web.endpoints import app

import pytest
import nest_asyncio
from pytest_mock import module_mocker, MockerFixture

nest_asyncio.apply()
pytestmark = pytest.mark.asyncio


class TestCron:

    client: TestClient = TestClient(app)

    async def test_fetch(self) -> None:

        response = self.client.get("/fetch/test")
        assert response.status_code == 403

    async def test_update(self) -> None:

        response = self.client.get("/update/test")
        assert response.status_code == 200
