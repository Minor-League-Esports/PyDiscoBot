from dataclasses import dataclass, field
import discord


@dataclass
class AdminChannels:
    """discord admin channels
    """
    admin: discord.abc.GuildChannel | None = field(default_factory=lambda: None)
    notification: discord.abc.GuildChannel | None = field(default_factory=lambda: None)
