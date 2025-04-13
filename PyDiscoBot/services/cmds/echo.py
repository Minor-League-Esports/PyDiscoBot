"""echo a string
    mostly just a testing function
    surprisingly, does support @ing people
    """
from __future__ import annotations

import discord
from discord import app_commands
from pydiscobot.types import cmd


class Echo(cmd.Cmd):
    """echo string
    """

    @app_commands.command(name='echo',
                          description='Echo.')
    @app_commands.describe(message='string to echo')
    @app_commands.default_permissions()
    async def echo(self,
                   interaction: discord.Interaction,
                   message: str):
        """Echo a string back to the user.

        Intended to debugging purposes (and messing with Flap)

        .. ------------------------------------------------------------

        Arguments
        -----------
        interaction: :class:`discord.Interaction`
            The interaction this command belongs to.

        message: :class:`str`
            Message to echo back to the user.

        """
        await interaction.response.send_message(message)
