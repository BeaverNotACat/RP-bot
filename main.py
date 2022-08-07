import discord
import os

from classes.discordclient import DiscordClient
from classes.database import DatabaseInterface


class Client(DiscordClient):
    def __init__(self):
        self.synced = False
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all(),)

    async def on_ready(self):
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print(
            f'Logged as: {self.user} | discord.py {discord.__version__}')

    async def setup_hook(self):
        self.__database = DatabaseInterface('roleplay.db')

        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])

    def get_database(self):
        return self.__database


if __name__ == '__main__':

    bot = Client()
    token = open('token')
    bot.run(token.read(70))
