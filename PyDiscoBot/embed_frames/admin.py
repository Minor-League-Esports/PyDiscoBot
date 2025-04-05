"""admin embed
    """

import discord
from .frame import frame
from ..types import AdminInfo, EmbedField


def admin(info: AdminInfo) -> discord.Embed:
    """admin info embed

    Args:
        info (AdminInfo): info to post

    Returns:
        discord.Embed: embed
    """
    embed = frame('**Bot Info**',
                  'For help, type `/help`',
                  [
                      EmbedField('Version', f"`{info.version}`"),
                      EmbedField('Boot Time', f"`{info.boot_time.strftime('%c')}`", True),
                      EmbedField('Current Tick', f"`{info.current_tick}`"),
                      EmbedField('Last Time', f"`{info.last_time}`"),
                      EmbedField('Cycle Time', f"`{info.cycle_time}`s", True)
                  ])

    return embed
