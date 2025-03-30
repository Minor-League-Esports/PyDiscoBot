import asyncio
import functools
import typing


def to_thread(func: typing.Callable) -> typing.Coroutine:
    """decorator to cast a blocking function into the async pool

    Returns:
        typing.Coroutine: async wrapped method
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        wrapped = functools.partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, wrapped)
    return wrapper
