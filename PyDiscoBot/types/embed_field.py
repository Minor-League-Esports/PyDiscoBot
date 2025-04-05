"""provide a class that fills an embed's field
    """

from dataclasses import dataclass


@dataclass
class EmbedField:
    """helper class to create embed fields more easily
    """
    name: str
    value: str
    inline: bool = False
