from typing import Any, cast

import pytest


from ghs.model.application.front import Pager

pytestmark = pytest.mark.asyncio


class _FakeRepository:
    async def page(self) -> dict[str, Any]:
        return {"some": "thing"}


class TestFront:
    async def test_front(self) -> None:

        p = Pager()
        # duck_typing ;)
        p.repository = _FakeRepository()  # type:ignore

        assert Pager()
