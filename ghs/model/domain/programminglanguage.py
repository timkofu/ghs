from pydantic import BaseModel, StrictStr


class Programminglanguage(BaseModel):
    name: StrictStr

    class Config:
        frozen = True
        extra = "forbid"
