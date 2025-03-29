from typing import Callable
import inspect
import discord
from discord.ext import tasks


class PeriodicTask:
    """ Periodic Task
    This class uses ***@task***s to run tasks as required.
    """

    def __init__(self,
                 parent):
        self.logger = parent.logger
        self.logger.info('initializing periodic task...')

        self.admin_message: discord.Message | None = None
        self.parent = parent
        self.on_tick: list[Callable] = []

    @tasks.loop()
    async def run(self):
        """ looping task\n
            **returns**: None\n
            """
        self.logger.info('running periodic task...')
        for cb in self.on_tick:
            if inspect.iscoroutinefunction(cb):
                self.logger.info('calling async func %s', cb.__name__)
                await cb()
            else:
                self.logger.info('calling func %s', cb.__name__)
                cb()

    def change_interval(self,
                        seconds: int) -> None:
        """ change interval of periodic task\n
        **param seconds**: period that the task will sleep between intervals\n
        **returns**: self\n
        """
        self.logger.info('changing periodic task to %s seconds...', str(seconds))
        self.parent.admin_info.cycle_time = seconds
        self.run.change_interval(seconds=float(self.parent.admin_info.cycle_time))
