"""Common discord command
    all discord commands should be derived from the meta class
    """
from __future__ import annotations

from discord.ext import commands
import pydiscobot


class Cmd(commands.Cog):
    """Pseudo 'meta' discord bot `Command`.

    Though this is not an :class:`ABC`, this class describes the meta
    relationship the command has within this environment.

    That being said, all commands used for the bot should be
    derived from this 'meta' `Command`

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: :class:`pydiscobot.Bot`
        The parent :class:`Bot` of this `Command`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    parent: :class:`pydiscobot.Bot`
        The parent :class:`Bot` of this `Command`.

    """

    def __init__(self,
                 parent: pydiscobot.Bot):
        self._parent = parent

    @property
    def parent(self) -> pydiscobot.Bot:
        """get parent of this command

        Returns:
            bot.Bot: parent bot
        """
        return self._parent
