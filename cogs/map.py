import asyncio
import discord
from discord import app_commands
from discord.ext import commands


class Map(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    @staticmethod
    def __gain_embed() -> discord.Embed:

        embed = discord.Embed(color=0xFFFFFF, title='Вывод карты местности:')
        file = discord.File("assets/images/map.png", filename="map.png")
        embed.set_image(url="attachment://map.png")
        return embed, file


    @app_commands.command(name='map', description='Вывод карты района')
    async def map(self, interaction: discord.Interaction) -> None:
        embed, file = self.__gain_embed()
        await interaction.response.defer()
        await interaction.followup.send(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Map(bot))
