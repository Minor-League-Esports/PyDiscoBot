"""mock Discord User
    """
from typing import Optional, Literal, TypedDict
import discord
from .mock_connection_state import MockConnectionState


class MockUserData(TypedDict):
    """mock message data
    """
    username: Optional[str]
    discriminator: Optional[str]
    avatar: None
    global_name: None
    id: int
    bot: bool
    system: bool
    mfa_enabled: bool
    locale: str
    verified: bool
    email: str
    flags: int
    premium_type: Literal[0, 1, 2]
    public_flags: int

    @classmethod
    def generic(cls):
        """get data as generic

        Returns:
            dict: data
        """
        return cls({
            'username': 'beef',
            'discriminator': 'your mom?',
            'avatar': None,
            'global_name': None,
            'id': 696969420,
            'bot': False,
            'system': False,
            'mfa_enabled': False,
            'locale': 'en-US',
            'verified': False,
            'email': None,
            'flags': 0,
            'premium_type': 0,
            'public_flags': 0,
        })


class MockUser(discord.User):
    """mock Discord User
    """

    def __init__(self,
                 data: Optional[dict]):
        if not data:
            data = MockUserData.generic()
        super().__init__(state=MockConnectionState(), data=data)
