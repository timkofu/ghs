
from starlette.routing import Route
from starlette.applications import Starlette

from .front import Front
from .cron import FetchStars, UpdateStars

from ghs.controller.commons import DEBUG


app = Starlette(

    debug=DEBUG,

    routes=[

        Route("/", Front),
        Route("/fetch", FetchStars),
        Route("/update", UpdateStars),

    ]

)
