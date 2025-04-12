"""bot administrative channels
    """

from dataclasses import dataclass
from typing import Optional
import discord


@dataclass
class AdminChannels:
    """Administrative channels dataclass for the parent :class:`Bot`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    admin: Optional[:class:`discord.abc.GuildChannel`]
        Administrative channel where admin embed is posted.

    notification: Optional[:class:`discord.abc.GuildChannel`]
        Notification channel where infos are posted

    """
    admin: Optional[discord.abc.GuildChannel] = None
    notification: Optional[discord.abc.GuildChannel] = None
