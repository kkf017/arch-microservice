import os 

DATABASE = os.getenv('DATABASE', "./files/db_test.db")
OUTPUT = os.getenv('FILEPATH', "./files/db_test.xlsx")
TABLE = os.getenv('TABLE', "project")