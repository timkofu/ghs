from starlette.routing import Route
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware

from .front import Front
from .update import UpdateStars

from ghs.model.commons import DEBUG


app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/", Front),
        Route("/update/{update_auth_token:str}", UpdateStars),
        Route("/page/{wanted_page:int}", Front),
    ],
    middleware=[Middleware(GZipMiddleware, minimum_size=512)],
)
