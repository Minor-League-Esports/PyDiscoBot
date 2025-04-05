"""user notification frame
    """

import discord
from .frame import frame, EmbedField


def notification(text: str) -> discord.Embed:
    """get notification embed

    Args:
        text (str): notification to display

    Returns:
        discord.Embed: notification embed with text included
    """
    embed = frame('**Notification**',
                  None,
                  [EmbedField('Message', value=text, inline=True)])
    return embed
