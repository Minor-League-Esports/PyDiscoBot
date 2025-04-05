"""bot administrative channels
    """

from dataclasses import dataclass
import discord


@dataclass
class AdminChannels:
    """discord admin channels
    """
    admin: discord.abc.GuildChannel | None = None
    notification: discord.abc.GuildChannel | None = None
