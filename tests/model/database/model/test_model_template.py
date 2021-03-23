
import pytest

from ghs.model.database.model import ModelTemplate


pytestmark = pytest.mark.asyncio


class TestModelTemplate:

    async def test_model_template(self) -> None:
        model = ModelTemplate()

        for method in ('create', 'read', 'update', 'delete'):
            with pytest.raises(NotImplementedError):
                await getattr(model, method)()
