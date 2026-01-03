import os

DATABASE = os.getenv("DATABASE", "/data/arch-microservice/files/db_test.db")
FILEPATH = os.getenv("FILEPATH", "/data/arch-microservice/files/db_test.xlsx")
TABLE = os.getenv("TABLE", "project")
