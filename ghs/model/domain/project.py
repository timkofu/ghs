from datetime import datetime

from pydantic import BaseModel
from pydantic import StrictInt, StrictStr, HttpUrl


class Project(BaseModel):

    """Project entity."""

    id: StrictInt
    name: StrictStr
    description: StrictStr
    url: HttpUrl
    initial_stars: StrictInt
    current_stars: StrictInt
    add_time: datetime
    initial_fork_count: StrictInt
    current_fork_count: StrictInt
