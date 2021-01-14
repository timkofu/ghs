
import os

from starlette.templating import Jinja2Templates


path = os.path.dirname(os.path.realpath(__file__))
templates_handle = Jinja2Templates(directory=path)
