import discord
import os

from classes.discordclient import DiscordClient
from classes.database import DatabaseInterface


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

        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])

    def get_database(self) -> DatabaseInterface:
        return self.__database


if __name__ == '__main__':

    bot = Client()
    token = open('token')
    bot.run(token.read(70))
