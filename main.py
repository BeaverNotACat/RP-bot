import discord
from discord.ext import commands

import random

from settings import config

from tools.imgs_tools import make_health_condition_pic, simple_def
# Самописные функции для работы с бд
from tools.db_tools import stat_read, cause_damage, money_transaction, health_condition_read, part_hp_read, create_aliases, find_char_id
# Заготовки под вывод сообщений
from tools.discord_tools import form_health_condition_emmed, form_health_changes_emmed, form_roll_result_emmed, form_money_transfer_emmed, form_error_emmed
from tools.erors import ownership_error, influence_money, stat_error

bot = commands.Bot(command_prefix=config['prefix'])
print(health_condition_read(1))
#################################################################################


@bot.command()
async def dice(ctx, stat=str(), character_name=str(), mod=0):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Вы не владете персонажем с таким именем')
    elif stat_error(stat):
        embed = form_error_emmed(
            'Неправильно указано название характеристики персонажа')
    else:
        character_id = find_char_id(character_name, ctx.author.id)
        stat_value = stat_read(stat, character_id)
        roll_value = random.randint(0, 20) + (stat_value-10)//2 + mod
        embed = form_roll_result_emmed(roll_value)

    await ctx.reply(embed=embed)


@bot.command()
async def transfer(ctx, character_name=str(), amount=int(), target_name=str()):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Вы не владете персонажем с таким именем')
    elif influence_money(find_char_id(character_name, ctx.author.id), amount):
        embed = form_error_emmed(
            'Недостаточно средств для совершения операции')
    else:
        money_transaction(character_name, amount, target_name)
        embed = form_money_transfer_emmed(character_name, amount, target_name)

    await ctx.reply(embed=embed)


@bot.command()
async def health(ctx, character_name=str()):

    if ownership_error(character_name, ctx.author.id):
        embed = form_error_emmed('Вы не владете персонажем с таким именем')
    else:
        health = health_condition_read(
            find_char_id(character_name, ctx.author.id))
        embed = form_health_condition_emmed(health)

    await ctx.reply(embed=embed)

# @bot.command()
# async def treat(ctx, target='', part='', amount=0):

#     if name_error(target, part, 'health'):
#         embed = form_error_emmed('Неправильно введено имя персонажа/часть тела')
#     else:
#         old_hp = part_hp_read(target, part)
#         cause_damage(target, part, -amount)
#         new_hp = part_hp_read(target, part)

#         embed = form_health_changes_emmed(old_hp, new_hp, part)

#     await ctx.reply(embed = embed)

##################################################################################


@bot.command()  # Не удалять
async def pat(ctx):
    await ctx.reply('UwU' + simple_def())

# @bot.command()   #Тестовая функция для нанесения урона, потом удалю
# async def bite(ctx, character='', target='', part='торс'):
#     old_hp = part_hp_read(target, part)

#     if old_hp == -1:
#         embed = form_error_emmed('Неправильно введено имя персонажа/часть тела')
#     else:
#         damage = random.randint(0,2)
#         cause_damage(target, part, damage)
#         new_hp = part_hp_read(target, part)

#         embed = form_health_changes_emmed(old_hp, new_hp, part)
#     await ctx.reply(embed=embed)

# @bot.command()   #Тестовая функция для нанесения урона, потом удалю
# async def pic(ctx):
#     embed = discord.Embed(color = 0xFFFFFF, title = 'аыыыыыыы')
#     file = discord.File("images/1.jpg", filename="1.jpg")
#     embed.set_image(url="attachment://1.jpg")
#     await ctx.reply(file=file, embed=embed)

bot.run(config['token'])
