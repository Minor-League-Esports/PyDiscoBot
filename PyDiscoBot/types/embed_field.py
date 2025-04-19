"""provide a class that fills an embed's field
    """
from __future__ import annotations


from dataclasses import dataclass
from typing import Optional


__all__ = (
    'EmbedField',
)


@dataclass
class EmbedField:
    """Embed field to inject into a :class:`discord.Embed`.

    .. ------------------------------------------------------------

    Arguments
    -----------
    name: :type:`str`
        Name of the field to display.

    value: :type:`str`
        Value to display in the field.

    inline: Optional[:type:`bool`]
        Defaults to ``False``.

        Whether to display this field in-line with others.


    .. ------------------------------------------------------------

    """
    name: str
    value: str
    inline: Optional[bool] = False
