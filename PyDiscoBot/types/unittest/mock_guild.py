"""mock Discord Guild
    """
import discord
from discord.state import ConnectionState


class MockGuild(discord.Guild):
    """mock Discord Guild
    """
    guild_member_count = 69
    guild_name = 'Test Guild'
    guild_id = 1234567890
    guild_owner_id = 123123123123
    mock_data = {
        'member_count': guild_member_count,
        'name': guild_name,
        'verification_level': 0,
        'notification_level': 0,
        'id': guild_id,
        'owner_id': guild_owner_id,
    }

    def __init__(self):
        super().__init__(data=MockGuild.mock_data, state=ConnectionState(dispatch=None,
                                                                         handlers=None,
                                                                         hooks=None,
                                                                         http=None))
