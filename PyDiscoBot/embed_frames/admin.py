import discord
from .frame import frame, EmbedField
from ..types import AdminInfo


def admin(info: AdminInfo) -> discord.Embed:
    """ helper to get information embed\n
        **returns**: discord.Embed with bot info attached\n
    """
    fields = [
        EmbedField('Version', f"`{info.version}`"),
        EmbedField('Boot Time', f"`{info.boot_time.strftime('%c')}`", inline=True),
        EmbedField('Current Tick', f"`{info.current_tick}`"),
        EmbedField('Last Time', f"`{info.last_time}`"),
        EmbedField('Cycle Time', f"`{info.cycle_time}`s", inline=True)
    ]
    embed = frame('**Bot Info**',
                  'For help, type `/help`',
                  fields)

    return embed
