"""mock Discord Message
    """
import datetime
from typing import Optional, TypedDict, Union
from typing_extensions import NotRequired
import discord
from .mock_connection_state import MockConnectionState
from .mock_channel import MockChannel
from .mock_user import MockUserData


class MockMessageData(TypedDict):
    """mock message data
    """
    id: int
    author: discord.User
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: list[discord.User]
    mention_roles: list[int]
    attachments: list[discord.Attachment]
    embeds: list[discord.Embed]
    pinned: bool
    type: discord.MessageType
    member: NotRequired[discord.Member]
    mention_channels: NotRequired[list[dict]]
    reactions: NotRequired[list[discord.Reaction]]
    nonce: NotRequired[Union[int, str]]
    webhook_id: NotRequired[int]
    activity: NotRequired[dict]
    application: NotRequired[discord.MessageApplication]
    application_id: NotRequired[int]
    message_reference: NotRequired[discord.MessageReference]
    flags: NotRequired[int]
    sticker_items: NotRequired[list[discord.StickerItem]]
    referenced_message: NotRequired[Optional[discord.Message]]
    interaction: NotRequired[discord.MessageInteraction]
    components: NotRequired[list[discord.Component]]
    position: NotRequired[int]
    role_subscription_data: NotRequired[dict]

    @classmethod
    def generic(cls):
        """get data as generic

        Returns:
            dict: data
        """
        return cls({
            'id': 123456,
            'author': MockUserData.generic(),
            'attachments': [],
            'embeds': [],
            'edited_timestamp': datetime.datetime.now().isoformat(),
            'type': discord.MessageType.chat_input_command,
            'pinned': False,
            'mention_everyone': False,
            'tts': False,
            'content': 'this is some content, right?',
        })


class MockMessage(discord.Message):
    """mock Discord Message
    """

    def __init__(self, *,
                 state=None,
                 channel=None,
                 data: MockMessageData = None):
        if not state:
            state = MockConnectionState()
        if not channel:
            channel = MockChannel()
        if not data:
            data = MockMessageData.generic()

        super().__init__(state=state, channel=channel, data=data)
