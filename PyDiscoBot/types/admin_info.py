from dataclasses import dataclass, field
from datetime import datetime
from .admin_channels import AdminChannels


@dataclass
class AdminInfo:
    """bot administrative information
    """
    version: str
    boot_time: datetime
    last_time: datetime
    cycle_time: int
    current_tick: int = 0
    channels: AdminChannels = field(default_factory=AdminChannels)
    initialized: bool = False
