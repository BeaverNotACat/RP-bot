from discord.ext import commands
from typing import Any

from classes.images import Images

from sqlalchemy.engine import Engine


class DiscordClient(commands.Bot):
    """Discord bot properties model
    For real bot class  open main.py"""
    
    @property
    def database() -> Engine:
        pass
    
    @property
    def images() -> Images:
        pass

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
