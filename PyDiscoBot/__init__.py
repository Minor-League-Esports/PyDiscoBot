"""PyDiscoBot - a bot by irox
    """

from .bot import Bot
from .types import BotNotLoaded, EmbedField, IllegalChannel, InsufficientPrivilege
from .types import ReportableError, Pagination, InteractionPagination
from .services import const, cmds
from .embed_frames import frame

__version__ = "1.1.2"

__all__ = (
    "Bot",
    'ReportableError',
    'IllegalChannel',
    'InsufficientPrivilege',
    'BotNotLoaded',
    "Pagination",
    "InteractionPagination",
    'const',
    'cmds',
    'frame',
    'EmbedField',
)
