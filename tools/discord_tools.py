import discord

def form_health_condition_emmed(health):
    embed = discord.Embed(color = 0xFFFFFF, title = 'Анализ состояния:')
    embed.add_field(name= health[0], value=f'''
    Голова - {health[1]}
    Рука(Л) - {health[2]}
    Рука(П) - {health[3]}
    Торс - {health[4]}
    Нога(Л) - {health[5]}
    Нога(П) - {health[6]}
    ''')
    return embed

def form_health_changes_emmed(old_hp, new_hp, part):
    embed = discord.Embed(color = 0xFFFFFF, title = 'Изменение состояния:')
    embed.add_field(name=f'{part}:', value=f'{old_hp} -> {new_hp}')
    return embed

def form_roll_result_emmed(dice_value):

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

    embed = discord.Embed(color = emmed_color, title = 'Бросок кубика:')
    embed.add_field(name= emmed_name, value=f'Ваш результат: {dice_value}')
    return embed

def form_money_transfer_emmed(character, amount, target):
    embed = discord.Embed(color = 0xFFFFFF, title = 'Денежная транзакция:')
    embed.add_field(name = 'Статус - подтверждена', value = f'{target} получает {amount} анх от персонажа {character} ')
    return embed

def form_error_emmed(message):
    embed = discord.Embed(color = 0xD22A00, title = 'Возникла ошибка!')
    embed.add_field(name = 'Операция не выполнена по причине:', value = f'{message}')
    return embed
