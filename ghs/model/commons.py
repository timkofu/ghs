import os

from ghs.model.database import database

DEBUG = not os.getenv("PRODUCTION")

DATABASE_HANDLE = database.Database()
