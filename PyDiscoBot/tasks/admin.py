"""run administrative functions for the bot
    i.e. 'alive' status channel or any additional funcs required
    """
from __future__ import annotations

from datetime import datetime
from typing import Optional
import discord
import pydiscobot
from pydiscobot.types import Task
from pydiscobot.services import channels
from pydiscobot import embed_frames


class AdminTask(Task):
    """Administrative task for :class:`pydiscobot.Bot`.

    Manages updating :class:`AdminInfo`.
    Also manages posting infos to admin :class:`discord.TextChannel` (if it exists).

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: :class:`pydiscobot.Bot`
        The bot this task belongs to.

    .. ------------------------------------------------------------

    Attributes
    -----------
    message: :class:`discord.Message`
        get the :class:`discord.Message` this :class:`Task` is managing.

    .. ------------------------------------------------------------
    """

    def __init__(self,
                 parent: pydiscobot.Bot):
        super().__init__(parent)
        self._msg: Optional[discord.Message] = None

    @property
    def message(self) -> Optional[discord.Message]:
        """get the :class:`discord.Message` this :class:`Task` is managing.

        Returns:
            :class:`discord.Message` | :type:`None`: :class:`AdminTask`'s message.
        """

    async def _msg_ch(self):
        if not self.parent.admin_info.channels.admin:
            self.logger.warning('no admin channel available...')
            return

        if self._msg:
            try:
                await self._msg.edit(embed=embed_frames.get_admin_frame(self.parent.admin_info))
                return
            except (discord.errors.NotFound, AttributeError, discord.errors.DiscordServerError):
                self.logger.info('creating new message...')

        await channels.clear_messages(self.parent.admin_info.channels.admin, 100)
        self._msg = await self.parent.admin_info.channels.admin.send(
            embed=embed_frames.get_admin_frame(self.parent.admin_info)
        )

    def _time(self):
        """ time function
        """
        self.parent.admin_info.last_time = datetime.now()

    async def _admin(self):
        """ periodic task admin
        """
        self.parent.admin_info.current_tick += 1
        self._time()

    async def run(self):
        """run the admin task
        """
        await self._msg_ch()
        await self._admin()
