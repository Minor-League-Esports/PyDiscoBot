"""mock Discord Member
    """
import discord
from .mock_guild import MockGuild
from .mock_connection_state import MockConnectionState


class MockMember(discord.Member):
    """mock Discord Member
    """
    member_id = 69420
    member_name = 'Big Doinkers Anon.'
    guild = MockGuild()
    connection = MockConnectionState()

    def __init__(self,
                 name: str | None = None,
                 memid: int | None = None,
                 guild: discord.Guild | None = None):
        data = {
            'name': MockMember.member_name if not name else name,
            'guild': MockMember.guild if not guild else guild,
            'roles': [],
            'flags': 0,
            'user': {
                'username': MockMember.member_name if not name else name,
                'discriminator': 'your mom?',
                'avatar': None,
                'global_name': None,
                'id': MockMember.member_id if not memid else memid,
                'bot': False,
                'system': False,
                'mfa_enabled': False,
                'locale': 'en-US',
                'verified': False,
                'email': None,
                'flags': 0,
                'premium_type': 0,
                'public_flags': 0,
            }
        }
        super().__init__(data=data, guild=data['guild'], state=MockMember.connection)
