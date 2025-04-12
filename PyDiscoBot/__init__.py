"""PyDiscoBot - a bot by irox
    """
from .bot import Bot
from .types import BotNotLoaded, EmbedField, IllegalChannel, InsufficientPrivilege
from .types import ReportableError, Pagination, InteractionPagination
from .services import const, cmds
from . import embed_frames

__version__ = "1.1.3"

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
    'embed_frames',
    'EmbedField',
)
