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
    def __gain_embed():
        embed = discord.Embed(color=0xFFFFFF, title='Бросок кубика:')
        embed.add_field(name='Пероснаж вылечен', value=f'')

        return embed

    @staticmethod
    def __get_parts_list(part: str) -> list:
        if part == 'all':
            return ['head', 'body', 'arm_r', 'arm_l', 'leg_r', 'leg_l']
        else:
            return [part]

    def __scale_heal_amount(self, character_id: int, part: str, heal_amount: int) -> int:
        max_hp = self.database.read_part_max_hp(part, character_id)
        current_hp = self.database.read_part_hp(part, character_id)

        if max_hp < current_hp + heal_amount:
            return max_hp - current_hp
        else:
            return heal_amount

    @app_commands.command(
        name='treat',
        description='Лечение персонажа')
    @app_commands.describe(
        character_name='Имя вашего персонажа',
        part='Часть тела',
        heal_amount='Колличество лечения')
    @app_commands.choices(part=[
        Choice(name='Все тело', value='all'),
        Choice(name='Голова', value='head'),
        Choice(name='Торс', value='body'),
        Choice(name='Правая рука', value='arm_r'),
        Choice(name='Левая рука', value='arm_l'),
        Choice(name='Правая нога', value='leg_r'),
        Choice(name='Левая_нога', value='leg_l')
    ])
    async def treat(self, interaction: discord.Interaction, character_name: str, part: str, heal_amount: int) -> None:
        await self.checkouts.check_admin_rights(interaction)

        character_id = self.database.find_char_id(
            character_name=character_name)

        for part in self.__get_parts_list(part):

            await self.database.cause_damage(
                body_part=part, damage=-self.__scale_heal_amount(
                    character_id=character_id, part=part, heal_amount=heal_amount), target_character_id=character_id)

        await interaction.response.send_message(embed=self.__gain_embed())


async def setup(bot):
    await bot.add_cog(Treat(bot))
