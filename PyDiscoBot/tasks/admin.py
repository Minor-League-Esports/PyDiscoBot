"""run administrative functions for the bot
    i.e. 'alive' status channel or any additional funcs required
    """

from datetime import datetime
import discord
from ..types.task import Task
from ..services.channels import clear_messages
from ..embed_frames import admin


class AdminTask(Task):
    """admin task for generating channel embeds and mainting run info
    """

    def __init__(self,
                 parent):
        super().__init__(parent)
        self._msg: discord.Message | None = None

    async def _msg_ch(self):
        if not self.parent.admin_info.channels.admin:
            self.logger.warning('no admin channel available...')
            return

        if self._msg:
            try:
                await self._msg.edit(embed=admin(self.parent.admin_info))
                return
            except (discord.errors.NotFound, AttributeError, discord.errors.DiscordServerError):
                self.logger.info('creating new message...')

        await clear_messages(self.parent.admin_info.channels.admin, 100)
        self._msg = await self.parent.admin_info.channels.admin.send(embed=admin(self.parent.admin_info))

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
