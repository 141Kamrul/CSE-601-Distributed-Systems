from sqlalchemy import create_engine
from os import getenv


class session:
    database_url=getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL is not set in the environment variables.")

    engine=create_engine(database_url,echo=True)
    