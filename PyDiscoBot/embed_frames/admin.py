"""admin embed
    """
from __future__ import annotations

import discord
from pydiscobot.types import AdminInfo, EmbedField
from .frame import get_frame


def get_admin_frame(info: AdminInfo) -> discord.Embed:
    """admin info embed

    Args:
        info (AdminInfo): info to post

    Returns:
        discord.Embed: embed
    """
    embed = get_frame('**Bot Info**',
                      'For help, type `/help`',
                      [
                          EmbedField('Version', f"`{info.version}`"),
                          EmbedField('Boot Time', f"`{info.boot_time.strftime('%c')}`", True),
                          EmbedField('Current Tick', f"`{info.current_tick}`"),
                          EmbedField('Last Time', f"`{info.last_time}`"),
                          EmbedField('Cycle Time', f"`{info.cycle_time}`s", True)
                      ])

    return embed
