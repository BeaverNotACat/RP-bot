import discord
from database import DatabaseInterface


class Checkouts:
    '''List of static utils methods, that checks user's unput'''

    @staticmethod
    async def check_admin_rights(interaction: discord.Interaction) -> None:
        if interaction.guild.get_role(898307915348332614) not in interaction.user.roles:
            raise discord.app_commands.AppCommandError(
                'Вы не имеете прав администратора')

    @staticmethod
    async def check_stat_name(stat: str) -> None:
        if stat != 'мужество' or stat != 'мудрость' or stat != 'выдержка' or stat != 'справедливость':
            raise discord.app_commands.AppCommandError(
                'Неправильноt название характеристики')

    @staticmethod
    async def check_negative_heal(amount):
        raise discord.app_commands.AppCommandError(
            'Запрещено лечение на отрицательные значения')

    @staticmethod
    async def check_name(name: str, database: DatabaseInterface) -> None:
        try:
            await database.find_char_id(name)
        except:
            raise discord.app_commands.AppCommandError(
                'Неправильное имя персонажа')

    @staticmethod
    async def check_inlfuence_money(name: str, database: DatabaseInterface) -> None:
        try:
            await database.read_money_amount(database.find_char_id(name))
        except:
            raise discord.app_commands.AppCommandError(
                'Недостаточно средств для совершения оперции')
