"""provide an abc base class for all tasks to derive from for consistent operations
    """

from abc import ABC, abstractmethod
from logging import Logger
from typing import Any
from ..services.log import logger


class Task(ABC):
    """task for cyclic operations
    """

    def __init__(self,
                 parent):
        self._parent = parent
        self._logger = logger(self.__class__.__name__)

    @property
    def logger(self) -> Logger:
        """get this task's logger

        Returns:
            Logger: logger
        """
        return self._logger

    @property
    def parent(self) -> Any:
        """get this task's parent

        Returns:
            Any: parent
        """
        return self._parent

    @abstractmethod
    async def run(self):
        """run the task
        """
