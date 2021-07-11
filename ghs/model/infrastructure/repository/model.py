"""
SQL Alchemy ORM models.

This will have no tests as it's pure SQLAlchemy, hich is itself tested.
"""

import datetime

from sqlalchemy.orm import declarative_base  # type: ignore
from sqlalchemy import Column, String, Integer, DateTime


Base = declarative_base()  # type: ignore


class Project(Base):  # type: ignore

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    url = Column(String)
    stars = Column(Integer)
    forks = Column(Integer)
    added_on = Column(DateTime, default=datetime.datetime.utcnow)


class ProgrammingLanguage(Base):  # type: ignore

    __tablename__ = "programming_language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
