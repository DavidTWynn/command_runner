from src import utils


def test_rich_exception():
    utils.enable_rich_traceback()


def test_log_settings():
    logger = utils.logging_settings()
