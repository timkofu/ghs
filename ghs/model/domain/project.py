from datetime import datetime

from pydantic import StrictInt, StrictStr, HttpUrl
from pydantic import BaseModel


class Project(BaseModel):

    """Project entity."""

    name: StrictStr
    description: StrictStr
    url: HttpUrl
    initial_stars: StrictInt
    current_stars: StrictInt
    initial_forks: StrictInt
    current_forks: StrictInt
    programming_language: StrictStr
    added_on: datetime

    class Config:
        frozen = True
        extra = "forbid"
