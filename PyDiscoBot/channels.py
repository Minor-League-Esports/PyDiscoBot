"""provide logical services to operate on discord channels
    """
from __future__ import annotations


from typing import Union
import discord


__all__ = (
    'find_ch',
    'clear_messages',
)


def find_ch(guilds: list[discord.Guild],
            channel_id: Union[str, int]) -> Union[discord.abc.GuildChannel, None]:
    """Get a :class:`discord.abc.GuildChannel` with a corresponding `id`, or none if it is not found.

    .. ------------------------------------------------------------

    Arguments
    -----------
    guilds: list[:class:`discord.Guild`]
        A list of guilds to search for the given channel id.

    channel_id: Union[:class:`str`, :class:`int`]
        Channel ID to search for.

    .. ------------------------------------------------------------

    Returns
    --------
    Union[:class:`discord.abc.GuildChannel`, :type:`None`]
        A corresponding :class:`discord.abc.GuildChannel` or :type:`None` if none found.

    .. ------------------------------------------------------------

    Examples
    ----------

    Get a channel and clear messages of said channel.

    .. code-block:: python

        import discord
        from pydiscobot.services import channels

        async def clear_this_channel(guilds_to_search: list[discord.Guild],
                                     channel_id: Union[int, str],
                                     count: int = 100):
            '''Clear a channel of some messages'''

            channel = channels.find_ch(guilds_to_search, int(channel_id))
            if channel:
                await channels.clear_messages(channel, count)

    """
    for guild in guilds:
        ch = guild.get_channel(int(channel_id))
        if ch:
            return ch
    return None


async def clear_messages(channel: discord.abc.GuildChannel,
                         count: int) -> bool:
    """Clear a :class:`discord.abc.GuildChannel` of a specified # of messages.

    This count **cannot** exceed `100` and the messages **cannot** be older than `14` days.

    .. ------------------------------------------------------------

    Arguments
    -----------
    channel: :class:`discord.abc.GuildChannel`
        The channel to delete messages from.

    count: :class:`int`
        The amount of messages to delete. **Cannot* be more than `100`.

    .. ------------------------------------------------------------

    Raises
    --------
    ValueError
        The amount of message passed was not valid (100 < count < 0 ).

    .. ------------------------------------------------------------

    Returns
    --------
    :class:`bool`
        Value of success.

    .. ------------------------------------------------------------

    Examples
    ----------

    Delete messages from a :class:`discord.TextChannel`.

    .. code-block:: python

        import discord
        from pydiscobot.services import channels

        async def clear_this_channel(channel: discord.TextChannel
                                    count: int = 100):
            '''Clear this channel of some messages'''

            await channels.clear_messages(channel, count)

    """
    if count > 100 or count <= 0:
        raise ValueError(f'Cannot delete that many messages!: {count}')
    try:
        await channel.delete_messages([message async for message in channel.history(limit=count)])
        return True
    except (discord.ClientException, discord.Forbidden, discord.HTTPException):
        return False
