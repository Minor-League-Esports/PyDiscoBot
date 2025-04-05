"""bot administrative information
    """

import os
from dataclasses import dataclass
from datetime import datetime
from .admin_channels import AdminChannels


@dataclass
class AdminInfo:
    """bot administrative information
    """
    version: str = os.getenv('VERSION')
    boot_time: datetime = datetime.now()
    last_time: datetime = datetime.now()
    cycle_time: int = int(os.getenv('CYCLE_TIME'))
    current_tick: int = 0
    channels: AdminChannels = AdminChannels
    initialized: bool = False
