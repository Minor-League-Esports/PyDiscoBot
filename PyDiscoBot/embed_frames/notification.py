"""notification frame
    """
from __future__ import annotations

import discord
from pydiscobot.types import EmbedField
from .frame import get_frame


def get_notification(text: str) -> discord.Embed:
    """Get built-in :class:`discord.Embed` (or 'frame') to display a standard notification.

    .. ------------------------------------------------------------

    Arguments
    -----------
    text: :class:`str`
        The message to display in the body of the :class:`discord.Embed`.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a :class:`discord.Embed` to display a general notification.

    .. code-block:: python

        import discord
        from pydiscobot.embed_frames import get_notification

        async def send_notfication(self,
                                    channel: discord.TextChannel):
            '''post notification to channel'''

            embed = get_notification('How are ya doin today?')

            await channel.send(embed=embed)

    """
    embed = get_frame('**Notification**',
                      None,
                      [EmbedField('Message', value=text, inline=True)])
    return embed
