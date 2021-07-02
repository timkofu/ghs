from typing import cast

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint

from ghs.model.application.front import Pager

from .templates.loader import templates_handle


class Front(HTTPEndpoint):
    async def get(self, request: Request) -> object:

        pager = Pager()

        rows = [r async for r in pager.page()]

        return templates_handle.TemplateResponse(
            "front.html",
            context={"rows": rows, "request": request},
        )
