"""bot tasker to periodically run assigned tasks
    """
from __future__ import annotations


import unittest


from discord.ext import tasks


from .task import BaseTask


__all__ = (
    'Tasker',
    'TestTasker',
)


class Tasker(list[BaseTask]):
    """task manager for PyDiscoBot
    """

    def __init__(self, *args):
        super().__init__(*args)
        self._task_hash: dict = {}

    def __contains__(self, item: BaseTask):
        return self._task_hash.get(item, None) is not None

    def append(self, task: BaseTask):
        if task not in self:
            super().append(task)
            self._task_hash[task.name] = task

    def remove(self,
               value: BaseTask):
        self._task_hash.pop(value.name, None)
        super().remove(value)

    def by_name(self,
                task_name: str) -> BaseTask | None:
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


class TestTasker(unittest.TestCase):
    """test tasker operations
    """

    def test_tasker(self):
        """tbd
        """
        class BingBong(BaseTask):
            pass

        class DingDong(BaseTask):
            pass

        task_a = BingBong(None)
        task_b = DingDong(None)

        tasker = Tasker()
        tasker.append(task_a)
        self.assertTrue(len(tasker) == 1)
        self.assertIsNotNone(tasker.by_name('BingBong'))
        tasker.append(task_b)
        self.assertTrue(len(tasker) == 2)
        self.assertIsNotNone(tasker.by_name('DingDong'))
        tasker.append(task_b)
        self.assertTrue(len(tasker) == 2)
        self.assertIsNotNone(tasker.by_name('DingDong'))
