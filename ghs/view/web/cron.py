from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse


class FetchStars(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:
        return PlainTextResponse("1")


class UpdateStars(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:
        return PlainTextResponse("1")
