
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.responses import HTMLResponse

from .templates.loader import templates_handle


class Front(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> HTMLResponse:
        return templates_handle.TemplateResponse(
            'front.html',
            context={'request': request}
        )
