import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from classes.discordclient import DiscordClient

from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from classes.models import BodyPart, Character
from classes.parent_cogs import Change_health

from utilties.decorators import check_is_character_name_exists, \
                                check_is_admin


class Heal(Change_health):
    @app_commands.command(
        name='heal',
        description='Лечение персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа',
        part='Часть тела',
        heal_amount='Колличество лечения')
    @app_commands.choices(part=[
        Choice(name='Все тело', value='all'),
        Choice(name='Голова', value='head'),
        Choice(name='Торс', value='body'),
        Choice(name='Правая рука', value='right_arm'),
        Choice(name='Левая рука', value='left_arm'),
        Choice(name='Правая нога', value='right_leg'),
        Choice(name='Левая_нога', value='left_leg'),
        Choice(name='Рассудок', value='sanity')
    ])
    async def heal(self, interaction: discord.Interaction, character_name: str, part: str, heal_amount: int) -> None:
        await self.heal_command(
                interaction=interaction, 
                character_name=character_name,
                part=part, heal_amount=heal_amount)


async def setup(bot):
    await bot.add_cog(Heal(bot))
