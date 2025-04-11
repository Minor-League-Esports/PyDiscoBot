"""make-shift interaction datas to support unit testing
    """


class MockInteractionResponse:
    """make-shift interaction response to support unit-testing
    """

    def __init__(self,
                 send_message_cb: callable):
        self.send_message: callable = send_message_cb


class MockInteraction:
    """make-shift interaction to support unit-testing
    """

    def __init__(self,
                 send_message_cb: callable):
        self.response: MockInteractionResponse = MockInteractionResponse(send_message_cb)
