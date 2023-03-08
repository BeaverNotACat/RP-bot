import discord
from discord.ext import commands
from classes.discordclient import DiscordClient

from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from classes.models import BodyPart, Character

from utilties.decorators import check_is_character_name_exists, \
                                check_is_admin


class Change_health(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.database = bot.database


    @staticmethod
    def check_is_heal_positive(method):
        def decorate(self, *args, **kwargs):
                if kwargs['heal_amount'] < 0:
                    raise ValueError('Запрещено изменять здоровье на отрицательные значения')
                return method(self, *args, **kwargs)
        return  decorate

    @staticmethod
    def check_is_damage_positive(method):
        def decorate(self, *args, **kwargs):
                if kwargs['damage_amount'] < 0:
                    raise ValueError('Запрещено изменять здоровье на отрицательные значения')
                return method(self, *args, **kwargs)
        return  decorate

    @staticmethod
    def translate_body_parts_name(name: str) -> str:
        dictionary = {
                'head': 'Голова',
                'body': 'Туловище',
                'left_arm': 'Левая рука',
                'right_arm': 'Правая рука',
                'left_leg': 'Левая нога',
                'right_leg': 'Правая нога',
                'sanity': 'Рассудок'
                }
        return dictionary[name]


    def __gain_hp_change_embed(self, hp_changes: list[dict]) -> discord.Embed:
        embed = discord.Embed(color= 0xFFFFFF, title='Изменение здоровья:')
        for hp_change in hp_changes:
            embed.add_field(
                    name=self.translate_body_parts_name(hp_change['name']),
                    value=f"{hp_change['old_hp']} ➟ {hp_change['new_hp']}")
        return embed   
    

    def make_body_parts_query(self, character_name: str, part: str):
        with Session(self.database) as session:
                character_id_query = select(Character.id).where(
                        Character.name == character_name)
                character_id = session.scalars(character_id_query).one()

                if part == 'all':
                    body_parts_query = select(BodyPart).where(
                            character_id == character_id)
                else:
                    body_parts_query = select(BodyPart).where(
                            (BodyPart.character_id == character_id) & (BodyPart.type == part))
        return body_parts_query


    @check_is_admin
    @check_is_character_name_exists
    @check_is_heal_positive
    async def heal_command(self, interaction: discord.Interaction,
                             character_name: str, part: str, heal_amount: int) -> None:
        body_parts_query = self.make_body_parts_query(character_name, part)
        hp_changes: list = []
        
        with Session(self.database) as session:
            for part in session.scalars(body_parts_query):
                hp_change:dict = {'name': part.type, 'old_hp': part.health_points}

                if part.health_points + heal_amount > part.max_health_points:
                    part.health_points = part.max_health_points
                else:
                    part.health_points = part.health_points + heal_amount
                session.commit()

                hp_change['new_hp'] = part.health_points
                hp_changes.append(hp_change)

        await interaction.response.send_message(
                embed=self.__gain_hp_change_embed(hp_changes))


    @check_is_admin
    @check_is_character_name_exists
    @check_is_damage_positive
    async def damage_command(self, interaction: discord.Interaction,
                             character_name: str, part: str, damage_amount: int) -> None:
        body_parts_query = self.make_body_parts_query(character_name, part)
        hp_changes: list = []

        with Session(self.database) as session:
            for part in session.scalars(body_parts_query):
                hp_change:dict = {'name': part.type, 'old_hp': part.health_points}

                if part.health_points - damage_amount < 0:
                    part.health_points = 0
                else:
                    part.health_points = part.health_points - damage_amount
                session.commit()

                hp_change['new_hp'] = part.health_points
                hp_changes.append(hp_change)

        await interaction.response.send_message(
                embed=self.__gain_hp_change_embed(hp_changes))

