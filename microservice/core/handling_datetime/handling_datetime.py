"""Module to check datetime."""

import os, sys, time, pathlib
from microservice.config.setup import *
from microservice.logging_module.handler import logger


def check_datetime_files() -> bool:
    """Function to ..."""

    if os.path.exists(FILEPATH):
        last_modif_db = os.path.getmtime(DATABASE)
        last_create_db = os.path.getctime(DATABASE)
        last_modif_file = os.path.getmtime(FILEPATH)


        last_create_file = os.path.getctime(FILEPATH)

        # print(f"\n\tlast_modif_db: {time.ctime(last_modif_db)}, last_create_db: {time.ctime(last_create_db)}")
        # print(f"\n\tlast_modif_file: {time.ctime(last_modif_file)}, last_create_file: {time.ctime(last_create_file)}")
        # print(f"\n\tTest if up: {last_create_file < last_modif_db}, {last_modif_file < last_modif_file}")

        if not (last_create_file < last_modif_db or last_modif_file < last_modif_db):
            logger.warning(f"File {DATABASE} has not been updated.")
            return False
    return True
