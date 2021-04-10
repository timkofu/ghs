from math import ceil
from typing import Any, Union
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.templating import _TemplateResponse

from ghs.controller.stars.front import Pager

from .templates.loader import templates_handle


class Front(HTTPEndpoint):
    async def get(self, request: Request) -> _TemplateResponse:

        wanted_page: Union[int, None] = request.path_params.get("wanted_page")

        pager = Pager()

        rows = [r async for r in pager.page()]

        # Now we can check if page number is too (large or small) as total_pages is now calculated
        # if wanted_page < 1 and wanted_page > pager.total_pages:
        #     raise HTTPException(404)
        # to be continued

        page_details: dict[str, Any] = {
            "current_page": ceil(
                pager.offset / pager.limit
            ),  # offset is already +20 by the time it's read here
            "last_page": pager.total_pages,
        }

        return templates_handle.TemplateResponse(
            "front.html",
            context={"rows": rows, "page_details": page_details, "request": request},
        )
