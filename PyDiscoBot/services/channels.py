import discord


def find_ch(guilds: list[discord.Guild],
            ch_id: str) -> discord.abc.GuildChannel | None:
    """find channel in given guilds

    Args:
        guilds (list[discord.Guild]): discord guilds this bot is a part of
        ch_id (str): channel id to search for

    Returns:
        discord.abc.GuildChannel | None: found channel or none
    """
    for guild in guilds:
        for ch in guild.channels:
            if str(ch.id) == ch_id:
                return ch
    return None


async def clear_messages(channel: discord.channel,
                         count: int) -> bool:
    """ Helper function to clear a channel of messages\n
        Max channel message delete count is 100\n
        **param channel**: the channel to delete messages from\n
        **param count**: number of messages to delete
        """
    if count > 100 | count <= 0:
        raise ValueError(f'Cannot delete that many messages!: {count}')
    try:
        await channel.delete_messages([message async for message in channel.history(limit=count)])
        return True
    except (discord.ClientException, discord.Forbidden, discord.HTTPException):
        return False
