"""bot administrative information
    """

import os
from datetime import datetime
from .admin_channels import AdminChannels


class AdminInfo:
    """Administrative information for the parent :class:`Bot`

    This data class describes the meta information about the bot.

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
    channels: :class:`AdminChannels`
    Administrative channels for the :class:`Bot` to use.
    """

    def __init__(self):
        self.version: str = os.getenv('VERSION')
        self.boot_time: datetime = datetime.now()
        self.last_time: datetime = datetime.now()
        try:
            self.cycle_time: int = os.getenv('CYCLE_TIME')
        except KeyError:
            self.cycle_time: int = 600   # 10 minute default time
        self.current_tick: int = 0
        self.channels: AdminChannels = AdminChannels
        self.initialized: bool = False
