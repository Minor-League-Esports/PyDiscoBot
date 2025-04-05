"""generate a unix date string for display common times across discord
    (Time zone agnostic)
    """

import datetime
import time
import discord
from discord import app_commands
from ...embed_frames import frame
from ...types import Cmd, EmbedField


class DateToUnix(Cmd):
    """convert string of date to unix
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
                         second: int):
        """convert string of date to unix

        Args:
            ctx (discord.ext.commands.Context): discord context
        """
        try:
            _d = f'{year}/{month}/{day} {hour}:{minute}:{second}'
            d = datetime.datetime.strptime(_d, '%y/%m/%d %H:%M:%S')
            unix_time = time.mktime(d.timetuple())

            f = [EmbedField('date ->',
                            f'template: <`t:{str(int(unix_time))}:F`>  (remember to add < and > around the template!)\n'
                            f'<t:{int(unix_time)}:F>')]
            await interaction.response.send_message(embed=frame('**Date To Unix**',
                                                                '',
                                                                f))

        except ValueError:
            await interaction.response.send_message('You must give a date in the following format:\n'
                                                    '%y/%m/%d %H:%M:%S\n'
                                                    'do not include am/pm. use 24 hour clock.')
