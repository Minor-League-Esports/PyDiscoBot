"""Common discord command
    all discord commands should be derived from the meta class
    """
from __future__ import annotations


from typing import Optional, TYPE_CHECKING


from . import types


if TYPE_CHECKING:
    from .bot import Bot


class Cog(types.BaseCog):
    """Pseudo 'meta' discord bot `Cog`.

    A :class:`Cog` is a container for discord `commands` and discord `app_commands`.

    Though this is not an :class:`ABC`, this class describes the meta
    relationship the cog has within this environment.

    That being said, all commands used for the bot should be
    derived from this 'meta' `Cog`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: Optional[:class:`Bot`]
        The parent :class:`Bot` of this `Cog`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    parent: :class:`Bot` | None
        The parent :class:`Bot` of this `Cog`.

    """

    def __init__(self,
                 parent: Optional[Bot] = None):
        self._parent: Bot = parent

    @property
    def parent(self) -> Optional[Bot]:
        """The parent :class:`Bot` of this `Cog`.

        .. ------------------------------------------------------------

        Returns
        -----------
            parent: :class:`Bot` | None
        """
        return self._parent
