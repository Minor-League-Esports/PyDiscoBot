"""provide a help display to discord users
    """

import discord
from discord import app_commands
from ...embed_frames import frame
from ...types import Cmd


class Help(Cmd):
    """help
    """

    @app_commands.command(name='help',
                          description='Get general help.')
    @app_commands.default_permissions()
    async def help(self,
                   interaction: discord.Interaction):
        """get general help.

        Args:
            interaction (discord.Interaction): discord interaction
        """
        embed = frame(
            '**help**', 'If you have an issue, please reach out to `irox_rl`.')
        await interaction.response.send_message(embed=embed)
