"""
SQL Alchemy ORM models.

This will have no tests as it's pure SQLAlchemy, hich is itself tested.
"""

from sqlalchemy.orm import declarative_base  # type: ignore
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()  # type: ignore


class Project(Base):  # type: ignore

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
