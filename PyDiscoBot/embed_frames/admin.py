"""admin embed
    """
from __future__ import annotations

import discord
from pydiscobot.services.const import DEF_TIME_FORMAT
from pydiscobot.types import AdminInfo, EmbedField
from .frame import get_frame


def get_admin_frame(info: AdminInfo) -> discord.Embed:
    """Get built-in :class:`discord.Embed` (or 'frame') to display :class:`Bot` :class:`AdminInfo`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    info: :class:`AdminInfo`
        The Administrative Information describing it's parent :class:`Bot`.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a :class:`discord.Embed` to display a to Admin channel.

    .. code-block:: python

        import discord
        from pydiscobot.embed_frames import get_admin_frame

        async def post_admin_info(self,
                                  channel: discord.TextChannel):
            '''post admin info to channel'''

            admin_embed = get_admin_frame(self.bot.admin_info)
            await channel.send(embed=admin_embed)

    """
    embed = get_frame('**Bot Info**',
                      'For help, type `/help`',
                      [
                          EmbedField('Version', f"`{info.version}`"),
                          EmbedField('Boot Time', f"`{info.boot_time.strftime(DEF_TIME_FORMAT)}`", True),
                          EmbedField('Current Tick', f"`{info.current_tick}`"),
                          EmbedField('Last Time', f"`{info.last_time}`"),
                          EmbedField('Cycle Time', f"`{info.cycle_time}`s", True)
                      ])

    return embed
