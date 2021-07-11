"""
SQL Alchemy ORM models.

This will have no tests as it's pure SQLAlchemy, hich is itself tested.
"""

import datetime

from sqlalchemy.orm import declarative_base  # type: ignore
from sqlalchemy import Column, String, Integer, DateTime  # type: ignore


Base = declarative_base()  # type: ignore


class Project(Base):  # type: ignore

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name = Column(String, index=True)  # type: ignore
    description = Column(String)  # type: ignore
    url = Column(String)  # type: ignore
    stars = Column(Integer)  # type: ignore
    forks = Column(Integer)  # type: ignore
    added_on = Column(DateTime, default=datetime.datetime.utcnow)  # type: ignore


class ProgrammingLanguage(Base):  # type: ignore

    __tablename__ = "programming_language"

    id = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name = Column(String, index=True)  # type: ignore
