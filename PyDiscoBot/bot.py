import asyncio
import datetime
import os
import discord
from discord.ext import commands as disco_commands
from discord import app_commands
from .embed_frames import notification
from .services import const, channels
from .services.cmds import Commands
from .services.log import logger
from .tasks.periodic_task import PeriodicTask
from .tasks.admin import AdminTask
from .types import AdminInfo, IllegalChannel, BotNotLoaded, ReportableError
from .types import InsufficientPrivilege


class Bot(discord.ext.commands.Bot):
    """ bot by irox
    """

    def __init__(self,
                 command_prefix: str | list,
                 bot_intents: discord.Intents | None,
                 command_cogs: list[disco_commands.Cog]):
        super().__init__(command_prefix=command_prefix,
                         intents=bot_intents,
                         help_command=None,
                         case_insensitive=True)

        self.logger = logger(__name__)
        self.logger.info('initializing bot...')

        try:
            self._server_icon = os.getenv('SERVER_ICON')
        except ValueError:
            self._server_icon = None

        self._admin_info = AdminInfo(
            version=os.getenv('VERSION'),
            boot_time=datetime.datetime.now(),
            last_time=datetime.datetime.now(),
            cycle_time=os.getenv('CYCLE_TIME'),
        )
        self._periodic_task = PeriodicTask(self)
        self._admin_task = None

        command_cogs.extend(Commands)
        for cog in command_cogs:
            asyncio.run(self.add_cog(cog(self)))

        self.tree.on_error = self.on_tree_error

    @property
    def admin_info(self) -> AdminInfo:
        """ return admin info for the bot
        """
        return self._admin_info

    @property
    def server_icon(self) -> str:
        """get server icon for this bot

        Returns:
            str: icon url
        """
        return self._server_icon

    async def notify(self,
                     message: str | Exception) -> None:
        """ Helper function to send error or notification messages to notify channel with a single parameter.\n
        **If a notification channel does not exist**, the notification is printed to console instead\n
        **param message**: message to report\n
        **returns**: None\n
        """
        if not message:
            return
        if not self._admin_info.channels.notification:
            return print(message)
        await self.send_notification(ctx=self._admin_info.channels.notification,
                                     text=message,
                                     as_reply=False)

    async def send_notification(self,
                                ctx: discord.abc.Messageable,
                                text: str,
                                as_reply: bool = False,
                                as_followup: bool = False) -> None:
        """ Helper function to send notifications
        """
        if isinstance(ctx, discord.ext.commands.Context):
            if as_reply and ctx.author is not None:
                await ctx.reply(embed=notification(text))
            else:
                await ctx.send(embed=notification(text))

        elif isinstance(ctx, discord.Interaction):
            if as_followup:
                await ctx.followup.send(embed=notification(text))
            else:
                try:
                    return await ctx.response.send_message(embed=notification(text))
                except discord.errors.InteractionResponded:
                    return await ctx.followup.send(embed=notification(text))

        elif isinstance(ctx, discord.TextChannel):
            await ctx.send(embed=notification(text))

    async def on_command_error(self,
                               ctx: discord.ext.commands.Context,
                               error) -> None:
        """ Override of discord.Bot on_command_error
            If CommandNotFound, simply reply to the user of the error.\n
            If not, raise the error naturally\n
            """
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.reply(const.ERR_BAD_CMD)
        elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.reply(const.ERR_MSG_PARAM)
        elif isinstance(error, discord.HTTPException):
            await ctx.reply(const.ERR_RATE_LMT)
        elif isinstance(error, InsufficientPrivilege):
            await ctx.reply(const.ERR_BAD_PRV)
        elif isinstance(error, IllegalChannel):
            await ctx.reply(const.ERR_BAD_CH)
        elif isinstance(error, BotNotLoaded):
            await ctx.reply(const.ERR_BOT_NL)
        elif isinstance(error, ReportableError):
            await ctx.reply(str(error))
        else:
            await self.notify(f'Error encountered:\n{str(error)}')
            raise error

    async def on_tree_error(self,
                            interaction: discord.Interaction,
                            error: app_commands.AppCommandError):
        """override of parent error method

        Args:
            interaction (discord.Interaction): interaction that caused the error
            error (app_commands.AppCommandError): error raised
        """
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(const.ERR_RATE_LMT)
            return

        elif isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(const.ERR_BAD_PRV)
            return

        elif isinstance(error, discord.app_commands.CommandInvokeError):
            if isinstance(error.original, ReportableError):
                await self.send_notification(interaction,
                                             str(error.original),
                                             as_followup=False)
                return

        await self.notify(error)
        raise error

    async def on_ready(self,
                       suppress_task=False) -> None:
        """ Method that is called by discord when the bot connects to the supplied guild\n
        **param suppress_task**: if True, do NOT run periodic task at the end of this call\n
        **returns**: None\n
        """
        self.logger.info('PyDiscoBot on_ready...')
        if self._admin_info.initialized:
            self.logger.warning('already initialized!')
            return

        admin_channel_token = os.getenv('ADMIN_CHANNEL')
        notification_channel_token = os.getenv('NOTIFICATION_CHANNEL')

        if admin_channel_token:
            self.logger.info('initializing admin channel...')
            self._admin_info.channels.admin = channels.find_ch(self.guilds,
                                                               admin_channel_token)
            if not self._admin_info.channels.admin:
                self.logger.warning('admin channel not found...')
            else:
                self._admin_task = AdminTask(self)
                self._periodic_task.on_tick.append(self._admin_task.run)

        if notification_channel_token:
            self.logger.info('initializing notification channel...')
            self._admin_info.channels.notification = channels.find_ch(self.guilds,
                                                                      notification_channel_token)
            if not self._admin_info.channels.notification:
                self.logger.warning('notification channel not found...')

        self._admin_info.initialized = True
        self.logger.info("POST -> %s", datetime.datetime.now().strftime('%c'))

        if not suppress_task:
            self.logger.info('beginning periodic task...')
            self._periodic_task.on_tick.append(self.on_task)
            self._periodic_task.change_interval(
                seconds=self.admin_info.cycle_time)
            self._periodic_task.run.start()

    async def on_task(self) -> None:
        """ callback method for periodic task to call during it's interval\n
            override this as needed
        **returns**: None\n
        """
        self.logger.info('PyDiscoBot on_task | tick: %s',
                         str(self.admin_info.current_tick))
