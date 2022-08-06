from discord.ext import commands
from typing import Any

from classes.database import DatabaseInterface


class DiscordClient(commands.Bot):
    """A Subclass of 'commands.Bot'."""

    database: DatabaseInterface
    """Represent the database connection."""

    command_prefix: str
    """Discord bot prefix"""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
