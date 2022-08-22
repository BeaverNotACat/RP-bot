import discord
from discord import app_commands
from discord.ext import commands
from classes.discordclient import DiscordClient


class Health(commands.cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot
        self.database = self.bot.get_databse()
        self.images = self.bot.get_images()
        self.checkouts = self.bot.get_checkouts()

    @staticmethod
    def __gain_embed() -> discord.Embed:

        embed = discord.Embed(
            color=0xFFFFFF, title='Анализ состояния здоровья:')
        file = discord.File("temp/hp_temp.png", filename="hp_temp.png")
        embed.set_image(url="attachment://hp_temp.png")

        return embed, file

    @app_commands.command(name='health', description='Вывод здоровья персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа')
    async def health(self, interaction: discord.Interaction, character_name: str) -> None:

        health = self.read_all_part_conditon(
            self.find_char_id(character_name)[0][0])
        self.images.health_condition_image(
            health[0], health[1], health[2], health[3], health[4], health[5], health[6])
        embed, file = self.__gain_embed()
        await interaction.response.defer()
        await interaction.followup.send(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Health(bot))
