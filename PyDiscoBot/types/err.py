"""provide error types for defining raise conditions
    """
from __future__ import annotations


from discord.ext import commands


__all__ = (
    'BotNotLoaded',
    'InsufficientPrivilege',
    'IllegalChannel',
    'ReportableError'
)


class BotNotLoaded(commands.CheckFailure):
    """bot has not finished loading yet.
    """


class InsufficientPrivilege(commands.CheckFailure):
    """user does not have correct privileges.
    """


class IllegalChannel(commands.CheckFailure):
    """you cannot do that action in this channel.
    """


class ReportableError(Exception):
    """reportable error to append text for notifications to
    """
