"""Interface between global variables and main functions."""

from microservice.config.setup import MAIN_DIR, DATABASE, FILEPATH, TABLE
from microservice.config.constants import ARGS

print(f"SETUP: \n\t{MAIN_DIR} \n\t{DATABASE} \n\t{FILEPATH} \n\t{TABLE}")
print(f"CONSTANTS: {ARGS}")
