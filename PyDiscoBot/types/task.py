"""provide an abc base class for all tasks to derive from for consistent operations
    """
from __future__ import annotations

from abc import ABC, abstractmethod
from logging import Logger
from pydiscobot import bot
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
                 parent: bot.Bot):
        self._parent: bot.Bot = parent
        self._logger = log.logger(self.__class__.__name__)

    @property
    def name(self) -> str:
        """Get the `name` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    name: :class:`str`
        The name of this :class:`Task`.

    """
        return self.__class__.__name__

    @property
    def logger(self) -> Logger:
        """Get the :class:`Logger` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    logger: :class:`Logger`
        The :class:`Logger` of this :class:`Task`.

    """
        return self._logger

    @property
    def parent(self) -> bot.Bot:
        """Get the :class:`pydiscobot.Bot` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    parent: :class:`pydiscobot.Bot`
        The parent :class:`pydiscobot.Bot` that owns this :class:`Task`.

    """
        return self._parent

    @abstractmethod
    async def run(self):
        """Abstract method that is called by :class:`pydiscobot.Bot` during it's ticks.

    A class inheriting this task must override this method.

    .. ------------------------------------------------------------

    Example
    ----------

    Create a child :type:`class` that inherits this class :class:`Task`
    and overrides the :callable:`run` function.

    .. code-block:: python

        import discord
        from pydiscobot.types import Task

        class MyTask(Task):
            'this is my task class!'

            def __init__(self,
                         parent: pydiscobot.Bot):
                super().__init__(parent)
                ...  # initialize the task

            def run(self):
                'this override gets triggered by the bot every tick!'
                ...  # do some logic


    """
