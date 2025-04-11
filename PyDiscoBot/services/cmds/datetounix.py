"""generate a unix date string for display common times across discord
    (Time zone agnostic)
    """
from __future__ import annotations

import datetime
import time
import discord
from discord import app_commands
from pydiscobot.embed_frames import frame
from pydiscobot.types import Cmd, EmbedField


ERR = '\n'.join([
    'You must give a date in the following format:'
    '%y/%m/%d %H:%M:%S -> e.g. "25/8/16 12:00:00"'
    'do not include am/pm. use 24 hour clock.'
])


class DateToUnix(Cmd):
    """convert date to unix string
    date is placed into embed, broken apart, so it can be copied and pasted by the user.
    """

    @app_commands.command(name='datetounix',
                          description='convert string of date to unix')
    @app_commands.describe(year='year')
    @app_commands.describe(month='month')
    @app_commands.describe(day='day')
    @app_commands.describe(hour='hour')
    @app_commands.describe(minute='minute')
    @app_commands.describe(second='second')
    @app_commands.default_permissions()
    async def datetounix(self,
                         interaction: discord.Interaction,
                         year: int,
                         month: int,
                         day: int,
                         hour: int,
                         minute: int,
                         second: int) -> None:
        """Convert passed params to a unix-based date.

        This date will display agnostically across discord :class:`TextChannel`s.

        Date is placed into embed, broken apart, so it can be copied and pasted by the user.

        Arguments
        -----------
        year: :class:`int`
            Year to display.
        month: :class:`int`
            Month to display.
        day: :class:`int`
            Day to display.
        hour: :class:`int`
            Hour to display.
        minute: :class:`int`
            Minute to display.
        second: :class:`int`
            Second to display.
        """
        try:
            _d = f'{year}/{month}/{day} {hour}:{minute}:{second}'
            d = datetime.datetime.strptime(_d, '%y/%m/%d %H:%M:%S')
            unix_time = time.mktime(d.timetuple())

            f = [EmbedField('date ->',
                            f'template: <`t:{str(int(unix_time))}:F`>\n'
                            f'<t:{int(unix_time)}:F>')]
            await interaction.response.send_message(embed=frame.get_frame('**Date To Unix**',
                                                                          '',
                                                                          f))

        except ValueError:
            await interaction.response.send_message(ERR)
