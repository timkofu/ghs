import pytest
from pydantic.error_wrappers import ValidationError

from ghs.model.infrastructure.database.repository.programming_language import (
    ProgrammingLanguage,
)


pytestmark = pytest.mark.asyncio


class TestProgramingLanguage:

    pl = ProgrammingLanguage()

    async def test_add_with_correct_params(self) -> None:
        assert await self.pl.add(domain_object={"name": "Python"})

    async def test_add_with_incorrect_params(self) -> None:
        with pytest.raises(ValidationError):  # type: ignore
            assert await self.pl.add(domain_object={"country": "heaven"})

    async def test_get_with_correct_params(self) -> None:
        assert await self.pl.get(filter={"name": "Python"})

    async def test_get_with_incorrect_params(self) -> None:
        with pytest.raises(ValidationError):  # type: ignore
            assert await self.pl.get(filter={"country": "heaven"})
