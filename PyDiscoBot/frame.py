"""provide a generalized embed or 'frame' to create all other embeds from
    this keeps the look nice and consistent
    """
from __future__ import annotations


import datetime
from typing import Optional, Union
import unittest

import discord

from . import const
from .types import EmbedField, Status


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


def get_status_frame(info: Status) -> discord.Embed:
    """Get built-in :class:`discord.Embed` (or 'frame') to display :class:`Bot` :class:`Status`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    info: :class:`Status`
        The Information describing it's parent :class:`Bot`.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a :class:`discord.Embed` to display a to channel.

    .. code-block:: python

        import discord
        from pydiscobot.embed_frames import get_status_frame

        async def post_info(self,
                                  channel: discord.TextChannel):
            '''post info to channel'''

            embed = get_status_frame(self.bot.status_info)
            await channel.send(embed=embed)

    """
    embed = get_frame('**Bot Info**',
                      'For help, type `/help`',
                      [
                          EmbedField('Version', f"`{info.version}`"),
                          EmbedField('Boot Time', f"`{info.boot_time.strftime(const.DEF_TIME_FORMAT)}`", True),
                          EmbedField('Current Tick', f"`{info.current_tick}`"),
                          EmbedField('Last Time', f"`{info.last_time}`"),
                          EmbedField('Cycle Time', f"`{info.cycle_time}`s", True)
                      ])

    return embed


def get_notification_frame(text: str) -> discord.Embed:
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


class TestFrames(unittest.TestCase):
    """test frames for pydisco bot
    """

    def test_get_frame(self):
        """test bot can compile and receive default frame
        """
        self.assertTrue(isinstance(get_frame(), discord.Embed))

    def test_get_status_frame(self):
        """test bot can compile and receive status frame
        """
        self.assertTrue(isinstance(get_status_frame(Status()), discord.Embed))

    def test_get_notification_frame(self):
        """test bot can compile and receive notification frame
        """
        self.assertTrue(isinstance(get_notification_frame('bing bong'), discord.Embed))
