from os import getenv

from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(getenv("DATABASE_URL"))
