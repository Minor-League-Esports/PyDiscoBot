"""PyDiscoBot built-in types
    """
from . import (
    bot,
    cog,
    embed_field,
    err,
    pagination,
    status,
    task,
    tasker,
)

from .status import Status
from .bot import BaseBot
from .cog import BaseCog
from .embed_field import EmbedField
from .err import BotNotLoaded, IllegalChannel, InsufficientPrivilege, ReportableError
from .pagination import Pagination, InteractionPagination
from .task import BaseTask
from .tasker import Tasker

__version__ = '1.1.4'

__all__ = (
    'bot',
    'cog',
    'embed_field',
    'err',
    'pagination',
    'status',
    'task',
    'tasker',
    'Status',
    'BaseBot',
    'BaseCog',
    'EmbedField',
    'BotNotLoaded',
    'IllegalChannel',
    'InsufficientPrivilege',
    'ReportableError',
    'Pagination',
    'InteractionPagination',
    'BaseTask',
    'Tasker',
)
