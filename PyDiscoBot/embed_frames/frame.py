"""provide a generalized embed or 'frame' to create all other embeds from
    this keeps the look nice and consistent
    """
from __future__ import annotations

import datetime
import discord
from pydiscobot.types import EmbedField


def get_frame(title: str,
              descr: str | None = None,
              fields: list[EmbedField] | None = None,
              color: str = str(discord.Color.dark_blue()),
              thumbnail: str = None) -> discord.Embed:
    """get generic embed frame for consistent formatting.

    Args:
        title (str): title of the embed
        descr (str | None, optional): description to add. Defaults to None.
        fields (list[EmbedField] | None, options): fields to add to embed

    Returns:
        discord.Embed: generic embed
    """

    embed = (discord.Embed(
        color=discord.Color.from_str(color),
        title=title,
        description=descr)
        .set_footer(text=f'Generated: {datetime.datetime.now()}')
        .set_thumbnail(url=thumbnail))

    for field in fields:
        if field is None:
            continue
        embed.add_field(name=field.name,
                        value=field.value,
                        inline=field.inline)

    return embed
