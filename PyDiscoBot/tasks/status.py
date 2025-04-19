"""run administrative functions for the bot
    i.e. 'alive' status channel or any additional funcs required
    """
from __future__ import annotations


from typing import Optional, TYPE_CHECKING
import discord

from .. import channels, frame
from .. import task

if TYPE_CHECKING:
    from ..types import BaseBot


class StatusTask(task.Task):
    """Status task for :class:`pydiscobot.Bot`.

    Manages updating :class:`Status`.
    Also manages posting infos to admin :class:`discord.TextChannel` (if it exists).

    .. ------------------------------------------------------------

    Attributes
    -----------
    message: :class:`discord.Message`
        get the :class:`discord.Message` this :class:`Task` is managing.

    .. ------------------------------------------------------------
    """

    def __init__(self,
                 parent: BaseBot):
        super().__init__(parent)
        self._msg: Optional[discord.Message] = None

    @property
    def message(self) -> Optional[discord.Message]:
        """get the :class:`discord.Message` this :class:`Task` is managing.

        Returns:
            :class:`discord.Message` | :type:`None`: :class:`AdminTask`'s message.
        """

    async def _msg_ch(self):
        if not self.parent.status.channels.admin:
            self.logger.warning('no admin channel available...')
            return

        if self._msg:
            try:
                await self._msg.edit(embed=frame.get_status_frame(self.parent.status))
                return
            except (discord.errors.NotFound, AttributeError, discord.errors.DiscordServerError):
                self.logger.info('creating new message...')

        await channels.clear_messages(self.parent.status.channels.admin, 100)
        self._msg = await self.parent.status.channels.admin.send(
            embed=frame.get_status_frame(self.parent.status)
        )

    async def run(self):
        """run the admin task
        """
        await self._msg_ch()
        self.parent.status.tick()
