import pytest
from pydantic.error_wrappers import ValidationError

from .programming_language import ProgrammingLanguage


pytestmark = pytest.mark.asyncio


class TestProgrammingLanguage:
    async def test_correct_date(self) -> None:

        assert ProgrammingLanguage(name="name")

    async def test_incorrect_data(self) -> None:

        with pytest.raises(ValidationError):  # type: ignore
            assert ProgrammingLanguage(name=1)

    async def test_extra_data_forbidden(self) -> None:

        with pytest.raises(ValidationError):  # type: ignore
            assert ProgrammingLanguage(name=1, country="country")
