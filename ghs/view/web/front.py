
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.responses import HTMLResponse

from ghs.controller.stars.front import Pager

from .templates.loader import templates_handle


class Front(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> HTMLResponse:

        pager = Pager()

        rows = [r async for r in pager.page()]

        return templates_handle.TemplateResponse(
            'front.html',
            context={
                'rows': rows,
                'request': request
            }
        )
