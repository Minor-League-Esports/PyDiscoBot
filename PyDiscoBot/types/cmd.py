"""Common discord command
    all discord commands should be derived from the meta class
    """
from __future__ import annotations

from discord.ext import commands
from pydiscobot import bot


class Cmd(commands.Cog):
    """generic bot command
    """

    def __init__(self,
                 parent: bot.Bot):
        self._parent = parent

    @property
    def parent(self) -> bot.Bot:
        """get parent of this command

        Returns:
            bot.Bot: parent bot
        """
