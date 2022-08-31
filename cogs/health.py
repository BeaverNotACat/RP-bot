import asyncio
import discord
from discord import app_commands
from discord.ext import commands

from classes.discordclient import DiscordClient


class Health(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot
        self.database = self.bot.get_database()
        self.checkouts = self.bot.get_checkouts()
        self.images = self.bot.get_images()

    @staticmethod
    def __gain_embed() -> discord.Embed:

        embed = discord.Embed(
            color=0xFFFFFF, title='Анализ с=остояния здоровья:')
        file = discord.File("images/temp/hp_temp.png", filename="hp_temp.png")
        embed.set_image(url="attachment://hp_temp.png")

        return embed, file

    @app_commands.command(name='health', description='Вывод здоровья персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа')
    async def health(self, interaction: discord.Interaction, character_name: str) -> None:

        health = self.database.read_all_part_conditon(
            self.database.find_char_id(character_name=character_name.title())[0][0])
        self.images.health_condition_image(
            health[0], health[1], health[2], health[3], health[4], health[5], health[6])
        embed, file = self.__gain_embed()
        await interaction.response.defer()
        await interaction.followup.send(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Health(bot))
