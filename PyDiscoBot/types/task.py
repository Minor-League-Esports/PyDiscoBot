"""provide an abc base class for all tasks to derive from for consistent operations
    """
from __future__ import annotations

from abc import ABC, abstractmethod
from logging import Logger
from typing import Any
import pydiscobot
from pydiscobot.services import log


class Task(ABC):
    """:class:`ABC` abstract class for :class:`Bot` tasks.

    All tasks should be derived from this abstract :class:`Task`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: :class:`pydiscobot.Bot`
        The bot this task belongs to.

    .. ------------------------------------------------------------

    Attributes
    -----------
    name: :class:`str`
        The name of this :class:`Task`.

    parent: :class:`pydiscobot.Bot`
        The parent :class:`Bot` of this :class:`Task`.

    .. ------------------------------------------------------------

    Examples
    ----------

    Create a child :type:`class` that inherits this class :class:`Task`

    .. code-block:: python

        import discord
        from pydiscobot.types import Task

        class MyTask(Task):
            'this is my task class!'

            def __init__(self,
                         parent: pydiscobot.Bot):
                super().__init__(parent)
                ...

            def run(self):
                'this override gets triggered by the bot every tick!'
                ...

    """

    def __init__(self,
                 parent: pydiscobot.Bot):
        self._parent = parent
        self._logger = log.logger(self.__class__.__name__)

    @property
    def name(self) -> str:
        """get the name of this task

        Returns:
            str: name
        """
        return self.__class__.__name__

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
