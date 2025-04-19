"""test task functionality for pydisco bot
    """
from __future__ import annotations

import asyncio
import unittest


import discord


from .. import bot


class TestTasks(unittest.TestCase):
    """test task functionality for pydisco bot
    """

    def test_admin_task(self):
        """test status task by ticking
        """
        _bot = bot.Bot('!', discord.Intents(8), [])
        self.assertIsNotNone(_bot.tasker.by_name('StatusTask'))
        self.assertEqual(_bot.status.current_tick, 0)
        asyncio.run(_bot.tasker.by_name('StatusTask').run())
        self.assertEqual(_bot.status.current_tick, 1)
