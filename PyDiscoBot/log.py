"""logger service to get a logger as a specified name, or the name of the file if none passed
    """
from __future__ import annotations

import logging


loggers = {}  # quick hash dict for loggers
# this prevents duplicates from being dealt out, as well as prevents duplicate handlers being set to a logger


def logger(name: str = __name__):
    """Get a :class:`Logger` of the specified name, creating one if none already exists.

    Each :class:`Logger` is hashed and stored locally.

    .. ------------------------------------------------------------

    Arguments
    -----------

    name: :class:`str`
        The name of the :class:`Logger` to get or create.


    .. ------------------------------------------------------------

    Returns
    --------
    :class:`Logger`
        `logging.Logger`, ready to display information.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a logger for a :type:`class` using the :type:`class`'s name

    .. code-block:: python

        from pydiscobot.services.log import logger

        class MyClass:
        'This is my class!'
        def __init__(self):
            self._logger = logger(self.__class__.__name__)
            self._logger.info('This is a great way to get my logger!')


        >>> r'06/9/2025, 12:04:20 | MyClass | INFO | This is a great way to get my logger!'


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
