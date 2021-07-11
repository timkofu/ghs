import pytest
from pydantic.error_wrappers import ValidationError

from .programming_language import ProgrammingLanguage

pytestmark = pytest.mark.asyncio


class TestProgrammingLanguage:
    async def test_not_string(self):
        with pytest.raises(ValidationError):  # type:ignore
            assert ProgrammingLanguage(name=1)

    async def test_is_string(self):
        assert ProgrammingLanguage(name="Python")
