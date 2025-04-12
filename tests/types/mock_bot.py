"""mock Bot
    """
from __future__ import annotations

import asyncio
import os
from typing import Self
import discord
import dotenv
from pydiscobot.bot import Bot
from pydiscobot.types.unittest.mock_user import MockUserData
from pydiscobot.types.unittest.mock_connection_state import MockConnectionState


class MockBot(Bot):
    """Mock :class:`Bot` to be used in unittesting
    """

    @classmethod
    def as_mock(cls) -> Self:
        """get this bot as a generated mock bot

        Returns:
            Self: an instance of bot
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dotenv.load_dotenv(f'{dir_path}\\.testenv')
        intents = discord.Intents(8)
        # noinspection PyDunderSlots
        intents.guilds = True
        # noinspection PyDunderSlots
        intents.members = True
        # noinspection PyDunderSlots
        intents.message_content = True
        # noinspection PyDunderSlots
        intents.messages = True
        bot = cls('!', intents, [])
        data = MockUserData.generic()
        data['id'] = 12341234  # change this in case any checks on the default user happen against the bot
        bot._connection.user = discord.User(state=MockConnectionState(), data=data)
        return bot

    @classmethod
    def as_ready(cls) -> Self:
        """get this mock bot as an already initialized bot

        Returns:
            Self: initialized mock bot
        """
        x = cls.as_mock()
        asyncio.run(x.on_ready(True))
        return x
