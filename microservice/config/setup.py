"""Module to manage paths and environment variables."""

import os

MAIN_DIR = os.getenv("ROOT_DIR", os.getcwd())
DATABASE = os.getenv("DATABASE", os.path.join(MAIN_DIR,"helpers","mock.db"))
FILEPATH = os.getenv("FILEPATH", os.path.join(MAIN_DIR,"helpers","mock.xlsx"))
TABLE = os.getenv("TABLE", "project")
