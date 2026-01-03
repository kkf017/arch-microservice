"""Interface between main.py and core/."""

from typing import List
from datetime import datetime
from microservice.logging_module.handler import logger
import microservice.core.handling_functions


def run() -> None:
    """Main function to run service."""
    start_time = datetime.now()

    microservice.core.handling_functions.function()

    end_time = datetime.now()
    logger.info(f"Execution Time: {end_time - start_time}s.")
