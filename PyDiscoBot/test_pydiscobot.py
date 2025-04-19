"""testing suite for PyDiscoBot
    """
from __future__ import annotations


import asyncio
import unittest
import discord


from .bot import Bot
from .task import Task


__all__ = (
    'TestPyDiscoBot',
)


class TestPyDiscoBot(unittest.TestCase):
    """test pydiscobot suite
    """

    def test_task_class(self):
        """test task class
        """
        bot = Bot('!', discord.Intents(8), [])
        task = Task(bot)
        self.assertIsNotNone(task)
        self.assertEqual(task.name, 'Task')
        with self.assertRaises(NotImplementedError) as context:
            asyncio.run(task.run())

        self.assertTrue(isinstance(context.exception, NotImplementedError))
