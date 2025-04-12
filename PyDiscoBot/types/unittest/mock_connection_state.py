"""mock connection state to be used for unit testing
    """
from discord.state import ConnectionState


class MockConnectionState(ConnectionState):
    """mock connection state to be used for unit testing
    """

    def __init__(self):
        super().__init__(dispatch=None, handlers=None, hooks=None, http=None)
