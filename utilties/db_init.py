import sqlite3

create_characters_table = """
CREATE TABLE IF NOT EXISTS characters (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  user_id TEXT NOT NULL
);
"""
create_stats_table = """
CREATE TABLE IF NOT EXISTS stats (
  char_id INTEGER PRIMARY KEY, 
  fortitude INTEGER NOT NULL,
  prudence INTEGER NOT NULL,
  temperance INTEGER NOT NULL,
  justice INTEGER NOT NULL,
  FOREIGN KEY (char_id) REFERENCES characters (id)
);"""

create_health_table = """
CREATE TABLE IF NOT EXISTS health (
  char_id INTEGER NOT NULL, 
  type TEXT NOT NULL,
  hp INTEGER NOT NULL,
  max_hp INTEGER NOT NULL, 
  description TEXT,       
  FOREIGN KEY (char_id) REFERENCES characters (id)
);"""

create_inventory_table = """
CREATE TABLE IF NOT EXISTS inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  char_id INTEGER NOT NULL, 
  type TEXT NOT NULL,
  amount INTEGER NOT NULL,
  name INTEGER NOT NULL, 
  description TEXT,       
  FOREIGN KEY (char_id) REFERENCES characters (id)
);"""

create_etc_table = """
CREATE TABLE IF NOT EXISTS etcetera (
  char_id INTEGER PRIMARY KEY,
  skills TEXT NOT NULL, 
  job TEXT NOT NULL,
  ideology TEXT NOT NULL,
  biography TEXT NOT NULL,
  traits TEXT NOT NULL,
  weaknesses TEXT NOT NULL,
  FOREIGN KEY (char_id) REFERENCES characters (id)
);"""

create_characters = """
INSERT INTO
  characters (name, type, user_id)
VALUES
    ('Маргарита', 'злодей - британец', '354177140087980042'),
    ('Константин', 'самый сексуальный мужик в мире','946181563266244648'),
    ('Рейсу', 'пубертатная язва', '392698208985284611');
"""

create_stats = """
INSERT INTO
  stats (char_id, prudence,  fortitude, temperance, justice)
VALUES
    ('1','15', '17', '16', '12'),
    ('2', '20', '20', '20', '20'),
    ('3', '14', '14', '15', '15'),
    ('4', '10', '15', '17', '12');
"""
create_health = """
INSERT INTO
  health (char_id, type, hp, max_hp)
VALUES
    ('1','голова', 10, 10),
    ('1','торс', 10, 10),
    ('1','рука(л)', 10, 10),
    ('1','рука(п)', 10, 10),
    ('1','нога(л)', 10, 10),
    ('1','нога(п)', 10, 10),
    ('1','sp', 10, 10),
    ('2','голова', 9999, 9999),
    ('2','торс', 9999, 9999),
    ('2','рука(л)', 9999, 9999),
    ('2','рука(п)', 9999, 9999),
    ('2','нога(л)', 9999, 9999),
    ('2','нога(п)', 9999, 9999),
    ('2','sp', 500, 500),
    ('3','голова', 10, 10),
    ('3','торс', 10, 10),
    ('3','рука(л)', 10, 10),
    ('3','рука(п)', 10, 10),
    ('3','нога(л)', 10, 10),
    ('3','нога(п)', 10, 10),
    ('3','sp', 10, 10),
    ('4','голова', 10, 10),
    ('4','торс', 10, 10),
    ('4','рука(л)', 10, 10),
    ('4','рука(п)', 10, 10),
    ('4','нога(л)', 10, 10),
    ('4','нога(п)', 10, 10),
    ('4','sp', 10, 10);
"""


connection = sqlite3.connect('./roleplay.db')
cursor = connection.cursor()

for i in [create_characters_table, create_stats_table, create_health_table, create_etc_table, create_inventory_table]:
    cursor.execute(i)
    connection.commit()

for i in [create_characters, create_stats, create_health]:
    cursor.execute(i)
    connection.commit()

# cursor.execute(create_characters)
# cursor.execute(create_stats)
# cursor.execute(create_health)
