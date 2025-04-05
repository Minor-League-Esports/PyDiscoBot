"""clear discord channel of messages
can only support up to 100, cannot delete older than 14 days (Discord rule)
    """

import discord
from discord import app_commands
from ..channels import clear_messages
from ...types import Cmd


class ClearChannel(Cmd):
    """clear text channel
    """

    @app_commands.command(name='clearchannel',
                          description='Clear channel messages.')
    @app_commands.describe(message_count='amt of messages to delete.')
    @app_commands.default_permissions()
    async def clearchannel(self,
                           interaction: discord.Interaction,
                           message_count: int):
        """'Clear channel messages. Include amt of messages to delete.'

        Args:
            interaction (discord.Interaction): interaction source
            message_count (int): amt of msgs to delete
        """
        await interaction.response.defer()
        await clear_messages(interaction.channel, message_count)
