import os, sys, csv, pandas
from typing import List, Tuple, Any
from microservice.logging_module.handler import logger


def _get_delimiter(filename: str) -> str:
    """Subfunction to detect delimiter in file (csv)."""
    with open(filename, "r") as freader:
        delimiter = str(csv.Sniffer().sniff(freader.read()).delimiter)
    return delimiter


def _read_csv(filename: str) -> pandas.DataFrame:
    """Subfunction to read a file (csv)."""
    return pandas.read_csv(filename, sep=get_delimiter(filename))


def _read_xlsx(filename: str) -> pandas.DataFrame:
    """Subfunction to read a file (xlsx)."""
    X = pandas.DataFrame([])
    try:
        X = pandas.read_excel(filename)
    except OSError as err:
        logger.error(__file__, f"{err}")
    return X


def reader(filename: str) -> pandas.DataFrame:
    """Function to read a file (csv/xlsx)."""
    filetype = filename.split(".")[-1]
    res = pandas.DataFrame([])
    match filetype:
        case "csv":
            res = _read_csv(filename)
        case "xlsx":
            res = _read_xlsx(filename)
        case _:
            # print(f"\033[0;33m\n[-]Error: Unknown type of file.\033[0m", file=sys.stderr)
            logger.error(f"Error: Unknown type of file.")
            raise Exception(f"Error: Unknown type of file.")
    return res


def _write_csv(filename: str, X: pandas.DataFrame) -> None:
    """Subfunction to write a file (csv)."""
    X.to_csv(filename, index=False)


def _write_xlsx(filename: str, X: pandas.DataFrame) -> None:
    """Subfunction to write a file (xlsx)."""
    X.to_excel(filename, index=False)


def writer(filename: str, X: pandas.DataFrame) -> None:
    """Function to write a file (csv/xlsx)."""
    filetype = filename.split(".")[-1]
    res = pandas.DataFrame([])
    match filetype:
        case "csv":
            res = _write_csv(filename, X)
        case "xlsx":
            res = _write_xlsx(filename, X)
        case _:
            # print(f"\033[0;33m\n[-]Error: Unknown type of file.\033[0m", file=sys.stderr)
            logger.error(f"Error: Unknown type of file.")
            raise Exception(f"\033[0;33m\n[-]Error: Unknown type of file.\033[0m")
    return res


def from_db_to_dataframe(X: List[Tuple[str]], columns: List[str]) -> None:
    """Function to convert list (of tuples) into dataframes (pandas)."""
    return pandas.DataFrame(X, columns=columns)
