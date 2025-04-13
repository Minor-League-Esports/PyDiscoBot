"""provide a help display to discord users
    """
from __future__ import annotations

import discord
from discord import app_commands
from pydiscobot.embed_frames import frame
from pydiscobot.types import cmd

MSG = '**help**', 'If you have an issue, please reach out to `irox_rl`.'


class Help(cmd.Cmd):
    """help
    """

    @app_commands.command(name='help',
                          description='Get general help.')
    @app_commands.default_permissions()
    async def help(self,
                   interaction: discord.Interaction):
        """Get general help, posted as a reply.

        There isn't much info here, but it helps nonetheless.

        Help used to be used with :class:`pydiscobot.types.InteractionPagination` to show all :class:`Cmd`s.
        Now, `app_command`s are used, which are controlled by server mods (by default).
        The allowed list is unique per user, and is displayed automagically by Discord
        when the user starts a message with `/`.

        Now, we have it as a legacy command, just to over-ride the :class:`discord.Bot` method.

        .. ------------------------------------------------------------

        Arguments
        -----------
        interaction: :class:`discord.Interaction`
            The interaction this command belongs to.

        """
        embed = frame.get_frame(MSG)
        await interaction.response.send_message(embed=embed)
