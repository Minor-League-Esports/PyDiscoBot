# PyDiscoBot

PyDiscoBot is a general use python-based discord utility bot.
It is meant as a very robust and feature-rich starting point for extending this repo into other bots.

## :dependabot: Setup :dependabot:
Download this repo and pip install it to begin using it immediately!

Start off by pip installing the module
``` python
pip install ../PyDiscoBot/. --upgrade
```

You can easily install the requirements via python's pip module!
```python
pip install -r requirements.txt
```

### :memo: Fill out the .env file to customize your bot! :memo:

Make sure to include these imports!
```python
import discord
from discord.ext import commands
import dotenv
import os
import pydiscobot
```

Create a custom class for your bot!
```python
class MyBot(pydiscobot.Bot):
    def __init__(self,
                 command_prefix: str | None = None,
                 bot_intents: discord.Intents | None = None,
                 command_cogs: [discord.ext.commands.Cog] = None):
        super().__init__(command_prefix=command_prefix,
                         bot_intents=bot_intents,
                         command_cogs=command_cogs)
```

To add functionality when the bot comes online, over-ride the on-ready function of the bot!
```python
async def on_ready(self,
                       suppress_task=False) -> None:
        await super().on_ready(suppress_task)  # remember to call the parent class here!
        # do_some_code_here!!!
```

To add functionality to each of the bot's "ticks", over-ride the on_task function of the bot!
```python
    async def on_task(self) -> None:
        await super().on_task()  # remember to call the parent class here!
        # do some task-y stuff here!
```

Run your file!
```python
if __name__ == '__main__':
    dotenv.load_dotenv()

    intents = discord.Intents(8)
    # noinspection PyDunderSlots
    intents.guilds = True
    # noinspection PyDunderSlots
    intents.members = True
    # noinspection PyDunderSlots
    intents.message_content = True
    # noinspection PyDunderSlots
    intents.messages = True
    # noinspection PyDunderSlots
    intents.reactions = True

    bot = MyBot('ub.',
                intents,
                [...discord.ext.commands.Cog])

    bot.run(os.getenv('DISCORD_TOKEN'))
```

## :computer: Development Status :computer:

Build - :construction: beta

Version - 1.1.3

### Requirements
- discord.py==2.3.2
- python-dotenv==1.0.1

## :soccer: Join MLE Today! :soccer:
:sparkler: Main Site:
  - https://mlesports.gg/
    
:postbox: Apply Today!:
  - https://mlesports.gg/apply
    
:camera: Check out our twitter!:
  - https://twitter.com/mlesportsgg
