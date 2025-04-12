"""test frames functionality for pydisco bot
    """
import unittest
import discord
from pydiscobot import embed_frames
from pydiscobot.types import AdminInfo


class TestFrames(unittest.TestCase):
    """test frames for pydisco bot
    """

    def test_get_frame(self):
        """test bot can compile and receive default frame
        """
        self.assertTrue(isinstance(embed_frames.get_frame(), discord.Embed))

    def test_get_admin_frame(self):
        """test bot can compile and receive admin frame
        """
        self.assertTrue(isinstance(embed_frames.get_admin_frame(AdminInfo()), discord.Embed))

    def test_get_notification_frame(self):
        """test bot can compile and receive notification frame
        """
        self.assertTrue(isinstance(embed_frames.get_notification('bing bong'), discord.Embed))
