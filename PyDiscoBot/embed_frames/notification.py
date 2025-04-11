"""user notification frame
    """
from __future__ import annotations

import discord
from pydiscobot.types import EmbedField
from .frame import get_frame


def get_notification(text: str) -> discord.Embed:
    """get notification embed

    Args:
        text (str): notification to display

    Returns:
        discord.Embed: notification embed with text included
    """
    embed = get_frame('**Notification**',
                      None,
                      [EmbedField('Message', value=text, inline=True)])
    return embed
