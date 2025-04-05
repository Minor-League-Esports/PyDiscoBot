"""provide error types for defining raise conditions
    """

from discord.ext import commands


class BotNotLoaded(commands.CheckFailure):
    """bot has not finished loading yet.
    """
    pass


class InsufficientPrivilege(commands.CheckFailure):
    """user does not have correct privileges.
    """
    pass


class IllegalChannel(commands.CheckFailure):
    """you cannot do that action in this channel.
    """
    pass


class ReportableError(Exception):
    pass
