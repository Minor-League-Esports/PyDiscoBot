"""frames module for discord embeds
    """

from .frame import get_frame
from .admin import get_admin_frame
from .notification import get_notification

__version__ = '1.1.2'

__all__ = (
    'get_frame',
    'get_admin_frame',
    'get_notification',
)
