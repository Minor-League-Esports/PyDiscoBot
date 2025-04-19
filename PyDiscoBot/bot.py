"""irox implimentation of Discord.Bot class
    """
from __future__ import annotations


import asyncio
import datetime
from io import StringIO
import os
import sys
from typing import Optional, Union
import unittest


import discord
from discord import app_commands
from discord.ext import commands

from .const import ERR_BAD_PRV, ERR_RATE_LMT
from .channels import find_ch
from .commands import Commands
from .frame import get_notification_frame
from .log import logger
from .tasks import StatusTask
from .types import (
    Status,
    BaseBot,
    Tasker,
    ReportableError
)


class Bot(BaseBot, commands.Bot):
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
                 command_cogs: list[commands.Cog]):

        super().__init__(command_prefix=command_prefix,
                         intents=bot_intents)

        self._logger = logger(self.__class__.__name__)
        self._status = Status()
        self._tasker = Tasker()
        self._tasker.append(StatusTask(self))

        command_cogs.extend(Commands)
        for cog in command_cogs:
            asyncio.run(self.add_cog(cog(self)))

        self.tree.on_error = self.on_tree_error

    async def notify(self,
                     message: Union[str, Exception]) -> None:
        """Send a message to the `Bot`'s notification channel (if exists).

        If there is no notification channel, the `message` is instead printed to console.

        .. ------------------------------------------------------------

        Arguments
        -----------
        message Union[:class:`str`, :class:`Exception`]
            The message to be sent. Will be wrapped in a generic :class:`discord.Embed`.

        """
        if not message:
            return

        if not self.status.channels.notification:
            print(message)
            return

        await self.send_notification(dest=self.status.channels.notification,
                                     msg=message,
                                     as_reply=False)

    async def on_ready(self,
                       suppress_task=False) -> None:
        """method called by discord api when the bot connects to the gateway server and is ready for production

        .. ------------------------------------------------------------

        Arguments
        -----------
        suppress_task :type:`bool`
            Whether to suppress the periodic task or not. Defaults to `False`.
        """
        self._logger.info('PyDiscoBot on_ready...')
        if self._status.initialized:
            self._logger.warning('already initialized!')
            return

        admin_channel_token = os.getenv('ADMIN_CHANNEL')
        notification_channel_token = os.getenv('NOTIFICATION_CHANNEL')

        if admin_channel_token:
            self._logger.info('initializing admin channel...')
            self._status.channels.admin = find_ch(self.guilds,
                                                  admin_channel_token)
            if not self._status.channels.admin:
                self._logger.warning('admin channel not found...')

        if notification_channel_token:
            self._logger.info('initializing notification channel...')
            self._status.channels.notification = find_ch(self.guilds,
                                                         notification_channel_token)
            if not self._status.channels.notification:
                self._logger.warning('notification channel not found...')

        self._status.initialized = True
        self._logger.info("POST -> %s", datetime.datetime.now().strftime('%c'))

        if not suppress_task:
            self._tasker.run.change_interval(seconds=self.status.cycle_time)
            self._tasker.run.start()

    async def on_tree_error(self,
                            interaction: discord.Interaction,
                            error: app_commands.AppCommandError):
        """override of parent error method

        .. ------------------------------------------------------------

        Arguments
        -----------
        interaction :class:`discord.Interaction`
            `interaction` that caused the error.
        error :class:`app_commands.AppCommandError`
            Error raised.
        """
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(ERR_RATE_LMT)
            return

        elif isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(ERR_BAD_PRV)
            return

        elif isinstance(error, discord.app_commands.CommandInvokeError):
            if isinstance(error.original, ReportableError):
                await self.send_notification(interaction,
                                             str(error.original),
                                             as_followup=False)
                return

        await self.notify(error)
        raise error

    async def send_notification(self,
                                dest: Union[commands.Context, discord.Interaction, discord.TextChannel],
                                msg: str,
                                as_reply: Optional[bool] = False,
                                as_followup: Optional[bool] = False) -> None:
        """Send a notification `embed` to a specified `Channel`, `Context` or `Interaction`.

        .. ------------------------------------------------------------

        Arguments
        -----------
        dest Union[:class:`commands.Context`, :class:`discord.Interaction`, :class:`discord.TextChannel`]
            The destination to send a notification `Embed` to.

        msg :type:`str`
            The message to be sent in the body of the notification `Embed`.

        as_reply Optional[:class:`bool`]
            Defaults to ``False``. Set if you want the bot to reply with the message.

            This works with both `Context` and `Interaction`.

        as_followup Optional[:class:`bool`]
            Defaults to ``False``. Set if you want the bot to followup to a defer.

            This ``only`` works with an `Interaction` that has been deferred.

            Otherwise, this WILL raise an `Exception`

        """
        embed = get_notification_frame(msg)

        if isinstance(dest, commands.Context):
            if as_reply and dest.author is not None:
                await dest.reply(embed=embed)
            else:
                await dest.send(embed=embed)

        elif isinstance(dest, discord.Interaction):
            if as_followup:
                await dest.followup.send(embed=embed)
            else:
                try:
                    await dest.response.send_message(embed=embed)
                except discord.errors.InteractionResponded:
                    await dest.followup.send(embed=embed)

        elif isinstance(dest, discord.TextChannel):
            await dest.send(embed=embed)

        else:
            raise TypeError(
                'Invalid type was passed.\n'
                'Destination must be of type `Context`, `Interaction` or `TextChannel`.')


class TestBaseBot(unittest.TestCase):
    """test case for `BaseBot`
    """

    def test_notify(self):
        """test bot notify
        """
        bot = Bot('!', discord.Intents(8), [])

        def notify_callback(**kwargs):
            ...

        capt = StringIO()
        sys.stdout = capt

        asyncio.run(bot.notify(None))
        self.assertEqual(capt.getvalue(), '')

        value = 'This is a notification!'
        asyncio.run(bot.notify(value))
        self.assertEqual(capt.getvalue(), value)

        bot.status.channels.notification = notify_callback

        sys.stdout = sys.__stdout__
