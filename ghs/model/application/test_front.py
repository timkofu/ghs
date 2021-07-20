from typing import Any, AsyncGenerator

import pytest


from ghs.model.application.front import Front

pytestmark = pytest.mark.asyncio


class _FakeRepository:
    async def get(self, filter: dict[str, Any]) -> AsyncGenerator[dict[str, Any], None]:
        yield {"some": "thing"}


class TestFront:
    async def test_front(self) -> None:

        # duck_typing ;)
        f = Front(_FakeRepository())  # type:ignore

        async for p in f.page():
            assert isinstance(p, dict)
