from discord.ext import commands
from typing import Any

from classes.database import DatabaseInterface
from classes.checkouts import Checkouts


class DiscordClient(commands.Bot):
    """Подкласс дискорд бота, для типизировання python. (МЕТОДЫ РАБОТАЮТ ЧЕРЕЗ ПЕГРУЗКУ В main.py!!!)"""

    def get_database() -> DatabaseInterface:
        pass

    def get_checkouts() -> Checkouts:
        pass

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
