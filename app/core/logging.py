import csv
import json
import logging
from io import StringIO

# from dotenv import load_dotenv
from app.core.config import settings

# load_dotenv()


# Custom logging formatters
class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


class CSVFormatter(logging.Formatter):
    def _init_(self, fmt: str | None = None, datefmt: str | None = None) -> None:
        super()._init_(fmt, datefmt)
        self.output = StringIO()
        self.writer = csv.writer(self.output)

    def format(self, record: logging.LogRecord) -> str:
        self.output.seek(0)
        self.output.truncate(0)
        self.writer.writerow(
            [
                self.formatTime(record, self.datefmt),
                record.levelname,
                record.getMessage(),
            ]
        )
        return self.output.getvalue().strip()


# LOG_FILE = os.getenv("LOG_FILE", "/var/log/app.log")
# LOG_FORMAT = os.getenv("LOG_FORMAT", "json")


def get_logger(name: str) -> None:
    logger = logging.getLogger(name)
    logger.setLevel(settings.log.level.upper())
    # settings.LOG_LEVEL
    # "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # if settings.log.format == "json":
    #     from pythonjsonlogger import jsonlogger

    #     formatter = jsonlogger.JSONFormatter()
    # elif settings.log.format == "csv":
    #     formatter = logging.Formatter(
    #         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    #     )
    # else:
    #     None

    file_handler = logging.FileHandler(settings.log.file)
    file_handler.setLevel(settings.log.level.upper())
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.debug("debug message (will go to file)")
    logger.info("info message (will go to file)")
    logger.warning("warning message (will go to file)")
    logger.error("Error message (will go to file)")

    return logger

    # logging.basicConfig(
    #     filename=LOG_FILE,
    #     level=logging.INFO,
    #     format=JSONFormatter(),
    #     handlers=[logging.StreamHandler()],
    # )
