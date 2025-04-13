"""sync the bot's app tree for slash commands
    this is required to populate new commands
    or to update attrs to existing commands
    """
from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands
from pydiscobot.types import cmd


class Sync(cmd.Cmd):
    """sync commands
    """

    @app_commands.command(name='sync',
                          description='Sync bot app tree.')
    async def app_cmd_sync(self,
                           interaction: discord.Interaction):
        """Sync bot app tree.

        This command is required when the signature of a command changes.
        It is also required when a new command is created.

        Usually, you will need to restart your `Discord Application` to see the new changes.
        Otherwise, the Discord API will respond with an err.

        .. ------------------------------------------------------------

        Arguments
        -----------
        interaction: :class:`discord.Interaction`
            The interaction this command belongs to.

        """
        await interaction.response.defer()
        await self._parent.tree.sync()
        await self._parent.send_notification(interaction,
                                             'Sync complete!',
                                             as_followup=True)

    @commands.command(name='sync',
                      description='Sync bot app tree.')
    async def sync(self,
                   ctx: discord.ext.commands.Context):
        """Sync bot app tree.

        This command is required when the signature of a command changes.
        It is also required when a new command is created.

        Usually, you will need to restart your `Discord Application` to see the new changes.
        Otherwise, the Discord API will respond with an err.

        .. ------------------------------------------------------------

        Arguments
        -----------
        interaction: :class:`discord.Interaction`
            The interaction this command belongs to.

        """
        await self._parent.tree.sync()
        await self._parent.send_notification(ctx,
                                             'Sync complete!',
                                             as_followup=True)
