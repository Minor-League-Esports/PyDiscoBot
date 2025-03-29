from datetime import datetime
import logging
import discord
from ..services.channels import clear_messages
from ..embed_frames import admin


class AdminTask:
    """admin task for generating channel embeds and mainting run info
    """

    def __init__(self,
                 parent):
        self._msg: discord.Message | None = None
        self.parent = parent
        self.logger = logging.getLogger(__name__)
        self._init_logging()

    def _init_logging(self):
        self.logger.setLevel(logging.INFO)

        cons = logging.StreamHandler()
        cons.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s')

        cons.setFormatter(formatter)
        self.logger.addHandler(cons)

        self.logger.info('logger initialized...')

    async def _msg_ch(self):
        if not self.parent.admin_info.channels.admin:
            self.logger.warning('no admin channel available...')
            return

        if self._msg:
            try:
                await self._msg.edit(embed=admin(self._ad_info))
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
        self.logger.info('running admin task...')
        await self._msg_ch()
        await self._admin()
