import discord
from discord.ext import commands

import random

from settings import config

# Самописные функции для работы с бд
from tools.db_tools import max_hp_read, stat_read, cause_damage, money_transaction, health_condition_read, part_hp_read, create_aliases, find_char_id
# Заготовки под вывод сообщений
from tools.discord_tools import form_health_condition_emmed, form_health_changes_emmed, form_roll_result_emmed, form_money_transfer_emmed, form_error_emmed
# Создании изображений для сообщений
from tools.imgs_tools import make_health_condition_pic
# Проверка ввода пользователей на ошибки
from tools.erors import name_error, ownership_error, stat_error, part_name_error, influence_money, negative_heal

bot = commands.Bot(command_prefix=config['prefix'])
#################################################################################
print(config['token'])


@bot.command()  # Готово
async def dice(ctx, stat=str(), character_name=str(), mod=0):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Вы не владее персонажем с таким именем')
    elif stat_error(stat):
        embed = form_error_emmed(
            'Неправильно указано название характеристики персонажа')
    else:
        character_id = find_char_id(character_name, ctx.author.id)
        stat_value = stat_read(stat, character_id)
        roll_value = random.randint(0, 20) + (stat_value-10)//2 + mod
        embed = form_roll_result_emmed(roll_value)

    await ctx.reply(embed=embed)


@bot.command()  # Готово
async def transfer(ctx, character_name=str(), amount=int(), target_name=str()):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Вы не владее персонажем с таким именем')
    elif influence_money(find_char_id(character_name), amount):
        embed = form_error_emmed(
            'Недостаточно средств для совершения операции')
    else:
        money_transaction(character_name, amount, target_name)
        embed = form_money_transfer_emmed(character_name, amount, target_name)

    await ctx.reply(embed=embed)


@bot.command()
async def health(ctx, character_name=str()):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Персонажа с таким именем не существует')
    else:
        health = health_condition_read(
            find_char_id(character_name))
        embed = form_health_condition_emmed(health)  # на переделке

    await ctx.reply(embed=embed)


@ bot.command()  # Готово
async def treat(ctx, target_name=str(), target_body_part=str(), amount=int()):

    if name_error(target_name):
        embed = form_error_emmed('Персонажа с таким именем не существует')
    elif negative_heal(amount):
        embed = form_error_emmed('Нельзя лечить на отрицательные значения')
    elif part_name_error(find_char_id(target_name), target_body_part):
        embed = form_error_emmed('Части тела с таким именем не существует')
    else:
        old_hp = part_hp_read(find_char_id(target_name), target_body_part)
        max_hp = max_hp_read(find_char_id(target_name), target_body_part)

        if old_hp+amount > max_hp:
            amount = max_hp-old_hp

        cause_damage(find_char_id(target_name), target_body_part, -amount)

        new_hp = part_hp_read(find_char_id(target_name), target_body_part)

        embed = form_health_changes_emmed(old_hp, new_hp, target_body_part)

    await ctx.reply(embed=embed)


@ bot.command()
async def man(ctx, command=str()):

    await ctx.reply('WIP')

##################################################################################


@ bot.command()  # Не удалять, поглаживания бота
async def pat(ctx):
    await ctx.reply('UwU')


@bot.command()  # Тестовая функция для нанесения урона, потом удалю
async def bite(ctx, character_name=str(), target_name=str(), target_body_part='торс'):
    if name_error(target_name):
        embed = form_error_emmed('Персонажа с таким именем не существует')
    elif part_name_error(find_char_id(target_name), target_body_part):
        embed = form_error_emmed('Части тела с таким именем не существует')
    else:
        old_hp = part_hp_read(find_char_id(target_name), target_body_part)

        amount = random.randint(1, 2)

        cause_damage(find_char_id(target_name), target_body_part, amount)

        new_hp = part_hp_read(find_char_id(target_name), target_body_part)

        embed = form_health_changes_emmed(old_hp, new_hp, target_body_part)

    await ctx.reply(embed=embed)


@bot.command()  # Тестовая функция для выведения картинки
async def pic(ctx):
    embed = discord.Embed(color=0xFFFFFF, title='аыыыыыыы')
    file = discord.File("images/1.jpg", filename="1.jpg")
    embed.set_image(url="attachment://1.jpg")
    await ctx.reply(file=file, embed=embed)

bot.run(config['token'])
