from typing import Any, cast

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint

from ghs.model.application.front import Pager

from .templates.loader import templates_handle


class Front(HTTPEndpoint):
    async def get(self, request: Request) -> object:

        pager = Pager({})

        rows: Any = [r async for r in cast(Any, pager.page())]

        return templates_handle.TemplateResponse(  # type: ignore
            name="front.html",
            context={"rows": rows, "request": request},
        )
