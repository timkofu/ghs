from starlette.routing import Route
from starlette.applications import Starlette

from .front import Front
from .update import UpdateStars
from .heroku_insomnia import HerokuInsomnia

from ghs.controller.commons import DEBUG


app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/", Front),
        Route("/heroku_insomnia", HerokuInsomnia),
        Route("/update/{update_auth_token:str}", UpdateStars),
        Route("/page/{wanted_page:int}", Front),
    ],
)
