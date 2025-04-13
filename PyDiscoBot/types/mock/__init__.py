"""PyDiscoBot built-in test types
Provide mock data and meta schemes to allow bot to test
Such as MockGuild, MockMessage, MockUser, MockInteraction, etc
    """
from . import mock_bot
from . import mock_channel
from . import mock_connection_state
from . import mock_guild
from . import mock_interaction
from . import mock_member
from . import mock_message
from . import mock_user

__version__ = '1.1.4'

__all__ = (
    'mock_bot',
    'mock_channel',
    'mock_connection_state',
    'mock_guild',
    'mock_interaction',
    'mock_member',
    'mock_message',
    'mock_user',
)
