
import os

import pytest
if os.getenv('CI'):
    pytest.skip("No PostgreSQL on GH Actions CI/CD", allow_module_level=True)


# from functools import partial

# import asyncpg

from ghs.model.database.model.project import Project

pytestmark = pytest.mark.asyncio


class TestProject:

    async def test_project(self) -> None:

        project = Project()

        for method in ('create', 'read', 'update', 'delete'):
            with pytest.raises(NotImplementedError):
                await getattr(project, method)()
