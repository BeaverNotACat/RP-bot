from modules.detached_utils.db_low_lvl_commands import db_connect, execute_query, execute_read_query


class InfluenceMoney:  # я не знаю где я оставил его с прошлых версий кода. но сейчас без него код не работает... пиздец
    pass


def ownership_error(character_name, user):
    print(f"Cheking {user}'s ownership:")

    connection = db_connect('roleplay.db')
    form = f'SELECT id FROM characters WHERE name = "{character_name}" AND user_id = "{user}";'

    try:
        execute_read_query(connection, form)[0][0]
        connection.close()
        return False
    except:
        connection.close()
        return True


def stat_error(stat):
    print("Cheking stat's name:")
    if stat == 'мужество' or stat == 'мудрость' or stat == 'выдержка' or stat == 'справедливость':
        return False
    else:
        return True


def name_error(character_name):
    print("Cheking characters's name:")

    connection = db_connect('roleplay.db')
    form = f'SELECT id FROM characters WHERE name = "{character_name}";'

    try:
        execute_read_query(connection, form)[0][0]
        connection.close()
        return False
    except:
        connection.close()
        return True


def influence_money(character_id, value):
    print("Cheking character's wallet:")

    connection = db_connect('roleplay.db')
    character_wallet_form = f'SELECT wallet FROM characters WHERE id = "{character_id}";'

    if execute_read_query(connection, character_wallet_form)[0][0] - value < 0:
        connection.close()
        return True
    else:
        connection.close()
        return False


def negative_heal(value):
    if value < 0:
        return True
    else:
        return False


def part_name_error(character_id, part_name):
    print("Cheking body part's name:")

    connection = db_connect('roleplay.db')
    form = f'SELECT id FROM health WHERE char_id = {character_id} AND type = "{part_name}";'

    try:
        execute_read_query(connection, form)[0][0]
        connection.close()
        return False
    except:
        connection.close()
        return True


def influence_wepon(character_id, weapon_name):
    print("Cheking body part's name:")

    connection = db_connect('roleplay.db')
    form = f'SELECT id FROM inventory WHERE char_id = {character_id} AND type = "weapon" AND name = "{weapon_name}";'

    try:
        execute_read_query(connection, form)[0][0]
        connection.close()
        return False
    except:
        connection.close()
        return True
