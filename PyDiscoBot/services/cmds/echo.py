"""echo a string
    mostly just a testing function
    surprisingly, does support @ing people
    """

import discord
from discord import app_commands
from ...types import Cmd


class Echo(Cmd):
    """echo string
    """

    @app_commands.command(name='echo',
                          description='Echo.')
    @app_commands.describe(message='string to echo')
    @app_commands.default_permissions()
    async def echo(self,
                   interaction: discord.Interaction,
                   message: str):
        """echo back to user

        Args:
            ctx (discord.ext.commands.Context): discord context to echo to
        """
        await interaction.response.send_message(message)
