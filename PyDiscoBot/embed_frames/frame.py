from dataclasses import dataclass
import datetime
import discord
from ..services.const import DEF_EMBED_COLOR, DEF_EMBED_URL


@dataclass
class EmbedField:
    """helper class to create embed fields more easily
    """
    name: str
    value: str
    inline: bool = False


def frame(title: str,
          descr: str | None = None,
          fields: list[EmbedField] | None = None,
          color: str = DEF_EMBED_COLOR,
          thumbnail: str = DEF_EMBED_URL) -> discord.Embed:
    """get generic embed frame for consistent formatting.

    Args:
        title (str): title of the embed
        descr (str | None, optional): description to add. Defaults to None.
        fields (list[EmbedField] | None, options): fields to add to embed

    Returns:
        discord.Embed: generic embed
    """

    embed = (discord.Embed(
        color=color,
        title=title,
        description=descr)
        .set_footer(text=f'Generated: {datetime.datetime.now()}')
        .set_thumbnail(url=thumbnail))

    for field in fields:
        embed.add_field(name=field.name,
                        value=field.value,
                        inline=field.inline)

    return embed
