import os

from ghs.model.infrastructure.database.database import Database

DEBUG = not os.getenv("PRODUCTION")

DATABASE_HANDLE = Database()
