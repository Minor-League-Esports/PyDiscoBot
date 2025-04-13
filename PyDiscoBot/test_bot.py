"""test class for pydisco bot
    """
from __future__ import annotations

import unittest
from pydiscobot.types.mock import mock_bot


class TestBot(unittest.TestCase):
    """test class for pydisco bot
    """

    def test_build(self):
        """test bot build without err
        """
        bot = mock_bot.MockBot.as_ready()
        self.assertTrue(bot.admin_info.initialized)
        self.assertIsNotNone(bot.admin_info.cycle_time)
        self.assertTrue(isinstance(bot.admin_info.cycle_time, int))
