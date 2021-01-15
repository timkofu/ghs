
from starlette.routing import Route
from starlette.applications import Starlette

from .front import Front
from .cron import FetchStars, UpdateStars
from .heroku_insomnia import HerokuInsomnia

from ghs.controller.commons import DEBUG


app = Starlette(

    debug=DEBUG,

    routes=[

        Route("/", Front),
        Route("/fetch", FetchStars),
        Route("/update", UpdateStars),
        Route("/heroku_insomnia", HerokuInsomnia),

    ]

)
