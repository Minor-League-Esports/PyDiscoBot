"""provide an abc base class for all tasks to derive from for consistent operations
    """
from __future__ import annotations


from logging import Logger
from typing import TYPE_CHECKING


from .log import logger
from .types import BaseTask


if TYPE_CHECKING:
    from .bot import Bot


__all__ = (
    'Task',
)


class Task(BaseTask):
    """PyDiscoBot :class:`Task` for logical, periodic operations.

    All user tasks should be derived from this :class:`Task`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    logger: :class:`Logger`
        The logger for this :class:`Task`

    .. ------------------------------------------------------------

    Examples
    ----------

    Create a child :type:`class` that inherits this class :class:`Task`

    .. code-block:: python

        import discord
        from pydiscobot import Task

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
                 parent: Bot):
        super().__init__(parent)
        self._logger = logger(self.name)

    @property
    def logger(self) -> Logger:
        """Get the :class:`pydiscobot.Bot` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    parent: :class:`pydiscobot.Bot`
        The parent :class:`pydiscobot.Bot` that owns this :class:`Task`.

    """
        return self._logger

    async def run(self):
        """Method that is called by :class:`pydiscobot.Bot` during it's ticks.

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
        raise NotImplementedError()
