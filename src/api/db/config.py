"""Database configuration module.

This module handles the retrieval of database configuration settings.
"""

from decouple import config as decouple_config

DATABASE_URL = decouple_config("DATABASE_URL", default="")
