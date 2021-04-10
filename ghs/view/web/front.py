from typing import Any
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.templating import _TemplateResponse

from ghs.controller.stars.front import Pager

from .templates.loader import templates_handle


class Front(HTTPEndpoint):
    async def get(self, request: Request) -> _TemplateResponse:

        pager = Pager()

        rows = [r async for r in pager.page()]
        page_details: dict[str, Any] = {
            "current_page": 1,
            "last_page": 1,
        }

        return templates_handle.TemplateResponse(
            "front.html",
            context={"rows": rows, "page_details": page_details, "request": request},
        )
