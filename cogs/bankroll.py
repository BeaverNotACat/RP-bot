import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from classes.discordclient import DiscordClient

from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from classes.models import BodyPart, Character, Item

from utilties.decorators import check_is_character_name_exists, \
                                check_is_item_exists, \
                                check_is_character_owner_or_admin


class Bankroll(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.database = bot.database


    @staticmethod
    def __gain_embed(character_name: str, ankh_amount:int, moonrock_amount:int) -> discord.Embed:
        embed = discord.Embed(
            color=0xFFFFFF, title=f'Баланс {character_name}:')
        embed.add_field(name='Аннх', value=ankh_amount)
        embed.add_field(name='Лунный камень', value=moonrock_amount)
        return embed


    @check_is_character_name_exists
    @check_is_character_owner_or_admin
    @check_is_item_exists(item_type='Ankh', item_name='Анкх')
    @check_is_item_exists(item_type='Moonrock', item_name='Лунный камень')
    async def balance_command(self, interaction: discord.Interaction, character_name:str) -> None:
        with Session(self.database) as session:
            character_id_query = select(Character.id).where(Character.name == character_name)
            character_id = session.execute(character_id_query).first()[0]

            ankh_amount_query = select(Item.amount).where(
                    (Item.character_id == character_id) & (Item.type == 'Ankh'))
            ankh_amount = session.execute(ankh_amount_query).first()[0]

            moonrock_amount_query = select(Item.amount).where(
                    (Item.character_id == character_id) & (Item.type == 'Moonrock'))
            moonrock_amount = session.execute(ankh_amount_query).first()[0]


        embed = self.__gain_embed(character_name, ankh_amount, moonrock_amount)
        await interaction.user.send(embed=embed)
        await interaction.response.send_message(
                'Информация о денежный средствах персонажа отправлена в личные сообщения')


    @app_commands.command(
        name='bankroll',
        description='Отправить баланс персонажа в личные сообщения')
    @app_commands.describe(
        character_name='Имя вашего персонажа')
    async def balance(self, interaction: discord.Interaction, character_name: str) -> None:
        await self.balance_command(
                interaction=interaction, 
                character_name=character_name)


async def setup(bot):
   await bot.add_cog(Bankroll(bot))
