from pydantic import BaseModel, StrictStr


class ProgrammingLanguage(BaseModel):
    name: StrictStr

    class Config:
        frozen = True
        extra = "forbid"
