import os

from legacy_ghs.model.database import database

DEBUG = not os.getenv("PRODUCTION")

DATABASE_HANDLE = database.Database()
