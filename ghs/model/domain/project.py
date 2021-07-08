from datetime import datetime

from pydantic import StrictInt, StrictStr, HttpUrl
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Project:

    """Project entity."""

    name: StrictStr
    description: StrictStr
    url: HttpUrl
    star_count: StrictInt
    fork_count: StrictInt
    add_time: datetime
