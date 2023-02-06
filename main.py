import discord
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from classes.discordclient import DiscordClient
from classes.database import DatabaseInterface
from classes.checkouts import Checkouts
from classes.images import Images

class Client(DiscordClient):
    def __init__(self) -> None:
        self.__database = DatabaseInterface('roleplay.db')
        self.__checkouts = Checkouts()
        self.__images = Images()
        self.__database_engine = create_engine("sqlite:///roleplay.db", echo=True, future=True)

        self.__synced = False
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all(),)

    async def on_ready(self) -> None:
        if not self.__synced:
            await self.tree.sync()
            self.__synced = True

    async def setup_hook(self) -> None:

        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])

    @property
    def images(self) -> Images:
        return self.__images

    @property
    def database(self) -> Engine:
        '''SQLAlchemy database engine'''
        return self.__database_engine


if __name__ == '__main__':

    bot = Client()
    token = open('token')
    bot.run(token.read(70))
