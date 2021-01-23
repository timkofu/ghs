
from starlette.routing import Route
from starlette.applications import Starlette

from .front import Front
from .cron import UpdateStars
from .heroku_insomnia import HerokuInsomnia

from ghs.controller.commons import DEBUG


app = Starlette(

    debug=DEBUG,

    routes=[

        Route("/", Front),
        Route("/update", UpdateStars),
        Route("/heroku_insomnia", HerokuInsomnia),
        Route("/update/{cron_auth_token}", UpdateStars),

    ]

)
