
import os
import re

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.responses import PlainTextResponse

from ghs.controller.stars.fetch import Fetch


class FetchStars(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:

        if request.path_params['cron_auth_token'] == os.getenv('CRON_AUTH_TOKEN'):
            await Fetch().stars()
            return PlainTextResponse("1")
        else:
            raise HTTPException(403, detail='Invalid auth token.')


class UpdateStars(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:
        return PlainTextResponse("1")
