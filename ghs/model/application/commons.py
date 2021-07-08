import os

from ghs.model.infrastructure.repository.repository import Repository

DEBUG = not os.getenv("PRODUCTION")

REPOSITORY_HANDLE = Repository()
