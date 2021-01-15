
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse


class HerokuInsomnia(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:
        return PlainTextResponse("I'm up!")
