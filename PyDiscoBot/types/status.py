"""status module
    """
from __future__ import annotations


import os
from datetime import datetime
from typing import Optional


import discord


__all__ = (
    'Status',
)


class _StatusChannels:
    """Status channels for :class:`Status`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    admin: Optional[:class:`discord.abc.GuildChannel`]
        Channel where admin embed is posted.

    notification: Optional[:class:`discord.abc.GuildChannel`]
        Channel where notifications are posted.

    """
    admin: Optional[discord.abc.GuildChannel] = None
    notification: Optional[discord.abc.GuildChannel] = None


class Status:
    """Status container for the parent :class:`Bot`

    This data class describes the meta information about bot status.

    .. ------------------------------------------------------------

    Attributes
    -----------
    version: :class:`str`
        Current running version the :class:`Bot` booted with.

    boot_time: :class:`datetime.datetime`
        Datetime describing the moment the bot initialized this class.

    last_time: :class:`datetime.datetime`
        Datetime describing the last time the :class:`Bot` ran it's administrative task.

    cycle_time: :class:`int`
        Number of **seconds** between periodic bot ticks.

    current_tick: :class:`int`
        Number describing the amount of ticks performed.

    channels: :class:`_StatusChannels`
        Status channels for the :class:`Bot` to use.

    initialized: :type:'bool'
        Bot has been initialized memory.

    """

    def __init__(self):
        self._version: str = os.getenv('VERSION', 'N/A?')
        self._boot_time: datetime = datetime.now()
        self._last_time: datetime = datetime.now()
        self._tick: int = 0
        self._channels: _StatusChannels = _StatusChannels()
        self._initialized: bool = False

        try:
            self._cycle_time: int = int(os.getenv('CYCLE_TIME', '600'))
        except KeyError:
            self._cycle_time: int = 600   # 10 minute default time

    @property
    def version(self) -> str:
        """ Current running version the :class:`Bot` booted with.

        Returns
        -----------
            :type:`str`
        """
        return self._version

    @property
    def boot_time(self) -> datetime:
        """ Datetime describing the moment the bot initialized this class.

        Returns
        -----------
            :class:`datetime.datetime`
        """
        return self._boot_time

    @property
    def last_time(self) -> datetime:
        """ Datetime describing the last time the :class:`Bot` ran it's administrative task.

        Returns
        -----------
            :class:`datetime.datetime`
        """
        return self._last_time

    @property
    def current_tick(self) -> int:
        """ Number describing the amount of ticks performed.

        Returns
        -----------
            :type:`int`
        """
        return self._tick

    @property
    def channels(self) -> _StatusChannels:
        """ Status channels for the :class:`Bot` to use.

        Returns
        -----------
            :class:`pydiscobot.types.status._StatusChannels`
        """
        return self._channels

    @property
    def initialized(self) -> bool:
        """ Bot has been initialized memory.

        Returns
        -----------
            :type:`bool`
        """
        return self._initialized

    @initialized.setter
    def initialized(self, value) -> None:
        self._initialized = value

    @property
    def cycle_time(self) -> int:
        """ Number of **seconds** between periodic bot ticks.

        Returns
        -----------
            :type:`int`
        """
        return self._cycle_time

    def tick(self) -> None:
        """Increment the `current_tick` by +1

        Also, updates the last time to `datetime.now()`
        """
        self._tick += 1
        self._last_time = datetime.now()
