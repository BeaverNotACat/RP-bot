import sqlite3


class DatabaseInterface:
    def __init__(self):
        self.__connection = sqlite3.connect('roleplay.db')
        self.__cursor = self.__connection.cursor()

    def __execute(self, query):
        self.__cursor.execute(query)
        self.__connection.commit()
        return self.__cursor

    def find_char_id(self, character_name: str):
        return self.__execute(f'SELECT id FROM characters WHERE name = "{character_name}";')

    def read_stat(self, stat: str, character_id: int):
        return self.__execute(f'SELECT {stat} FROM stats WHERE char_id = "{character_id}";')

    def read_part_hp(self,  body_part: str, character_id: int):
        return self.__execute(f'SELECT hp FROM health WHERE char_id = {character_id} AND type = "{body_part}";')

    def read_part_max_hp(self, body_part: str, character_id: int):
        return self.__execute(f'SELECT max_hp FROM health WHERE char_id = {character_id} AND type = "{body_part}";')

    def cause_damage(self,  body_part: str, damage: int, target_character_id: int):
        return self.__execute(f'UPDATE health SET hp = {self.read_part_hp(target_character_id, body_part)-damage} WHERE char_id = {target_character_id} AND type = "{body_part}";')

    def read_money_amount(self, character id):
        return self.__execute()

    def spend_money(self, amount: int, character_id: int):
        return self.__execute()

    def __del__(self):
        self.__connection.close()
