"""PyDiscoBot built-in unittest types
Provide mock data and meta schemes to allow bot to test
Such as MockGuild, MockMessage, MockUser, MockInteraction, etc
    """
from .mock_channel import MockChannel
from .mock_connection_state import MockConnectionState
from .mock_interaction import MockInteraction, MockInteractionResponse
from .mock_user import MockUser, MockUserData

__version__ = '1.1.3'

__all__ = (
    'MockChannel',
    'MockConnectionState',
    'MockInteraction',
    'MockInteractionResponse',
    'MockUser',
    'MockUserData',
)
