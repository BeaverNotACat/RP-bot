import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands

from classes.discordclient import DiscordClient


class Treat(commands.Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot
        self.database = self.bot.get_database()
        self.checkouts = self.bot.get_checkouts()

    @staticmethod
    def __get_parts_list(part):
        if part == 'all':
            return ['head', 'body', 'arm_r', 'arm_l', 'leg_r', 'leg_l']
        else:
            return [part]

    @app_commands.command(
        name='treat',
        description='Лечение персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа',
        part='Часть тела',
        value='Колличество лечения')
    @app_commands.choices(part=[
        Choice(name='Все тело', value='all'),
        Choice(name='Голова', value='head'),
        Choice(name='Торс', value='body'),
        Choice(name='Правая рука', value='arm_r'),
        Choice(name='Левая рука', value='arm_l'),
        Choice(name='Правая нога', value='leg_r'),
        Choice(name='Левая_нога', value='leg_l')
    ])
    async def treat(self, interaction: discord.Interaction, character_name: str, part: str, value: int) -> None:
        self.checkouts.check_admin_rights(interaction)

        for part in self.__get_parts_list(part):
            self.database.cause_damage(
                body_part=part, damage=-value, target_character_id=self.database.find_char_id(character_name=character_name))
        await interaction.response.send_message(1)


async def setup(bot):
    await bot.add_cog(Treat(bot))
