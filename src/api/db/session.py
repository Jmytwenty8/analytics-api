"""Current module initializes the database session and engine.

It provides the `init_db` function to create all database tables
using the SQLModel metadata and the configured database engine.
"""

import sqlmodel
from sqlmodel import SQLModel

from api.db.config import DATABASE_URL

if DATABASE_URL == "":
    error_message = "DATABASE_URL is not set"
    raise NotImplementedError(error_message)

engine = sqlmodel.create_engine(str(DATABASE_URL))


def init_db() -> None:
    """Initialize the database by creating all tables.

    This function uses the SQLModel metadata and the configured
    database engine to create all database tables.
    """
    SQLModel.metadata.create_all(engine)
