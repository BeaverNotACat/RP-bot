import discord
import os

from classes.discordclient import DiscordClient
from classes.database import DatabaseInterface
from classes.checkouts import Checkouts
from classes.images import Images


class Client(DiscordClient):
    def __init__(self) -> None:
        self.__synced = False
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all(),)

    async def on_ready(self) -> None:
        if not self.__synced:
            await self.tree.sync()
            self.__synced = True

    async def setup_hook(self) -> None:
        self.__database = DatabaseInterface('roleplay.db')
        self.__checkouts = Checkouts()
        self.__images = Images()

        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])

    def get_database(self) -> DatabaseInterface:
        return self.__database

    def get_checkouts(self) -> Checkouts:
        return self.__checkouts

    def get_images(self) -> Images:
        return self.__images


if __name__ == '__main__':

    bot = Client()
    token = open('token')
    bot.run(token.read(70))
