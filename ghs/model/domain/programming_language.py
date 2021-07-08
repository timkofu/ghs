from pydantic import StrictStr
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class ProgrammingLanguage:
    language: StrictStr
