import os
import discord

BOT_LOG_NAME = 'bot logger'

DEF_EMBED_COLOR = discord.Color.dark_blue()
DEF_EMBED_URL = os.getenv('SERVER_ICON')

ERR_BAD_CMD = "That command wasn't found! Type '/' to see all commands."
ERR_MSG_PARAM = 'You must fill in additional arguments for this command!'
ERR_RATE_LMT = 'We are being rate limited... Please wait a few moments before trying that again.'
ERR_BAD_PRV = 'You do not have sufficient privelages to do that...'
ERR_BAD_CH = 'You cannot do that in this channel...'
ERR_BOT_NL = 'Bot is initializing... Please try again later...'
