"""test commands for pydisco bot
    """
import asyncio
import unittest
import discord
from pydiscobot.types.unittest import MockInteraction
from pydiscobot.services.cmds.datetounix import ERR
from tests.types import MockBot


class TestCommands(unittest.TestCase):
    """test commands for pydisco bot
    """

    def test_datetounix(self):
        """test datetounix command
        """
        bot = MockBot.as_ready()

        cog = bot.cogs['DateToUnix']
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
        bot = MockBot.as_ready()

        echo_cog = bot.cogs['Echo']
        self.assertIsNotNone(echo_cog)

        echo_cmd = next((x for x in echo_cog.get_app_commands() if x is not None), None)
        self.assertIsNotNone(echo_cmd)

        sent_value = 'echo these nutz'

        async def test_callback(message):
            bot.logger.info(message)  # nice
            self.assertEqual(sent_value, message)

        # create dummy interaction
        # run the command to validate at least an echo works with a built bot
        asyncio.run(echo_cmd.callback(self=echo_cmd,
                                      interaction=MockInteraction(test_callback),
                                      message=sent_value))
