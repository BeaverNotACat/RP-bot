from database.db import db_connect, execute_query, execute_read_query
from tools.erors import InfluenceMoney


# Функции что то возвращающие
######################################################################
def find_char_id(character_name):
    print(f"Finding {character_name} id")

    connection = db_connect('database/roleplay.db')

    form = f'SELECT id FROM characters WHERE name = "{character_name}";'
    character_id = execute_read_query(connection, form)[0][0]
    connection.close()

    return character_id


def stat_read(stat, character_id):
    print(f'Reading stat of {stat} with id {character_id}:')

    connection = db_connect('database/roleplay.db')

    stat_read_form = f'SELECT {stat} FROM stats WHERE char_id = "{character_id}";'

    stat = execute_read_query(connection, stat_read_form)[0][0]
    connection.close()
    return stat


def health_condition_read(character_id):
    print(f'Reading all health with id {character_id}:')

    connection = db_connect('database/roleplay.db')
    hp = []

    for type in ['голова', 'торс', 'рука(л)', 'рука(п)', 'нога(л)', 'нога(п)']:
        hp_form = f'SELECT hp FROM health WHERE char_id = {character_id} AND type = "{type}";'
        max_hp_form = f'SELECT max_hp FROM health WHERE char_id = {character_id} AND type = "{type}";'
        hp.append([execute_read_query(connection, hp_form)[0][0],
                  execute_read_query(connection, max_hp_form)[0][0]])

    connection.close()
    return hp


def part_hp_read(character_id, body_part):
    print(f'Reading hp of {body_part} with charracter id {character_id}:')

    connection = db_connect('database/roleplay.db')

    hp_form = f'SELECT hp FROM health WHERE char_id = "{character_id}" AND type = "{body_part}";'

    hp = execute_read_query(connection, hp_form)[0][0]
    connection.close()
    return hp

# Остальные
######################################################################


def cause_damage(target_character_id, body_part, damage):
    print(
        f'Causing damage of {damage} to the {body_part} with character id {target_character_id}:')

    connection = db_connect('database/roleplay.db')

    part_select_form = f'SELECT hp FROM health WHERE char_id = "{target_character_id}" AND type = "{body_part}";'

    new_hp = execute_read_query(connection, part_select_form)[0][0] - damage
    cause_damage_form = f'UPDATE health SET hp = {new_hp} FROM health WHERE char_id = "{target_character_id} AND type = {body_part}";'
    execute_query(connection,  cause_damage_form)

    connection.close()
    return


def money_transaction(character, amount, target):
    print(f'Transfering {amount} from {character} to {target}:')

    connection = db_connect('database/roleplay.db')

    character_wallet_form = f'SELECT wallet FROM characters WHERE name = "{character}";'
    target_wallet_form = f'SELECT wallet FROM characters WHERE name = "{target}";'

    character_wallet = execute_read_query(
        connection, character_wallet_form)[0][0] - amount
    target_wallet = execute_read_query(
        connection, target_wallet_form)[0][0] + amount

    character_transact_money_form = f'UPDATE characters SET wallet = {character_wallet} WHERE name = "{character}"'
    execute_query(connection,  character_transact_money_form)
    target_transact_money_form = f'UPDATE characters SET wallet = {target_wallet} WHERE name = "{target}"'
    execute_query(connection,  target_transact_money_form)

    connection.close()
    return


def create_aliases():
    print('Creating aliaces:')
    connection = db_connect('database/roleplay.db')

    fortitude_alias = 'SELECT fortitude AS мужество FROM stats;'
    execute_query(connection,  fortitude_alias)

    prudence_alias = 'SELECT prudence AS мудрость FROM stats;'
    execute_query(connection,  prudence_alias)

    temperance_alias = 'SELECT temperance AS выжержка FROM stats;'
    execute_query(connection,  prudence_alias)

    justice_alias = 'SELECT justice AS справделивость FROM stats;'
    execute_query(connection,  prudence_alias)

    connection.close()
    return
