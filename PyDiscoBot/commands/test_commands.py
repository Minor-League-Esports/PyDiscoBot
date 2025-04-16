"""test commands for pydisco bot
    """
from __future__ import annotations


import asyncio
from typing import Optional
import unittest
import discord
from discord.state import ConnectionState
from discord.ext import commands


from .clearchannel import ClearChannel
from .datetounix import DateToUnix, ERR
from .echo import Echo
from .help import Help
from .sync import Sync


__all__ = (
    'MockGuild',
    'MockChannel',
    'MockInteractionResponse',
    'MockInteraction',
    'TestCommands',
)


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


class MockChannel(discord.TextChannel):
    """mock Discord Text Channel
    """
    channel_id = 69420
    channel_name = 'Big Doinkers Anon.'
    guild = MockGuild()
    state = discord.state.ConnectionState(dispatch=None,
                                          handlers=None,
                                          hooks=None,
                                          http=None)

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

    async def delete_messages(self,
                              *args,
                              **kwargs):
        """dummy method
        """

    async def history(self,
                      *args,
                      **kwargs):
        """dummy method
        """
        for _ in range(0, 0):
            yield None


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


class TestCommands(unittest.TestCase):
    """test commands for pydisco bot
    """

    def test_clearchannel(self):
        """test clearchannel command
        """
        cog = ClearChannel()
        self.assertIsNotNone(cog)

        cmd = next((x for x in cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(cmd)

        setattr(self, 'msgs_deleted', 0)

        # check it doesn't err
        async def test_cb(*_, **__):
            setattr(self, 'msgs_deleted', getattr(self, 'msgs_deleted')+1)

        interaction = MockInteraction()
        interaction.channel.delete_messages = test_cb

        asyncio.run(cmd.callback(self=cmd,
                                 interaction=interaction,
                                 message_count=10))

        self.assertEqual(getattr(self, 'msgs_deleted'), 1)

        # check upper level err
        with self.assertRaises(ValueError) as context:
            asyncio.run(cmd.callback(self=cmd,
                                     interaction=MockInteraction(),
                                     message_count=250))

        self.assertTrue(isinstance(context.exception, ValueError))

        # check lwr level err
        with self.assertRaises(ValueError) as context:
            asyncio.run(cmd.callback(self=cmd,
                                     interaction=MockInteraction(),
                                     message_count=0))

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_datetounix(self):
        """test datetounix command
        """
        cog = DateToUnix()
        self.assertIsNotNone(cog)

        cmd = next((x for x in cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(cmd)

        async def test_callback_succeed(embed):
            self.assertTrue(isinstance(embed, discord.Embed))

        async def test_callback_fail(embed):
            self.assertEqual(ERR, embed)

        # create dummy interaction
        # run to validate command sends ERR
        asyncio.run(cmd.callback(self=cmd,
                                 interaction=MockInteraction(test_callback_fail),
                                 year='a',
                                 month='b',
                                 day='c',
                                 hour='d',
                                 minute='e',
                                 second='f'))

        # if we know it errs, lets check that it DOESNT err
        asyncio.run(cmd.callback(self=cmd,
                                 interaction=MockInteraction(test_callback_succeed),
                                 year='25',
                                 month='8',
                                 day='16',
                                 hour='12',
                                 minute='00',
                                 second='00'))

    def test_echo(self):
        """test echo command
        """
        cog = Echo()
        self.assertIsNotNone(cog)

        cmd = next((x for x in cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(cmd)

        sent_value = 'echo these nutz'

        async def test_callback(message):
            self.assertEqual(sent_value, message)

        # create dummy interaction
        # run the command to validate at least an echo works with a built bot
        asyncio.run(cmd.callback(self=cmd,
                                 interaction=MockInteraction(test_callback),
                                 message=sent_value))

    def test_help(self):
        """test help command
        """
        cog = Help()
        self.assertIsNotNone(cog)

        cmd = next((x for x in cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(cmd)

        async def test_callback(embed):
            self.assertTrue(isinstance(embed, discord.Embed))

        # create dummy interaction
        # run the command to validate at least an echo works with a built bot
        asyncio.run(cmd.callback(self=cmd,
                                 interaction=MockInteraction(test_callback)))

    def test_sync(self):
        """test sync command
        """
        bot = commands.Bot('!', intents=discord.Intents(0))
        cog = Sync(bot)
        cog._parent = bot
        self.assertIsNotNone(cog)

        cmd = next((x for x in cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(cmd)

        # check err raises by discord package
        # this `should` err anyways, we've made a mock struct after all
        with self.assertRaises(discord.app_commands.errors.MissingApplicationID) as context:
            asyncio.run(cmd.callback(self=cog,
                                     interaction=MockInteraction()))

        self.assertTrue(isinstance(context.exception, discord.app_commands.errors.MissingApplicationID))
