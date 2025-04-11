"""test class for pydisco bot
    """
from __future__ import annotations

import asyncio
import unittest
from .mock_bot import MockBot


class TestBot(unittest.TestCase):
    """test class for pydisco bot
    """

    def test_build(self):
        """test bot build without err
        """
        bot = MockBot.as_ready()
        self.assertTrue(bot.admin_info.initialized)
        self.assertIsNotNone(bot.admin_info.cycle_time)

    def test_admin_task(self):
        """test admin task by ticking
        """
        bot = MockBot.as_ready()
        self.assertIsNotNone(bot.tasker.by_name('AdminTask'))
        self.assertEqual(bot.admin_info.current_tick, 0)
        asyncio.run(bot.tasker.by_name('AdminTask').run())
        self.assertEqual(bot.admin_info.current_tick, 1)
