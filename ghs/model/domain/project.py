from datetime import datetime

from pydantic import StrictInt, StrictStr, HttpUrl
from pydantic import BaseModel


class Project(BaseModel):

    """Project entity."""

    name: StrictStr
    description: StrictStr
    url: HttpUrl
    stars: StrictInt
    forks: StrictInt
    added_on: datetime

    class Config:
        frozen = True
        extra = "forbid"
