
from ghs.model.commons import DEBUG

import pytest
pytestmark = pytest.mark.asyncio


async def test_is_debug() -> None:
    assert DEBUG is True
