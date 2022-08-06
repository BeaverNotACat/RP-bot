import discord
from discord.ext import commands
import os

from classes.discordclient import DiscordClient


class Client(DiscordClient):

    def __init__(self,):
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all(),)

    async def on_ready(self):
        print(f'Bot is now online!')

    async def setup_hook(self):
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])


bot = Client()

token = open('token')
bot.run(token.read(70))
