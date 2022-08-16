import sqlite3


class DatabaseInterface:
    def __init__(self, path_to_database: str):
        self.__connection = sqlite3.connect(path_to_database)
        self.__cursor = self.__connection.cursor()

    def __execute(self, query):
        self.__cursor.execute(query)
        self.__connection.commit()
        return self.__cursor

    def __read(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def find_char_id(self, character_name: str) -> int:
        return self.__read(f'SELECT id FROM characters WHERE name = "{character_name}";')

    def read_stat(self, stat: str, character_id: int) -> int:
        return self.__read(f'SELECT {stat} FROM stats WHERE char_id = "{character_id}";')

    def read_part_hp(self,  body_part: str, character_id: int) -> int:
        return self.__read(f'SELECT hp FROM health WHERE char_id = {character_id} AND type = "{body_part}";')

    def read_part_max_hp(self, body_part: str, character_id: int) -> int:
        return self.__read(f'SELECT max_hp FROM health WHERE char_id = {character_id} AND type = "{body_part}";')

    def cause_damage(self,  body_part: str, damage: int, target_character_id: int) -> None:
        return self.__execute(f'UPDATE health SET hp = {self.read_part_hp(character_id=target_character_id,body_part=body_part)[0][0]-damage} WHERE char_id = {target_character_id} AND type = "{body_part}";')

    def read_money_amount(self, character_id) -> int:
        return self.__read(f'SELECT amount FROM inventory WHERE name = "ankh" AND char_id = "{character_id}";')

    def spend_money(self, amount: int, character_id: int) -> None:
        return self.__execute(f'UPDATE inventory SET amount = "{self.read_money_amount(character_id)[0][0]-amount}" WHERE name = "ankh" AND char_id = "{character_id}";')

    def __del__(self):
        self.__connection.close()


# db = DatabaseInterface('./roleplay.db')
# print(db.read_part_hp('head', 1))
# print(db.read_part_max_hp('head', 1))
