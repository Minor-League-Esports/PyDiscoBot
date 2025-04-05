"""bot tasker to periodically run assigned tasks
    """

from discord.ext import tasks
from .task import Task


class Tasker(list[Task]):
    """task manager for PyDiscoBot
    """

    def append(self, task: Task):
        if task not in self:
            super().append(task)

    @tasks.loop()
    async def run(self) -> bool:
        """run the task manager

        Returns:
            bool: all tasks completed successfully
        """
        _ = [await task.run() for task in self]
