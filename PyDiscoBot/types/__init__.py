"""PyDiscoBot built-in types
    """

from .admin_info import AdminInfo
from .cmd import Cmd
from .embed_field import EmbedField
from .err import BotNotLoaded, IllegalChannel, InsufficientPrivilege, ReportableError
from .pagination import Pagination, InteractionPagination
from .task import Task
from .tasker import Tasker

__version__ = '1.1.2'

__all__ = (
    'AdminInfo',
    'BotNotLoaded',
    'Cmd',
    'EmbedField',
    'IllegalChannel',
    'InsufficientPrivilege',
    'Pagination',
    'InteractionPagination',
    'ReportableError',
    'Task',
    'Tasker',
)
