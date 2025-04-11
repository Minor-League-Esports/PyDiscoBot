"""logger service to get a logger as a specified name, or the name of the file if none passed
    """
from __future__ import annotations

import logging


loggers = {}  # quick hash dict for loggers
# this prevents duplicates from being dealt out, as well as prevents duplicate handlers being set to a logger


def logger(name: str = __name__):
    """get common logger

    Args:
        name (str, optional): name of logger. Defaults to __name__.

    Returns:
        logging.Logger: logger
    """
    if loggers.get(name):
        return loggers.get(name)

    _logger = logging.getLogger(name)
    _logger.setLevel(logging.INFO)

    cons = logging.StreamHandler()
    cons.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt="%m/%d/%Y, %H:%M:%S")

    cons.setFormatter(formatter)
    _logger.addHandler(cons)

    loggers[name] = _logger

    return _logger
