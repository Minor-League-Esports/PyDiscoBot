"""provide an abc base class for all tasks to derive from for consistent operations
    """
from __future__ import annotations


from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .bot import BaseBot


__all__ = (
    'BaseTask',
)


class BaseTask:
    """Base class for :class:`Task`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: :class:`pydiscobot.Bot`
        The bot this task belongs to.

    .. ------------------------------------------------------------

    Attributes
    -----------
    name: :class:`str`
        The name of this :class:`Task`.

    parent: :class:`pydiscobot.Bot`
        The parent :class:`Bot` of this :class:`Task`.

    .. ------------------------------------------------------------

    """

    def __init__(self,
                 parent: BaseBot):
        self._parent: BaseBot = parent

    @property
    def name(self) -> str:
        """Get the `name` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    name: :class:`str`
        The name of this :class:`Task`.

    """
        return self.__class__.__name__

    @property
    def parent(self) -> BaseBot:
        """Get the :class:`pydiscobot.Bot` of this :class:`Task`.

    .. ------------------------------------------------------------

    Returns
    -----------
    parent: :class:`pydiscobot.Bot`
        The parent :class:`pydiscobot.Bot` that owns this :class:`Task`.

    """
        return self._parent
