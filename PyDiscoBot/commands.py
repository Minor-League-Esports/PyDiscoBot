#!/usr/bin/env python
""" Minor League E-Sports Bot Commands
# Author: irox_rl
# Purpose: General Functions and Commands
# Version 1.0.5
#
# v1.0.5 - remove err string (unused anyways)
#           hide a few commands
#           update help function for pagination
"""

# local imports #
from .pagination import Pagination

# non-local imports
import datetime
import discord
from discord.ext import commands
import time


class Commands(commands.Cog):
    def __init__(self,
                 master_bot):
        self.bot = master_bot

    @commands.command(name='echo',
                      description='echo',
                      hidden=True)
    async def echo(self,
                   ctx: discord.ext.commands.Context,
                   *_str: str):
        await ctx.send(' '.join(_str))

    @commands.command(name='datetounix',
                      description='convert date to unix code for discord purposes.\n'
                                  'You must give a date in the following format: y/m/d H:M:S')
    async def datetounix(self,
                         ctx: discord.ext.commands.Context,
                         *date: str):
        try:
            _date = ' '.join(date)
            d = datetime.datetime.strptime(_date, '%y/%m/%d %H:%M:%S')
            unix_time = time.mktime(d.timetuple())
            await ctx.send(f'template: <`t:{str(int(unix_time))}:F`>  (remember to add < and > around the template!)')
            await ctx.send(f'<t:{int(unix_time)}:F>')
        except ValueError:
            await ctx.reply('You must give a date in the following format:\n'
                            '%y/%m/%d %H:%M:%S\n'
                            'do not include am/pm. use 24 hour clock.')

    @commands.command(name='help',
                      description="Show all available commands for this bot.")
    async def help(self, ctx: discord.ext.commands.Context):
        sorted_commands = sorted([command for command in self.bot.commands if not command.hidden], key=lambda x: x.name)

        async def get_page(page: int):
            emb: discord.Embed = self.bot.default_embed('**Available Bot Commands**\n\n',
                                                        'All commands are prefaced with "ub."\n\n')
            elements_per_page = 5
            offset = (page - 1) * elements_per_page
            for cmd in sorted_commands[offset:offset + elements_per_page]:
                emb.add_field(name=f'**ub.{cmd}**',
                              value=f'`{cmd.description}`',
                              inline=False)
            total_pages = Pagination.compute_total_pages(len(sorted_commands),
                                                         elements_per_page)

            emb.set_footer(text=f'Page {page} of {total_pages}')
            return emb, total_pages

        await Pagination(ctx, get_page).navigate()

    @commands.command(name="info",
                      description="Get build info.")
    async def info(self,
                   ctx: discord.ext.commands.Context):
        if ctx.channel is not discord.DMChannel:
            if self.bot.public_commands_channel is None or ctx.channel is not self.bot.public_commands_channel:
                if self.bot.admin_commands_channel is None or ctx.channel is not self.bot.admin_commands_channel:
                    return
        return await ctx.reply(embed=self.bot.info_embed())

    @commands.command(name='test',
                      description='developer test function',
                      hidden=True)
    async def test(self,
                   ctx: discord.ext.commands.Context):
        await ctx.send('guh? huh? who what? where am i?')

    @commands.Cog.listener()
    async def on_message(self,
                         message: discord.Message):
        if message.author == self.bot.user:
            return

        if 'nice' == message.content.lower():
            await message.reply('nice')
