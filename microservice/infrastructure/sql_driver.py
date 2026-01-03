"""Module to manage sql."""

import os, sqlite3, hashlib
from typing import List, Tuple, Optional, Any
from microservice.config.setup import *
from microservice.logging_module.handler import logger

HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()


def get_columns_name(database: str, table: str) -> List[str]:
    """Function to get columns name (from table)."""
    columns = []
    try:
        db = sqlite3.connect(database)
        cursor = db.execute(f"""SELECT * FROM {table};""")
        columns = list(map(lambda x: x[0], cursor.description))
        db.close()
    except Exception as err:
        logger.error(f"Error sql get columns name: {err}")
    return columns


def request(database: str, value: str) -> List[Tuple[Any]]:
    """Function to execute a query (SQL)."""
    x = []
    try:
        db = sqlite3.connect(database)
        cursor = db.cursor()
        rows = cursor.execute(value)
        x = list(rows)
        db.commit()
        db.close()
    except Exception as err:
        logger.error(f"Error sql request: {err}")
    return x
