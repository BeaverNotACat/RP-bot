import discord
from discord import app_commands
from discord.ext import commands


import random


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener("on_app_command_error")
    async def get_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        interaction.response.send_message('1')


async def setup(bot):
    await bot.add_cog(CommandErrorHandler(bot))
