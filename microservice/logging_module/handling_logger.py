import logging


class Logger:
    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)
        self.set_stream_handler()

        self.DEBUG = "%(asctime)s | \033[0;34m %(levelname)s \033[0m | %(message)s"
        self.INFO = "%(asctime)s | \033[0;32m %(levelname)s \033[0m  | %(message)s"
        self.WARNING = "%(asctime)s | \033[0;33m %(levelname)s \033[0m | %(message)s"
        self.ERROR = "%(asctime)s | \033[0;31m %(levelname)s \033[0m | %(message)s"
        self.CRITICAL = "%(asctime)s | \033[0;35m %(levelname)s \033[0m | %(message)s"
        # self.CRITICAL = "%(asctime)s | \033[0;35m %(levelname)s \033[0m | %(filename)s:%(lineno)s | %(message)s"

        self.DATE = "%Y-%m-%d %H:%M:%S"

    def set_level(self, level: int) -> None:
        self.logger.setLevel(level)

    def set_stream_handler(
        self,
    ) -> None:
        self.handler = logging.StreamHandler()
        self.logger.addHandler(self.handler)

    def set_file_handler(self, filename) -> None:
        self.handler = logging.FileHandler(filename, mode="w", encoding="utf-8")
        self.logger.addHandler(self.handler)

    def debug(self, msg: str) -> None:
        form = logging.Formatter(self.DEBUG, datefmt=self.DATE)
        self.handler.setFormatter(form)
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        form = logging.Formatter(self.INFO, datefmt=self.DATE)
        self.handler.setFormatter(form)
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        form = logging.Formatter(self.WARNING, datefmt=self.DATE)
        self.handler.setFormatter(form)
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        form = logging.Formatter(self.ERROR, datefmt=self.DATE)
        self.handler.setFormatter(form)
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        form = logging.Formatter(self.CRITICAL, datefmt=self.DATE)
        self.handler.setFormatter(form)
        self.logger.critical(msg)
