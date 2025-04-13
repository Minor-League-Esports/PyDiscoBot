"""test frames functionality for pydisco bot
    """
from __future__ import annotations

import unittest
import discord
from pydiscobot.embed_frames import frame, admin, notification
from pydiscobot.types import admin_info


class TestFrames(unittest.TestCase):
    """test frames for pydisco bot
    """

    def test_get_frame(self):
        """test bot can compile and receive default frame
        """
        frm = frame.get_frame()
        self.assertTrue(isinstance(frm, discord.Embed))

    def test_get_admin_frame(self):
        """test bot can compile and receive admin frame
        """
        self.assertTrue(isinstance(admin.get_admin_frame(admin_info.AdminInfo()), discord.Embed))

    def test_get_notification_frame(self):
        """test bot can compile and receive notification frame
        """
        self.assertTrue(isinstance(notification.get_notification('bing bong'), discord.Embed))
