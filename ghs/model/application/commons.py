import os

from ghs.model.infrastructure.database.legacy_repo import Repository

DEBUG = not os.getenv("PRODUCTION")

REPOSITORY_HANDLE = Repository()
