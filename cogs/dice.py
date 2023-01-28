import random
import discord

from sqlalchemy import select, text
from sqlalchemy.orm import Session
from classes.models import Character

from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands

from utilties.decorators import check_is_character_owner

class Dice(commands.Cog):
    def __init__(self, bot) -> None:
        self.database = bot.database_engine
        self.checkouts = bot.checkouts

    def __gain_dice_vaue(self, dice: int, stat: str, character_name: str, mod: int) -> int:
        with Session(self.database) as session:
            character_id_query = select(Character.id).where(Character.name == character_name)
            charater_id = session.execute(character_id_query).first()[0]

            specified_stat_query = text(
                    'SELECT stats.%s FROM stats WHERE character_id = %i' % (stat, charater_id))
            specified_stat = session.execute(specified_stat_query).first()[0] 

        return random.randint(0, dice) + (specified_stat - 10) // 2 + mod

    @check_is_character_owner
    async def dice_command(self, interaction: discord.Interaction,
                   stat: str, character_name: str, mod: int, 
                   dice: int) -> None:
        dice_value = self.__gain_dice_vaue(dice, stat, character_name, mod)

        await interaction.response.send_message(embed=self.__gain_embed(dice_value=dice_value))


    @staticmethod
    def __gain_embed(dice_value: int) -> discord.Embed:
        if dice_value >= 20:
            emmed_color = 0x15D200
            emmed_name = 'Критический успех!'
        elif dice_value > 10:
            emmed_color = 0x90D200
            emmed_name = 'Успех'
        elif dice_value == 10:
            emmed_color = 0xD2D200
            emmed_name = 'Средне'
        elif dice_value > 0:
            emmed_color = 0xD22B00
            emmed_name = 'Провал!'
        else:
            emmed_color = 0xD22A00
            emmed_name = 'Критический провал!'

        embed = discord.Embed(color=emmed_color, title='Бросок кубика:')
        embed.add_field(name=emmed_name, value=f'Ваш результат: {dice_value}')

        return embed
    
    @app_commands.command(
        name='dice',
        description='Бросок кубика персонажа, для получения результата действия')
    @app_commands.describe(
        dice='Колличетсво граней кубика',
        stat='Характеристики вашего персонажа',
        character_name='Имя вашего персонажа',
        mod='Модификатор броска')
    @app_commands.choices(stat=[
        Choice(name='Мужество', value='fortitude'),
        Choice(name='Мудрость', value='prudence'),
        Choice(name='Выдержка', value='temperance'),
        Choice(name='Справедливость', value='justice')])
    async def dice(self, interaction: discord.Interaction,
                   stat: str, character_name: str, mod: int = 0, 
                   dice: int = 20) -> None:
        await self.dice_command(interaction=interaction, stat=stat, character_name=character_name, mod=mod, dice=dice)


async def setup(bot):
    await bot.add_cog(Dice(bot))
