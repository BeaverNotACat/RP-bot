import discord
from discord import app_commands
from discord.ext import commands

class Map(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @staticmethod
    def __gain_embed() -> discord.Embed:

        embed = discord.Embed(color=0xFFFFFF, title='Вывод карты местности:')
        file = discord.File("images/map.png", filename="map.png")
        embed.set_image(url="attachment://map.png")

        return embed, file

    @app_commands.command(name = 'map', description = 'Вывод карты района')
    async def map(self, interaction: discord.Interaction) -> None:
        embed_and_file = self.__gain_embed()
        embed = embed_and_file[0]
        file = embed_and_file[1]
        await interaction.response.interaction.followup.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Map(bot))