"""clear discord channel of messages
can only support up to 100, cannot delete older than 14 days (Discord rule)
    """

import discord
from discord import app_commands
from pydiscobot.services.channels import clear_messages
from pydiscobot.types import Cmd


class ClearChannel(Cmd):
    """ClearChannel command cog.
        """

    @app_commands.command(name='clearchannel',
                          description='Clear channel messages.')
    @app_commands.describe(message_count='amt of messages to delete.')
    @app_commands.default_permissions()
    async def clearchannel(self,
                           interaction: discord.Interaction,
                           message_count: int):
        """Clear a discord :class:`TextChannel` of messages.

        Arguments
        -----------
        interaction: :class:`discord.Interaction`
            The interaction this command belongs to.
        message_count: :class:`int`
            Number of messages to delete. Must be < 100.
        """
        await interaction.response.defer()
        await clear_messages(interaction.channel, message_count)
