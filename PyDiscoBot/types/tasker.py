"""bot tasker to periodically run assigned tasks
    """

from discord.ext import tasks
from .task import Task


class Tasker(list[Task]):
    """task manager for PyDiscoBot
    """

    def __init__(self, *args):
        super().__init__(*args)
        self._task_hash: dict = {}

    def append(self, task: Task):
        if task not in self:
            super().append(task)
            self._task_hash[task.name] = task

    def remove(self,
               value: Task):
        self._task_hash.pop(value.name, None)
        super().remove(value)

    def by_name(self,
                task_name: str) -> Task | None:
        """get Task by name

        Args:
            task_name (str): name of task

        Returns:
            Task | None: Task (or none if not in list)
        """
        return self._task_hash.get(task_name, None)

    @tasks.loop()
    async def run(self) -> bool:
        """run the task manager

        Returns:
            bool: all tasks completed successfully
        """
        _ = [await task.run() for task in self]
