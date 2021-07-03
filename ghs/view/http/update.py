import os
from typing import Union

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.background import BackgroundTask
from starlette.responses import PlainTextResponse

from ghs.model.application.update import Update


class UpdateStars(HTTPEndpoint):
    async def get(self, request: Request) -> PlainTextResponse:

        cron_auth_token: Union[str, None] = request.path_params.get("update_auth_token")  # type: ignore

        if cron_auth_token and (cron_auth_token == os.getenv("UPDATE_AUTH_TOKEN")):
            return PlainTextResponse("1", background=BackgroundTask(Update().stars))
        else:
            raise HTTPException(403, detail="Invalid auth token.")
