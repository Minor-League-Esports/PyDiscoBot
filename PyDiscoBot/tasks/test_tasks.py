"""test task functionality for pydisco bot
    """
from __future__ import annotations

import asyncio
import unittest
from pydiscobot.types.mock import mock_bot


class TestTasks(unittest.TestCase):
    """test task functionality for pydisco bot
    """

    def test_admin_task(self):
        """test admin task by ticking
        """
        bot = mock_bot.MockBot.as_ready()
        self.assertIsNotNone(bot.tasker.by_name('AdminTask'))
        self.assertEqual(bot.admin_info.current_tick, 0)
        asyncio.run(bot.tasker.by_name('AdminTask').run())
        self.assertEqual(bot.admin_info.current_tick, 1)
