"""Common discord command
    all discord commands should be derived from the meta class
    """
from __future__ import annotations

from typing import TYPE_CHECKING


from discord.ext import commands


if TYPE_CHECKING:
    from .bot import BaseBot


__all__ = (
    'BaseCog',
)


class BaseCog(commands.Cog):
    """Base `Cog` for PyDiscoBot commands.

    A :class:`Cog` is a container for discord `commands` and discord `app_commands`.

    Though this is not an :class:`ABC`, this class describes the meta
    relationship the cog has within this environment.

    That being said, all commands used for the bot should be
    derived from this 'meta' `Cog`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    parent: :class:`Bot`
        The parent :class:`Bot` of this `Cog`.

    .. ------------------------------------------------------------

    Attributes
    -----------
    parent: :class:`Bot`
        The parent :class:`Bot` of this `Cog`.

    """
    _parent: BaseBot

    @property
    def parent(self) -> BaseBot:
        """ Parent container for this cog.

        .. ------------------------------------------------------------

        Returns
        -----------
            :class:`pydiscobot.types.BaseBot`
        """
        return self._parent
