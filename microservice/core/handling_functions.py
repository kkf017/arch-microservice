"""Module to manage main function (calls)."""

from microservice.config.setup import FILEPATH,DATABASE, TABLE
from microservice.logging_module.handler import logger
import microservice.infrastructure.sql_driver
import microservice.infrastructure.csv_driver
import microservice.core.handling_datetime.handling_datetime

def function() -> None:
    """
    Function to execute main code.
    """
    if not microservice.core.handling_datetime.handling_datetime.check_datetime_files():
        logger.info("No file created.")
        return
    try:
        columns = microservice.infrastructure.sql_driver.get_columns_name(
            DATABASE, TABLE
        )
        x = microservice.infrastructure.sql_driver.request(
            DATABASE, f"""SELECT * FROM {TABLE};"""
        )
        x = microservice.infrastructure.csv_driver.from_db_to_dataframe(x, columns)
        microservice.infrastructure.csv_driver.writer(FILEPATH, x)
        logger.info("File created successfully.")
    except Exception as err:
        logger.error(f"{err}")
