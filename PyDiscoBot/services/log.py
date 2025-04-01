import logging


def logger(name: str = __name__):
    """get common logger

    Args:
        name (str, optional): name of logger. Defaults to __name__.

    Returns:
        logging.Logger: logger
    """
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.INFO)

    cons = logging.StreamHandler()
    cons.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt="%m/%d/%Y, %H:%M:%S")

    cons.setFormatter(formatter)
    _logger.addHandler(cons)

    return _logger
