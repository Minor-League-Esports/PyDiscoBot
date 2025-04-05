"""sync the bot's app tree for slash commands
    this is required to populate new commands
    or to update attrs to existing commands
    """

import discord
from discord import app_commands
from discord.ext import commands
from ...types import Cmd


class Sync(Cmd):
    """sync commands
    """

    @app_commands.command(name='sync',
                          description='Sync bot app tree.')
    async def app_cmd_sync(self,
                           interaction: discord.Interaction):
        """sync discord bot tree to server

        Args:
            interaction (discord.Interaction): discord interaction
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
        """sync discord bot tree to server

        Args:
            interaction (discord.Interaction): discord interaction
        """
        await self._parent.tree.sync()
        await self._parent.send_notification(ctx,
                                             'Sync complete!',
                                             as_followup=True)
