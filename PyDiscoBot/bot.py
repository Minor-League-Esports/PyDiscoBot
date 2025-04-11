"""irox implimentation of Discord.Bot class
    """
from __future__ import annotations

import asyncio
import datetime
import os
from logging import Logger
from typing import Union
import discord
from discord.ext import commands as disco_commands
from discord import app_commands
from .embed_frames import get_notification
from .services import const, channels
from .services.cmds import Commands
from .services.log import logger
from .tasks.admin import AdminTask
from .types import AdminInfo, IllegalChannel, BotNotLoaded, ReportableError
from .types import InsufficientPrivilege, Tasker


class Bot(disco_commands.Bot):
    """Represents a Discord bot, wrapped with built-in logic

    This class is a subclass of :class:`discord.ext.commands.Bot` and as a result
    anything that you can do with a :class:`discord.ext.commands.Bot` you can do with
    this bot. To note, :class:`discord.ext.commands.Bot` is a subclass of
     :class:`discord.Client`, meaning this bot can also perform all :class:`discord.Client` tasks.

    Arguments
    -----------
    command_prefix: Union[:class:`str`, :class:`list`]
        A legacy command prefix. Supports :class:`callable` by default.
        However, this is not the intended design strategy.
        We consume a string for a prefix to allow for certain commands,
        such as 'Sync' but most other commands are built only for app_commands
        or 'Slash' commands.
    bot_intents: :class:`discord.Intents`
        The discord intents this bot has been registered for.
        This should reflect the permissions the bot has in the server it would be operating in.
        The Discord Developer Portal has a tool to help create the integer required for this class.
    command_cogs: list[:class:`discord.ext.commands.Cog`]
        A list of commands to append to this bot when initializing.
        During the __init__ call, this list will be appended asyncronously to the bot's cogs.
        After modifying what commands a bot has access to, or the parameters of the commands, 
        a 'sync' command will be required to sync the bot tree.

    Examples
    ----------

        Initialize a bot with a few custom made command cogs ::

            import os
            import discord
            import dotenv
            from pydiscobot import Bot
            from my_command_module import my_commands
            from their_command_module import their_commands


            if __name__ == '__main__':
                dir_path = os.path.dirname(os.path.realpath(__file__))
                dotenv.load_dotenv(f'{dir_path}/.env')
                intents = discord.Intents(8)
                bot = Bot('!',
                          intents,
                          [my_commands, their_commands])
                bot.run(os.getenv('DISCORD_TOKEN'))
    """

    def __init__(self,
                 command_prefix: Union[str, list],
                 bot_intents: discord.Intents,
                 command_cogs: list[disco_commands.Cog]):
        super().__init__(command_prefix=command_prefix,
                         intents=bot_intents)

        self._logger = logger(self.__class__.__name__)
        self.logger.info('initializing...')

        self._admin_info = AdminInfo()
        self._tasker = Tasker()
        self._tasker.append(AdminTask(self))

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
    def logger(self) -> Logger:
        """get logger of the bot

        Returns:
            Logger: logger
        """
        return self._logger

    @property
    def tasker(self) -> Tasker:
        """get this bot's task list

        Returns:
            Tasker: task list (Tasker)
        """
        return self._tasker

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
                await ctx.reply(embed=get_notification(text))
            else:
                await ctx.send(embed=get_notification(text))

        elif isinstance(ctx, discord.Interaction):
            if as_followup:
                await ctx.followup.send(embed=get_notification(text))
            else:
                try:
                    return await ctx.response.send_message(embed=get_notification(text))
                except discord.errors.InteractionResponded:
                    return await ctx.followup.send(embed=get_notification(text))

        elif isinstance(ctx, discord.TextChannel):
            await ctx.send(embed=get_notification(text))

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
        """method called by discord api when the bot connects to the gateway server and is ready for production

        Args:
            suppress_task (bool, optional): run periodic task or not. Defaults to False.
        """
        self._logger.info('PyDiscoBot on_ready...')
        if self._admin_info.initialized:
            self._logger.warning('already initialized!')
            return

        admin_channel_token = os.getenv('ADMIN_CHANNEL')
        notification_channel_token = os.getenv('NOTIFICATION_CHANNEL')

        if admin_channel_token:
            self._logger.info('initializing admin channel...')
            self._admin_info.channels.admin = channels.find_ch(self.guilds,
                                                               admin_channel_token)
            if not self._admin_info.channels.admin:
                self._logger.warning('admin channel not found...')

        if notification_channel_token:
            self._logger.info('initializing notification channel...')
            self._admin_info.channels.notification = channels.find_ch(self.guilds,
                                                                      notification_channel_token)
            if not self._admin_info.channels.notification:
                self._logger.warning('notification channel not found...')

        self._admin_info.initialized = True
        self._logger.info("POST -> %s", datetime.datetime.now().strftime('%c'))

        if not suppress_task:
            self._tasker.run.change_interval(seconds=self.admin_info.cycle_time)
            self._tasker.run.start()
