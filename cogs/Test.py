import discord
from discord import app_commands
from discord.ext import commands
import random


class Dice(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(
        name='Dice'
    )
    async def dice(self, ctx):
        await ctx.send(random.randint(0, 20))


async def setup(bot):
    await bot.add_cog(Dice(bot))
