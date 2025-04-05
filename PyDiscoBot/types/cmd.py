"""Common discord command
    all discord commands should be derived from the meta class
    """

from discord.ext import commands


class Cmd(commands.Cog):
    """generic bot command
    """

    def __init__(self,
                 parent):
        self._parent = parent
