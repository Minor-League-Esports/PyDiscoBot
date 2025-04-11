"""mock Discord Text Channel
    """
import discord
from .mock_guild import MockGuild
from .mock_connection_state import MockConnectionState


class MockChannel(discord.TextChannel):
    """mock Discord Text Channel
    """
    channel_id = 69420
    channel_name = 'Big Doinkers Anon.'
    guild = MockGuild()
    state = MockConnectionState()

    def __init__(self,
                 name: str | None = None,
                 chid: int | None = None,
                 guild: discord.Guild | None = None):
        data = {
            'id': MockChannel.channel_id if not chid else chid,
            'name': MockChannel.name if not name else name,
            'type': discord.channel.TextChannel,
            'position': 0,
            'guild': MockChannel.guild if not guild else guild
        }
        super().__init__(state=MockChannel.state, guild=data['guild'], data=data)
