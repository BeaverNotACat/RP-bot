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
  character_id INTEGER PRIMARY KEY, 
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
  characters (name,  user_id, level, wallet)
VALUES
    ('Маргарита', '354177140087980042', 1, 100),
    ('Константин','946181563266244648', 1, 100),
    ('Рейсу', '392698208985284611', 1, 100),
    ('Лиза', '695457412097769472', 1, 100);
"""

create_stats = """
INSERT INTO
  stats (char_id, мужество,  мудрость, выдержка, справделивость)
VALUES
    ('1','15', '17', '16', '12'),
    ('2', '20', '20', '20', '20'),
    ('3', '14', '14', '15', '15'),
    ('4', '10', '15', '17', '12');
"""
create_health = """
INSERT INTO
  health (char_id, type, hp, max_hp, description)
VALUES
    ('1','голова', 10, 10, 'none'),
    ('1','торс', 10, 10, 'none'),
    ('1','рука(л)', 10, 10, 'none'),
    ('1','рука(п)', 10, 10, 'none'),
    ('1','нога(л)', 10, 10, 'none'),
    ('1','нога(п)', 10, 10, 'none'),
    ('1','sp', 10, 10, 'none'),
    ('2','голова', 9999, 9999, 'none'),
    ('2','торс', 9999, 9999, 'none'),
    ('2','рука(л)', 9999, 9999, 'none'),
    ('2','рука(п)', 9999, 9999, 'none'),
    ('2','нога(л)', 9999, 9999, 'none'),
    ('2','нога(п)', 9999, 9999, 'none'),
    ('2','sp', 500, 500, 'none'),
    ('3','голова', 10, 10, 'none'),
    ('3','торс', 10, 10, 'none'),
    ('3','рука(л)', 10, 10, 'none'),
    ('3','рука(п)', 10, 10, 'none'),
    ('3','нога(л)', 10, 10, 'none'),
    ('3','нога(п)', 10, 10, 'none'),
    ('3','sp', 10, 10, 'none'),
    ('4','голова', 10, 10, 'none'),
    ('4','торс', 10, 10, 'none'),
    ('4','рука(л)', 10, 10, 'none'),
    ('4','рука(п)', 10, 10, 'none'),
    ('4','нога(л)', 10, 10, 'none'),
    ('4','нога(п)', 10, 10, 'none'),
    ('4','sp', 10, 10, 'none');
"""


connection = sqlite3.connect('./roleplay.db')
cursor = connection.cursor()
cursor.execute(create_characters_table)


cursor.execute(create_stats_table)
cursor.execute(create_health_table)
cursor.execute(create_etc_table)
cursor.execute(create_inventory_table)

# cursor.execute(create_characters)
# cursor.execute(create_stats)
# cursor.execute(create_health)
connection.commit()
