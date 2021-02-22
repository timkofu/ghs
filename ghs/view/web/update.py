
import os

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.background import BackgroundTask
from starlette.responses import PlainTextResponse

from ghs.controller.stars.update import Update


class UpdateStars(HTTPEndpoint):

    async def get(self, request: Request) -> PlainTextResponse:

        cron_auth_token: str = str(request.path_params.get('update_auth_token'))

        if cron_auth_token and (cron_auth_token == os.getenv('UPDATE_AUTH_TOKEN')):
            return PlainTextResponse("1", background=BackgroundTask(Update().stars))
        else:
            raise HTTPException(403, detail='Invalid auth token.')
