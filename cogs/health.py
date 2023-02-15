import discord
from discord import app_commands
from discord.ext import commands
from classes.discordclient import DiscordClient

from sqlalchemy import select
from sqlalchemy.orm import Session
from classes.models import BodyPart, Character

from utilties.decorators import check_is_character_name_exists


class Health(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.database = bot.database
        self.images = bot.images


    @staticmethod
    def __gain_embed() -> tuple[discord.Embed, discord.File]:
        embed = discord.Embed(
            color=0xFFFFFF, title='Анализ состояния здоровья:')
        file = discord.File("assets/hp_temp.png", filename="hp_temp.png")
        embed.set_image(url="attachment://hp_temp.png")
        return embed, file


    @check_is_character_name_exists
    async def health_command(self, interaction: discord.Interaction, character_name:str) -> None:
        with Session(self.database) as session:
            character_id_query = select(Character.id).where(Character.name == character_name)
            character_id = session.execute(character_id_query).first()[0]

            body_parts_query = select(BodyPart).filter(BodyPart.character_id == character_id)
           
            body_parts:dict = {}
            for part in session.scalars(body_parts_query):
                body_parts[part.type] = (part.health_points, part.max_health_points)
            self.images.health_condition_image(**body_parts)

        embed, file = self.__gain_embed()
        await interaction.followup.send(embed=embed, file=file)


    @app_commands.command(name='health', description='Вывод здоровья персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа')
    async def health(self, interaction: discord.Interaction, character_name: str) -> None:
        await interaction.response.defer()
        await self.health_command(interaction=interaction, character_name=character_name)


async def setup(bot):
    await bot.add_cog(Health(bot))
