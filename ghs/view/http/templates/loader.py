from pathlib import Path

from starlette.templating import Jinja2Templates


templates_handle: Jinja2Templates = Jinja2Templates(
    directory=Path(__file__).resolve().parent.as_posix()
)
