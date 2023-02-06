import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from classes.discordclient import DiscordClient

from sqlalchemy import select
from sqlalchemy.orm import Session
from classes.models import BodyPart, Character

from utilties.decorators import check_is_character_name_exists, \
                                check_is_admin

class Heal(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.database = bot.database


    @staticmethod
    def __gain_embed(part: list):
        embed = discord.Embed(color=0xFFFFFF, title='Лечение персонажа:')
        embed.add_field(name='Текущее здоровье персонажа:',
                        value=f'сюда выводить картинку с хепешкой')
        return embed


    @staticmethod
    def __get_parts_list(part: str) -> list:
        if part == 'all':
            return ['head', 'body', 'arm_r', 'arm_l', 'leg_r', 'leg_l']
        else:
            return [part]


    def __scale_heal_amount(self, character_id: int, part: str, heal_amount: int) -> int:
        max_hp = self.database.read_part_max_hp(part, character_id)[0][0]
        current_hp = self.database.read_part_hp(part, character_id)[0][0]

        if max_hp < current_hp + heal_amount:
            return max_hp - current_hp
        else:
            return heal_amount


    @check_is_admin
    @check_is_character_name_exists
    async def health_command(self, interaction: discord.Interaction,
                             character_name: str, part: str, heal_amount: int) -> None:
        with Session(self.database) as session:
            character_id_query = select(Character.id).where(Character.name == character_name)
            character_id = session.scalars(character_id_query).one()

            if part == 'all':
                body_parts_query = select(BodyPart).where(character_id == character_id)
            else:
                body_parts_query = select(BodyPart).where((character_id == character_id) & (type == part))

            for part in session.scalars(body_parts_query):
                if part.health_points + heal_amount > part.max_health_points:
                    part.health_points = part.max_health_points
                else:
                    part.health_points = part.health_points + heal_amount
                    session.commit()

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
        await self.health_command(interaction=interaction, character_name=character_name,
                            part=part, heal_amount=heal_amount)

        #await self.checkouts.check_admin_rights(interaction)

        #character_id = self.database.find_char_id(
        #    character_name=character_name.title())[0][0]

        #for part in self.__get_parts_list(part):

        #    self.database.cause_damage(
        #        body_part=part, damage=-self.__scale_heal_amount(
        #            character_id=character_id, part=part, heal_amount=heal_amount), target_character_id=character_id)

        #await interaction.response.send_message(embed=self.__gain_embed(part=part))


async def setup(bot):
    await bot.add_cog(Heal(bot))
