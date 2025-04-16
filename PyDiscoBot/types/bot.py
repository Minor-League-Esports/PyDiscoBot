"""bot type module
    """
from __future__ import annotations


from logging import Logger
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .status import Status
    from .tasker import Tasker


__all__ = (
    'BaseBot',
)


class BaseBot:
    """Base bot type.

    .. ------------------------------------------------------------

    Attributes
    -----------
    admin_info: :class:`AdminInfo`
        Administrative information for the bot, such as `ticks` and `version`

    logger: :class:`Logger`
        Logging module for the bot. Displays information to terminal.

    tasker: :class:`Tasker`
        Periodic task manager for the bot. Calls periodic tasks on `tick`.

    """
    _status: Status
    _logger: Logger
    _tasker: Tasker

    @property
    def status(self) -> Status:
        """ Administrative information for the bot, such as `ticks` and `version`

        .. ------------------------------------------------------------

        Returns
        -----------
            :class:`pydiscobot.types.AdminInfo`
        """
        return self._status

    @property
    def logger(self) -> Logger:
        """Logging module for the bot. Displays information to terminal.

        .. ------------------------------------------------------------

        Returns
        -----------
            :class:`logging.Logger`
        """
        return self._logger

    @property
    def tasker(self) -> Tasker:
        """Periodic task manager for the bot. Calls periodic tasks on `tick`.

        .. ------------------------------------------------------------

        Returns
        -----------
            :class:`pydiscobot.types.Tasker`
        """
        return self._tasker
