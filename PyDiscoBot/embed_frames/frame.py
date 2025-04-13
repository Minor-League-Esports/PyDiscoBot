"""provide a generalized embed or 'frame' to create all other embeds from
    this keeps the look nice and consistent
    """
from __future__ import annotations

import datetime
from typing import Optional, Union
import discord
from pydiscobot.services import const
from pydiscobot.types.embed_field import EmbedField


def get_frame(title: Optional[str] = None,
              descr: Optional[str] = None,
              fields: Optional[list[EmbedField]] = None,
              color: Union[discord.Color, str] = discord.Color.dark_blue(),
              thumbnail: Optional[str] = None) -> discord.Embed:
    """Get built-in :class:`discord.Embed` (or 'frame') for consistent formatting.

    It is recommended all :class:`discord.Embed`s displayed are created through this method.

    .. ------------------------------------------------------------

    Arguments
    -----------
    title: Optional[:class:`str`]
        The title to create the :class:`discord.Embed` with.

    descr: Optional[:class:`str`]
        An optional header description to begin the :class:`discord.Embed` with.

    fields: Optional[list[:class:`EmbedField`]]
        An optional list of :class:`EmbedField` to append to the :class:`discord.Embed`
        during it's creation.

    color: Union[:class:`discord.Color`, :class:`str`]
        A color to decorate the Embed with. Will default to ::

            discord.Color.dark_blue()

    thumbnail: Optional[:class:`str`]
        An optional thumbnail or 'image' to append to the embed.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a :class:`discord.Embed` to display a notification to the user

    .. app_command --->

    .. code-block:: python

        import discord
        from pydiscobot.embed_frames import get_frame
        from pydiscobot.types import EmbedField

        MY_ERR_VALUE = 'you are being notified!'

        async def send_notification(self,
                                    interaction: discord.Interaction):
            '''send notification to user'''
            await interaction.response.defer()

            my_frame = get_frame(title='**Notification**',
                                descr='An Error Has Occured...',
                                fields=[EmbedField(
                                name='Error',
                                value=MY_ERR_VALUE
                                )])

            await interaction.followup.send(embed=my_frame)

    .. ------------------------------------------------------------

    .. command --->

    .. code-block:: python

        import discord
        from pydiscobot.embed_frames import get_frame
        from pydiscobot.types import EmbedField

        MY_ERR_VALUE = 'you are being notified!'

        async def send_notification(self,
                                    ctx: discord.ext.commands.Context):
            '''send notification to user'''

            my_frame = get_frame(title='**Notification**',
                                    descr='An Error Has Occured...',
                                    fields=[EmbedField(
                                    name='Error',
                                    value=MY_ERR_VALUE
                                )])

            await ctx.send(embed=my_frame)

    """

    embed = (discord.Embed(
        color=discord.Color.from_str(str(color)),
        title=title,
        description=descr)
        .set_footer(text=f'Generated: {datetime.datetime.now().strftime(const.DEF_TIME_FORMAT)}')
        .set_thumbnail(url=thumbnail))

    if not fields:
        return embed

    for field in fields:
        if field is None:
            continue
        embed.add_field(name=field.name,
                        value=field.value,
                        inline=field.inline)

    return embed
