import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands


import random


class Dice(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.database = self.bot.get_database()
        self.checkouts = self.bot.get_checkouts()

    def __gain_dice_vaue(self, dice: int, stat: str, character_name: str, mod: int) -> int:
        return random.randint(0, dice) + (self.database.read_stat(
            stat=stat, character_id=self.database.find_char_id(character_name=character_name.title())[0][0])[0][0]-10)//2+mod

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
        mod='Опционально! Модификатор броска')
    @app_commands.choices(stat=[
        Choice(name='мужество', value='fortitude'),
        Choice(name='мудрость', value='prudence'),
        Choice(name='выдержка', value='temperance'),
        Choice(name='справедливость', value='justice')])
    async def dice(self, interaction: discord.Interaction, stat: str, character_name: str, mod: int = 0, dice: int = 20) -> None:
        self.check_admin_rights(interaction=interaction)

        dice_value = self.__gain_dice_vaue(dice, stat, character_name, mod)

        await interaction.response.send_message(embed=self.__gain_embed(dice_value=dice_value))


async def setup(bot):
    await bot.add_cog(Dice(bot))
