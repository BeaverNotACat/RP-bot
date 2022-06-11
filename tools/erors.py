from database.db import db_connect, execute_query, execute_read_query

class InfluenceMoney(Exception):
    pass

# Проверка правильности параметров. Вынес отдельно, чтобы не засорять код
######################################################################
def ownership_error(character_name, user):
    print(f"Cheking user's ownership:")

    connection = db_connect('database/roleplay.db')
    form = f'SELECT id FROM characters WHERE name = "{character_name}" AND user_id = "{user}";'

    try:
        execute_read_query(connection, form)[0][0]
        connection.close()
        return False
    except:
        connection.close()
        return True

def stat_error(stat):
    if stat == 'мужество' or 'мудрость' or 'выдержка' or 'справедливость':
        return False
    else: 
        return True 

def influence_money(character_id, value):

    connection = db_connect('database/roleplay.db')
    character_wallet_form = f'SELECT wallet FROM characters WHERE id = "{character_id}";'
    
    if execute_read_query(connection, character_wallet_form)[0][0] - value < 0:
        connection.close()
        return True
    else:
        connection.close()
        return False