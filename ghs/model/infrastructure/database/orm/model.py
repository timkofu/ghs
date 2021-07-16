"""
SQL Alchemy ORM models.

This will have no tests as it's pure SQLAlchemy, hich is itself tested.
"""

import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey  # type: ignore
from sqlalchemy.orm import backref, declarative_base, relationship  # type: ignore


Base = declarative_base()  # type: ignore


class ProgrammingLanguage(Base):  # type: ignore

    __tablename__ = "programming_language"

    id = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name = Column(String, index=True, unique=True)  # type: ignore
    projects = relationship(  # type:ignore
        "Project", back_populates="programming_language"
    )  # type:ignore


class Project(Base):  # type: ignore

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name = Column(String, index=True, unique=True, nullable=False)  # type: ignore
    description = Column(String)  # type: ignore
    url = Column(String, unique=True, nullable=False)  # type: ignore
    initial_stars = Column(Integer)  # type: ignore
    current_stars = Column(Integer, index=True)  # type: ignore
    initial_forks = Column(Integer)  # type: ignore
    current_forks = Column(Integer)  # type: ignore
    programming_language_id = Column(  # type: ignore
        Integer, ForeignKey("programming_language.id")
    )  # type:ignore
    added_on = Column(DateTime, default=datetime.datetime.utcnow)  # type: ignore
    programming_language = relationship("ProgrammingLanguage", back_populates="projects")  # type: ignore
