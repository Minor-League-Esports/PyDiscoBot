"""PyDiscoBot - a bot by irox
    """
from . import (
    commands,
    tasks,
    types,
    channels,
    const,
    frame,
    log,
    test_pydiscobot
)


from .bot import Bot
from .cog import Cog
from .task import Task
from .types import EmbedField, InteractionPagination

__version__ = "1.1.4"

__all__ = (
    'commands',
    'tasks',
    'types',
    'channels',
    'const',
    'frame',
    'log',
    'task',
    'test_pydiscobot',
    'Bot',
    'Cog',
    'EmbedField',
    'InteractionPagination',
    'Task',
)
