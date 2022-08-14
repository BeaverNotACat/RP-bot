import discord
from discord import app_commands
from discord.ext import commands

import traceback


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        bot.tree.error(coro=self.__dispatch_to_app_command_handler)

    @staticmethod
    def __gain_embed(error) -> discord.Embed:
        embed = discord.Embed(color=0xD22A00, title='Ошибка!:')
        embed.add_field(
            name='Операция не выполненна по причине:', value=error)
        return embed

    async def __dispatch_to_app_command_handler(self, interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
        self.bot.dispatch("app_command_error", interaction, error)

    async def __respond_to_interaction(self, interaction: discord.Interaction, error: str) -> bool:
        try:
            await interaction.response.send_message(embed=self.__gain_embed(error=error), ephemeral=True)
            return True
        except discord.errors.InteractionResponded:
            return False

    @commands.Cog.listener("on_app_command_error")
    async def get_app_command_error(self, interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
        await self.__respond_to_interaction(interaction, error=error)


async def setup(bot):
    await bot.add_cog(CommandErrorHandler(bot))
