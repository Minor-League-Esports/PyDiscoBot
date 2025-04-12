"""make-shift interaction datas to support unit testing
    """
from typing import Optional
from .mock_channel import MockChannel


class MockInteractionResponse:
    """make-shift interaction response to support unit-testing
    """

    def __init__(self,
                 send_message_cb: Optional[callable] = None):
        self.send_message: callable = send_message_cb

    async def defer(self):
        """dummy callback for interaction response -> defer
        """


class MockInteraction:
    """make-shift interaction to support unit-testing
    """

    def __init__(self,
                 send_message_cb: Optional[callable] = None):
        self.channel = MockChannel()
        self.response: MockInteractionResponse = MockInteractionResponse(send_message_cb)
