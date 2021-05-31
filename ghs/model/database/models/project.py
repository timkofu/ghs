from datetime import datetime

from sqlalchemy import Text, Column, Integer, DateTime

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Project(Base):  # type: ignore
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(Text(255))
    description = Column(Text)
    url = Column(Text())
    initial_stars = Column(Integer)
    current_stars = Column(Integer)
    add_time = Column(DateTime, default=datetime.now)

    def __str__(self) -> Column:
        return self.name
