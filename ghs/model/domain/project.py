from datetime import datetime

from pydantic import BaseModel
from pydantic import StrictInt, StrictStr, HttpUrl


class Project(BaseModel):

    """Project entity."""

    name: StrictStr
    description: StrictStr
    url: HttpUrl
    star_count: StrictInt
    fork_count: StrictInt
    add_time: datetime

    class Config:
        frozen = True
