
from starlette.routing import Route
from starlette.applications import Starlette

from .front import Front

from ghs.controller.commons import DEBUG


app = Starlette(

    debug=DEBUG,

    routes=[

        Route("/", Front),

    ]

)
