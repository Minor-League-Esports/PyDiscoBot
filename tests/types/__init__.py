"""Types meant ONLY for unit testing, and do not belong in general production code
    """
from .bot import TestBot
from .mock_bot import MockBot


__version__ = "1.1.3"

__all__ = (
    'TestBot',
    'MockBot',
)
