from db import db_connect, execute_query

create_characters_table = """
CREATE TABLE IF NOT EXISTS characters (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT NOT NULL, 
  user_id TEXT NOT NULL, 
  level INTEGER NOT NULL,
  wallet INTEGER NOT NULL
);
"""
create_stats_table = """
CREATE TABLE IF NOT EXISTS stats (
    char_id INTEGER PRIMARY KEY, 
    мужество INTEGER NOT NULL,
    мудрость INTEGER NOT NULL,
    выдержка INTEGER NOT NULL,
    справделивость INTEGER NOT NULL,
    FOREIGN KEY (char_id) REFERENCES character (id)
);"""

create_health_table = """
CREATE TABLE IF NOT EXISTS health (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    char_id INTEGER NOT NULL, 
    type TEXT NOT NULL,
    hp INTEGER NOT NULL,
    max_hp INTEGER NOT NULL, 
    description TEXT NOT NULL,       
    FOREIGN KEY (char_id) REFERENCES character (id)
);"""

create_etc_table = """
CREATE TABLE IF NOT EXISTS etcetera (
    char_id INTEGER PRIMARY KEY,
    skills TEXT NOT NULL, 
    job TEXT NOT NULL,
    ideology TEXT NOT NULL,
    biografy TEXT NOT NULL,
    traits TEXT NOT NULL,
    weaknesses TEXT NOT NULL,
    low_sp_actions TEXT NOT NULL,
    contacts TEXT NOT NULL,
    FOREIGN KEY (char_id) REFERENCES character (id)
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
    ('2','голова', 10, 10, 'none'),
    ('2','торс', 10, 10, 'none'),
    ('2','рука(л)', 10, 10, 'none'),
    ('2','рука(п)', 10, 10, 'none'),
    ('2','нога(л)', 10, 10, 'none'),
    ('2','нога(п)', 10, 10, 'none'),
    ('2','sp', 10, 10, 'none'),
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
create_augmentations = """ 
INSERT INTO
  augmentations (id, голова, рука_л, рука_п, торс, нога_л, нога_п)
VALUES
    ('Маргарита','Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет'),
    ('Рейсу', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет');
"""


connection = db_connect('database/roleplay.db')
execute_query(connection,  create_characters_table)
execute_query(connection,  create_stats_table)
execute_query(connection,  create_health_table)
execute_query(connection,  create_etc_table)

execute_query(connection,  create_characters)
execute_query(connection,  create_stats)
execute_query(connection,  create_health)
