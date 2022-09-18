from rich.logging import RichHandler
from rich import traceback

import logging


def logging_settings() -> logging.Logger:
    """Enables generic logging settings with rich."""
    log_format = logging.Formatter("%(funcName)s() %(message)s")

    logger = logging.getLogger("command_runner")
    logger.setLevel(logging.INFO)

    stream_handler = RichHandler()
    stream_handler.setFormatter(log_format)

    logger.addHandler(stream_handler)

    return logger


def enable_rich_traceback() -> None:
    """Turns on rich printing for exceptions."""
    traceback.install()
